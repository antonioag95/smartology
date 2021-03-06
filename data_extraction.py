# -*- coding: utf-8 -*-
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed, EndPointNotFound, EndPointInternalError
from collections import defaultdict
from urllib import request, error
import time


class Data_Extraction:

  def __init__(self,query,limit,offset,stop):

    self.query = query #The submitted query must have LIMIT inside
    self.LIMIT = n_limit #Numeric value associated with LIMIT
    self.OFFSET = n_offset #Numeric value associated with OFFSET
    self.STOP = n_stop #to have no limits in pagination: []

  def query_sparql(query, url_endpoint):
    '''
    The function allows the extraction of data from a sparql endpoint via SPARQL 
    queries.
    '''
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
    #answert_dict: {'variable_name:[data from ontology]'}
    return answer_dict


  def pagination(query, n_limit, n_offset, n_stop, select_variable):
    '''
    The function modifies the query to allow paging and total rendering of the 
    data from the sparql endpoint.
    - Select_variabile: name of a reference variable called in the SELECT query
    '''
    offset_count = 0
    len_ = 1
    results = defaultdict(list)

    while (len_ != 0):
          complete_query=query.replace(query.split()[query.split().index('LIMIT')+1],str(n_limit))
          complete_query=complete_query.split()
          complete_query= complete_query[:complete_query.index("LIMIT")+2] + ["OFFSET " + str(offset_count)] + complete_query[complete_query.index("LIMIT")+2:]
          complete_query=' '.join(complete_query)

          res_query = Data_Extraction.query_sparql(complete_query, _url_endpoint)
          
          len_ = len(res_query[select_variable])
          print(offset_count) #Check
          if offset_count == n_stop: break
          for k, v in res_query.items():
              results[k] += v

          offset_count += n_offset

    results = {k: [ele.strip() for ele in v] for k, v in results.items()} 

    return results



#Application of code
_url_endpoint = "https://dati.beniculturali.it/sparql" 

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

    { SELECT DISTINCT ?culturalProperty 
      WHERE {
             ?culturalProperty foaf:depiction ?depiction.
             } GROUP BY ?culturalProperty HAVING COUNT(?depiction)=1
     }
   FILTER (?DefinitionLabel = 'dipinto')
} GROUP BY ?culturalProperty LIMIT 100
"""

if __name__ == "__main__":
  results = Data_Extraction.pagination(query,5,5,10,'culturalProperty')

  #To view the results
  displacy= ' '.join(f"{results['titleLabel'][pos]} \t {results['authorLabel'][pos]} \t {results['culturalProperty'][pos]}\n" 
                   for pos in range (len(results['culturalProperty'])))
  print(displacy)
