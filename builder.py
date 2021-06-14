from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import RDF, RDFS, OWL, XSD, DC

BUILD_TAXONOMY = False

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
	
	
def saveToFile(ontology, fileName):
	with open("{}.ttl".format(fileName), "w") as ontFile:
		ontFile.write(ontology)

def buildTaxonomy():
	semioticDescription()
	connotativeDescription()
	expressiveDescription()
	denotativeDescription()
	complete = culturalMovement()
	saveToFile(complete, "ontology")

def addToOntology(resource):
	for key, value in resource.items():
		if (key == "resource"):
			res = URIRef(value)
			g.add((res, RDF.type, arco.CulturalProperty))
		if (key == "subject"):
			subject = value
			g.add((res, arcoSD.hasSubject, Literal(subject)))
		if (key == "scene"):
			scene = value
			g.add((res, arcoSD.hasDescriptionScene, Literal(scene)))
		if (key == "environment"):
			environment = value
			g.add((res, arcoSD.hasEnvironment, Literal(environment)))
		if (key == "foreground"):
			foreground = value
			g.add((res, arcoSD.hasForegroundElements, Literal(foreground)))
		if (key == "background"):
			background = value
			g.add((res, arcoSD.hasBackgroundElements, Literal(background)))
		if (key == "hasPerspectiveStudy"):
			perspectiveStudy = value
			g.add((res, arcoSD.hasPerspectiveStudy, Literal(perspectiveStudy)))
		'''
		if (key == "hasDescriptionRelations"):
			# TO DO
			descriptionRelations = value
			g.add((res, arcoSD.hasPerspectiveStudy, Literal(perspectiveStudy)))
		'''
		if (key == "denotativeTypeDefinition"):
			denotativeTypeDefinition = value
			g.add((res, arcoSD.hasDenotativeTypeDefinition,arcoSD[denotativeTypeDefinition]))
		if (key == "elementsRelationshipsType"):
			elementsRelationshipsType = value
			g.add((res, arcoSD.hasElementRelationshipsType,arcoSD[elementsRelationshipsType]))
		if (key == "hasSource"):
			hasSource = value
			g.add((res, arcoSD.hasSource,Literal(hasSource)))
		if (key == "hasMessage"):
			hasMessage = value
			g.add((res, arcoSD.hasMessage,Literal(hasMessage)))
		if (key == "hasTopic"):
			hasTopic = value
			g.add((res, arcoSD.hasTopic,Literal(hasTopic)))
		if (key == "hasLight"):
			hasLight = value
			g.add((res, arcoSD.hasLights,Literal(hasLight)))

def main():
	if (BUILD_TAXONOMY):
		buildTaxonomy()
	else:
		#
		dataToBeAdded = [
							{
								"resource": "https://w3id.org/arco/resource/HistoricOrArtisticProperty/0900287181",
								"subject": "The child Jesus, Mary, and Joseph",
								"scene": "The Holy Family",
								"environment": "The scene appears to be a rural one",
								"foreground": "The Holy Family",
								"background": "Five Nudes",
								"hasPerspectiveStudy": "The exedra where the naked in the background reside lies on a different perspective surface and with a lower vanishing point compared to the laying surface of the main figures and the low wall under Joseph, which has the task of concealing the gap.",
								"hasDescriptionRelations": "Mary is the most prominent figure in the composition, taking up much of the center of the image. Joseph is positioned higher in the image than Mary, although this is an unusual feature in compositions of the Holy Family. Mary is seated between his legs, as if he is protecting her, his great legs forming a kind of de facto throne. Saint John the Baptist is in the middle-ground of the painting, between the Holy Family and the background.",
								"denotativeTypeDefinition": "Figurative",
								"elementsRelationshipsType": "Symmetrical",
								"hasSource": "Wikipedia",
								"hasTopic": "Holy Family"
							},
							{
								"resource": "https://w3id.org/arco/resource/HistoricOrArtisticProperty/0900281988",
								"subject": "David",
								"scene": "Renaissance interpretation of a common ancient Greek theme of the standing heroic male nude",
								"environment": "Hero standing victorious over the head of Goliath",
								"foreground": "David",
								"hasDescriptionRelations": "This is typified in David, as the figure stands with one leg holding its full weight and the other leg forward. This classic pose causes the figure's hips and shoulders to rest at opposing angles, giving a slight s-curve to the entire torso. The contrapposto is emphasized by the turn of the head to the left, and by the contrasting positions of the arms. The proportions of the David are atypical of Michelangelo's work; the figure has an unusually large head and hands (particularly apparent in the right hand). The small size of the genitals, though, is in line with his other works and with Renaissance conventions in general, perhaps referencing the ancient Greek ideal of pre-pubescent male nudity.",
								"denotativeTypeDefinition": "Figurative",
								"elementsRelationshipsType": "Symmetrical",
								"hasSource": "Wikipedia",
								"hasMessage": "It is possible that the David was conceived as a political statue before Michelangelo began to work on it. Certainly, David the giant-killer had long been seen as a political figure in Florence, and images of the Biblical hero already carried political implications there.",
								"hasTopic": "David And Goliath"
							}

						]
		g.parse("smartology.owl", format="xml")
		for resource in dataToBeAdded:
			addToOntology(resource)
		saveToFile(g.serialize(format='turtle').decode("utf-8"), "test")


if __name__ == "__main__":
	main()

