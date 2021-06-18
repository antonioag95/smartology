# Smartology 
### Semiotic Description Ontology (Smartology network)
Il progetto Smartology si pone l’obiettivo di raggiungere un’ottimizzazione del processo di automatizzazione in campo ontologico tramite strumenti di intelligenza artificiale.
L’unione tra questi due ambiti ha portato all’ideazione e alla creazione di un tool capace di estrarre, analizzare e trattare dati testuali non strutturati. Tale processo è finalizzato al recupero di informazioni pertinenti che possano implementare la descrizione di una risorsa all’interno di un’ontologia già strutturata.
Smartology vede inoltre al suo interno una sezione parallela interamente dedicata alla modellazione di una nuova ontologia: Semiotic Description Ontology. Quest’ultima è stata strutturata ai fini di una futura implementazione dell’esistente rete semantica chiamata [_ArCo_](http://wit.istc.cnr.it/arco) (Architetture della Conoscenza). Attualmente, ArCo fornisce utili informazioni in merito alla classificazione e alla registrazione dei beni culturali italiani ma non contempla al suo interno la loro analisi interpretativa. A seguito di un’accurata fase di studio e analisi, Semiotic Description Ontology provvede a donare un modello strutturato in grado di accogliere e ordinare dati testuali appartenenti alla semantica di un’opera d’arte. 
Data la mancanza di esperti di dominio in grado di fornire informazioni che potessero implementare lo scheletro da noi ideato, abbiamo deciso di testare il tool sopra presentato direttamente sull’ontologia creata.

### Interrogazione di ArCo
Al fine di estrarre dati da ArCo e ottenere un collegamento con le risorse contenute in esso, è stato generato il codice chiamato [data_extraction](https://github.com/antonioag95/smartology/blob/main/data_extraction.py). 
Tramite l’utilizzo della libreria _SPARQLWrapper_ è stato possibile interrogare il grafo sopramenzionato ed ottenere informazioni dettagliate sui beni culturali al suo interno. Genericamente, il codice può essere adattato a query differenti. Tuttavia, ai fini del funzionamento del processo da noi ideato, è stato necessario estrarre le informazioni associate alle proprietà sotto menzionate: 

- _rdfs:label_: etichetta attribuita all’opera
- _a-cd:hasAuthor_: l’autore del bene culturale
- _dc:description_: la descrizione del bene culturale fornita dai catalogatori
- _a-cd:historicalInformation_: le informazioni storiche associate ad ogni risorsa
- l'uri corrispondente alla risorsa

Al fine di evitare la duplicazione dei risultati ottenuti, sarebbe preferibile applicare i costrutti _SAMPLE_ e _GROUP BY_ all’interrogazione sottoposta. Tuttavia, a causa di un rallentamento dell’endpoint durante il processamento di query complesse, è stato necessario semplificare la costruzione della query e operare un’eliminazione delle risorse duplicate direttamente da codice. 
In ultima analisi, il codice è abilitato allo scorrimento della paginazione tramite l’implementazione automatica dei costrutti _LIMIT_ e _OFFSET_. Questo meccanismo permette di estrarre la totalità dei dati rispondenti alla query sottoposta.
Al fine del processo di estrazione, i dati restituiti originariamente in formato JSON, sono processati e organizzati in un DataFrame che permette il loro utilizzo per le fasi successive del processo.
L’interrogazione diretta dello Sparql Endpoint utilizzato è possibile al seguente link.


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
Una volta ultimata la fase di estrazione, è stato possibile elaborare e analizzare i dati ottenuti tramite l’applicazione di modelli di machine learning. Nello specifico, sono stati eseguiti task di _Question answering (QA)_ e di _Text summarization_: con il primo, l'IA è in grado di rispondere a domande, espresse attraverso l'uso del linguaggio naturale; con il secondo, invece, è possibile formulare dei riassunti di testi in maniera automatica. 
Inoltre, il modello di Text Summarization è stato implementato in una funzione che ne permette un uso alternativo e innovativo. 
Dato un testo libero, la funzione denominata _hasLiteral_ è in grado di estrarre informazioni in base a una determinata parola chiave. Una volta estrapolato il periodo contenente il termine prescelto, le frasi vengono raggruppate ed elaborate attraverso un processo di sintesi durante il quale è applicata una correzione grammaticale al fine di rendere la risposta semanticamente e sintatticamente corretta.
Tale processo è finalizzato al recupero di informazioni pertinenti che possano implementare la descrizione di una risorsa all’interno di un’ontologia già strutturata.
Per visionare la classe che racchiude i modelli scelti e le funzioni che ne permettono il funzionamento, si veda il codice [Bert_Text Processing.py](https://github.com/antonioag95/smartology/blob/main/Bert_Text%20Processing.py). Per visionare la funzione hasLiteral si rimanda al codice [final_execution.py](https://github.com/antonioag95/smartology/blob/main/final_execution.py).
Il tool è stato attualmente testato prendendo in input le informazioni estratte da ArCo e Wikipedia e implementando in output alcuni tra i letterali presenti nell’ontologia _Semiotic Description Ontology_. 
Il caso studio riportato, il cui esito è possibile visionare nel seguente [Bert-smartology.ttl](https://github.com/antonioag95/smartology/blob/main/Bert-smartology.ttl), comprende l’implementazione delle informazioni ascrivibili a due rinomati beni culturali: il _Tondo Doni_ e il _David_, entrambi attribuibili a _Michelangelo Buonarroti_. 



### Modellazione dell'ontologia
Un’analisi preliminare in seno al dominio dei beni culturali è stata condotta al fine di orientare la nostra ricerca e strutturare una modellazione pertinente ed accurata. 
In questa fase di lavoro, è stata essenziale la comprensione della metodologia tradizionalmente adoperata per interpretare il messaggio di un’opera d’arte. Inoltre, al fine di consolidare l’accuratezza dello schema di modellazione, sono state prese in considerazione anche le domande più frequentemente poste dalle persone nei confronti di un bene culturale (ad esempio, interrogazioni contestuali o interpretative).
Lo schema di modellazione si articola in cinque parti:

- _Denotative Description_: fornisce una prima lettura del bene culturale basata sull'analisi descrittiva degli elementi che lo compongono (es. scena, tipo denotativo, soggetto).
- _Connotative Description_: fornisce una seconda lettura del bene culturale basata sull'analisi del messaggio e dei temi a cui è associato (es. messaggio, argomento).
- _Expressive Description_: fornisce una lettura dell'opera in chiave espressiva. Il bene culturale viene analizzato dal punto di vista delle componenti tecniche atte a veicolarne il significato (i.e. colore, luci e ombre).
- _Cultural Movement_: parte dell’ongoing work, questa sezione fornirà un approfondimento sul movimento culturale proprio dell’opera d’arte.

Lo schema preliminare di modellazione è visibile al [schema_di_modellazione.pdf](https://github.com/antonioag95/smartology/blob/main/schema_di_modellazione.pdf). 


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
* Costruzione di un sistema che riesca a trovare i sinonimi di alcune _keyword_, questo ci permetterà di estrarre la descrizione da _Wikipedia_ con maggiore certezza; al momento la descrizione dell'opera dall'enciclopedia viene estratta eseguendo lo _scraping_ della prima sezione dopo l'abstract, come anticipato sopra, poiché la maggior parte delle volte la descrizione si trova proprio in quella sezione. Tuttavia, un maggior controllo del contenuto estratto potrebbe portarci ad estrarre il contenuto che ci interessa, quindi non solo la descrizione, con maggiore precisione e controllo.
* L'utilizzo di BERT e l'esecuzione del _task_ di QA ci ha visti costretti a cercare le domande giuste da porre a BERT affinché rispondesse in maniera efficace e concisa, trovare dei sinonimi, anche in questo caso, potrebbe portare a formulare domande che soddisfano il _threshold_ per considerare valide le risposte fornite.
* Implementazione di una classe 'CulturalMovement' che contenga tutti i movimenti culturali in maniera organizzata per quanto riguarda le classi e sottoclassi, è possibile infatti che un determinato movimento culturale sia inglobato da un altro. È possibile visionare la modellazione teorica della classe su questo [schema_di_modellazione.pdf](https://github.com/antonioag95/smartology/blob/main/schema_di_modellazione.pdf).
* Ristrutturazione del codice che gestisce l'estrazione di _feature_ attraverso l'impiego di IA. Al momento non è prevista la parallelizzazione e ciò rende l'esecuzione lenta, con l'impiego del modulo di _threading_ possiamo velocizzare il processo, in vista di un'elaborazione di un quantitativo maggiore di opere.
*  Creare un modello di classificazione per estrarre i letterali che al momento mancano, allenando una rete neurale che funzioni direttamente sulla lingua italiana.

