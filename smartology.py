import requests, json, re
from bs4 import BeautifulSoup as bs
from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("http://query.wikidata.org/sparql")

def wikiSearch(url):
	response = requests.get(url)
	toBeRuturned = {"gotResult": False, "title": "", "pageID": 0}
	# Check connection status code
	if (response.status_code == 200):
		content = response.json()
		# Let's check if query returned at least a result
		hits = content["query"]["searchinfo"]["totalhits"]
		if (hits > 1):
			# Got a result, return some useful info needed to find the actual Wikipedia page
			toBeRuturned["gotResult"] = True
			toBeRuturned["title"] = content["query"]["search"][0]["title"]
			toBeRuturned["pageID"] = content["query"]["search"][0]["pageid"]
		else:
			print("No data returned for query")
	else:
		print("Error while calling Wikipedia API")
	return toBeRuturned

def encodeSearchWord(searchString):
	'''
	All queries need to be transformed following the HTML syntax
	'''
	return searchString.replace(" ", "%20").lower()

def wikiOntology(curID, language="en"):
	'''
	Wikipedia offers an ontology where we can get data from, unfortunately this info is only 
	provided in the HTML source code, so we need to parse it.
	'''
	response = requests.get("https://{}.wikipedia.org/?curid={}".format(language, curID))
	if (response.status_code == 200):
		content = response.text
		soup = bs(content, features="lxml")
		ontologyInfo = soup.find("script", {"type": "application/ld+json"}).string
		ontologyJSON = json.loads(ontologyInfo)
		return ontologyJSON["mainEntity"].split("/")[-1]
	return None

def wikiSections(curID, language="en"):
	'''
	We need to understand how a Wikipedia page is made, we need to understand if we have a 'Description' field, then retrieve index numbers we need.
	This includes a little dirty hack to retrieve subsection of 'Description' as there is no way to straightly retrieve them 
	'''
	response = requests.get("https://{}.wikipedia.org/w/api.php?action=parse&format=json&pageid={}&prop=sections&disabletoc=1".format(language, curID))
	needed = []
	if (response.status_code == 200):
		content = response.json()["parse"]
		isSectionFound = False
		numberMacroSection = None
		for section in content["sections"]:
			lineName = section["line"]
			number = section["number"] 
			index = section["index"]
			if ("description" in section["line"].lower()):
				isSectionFound = True
				numberMacroSection = number
			if (isSectionFound):
				if (number[0] == numberMacroSection[0]):
					needed.append({int(index):lineName})
	return needed

def wikiSectionContent(curID, sections, language="en"):
	'''
	We need to extract sections from Wikipedia, as we have to use this API to retrieve single section, we need to manually
	parse text from sections, for this we need to use a dirty hack e.g. regex. Sources from Wikipedia can have just a single
	element e.g. 'Description' or can have various subsections
	'''
	response = requests.get("https://{}.wikipedia.org/w/api.php?action=query&format=json&pageids={}&prop=extracts&explaintext".format(language, curID))
	contents = []
	if (response.status_code == 200):
		sectionNames = [list(x.values())[0] for x in sections]
		print(sectionNames)
		content = response.json()
		text = content["query"]["pages"][str(curID)]["extract"]
		splittedText = re.split(r'\r?\n\n\n', text)
		for x in splittedText:
			search = re.match(r'==?= (.*?) ==?=', x)
			match = search.group(1) if search else ""
			if (match in sectionNames):
				contents.append(x)
	return contents

def querySparql(wd, wdt):
	sparql.setQuery("""

		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
		PREFIX wd: <http://www.wikidata.org/entity/> 
		PREFIX wdt: <http://www.wikidata.org/prop/direct/>
		PREFIX wikibase: <http://wikiba.se/ontology#>
		PREFIX bd: <http://www.bigdata.com/rdf#>
		
		SELECT ?o ?label WHERE {
			wd:""" + wd + """ wdt:""" + wdt + """ ?o .
			?o rdfs:label ?label .
			FILTER (langMatches( lang(?label), "EN" ) )
			SERVICE wikibase:label {
				bd:serviceParam wikibase:language "EN" .
			}
		}

	""")

	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	for result in results["results"]["bindings"]:
		return (result["label"]["value"])


def main():
	search = "St. Mark rescues a Sarracen"
	url = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&utf8=&format=json".format(encodeSearchWord(search))
	preliminarSearch = wikiSearch(url)
	if (preliminarSearch["gotResult"]):
		print("The content '{}' was found with pageID {}".format(preliminarSearch["title"], preliminarSearch["pageID"]))

		sections = wikiSections(preliminarSearch["pageID"])
		print("Description sections found:\n{}".format(sections))

		#print(wikiSectionContent(preliminarSearch["pageID"], sections))
		wikiOntReference = wikiOntology(preliminarSearch["pageID"])
		print("Found ontology reference: {}".format(wikiOntReference))
		end = querySparql(wikiOntReference, "P135")
		print("'{}' belongs to {}".format(preliminarSearch["title"], end))

def prova():
	querySparql("Q25729", "P135")

if __name__ == "__main__":
	#prova()
	main()

