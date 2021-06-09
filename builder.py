from rdflib import Graph, Literal, RDF, RDFS, URIRef
# rdflib knows about some namespaces, like FOAF
from rdflib.namespace import XSD, OWL
from rdflib import Namespace

bene = "Ultima_cena"

arcoCd = Namespace("https://w3id.org/arco/ontology/context-description/")
arco = Namespace("https://w3id.org/arco/ontology/arco/")

def connotativeDescription():
	# create a Graph
	g = Graph()
	g.bind("arco", arco)
	g.bind("a-cd", arcoCd)

	# Create an RDF URI node to use as the subject for multiple triples
	subject = URIRef("{}/TheLastSupper/".format(arco.name))

	# Add triples using store's add() method.
	g.add((subject, RDF.type, arco.CulturalProperty))
	g.add((arcoCd.Interpretation, RDFS.subClassOf, arcoCd.ConnotativeDescription))
	g.add((arcoCd.Message, RDFS.subClassOf, arcoCd.Interpretation))
	g.add((arcoCd.Topic, RDFS.subClassOf, arcoCd.Interpretation))
	g.add((arcoCd.hasMessage, RDF.type, OWL.ObjectProperty))
	g.add((arcoCd.Message, arcoCd.hasMessage, Literal("Qualcosa", datatype=XSD.string)))
	g.add((arcoCd.hasSource, RDF.type, OWL.ObjectProperty))
	g.add((arcoCd.Message, arcoCd.hasSource, Literal("Wikipedia?", datatype=XSD.string)))
	g.add((arcoCd.hasTopic, RDF.type, OWL.ObjectProperty))
	g.add((arcoCd.Topic, arcoCd.hasTopic, Literal("Topic", datatype=XSD.string)))

	ont = g.serialize(format='turtle').decode("utf-8")
	print(ont)
	return ont

def expressiveDescription():
	# create a Graph
	g = Graph()
	g.bind("arco", arco)
	g.bind("a-cd", arcoCd)

	# Create an RDF URI node to use as the subject for multiple triples
	subject = URIRef("{}/TheLastSupper/".format(arco.name))

	g.add((subject, RDF.type, arco.CulturalProperty))
	g.add((arcoCd.Colour, RDFS.subClassOf, arcoCd.ExpressiveDescription))
	g.add((arcoCd.Lights, RDFS.subClassOf, arcoCd.ExpressiveDescription))
	g.add((arcoCd.hasColour, RDF.type, OWL.ObjectProperty))
	g.add((arcoCd.Colour, arcoCd.hasColour, Literal("Colore", datatype=XSD.string)))
	g.add((arcoCd.hasLights, RDF.type, OWL.ObjectProperty))
	g.add((arcoCd.Lights, arcoCd.hasLights, Literal("Luci", datatype=XSD.string)))

	ont = g.serialize(format='turtle').decode("utf-8")
	print(ont)
	return ont

def saveToFile(ontology):
	with open("ontology.ttl", "w") as ontFile:
		ontFile.write(ontology)

def main():
	ontology = expressiveDescription()
	saveToFile(ontology)

if __name__ == '__main__':
	main()
