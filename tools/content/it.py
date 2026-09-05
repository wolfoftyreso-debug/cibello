"""Contenuti in italiano per tools/build_lang.py. Struttura: vedi _schema.py."""

LANG = "it"

# ---------------------------------------------------------------------------
# Le tre guide (percorsi esistenti, con hreflang). Ordine: pianificatore, ricette, spreco.
# ---------------------------------------------------------------------------
GUIDES = {
    "/it/pianificatore-pasti/": dict(
        title="Pianificatore pasti e menu settimanale | Cibello",
        desc="Come costruire un menu settimanale partendo da ciò che hai in casa: varietà, alimenti freschi usati per primi e una lista della spesa condivisa.",
        eyebrow="Una settimana pianificata con calma",
        h1="Pianificatore pasti: un menu settimanale che parte dalla tua cucina",
        lead="Un menu settimanale non deve essere un programma rigido né sette ricette nuove. Cibello ti propone una settimana costruita su ciò che hai in frigo, in freezer e in dispensa, che tu controlli e modifichi prima di fare la spesa.",
        sections=[
            ("Perché un menu settimanale semplifica tutto", """<p>Alle cinque del pomeriggio la domanda «cosa mangiamo stasera?» pesa più della cottura in sé. Decidere ogni giorno da zero significa aprire il frigo senza un’idea, fare un salto al supermercato per una cosa sola e tornare con quattro, e scoprire il venerdì che le zucchine comprate lunedì non ce l’hanno fatta. Un menu settimanale sposta quella decisione in un momento tranquillo, una volta sola, e trasforma sette scelte separate in un unico sguardo d’insieme.</p><p>Non serve una pianificazione perfetta. Serve un punto di partenza realistico: cosa c’è già in casa, quante sere avete davvero tempo di cucinare e cosa piace alle persone che si siedono a tavola. Cibello parte proprio da lì.</p>"""),
            ("Varietà senza complicazioni", """<p>Un piano fatto in automatico non dovrebbe proporre la stessa pasta a pranzo e a cena, né ripetere il pollo tre giorni di fila. Cibello alterna piatti, ingredienti principali e tipi di pasto, così la settimana resta varia senza che tu debba controllare ogni combinazione. Le proposte tengono conto di ciò che avete in casa, di ciò che va consumato presto e dei gusti della famiglia, e spiegano sempre il perché di ogni scelta.</p><p>Il menu è una bozza: puoi accettarlo com’è, spostare un piatto a un altro giorno, cancellarne uno o inserire una ricetta di famiglia che non è nell’app. Se cerchi idee per riempire le caselle vuote, la guida <a href="/it/ricette-con-ingredienti/">ricette con quello che hai in casa</a> spiega come l’app ordina le proposte in base alla tua dispensa.</p>"""),
            ("Usa gli alimenti nell’ordine giusto", """<p>Gli alimenti freschi meritano un posto a inizio settimana. Se l’inventario è collegato al piano, è più facile mettere il pesce e l’insalata al lunedì e lasciare pasta, legumi e surgelati per i giorni in cui la spesa è lontana. Cibello sa cosa hai e dove si trova, e ti avvisa con un promemoria gentile prima che qualcosa vada a male. Questo riduce sia gli acquisti impulsivi sia gli sprechi silenziosi in fondo al frigo. Per approfondire, leggi <a href="/it/ridurre-spreco-alimentare/">come ridurre lo spreco alimentare in casa</a>.</p>"""),
            ("Un menu settimanale per la famiglia", """<p>Un menu per una famiglia non vuol dire sette ricette nuove. Una settimana che regge nel tempo si costruisce di solito con qualche piatto collaudato, una o due idee nuove e spazio per gli avanzi. Un esempio di struttura, da adattare alle vostre abitudini:</p><table><thead><tr><th>Giorno</th><th>Tipo di pasto</th><th>Perché</th></tr></thead><tbody><tr><td>Lunedì</td><td>Piatto con gli alimenti più freschi</td><td>Pesce, verdure a foglia e latticini aperti si usano prima</td></tr><tr><td>Martedì e mercoledì</td><td>Piatti collaudati</td><td>Veloci da preparare, piacciono a tutti</td></tr><tr><td>Giovedì</td><td>Una ricetta nuova</td><td>Un po’ di varietà senza stravolgere la settimana</td></tr><tr><td>Venerdì</td><td>Svuota-frigo</td><td>Avanzi e box pasti già presenti nell’inventario</td></tr><tr><td>Weekend</td><td>Più tempo e più calma</td><td>Una cottura lunga, o qualcosa da condividere</td></tr></tbody></table><p>Nell’app inserisci i pasti giorno per giorno, vedi quali ingredienti sono già in casa e raccogli il resto nella lista della spesa. Gli avanzi, se li registri come box pasti, restano visibili nell’inventario e possono essere considerati nelle proposte.</p>"""),
            ("Dal piano alla lista della spesa", """<p>Quando il menu è pronto, la lista della spesa raccoglie solo ciò che manca davvero. Niente doppioni di passata di pomodoro, niente terza confezione di riso. La lista è condivisa con la famiglia, durante il periodo di prova e poi con un piano a pagamento: chi passa al supermercato vede la stessa lista di chi ha pianificato e può aggiungere a mano ciò che serve.</p><p>Una cosa resta sempre a carico tuo: controllare ingredienti e confezioni, soprattutto in caso di allergie o intolleranze. I filtri per allergeni sono un aiuto, non una garanzia.</p>"""),
            ("Un piano che cambia con te", """<p>Il menu settimanale è un appoggio, non un obbligo. Cambiano i turni, arriva un invito a cena, qualcuno non ha fame: sposta i giorni, cancella un piatto, aggiungi i tuoi preferiti. Più l’inventario e la lista restano aggiornati, magari con una foto dello scontrino dopo la spesa, più le proposte della settimana successiva saranno centrate.</p><p>Cibello è pensato per adulti e si prova gratis per 14 giorni, senza carta. Se vuoi vedere come funziona nel suo insieme, parti dalla <a href="/it/">pagina principale in italiano</a>.</p>"""),
        ],
        faq=[
            ("Cibello può creare un menu settimanale in automatico?", "Sì. L’app propone una settimana basata su ciò che hai in casa, su ciò che va consumato presto e sui gusti della famiglia. Tu controlli la proposta e la modifichi prima di salvarla."),
            ("Il menu tiene conto di ciò che ho già in frigo e in dispensa?", "Sì. L’inventario che hai verificato è la base delle proposte, così gli alimenti che avete già vengono usati prima di comprarne di nuovi."),
            ("Posso modificare un pasto già pianificato?", "Certo. Il piano è una bozza: puoi spostare, sostituire o cancellare qualsiasi pasto e aggiungere ricette che non sono nell’app."),
            ("Tutta la famiglia vede lo stesso menu?", "Sì. Durante la prova, e poi con un piano a pagamento, la famiglia condivide inventario, menu e lista della spesa."),
        ],
    ),
    "/it/ricette-con-ingredienti/": dict(
        title="Ricette con quello che hai in casa | Cibello",
        desc="Cosa cucinare stasera con quello che c’è in frigo: Cibello riconosce i prodotti da una foto, ordina oltre 9.000 ricette e mostra cosa manca.",
        eyebrow="Cosa cucino stasera?",
        h1="Ricette con gli ingredienti che hai già in casa",
        lead="Fotografa frigo, freezer e dispensa e trasforma quello che c’è in idee concrete per la cena. Cibello ordina le ricette in base a quanto hai già in casa, ti mostra cosa manca e ti spiega perché ti propone proprio quel piatto.",
        sections=[
            ("Parti dal frigo, non dal ricettario", """<p>La maggior parte delle app di ricette funziona al contrario: prima scegli un piatto, poi scopri che ti mancano tre ingredienti su otto. Alle sette di sera questo significa un giro extra al supermercato o una rinuncia. Cibello ribalta l’ordine: parte da quello che hai davvero in casa, che si tratti di mezza confezione di ricotta, due uova e un po’ di spinaci, e ti mostra cosa puoi cucinare con quello.</p><p>La domanda «cosa cucino stasera con quello che ho?» trova così una risposta concreta, senza dover scorrere decine di ricette che non c’entrano nulla con la tua cucina.</p>"""),
            ("Dalla foto all’inventario", """<p>Perché le proposte siano utili, l’app deve sapere cosa c’è in casa. Non serve scrivere ogni prodotto a mano:</p><ol><li><strong>Fotografa</strong> frigo, freezer e dispensa. L’IA riconosce i prodotti e dove si trovano, per esempio il parmigiano nello sportello del frigo.</li><li><strong>Controlla</strong> il risultato prima di salvarlo. L’IA a volte legge male un’etichetta o salta un prodotto nascosto in fondo, quindi correggi nomi, date e quantità.</li><li><strong>Aggiorna</strong> dopo la spesa con una foto dello scontrino o scansionando i codici a barre.</li></ol><p>Il risultato è il tuo Food Twin: un’immagine viva della cucina che resta affidabile finché la tieni aggiornata con piccoli gesti.</p>"""),
            ("Ricette ordinate per quello che hai", """<p>Cibello confronta l’inventario verificato con oltre 9.000 ricette e le ordina in base alla percentuale di ingredienti già disponibili. In cima trovi i piatti che puoi fare subito, con l’indicazione di ciò che eventualmente manca. Le proposte tengono conto anche di ciò che scade presto e di ciò che vi piace, e spiegano sempre il perché: «pollo e panna scadono presto, e ti piacciono i piatti cremosi».</p><p>In pratica, in una serata normale in cima alla lista finiscono una pasta, una frittata, una zuppa di legumi o un risotto con le verdure rimaste. Non ricette da rivista, ma piatti che si possono fare davvero con quello che c’è.</p>"""),
            ("Confezioni aperte, verdure rimaste e avanzi", """<p>Le ricette più utili sono spesso quelle che risolvono un mezzo problema: la ricotta aperta da tre giorni, il mazzo di prezzemolo usato a metà, il riso avanzato dalla cena di ieri. Se questi ingredienti sono nell’inventario, con le date registrate, l’app li mette in evidenza e li fa pesare nelle proposte, così una confezione iniziata diventa il punto di partenza del prossimo piatto invece di finire dimenticata.</p><p>Gli avanzi si registrano come box pasti e restano visibili accanto agli altri alimenti. Un promemoria gentile ti ricorda cosa va usato presto, senza rimproveri: sei tu a decidere se riscaldare, trasformare o congelare.</p>"""),
            ("Proposte che imparano dai vostri gusti", """<p>Con il tempo l’app impara cosa scegliete di solito e cosa lasciate sempre da parte, e adatta le proposte alla famiglia. Puoi indicare allergie, intolleranze e abitudini alimentari, che vengono considerate nelle ricette. Anche qui vale una regola semplice: i filtri sono un’indicazione, non una garanzia. Leggi sempre gli ingredienti e controlla la confezione, soprattutto quando è in gioco la salute di qualcuno. I valori nutrizionali, quando indicati, sono stime utili per pianificare e non un consiglio dietetico.</p>"""),
            ("Dall’idea alla lista della spesa", """<p>Scelta la ricetta, gli ingredienti mancanti possono finire direttamente nella lista della spesa condivisa. L’obiettivo non è farti comprare di più, ma rendere chiaro cosa serve davvero ed evitare i doppi acquisti. La lista è condivisa con la famiglia, durante la prova e poi con un piano a pagamento, e ognuno può aggiungere a mano ciò che manca. Se preferisci ragionare su tutta la settimana invece che su una sera alla volta, la guida al <a href="/it/pianificatore-pasti/">menu settimanale</a> spiega come collegare ricette, piano e spesa in un unico giro.</p>"""),
            ("Decidi sempre tu", """<p>Cibello non decide al posto tuo. Ogni proposta, quantità, data e informazione sugli allergeni va controllata prima di cucinare o salvare. L’app è un supporto che riduce il carico mentale, non un sostituto del buon senso in cucina. Cucinare partendo da quello che hai è anche il modo più semplice per <a href="/it/ridurre-spreco-alimentare/">ridurre lo spreco alimentare</a> senza pensarci troppo.</p><p>Vuoi capire come Cibello si confronta con SuperCook, Samsung Food e altre app di ricette? C’è un <a href="/en/best-recipe-app/">confronto in inglese</a>. Per una panoramica dell’app in italiano, parti dalla <a href="/it/">pagina principale</a>.</p>"""),
        ],
        faq=[
            ("Devo inserire tutti i prodotti a mano?", "No. Fotografa frigo, freezer, dispensa o scontrino, oppure scansiona i codici a barre. Controlli il risultato prima di salvarlo, perché l’IA può sbagliare o saltare un prodotto."),
            ("Cibello propone ricette anche con gli avanzi?", "Sì. Quando avanzi e box pasti sono registrati nell’inventario, possono essere considerati nelle proposte insieme agli altri ingredienti."),
            ("L’app tiene conto delle allergie?", "Puoi indicare allergie e abitudini alimentari, ma il filtro è un’indicazione e non una garanzia. Leggi sempre gli ingredienti e l’etichetta."),
            ("Le ricette sono in italiano?", "L’app è disponibile in 12 lingue, italiano compreso, con testi formulati in modo naturale e non tradotti parola per parola."),
        ],
    ),
    "/it/ridurre-spreco-alimentare/": dict(
        title="Ridurre lo spreco alimentare in casa | Cibello",
        desc="Consigli pratici per ridurre lo spreco alimentare in casa: inventario di frigo e dispensa, promemoria prima della scadenza e ricette con ciò che hai.",
        eyebrow="Meno spreco, senza sensi di colpa",
        h1="Ridurre lo spreco alimentare in casa, senza sensi di colpa",
        lead="Buona parte del cibo che buttiamo è cibo che avevamo semplicemente dimenticato. Con un inventario aggiornato, promemoria gentili e ricette costruite su ciò che hai già, Cibello ti aiuta a usare gli alimenti in tempo. Le decisioni restano tue.",
        sections=[
            ("Che cos’è lo spreco alimentare", """<p>Spreco alimentare è tutto il cibo che si sarebbe potuto mangiare e che invece finisce nella spazzatura: gli avanzi dimenticati in un contenitore, le verdure ammosciate nel cassetto, lo yogurt oltre la data che nessuno ha annusato prima di buttarlo. Una parte importante di questo spreco nasce nelle case, e raramente per cattiva volontà. Il motivo più comune è la mancanza di una visione d’insieme: non sappiamo cosa abbiamo, dove sta e quando va usato.</p><p>Il costo non è solo ambientale. Ogni sacchetto di insalata buttato è denaro speso due volte: una alla cassa e una quando lo si ricompra. Per una famiglia, nell’arco di un anno, sono cifre che si notano.</p><p>È esattamente il punto su cui un inventario di casa e qualche promemoria al momento giusto possono fare la differenza, senza trasformare la cucina in un ufficio.</p>"""),
            ("Vedi cosa rischia di essere dimenticato", """<p>Con una foto di frigo, freezer e dispensa, Cibello riconosce i prodotti e dove si trovano. Se le date sono registrate, l’app ti ricorda con gentilezza cosa va usato presto. Il promemoria non è un rimprovero: è un modo per far tornare in mente il petto di pollo che altrimenti sarebbe scaduto in silenzio.</p><p>Le date e le letture dell’IA possono essere sbagliate, quindi l’ultima parola è tua: guarda, annusa e segui le indicazioni della confezione. Ricorda anche la differenza tra «da consumarsi entro», che riguarda la sicurezza, e «da consumarsi preferibilmente entro», che riguarda la qualità: molti alimenti nella seconda categoria sono ancora buoni per giorni o settimane.</p>"""),
            ("Cucina attorno agli ingredienti, non il contrario", """<p>Invece di comprare un set completo di ingredienti nuovi per ogni ricetta, cerca piatti che usino ciò che hai già. Cibello ordina oltre 9.000 ricette in base a quanto è già disponibile in casa e mette in evidenza ciò che sta per scadere. Le carote un po’ stanche diventano una vellutata, il pane di ieri una panzanella, la mozzarella aperta il condimento di una pasta al forno. Ciò che manca davvero finisce nella lista della spesa. Come funziona nel dettaglio lo spieghiamo nella guida <a href="/it/ricette-con-ingredienti/">ricette con quello che hai in casa</a>.</p>"""),
            ("Pianifica la settimana in base alle scadenze", """<p>Molto spreco si evita a monte, quando si decide cosa cucinare. Un <a href="/it/pianificatore-pasti/">menu settimanale</a> costruito sull’inventario mette gli alimenti freschi nei primi giorni e lascia quelli a lunga conservazione per dopo. Gli avanzi si possono registrare come box pasti nell’inventario, così restano visibili e tornano utili per un pranzo invece di sparire in fondo al frigo. E se un piatto salta, sposti tutto di un giorno senza rifare il piano da zero.</p><p>La lista della spesa che nasce dal piano contiene solo ciò che manca davvero. È il modo più semplice per non comprare la terza confezione di riso o una seconda passata di pomodoro quando la prima è ancora in dispensa.</p>"""),
            ("Piccole abitudini che fanno la differenza", """<ul><li>Guarda il frigo prima di scrivere la lista, non dopo.</li><li>Dopo la spesa fotografa lo scontrino, così l’inventario resta aggiornato senza fatica.</li><li>Tieni un ripiano «da usare prima» dove mettere confezioni aperte e alimenti vicini alla scadenza.</li><li>Congela le porzioni che sai di non riuscire a mangiare entro pochi giorni, con la data scritta sopra.</li><li>Dedica una sera a settimana a un piatto svuota-frigo: frittata, minestra, pasta al forno.</li><li>Compra quantità realistiche: una confezione grande in offerta non è un risparmio se metà finisce nel bidone.</li></ul>"""),
            ("Condividi la panoramica, senza sensi di colpa", """<p>Quando tutta la famiglia vede lo stesso inventario e la stessa lista della spesa, i doppi acquisti diminuiscono e il cibo si usa in tempo. Chi torna a casa per ultimo sa cosa c’è, chi fa la spesa sa cosa manca. Cibello non usa la vergogna né conta le calorie: l’obiettivo è una quotidianità in cucina più calma e più pratica.</p><p>Sei tu a decidere cosa mangiare, cosa congelare e cosa buttare. Controlla sempre data, odore e aspetto, in particolare per i bambini e per chi ha un sistema immunitario indebolito. L’app si prova gratis per 14 giorni senza carta: trovi tutto sulla <a href="/it/">pagina principale in italiano</a>.</p>"""),
        ],
        faq=[
            ("Un’app può garantire che un alimento sia ancora sicuro?", "No. Controlla sempre data, conservazione, odore, aspetto e le indicazioni sulla confezione. I promemoria di Cibello sono un aiuto per ricordare, non un giudizio sulla sicurezza."),
            ("Come aiutano le ricette a ridurre lo spreco?", "Le ricette basate sull’inventario rendono più facile usare gli ingredienti che avete già prima di comprarne di nuovi, e mettono in evidenza ciò che sta per scadere."),
            ("Più persone possono aggiornare lo stesso inventario?", "Sì. La funzione famiglia è pensata per una panoramica condivisa di inventario, menu e lista della spesa, durante la prova e poi con un piano a pagamento."),
            ("Cibello mi rimprovera se butto qualcosa?", "No. L’app manda promemoria gentili prima che il cibo vada a male e non giudica mai cosa mangi o cosa butti."),
        ],
    ),
}

# ---------------------------------------------------------------------------
# Testo proprio della pagina di destinazione /it/
# ---------------------------------------------------------------------------
HUBTEXT = """<section><h2>Cosa mangiamo stasera?</h2><p>È la domanda più ripetuta in ogni casa, e la più faticosa. Cibello risponde partendo dalla tua cucina: fotografi frigo, freezer e dispensa, l’app riconosce i prodotti e dove si trovano, e da lì propone ricette che puoi fare davvero, con quello che c’è già. Le proposte spiegano sempre il perché, tengono conto di ciò che scade presto e dei gusti della famiglia, e restano sotto il tuo controllo. Nella guida <a href="/it/ricette-con-ingredienti/">ricette con quello che hai in casa</a> trovi come funziona passo per passo.</p></section>
<section><h2>Una settimana pianificata con calma</h2><p>Decidere una volta sola, in un momento tranquillo, invece di sette volte alle sei di sera. Il <a href="/it/pianificatore-pasti/">pianificatore pasti</a> costruisce un menu settimanale vario, mette gli alimenti freschi nei primi giorni e raccoglie nella lista della spesa solo ciò che manca. Tu sposti, cancelli e aggiungi quello che vuoi: il piano è una bozza, non un obbligo.</p></section>
<section><h2>Meno spreco, nessun senso di colpa</h2><p>Buona parte del cibo che buttiamo è cibo che avevamo dimenticato. Un inventario aggiornato e un promemoria gentile al momento giusto bastano spesso a usare le cose in tempo. Nella guida su <a href="/it/ridurre-spreco-alimentare/">come ridurre lo spreco alimentare in casa</a> raccogliamo abitudini semplici e spieghiamo come l’app ti aiuta, senza mai giudicare.</p></section>
<section><h2>Un aiuto onesto</h2><p>L’IA a volte sbaglia: può leggere male un’etichetta o saltare un prodotto. Per questo controlli sempre il risultato prima di salvarlo, e i filtri per allergie restano un’indicazione, non una garanzia. I tuoi dati sono conservati nell’UE e puoi eliminare l’account direttamente dall’app. Cibello è pensato per adulti, è disponibile in 12 lingue e si prova gratis per 14 giorni, senza carta.</p></section>"""

# ---------------------------------------------------------------------------
# Pagine condivise
# ---------------------------------------------------------------------------
ABOUT = dict(
    title="Chi siamo: l’app Cibello e l’azienda che la sviluppa | LandveX AB",
    desc="Cibello è sviluppata da LandveX AB a Tyresö, in Svezia. Perché esiste l’app, come pensiamo a IA, dati e spreco alimentare e come contattarci.",
    h1="Chi siamo",
    lead="Cibello è un’app svedese per il cibo di ogni giorno, sviluppata da LandveX AB. È nata per rispondere a una domanda che si ripete in quasi tutte le case, tutti i giorni: cosa mangiamo? Questa pagina spiega cosa cerchiamo di fare, come lavoriamo con l’IA e con i dati e come contattarci.",
    sections=[
        ("Perché esiste Cibello", """<p>La maggior parte delle app di ricette parte dalle ricette. Noi volevamo partire dalla cucina: cosa c’è davvero in frigo, in freezer e in dispensa, cosa sta per scadere e cosa piace alla famiglia. Per questo il cuore di Cibello è un inventario degli alimenti, il tuo Food Twin, costruito da foto, scontrini e codici a barre. Ricette, menu settimanale, lista della spesa e promemoria si appoggiano tutti sugli stessi dati. L’obiettivo è meno stress quotidiano e <a href="/it/ridurre-spreco-alimentare/">meno spreco alimentare</a>, senza prediche.</p>"""),
        ("Come pensiamo all’IA", """<p>L’IA rende possibile Cibello, ma a volte sbaglia. La scansione può leggere male un prodotto, saltare qualcosa in fondo al ripiano o indovinare una data errata. Per questo controlli sempre il risultato prima che venga salvato, e le proposte restano proposte. I filtri per ricette e allergie sono un’indicazione, mai una garanzia, e i valori nutrizionali sono stime utili per pianificare, non consigli dietetici. I modelli di Cibello si addestrano solo sulle tue correzioni e, se lo scegli separatamente, su immagini ripulite. Entrambe le opzioni sono disattivate per impostazione predefinita. Leggi l’<a href="/it/privacy/">informativa sulla privacy</a>.</p>"""),
        ("I tuoi dati", """<p>Tutto è conservato nell’UE. Puoi vedere i tuoi dati nell’app ed <a href="/it/delete-account/">eliminare l’account</a> quando vuoi, senza contattare l’assistenza. Non vendiamo dati personali.</p>"""),
        ("L’azienda", """<p>Cibello è sviluppata e di proprietà di LandveX AB, numero di registrazione 559141-7042, Antennvägen 2, 135 48 Tyresö, Svezia. L’app è disponibile per iOS e Android in dodici lingue ed è realizzata in Svezia. Per ora è destinata a persone di almeno 18 anni, perché le condizioni del servizio IA utilizzato richiedono utenti adulti. La prova dura 14 giorni e non richiede una carta.</p>"""),
        ("Contatti", """<p>Domande generali e collaborazioni: <a href="mailto:hello@cibello.app">hello@cibello.app</a>. Assistenza: <a href="mailto:support@cibello.app">support@cibello.app</a>. Privacy e protezione dei dati: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>. Le richieste della stampa sono benvenute allo stesso indirizzo; di norma rispondiamo entro un paio di giorni lavorativi.</p><p>Seguici su <a href="https://www.instagram.com/cibelloapp/" rel="noopener">Instagram</a>, <a href="https://www.tiktok.com/@cibello73" rel="noopener">TikTok</a> e <a href="https://www.facebook.com/profile.php?id=61593336222919" rel="noopener">Facebook</a>.</p>"""),
    ],
)

PRESS = dict(
    title="Stampa e media: fatti, immagini e contatti | Cibello",
    desc="Kit per la stampa di Cibello: descrizione breve, fatti sull’app, logo e immagini, dati sullo spreco alimentare con fonti e il contatto stampa di LandveX AB.",
    eyebrow="Per giornalisti e autori",
    h1="Stampa e media",
    lead="Tutto ciò che serve per scrivere di Cibello: una descrizione breve, i fatti, le immagini e un contatto che risponde in fretta. Tutto il contenuto di questa pagina può essere usato liberamente in contesti editoriali.",
    sections=[
        ("Cibello in breve", """<p>Cibello è un’app svedese per il cibo di ogni giorno che fotografa frigo e dispensa, tiene un inventario degli alimenti con posizione e date, propone ricette con ciò che c’è davvero in casa, pianifica la settimana e condivide la lista della spesa con la famiglia. Ricorda con gentilezza prima che il cibo vada a male e non giudica mai cosa mangia nessuno. Disponibile per iOS e Android in dodici lingue, con dati conservati nell’UE, sviluppata da LandveX AB a Tyresö, in Svezia.</p><p><strong>In una frase:</strong> Cibello è l’app che vede cosa hai in casa e risponde alla domanda «cosa mangiamo?».</p>"""),
        ("Fatti", """<ul><li>Disponibile per iOS e Android. Età minima 18 anni.</li><li>Prova: 14 giorni senza carta, poi abbonamento tramite App Store o Google Play.</li><li>Ricette: oltre 9.000, abbinate all’inventario alimentare dell’utente.</li><li>Lingue: svedese, inglese, tedesco, francese, spagnolo, italiano, olandese, polacco, danese, norvegese, finlandese, portoghese.</li><li>Dati: conservati nell’UE. Account e dati si possono eliminare direttamente nell’app.</li><li>IA: scansione di frigo, dispensa, scontrini e codici a barre. L’utente controlla sempre il risultato. I modelli di Cibello si addestrano solo sulle correzioni degli utenti e, con consenso separato, su immagini ripulite.</li><li>Prezzo: prova gratuita, poi un piano a pagamento per le funzioni famiglia. I prezzi aggiornati sono su App Store e Google Play.</li><li>Azienda: LandveX AB, n. reg. 559141-7042, Antennvägen 2, 135 48 Tyresö, Svezia.</li></ul>"""),
        ("Logo e immagini", """<ul><li><a href="/img/icon-512.png">Icona dell’app, PNG 512×512</a></li><li><a href="/img/og-it.png">Immagine di condivisione, PNG 1200×630 (italiano)</a></li><li><a href="/img/og.png">Immagine di condivisione, PNG 1200×630 (svedese)</a></li><li><a href="/favicon.svg">Simbolo, SVG</a></li></ul><p>Le schermate dell’app sono disponibili su richiesta. Le immagini possono essere usate liberamente in contesti editoriali citando Cibello.</p>"""),
        ("Contatto stampa", """<p><a href="mailto:hello@cibello.app?subject=Richiesta%20stampa">hello@cibello.app</a>. Di norma rispondiamo alle richieste della stampa entro un giorno lavorativo. Il fondatore è disponibile per interviste sullo spreco alimentare domestico, sull’IA nella vita quotidiana e sul perché «cosa mangiamo?» sia una domanda che vale la pena risolvere.</p><p>Altre informazioni sull’azienda: <a href="/it/about/">Chi siamo</a>.</p>"""),
    ],
)

NEWS = dict(
    title="Novità di Cibello: aggiornamenti e nuove guide",
    desc="Nuove guide, strumenti e aggiornamenti su cibello.app, con data. Disponibile anche via RSS.",
    h1="Novità di Cibello",
    lead="Cosa è stato aggiunto al sito e all’app, dal più recente. È disponibile un feed RSS.",
    rss_label="Feed RSS",
    entries=[
        ("2026-09-04", "Nuova guida: lo spreco alimentare in Svezia in cifre", "/matsvinn-statistik/",
         "I dati ufficiali dell’Agenzia svedese per l’ambiente e dell’Agenzia alimentare svedese in una sola pagina (in svedese): 880.000 tonnellate di spreco alimentare, 16 kg di cibo commestibile per persona nelle famiglie e 1.330 corone per persona all’anno, con la fonte di ogni cifra."),
        ("2026-09-04", "Tre nuove guide in inglese e due confronti", "/en/best-meal-planning-app/",
         "Cosa mangiare stasera, pianificatore pasti con IA e app per la dispensa, oltre a confronti onesti tra app di pianificazione dei pasti e app di ricette con Mealime, Samsung Food, Plan to Eat, Paprika e SuperCook."),
        ("2026-09-04", "Pagine di destinazione complete in dodici lingue", "/it/",
         "Ogni lingua ha ora una pagina di destinazione completa invece di una breve pagina di testo, e nulla viene più tradotto nel browser. Anche le tre guide in italiano sono state riscritte e ampliate."),
        ("2026-08-30", "Informativa sulla privacy e condizioni d’uso, versione 2.0", "/it/privacy/",
         "Testi aggiornati che coprono l’analisi con Gemini, l’addestramento volontario di Cibello AI, la prova di 14 giorni senza carta e il limite di età di 18 anni. Sono disponibili le traduzioni in italiano; in caso di differenze prevale la versione svedese."),
    ],
)

# ---------------------------------------------------------------------------
# Testi legali: traduzioni fedeli di integritet.html, villkor.html e delete-account.html (v2.0)
# ---------------------------------------------------------------------------
PRIVACY = dict(
    title="Informativa sulla privacy – Cibello",
    desc="Come Cibello tratta dati personali, immagini, analisi con Gemini e addestramento volontario di Cibello AI. Traduzione italiana dell’informativa svedese, versione 2.0.",
    h1="Informativa sulla privacy",
    notice="<strong>In breve:</strong> un servizio IA esterno esegue l’analisi delle immagini attuale. Il modello IA di Cibello può essere addestrato solo sulle correzioni dell’utente e su immagini ripulite, dopo una scelta separata, volontaria e attiva durante l’introduzione. Le risposte dell’IA esterna non vengono mai usate come riferimento di addestramento.",
    body="""<h2>1. Titolare del trattamento</h2>
<p>LandveX AB, numero di registrazione 559141-7042, Antennvägen 2, 135 48 Tyresö, Svezia, è il titolare del trattamento per Cibello. Le domande sulla privacy vanno inviate a <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>

<h2>2. Dati e finalità</h2>
<ul>
<li><strong>Account:</strong> indirizzo e-mail, nome visualizzato, identità di autenticazione e registri di sicurezza, per creare e proteggere l’account.</li>
<li><strong>Dati su alimenti e famiglia:</strong> inventario, ricette, preferenze, allergie e correzioni dell’utente, per le funzioni dell’app.</li>
<li><strong>Immagini:</strong> le immagini che l’utente sceglie di scansionare per identificare alimenti o scontrini.</li>
<li><strong>Pagamento:</strong> stato dell’abbonamento e riferimenti delle transazioni. I dati della carta e di pagamento sono gestiti da Apple App Store o Google Play.</li>
<li><strong>Dati tecnici:</strong> errori, prestazioni e analisi del prodotto, solo secondo le scelte dell’utente e le necessità di sicurezza.</li>
<li><strong>Protezione contro l’abuso del periodo di prova gratuito:</strong> un’impronta HMAC pseudonima e con chiave dell’indirizzo e-mail normalizzato viene conservata per un massimo di cinque anni. Non può essere usata per l’accesso o per contattare l’utente e non contiene l’indirizzo in chiaro, l’ID utente né l’identità Firebase. Il suo unico scopo è impedire periodi di prova ripetuti dopo l’eliminazione dell’account e una nuova registrazione.</li>
</ul>

<h2>3. Gemini in produzione</h2>
<p>Le immagini selezionate e le istruzioni necessarie vengono inviate all’API Google Gemini per generare il risultato mostrato nell’app. Cibello utilizza il servizio a pagamento all’interno del SEE. Secondo le condizioni di Google, i dati nel servizio a pagamento non vengono usati per migliorare i prodotti Google, ma può esserci una registrazione limitata per motivi di sicurezza e di contrasto agli abusi, salvo che si applichi una specifica modalità a conservazione zero. Cibello non promette quindi una conservazione zero al di fuori del proprio ambiente senza conferma tecnica del fornitore.</p>
<p>I risultati di Gemini sono stime automatiche. L’utente deve controllare contenuto, allergeni, date e quantità prima di usare le informazioni.</p>

<h2>4. Il modello IA di Cibello: addestramento separato e volontario</h2>
<p>Cibello sviluppa un proprio modello di IA. Il flusso di addestramento è separato, tecnicamente e giuridicamente, dal servizio IA esterno che fornisce all’utente i risultati attuali:</p>
<ul>
<li>Le risposte, i ragionamenti o le proposte di Gemini non vengono mai esportati come etichette o riferimento di addestramento per il modello IA di Cibello.</li>
<li>Il <strong>miglioramento anonimizzato dell’IA</strong> consente di usare la correzione esplicita dell’utente o il riferimento confermato manualmente, senza l’immagine.</li>
<li>L’<strong>addestramento con immagini</strong> consente di collegare una copia ripulita dell’immagine dell’utente alla sua correzione. I metadati vengono rimossi e l’immagine viene ridotta di dimensione prima della conservazione.</li>
<li>L’introduzione mostra un’unica scelta chiara per queste due parti della stessa finalità di addestramento. La scelta non è preselezionata e l’app funziona anche se l’utente non acconsente.</li>
<li>Il consenso può essere revocato con un pulsante in Profilo. Da quel momento cessa ogni uso futuro, l’archivio di addestramento attivo gestito dall’app viene svuotato e i riferimenti alle immagini vengono rimossi. I parametri del modello già prodotti e aggregati normalmente non possono essere ricondotti a una persona.</li>
<li>Cibello AI non influisce sul risultato in produzione finché non sono state raggiunte soglie documentate di benchmark e di sicurezza.</li>
</ul>

<h2>5. Base giuridica</h2>
<p>Account e funzioni principali sono trattati per l’esecuzione del contratto. La registrazione di sicurezza e l’impronta limitata contro i periodi di prova ripetuti sono trattate sulla base del legittimo interesse. Obblighi di legge possono richiedere altri trattamenti limitati. L’analisi del prodotto, il miglioramento dell’IA e l’addestramento con immagini, tutti volontari, si basano su consensi separati che possono essere revocati.</p>

<h2>6. Conservazione e destinatari</h2>
<p>I dati sono conservati per il tempo necessario al servizio, alla sicurezza, agli obblighi di legge e alla conservazione documentata dei backup. I fornitori possono includere AWS per hosting e archiviazione, Firebase per l’autenticazione, Google Gemini per l’analisi IA selezionata e Apple o Google per i pagamenti. Cibello non vende dati personali. L’impronta del periodo di prova viene cancellata automaticamente al più tardi cinque anni dopo l’inizio della prova.</p>

<h2>7. I tuoi diritti</h2>
<p>Puoi chiedere accesso, rettifica, portabilità dei dati, limitazione o cancellazione e opporti a determinati trattamenti. I consensi si modificano in Profilo. L’account può essere eliminato direttamente nell’app o tramite la <a href="/it/delete-account/">pagina per l’eliminazione dell’account</a>. Puoi anche rivolgerti all’autorità svedese per la protezione dei dati (Integritetsskyddsmyndigheten).</p>

<h2>8. Età</h2>
<p>Per il momento Cibello è destinato a persone di almeno 18 anni, perché le condizioni del servizio API Gemini utilizzato richiedono utenti adulti. Il requisito di età sarà riconsiderato se la soluzione tecnica del fornitore dovesse cambiare.</p>

<h2>9. Modifiche</h2>
<p>Le modifiche sostanziali ricevono un numero di versione e richiedono una nuova accettazione nell’app prima di continuare a usarla.</p>""",
)

TERMS = dict(
    title="Condizioni d’uso – Cibello",
    desc="Condizioni d’uso di Cibello: account, limite di età, abbonamenti e prova di 14 giorni, analisi IA e uso sicuro. Traduzione italiana delle condizioni svedesi, versione 2.0.",
    h1="Condizioni d’uso",
    body="""<h2>1. Contratto e limite di età</h2>
<p>Le presenti condizioni si applicano tra l’utente e LandveX AB, numero di registrazione 559141-7042. Per il momento Cibello è riservato a persone di almeno 18 anni. Creando un account, l’utente conferma la propria età e accetta le condizioni e l’<a href="/it/privacy/">informativa sulla privacy</a>.</p>

<h2>2. Il servizio</h2>
<p>Cibello aiuta l’utente a organizzare gli alimenti, a interpretare immagini e scontrini selezionati e a ricevere proposte di ricette e di pasti. I risultati possono essere incompleti o errati e devono essere controllati dall’utente.</p>

<h2>3. Nessuna consulenza medica o professionale</h2>
<p>Cibello offre ispirazione e informazioni generali, non consulenza medica, dietetica, allergologica o di altro tipo professionale. L’utente è responsabile del controllo di ingredienti, allergeni, porzioni, conservazione, preparazione e sicurezza alimentare. In caso di malattia, gravidanza, allergie gravi o esigenze particolari occorre consultare personale sanitario qualificato.</p>

<h2>4. IA e controllo umano</h2>
<p>Per l’analisi attuale in produzione viene utilizzato un servizio IA esterno. Il modello IA di Cibello viene sviluppato in parallelo, ma può essere addestrato solo secondo il consenso e le limitazioni descritte nell’<a href="/it/privacy/">informativa sulla privacy</a>. Le risposte dell’IA esterna non vengono mai usate come riferimento di addestramento. I risultati automatici devono sempre poter essere corretti dall’utente.</p>

<h2>5. Consensi volontari all’addestramento</h2>
<p>L’accesso alle funzioni principali di Cibello non può essere condizionato al consenso al miglioramento dell’IA o all’addestramento con immagini. La scelta è disattivata dall’inizio, è separata dall’accettazione delle condizioni e può essere modificata in Profilo.</p>

<h2>6. Account e sicurezza</h2>
<p>L’utente deve fornire dati corretti, proteggere le proprie credenziali di accesso e segnalare a Cibello eventuali sospetti di abuso. L’account può essere eliminato in Profilo o tramite la <a href="/it/delete-account/">procedura web</a>.</p>

<h2>7. Abbonamenti e pagamento</h2>
<p>Gli abbonamenti digitali nell’app mobile si acquistano e si gestiscono tramite Apple App Store o Google Play. Il periodo di prova di 14 giorni senza carta, controllato dai server di Cibello, vale una sola volta per identità e-mail nell’arco di cinque anni. Un account eliminato può essere creato di nuovo, ma non dà automaticamente diritto a un nuovo periodo gratuito. Prezzo, durata, rinnovo automatico e disdetta sono indicati dal rispettivo store prima dell’acquisto. I rimborsi sono gestiti secondo le regole dello store e il diritto dei consumatori inderogabile.</p>

<h2>8. Uso consentito</h2>
<p>Il servizio non può essere usato per contenuti illegali, violazioni di diritti, molestie, sovraccarico automatizzato, aggiramento della sicurezza o tentativi di estrarre dati di altri utenti. Cibello può limitare gli account in caso di rischio per la sicurezza o di violazione sostanziale del contratto.</p>

<h2>9. Disponibilità e modifiche</h2>
<p>Il servizio è in continuo sviluppo e può essere temporaneamente non disponibile. Le funzioni possono cambiare per motivi di sicurezza, di legge, di qualità o tecnici. Le modifiche sostanziali alle condizioni ricevono un numero di versione e richiedono una nuova accettazione.</p>

<h2>10. Responsabilità e diritto inderogabile</h2>
<p>LandveX AB risponde secondo il diritto inderogabile applicabile. Nulla nelle presenti condizioni limita diritti a cui non è possibile rinunciare per legge. Si applica il diritto svedese; il consumatore può inoltre far valere il diritto inderogabile e il foro competente del proprio Paese di residenza.</p>

<h2>11. Contatti</h2>
<p>Assistenza: <a href="mailto:support@cibello.app">support@cibello.app</a>. Privacy: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>""",
)

DELETE = dict(
    title="Eliminare account e dati – Cibello",
    desc="Come eliminare il tuo account Cibello e i dati personali collegati direttamente nell’app, oppure via e-mail se non riesci ad accedere.",
    h1="Eliminare account e dati",
    body="""<h2>Direttamente nell’app</h2>
<ol>
<li>Accedi a Cibello.</li>
<li>Apri <strong>Profilo</strong>.</li>
<li>Scegli <strong>Elimina account</strong> e conferma.</li>
</ol>
<p>Vengono eliminati l’account, l’identità Firebase, le immagini attive e i dati personali dell’app. I riferimenti delle transazioni economiche possono essere pseudonimizzati e conservati quando la legge lo richiede. I backup vengono eliminati a rotazione secondo la conservazione documentata.</p>

<h2>Se non riesci ad aprire l’app</h2>
<p>Invia la richiesta dall’indirizzo e-mail registrato sull’account a <a href="mailto:privacy@cibello.app?subject=Elimina%20il%20mio%20account%20Cibello">privacy@cibello.app</a>. Scrivi «Elimina il mio account Cibello». Prima dell’eliminazione verifichiamo che tu abbia il controllo dell’indirizzo.</p>

<h2>Dati di addestramento</h2>
<p>Al momento dell’eliminazione, le correzioni dell’utente e i riferimenti alle immagini vengono rimossi dall’archivio di addestramento attivo. Le risposte di Gemini non sono mai state esportate come riferimento di addestramento per Cibello AI. I parametri del modello già aggregati normalmente non possono essere ricondotti a una persona.</p>""",
)

# ---------------------------------------------------------------------------
# Stringhe di interfaccia
# ---------------------------------------------------------------------------
UI = dict(
    faq_title="Domande frequenti",
    privacy_nav="Privacy",
    terms_nav="Condizioni d’uso",
    delete_nav="Eliminare l’account",
    legal_meta="Cibello · versione 2.0 · in vigore dal 30 agosto 2026 · traduzione italiana",
    translation_label="Informazioni su questa traduzione:",
    translation_note="Questa è una traduzione italiana dell’originale svedese (<a href=\"{sv}\" lang=\"sv\">originale</a>). In caso di differenze prevale la versione svedese.",
)
