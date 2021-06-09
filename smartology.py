import requests, json, re
from bs4 import BeautifulSoup as bs
from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("http://query.wikidata.org/sparql")

def encodeSearchWord(searchString):
	'''
	All queries need to be transformed following the HTML syntax
	'''
	return searchString.replace(" ", "%20").lower()

def encodeWikipediaName(entryName):
	'''
	Wikipedia entries follows the following syntax: This_is_an_example
	Underscores need to be added instead of spaces.
	'''
	return "_".join(entryName.split(" "))

def findInfo(keyword, lang="it"):
	'''
	In order to find as much works as possible, we need a good search system, the one provided
	by Wikipedia itself is good enough to search for free text and return the desired result.
	Entries can be searched in Italian
	'''
	url = "https://{}.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&utf8=&format=json".format(lang, keyword)
	response = requests.get(url)
	toBeRuturned = {"gotResult": False, "title": "", "pageID": 0, "lang":lang}
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
		print("Error while calling Wikipedia API")
	return toBeRuturned

def ontoSearch(keyword, lang="it"):
	'''
	This is used to convert the Title of the page found with 'findInfo' function into the
	correspondent ontology page, so we can grab the ontology ID for the searched entry
	'''
	url = "https://www.wikidata.org/wiki/Special:ItemByTitle?site={}wiki&page={}".format(lang, encodeWikipediaName(keyword))
	newURL = requests.get(url, allow_redirects=True)
	if (newURL.status_code == 200):
		return newURL.url.split("/")[-1]
	return None

def wikiOntology(ontoID):
	'''
	Wikidata offers an ontology where we can get data from, unfortunately reference
	to its content to Wikipedia can only be found on JSON version of ontology.
	This method allow to gather all links for every available language for a specific entry
	'''
	response = requests.get("https://www.wikidata.org/wiki/Special:EntityData/{}.json".format(ontoID))
	data = []
	if (response.status_code == 200):
		content = response.json()
		references = content["entities"][ontoID]["sitelinks"]
		for reference in references:
			lang = references[reference]["site"].split("wiki")[0]
			title = references[reference]["title"]
			url =  references[reference]["url"]
			dataDict = {"language": lang, "title": title, "url": url}
			data.append(dataDict)
	return data


def desiredLanguage(urls, langs=["it", "en"]):
	'''
	It allows to extract Wikipedia links only for desired languages, at this point English is preferred
	as it will be easier to work with IA, if English is not available then Italian content link will be 
	used.
	'''
	for language in urls:
		if (language["language"] == "en"):
			return language
		if (language["language"] == "it"):
			return language
	return None

def extractSections(soup):
	toclevel = soup.findAll("li", attrs={"class": "tocsection-1"})
	sectionList = []
	for toc in toclevel:
		rawText = toc.findAll("span", attrs={"class":"toctext"})
		for section in rawText:
			sectionList.append(section.text)
	return sectionList


def wikiSections(pageName, language):
	'''
	We need to understand how a Wikipedia page is made, we need to understand if we have a 'Description' field, then retrieve index numbers we need.
	This includes a little dirty hack to retrieve subsection of 'Description' as there is no way to straightly retrieve them 
	'''
	response = requests.get("https://{}.wikipedia.org/w/api.php?action=parse&format=json&page={}&prop=sections&disabletoc=1".format(language, pageName))
	needed = []
	if (response.status_code == 200):
		content = response.json()["parse"]
		pageID = content["pageid"]
		for section in content["sections"]:
			# We want to take only the first section, that means that number "1" or "1.x" need to be there
			if (section["number"] == "1" or "1." in section["number"]):
				needed.append({section["number"]:section["line"]})
	return pageID, needed

def wikiSectionContent(pageName, pageID, sections, language):
	'''
	We need to extract sections from Wikipedia, as we have to use this API to retrieve single section, we need to manually
	parse text from sections, for this we need to use a dirty hack e.g. regex. Sources from Wikipedia can have just a single
	element e.g. 'Description' or can have various subsections
	'''
	response = requests.get("https://{}.wikipedia.org/w/api.php?action=query&format=json&titles={}&prop=extracts&explaintext".format(language, pageName))
	contents = []
	if (response.status_code == 200):
		sectionNames = [list(x.values())[0] for x in sections]
		content = response.json()
		text = content["query"]["pages"][str(pageID)]["extract"]
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
			FILTER (langMatches( lang(?label), "IT" ) )
			SERVICE wikibase:label {
				bd:serviceParam wikibase:language "IT" .
			}
		}

	""")

	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	res = []
	for result in results["results"]["bindings"]:
		res.append(result["label"]["value"])
	return res


def extractCulturalMovement(keyword):
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
			movement = querySparql(ontoID, "P135")
			if (len(movement) > 0):
				print("\n'{}' belongs to '{}' movement.\n".format(title, movement[0]))
				return movement[0]
	return None

def main():
	keyword = "ultima cena leonardo"
	#keyword = "San Marco salva saraceno"
	#keyword = "la persistenza della memoria"
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

if __name__ == "__main__":
	main()

