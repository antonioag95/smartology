# Smartology 
### Semiotic Description Ontology (Smartology network)
In un mondo in cui l'intelligenza artificiale vige in ogni campo, riteniamo che occorra rivoluzionare anche il campo delle ontologie, in particolare, ci occupiamo di estendere l'ontologia pre-esistente di ArCo (Architettura della Conoscenza), un'ontologia tutta italiana che descrive il patrimonio culturale del nostro Paese con dati estratti dal Catalogo Generale dei Beni Culturali. 
In particolare, ArCo, suppur rappresenti un'ontologia ben strutturata, è carente di alcune voci che renderebbero la fruibilità della stessa ontologia utile per i visitatori, ricercatori ed appassionati che la consultano. In seguito ad un sondaggio, infatti, sono state individuate alcune domande su cui la gente si interroga maggiormente quando si trova ad ammirare un'opera culturale. Tra queste domande figurano:

* Cosa rappresenta un'opera?
* Qual è il messaggio che essa vuole trasmettere?

Abbiamo deciso, quindi, di implementare ArCo ed estenderla creando un'ontologia, dopo averne esplorato la composizione, in modo tale da ricalcarne i tratti salienti, colmando però, allo stesso tempo, gli interrogativi di cui sopra. Per portare a termine questo _task_ ci siamo avvalsi di innovativi strumenti di _Intelligenza Artificiale_, che potessero rispondere a _task_ di _Question answering_ (QA) e di _Text summarization_: con il primo, l'IA è in grado di rispondere a domande, espresse attraverso l'uso del linguaggio naturale; con il secondo, invece, è possibile eseguire dei riassunti di testi in maniera automatica, in modo tale che le informazioni saltino subito all'occhio. Per potere alimentare una rete neurale sono necessari dei dati di partenza da raffinare e sui quali lavorare. Ai fini dimostrativi verranno implementate, all'interno della nostra estensione dell'ontologia, due opere e ne verranno analizzati i risultati. Ci occuperemo, in una seconda fase, di capire quali siano le difficoltà incontrate e quali siano le implementazioni future. Tutti questi aspetti verranno affrontati man mano nel corso di questa trattazione. Ovviamente si tratta di un'operazione che può essere eseguita nella sua interezza in maniera manuale, ma i tempi per la realizzazione ed i costi, poiché sono necessari esperti di dominio, sarebbero ingenti. Su ArCo sono presenti infatti milioni di opere che, grazie a questo metodo, possono essere inserite in ontologia in maniera automatica.

### Interrogazione di ArCo
TO DO

### Raccolta dei dati
È innanzitutto necessario occuparci della raccolta dei dati, nel nostro caso dei dati testuali per poter affrontare operazioni di _NLP_ (_Natural Language Processing_). Ricordiamo che l'origine di ogni bene culturale è su ArCo, che rappresenta su quell'ontologia una classe chiamata _CulturalProperty_. Per ricavare dei dati ci serve innanzitutto associare l'opera di ArCo a delle fonti attendibili e libere presenti sul _web_. Abbiamo deciso di utilizzare _Wikipedia_, la nota enciclopedia libera, che mette a disposizione dei programmatori numerose _API_ per la consultazione e gestione dei dati. Una prima difficoltà da incontrare risiede proprio nell'associazione di queste risorse, ArCo infatti non contiene, ovviamente nessun collegamento alla relativa pagina di _Wikipedia_. Per fortuna, quest'ultima mette a disposizione un'interessante _API_ in grado di cercare, date delle _keyword_ ed anche in maniera piuttosto flessibile, all'interno del vastissimo catalogo di risorse messe a disposizione. Ad esempio, se all'interno di ArCo un'opera viene chiamata con il nome de "Cenacolo" avrà la sua corrispondenza su _Wikipedia_ con il nome esatto di "Ultima Cena (Leonardo)", l'API in questione, ricercando non solo nel titolo, ma anche all'interno del contenuto delle voci, riesce ad eseguire queste associazioni.
Una volta che viene identificato il titolo della voce su _Wikipedia_, può essere cercata la relativa ontologia avente quel titolo esatto. L'ontologia di _Wikidata_ viene utilizzata per estrarre il movimento culturale a cui appartiene l'opera, attraverso una semplice _query_ di SPARQL, dove _wd_ secondo l'ontologia di _Wikidata_ rappresenta l'entità e _wdt_ rappresenta la proprietà:
```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX wd: <http://www.wikidata.org/entity/> 
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX bd: <http://www.bigdata.com/rdf#>
		
SELECT ?o ?label WHERE {
			wd wdt ?o .
			?o rdfs:label ?label .
			FILTER (langMatches( lang(?label), "IT" ) )
			SERVICE wikibase:label {
				bd:serviceParam wikibase:language "IT" .
			}
}
```
_Wikidata_ ha un'ontologia un po' anomala, sia le risorse sia le proprietà sono identificate da una URI contenente solamente dei numeri, quindi non sono autoesplicativi. Ad esempio, la proprietà _P135_ rappresenta proprio il "movimento" e l'entità _Q1473546_ rappresenta l'opera "Tondo Doni" di Michelangelo. L'URI dell'entità viene estratta nella fase precedente, attraverso l'uso dell'_API_, dalla quale vengono estratti anche i relativi riferimenti alle pagine di _Wikipedia_ in ogni lingua disponibile: verrà estratto il link della voce in inglese, qualora disponibile, altrimenti in italiano. La scelta della preferenza della lingua inglese della risorsa è dovuta al fatto che i modelli di IA utilizzati sono funzionanti per la lingua inglese, anche se, in futuro, desideriamo implementare un classificatore multiclasse funzionante per la lingua italiana.
Dalla pagina di _Wikipedia_, attraverso la tecnica dello _scraping_ impiegando la libreria _BeautifulSoup_ viene estratta la prima sezione dopo l'abstract, che contiene, nella maggior parte dei casi, proprio la descrizione dell'opera che servirà ad alimentare i meccanismi di IA. È stata anche valutata l'idea di utilizzare _DBpedia_ per facilitare e snellire la procedura ma viene solamente fornito l'abstract presente su Wikipedia, il che sarebbe risultato poco producente e scarno per la quantità di informazioni che ci occorrono.
Il codice di questo processo può essere trovato all'interno del file [smartology.py](https://github.com/antonioag95/smartology/blob/main/smartology.py).

### BERT aka lo Stato dell'arte dell'NLP
TO DO

### Modellazione dell'ontologia
TO DO

### Generazione della tassonomia
Una volta definita la modellazione della nostra ontologia, occorre che venga implementata. Anche in questo caso, abbiamo preferito costruire la tassonomia da codice, è stata utilizzata infatti la libreria _RDFLib_, grazie alla quale, attraverso l'_import_ dei _namespace_ predefiniti di RDF, RDFS ed OWL e la scrittura delle triple è stata costruita l'ontologia. Abbiamo definito, inoltre, il _namespace_ dell'ontologia da noi creata:
```
arcoSD = Namespace("https://domain/smartology/semiotic-description/")
```
Le righe di codice per portare a termine la costruzione dell'ontologia con la sola presenza delle risorse di base tra classi e proprietà sono circa 450. Le classi, le sottoclassi, le proprietà e le relative inverse, il _range_ ed il dominio sono state definite, con semplici triple, vediamone insieme un esempio:
```
g.add((arcoSD.ExpressiveDescription, RDF.type, OWL.Class))
g.add((arcoSD.ExpressiveDescription, RDFS.subClassOf, arcoSD.SemioticDescription))
```
Al termine della sua costruzione, la stessa è stata importata su _Protégé_ e salvata in formato RDF/XML per poi essere caricata su _[**L**ive  **O**WL  **D**ocumentation  **E**nvironment](http://www.github.com/essepuntato/LODE)_ (_LODE_), un _tool_ che riesce ad estrarre automaticamente classi, _object properties_, _data properties_ e _individuals_ dall'ontologia generata per crearne una documentazione di riferimento, la cui leggibilità è semplice ed immediata. Una copia della documentazione, che includono i commenti per ogni elemento, può essere [consultata qui](http://150.146.207.114/lode/extract?url=https%3A%2F%2Fraw.githubusercontent.com%2Fantonioag95%2Fsmartology%2Fmain%2Fsmartology.owl%3Ftoken%3DAHJEFQVNJGTXGNHUQPJMM2DA2OBTY&owlapi=true&lang=en).
È possibile importare ed effettuare il _parsing_ di un'ontologia pre-esistente o comunque precedentemente salvata, utile nel caso in cui si debbano apportare delle modifiche alla stessa. Per aggiungere le triple corrette, in seguito alle elaborazioni descritte sopra si è pensato di definire una lista di dizionario contenenti delle chiavi specifiche che verranno riconosciute, ad esempio:
```
[
		{
			"resource": "https://w3id.org/arco/resource/HistoricOrArtisticProperty/0900287181",
			"hasSubject": "The child Jesus, Mary, and Joseph",
			"scene": "The Holy Family",
			"environment": "The scene appears to be a rural one",
			"hasForegroundElement": "The Holy Family",
			"hasBackgroundElement": "Five Nudes",
			"hasPerspectiveStudy": "The exedra where the naked in the background reside lies on a different perspective surface and with a lower vanishing point compared to the laying surface of the main figures and the low wall under Joseph, which has the task of concealing the gap.",
			"hasDescriptionRelations": "Mary is the most prominent figure in the composition, taking up much of the center of the image. Joseph is positioned higher in the image than Mary, although this is an unusual feature in compositions of the Holy Family. Mary is seated between his legs, as if he is protecting her, his great legs forming a kind of de facto throne. Saint John the Baptist is in the middle-ground of the painting, between the Holy Family and the background.",
			"denotativeTypeDefinition": "Figurative",
			"elementsRelationshipsType": "Symmetrical",
			"hasSource": "Wikipedia",
			"hasTopic": "Holy Family"
		}
]
```
Man mano verranno implementate altre _keywords_, si consiglia di visionare  il file [builder.py](https://github.com/antonioag95/smartology/blob/main/builder.py) per visionare tutte le proprietà che è possibile implementare nell'ontologia e per visionare maggiori esempi su come essa è stata costruita.

### Ongoing work
TO DO

