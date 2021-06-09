# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xlgo_3Elw5S6LOWs1DHHXWbV2Axd7AbM
"""

import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed, EndPointNotFound, EndPointInternalError
from collections import defaultdict
from urllib import request, error
import time

_url_endpoint = "https://dati.beniculturali.it/sparql" 

LIMIT = 30
OFFSET = 30
STOP = 30 #to have no limits: []

def query_sparql(query, url_endpoint):
    sparql = SPARQLWrapper(url_endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    try:
        results = sparql.query().convert()
    except ConnectionResetError as exc:
          print('Connection Error', str(exc))
          time.sleep(60)
          results = sparql.query().convert()
    except (error.HTTPError, EndPointInternalError):
          print("Error 500")
          time.sleep(60)
          try:
              results=sparql.query().convert()
          except (error.HTTPError, EndPointInternalError):
              print("Error 500")

    answer = results['results']['bindings']
    answer_dict = defaultdict(list)      
    for data in answer:
          for key, values in data.items():
              answer_dict[key].append(values['value'])
          #For null results:
          if len([k for k in answer_dict.keys()]) != len([k for k in answer_dict.keys()]):
              for k in answer_dict.keys():
                  if k not in data.keys():
                      answer_dict[k] += [""]
                  else:
                      pass                          
      
    return answer_dict


def pagination(query, n_limit, n_offset):
      i = 0
      len_ = 1
      results = defaultdict(list)

      while (len_ != 0):
          complete_query=query.replace(query.split()[query.split().index('LIMIT')+1],str(n_limit))
          complete_query=complete_query.split()
          complete_query= complete_query[:complete_query.index("LIMIT")+2] + ["OFFSET " + str(i)] + complete_query[complete_query.index("LIMIT")+2:]
          complete_query=' '.join(complete_query)

          res_query = data_extraction.query_sparql(complete_query, _url_endpoint)
          if res_query == "None":
              break  #If the query returns no results

          len_ = len(res_query['culturalProperty'])
          print(i)
          if i == STOP: break
          for k, v in res_query.items():
              results[k] += v

          i += n_offset

      results = {k: [ele.strip() for ele in v] for k, v in results.items()} 

      return results


query= """
PREFIX arco: <https://w3id.org/arco/ontology/arco/> 
PREFIX arco-dd: <https://w3id.org/arco/ontology/denotative-description/>
PREFIX arco-cd: <https://w3id.org/arco/ontology/context-description/>

SELECT DISTINCT  ?culturalProperty (SAMPLE(?titleLabel) AS ?titleLabel) (SAMPLE(?authorLabel) AS ?authorLabel)
WHERE {
  ?culturalProperty foaf:depiction ?depiction .
  ?culturalProperty arco-dd:hasCulturalPropertyType ?culturalPropertyType .
  ?culturalPropertyType arco-dd:hasCulturalPropertyDefinition ?culturalPropertyDefinition .
  ?culturalPropertyDefinition rdfs:label ?DefinitionLabel .
  ?culturalProperty arco-cd:hasTitle ?title .
  ?title rdfs:label ?titleLabel .
  ?culturalProperty a-cd:hasAuthor ?author .
  ?author rdfs:label ?authorLabel .

  {SELECT DISTINCT ?culturalProperty WHERE {
  ?culturalProperty foaf:depiction ?depiction.
  } GROUP BY ?culturalProperty HAVING COUNT(?depiction)=1}

  FILTER (?DefinitionLabel = 'dipinto')
 } GROUP BY ?culturalProperty LIMIT 100

"""

results = pagination(query,LIMIT,OFFSET)

#To view the results
displacy= ' '.join(f"{results['titleLabel'][pos]} \t {results['authorLabel'][pos]} \t {results['culturalProperty'][pos]}\n" 
                   for pos in range (len(results['culturalProperty'])))
print(displacy)