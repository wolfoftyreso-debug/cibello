"""Norsk (bokmål) innhold for cibello.app. Struktur: se _schema.py."""

LANG = "nb"

# De tre guidene. Rekkefølge: planlegger, oppskrifter, matsvinn.
GUIDES = {
    "/nb/matplanlegger/": dict(
        title="Matplanlegger for en enklere og mer variert uke | Cibello",
        desc="Planlegg ukens middager etter husstanden, maten dere har hjemme og det som bør brukes snart. Cibello kobler ukeplanen til handlelisten.",
        eyebrow="Ukeplan for hele husstanden",
        h1="Matplanlegger for en enklere og mer variert uke",
        lead="Planlegg etter husstanden, maten dere har og det som bør brukes snart. Cibello foreslår en ukeplan du går gjennom og endrer, og kobler den til handlelisten.",
        sections=[
            ("Hvorfor en ukeplan gir roligere kvelder", """<p>Klokka er fem, alle er sultne, og spørsmålet er det samme som i går: hva skal vi spise? Det er sjelden selve matlagingen som tapper energi, det er å bestemme seg. En ukeplan flytter den avgjørelsen til et rolig øyeblikk, for eksempel søndag ettermiddag, slik at hverdagskveldene bare handler om å lage det som allerede er bestemt.</p><p>En god ukeplan er et utkast, ikke en timeplan du må følge. Den skal tåle at noen kommer sent hjem, at restene fra tirsdag holder til onsdag, og at planen endrer seg når uken ikke går som tenkt. Cibello er laget for akkurat det: appen foreslår, du går gjennom og bestemmer.</p>"""),
            ("En enkel rutine for hele uken", """<p>Rutinen trenger ikke være komplisert. Slik kan en uke se ut:</p><ol><li><strong>Se hva du har.</strong> Ta bilde av kjøleskap, fryser og skap. Cibello kjenner igjen varene og hvor de står, og du kontrollerer resultatet før det lagres, siden KI kan overse eller feiltolke noe.</li><li><strong>Velg retter.</strong> Få forslag som bygger på det du faktisk har, med det som snart går ut høyt oppe. Bytt ut det som ikke passer.</li><li><strong>Legg måltidene inn per dag.</strong> Flytt dem rundt til uken ser realistisk ut.</li><li><strong>La handlelisten samle det som mangler.</strong> Bare det som ikke allerede finnes hjemme.</li><li><strong>Oppdater underveis.</strong> Når noen i husstanden kjøper eller bruker en vare, kan den felles oversikten oppdateres for alle.</li></ol><p>Slik får dere et praktisk kretsløp fra matlager til måltid og neste innkjøp, uten å starte på nytt hver dag. Jo oftere matlageret og handlelisten holdes oppdatert, desto bedre treffer forslagene neste uke.</p>"""),
            ("Variasjon uten unødvendig styr", """<p>Automatiske forslag skal ikke gi samme rett til lunsj og middag eller gjenta den samme hovedråvaren flere dager på rad. Cibello varierer retter, råvarer og måltidstyper når uken settes opp, slik at kylling på mandag ikke blir kylling igjen på tirsdag og onsdag. Du ser hele planen før uken begynner og kan bytte enkeltdager uten å lage alt på nytt.</p><p>Variasjon betyr likevel ikke sju nye oppskrifter. De fleste husstander har noen faste retter som alltid fungerer. Bruk dem som ryggrad, og la appen fylle på med én eller to nye ideer fra de mer enn 9 000 oppskriftene som matches mot matlageret ditt. Flere ideer finner du i guiden om <a href="/nb/oppskrifter-med-ingredienser/">oppskrifter med ingrediensene du allerede har</a>.</p>"""),
            ("Bruk maten i riktig rekkefølge", """<p>Varer med kort holdbarhet bør få en plass tidlig i uken. Når matlageret er koblet til ukeplanen, blir det enklere å bruke det ømfintlige først og spare det holdbare til senere. Det reduserer både impulskjøp og mat som blir glemt bakerst i kjøleskapet.</p><table><thead><tr><th>Når i uken</th><th>Passer for</th><th>Eksempel</th></tr></thead><tbody><tr><td>Tidlig</td><td>Ferske råvarer med kort holdbarhet</td><td>Fisk, salat, ferske urter, åpnet fløte</td></tr><tr><td>Midt i uken</td><td>Kjøtt og grønnsaker som holder noen dager</td><td>Kylling, kjøttdeig, brokkoli, paprika</td></tr><tr><td>Senere</td><td>Tørrvarer, fryservarer og rotgrønnsaker</td><td>Pasta, linser, frosne erter, gulrot, potet</td></tr></tbody></table><p>Cibello kan gi en mild påminnelse før noe blir dårlig, men datoer og KI-tolkninger kan være feil. Lukt, se og følg alltid anvisningen på pakningen. Mer om dette i guiden om å <a href="/nb/redusere-matsvinn/">redusere matsvinn</a>.</p>"""),
            ("Ukeplan for en familie", """<p>Med barn i huset må middagen ofte være både rask, kjent og mulig å variere uten protester. En holdbar familieplan pleier å bygge på noen faste hverdagsretter, én eller to nye ideer og plass til rester. Legg gjerne inn en restedag: rester som er registrert som matbokser, finnes i matlageret og kan veies inn i forslagene.</p><p>La gjerne barna velge mellom to eller tre retter du allerede har godkjent. De får være med og bestemme, og du slipper diskusjonen klokka fem. Selve appen er laget for voksne, så det er du som fotograferer, kontrollerer og lagrer.</p>"""),
            ("Del planen med husstanden", """<p>Den som planlegger, skal ikke måtte bære alt alene. I Cibello kan medlemmer i husstanden bruke samme matlager, ukeplan og handleliste. Alle ser det samme utgangspunktet, og den som er i butikken, ser hva som faktisk mangler. Deling i husstanden er med i prøveperioden og deretter i betalplanen.</p><p>Husk at hver oppskrift fortsatt må kontrolleres mot husstandens allergier, ingredienser og emballasje. Oppskrift- og allergenfiltre er veiledning, ikke en garanti, og næringsverdier er anslag.</p>"""),
            ("Fra forslag til vane", """<p>Cibello samler matlager, oppskrifter, planlegging og innkjøp, slik at det dere allerede har kan bli til en plan og en felles liste. KI-forslag støtter valget, men du kontrollerer alltid ingredienser, allergier og hva som lagres. Prøv appen i 14 dager uten kort, og se om søndagsplanen gir roligere hverdagskvelder. En oversikt over hele appen finner du på <a href="/nb/">startsiden</a>.</p>"""),
        ],
        faq=[
            ("Kan Cibello lage en ukeplan automatisk?", "Cibello foreslår en ukeplan som varierer retter og råvarer ut fra det du har hjemme. Du går gjennom forslaget, bytter det som ikke passer og bestemmer hva som lagres."),
            ("Tar ukeplanen hensyn til maten vi har hjemme?", "Ja. Det kontrollerte matlageret er utgangspunktet, og varer som snart går ut, får plass tidlig i uken. Handlelisten samler bare det som mangler."),
            ("Kan jeg endre et planlagt måltid?", "Ja. Planen er et forslag. Du kan flytte måltider mellom dager, stryke retter og legge til egne favoritter når som helst."),
            ("Kan flere i husstanden se den samme planen?", "Ja. Husstanden kan dele matlager, ukeplan og handleliste. Delingen er med i prøveperioden på 14 dager og deretter i betalplanen."),
        ],
    ),
    "/nb/oppskrifter-med-ingredienser/": dict(
        title="Oppskrifter med ingrediensene du allerede har | Cibello",
        desc="Gjør et kontrollert kjøleskap og matlager om til middagsideer. Cibello matcher mer enn 9 000 oppskrifter mot det du har hjemme og viser hva som mangler.",
        eyebrow="Middag av det du har",
        h1="Oppskrifter med ingrediensene du allerede har",
        lead="Hva skal vi spise i kveld, med det som faktisk står i kjøleskapet? Cibello tar utgangspunkt i matlageret ditt, rangerer oppskrifter etter hvor mye du har hjemme og viser hva som eventuelt mangler.",
        sections=[
            ("Begynn med det som finnes i kjøleskap og skap", """<p>Gode middagstips må være mulige å lage. Derfor tar Cibello utgangspunkt i varene du selv har fotografert, skannet eller lagt inn, ikke i en oppskrift du først må handle til. Forslagene kan prioritere det som bør brukes snart og viser hva som eventuelt mangler. Du slipper å velge en rett og så oppdage at halvparten av ingrediensene ikke er hjemme.</p><p>Det er en liten forskjell i rekkefølge som gjør stor forskjell klokka fem: først hva du har, så hva du kan lage.</p>"""),
            ("Fra skanning til en nyttig oversikt", """<p>Ta bilde av kjøleskapet, fryseren og skapet. Cibello kjenner igjen varene og hvor de står, for eksempel at rekeosten står i kjøleskapsdøren. Kvitteringer og strekkoder kan også skannes, så lageret kan oppdateres etter en handletur uten at du skriver inn alt for hånd.</p><p>Resultatet kontrollerer du før det lagres. KI kan overse en vare bakerst i hyllen, blande sammen to produkter eller gjette feil dato. Når du retter det som er usikkert, blir matlageret mer pålitelig, og både oppskriftsforslag og ukeplan får et bedre utgangspunkt.</p>"""),
            ("Slik rangeres forslagene", """<p>Cibello matcher det kontrollerte matlageret mot mer enn 9 000 oppskrifter. Forslagene rangeres etter hvor stor andel av ingrediensene du har hjemme, og appen forklarer alltid hvorfor en rett kommer høyt opp. Dette veies inn:</p><ul><li><strong>Andel hjemme.</strong> En rett der 82 prosent av ingrediensene finnes, kommer foran en der du mangler det meste.</li><li><strong>Det som snart går ut.</strong> Kylling og fløte som nærmer seg datoen, løfter retter der de brukes.</li><li><strong>Husstandens vaner.</strong> Appen lærer med tiden hva dere pleier å velge, og foreslår retter som ligner favorittene deres.</li><li><strong>Det som mangler.</strong> Manglende ingredienser vises tydelig, så du kan avgjøre om det er verdt en tur i butikken eller om en annen rett passer bedre.</li></ul>"""),
            ("Middag på en vanlig tirsdag", """<p>Hverdagsmiddagen skal gå raskt og kjennes rimelig. Middagstipsene som fungerer på en tirsdag, er sjelden avanserte. Det er pastaretten, omeletten, woken eller den enkle gryta som kan lages med det som allerede står i kjøleskapet. Fordi forslagene sorteres etter andel hjemme, er det nettopp slike retter som havner øverst når det er dem du faktisk kan lage i kveld.</p><p>Søk gjerne på en råvare du vil bruke opp, som «brokkoli» eller «kjøttdeig», og se hvilke retter som dukker opp. Har du en travel uke foran deg, kan du legge rettene rett inn i ukeplanen. Hvordan det fungerer, står i guiden om <a href="/nb/matplanlegger/">matplanlegger for en enklere uke</a>.</p>"""),
            ("Helg, rester og barn i huset", """<p>I helgen er det oftere tid til langkok, baking eller noe å by på. Da kan forslagene veie inn annet enn tid: råvarer som fortjener litt mer omsorg, retter dere har lagret som favoritter, eller noe husstanden har ønsket seg. Planlegger du helgen allerede i uken, havner det som trengs på handlelisten.</p><p>Rester fra lørdagsmiddagen kan registreres som matbokser i matlageret. Da er de med i oversikten og kan veies inn i forslagene til mandag. Med barn i huset kan det være lurt å la dem velge mellom to retter du allerede har sett gjennom. Appen er laget for voksne, men valget mellom taco og pasta kan fint tas av en åtteåring.</p>"""),
            ("Allergier og filtre er veiledning", """<p>Du kan angi allergier og matvaner, og forslagene tar hensyn til dem. Men filtreringen er ingen garanti. Oppskrifter kan inneholde feil, produkter endrer innhold, og en KI kan feiltolke en pakning. Les alltid ingredienslisten og merkingen selv, særlig ved allergi eller intoleranse. Næringsverdier i appen er anslag til planlegging, ikke kostholdsråd, og Cibello gir ingen medisinsk veiledning.</p>"""),
            ("Fra forslag til handleliste", """<p>Når du har valgt maten, kan en felles handleliste gjøre neste steg enklere. Målet er ikke at du skal handle mer, men at det blir tydelig hva som mangler, slik at husstanden unngår dobbeltkjøp. Den som er i butikken, ser listen, og den som er hjemme, kan legge til det som gikk tomt.</p><p>Cibello kombinerer oppskrifter, planlegging, matlager og husstand i én app, og du kan prøve den i 14 dager uten kort. Vil du bruke opp maten før du handler nytt, kan du lese videre i guiden om å <a href="/nb/redusere-matsvinn/">redusere matsvinn</a>, eller gå til <a href="/nb/">startsiden</a> for en oversikt over appen.</p>"""),
        ],
        faq=[
            ("Kan Cibello foreslå middag av rester?", "Ja. Når rester og råvarer er registrert i matlageret, for eksempel som matbokser, kan de veies inn i forslagene."),
            ("Må jeg skrive inn alle varene manuelt?", "Nei. Du kan ta bilde av kjøleskap, fryser og skap og skanne kvitteringer og strekkoder. Resultatet må alltid kontrolleres før det lagres, siden KI kan tolke feil."),
            ("Tar Cibello hensyn til allergier?", "Du kan angi allergier og matvaner, men filtreringen er ingen garanti. Les alltid ingredienslisten og merkingen på pakningen selv."),
            ("Hvor mange oppskrifter finnes i appen?", "Mer enn 9 000. De rangeres etter hvor stor andel av ingrediensene du har hjemme, og appen viser hva som mangler."),
        ],
    ),
    "/nb/redusere-matsvinn/": dict(
        title="Reduser matsvinn med bedre oversikt | Cibello",
        desc="Se hva som finnes hjemme, bruk maten i tide og unngå dobbeltkjøp. Cibello kobler matlager, oppskrifter og handleliste og minner deg før maten blir dårlig.",
        eyebrow="Mindre svinn, mer ro",
        h1="Reduser matsvinn med bedre oversikt",
        lead="Det meste av maten som kastes hjemme, kastes fordi den ble glemt, ikke fordi noen ville kaste den. Med oversikt over kjøleskap, fryser og skap blir det enklere å bruke maten i tide og handle mindre dobbelt.",
        sections=[
            ("Hva er matsvinn, egentlig", """<p>Matsvinn er mat som kunne ha blitt spist, men som kastes i stedet. Restene som ble glemt i en boks bakerst i kjøleskapet, salaten som ble brun før noen rakk å bruke den, yoghurten som gikk ut på dato uten at noen sjekket om den fortsatt var god. Undersøkelser i Norge peker i samme retning som i resten av Europa: husholdningene står for en stor del av svinnet, og mye av det skyldes manglende oversikt, ikke mangel på vilje.</p><p>Det er der et matlager og påminnelser i tide gjør en forskjell. Ingen trenger å bli en annen person for å kaste mindre. Det er nok å vite hva som finnes, og å få et hint før det er for sent.</p>"""),
            ("Se hva som risikerer å bli glemt", """<p>Et matlager gjør det enklere å finne varer i kjøleskap, fryser og skap. Ta bilde, så kjenner Cibello igjen varene og hvor de står. Kvitteringer og strekkoder kan skannes etter en handletur. Du kontrollerer alltid resultatet før det lagres, for KI kan overse noe eller gjette feil dato.</p><p>Når det finnes informasjon om holdbarhet, kan Cibello gi en mild påminnelse om det som bør brukes snart. Appen bruker verken skam eller kaloripress. Målet er en roligere og mer praktisk mathverdag. Men datoer og KI-tolkninger kan være feil. Lukt, se og følg alltid anvisningen på pakningen, særlig når maten skal til barn, gravide eller personer med nedsatt immunforsvar.</p>"""),
            ("Best før er ikke det samme som siste forbruksdag", """<p>Mye spiselig mat kastes fordi datomerkingen misforstås. De to merkingene betyr forskjellige ting:</p><table><thead><tr><th>Merking</th><th>Hva den betyr</th><th>Hva du gjør</th></tr></thead><tbody><tr><td>Best før</td><td>Produsentens garanti for kvalitet, ikke en grense for sikkerhet. Mange varer er gode lenge etter, og flere norske produsenter skriver «best før, ofte god etter».</td><td>Se, lukt og smak før du kaster tørrvarer, meieriprodukter og egg.</td></tr><tr><td>Siste forbruksdag</td><td>Brukes på lett bedervelige varer som fersk fisk, kjøtt og kylling. Etter denne dagen kan maten være helsefarlig selv om den ser fin ut.</td><td>Ikke spis etter datoen. Frys ned i god tid hvis du ikke rekker å bruke varen.</td></tr></tbody></table><p>Det er alltid du som vurderer om maten kan spises. Appen kan minne deg på datoen, men ikke lukte på melken for deg.</p>"""),
            ("Planlegg oppskrifter rundt råvarene", """<p>I stedet for å kjøpe et helt nytt sett ingredienser kan du lete etter oppskrifter som bruker det du har. Cibello matcher matlageret mot mer enn 9 000 oppskrifter, rangert etter hvor mye du allerede har hjemme, og løfter retter som bruker det som snart går ut. Det som faktisk mangler, kan legges på handlelisten. Les mer i guiden om <a href="/nb/oppskrifter-med-ingredienser/">oppskrifter med ingrediensene du allerede har</a>.</p><p>Planlegger du hele uken, kan de ømfintlige råvarene få plass tidlig og de holdbare senere. Guiden om <a href="/nb/matplanlegger/">matplanlegger for en enklere uke</a> viser hvordan en enkel ukerutine kan se ut.</p>"""),
            ("Rester og matbokser", """<p>Rester er ikke et problem, det er ferdig middag. Problemet er at de glemmes. Registrer restene som matbokser i matlageret, så er de med i oversikten på samme måte som andre varer, og du kan få en påminnelse før de bør spises. En liten vane som hjelper: ha en fast plass i kjøleskapet for det som skal brukes først, og se dit før du begynner å planlegge kveldens middag.</p>"""),
            ("Del oversikten i husstanden", """<p>Når husstanden deler matlager, ukeplan og handleliste, blir det lettere å unngå dobbeltkjøp. Den som handler på vei hjem, ser at det allerede står melk i kjøleskapet, og den som lager middag, ser at kyllingen bør brukes i dag. Planleggingen blir synlig for flere, og maten kan brukes i tide. Deling i husstanden er med i prøveperioden og deretter i betalplanen.</p>"""),
            ("Små vaner som gir mindre svinn", """<p>Mindre svinn handler om vaner, ikke om skyld. Noen som er enkle å begynne med:</p><ul><li>Sjekk matlageret før du handler, så kjøper du ikke det du allerede har.</li><li>Handle etter en plan, og la handlelisten bare inneholde det som mangler.</li><li>Bruk det ømfintlige først, og spar det holdbare til senere i uken.</li><li>Frys ned det du ikke rekker å bruke, før datoen går ut.</li><li>Gi restene en plass i matlageret, så de ikke forsvinner bakerst i kjøleskapet.</li></ul><p>Cibello minner mildt og foreslår oppskrifter, men du avgjør hva som skal spises, fryses eller kastes. Du kan prøve appen i 14 dager uten kort. Mer om Cibello finner du på <a href="/nb/">startsiden</a>.</p>"""),
        ],
        faq=[
            ("Kan en app garantere at maten fortsatt er trygg?", "Nei. Kontroller alltid dato, oppbevaring, lukt, utseende og informasjonen på pakningen selv. Appen kan minne deg på datoen, men vurderingen er din."),
            ("Hva er forskjellen på best før og siste forbruksdag?", "Best før handler om kvalitet, og mange varer er gode lenge etter datoen. Siste forbruksdag brukes på lett bedervelige varer og skal ikke overskrides."),
            ("Hvordan hjelper oppskrifter med å redusere matsvinn?", "Oppskrifter basert på matlageret gjør det lettere å bruke råvarer dere allerede har før dere handler nytt. Retter som bruker det som snart går ut, kommer høyere opp i forslagene."),
            ("Kan flere personer oppdatere samme matlager?", "Ja. Husstandsfunksjonen er laget for en felles oversikt over matlager, ukeplan og handleliste. Den er med i prøveperioden og deretter i betalplanen."),
        ],
    ),
}

# Landingssidens egen tekst.
HUBTEXT = """<section><h2>Først hva du har, så hva du kan lage</h2><p>De fleste matapper begynner med oppskriften. Cibello begynner i kjøkkenet ditt. Ta bilde av kjøleskap, fryser og skap, så kjenner appen igjen varene og hvor de står. Du kontrollerer resultatet før det lagres, og deretter matches matlageret mot mer enn 9 000 oppskrifter, rangert etter hvor mye du allerede har hjemme. Slik fungerer <a href="/nb/oppskrifter-med-ingredienser/">oppskrifter med ingrediensene du allerede har</a>.</p></section>
<section><h2>En ukeplan du faktisk kan følge</h2><p>Planen er et utkast, ikke en timeplan. Cibello foreslår en uke med variasjon mellom retter og råvarer, der det som snart går ut får plass tidlig. Du bytter dager, stryker retter og legger til egne favoritter, og handlelisten samler bare det som mangler. Hele husstanden kan dele plan og liste. Les mer i guiden om <a href="/nb/matplanlegger/">matplanlegger for en enklere uke</a>.</p></section>
<section><h2>Mindre svinn uten pekefinger</h2><p>Mye av maten som kastes hjemme, kastes fordi den ble glemt. Med oversikt over det som finnes, milde påminnelser før noe blir dårlig og rester registrert som matbokser, blir det enklere å bruke maten i tide. Appen bruker verken skam eller kaloripress. Se guiden om å <a href="/nb/redusere-matsvinn/">redusere matsvinn</a>.</p></section>
<section><h2>Du bestemmer, appen støtter</h2><p>KI kan ta feil, og derfor går du alltid gjennom det som skannes og foreslås. Oppskrift- og allergenfiltre er veiledning, ikke en garanti, og næringsverdier er anslag. Dataene dine lagres i EU, kontoen kan slettes direkte i appen, og du kan prøve Cibello i 14 dager uten kort.</p></section>"""

ABOUT = dict(
    title="Om Cibello: appen og selskapet bak | LandveX AB",
    desc="Cibello utvikles av LandveX AB i Tyresö i Sverige. Hvorfor appen finnes, hvordan vi tenker om KI, data og matsvinn, og hvordan du kontakter oss.",
    h1="Om Cibello",
    lead="Cibello er en svensk matapp fra LandveX AB. Den ble laget for å svare på et spørsmål som stilles i nesten alle hjem hver dag: hva skal vi spise? Her forklarer vi hva vi prøver å få til, hvordan vi jobber med KI og data, og hvordan du når oss.",
    sections=[
        ("Hvorfor Cibello finnes", """<p>De fleste oppskriftsapper begynner med oppskriftene. Vi ville begynne i kjøkkenet: hva som faktisk står i kjøleskapet, fryseren og skapet, hva som snart går ut og hva husstanden pleier å like. Derfor er kjernen i Cibello et matlager, din «Food Twin», bygget opp av bilder, kvitteringer og strekkoder. Oppskrifter, ukeplan, handleliste og påminnelser hviler på de samme dataene. Målet er mindre hverdagsstress og <a href="/nb/redusere-matsvinn/">mindre matsvinn</a>, uten mas.</p>"""),
        ("Slik tenker vi om KI", """<p>KI gjør Cibello mulig, men den tar iblant feil. En skanning kan lese en vare feil, overse noe bakerst i hyllen eller gjette feil dato. Derfor går du alltid gjennom resultatet før det lagres, og derfor er forslag bare forslag. Oppskrift- og allergenfiltre er veiledning, aldri en garanti, og næringsverdier er anslag til planlegging, ikke kostholdsråd. Cibellos egne modeller trenes bare på rettelsene dine og, hvis du velger det separat, på sanerte bilder. Begge valgene er av fra starten. Se <a href="/nb/privacy/">personvernerklæringen</a>.</p>"""),
        ("Dine data", """<p>Alt lagres i EU. Du kan se dataene dine i appen og <a href="/nb/delete-account/">slette kontoen</a> når du vil, uten å kontakte support. Vi selger ikke personopplysninger.</p>"""),
        ("Selskapet", """<p>Cibello utvikles og eies av LandveX AB, org.nr 559141-7042, Antennvägen 2, 135 48 Tyresö, Sverige. Appen er tilgjengelig for iOS og Android på tolv språk og er laget i Sverige. Inntil videre er den beregnet på personer som er 18 år eller eldre, fordi vilkårene for KI-tjenesten den bruker, krever voksne brukere. Prøveperioden er 14 dager uten kort.</p>"""),
        ("Kontakt", """<p>Generelle spørsmål og samarbeid: <a href="mailto:hello@cibello.app">hello@cibello.app</a>. Support: <a href="mailto:support@cibello.app">support@cibello.app</a>. Personvern og databeskyttelse: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>. Pressehenvendelser er velkomne på samme adresse. Vi svarer normalt i løpet av et par virkedager.</p><p>Følg oss på <a href="https://www.instagram.com/cibelloapp/" rel="noopener">Instagram</a>, <a href="https://www.tiktok.com/@cibello73" rel="noopener">TikTok</a> og <a href="https://www.facebook.com/profile.php?id=61593336222919" rel="noopener">Facebook</a>.</p>"""),
    ],
)

PRESS = dict(
    title="Presse og media: fakta, bilder og kontakt | Cibello",
    desc="Pressemateriell for Cibello: kort beskrivelse, fakta om appen, logo og bilder, og pressekontakten hos LandveX AB. Alt kan brukes fritt i redaksjonell sammenheng.",
    eyebrow="For journalister og skribenter",
    h1="Presse og media",
    lead="Alt du trenger for å skrive om Cibello: en kort beskrivelse, fakta, bilder og en kontakt som svarer raskt. Alt på denne siden kan brukes fritt i redaksjonell sammenheng.",
    sections=[
        ("Cibello i korte trekk", """<p>Cibello er en svensk matapp som fotograferer kjøleskapet og skapet ditt, holder et matlager med plassering og datoer, foreslår oppskrifter ut fra det som faktisk finnes hjemme, planlegger uken og deler handlelisten med husstanden. Den minner deg mildt før maten blir dårlig og dømmer aldri hva noen spiser. Tilgjengelig for iOS og Android på tolv språk, med data lagret i EU, utviklet av LandveX AB i Tyresö i Sverige.</p><p><strong>Én setning:</strong> Cibello er appen som ser hva du har hjemme og svarer på «hva skal vi spise?».</p>"""),
        ("Fakta", """<ul><li>Tilgjengelig for iOS i <a href="https://apps.apple.com/app/id6807100747" rel="noopener">App Store</a> og for Android på <a href="https://play.google.com/store/apps/details?id=com.cibello.app" rel="noopener">Google Play</a>. Aldersgrense 18 år.</li><li>Prøveperiode: 14 dager uten kort, deretter abonnement via App Store eller Google Play.</li><li>Oppskrifter: mer enn 9 000, matchet mot brukerens matlager.</li><li>Språk: svensk, engelsk, tysk, fransk, spansk, italiensk, nederlandsk, polsk, dansk, norsk, finsk og portugisisk.</li><li>Data: lagres i EU. Konto og data kan slettes i appen.</li><li>KI: skanning av kjøleskap, skap, kvitteringer og strekkoder. Brukeren går alltid gjennom resultatet. Cibellos egne modeller trenes bare på brukerens rettelser og, med separat samtykke, sanerte bilder.</li><li>Pris: gratis prøveperiode, deretter betalplan for husstandsfunksjoner. Gjeldende priser vises i App Store og Google Play.</li><li>Selskap: LandveX AB, org.nr 559141-7042, Antennvägen 2, 135 48 Tyresö, Sverige.</li></ul>"""),
        ("Logo og bilder", """<ul><li><a href="/img/icon-512.png">Appikon, 512×512 PNG</a></li><li><a href="/img/og-nb.png">Delingsbilde, 1200×630 PNG (norsk)</a></li><li><a href="/img/og.png">Delingsbilde, 1200×630 PNG (svensk)</a></li><li><a href="/favicon.svg">Symbol, SVG</a></li></ul><p>Skjermbilder fra appen sendes på forespørsel. Bildene kan brukes fritt i redaksjonell sammenheng med kreditering til Cibello.</p>"""),
        ("Pressekontakt", """<p><a href="mailto:hello@cibello.app?subject=Pressehenvendelse">hello@cibello.app</a>. Vi svarer normalt på pressehenvendelser innen én virkedag. Grunnleggeren stiller gjerne til intervju om matsvinn i husholdningene, KI i hverdagen og hvorfor «hva skal vi spise?» er et spørsmål verdt å løse.</p><p>Mer om selskapet: <a href="/nb/about/">Om Cibello</a>.</p>"""),
    ],
)

NEWS = dict(
    title="Nytt hos Cibello: oppdateringer og nye guider",
    desc="Nye guider, verktøy og oppdateringer på cibello.app, med dato. Abonner via RSS.",
    h1="Nytt hos Cibello",
    lead="Det som er lagt til på nettstedet og i appen, nyeste først. Du kan også følge oppdateringene som",
    rss_label="RSS-strøm",
    entries=[
        ("2026-09-04", "Ny guide: matsvinn i Sverige i tall", "/matsvinn-statistik/", "Offisielle tall fra svenske Naturvårdsverket og Livsmedelsverket samlet på én side (på svensk): 880 000 tonn matsvinn, 16 kg spiselig mat per person i husholdningene og 1 330 svenske kroner per person og år, med kilde for hvert tall."),
        ("2026-09-04", "Tre nye engelske guider og to sammenligninger", "/en/#guider", "Hva skal vi spise i kveld, KI-matplanlegger og matlagerapp, pluss ærlige sammenligninger av matplanleggingsapper og oppskriftsapper opp mot Mealime, Samsung Food, Plan to Eat, Paprika og SuperCook."),
        ("2026-09-04", "Komplette landingssider på tolv språk", "/nb/", "Alle språk har nå en fullstendig landingsside i stedet for en kort tekstside, og ingenting oversettes lenger i nettleseren."),
        ("2026-08-30", "Personvernerklæring og vilkår versjon 2.0", "/nb/privacy/", "Oppdaterte tekster som dekker Gemini-analyse, den frivillige treningen av Cibello AI, prøveperioden på 14 dager uten kort og aldersgrensen på 18 år. Norsk oversettelse finnes, og den svenske versjonen gjelder ved avvik."),
    ],
)

PRIVACY = dict(
    title="Personvernerklæring – Cibello",
    desc="Slik behandler Cibello personopplysninger, bilder, Gemini-analyse og frivillig trening av Cibello AI. Norsk oversettelse av den svenske originalen, versjon 2.0.",
    h1="Personvernerklæring",
    notice="<strong>Kort sagt:</strong> En ekstern KI-tjeneste brukes til dagens bildeanalyse. Cibellos egen KI-modell kan bare trenes på brukerens egne rettelser og sanerte bilder etter et separat, frivillig og aktivt valg i introduksjonen. Eksterne KI-svar brukes aldri som treningsfasit.",
    body="""<h2>1. Behandlingsansvarlig</h2>
<p>LandveX AB, org.nr 559141-7042, Antennvägen 2, 135 48 Tyresö, Sverige, er behandlingsansvarlig for Cibello. Spørsmål om personvern sendes til <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>

<h2>2. Opplysninger og formål</h2>
<ul>
<li><strong>Konto:</strong> e-postadresse, visningsnavn, autentiseringsidentitet og sikkerhetslogger for å opprette og beskytte kontoen.</li>
<li><strong>Mat- og husstandsdata:</strong> matlager, oppskrifter, preferanser, allergier og egne rettelser for appens funksjoner.</li>
<li><strong>Bilder:</strong> bilder som brukeren velger å skanne for å identifisere matvarer eller kvitteringer.</li>
<li><strong>Betaling:</strong> abonnementsstatus og transaksjonsreferanser. Kort- og betalingsopplysninger håndteres av Apple App Store eller Google Play.</li>
<li><strong>Tekniske data:</strong> feil, ytelse og produktanalyse bare i tråd med brukerens valg og nødvendige sikkerhetsbehov.</li>
<li><strong>Beskyttelse mot misbruk av gratisperioden:</strong> et nøklet, pseudonymt HMAC-fingeravtrykk av den normaliserte e-postadressen lagres i høyst fem år. Det kan ikke brukes til innlogging eller kontakt og inneholder verken adressen i klartekst, bruker-ID eller Firebase-identitet. Formålet er utelukkende å hindre gjentatte gratisperioder etter sletting av konto og ny registrering.</li>
</ul>

<h2>3. Gemini i produksjon</h2>
<p>Valgte bilder og nødvendig instruksjon sendes til Google Gemini API for å lage resultatet som vises i appen. Cibello bruker den betalte tjenesten innenfor EØS. I henhold til Googles vilkår brukes data i den betalte tjenesten ikke til å forbedre Googles produkter, men begrenset logging kan forekomme av hensyn til sikkerhet og bekjempelse av misbruk, med mindre en særskilt nullagringsmodus gjelder. Cibello lover derfor ikke nullagring utenfor sitt eget miljø uten teknisk bekreftelse fra leverandøren.</p>
<p>Gemini-resultater er automatiske anslag. Brukeren skal kontrollere innhold, allergener, datoer og mengder før informasjonen brukes.</p>

<h2>4. Cibellos egen KI-modell: separat og frivillig trening</h2>
<p>Cibello utvikler en egen KI-modell. Treningsflyten er teknisk og juridisk atskilt fra den eksterne KI-tjenesten som gir brukeren dagens resultat:</p>
<ul>
<li>Gemini-svar, resonnementer eller forslag eksporteres aldri som treningsetiketter eller treningsfasit til Cibellos egen KI-modell.</li>
<li><strong>Anonymisert KI-forbedring</strong> tillater at brukerens uttrykkelige rettelse eller manuelt bekreftede fasit brukes uten bilde.</li>
<li><strong>Bildetrening</strong> tillater at en sanert kopi av brukerens bilde kobles til brukerens egen rettelse. Metadata fjernes og bildet størrelsesbegrenses før lagring.</li>
<li>Introduksjonen viser ett felles, tydelig valg for disse to delene av samme treningsformål. Valget er ikke forhåndsvalgt, og appen fungerer også om brukeren ikke samtykker.</li>
<li>Samtykket kan trekkes tilbake med en knapp i Profil. Da stoppes fremtidig bruk, den appeide aktive treningsbanken tømmes og bildereferanser fjernes. Allerede fremstilte, aggregerte modellparametere kan normalt ikke knyttes tilbake til en person.</li>
<li>Cibello AI påvirker ikke produksjonssvaret før dokumenterte grenser for referansemåling og sikkerhet er nådd.</li>
</ul>

<h2>5. Rettslig grunnlag</h2>
<p>Konto og kjernefunksjoner behandles for å oppfylle avtalen. Sikkerhetslogging og det begrensede fingeravtrykket som skal motvirke gjentatte gratisperioder, behandles på grunnlag av berettiget interesse. Rettslige forpliktelser kan kreve annen begrenset behandling. Frivillig produktanalyse, KI-forbedring og bildetrening bygger på separate samtykker som kan trekkes tilbake.</p>

<h2>6. Lagring og mottakere</h2>
<p>Opplysninger lagres så lenge det kreves for tjenesten, sikkerhet, rettslige krav og dokumentert oppbevaring av sikkerhetskopier. Leverandører kan omfatte AWS for drift og lagring, Firebase for autentisering, Google Gemini for valgt KI-analyse og Apple eller Google for betaling. Cibello selger ikke personopplysninger. Fingeravtrykket for gratisperioden slettes automatisk senest fem år etter at prøveperioden startet.</p>

<h2>7. Dine rettigheter</h2>
<p>Du kan be om innsyn, retting, dataportabilitet, begrensning eller sletting og protestere mot visse former for behandling. Samtykker endres i Profil. Kontoen kan slettes direkte i appen eller via <a href="/nb/delete-account/">nettsiden for sletting av konto</a>. Du kan også kontakte den svenske tilsynsmyndigheten for personvern, Integritetsskyddsmyndigheten.</p>

<h2>8. Alder</h2>
<p>Cibello er inntil videre beregnet på personer som er minst 18 år, fordi vilkårene for Gemini API-tjenesten som brukes, krever voksne brukere. Alderskravet vurderes på nytt dersom den tekniske leverandørløsningen endres.</p>

<h2>9. Endringer</h2>
<p>Vesentlige endringer versjonsnummereres og krever en ny godkjenning i appen før videre bruk.</p>""",
)

TERMS = dict(
    title="Brukervilkår – Cibello",
    desc="Brukervilkår for Cibello: konto, aldersgrense, abonnement, 14 dagers prøveperiode og KI-analyse. Norsk oversettelse av de svenske vilkårene, versjon 2.0.",
    h1="Brukervilkår",
    body="""<h2>1. Avtale og aldersgrense</h2>
<p>Disse vilkårene gjelder mellom brukeren og LandveX AB, org.nr 559141-7042. Cibello er inntil videre bare for personer som er minst 18 år. Ved å opprette en konto bekrefter brukeren alderen sin og godtar vilkårene og <a href="/nb/privacy/">personvernerklæringen</a>.</p>

<h2>2. Tjenesten</h2>
<p>Cibello hjelper brukeren med å organisere mat, tolke valgte bilder og kvitteringer og få forslag til oppskrifter og måltider. Resultater kan være ufullstendige eller feilaktige og skal gjennomgås av brukeren.</p>

<h2>3. Ingen medisinsk eller profesjonell rådgivning</h2>
<p>Cibello gir inspirasjon og generell informasjon, ikke medisinsk, ernæringsfaglig, allergifaglig eller annen profesjonell rådgivning. Brukeren har ansvar for å kontrollere ingredienser, allergener, porsjonsstørrelse, holdbarhet, tilberedning og mattrygghet. Ved sykdom, graviditet, alvorlig allergi eller særskilte behov skal kvalifisert helsepersonell rådspørres.</p>

<h2>4. KI og menneskelig kontroll</h2>
<p>En ekstern KI-tjeneste brukes til den nåværende produksjonsanalysen. Cibellos egen KI-modell utvikles parallelt, men kan bare trenes i tråd med samtykket og begrensningene som beskrives i <a href="/nb/privacy/">personvernerklæringen</a>. Eksterne KI-svar brukes aldri som treningsfasit. Automatiske resultater skal alltid kunne rettes av brukeren.</p>

<h2>5. Frivillige treningssamtykker</h2>
<p>Tilgang til Cibellos kjernefunksjoner kan ikke gjøres betinget av samtykke til KI-forbedring eller bildetrening. Valget er av fra starten, atskilt fra godkjenningen av vilkårene, og kan endres i Profil.</p>

<h2>6. Konto og sikkerhet</h2>
<p>Brukeren skal oppgi korrekte opplysninger, beskytte innloggingen sin og varsle Cibello om mistenkt misbruk. Kontoen kan slettes i Profil eller via <a href="/nb/delete-account/">nettflyten</a>.</p>

<h2>7. Abonnement og betaling</h2>
<p>Digitale abonnementer i mobilappen kjøpes og administreres via Apple App Store eller Google Play. Cibellos serverstyrte prøveperiode på 14 dager uten kort gjelder én gang per e-postidentitet i løpet av en femårsperiode. En slettet konto kan opprettes på nytt, men gir ikke automatisk en ny gratisperiode. Pris, periode, automatisk fornyelse og oppsigelse vises av den aktuelle butikken før kjøp. Refusjoner håndteres etter butikkens regler og ufravikelig forbrukerlovgivning.</p>

<h2>8. Tillatt bruk</h2>
<p>Tjenesten kan ikke brukes til ulovlig innhold, krenkelser, trakassering, automatisert overbelastning, omgåelse av sikkerhet eller forsøk på å hente ut andre brukeres data. Cibello kan begrense kontoer ved sikkerhetsrisiko eller vesentlig avtalebrudd.</p>

<h2>9. Tilgjengelighet og endringer</h2>
<p>Tjenesten utvikles fortløpende og kan være midlertidig utilgjengelig. Funksjoner kan endres av sikkerhetsmessige, juridiske, kvalitetsmessige eller tekniske grunner. Vesentlige endringer i vilkårene versjonsnummereres og krever ny godkjenning.</p>

<h2>10. Ansvar og ufravikelig rett</h2>
<p>LandveX AB har ansvar i henhold til gjeldende ufravikelig lovgivning. Ingenting i vilkårene begrenser rettigheter som ikke lovlig kan fravikes ved avtale. Svensk rett gjelder, og en forbruker kan også påberope seg ufravikelig rett og kompetent domstol i sitt hjemland.</p>

<h2>11. Kontakt</h2>
<p>Support: <a href="mailto:support@cibello.app">support@cibello.app</a>. Personvern: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>""",
)

DELETE = dict(
    title="Slett konto og data – Cibello",
    desc="Slik sletter du Cibello-kontoen din og tilhørende personopplysninger direkte i appen, og hva du gjør hvis du ikke får åpnet appen.",
    h1="Slett konto og data",
    body="""<h2>Direkte i appen</h2>
<ol>
<li>Logg inn i Cibello.</li>
<li>Åpne <strong>Profil</strong>.</li>
<li>Velg <strong>Slett konto</strong> og bekreft.</li>
</ol>
<p>Kontoen, Firebase-identiteten, aktive bilder og personlige appdata slettes. Økonomiske transaksjonsreferanser kan pseudonymiseres og oppbevares når loven krever det. Sikkerhetskopier roteres ut i henhold til dokumentert oppbevaringstid.</p>

<h2>Hvis du ikke får åpnet appen</h2>
<p>Send forespørselen fra e-postadressen som er registrert på kontoen, til <a href="mailto:privacy@cibello.app?subject=Slett%20Cibello-kontoen%20min">privacy@cibello.app</a>. Skriv «Slett Cibello-kontoen min». Vi bekrefter at du har kontroll over adressen før sletting.</p>

<h2>Treningsdata</h2>
<p>Ved sletting fjernes brukerens rettelser og bildereferanser fra den aktive treningsbanken. Gemini-svar har aldri blitt eksportert som treningsfasit for Cibello AI. Allerede aggregerte modellparametere kan normalt ikke knyttes tilbake til en person.</p>""",
)

UI = dict(
    faq_title="Vanlige spørsmål",
    privacy_nav="Personvern",
    terms_nav="Vilkår",
    delete_nav="Slett konto",
    legal_meta="Cibello · versjon 2.0 · gjelder fra 30. august 2026 · norsk oversettelse",
    translation_label="Om denne oversettelsen:",
    translation_note='Dette er en norsk oversettelse av den svenske originalen (<a href="{sv}" lang="sv">original</a>). Ved avvik gjelder den svenske versjonen.',
)
