# -*- coding: utf-8 -*-


import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed, EndPointNotFound, EndPointInternalError
from collections import defaultdict
from urllib import request, error
import time

import transformers
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import AutoModelForSeq2SeqLM
from transformers import pipeline
import spacy

import requests, json, re
from bs4 import BeautifulSoup as bs

from data_extraction import Data_Extraction
from Bert_Text_Processing import Information_Retrieval
from smartology import findInfo, ontoSearch, desiredLanguage, wikiOntology, wikiSectionContent, wikiSections, querySparql, encodeWikipediaName


##Estrazione:
modello_QAandSum="deepset/bert-large-uncased-whole-word-masking-squad2"
modello_ITATranslation = "Helsinki-NLP/opus-mt-en-it"
modello_ENTranslation = "Helsinki-NLP/opus-mt-it-en"

sparql = SPARQLWrapper("http://query.wikidata.org/sparql")

_url_endpoint = "https://dati.beniculturali.it/sparql"


#The query to be submitted to the extraction program can be formulated freely. 
#However, for the process to run smoothly, information about the title and author of the work must be extracted. 
#If more accuracy is desired, it is also possible to extract the description associated with the cultural property.

query= """
PREFIX arco: <https://w3id.org/arco/ontology/arco/> 
PREFIX arco-dd: <https://w3id.org/arco/ontology/denotative-description/>
PREFIX arco-cd: <https://w3id.org/arco/ontology/context-description/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT DISTINCT  ?titleLabel ?authorLabel ?description ?HistoricalInfo ?culturalProperty
WHERE {
  ?culturalProperty foaf:depiction ?depiction .
  ?culturalProperty arco-cd:historicalInformation ?HistoricalInfo .
  ?culturalProperty dc:description ?description .
  ?culturalProperty rdfs:label ?titleLabel .
  ?culturalProperty arco-cd:hasAuthor ?author .
  ?author rdfs:label ?authorLabel .

?culturalProperty arco:uniqueIdentifier ?id .
  

FILTER (?authorLabel = "Michelangelo Buonarroti")
FILTER (?id = "0900287181" || ?id = "0900281988")
}  LIMIT 100
"""

def hasLiteral (keyword):
  '''
  Given a free text, this function is capable of extracting information based on a certain keyword. 
  Once the period containing the chosen term has been extrapolated, the sentences are processed through a synthesis 
  process during which a grammatical correction is applied to make the answer semantically and syntactically correct.
  '''
  matching = [sent for sent in context.split('.') if keyword in sent.lower()]
  if len(matching) >0:
    sum = [Information_Retrieval.summarize_Bert("modello_QAandSum",sent,0,300) 
    if len(sent) >100 else sent for sent in matching]  
    hasProperty = '\n'.join(sent for sent in sum if keyword in sent.lower())
    hasProperty = Information_Retrieval.summarize_Bert("modello_QAandSum",hasProperty,30,130) 
 
    return '. '.join(sent for sent in hasProperty.split('.') if keyword in sent.lower())

#graph to implement:
g = rdflib.Graph()
g.parse("smartology.owl", format="xml")

if __name__ == "__main__":
  
  results = Data_Extraction.pagination(query,5,5,10,'culturalProperty')
  results = pd.DataFrame(results,columns=['titleLabel', 'authorLabel', 'description', 'HistoricalInfo', 'culturalProperty'])
  results = results.drop_duplicates(subset="culturalProperty")
  
  ontology_implementation = []

  #for every cultural asset
  for index, row in results.iterrows():
    print(f"Il titolo dell'opera è: {row['titleLabel']}")
    print(f"L'autore dell'opera è: {row['authorLabel']}\n")
    
    #Properties extracted by scraping: hasCulturalMovement, hasWikiDescription, hasSubject.
    keyword = row['titleLabel'] if len(row['titleLabel'].split()) < 5 else ' '.join(row['titleLabel'].split()[:2])
    keyword = keyword + row['authorLabel'].split()[0] ## da valutare.
    print(keyword)
    
    info = findInfo(keyword)
    if (info["gotResult"]):
      title = info["title"]
      lang = info["lang"]
      pageID = info["pageID"]
      print("Got result from Wikipedia Search:\n\nTitle: {}\nLanguage: {}\nPage ID: {}".format(title, lang, pageID))
      print("\nLooking for ontology ID...\n")
      ontoID = ontoSearch(info["title"])
      if (ontoID):
        print("Ontology ID: {}\n".format(ontoID))
        ontologyContent = wikiOntology(ontoID)
        prefLang = desiredLanguage(ontologyContent)
        print(prefLang)
        sections = wikiSections(encodeWikipediaName(prefLang["title"]), prefLang["language"])
        print(sections)
        content = wikiSectionContent(encodeWikipediaName(prefLang["title"]), sections[0], sections[1], prefLang["language"])
        print(content)
        movement = querySparql(ontoID, "P135")
        if (len(movement) > 0):
          print("\n'{}' belongs to '{}' movement.\n".format(title, movement[0]))
        depicts = querySparql(ontoID, "P180")
        if (len(depicts) > 0):
          print("Depicts: {}\n".format(", ".join(depicts)))
      else:
        print("Ontology ID could not be found")
    else:
      print("No Wikipedia entry found")

    #DataProperties extracted through machine learning models: 
    context = Information_Retrieval.translationEN_Bert(modello_ENTranslation,row['description']+row['HistoricalInfo'])
    context = prefLang["title"] + context + ' '.join(content)

    #DataProperties extracted through Question-Aswering
    questions = {'hasEnvironment':'what is the scene?', 'hasMessage':'what is the painting about?'} # da valutare.
    QAResults={k:Information_Retrieval.QA_Bert(modello_QAandSum,context,question) for k,question in questions.items()}
    
    #DataProperties extracted through Textual Analysis
    subject_en = [Information_Retrieval.translationEN_Bert(modello_ENTranslation,element) for element in depicts]
    hasDescriptionRelations = [[element, hasLiteral(element.lower())] for element in subject_en if element[0].isupper()]
    hasDescriptionRelations = '\n'.join([f"Relation about {element[0]}: \n {element[1]}" for element in hasDescriptionRelations if element[1] != None ]) 

    DataProperties = {'resource':row['culturalProperty'],
                       'hasSource':'Wikipedia',
                       'hasSubject':", ".join([element for element in depicts if element[0].isupper()]),
                       'hasWikiDescription':' '.join(content),
                       'hasCulturalMovement':' '.join(movement),
                       'hasPerspectiveStudy':hasLiteral('perspective'),
                       'hasBackgroundElement':hasLiteral('background'),
                       'hasForegroundElement':hasLiteral('foreground'),
                       'hasLights':hasLiteral('light'),
                       'hasColour':hasLiteral('colour'),
                       'hasTopic':hasLiteral('theme'),
                       'hasDescriptionRelations': hasDescriptionRelations,
                       'hasDescriptionScene':hasLiteral('scene')
                       }
    DataProperties.update(QAResults)
    
    results = {k:v for k,v in DataProperties.items() if v != None }

    for k,v in DataProperties.items():
        print(f'{k}: \n{v}\n\n')
        
    ontology_implementation += [DataProperties]
     
    #Check:
    print(ontology_implementation)
    #ontology implementation
    main(False,ontology_implementation)



