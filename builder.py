from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import RDF, RDFS, OWL, XSD, DC

BUILD_TAXONOMY = True
TAXONOMY_FILE = "smartology"

arcoSD = Namespace("https://domain/smartology/semiotic-description/")
arco = Namespace("https://w3id.org/arco/ontology/arco/")
arcoCd = Namespace("https://w3id.org/arco/ontology/context-description/")

#Create a graph
g = Graph()
g.bind("arco", arco)
g.bind("s-sd", arcoSD)
g.bind("a-cd",arcoCd)
g.bind("dc", DC)
g.bind("owl", OWL)


def semioticDescription():
	# Semiotic Description
	g.add((arcoSD.hasWikiDescription, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasWikiDescription, RDFS.domain, arco.CulturalProperty))
	g.add((arcoSD.hasWikiDescription, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasWikiDescription, RDFS.comment, Literal("This property represents the description of the cultural asset provided by Wikipedia.", lang="en")))

	g.add((arco.CulturalProperty, RDF.type, OWL.Class))

	g.add((arcoSD.hasSemioticDescription, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasSemioticDescription, RDFS.domain, arco.CulturalProperty))
	g.add((arcoSD.hasSemioticDescription, RDFS.range, arcoSD.SemioticDescription))
	g.add((arcoSD.hasSemioticDescription, OWL.inverseOf, arcoSD.isSemioticDescriptionOf))
	g.add((arcoSD.hasSemioticDescription, RDFS.comment, Literal("This property connects a 'CulturalProperty' with 'SemioticDescription'.", lang="en")))

	g.add((arcoSD.isSemioticDescriptionOf, RDFS.domain, arcoSD.SemioticDescription))
	g.add((arcoSD.isSemioticDescriptionOf, RDFS.range, arco.CulturalProperty))
	g.add((arcoSD.isSemioticDescriptionOf, OWL.inverseOf, arcoSD.hasSemioticDescription))
	g.add((arcoSD.isSemioticDescriptionOf, RDFS.comment, Literal("This is the inverse property of 'hasSemioticDescription'.", lang="en")))

	g.add((arcoSD.SemioticDescription, RDF.type, OWL.Class))
	g.add((arcoSD.SemioticDescription, RDFS.subClassOf, arco.CulturalProperty))
	g.add((arcoSD.SemioticDescription, RDFS.comment, Literal("This class represents the semiotic description of a cultural asset, taking into consideration the meanings present in a painting, a sculpture or a print.", lang="en")))

	g.add((arcoSD.hasExpressiveDescription, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasExpressiveDescription, RDFS.domain, arcoSD.SemioticDescription))
	g.add((arcoSD.hasExpressiveDescription, RDFS.range, arcoSD.ExpressiveDescription))
	g.add((arcoSD.hasExpressiveDescription, OWL.inverseOf, arcoSD.isExpressiveDescriptionOf))
	g.add((arcoSD.hasExpressiveDescription, RDFS.comment, Literal("This property relates a cultural asset to its expressive description.", lang="en")))

	g.add((arcoSD.isExpressiveDescriptionOf, RDFS.domain, arcoSD.ExpressiveDescription))
	g.add((arcoSD.isExpressiveDescriptionOf, RDFS.range, arcoSD.SemioticDescription))
	g.add((arcoSD.isExpressiveDescriptionOf, OWL.inverseOf, arcoSD.hasExpressiveDescription))
	g.add((arcoSD.isExpressiveDescriptionOf, RDFS.comment, Literal("This property relates the expressive description with the related cultural asset.", lang="en")))

	g.add((arcoSD.ExpressiveDescription, RDF.type, OWL.Class))
	g.add((arcoSD.ExpressiveDescription, RDFS.subClassOf, arcoSD.SemioticDescription))
	g.add((arcoSD.ExpressiveDescription, RDFS.comment, Literal("This class represents a reading of the work in an expressive key. The cultural asset is analyzed from the point of view of the technical components designed to convey its meaning (i.e. colour, lights and shadows).", lang="en")))

	#CULTURAL MOVEMENT AS CLASS WILL BE IMPLEMENTED LATER
	g.add((arcoSD.hasCulturalMovement, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasCulturalMovement, RDFS.domain, arco.CulturalProperty))
	#g.add((arcoSD.hasCulturalMovement, RDFS.range, arcoSD.CulturalMovement))
	#g.add((arcoSD.hasCulturalMovement, OWL.inverseOf, arcoSD.isCulturalMovementOf))
	g.add((arcoSD.hasCulturalMovement, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasCulturalMovement, RDFS.comment, Literal("This property links the cultural property to the related cultural movement", lang="en")))
	
	#CULTURAL MOVEMENT AS CLASS WILL BE IMPLEMENTED LATER
	#g.add((arcoSD.isCulturalMovementOf, RDFS.domain, arcoSD.CulturalMovement))
	#g.add((arcoSD.isCulturalMovementOf, RDFS.range, arco.CulturalProperty))
	#g.add((arcoSD.isCulturalMovementOf, OWL.inverseOf, arcoSD.hasCulturalMovement))
	#g.add((arcoSD.isCulturalMovementOf, RDFS.comment, Literal("This property links the cultural movement to the related cultural property.", lang="en")))

	#g.add((arcoSD.CulturalMovement, RDF.type, OWL.Class))
	#g.add((arcoSD.CulturalMovement, RDFS.comment, Literal("This class represents the cultural movement to which the cultural asset is linked (i.e. Renaissance, Gotic).", lang="en")))

	g.add((arcoSD.hasConnotativeDescription, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasConnotativeDescription, RDFS.domain, arcoSD.SemioticDescription))
	g.add((arcoSD.hasConnotativeDescription, RDFS.range, arcoSD.ConnotativeDescription))
	g.add((arcoSD.hasConnotativeDescription, OWL.inverseOf, arcoSD.isConnotativeDescriptionOf))
	g.add((arcoSD.hasConnotativeDescription, RDFS.comment, Literal("This property relates a cultural asset to its connotative description.", lang="en")))


	g.add((arcoSD.isConnotativeDescriptionOf, RDFS.domain, arcoSD.ConnotativeDescription))
	g.add((arcoSD.isConnotativeDescriptionOf, RDFS.range, arcoSD.SemioticDescription))
	g.add((arcoSD.isConnotativeDescriptionOf, OWL.inverseOf, arcoSD.hasConnotativeDescription))
	g.add((arcoSD.isConnotativeDescriptionOf, RDFS.comment, Literal("This property relates the connotative description with the related cultural asset.", lang="en")))

	g.add((arcoSD.ConnotativeDescription, RDF.type, OWL.Class))
	g.add((arcoSD.ConnotativeDescription, RDFS.subClassOf, arcoSD.SemioticDescription))
	g.add((arcoSD.ConnotativeDescription, RDFS.comment, Literal("This class represents a second reading of the cultural asset based on the analysis of the message and topics to which it is associated (i.e. message, topic).", lang="en")))

	g.add((arcoSD.hasDenotativeDescription, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasDenotativeDescription, RDFS.domain, arcoSD.SemioticDescription))
	g.add((arcoSD.hasDenotativeDescription, RDFS.range, arcoSD.DenotativeDescription))
	g.add((arcoSD.hasDenotativeDescription, OWL.inverseOf, arcoSD.isDenotativeDescriptionOf))
	g.add((arcoSD.hasDenotativeDescription, RDFS.comment, Literal("This property relates a cultural asset to its denotative description.", lang="en")))

	g.add((arcoSD.isDenotativeDescriptionOf, RDFS.domain, arcoSD.DenotativeDescription))
	g.add((arcoSD.isDenotativeDescriptionOf, RDFS.range, arcoSD.SemioticDescription))
	g.add((arcoSD.isDenotativeDescriptionOf, OWL.inverseOf, arcoSD.hasDenotativeDescription))
	g.add((arcoSD.isDenotativeDescriptionOf, RDFS.comment, Literal("This property relates the denotative description with the related cultural asset.", lang="en")))

	g.add((arcoSD.DenotativeDescription, RDF.type, OWL.Class))
	g.add((arcoSD.DenotativeDescription, RDFS.subClassOf, arcoSD.SemioticDescription))
	g.add((arcoSD.DenotativeDescription, RDFS.comment, Literal("This class represents a first reading of the cultural asset based on the descriptive analysis of the elements that compose it (i.e. scene, denotative type, subject).", lang="en")))
	
	ont = g.serialize(format='turtle').decode("utf-8")
	return ont

def connotativeDescription():
	#ConnotativeDescription
	g.add((arcoSD.ConnotativeDescription, RDF.type, OWL.Class))
	g.add((arcoSD.ConnotativeDescription, RDFS.comment, Literal("This class represents a second reading of the cultural asset based on the analysis of the message and topics to which it is associated (i.e. message, topic).", lang="en")))

	g.add((arcoSD.Interpretation, RDF.type, OWL.Class))
	g.add((arcoSD.Interpretation, RDFS.subClassOf, arcoSD.ConnotativeDescription))
	g.add((arcoSD.Interpretation, RDFS.comment, Literal("This class groups together the elements on which the interpretation of a cultural asset is based (eg message, topic).", lang="en")))

	g.add((arcoSD.hasInterpretation, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasInterpretation, RDFS.domain, arcoSD.ConnotativeDescription))
	g.add((arcoSD.hasInterpretation, RDFS.range, arcoSD.Interpretation))
	g.add((arcoSD.hasInterpretation, OWL.inverseOf, arcoSD.isInterpretationOf))
	g.add((arcoSD.hasInterpretation, RDFS.comment, Literal("This property relates a cultural asset to its connotative interpretation.", lang="en")))

	g.add((arcoSD.isInterpretationOf, RDFS.domain, arcoSD.Interpretation))
	g.add((arcoSD.isInterpretationOf, RDFS.range, arcoSD.ConnotativeDescription))
	g.add((arcoSD.isInterpretationOf, OWL.inverseOf, arcoSD.hasInterpretation))
	g.add((arcoSD.isInterpretationOf, RDFS.comment, Literal("This property relates the connotative interpretation with the related cultural asset.", lang="en")))

	g.add((arcoSD.hasMessageInterpretation, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasMessageInterpretation, RDFS.domain, arcoSD.Interpretation))
	g.add((arcoSD.hasMessageInterpretation, RDFS.range, arcoSD.Message))
	g.add((arcoSD.hasMessageInterpretation, OWL.inverseOf, arcoSD.isMessageInterpretationOf))
	g.add((arcoSD.hasMessageInterpretation, RDFS.comment, Literal("This property relates the generic class that specifies the interpretation of a cultural asset with the specific class which makes explicit its message.", lang="en")))

	g.add((arcoSD.isMessageInterpretationOf, RDFS.domain, arcoSD.Message))
	g.add((arcoSD.isMessageInterpretationOf, RDFS.range, arcoSD.Interpretation))
	g.add((arcoSD.isMessageInterpretationOf, OWL.inverseOf, arcoSD.hasMessageInterpretation))
	g.add((arcoSD.isMessageInterpretationOf, RDFS.comment, Literal("This is the inverse property of 'has message interpretation'.", lang="en")))

	g.add((arcoSD.Message, RDF.type, OWL.Class))
	g.add((arcoSD.Message, RDFS.subClassOf, arcoSD.Interpretation))
	g.add((arcoSD.Message, RDFS.comment, Literal("This class groups together the elements related to the message conveyed by the cultural property.", lang="en")))

	g.add((arcoSD.hasMessage, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasMessage, RDFS.domain, arcoSD.Message))
	g.add((arcoSD.hasMessage, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasMessage, RDFS.comment, Literal("This property relates the cultural asset to the analysis of its message.", lang="en")))

	g.add((arcoSD.hasSource, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasSource, RDFS.domain, arcoSD.Message))
	g.add((arcoSD.hasSource, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasSource, RDFS.comment, Literal("This property relates the source of data to the class 'Message'.", lang="en")))

	g.add((arcoSD.hasTopic, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasTopic, RDFS.domain, arcoSD.Interpretation))
	g.add((arcoSD.hasTopic, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasTopic, RDFS.comment, Literal("This property relates the cultural asset to the analysis of its topics.", lang="en")))

	ont = g.serialize(format='turtle').decode("utf-8")
	return ont

def expressiveDescription():
	# Expressive Detection
	g.add((arcoSD.ExpressiveDescription, RDF.type, OWL.Class))
	g.add((arcoSD.ExpressiveDescription, RDFS.comment, Literal("This class represents a reading of the work in an expressive key. The cultural asset is analyzed from the point of view of the technical components designed to convey its meaning (i.e. colour, lights and shadows).", lang="en")))
	
	g.add((arcoSD.hasColour, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasColour, RDFS.domain, arcoSD.ExpressiveDescription))
	g.add((arcoSD.hasColour, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasColour, RDFS.comment, Literal("This property relates the cultural asset to the analysis of the main colours that compose it.", lang="en")))
	
	g.add((arcoSD.hasLights, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasLights, RDFS.domain, arcoSD.ExpressiveDescription))
	g.add((arcoSD.hasLights, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasLights, RDFS.comment, Literal("This property relates the cultural asset to the analysis of the lights and shadows that compose it.", lang="en")))
	
	ont = g.serialize(format='turtle').decode("utf-8")
	return ont

def denotativeDescription():
	# Denotative description
	g.add((arcoSD.Iconic, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Iconic,RDF.type,arcoSD.DenotativeTypeDefinition))
	g.add((arcoSD.Iconic, RDFS.comment, Literal("This individual represents a high figurative gradualness of the painting.", lang="en")))

	g.add((arcoSD.Figurative, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Figurative,RDF.type,arcoSD.DenotativeTypeDefinition))
	g.add((arcoSD.Figurative, RDFS.comment, Literal("This individual represents a medium figurative gradualness of the painting.", lang="en")))

	g.add((arcoSD.Abstract, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Abstract,RDF.type,arcoSD.DenotativeTypeDefinition))
	g.add((arcoSD.Abstract, RDFS.comment, Literal("This individual represents a low figurative gradualness of the painting.", lang="en")))

	g.add((arcoSD.Symmetrical, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Symmetrical,RDF.type,arcoSD.ElementsRelationshipsType))
	g.add((arcoSD.Symmetrical, RDFS.comment, Literal("This individual represents a symmetrically organized cultural asset. Therefore the work of art is linked to the concepts of order, clarity, balance and stability.", lang="en")))

	g.add((arcoSD.Asymmetrical, RDF.type, OWL.NamedIndividual))
	g.add((arcoSD.Asymmetrical,RDF.type,arcoSD.ElementsRelationshipsType))
	g.add((arcoSD.Asymmetrical, RDFS.comment, Literal("This individual represents an asymmetrically organized cultural asset. A more natural effect is therefore sought in the work, capable of capturing the nuances of the movements of the figures or human moods.", lang="en")))

	g.add((arcoSD.DenotativeDescription, RDF.type, OWL.Class))
	g.add((arcoSD.DenotativeDescription, RDFS.comment, Literal("This class represents a first reading of the cultural asset based on the descriptive analysis of the elements that compose it (i.e. scene, denotative type, subject).", lang="en")))

	g.add((arcoSD.DenotativeTypeDefinition, RDF.type, OWL.Class))
	g.add((arcoSD.DenotativeTypeDefinition, RDFS.subClassOf, arcoSD.DenotativeDescription))
	g.add((arcoSD.DenotativeTypeDefinition, RDFS.comment, Literal("This class groups together the typology related to a denotative description of a cultural asset (figurative, iconic or abstract).", lang="en")))

	g.add((arcoSD.ElementsRelationshipsType, RDF.type, OWL.Class))
	g.add((arcoSD.ElementsRelationshipsType, RDFS.subClassOf, arcoSD.ElementRelationships))
	g.add((arcoSD.ElementsRelationshipsType, RDFS.comment, Literal("This class groups the typology related to a relational description of the elements that make up a cultural asset. It can be symmetrical or asymmetrical.", lang="en")))

	g.add((arcoSD.hasDenotativeTypeDefinition, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasDenotativeTypeDefinition, RDFS.domain, arcoSD.DenotativeDescription))
	g.add((arcoSD.hasDenotativeTypeDefinition, RDFS.range, arcoSD.DenotativeTypeDefinition))
	g.add((arcoSD.hasDenotativeTypeDefinition, OWL.inverseOf, arcoSD.isDenotativeTypeDefinitionOf))
	g.add((arcoSD.hasDenotativeTypeDefinition, RDFS.comment, Literal("This property represents the description of the typology of the cultural asset based on a denotative reading (iconic, figurative, abstract).", lang="en")))

	g.add((arcoSD.isDenotativeTypeDefinitionOf, RDFS.domain, arcoSD.DenotativeTypeDefinition))
	g.add((arcoSD.isDenotativeTypeDefinitionOf, RDFS.range, arcoSD.DenotativeDescription))
	g.add((arcoSD.isDenotativeTypeDefinitionOf, OWL.inverseOf, arcoSD.hasDenotativeTypeDefinition))
	g.add((arcoSD.isDenotativeTypeDefinitionOf, RDFS.comment, Literal("This is the inverse property of 'has denotative type definition'.", lang="en")))

	g.add((arcoSD.hasScene, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasScene, RDFS.domain, arcoSD.DenotativeDescription))
	g.add((arcoSD.hasScene, RDFS.range, arcoSD.Scene))
	g.add((arcoSD.hasScene, OWL.inverseOf, arcoSD.isSceneOf))
	g.add((arcoSD.hasScene, RDFS.comment, Literal("This property relates a cultural asset to the scene it represents.", lang="en")))

	g.add((arcoSD.isSceneOf, RDFS.domain, arcoSD.Scene))
	g.add((arcoSD.isSceneOf, RDFS.range, arcoSD.DenotativeDescription))
	g.add((arcoSD.isSceneOf, OWL.inverseOf, arcoSD.hasScene))
	g.add((arcoSD.isSceneOf, RDFS.comment, Literal("This property relates the scene with the related cultural asset.", lang="en")))

	g.add((arcoSD.Scene, RDF.type, OWL.Class))
	g.add((arcoSD.Scene, RDFS.subClassOf, arcoSD.DenotativeDescription))
	g.add((arcoSD.Scene, RDFS.comment, Literal("This class indicates the episode represented by the cultural asset.", lang="en")))

	g.add((arcoSD.hasDescriptionScene, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasDescriptionScene, RDFS.domain, arcoSD.Scene))
	g.add((arcoSD.hasDescriptionScene, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasDescriptionScene, RDFS.comment, Literal("This property represents the description of the scene as it is shown by the cultural asset.", lang="en")))

	g.add((arcoSD.hasEnvironment, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasEnvironment, RDFS.domain, arcoSD.Scene))
	g.add((arcoSD.hasEnvironment, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasEnvironment, RDFS.comment, Literal("This property makes explicit the environmental references linked to the description of the scene.", lang="en")))

	g.add((arcoSD.hasComposition, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasComposition, RDFS.domain, arcoSD.DenotativeDescription))
	g.add((arcoSD.hasComposition, RDFS.range, arcoSD.Composition))
	g.add((arcoSD.hasComposition, OWL.inverseOf, arcoSD.isCompositionOf))
	g.add((arcoSD.hasComposition, RDFS.comment, Literal("This property relates a cultural asset to the class that indicates its composition.", lang="en")))

	g.add((arcoSD.isCompositionOf, RDFS.domain, arcoSD.Composition))
	g.add((arcoSD.isCompositionOf, RDFS.range, arcoSD.DenotativeDescription))
	g.add((arcoSD.isCompositionOf, OWL.inverseOf, arcoSD.hasComposition))
	g.add((arcoSD.isCompositionOf, RDFS.comment, Literal("This property relates the class that indicates a cultural asset’s composition with the related work of art.", lang="en")))

	g.add((arcoSD.Composition, RDF.type, OWL.Class))
	g.add((arcoSD.Composition, RDFS.subClassOf, arcoSD.DenotativeDescription))
	g.add((arcoSD.Composition, RDFS.comment, Literal("This class represents the spatial organization of the cultural asset. The work of art is therefore linked to the analysis of its visual elements (i.e. subject, foreground element, background element).", lang="en")))

	g.add((arcoSD.hasSubject, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasSubject, RDFS.domain, arcoSD.Composition))
	g.add((arcoSD.hasSubject, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasSubject, RDFS.comment, Literal("This property describes the subject of 'CulturalProperty'.", lang="en")))

	g.add((arcoSD.hasElementsComposition, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasElementsComposition, RDFS.domain, arcoSD.Composition))
	g.add((arcoSD.hasElementsComposition, RDFS.range, arcoSD.ElementsComposition))
	g.add((arcoSD.hasElementsComposition, OWL.inverseOf, arcoSD.isElementsCompositionOf))
	g.add((arcoSD.hasElementsComposition, RDFS.comment, Literal("The property links the class which indicates the generic composition of the cultural asset with the specific class which makes explicit the division between its elements.", lang="en")))

	g.add((arcoSD.isElementsCompositionOf, RDFS.domain, arcoSD.ElementsComposition))
	g.add((arcoSD.isElementsCompositionOf, RDFS.range, arcoSD.Composition))
	g.add((arcoSD.isElementsCompositionOf, OWL.inverseOf, arcoSD.hasElementsComposition))
	g.add((arcoSD.isElementsCompositionOf, RDFS.comment, Literal("This is the inverse property of 'has element composition'.", lang="en")))

	g.add((arcoSD.ElementsComposition, RDF.type, OWL.Class))
	g.add((arcoSD.ElementsComposition, RDFS.subClassOf, arcoSD.Composition))
	g.add((arcoSD.ElementsComposition, RDFS.comment, Literal("This class represents a classification of the elements that make up the cultural property according to their spatial arrangement (foreground and background elements).", lang="en")))

	g.add((arcoSD.hasForegroundElements, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasForegroundElements, RDFS.domain, arcoSD.ElementsComposition))
	g.add((arcoSD.hasForegroundElements, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasForegroundElements, RDFS.comment, Literal("This property describes the foreground elements that are part of the cultural asset.", lang="en")))

	g.add((arcoSD.hasBackgroundElements, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasBackgroundElements, RDFS.domain, arcoSD.ElementsComposition))
	g.add((arcoSD.hasBackgroundElements, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasBackgroundElements, RDFS.comment, Literal("This property describes the background elements that are part of the cultural asset.", lang="en")))

	g.add((arcoSD.hasRelationsComposition, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasRelationsComposition, RDFS.domain, arcoSD.Composition))
	g.add((arcoSD.hasRelationsComposition, RDFS.range, arcoSD.RelationsComposition))
	g.add((arcoSD.hasRelationsComposition, OWL.inverseOf, arcoSD.isRelationsCompositionOf))
	g.add((arcoSD.hasRelationsComposition, RDFS.comment, Literal("The property links the class which indicates the generic composition of the cultural asset with the specific class which describes the relationships between the various components of the work.", lang="en")))

	g.add((arcoSD.isRelationsCompositionOf, RDFS.domain, arcoSD.RelationsComposition))
	g.add((arcoSD.isRelationsCompositionOf, RDFS.range, arcoSD.Composition))
	g.add((arcoSD.isRelationsCompositionOf, OWL.inverseOf, arcoSD.hasRelationsComposition))
	g.add((arcoSD.isRelationsCompositionOf, RDFS.comment, Literal("This is the inverse property of 'has relation composition'.", lang="en")))

	g.add((arcoSD.RelationsComposition, RDF.type, OWL.Class))
	g.add((arcoSD.RelationsComposition, RDFS.subClassOf, arcoSD.Composition))
	g.add((arcoSD.RelationsComposition, RDFS.comment, Literal("This class describes the relationships between the various components of the work (i.e. elements composition, study of perspective).", lang="en")))

	g.add((arcoSD.hasPerspectiveStudy, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasPerspectiveStudy, RDFS.domain, arcoSD.RelationsComposition))
	g.add((arcoSD.hasPerspectiveStudy, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasPerspectiveStudy, RDFS.comment, Literal("This property relates the cultural asset to the analysis of the perspective elements that compose it.", lang="en")))

	g.add((arcoSD.hasElementRelationships, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasElementRelationships, RDFS.domain, arcoSD.RelationsComposition))
	g.add((arcoSD.hasElementRelationships, RDFS.range, arcoSD.ElementRelationships))
	g.add((arcoSD.hasElementRelationships, OWL.inverseOf, arcoSD.isElementRelationshipsOf))
	g.add((arcoSD.hasElementRelationships, RDFS.comment, Literal("The property links the class which indicates the generic composition of the cultural asset with the specific class which makes explicit the relationship between its elements.", lang="en")))

	g.add((arcoSD.isElementRelationshipsOf, RDFS.domain, arcoSD.ElementRelationships))
	g.add((arcoSD.isElementRelationshipsOf, RDFS.range, arcoSD.RelationsComposition))
	g.add((arcoSD.isElementRelationshipsOf, OWL.inverseOf, arcoSD.hasElementRelationships))
	g.add((arcoSD.isElementRelationshipsOf, RDFS.comment, Literal("This is the inverse property of 'has elements relationships'.", lang="en")))

	g.add((arcoSD.ElementRelationships, RDF.type, OWL.Class))
	g.add((arcoSD.ElementRelationships, RDFS.subClassOf, arcoSD.RelationsComposition))
	g.add((arcoSD.ElementRelationships, RDFS.comment, Literal("This class describes the relationships between the elements that make up the cultural good (e.g. relationship between main and secondary characters, relationship between characters and environment, connections between foreground and background elements).", lang="en")))

	g.add((arcoSD.hasElementRelationshipsType, RDF.type, OWL.ObjectProperty))
	g.add((arcoSD.hasElementRelationshipsType, RDFS.domain, arcoSD.ElementRelationships))
	g.add((arcoSD.hasElementRelationshipsType, RDFS.range, arcoSD.ElementsRelationshipsType))
	g.add((arcoSD.hasElementRelationshipsType, OWL.inverseOf, arcoSD.isElementRelationshipsTypeOf))
	g.add((arcoSD.hasElementRelationshipsType, RDFS.comment, Literal("This property describes the typology of the cultural asset based on its visual components and its expressive meaning. The work can be symmetrical (related to the concepts of order, clarity, balance and stability) or asymmetrical.", lang="en")))

	g.add((arcoSD.isElementRelationshipsTypeOf, RDFS.domain, arcoSD.ElementsRelationshipsType))
	g.add((arcoSD.isElementRelationshipsTypeOf, RDFS.range, arcoSD.ElementRelationships))
	g.add((arcoSD.isElementRelationshipsTypeOf, OWL.inverseOf, arcoSD.hasElementRelationshipsType))
	g.add((arcoSD.isElementRelationshipsTypeOf, RDFS.comment, Literal("This is the inverse property of 'has element relationship type'.", lang="en")))

	ont = g.serialize(format='turtle').decode("utf-8")
	return ont


#CULTURAL MOVEMENT AS CLASS WILL BE IMPLEMENTED LATER
def culturalMovement():
	#Cultural Movement
	'''
	g.add((arcoSD.CulturalMovement, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.CulturalMovement, RDFS.comment, Literal("This class represents the cultural movement to which the cultural asset is linked (i.e. Renaissance, Gotic).", lang="en")))

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

	g.add((arcoSD.hasStartDate, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasStartDate, RDFS.domain, arcoSD.CulturalMovement))
	g.add((arcoSD.hasStartDate, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasStartDate, RDFS.comment, Literal("This property tells us the start date of a movement.", lang="en")))

	g.add((arcoSD.hasEndDate, RDF.type, OWL.DatatypeProperty))
	g.add((arcoSD.hasEndDate, RDFS.domain, arcoSD.CulturalMovement))
	g.add((arcoSD.hasEndDate, RDFS.range, RDFS.Literal))
	g.add((arcoSD.hasEndDate, RDFS.comment, Literal("This property tells us the end date of a movement.", lang="en")))
'''
		
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
	saveToFile(complete, TAXONOMY_FILE)

def addToOntology(resource):
	for key, value in resource.items():
		if (key == "resource"):
			res = URIRef(value)
			g.add((res, RDF.type, arco.CulturalProperty))
		if (key == "hasSubject"):
			hasSubject = value
			g.add((res, arcoSD.hasSubject, Literal(hasSubject)))
		if (key == "hasWikiDescription"):
			hasWikiDescription = value
			g.add((res, arcoSD.hasWikiDescription, Literal(hasWikiDescription)))
		if (key == "hasCulturalMovement"):
			hasCulturalMovement = value
			# As 'hasCulturalMovement' is only a property - up to this moment - it only takes a Literal
			g.add((res, arcoSD.hasCulturalMovement, Literal(hasCulturalMovement)))
		if (key == "hasPerspectiveStudy"):
			hasPerspectiveStudy = value
			g.add((res, arcoSD.hasPerspectiveStudy, Literal(hasPerspectiveStudy)))
		if (key == "hasBackgroundElement"):
			hasBackgroundElement = value
			g.add((res, arcoSD.hasBackgroundElement, Literal(hasBackgroundElement)))
		if (key == "hasForegroundElement"):
			hasForegroundElement = value
			g.add((res, arcoSD.hasForegroundElement, Literal(hasForegroundElement)))
		if (key == "hasLights"):
			hasLights = value
			g.add((res, arcoSD.hasLights,Literal(hasLights)))
		if (key == "hasColour"):
			hasColour = value
			g.add((res, arcoSD.hasColour,Literal(hasColour)))
		if (key == "hasTopic"):
			hasTopic = value
			g.add((res, arcoSD.hasTopic,Literal(hasTopic)))
		if (key == "scene"):
			scene = value
			g.add((res, arcoSD.hasDescriptionScene, Literal(scene)))
		if (key == "environment"):
			environment = value
			g.add((res, arcoSD.hasEnvironment, Literal(environment)))
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

def buildAuthorInfo():
	ontologyIRI = URIRef("https://domain/smartology/semiotic-description")
	# Add Ontology IRI
	g.add((ontologyIRI, RDF.type, OWL.Ontology))
	g.add((ontologyIRI, OWL.versionIRI, URIRef("https://domain/smartology/semiotic-description/1.1"))) 
	g.add((ontologyIRI, DC.creator, Literal("Antonio Picone")))
	g.add((ontologyIRI, DC.creator, Literal("Luana Bulla")))
	g.add((ontologyIRI, DC.creator, Literal("Luca Failla")))
	g.add((ontologyIRI, DC.title, Literal("Semiotic Description Ontology (Smartology network)", lang="en")))
	g.add((ontologyIRI, RDFS.label, Literal("Semiotic Description Ontology (Smartology network)", lang="en")))

def main():
	if (BUILD_TAXONOMY):
		buildAuthorInfo()
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
		g.parse("{}.owl".format(TAXONOMY_FILE), format="xml")
		for resource in dataToBeAdded:
			addToOntology(resource)
		saveToFile(g.serialize(format='turtle').decode("utf-8"), "test")


if __name__ == "__main__":
	main()

