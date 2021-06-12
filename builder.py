from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import RDF, RDFS, OWL, XSD, DC
from rdflib import Namespace

arcoSD = Namespace("https://domain/smartology/semiotic-description/")
arco = Namespace("https://w3id.org/arco/ontology/arco/")
arcoCd = Namespace("https://w3id.org/arco/ontology/context-description/")
AGID = Namespace("https://w3id.org/italia/onto/TI/")

#Create a graph
g = Graph()
g.bind("arco", arco)
g.bind("s-sd", arcoSD)
g.bind("a-cd",arcoCd)
g.bind("dc", DC)

def semioticDescription():
	# Semiotic Description
	g.add((arcoSD.hasWikiDescription, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasWikiDescription, RDFS.domain, arco.CulturalProperty))
	g.add((arcoSD.hasWikiDescription, RDFS.range, RDFS.Literal))

	g.add((arco.CulturalProperty, RDF.type, OWL.Class))

	g.add((arcoSD.hasSemioticDescription, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasSemioticDescription, RDFS.domain, arco.CulturalProperty))
	g.add((arcoSD.hasSemioticDescription, RDFS.range, arcoSD.SemioticDescription))
	g.add((arcoSD.hasSemioticDescription, OWL.inverseOf, arcoSD.isSemioticDescriptionOf))
	g.add((arcoSD.isSemioticDescriptionOf, RDFS.domain, arcoSD.SemioticDescription))
	g.add((arcoSD.isSemioticDescriptionOf, RDFS.range, arco.CulturalProperty))
	g.add((arcoSD.isSemioticDescriptionOf, OWL.inverseOf, arcoSD.hasSemioticDescription))

	g.add((arcoSD.SemioticDescription, RDF.type, OWL.Class))
	g.add((arcoSD.SemioticDescription, RDFS.subClassOf, arco.CulturalProperty))

	g.add((arcoSD.hasExpressiveDescription, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasExpressiveDescription, RDFS.domain, arcoSD.SemioticDescription))
	g.add((arcoSD.hasExpressiveDescription, RDFS.range, arcoSD.ExpressiveDescription))
	g.add((arcoSD.hasExpressiveDescription, OWL.inverseOf, arcoSD.isExpressiveDescriptionOf))
	g.add((arcoSD.isExpressiveDescriptionOf, RDFS.domain, arcoSD.ExpressiveDescription))
	g.add((arcoSD.isExpressiveDescriptionOf, RDFS.range, arcoSD.SemioticDescription))
	g.add((arcoSD.isExpressiveDescriptionOf, OWL.inverseOf, arcoSD.hasExpressiveDescription))


	g.add((arcoSD.ExpressiveDescription, RDF.type, OWL.Class))
	g.add((arcoSD.ExpressiveDescription, RDFS.subClassOf, arcoSD.SemioticDescription))

	g.add((arcoSD.hasCulturalMovement, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasCulturalMovement, RDFS.domain, arco.CulturalProperty))
	g.add((arcoSD.hasCulturalMovement, RDFS.range, arcoSD.CulturalMovement))
	g.add((arcoSD.hasCulturalMovement, OWL.inverseOf, arcoSD.isCulturalMovementOf))
	g.add((arcoSD.isCulturalMovementOf, RDFS.domain, arcoSD.CulturalMovement))
	g.add((arcoSD.isCulturalMovementOf, RDFS.range, arco.CulturalProperty))
	g.add((arcoSD.isCulturalMovementOf, OWL.inverseOf, arcoSD.hasCulturalMovement))

	g.add((arcoSD.CulturalMovement, RDF.type, OWL.Class))
	g.add((arcoSD.CulturalMovement, RDFS.subClassOf, arco.CulturalProperty))

	g.add((arcoSD.hasConnotativeDescription, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasConnotativeDescription, RDFS.domain, arcoSD.SemioticDescription))
	g.add((arcoSD.hasConnotativeDescription, RDFS.range, arcoSD.ConnotativeDescription))
	g.add((arcoSD.hasConnotativeDescription, OWL.inverseOf, arcoSD.isConnotativeDescriptionOf))
	g.add((arcoSD.isConnotativeDescriptionOf, RDFS.domain, arcoSD.ConnotativeDescription))
	g.add((arcoSD.isConnotativeDescriptionOf, RDFS.range, arcoSD.SemioticDescription))
	g.add((arcoSD.isConnotativeDescriptionOf, OWL.inverseOf, arcoSD.hasConnotativeDescription))

	g.add((arcoSD.ConnotativeDescription, RDF.type, OWL.Class))
	g.add((arcoSD.ConnotativeDescription, RDFS.subClassOf, arcoSD.SemioticDescription))

	g.add((arcoSD.hasDenotativeDescription, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasDenotativeDescription, RDFS.domain, arcoSD.SemioticDescription))
	g.add((arcoSD.hasDenotativeDescription, RDFS.range, arcoSD.DenotativeDescription))
	g.add((arcoSD.hasDenotativeDescription, OWL.inverseOf, arcoSD.isDenotativeDescriptionOf))
	g.add((arcoSD.isDenotativeDescriptionOf, RDFS.domain, arcoSD.DenotativeDescription))
	g.add((arcoSD.isDenotativeDescriptionOf, RDFS.range, arcoSD.SemioticDescription))
	g.add((arcoSD.isDenotativeDescriptionOf, OWL.inverseOf, arcoSD.hasDenotativeDescription))

	g.add((arcoSD.DenotativeDescription, RDF.type, OWL.Class))
	g.add((arcoSD.DenotativeDescription, RDFS.subClassOf, arcoSD.SemioticDescription))
	
	ont = g.serialize(format='turtle').decode("utf-8")
	return ont

def connotativeDescription():
	#ConnotativeDescription
	g.add((arcoSD.ConnotativeDescription, RDF.type, OWL.Class))
	g.add((arcoSD.Interpretation, RDF.type, OWL.Class))
	g.add((arcoSD.Interpretation, RDFS.subClassOf, arcoSD.ConnotativeDescription))

	g.add((arcoSD.hasInterpretation, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasInterpretation, RDFS.domain, arcoSD.ConnotativeDescription))
	g.add((arcoSD.hasInterpretation, RDFS.range, arcoSD.Interpretation))
	g.add((arcoSD.hasInterpretation, OWL.inverseOf, arcoSD.isInterpretationOf))
	g.add((arcoSD.isInterpretationOf, RDFS.domain, arcoSD.Interpretation))
	g.add((arcoSD.isInterpretationOf, RDFS.range, arcoSD.ConnotativeDescription))
	g.add((arcoSD.isInterpretationOf, OWL.inverseOf, arcoSD.hasInterpretation))

	g.add((arcoSD.hasMessageInterpretation, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasMessageInterpretation, RDFS.domain, arcoSD.Interpretation))
	g.add((arcoSD.hasMessageInterpretation, RDFS.range, arcoSD.Message))
	g.add((arcoSD.hasMessageInterpretation, OWL.inverseOf, arcoSD.isMessageInterpretationOf))
	g.add((arcoSD.isMessageInterpretationOf, RDFS.domain, arcoSD.Message))
	g.add((arcoSD.isMessageInterpretationOf, RDFS.range, arcoSD.Interpretation))
	g.add((arcoSD.isMessageInterpretationOf, OWL.inverseOf, arcoSD.hasMessageInterpretation))


	g.add((arcoSD.Message, RDF.type, OWL.Class))
	g.add((arcoSD.Message, RDFS.subClassOf, arcoSD.Interpretation))

	g.add((arcoSD.hasMessage, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasMessage, RDFS.domain, arcoSD.Message))
	g.add((arcoSD.hasMessage, RDFS.range, RDFS.Literal))

	g.add((arcoSD.hasSource, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasSource, RDFS.domain, arcoSD.Message))
	g.add((arcoSD.hasSource, RDFS.range, RDFS.Literal))

	g.add((arcoSD.hasTopic, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasTopic, RDFS.domain, arcoSD.Interpretation))
	g.add((arcoSD.hasTopic, RDFS.range, RDFS.Literal))

	ont = g.serialize(format='turtle').decode("utf-8")
	return ont

def expressiveDescription():
	# Expressive Detection
	g.add((arcoSD.ExpressiveDescription, RDF.type, OWL.Class))
	
	g.add((arcoSD.hasColour, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasColour, RDFS.domain, arcoSD.ExpressiveDescription))
	g.add((arcoSD.hasColour, RDFS.range, RDFS.Literal))
	
	g.add((arcoSD.hasLights, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasLights, RDFS.domain, arcoSD.ExpressiveDescription))
	g.add((arcoSD.hasLights, RDFS.range, RDFS.Literal))
	
	ont = g.serialize(format='turtle').decode("utf-8")
	return ont

def denotativeDescription():
	# Denotative description
	g.add((arcoSD.Iconic, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Iconic,RDF.type,arcoSD.DenotativeTypeDefinition))

	g.add((arcoSD.Figurative, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Figurative,RDF.type,arcoSD.DenotativeTypeDefinition))

	g.add((arcoSD.Abstract, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Abstract,RDF.type,arcoSD.DenotativeTypeDefinition))

	g.add((arcoSD.Symmetrical, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Symmetrical,RDF.type,arcoSD.ElemetsRelationshipsType))

	g.add((arcoSD.Asymmetrical, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Asymmetrical,RDF.type,arcoSD.ElemetsRelationshipsType))

	g.add((arcoSD.DenotativeDescription, RDF.type, OWL.Class))

	g.add((arcoSD.DenotativeTypeDefinition, RDF.type, OWL.Class))
	g.add((arcoSD.DenotativeTypeDefinition, RDFS.subClassOf, arcoSD.DenotativeDescription))

	g.add((arcoSD.ElemetsRelationshipsType, RDF.type, OWL.Class))
	g.add((arcoSD.ElemetsRelationshipsType, RDFS.subClassOf, arcoSD.ElementRelationships))

	g.add((arcoSD.hasDenotativeTypeDefinition, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasDenotativeTypeDefinition, RDFS.domain, arcoSD.DenotativeDescription))
	g.add((arcoSD.hasDenotativeTypeDefinition, RDFS.range, arcoSD.DenotativeTypeDefinition))
	g.add((arcoSD.hasDenotativeTypeDefinition, OWL.inverseOf, arcoSD.isDenotativeTypeDefinitionOf))
	g.add((arcoSD.isDenotativeTypeDefinitionOf, RDFS.domain, arcoSD.DenotativeTypeDefinition))
	g.add((arcoSD.isDenotativeTypeDefinitionOf, RDFS.range, arcoSD.DenotativeDescription))
	g.add((arcoSD.isDenotativeTypeDefinitionOf, OWL.inverseOf, arcoSD.hasDenotativeTypeDefinition))

	g.add((arcoSD.hasScene, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasScene, RDFS.domain, arcoSD.DenotativeDescription))
	g.add((arcoSD.hasScene, RDFS.range, arcoSD.Scene))
	g.add((arcoSD.hasScene, OWL.inverseOf, arcoSD.isSceneOf))
	g.add((arcoSD.isSceneOf, RDFS.domain, arcoSD.Scene))
	g.add((arcoSD.isSceneOf, RDFS.range, arcoSD.DenotativeDescription))
	g.add((arcoSD.isSceneOf, OWL.inverseOf, arcoSD.hasScene))

	g.add((arcoSD.Scene, RDF.type, OWL.Class))
	g.add((arcoSD.Scene, RDFS.subClassOf, arcoSD.DenotativeDescription))

	g.add((arcoSD.hasDescriptionScene, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasDescriptionScene, RDFS.domain, arcoSD.Scene))
	g.add((arcoSD.hasDescriptionScene, RDFS.range, RDFS.Literal))

	g.add((arcoSD.hasEnvironment, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasEnvironment, RDFS.domain, arcoSD.Scene))
	g.add((arcoSD.hasEnvironment, RDFS.range, RDFS.Literal))

	g.add((arcoSD.hasComposition, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasComposition, RDFS.domain, arcoSD.DenotativeDescription))
	g.add((arcoSD.hasComposition, RDFS.range, arcoSD.Composition))
	g.add((arcoSD.hasComposition, OWL.inverseOf, arcoSD.isCompositionOf))
	g.add((arcoSD.isCompositionOf, RDFS.domain, arcoSD.Composition))
	g.add((arcoSD.isCompositionOf, RDFS.range, arcoSD.DenotativeDescription))
	g.add((arcoSD.isCompositionOf, OWL.inverseOf, arcoSD.hasComposition))

	g.add((arcoSD.Composition, RDF.type, OWL.Class))
	g.add((arcoSD.Composition, RDFS.subClassOf, arcoSD.DenotativeDescription))

	g.add((arcoSD.hasSubject, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasSubject, RDFS.domain, arcoSD.Composition))
	g.add((arcoSD.hasSubject, RDFS.range, RDFS.Literal))

	g.add((arcoSD.hasElementsComposition, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasElementsComposition, RDFS.domain, arcoSD.Composition))
	g.add((arcoSD.hasElementsComposition, RDFS.range, arcoSD.ElementsComposition))
	g.add((arcoSD.hasElementsComposition, OWL.inverseOf, arcoSD.isElementsCompositionOf))
	g.add((arcoSD.isElementsCompositionOf, RDFS.domain, arcoSD.ElementsComposition))
	g.add((arcoSD.isElementsCompositionOf, RDFS.range, arcoSD.Composition))
	g.add((arcoSD.isElementsCompositionOf, OWL.inverseOf, arcoSD.hasElementsComposition))

	g.add((arcoSD.ElementsComposition, RDF.type, OWL.Class))
	g.add((arcoSD.ElementsComposition, RDFS.subClassOf, arcoSD.Composition))

	g.add((arcoSD.hasForegroundElements, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasForegroundElements, RDFS.domain, arcoSD.ElementsComposition))
	g.add((arcoSD.hasForegroundElements, RDFS.range, RDFS.Literal))

	g.add((arcoSD.hasBackgroundElements, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasBackgroundElements, RDFS.domain, arcoSD.ElementsComposition))
	g.add((arcoSD.hasBackgroundElements, RDFS.range, RDFS.Literal))

	g.add((arcoSD.hasRelationsComposition, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasRelationsComposition, RDFS.domain, arcoSD.Composition))
	g.add((arcoSD.hasRelationsComposition, RDFS.range, arcoSD.RelationsComposition))
	g.add((arcoSD.hasRelationsComposition, OWL.inverseOf, arcoSD.isRelationsCompositionOf))
	g.add((arcoSD.isRelationsCompositionOf, RDFS.domain, arcoSD.RelationsComposition))
	g.add((arcoSD.isRelationsCompositionOf, RDFS.range, arcoSD.Composition))
	g.add((arcoSD.isRelationsCompositionOf, OWL.inverseOf, arcoSD.hasRelationsComposition))

	g.add((arcoSD.RelationsComposition, RDF.type, OWL.Class))
	g.add((arcoSD.RelationsComposition, RDFS.subClassOf, arcoSD.Composition))

	g.add((arcoSD.hasPerspectiveStudy, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasPerspectiveStudy, RDFS.domain, arcoSD.RelationsComposition))
	g.add((arcoSD.hasPerspectiveStudy, RDFS.range, RDFS.Literal))

	g.add((arcoSD.hasElementRelationships, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasElementRelationships, RDFS.domain, arcoSD.RelationsComposition))
	g.add((arcoSD.hasElementRelationships, RDFS.range, arcoSD.ElementRelationships))
	g.add((arcoSD.hasElementRelationships, OWL.inverseOf, arcoSD.isElementRelationshipsOf))
	g.add((arcoSD.isElementRelationshipsOf, RDFS.domain, arcoSD.ElementRelationships))
	g.add((arcoSD.isElementRelationshipsOf, RDFS.range, arcoSD.RelationsComposition))
	g.add((arcoSD.isElementRelationshipsOf, OWL.inverseOf, arcoSD.hasElementRelationships))

	g.add((arcoSD.ElementRelationships, RDF.type, OWL.Class))
	g.add((arcoSD.ElementRelationships, RDFS.subClassOf, arcoSD.RelationsComposition))

	g.add((arcoSD.hasElementRelationshipsType, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasElementRelationshipsType, RDFS.domain, arcoSD.ElementRelationships))
	g.add((arcoSD.hasElementRelationshipsType, RDFS.range, arcoSD.ElemetsRelationshipsType))
	g.add((arcoSD.hasElementRelationshipsType, OWL.inverseOf, arcoSD.isElementRelationshipsTypeOf))
	g.add((arcoSD.isElementRelationshipsTypeOf, RDFS.domain, arcoSD.ElemetsRelationshipsType))
	g.add((arcoSD.isElementRelationshipsTypeOf, RDFS.range, arcoSD.ElementRelationships))
	g.add((arcoSD.isElementRelationshipsTypeOf, OWL.inverseOf, arcoSD.hasElementRelationshipsType))

	ont = g.serialize(format='turtle').decode("utf-8")
	return ont

def culturalMovement():
	#Cultural Movement
	g.add((arcoSD.CulturalMovement, RDF.type, OWL.Class))

	g.add((DC.title, RDF.type, OWL.DatatypeProperty))
	g.add((DC.title, RDFS.range, RDFS.Literal))
	g.add((DC.title, RDFS.domain, arcoSD.CulturalMovement))

	g.add((DC.description, RDF.type, OWL.DatatypeProperty))
	g.add((DC.description, RDFS.range, RDFS.Literal))
	g.add((DC.description, RDFS.domain, arcoSD.CulturalMovement))

	g.add((DC.location, RDF.type, OWL.DatatypeProperty))
	g.add((DC.location, RDFS.range, RDFS.Literal))
	g.add((DC.location, RDFS.domain, arcoSD.CulturalMovement))

	g.add((DC.source, RDF.type, OWL.DatatypeProperty))
	g.add((DC.source, RDFS.range, RDFS.Literal))
	g.add((DC.source, RDFS.domain, arcoSD.CulturalMovement))
	
	g.add((AGID.TimeInterval, RDF.type, OWL.Class))
	g.add((AGID.TimeInterval, RDFS.subClassOf, arcoSD.CulturalMovement))

	g.add((arcoCd.startTime, RDF.type, OWL.DatatypeProperty))
	g.add((arcoCd.startTime, RDFS.range, RDFS.Literal))
	g.add((arcoCd.startTime, RDFS.domain, AGID.TimeInterval))

	g.add((arcoCd.endTime, RDF.type, OWL.DatatypeProperty))
	g.add((arcoCd.endTime, RDFS.range, RDFS.Literal))
	g.add((arcoCd.endTime, RDFS.domain, AGID.TimeInterval))

	g.add((arcoSD.hasTimeInterval, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasTimeInterval, RDFS.range, AGID.TimeInterval))
	g.add((arcoSD.hasTimeInterval, RDFS.domain, arcoSD.CulturalMovement))
	g.add((arcoSD.hasTimeInterval, OWL.inverseOf, arcoSD.isTimeIntervalOf))
	g.add((arcoSD.isTimeIntervalOf, RDFS.domain, AGID.TimeInterval))
	g.add((arcoSD.isTimeIntervalOf, RDFS.range, arcoSD.CulturalMovement))
	g.add((arcoSD.isTimeIntervalOf, OWL.inverseOf, arcoSD.hasTimeInterval))
	
	ont = g.serialize(format='turtle').decode("utf-8")
	return ont
	
	
def saveToFile(ontology):
	with open("ontology.ttl", "w") as ontFile:
		ontFile.write(ontology)

def main():
	semioticDescription()
	connotativeDescription()
	expressiveDescription()
	denotativeDescription()
	complete = culturalMovement()
	saveToFile(complete)

if __name__ == "__main__":
	main()

