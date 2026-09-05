"""Dansk indhold til cibello.app. Struktur: se _schema.py. Renderes af tools/build_lang.py da."""

LANG = "da"

GUIDES = {
    "/da/madplan/": dict(
        title="Madplan til en nemmere og mere varieret uge | Cibello",
        desc="Lav en madplan for ugen ud fra det, du allerede har hjemme. Sådan varierer du retterne, bruger maden i tide og samler det manglende på én indkøbsliste.",
        eyebrow="Madplan og ugeplan",
        h1="Madplan: en nemmere og mere varieret uge",
        lead="En madplan behøver ikke være et skema, du skal følge til punkt og prikke. Det er et udkast, der svarer på spørgsmålet om aftensmaden, før klokken bliver 17. Her får du en enkel metode, og du ser, hvordan Cibello kan hjælpe med at bygge ugen på det, der allerede står i køleskabet.",
        sections=[
            ("Hvorfor en madplan gør hverdagen lettere", """<p>De fleste husstande stiller det samme spørgsmål hver dag: hvad skal vi have til aftensmad? Uden en plan bliver svaret ofte det, der er hurtigst at skaffe, og så ender ugen med flere impulskøb, flere ture i supermarkedet og mad, der bliver glemt bagerst i køleskabet. En madplan for ugen flytter beslutningen til et tidspunkt, hvor du har ro til at tage den.</p><p>Gevinsten er ikke kun tid. Når du ved, hvad der skal laves, kan du købe ind én gang, bruge råvarerne i den rigtige rækkefølge og lade rester indgå i planen i stedet for at smide dem ud. Det er også den enkleste vej til at <a href="/da/mindske-madspild/">mindske madspild</a> i hverdagen.</p>"""),
            ("Begynd med det, der allerede er hjemme", """<p>En god plan starter i dit eget køkken, ikke i en kogebog. Se først, hvad der ligger i køleskab, fryser og skabe, og læg mærke til det, der snart bør bruges: den åbnede pakke feta, de sidste gulerødder, kødet med kort dato. Byg ugens første dage omkring de varer, og gem de holdbare ting til senere på ugen.</p><p>I Cibello tager du et billede af køleskabet eller skabet, og appen genkender varerne og hvor de står. Kvitteringer og stregkoder kan også scannes. Du gennemgår altid resultatet, før det gemmes, fordi AI kan tage fejl på en dato eller overse noget bagerst på hylden. Når madlageret er opdateret, kan appen foreslå <a href="/da/opskrifter-med-ingredienser/">opskrifter med de ingredienser, du allerede har</a>, sorteret efter hvor stor en andel af ingredienserne der findes hjemme.</p>"""),
            ("Variation uden besvær", """<p>En madplan, der gentager den samme hovedråvare tre dage i træk, bliver hurtigt kedelig og ender med at blive droppet. Omvendt behøver du ikke syv nye retter hver uge. Det, der holder i længden, er en blanding: nogle faste hverdagsretter, som alle kan lide, en eller to nye idéer og plads til rester.</p><p>Cibellos ugeplan varierer retter og råvarer, så du ikke får pasta med tomatsovs både mandag og tirsdag, og forslagene vægter det, der snart udløber, og det husstanden plejer at vælge. Til hvert forslag følger en kort forklaring på, hvorfor det kom med. Planen er et udkast: byt dage, stryg retter og læg dine egne favoritter ind, indtil den passer til jeres uge.</p>"""),
            ("Sådan bygger du ugens madplan", """<ol><li><strong>Tjek madlageret.</strong> Fem minutter foran køleskabet eller et billede i appen. Læg mærke til det med kort holdbarhed.</li><li><strong>Vælg retter til de travle dage først.</strong> De aftener, hvor der er sport eller møder, skal have noget hurtigt og velkendt.</li><li><strong>Fyld op med det, der skal bruges.</strong> Lad grøntsager og kød med kort dato styre valget først på ugen.</li><li><strong>Planlæg én ret, der giver rester.</strong> En stor portion suppe, gryderet eller ovnret bliver til frokost eller en aftensmad mere.</li><li><strong>Lad indkøbslisten samle det manglende.</strong> Når retterne ligger i planen, ser du, hvad der faktisk skal købes.</li></ol><p>Det hele behøver ikke være perfekt. En plan for fire dage er bedre end ingen plan, og de sidste dage kan blive restedage eller frit valg.</p>"""),
            ("Madplan for familien", """<p>Med børn i husstanden skal aftensmaden ofte være både hurtig, genkendelig og til at variere uden protester. Her er en struktur, som mange familier finder ro i:</p><table><thead><tr><th>Dag</th><th>Type ret</th></tr></thead><tbody><tr><td>Mandag</td><td>Hurtig hverdagsret med det, der skal bruges først</td></tr><tr><td>Tirsdag</td><td>Fast favorit, som alle kender</td></tr><tr><td>Onsdag</td><td>Stor portion, der giver rester</td></tr><tr><td>Torsdag</td><td>Rester eller noget fra fryseren</td></tr><tr><td>Fredag</td><td>Noget hyggeligt, gerne med børnene i køkkenet</td></tr><tr><td>Weekend</td><td>Én ny ret at prøve og én dag uden plan</td></tr></tbody></table><p>Lad gerne børnene vælge mellem to eller tre forslag. Det giver medbestemmelse uden at åbne hele menukortet. Selve appen er til voksne, og det er dig, der kontrollerer ingredienser og allergener, før noget lander på bordet.</p>"""),
            ("En fælles plan for husstanden", """<p>Den, der planlægger, behøver ikke have det hele i hovedet alene. I Cibello kan husstandens medlemmer dele madlager, madplan og indkøbsliste, så alle ser det samme udgangspunkt. Når én køber mælk eller bruger det sidste løg, kan overblikket opdateres for alle. Det gør dobbeltkøb sjældnere og gør det lettere at bytte om på, hvem der laver mad hvornår.</p><p>Deling er med i de 14 dages prøveperiode og derefter i betalingsplanen. Uanset hvem der har lagt planen, er det stadig den, der står ved komfuret, der tjekker ingredienser og emballage, især ved allergi eller intolerance.</p>"""),
            ("Fra udkast til vane", """<p>Den første uge går sjældent som planlagt, og det er helt i orden. Pointen er ikke at følge planen slavisk, men at have et svar klar, når nogen spørger, hvad vi skal have. Jo oftere madlageret og indkøbslisten holdes opdateret, desto mere brugbare bliver næste uges forslag, fordi appen lærer, hvad husstanden faktisk vælger.</p><p>Cibello træffer ikke beslutningerne for dig. Appen holder overblikket og kommer med forslag, men du bestemmer, hvad der gemmes, byttes eller stryges. Vil du se, hvordan madplanen hænger sammen med resten af appen, kan du starte på <a href="/da/">forsiden for Cibello på dansk</a>.</p>"""),
        ],
        faq=[
            ("Kan Cibello lave en madplan automatisk?", "Cibello kan foreslå en ugeplan, der varierer retter og råvarer og tager højde for det, du har hjemme. Du gennemgår planen og ændrer den, før ugen begynder."),
            ("Tager madplanen højde for maden i køleskabet?", "Ja. Madlageret bruges som udgangspunkt, så råvarer med kort holdbarhed kan komme først på ugen, og indkøbslisten kun indeholder det, der mangler."),
            ("Kan jeg ændre en planlagt ret?", "Ja. Planen er et forslag. Du kan bytte dage, fjerne retter og lægge egne favoritter ind, og det er altid dig, der bestemmer, hvad der gemmes."),
            ("Kan hele husstanden se den samme madplan?", "Ja. Madplan, madlager og indkøbsliste kan deles i husstanden, så alle arbejder ud fra samme overblik. Deling er med i prøveperioden og derefter i betalingsplanen."),
        ],
    ),
    "/da/opskrifter-med-ingredienser/": dict(
        title="Opskrifter med ingredienser, du allerede har | Cibello",
        desc="Find opskrifter ud fra det, der ligger i køleskabet og skabet. Cibello scanner dine varer, viser mulige retter og fortæller, hvad der eventuelt mangler.",
        eyebrow="Aftensmad med det, du har",
        h1="Opskrifter med de ingredienser, du allerede har",
        lead="Det er sjældent mangel på opskrifter, der gør aftensmaden svær. Det er, at halvdelen af ingredienserne ikke er hjemme, når du står i køkkenet klokken 17. Denne guide handler om at vende rækkefølgen om: først køleskabet, så opskriften.",
        sections=[
            ("Hvad skal vi have til aftensmad i dag?", """<p>Spørgsmålet kommer hver dag, og de fleste af os svarer på det på den svære måde: vi finder en ret, vi har lyst til, og opdager bagefter, at der mangler tre ting. Så bliver det enten en ekstra tur i supermarkedet eller noget helt andet end planlagt.</p><p>Den nemmere vej er at begynde med det, der allerede er hjemme. Et halvt blomkål, en rest kylling, en dåse kokosmælk og lidt ris er faktisk en aftensmad. Udfordringen er bare at huske, hvad der ligger der, og at koble det til en ret, der giver mening. Det er præcis det, en opskriftsapp bygget på dit eget madlager kan hjælpe med.</p>"""),
            ("Begynd i køleskabet, ikke i kogebogen", """<p>Når du søger opskrifter ud fra dine egne råvarer, vender du rækkefølgen om. I stedet for at lede efter en ret og derefter købe ind, leder du efter retter, der passer til det, du har, og køber kun det, der mangler. Det sparer penge, sparer tid og er den mest praktiske måde at <a href="/da/mindske-madspild/">mindske madspild</a> på.</p><p>Metoden virker også uden en app: kig i køleskabet, vælg de to eller tre ting, der skal bruges først, og byg retten omkring dem. Men når husstanden har mange varer, flere skabe og en fryser, bliver det svært at holde overblikket i hovedet. Der begynder et digitalt madlager at betale sig.</p>"""),
            ("Fra foto til madlager", """<p>I Cibello tager du et billede af køleskabet, fryseren eller skabet, og appen genkender varerne og hvor de står. Du kan også scanne kvitteringen efter et indkøb eller stregkoden på en enkelt vare. Resultatet vises, før det gemmes, og du retter det, der er tolket forkert: en dato, en mængde eller en vare, appen ikke fik med bagerst på hylden.</p><p>Det er vigtigt at være ærlig om, at AI kan tage fejl. Derfor er din gennemgang ikke et ekstra trin, men selve fundamentet. Et madlager, du har kontrolleret, giver bedre opskriftsforslag og en mere præcis indkøbsliste end et, der aldrig er blevet rettet.</p>"""),
            ("Sådan sorteres forslagene", """<p>Cibello har mere end 9.000 opskrifter. Når madlageret er opdateret, sorteres de efter, hvor stor en andel af ingredienserne du allerede har hjemme, så en ret med næsten alle ingredienser på plads kommer før en, hvor det meste skal købes. Ved hver ret kan du se, hvad der eventuelt mangler, så du selv kan vurdere, om det er værd at handle ind eller vælge noget andet.</p><p>Forslagene vægter også det, der snart udløber, og det husstanden plejer at kunne lide, og de kommer med en kort forklaring på, hvorfor netop den ret blev foreslået. Det gør det lettere at vælge hurtigt uden at skulle bladre gennem hundredvis af opskrifter.</p>"""),
            ("Hverdag, weekend og børn", """<ul><li><strong>Hverdag:</strong> De bedste tirsdagsretter er sjældent de mest avancerede. Pasta, omelet, wok, en enkel gryderet eller en ovnret med det, der er i køleskabet, dækker de fleste aftener.</li><li><strong>Weekend:</strong> Her er der oftere tid til simremad, bagning eller noget at byde gæster på. Planlægger du weekenden allerede i ugen, ligger det, der skal købes, klar på indkøbslisten.</li><li><strong>Børn:</strong> Retter, der ligner de kendte favoritter, men bruger det, der er hjemme, går ofte lettere igennem end noget helt nyt. Lad børnene vælge mellem to forslag; appen er til voksne, og det er dig, der scanner og kontrollerer.</li></ul><p>Vil du lægge retterne ind i en hel uge, kan du læse videre i guiden om <a href="/da/madplan/">madplan for ugen</a>.</p>"""),
            ("Allergier og madvaner", """<p>Du kan angive allergier, intolerancer og madvaner i Cibello, og forslagene tager højde for dem. Men filtrene er vejledning, ikke en garanti. Opskrifter kan indeholde fejl, produkter ændrer indhold, og scanningen kan have tolket en vare forkert. Læs derfor altid ingredienslisten og emballagen selv, især når du laver mad til nogen med alvorlig allergi.</p><p>Det samme gælder næringsværdier, som vises som skøn til planlægning og ikke som ernæringsrådgivning. Har du særlige behov på grund af sygdom eller graviditet, er det fagpersoner, du skal spørge, ikke en app.</p>"""),
            ("Fra idé til indkøbsliste", """<p>Når du har valgt aftensmaden, kan det, der mangler, lægges på husstandens fælles indkøbsliste. Målet er ikke at få dig til at købe mere, men at gøre det tydeligt, hvad der faktisk skal med hjem, så I undgår dobbeltkøb og glemte varer. Listen deles med husstanden i prøveperioden og derefter i betalingsplanen.</p><p>Cibello samler madlager, opskrifter, madplan og indkøb i samme app, så vejen fra "hvad har vi?" til "det laver vi" bliver kort. Du kan læse mere om helheden på <a href="/da/">den danske forside</a> eller se, hvordan Cibello står i forhold til andre opskriftsapps, i den <a href="/en/best-recipe-app/">engelske sammenligning</a>.</p>"""),
        ],
        faq=[
            ("Kan Cibello foreslå opskrifter med rester?", "Ja. Når rester og råvarer er registreret i madlageret, kan de indgå i forslagene, og retter, der bruger dem, kan rykke op på listen."),
            ("Skal jeg skrive alle varer ind manuelt?", "Nej. Du kan tage billeder af køleskab, fryser og skabe og scanne kvitteringer og stregkoder. Resultatet skal altid gennemgås, før det gemmes, fordi AI kan tage fejl."),
            ("Tager Cibello højde for allergier?", "Du kan angive allergier og madvaner, men filtreringen er ingen garanti. Læs altid ingredienser og mærkning selv, især ved alvorlig allergi."),
            ("Hvad sker der, hvis der mangler en ingrediens?", "Appen viser, hvilke ingredienser der mangler i hver ret, så du kan vurdere, om du vil købe dem, lægge dem på indkøbslisten eller vælge en anden ret."),
        ],
    ),
    "/da/mindske-madspild/": dict(
        title="Mindsk madspild med bedre overblik | Cibello",
        desc="Sådan mindsker du madspild i hverdagen: se hvad der er hjemme, brug maden i tide og undgå dobbeltkøb. Cibello forbinder madlager, opskrifter og indkøb.",
        eyebrow="Mindre madspild i hverdagen",
        h1="Mindsk madspild med bedre overblik",
        lead="Det meste af den mad, der smides ud i hjemmet, bliver ikke smidt ud af ligegyldighed. Den bliver glemt. Denne guide handler om de små vaner og det overblik, der gør, at maden bliver brugt, før det er for sent, uden skyldfølelse og uden at gøre køkkenet til et regnskab.",
        sections=[
            ("Hvad er madspild?", """<p>Madspild er mad, der kunne være blevet spist, men som i stedet ender i skraldespanden: rester, der glemmes bagerst i køleskabet, grøntsager, der når at blive bløde, brød, der bliver tørt, og varer, der har passeret datoen, uden at nogen tjekkede, om de stadig var fine. Det er noget andet end skræller, ben og kaffegrums, som ikke kunne spises alligevel.</p><p>I de fleste husstande handler det sjældent om uvilje. Det handler om manglende overblik: flere mennesker, der køber ind, en fryser, ingen rigtig kender indholdet af, og en uge, der sjældent går som planlagt. Det er også derfor, en madplan og et opdateret madlager virker bedre end løfter om at gøre det bedre.</p>"""),
            ("Se hvad der er ved at blive glemt", """<p>Det første skridt er at vide, hvad du har. Et madlager i appen gør det lettere at finde varer i køleskab, fryser og skabe, og når der er oplysninger om holdbarhed, kan Cibello gøre dig opmærksom på det, der bør bruges snart. Påmindelserne er blide og kommer i tide, ikke som en bebrejdelse bagefter.</p><p>Du fylder madlageret ved at tage et billede af køleskabet eller skabet, scanne kvitteringen efter indkøb eller læse en stregkode. Appen genkender varerne og hvor de står, og du gennemgår resultatet, før det gemmes. Datoer og AI-tolkninger kan være forkerte, så brug altid også næsen og øjnene, og følg emballagens anvisninger.</p>"""),
            ("Planlæg opskrifter omkring råvarerne", """<p>I stedet for at købe et helt nyt sæt ingredienser til en ret, du har set et sted, kan du finde retter, der bruger det, der allerede er hjemme. Cibello matcher dit madlager med mere end 9.000 opskrifter og sorterer dem efter, hvor stor en andel af ingredienserne du har. Det, der snart udløber, vægtes højere, og det, der eventuelt mangler, kan lægges på indkøbslisten.</p><p>Guiden om <a href="/da/opskrifter-med-ingredienser/">opskrifter med de ingredienser, du har</a> går mere i dybden med metoden. Kort fortalt: vælg de to eller tre ting, der skal bruges først, og byg aftensmaden omkring dem.</p>"""),
            ("Bedst før og sidste anvendelsesdato", """<p>To mærkninger bliver ofte blandet sammen. <strong>Bedst før</strong> er producentens vurdering af, hvor længe varen har fuld kvalitet. Mange varer er fine længe efter, hvis de er opbevaret rigtigt: se, lugt og smag. <strong>Sidste anvendelsesdato</strong> bruges på letfordærvelige varer som fersk kød og fisk og skal respekteres.</p><ul><li>Stil det, der skal bruges først, forrest i køleskabet.</li><li>Frys ned, mens maden stadig er god, ikke dagen efter datoen.</li><li>Tjek fryseren en gang om måneden, så den ikke bliver et arkiv.</li></ul><p>Ingen app kan garantere, at mad er sikker at spise. Vær ekstra forsigtig med mad til små børn, gravide og personer med svækket immunforsvar.</p>"""),
            ("Rester er også mad", """<p>En stor portion gryderet eller en ovnret giver ofte mad til to dage. Problemet er sjældent at lave resterne, men at huske dem. I Cibello kan rester og madkasser lægges ind i madlageret ligesom andre varer, så de er med i overblikket og kan indgå i forslagene til de næste måltider. Planlægger du ugen på forhånd, kan du sætte en <a href="/da/madplan/">restedag i madplanen</a>, så resterne får en plads i stedet for at blive skubbet længere og længere ind.</p>"""),
            ("Del overblikket i husstanden", """<p>Når flere køber ind, sker dobbeltkøb tit: to poser salat, tre pakker smør. Med et fælles madlager og en fælles indkøbsliste ser alle det samme, og listen indeholder kun det, der faktisk mangler. Deling er med i prøveperioden og derefter i betalingsplanen.</p><p>Cibello bruger hverken skam eller kaloriepres. Målet er en roligere og mere praktisk madhverdag, hvor maden bliver brugt, fordi det er nemt, ikke fordi nogen holder øje.</p>"""),
            ("Små vaner, der gør en forskel", """<ul><li>Tag et billede af køleskabet, før du skriver indkøbslisten.</li><li>Planlæg ugens første to dage omkring det, der skal bruges snart.</li><li>Lav én restevenlig ret om ugen, og sæt en dag af til den.</li><li>Hold en "brug mig først"-hylde i køleskabet.</li><li>Frys brød, krydderurter og rester i portioner, du faktisk kommer til at bruge.</li></ul><p>Cibello minder blidt om og foreslår retter, men det er dig, der afgør, hvad der skal spises, fryses eller kasseres. Læs mere om, hvordan appen hænger sammen, på <a href="/da/">den danske forside</a>.</p>"""),
        ],
        faq=[
            ("Kan en app garantere, at maden stadig er sikker at spise?", "Nej. Kontrollér altid dato, opbevaring, lugt, udseende og emballagens oplysninger selv. Appen giver overblik og påmindelser, ikke garantier."),
            ("Hvordan hjælper opskrifter med at mindske madspild?", "Opskrifter ud fra madlageret gør det lettere at bruge de råvarer, I allerede har, før I køber nyt. Det, der snart udløber, vægtes højere i forslagene."),
            ("Kan flere personer opdatere det samme madlager?", "Ja. Husstandsfunktionen er lavet til et fælles overblik over madlager, madplan og indkøbsliste. Den er med i prøveperioden og derefter i betalingsplanen."),
            ("Får jeg besked, før maden bliver dårlig?", "Ja. Når der er oplysninger om holdbarhed på varen, kan Cibello minde dig blidt om det, der bør bruges snart. Datoerne skal gennemgås, når varen gemmes, fordi AI kan tage fejl."),
        ],
    ),
}

HUBTEXT = """<section><h2>Begynd med det, du har</h2><p>De fleste mad-apps begynder med opskrifter. Cibello begynder i dit køkken. Du tager et billede af køleskabet, fryseren eller skabet, og appen genkender varerne og hvor de står. Kvitteringer og stregkoder kan også scannes. Du gennemgår resultatet, før det gemmes, fordi AI kan tage fejl på en dato eller overse noget bagerst på hylden. Når madlageret er på plads, kan appen vise <a href="/da/opskrifter-med-ingredienser/">opskrifter med de ingredienser, du allerede har</a>, sorteret efter hvor stor en andel der findes hjemme, og med besked om det, der eventuelt mangler.</p></section>
<section><h2>Fra køleskab til madplan</h2><p>Når du ved, hvad der er hjemme, bliver det lettere at planlægge ugen. Cibello foreslår en ugeplan, der varierer retter og råvarer og vægter det, der snart bør bruges. Du bytter dage, stryger retter og lægger egne favoritter ind, og indkøbslisten samler kun det, der faktisk skal købes. Husstanden kan dele madlager, madplan og liste, så alle ser det samme. Læs mere i guiden om <a href="/da/madplan/">madplan for ugen</a>.</p></section>
<section><h2>Mindre madspild, mere ro</h2><p>Mad smides sjældent ud af ligegyldighed. Den bliver glemt. Med oplysninger om holdbarhed i madlageret kan Cibello minde dig blidt om det, der bør bruges snart, og foreslå retter, der bruger det. Rester kan lægges ind som andre varer, så de også er med i overblikket. Guiden om at <a href="/da/mindske-madspild/">mindske madspild</a> samler de vaner, der gør en forskel i hverdagen.</p></section>
<section><h2>Et støtteværktøj, ikke en dommer</h2><p>Cibello træffer ikke beslutningerne for dig. Opskrifts- og allergifiltre er vejledning, ikke garanti, og næringsværdier er skøn. Du bestemmer altid, hvad der gemmes, laves og købes. Appen findes på tolv sprog, dine data opbevares i EU, og du kan prøve den i 14 dage uden at oplyse kort. Appen er til voksne fra 18 år.</p></section>"""

ABOUT = dict(
    title="Om Cibello: appen og virksomheden bag | LandveX AB",
    desc="Cibello er udviklet af LandveX AB i Tyresö, Sverige. Hvorfor appen findes, hvordan vi tænker om AI, data og madspild, og hvordan du kontakter os.",
    h1="Om Cibello",
    lead="Cibello er en svensk mad-app fra LandveX AB. Den er lavet for at svare på et spørgsmål, der stilles i næsten alle husstande hver dag: hvad skal vi have at spise? Her kan du læse, hvad vi forsøger at gøre, hvordan vi arbejder med AI og data, og hvordan du kommer i kontakt med os.",
    sections=[
        ("Hvorfor Cibello findes", """<p>De fleste opskriftsapps begynder med opskrifter. Vi ville begynde i køkkenet: hvad der faktisk ligger i køleskab, fryser og skabe, hvad der snart udløber, og hvad husstanden plejer at kunne lide. Derfor er kernen i Cibello et madlager, din "Food Twin", bygget op af billeder, kvitteringer og stregkoder. Opskrifter, ugeplan, indkøbsliste og påmindelser hviler alle på de samme data. Målet er mindre stress i hverdagen og <a href="/da/mindske-madspild/">mindre madspild</a>, uden løftede pegefingre.</p>"""),
        ("Sådan tænker vi om AI", """<p>AI gør Cibello muligt, men den tager af og til fejl. En scanning kan læse en vare forkert, overse noget bagerst på hylden eller gætte en forkert dato. Derfor gennemgår du altid resultatet, før det gemmes, og derfor er forslag kun forslag. Opskrifts- og allergifiltre er vejledning, aldrig en garanti, og næringsværdier er skøn til planlægning, ikke ernæringsrådgivning. Cibellos egne modeller trænes kun på dine rettelser og, hvis du siger ja til det separat, på sanerede billeder. Begge valg er slået fra fra start. Se <a href="/da/privacy/">privatlivspolitikken</a>.</p>"""),
        ("Dine data", """<p>Alt opbevares i EU. Du kan se dine data i appen og <a href="/da/delete-account/">slette din konto</a>, når du vil, uden at kontakte support. Vi sælger ikke personoplysninger.</p>"""),
        ("Virksomheden", """<p>Cibello udvikles og ejes af LandveX AB, org.nr 559141-7042, Antennvägen 2, 135 48 Tyresö, Sverige. Appen findes til iOS og Android på tolv sprog og er udviklet i Sverige. Indtil videre er den beregnet til personer på 18 år eller derover, fordi vilkårene for den AI-tjeneste, appen bruger, kræver voksne brugere. Prøveperioden er 14 dage uden kort.</p>"""),
        ("Kontakt", """<p>Generelle spørgsmål og samarbejder: <a href="mailto:hello@cibello.app">hello@cibello.app</a>. Support: <a href="mailto:support@cibello.app">support@cibello.app</a>. Privatliv og databeskyttelse: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>. Pressehenvendelser er velkomne på samme adresse; vi svarer normalt inden for et par hverdage. Se også <a href="/da/press/">pressesiden</a> og <a href="/da/news/">nyt hos Cibello</a>.</p><p>Følg os på <a href="https://www.instagram.com/cibelloapp/" rel="noopener">Instagram</a>, <a href="https://www.tiktok.com/@cibello73" rel="noopener">TikTok</a> og <a href="https://www.facebook.com/profile.php?id=61593336222919" rel="noopener">Facebook</a>.</p>"""),
    ],
)

PRESS = dict(
    title="Presse og medier: fakta, billeder og kontakt | Cibello",
    desc="Pressemateriale om Cibello: kort beskrivelse, fakta om appen, logo og billeder samt pressekontakten hos LandveX AB. Frit til redaktionel brug.",
    eyebrow="Til journalister og skribenter",
    h1="Presse og medier",
    lead="Alt, du har brug for, når du skriver om Cibello: en kort beskrivelse, fakta, billeder og en kontakt, der svarer hurtigt. Alt på denne side må bruges frit i redaktionel sammenhæng.",
    sections=[
        ("Cibello kort fortalt", """<p>Cibello er en svensk mad-app, der fotograferer dit køleskab og dine skabe, holder et madlager med placering og datoer, foreslår opskrifter ud fra det, der faktisk er hjemme, planlægger ugen og deler indkøbslisten med husstanden. Den minder blidt om, før maden bliver dårlig, og dømmer aldrig, hvad nogen spiser. Findes til iOS og Android på tolv sprog, med data opbevaret i EU, udviklet af LandveX AB i Tyresö, Sverige.</p><p><strong>Én sætning:</strong> Cibello er appen, der ser, hvad du har hjemme, og svarer på spørgsmålet "hvad skal vi have at spise?".</p>"""),
        ("Fakta", """<ul><li>Findes til iOS og Android. Aldersgrænse 18 år.</li><li>Prøveperiode: 14 dage uden kort, derefter abonnement via App Store eller Google Play.</li><li>Opskrifter: mere end 9.000, matchet mod brugerens madlager.</li><li>Sprog: svensk, engelsk, tysk, fransk, spansk, italiensk, hollandsk, polsk, dansk, norsk, finsk, portugisisk.</li><li>Data: opbevares i EU. Konto og data kan slettes i appen.</li><li>AI: scanning af køleskab, skabe, kvitteringer og stregkoder. Brugeren gennemgår altid resultatet. Cibellos egne modeller trænes kun på brugerens rettelser og, med separat samtykke, sanerede billeder.</li><li>Pris: gratis prøveperiode, derefter betalingsplan for husstandsfunktioner. Aktuelle priser i App Store og Google Play.</li><li>Virksomhed: LandveX AB, org.nr 559141-7042, Antennvägen 2, 135 48 Tyresö, Sverige.</li></ul>"""),
        ("Logo og billeder", """<ul><li><a href="/img/icon-512.png">App-ikon, 512×512 PNG</a></li><li><a href="/img/og-da.png">Delingsbillede, 1200×630 PNG (dansk)</a></li><li><a href="/img/og.png">Delingsbillede, 1200×630 PNG (svensk)</a></li><li><a href="/favicon.svg">Symbol, SVG</a></li></ul><p>Skærmbilleder fra appen sendes på forespørgsel. Billederne må bruges frit i redaktionel sammenhæng med angivelse af Cibello som kilde.</p>"""),
        ("Pressekontakt", """<p><a href="mailto:hello@cibello.app?subject=Pressehenvendelse">hello@cibello.app</a>. Vi svarer normalt på pressehenvendelser inden for én hverdag. Grundlæggeren stiller gerne op til interview om madspild i husholdningerne, AI i hverdagen, og hvorfor "hvad skal vi have at spise?" er et spørgsmål, der er værd at løse.</p><p>Mere om virksomheden: <a href="/da/about/">Om Cibello</a>. Seneste opdateringer: <a href="/da/news/">Nyt hos Cibello</a>.</p>"""),
    ],
)

NEWS = dict(
    title="Nyt hos Cibello: opdateringer og nye guider",
    desc="Nye guider, værktøjer og opdateringer på cibello.app med dato. Følg med via RSS.",
    h1="Nyt hos Cibello",
    lead="Det, der er kommet til på sitet og i appen, nyeste først. Der findes et RSS-feed.",
    rss_label="RSS-feed",
    entries=[
        ("2026-09-04", "Ny guide: madspild i Sverige i tal", "/matsvinn-statistik/", "Officielle tal fra de svenske myndigheder Naturvårdsverket og Livsmedelsverket samlet på én side (på svensk): 880.000 ton madspild, 16 kg spiselig mad pr. person i husholdningerne og 1.330 svenske kroner pr. person om året, med kilde til hvert tal."),
        ("2026-09-04", "Tre nye engelske guider og to sammenligninger", "/en/best-meal-planning-app/", "Hvad skal vi have til aftensmad, AI-madplanlægger og køkkenskabsapp, samt ærlige sammenligninger af madplan-apps og opskriftsapps med Mealime, Samsung Food, Plan to Eat, Paprika og SuperCook."),
        ("2026-09-04", "Fulde landingssider på tolv sprog", "/da/", "Alle sprog har nu en komplet landingsside i stedet for en kort tekstside, og intet oversættes længere i browseren. Den danske side samler guiderne om madplan, opskrifter med det du har, og mindre madspild."),
        ("2026-08-30", "Privatlivspolitik og brugervilkår version 2.0", "/da/privacy/", "Opdaterede tekster om Gemini-analyse, den frivillige træning af Cibello AI, de 14 dages prøveperiode uden kort og aldersgrænsen på 18 år. Danske oversættelser findes; den svenske version gælder."),
    ],
)

PRIVACY = dict(
    title="Privatlivspolitik – Cibello",
    desc="Sådan behandler Cibello personoplysninger, billeder, Gemini-analyse og frivillig træning af Cibello AI. Dansk oversættelse af den svenske politik, version 2.0.",
    h1="Privatlivspolitik",
    notice="<strong>Kort fortalt:</strong> En ekstern AI-tjeneste bruges til den aktuelle billedanalyse. Cibellos egen AI-model må kun trænes på brugerens egne rettelser og sanerede billeder efter et separat, frivilligt og aktivt valg i introduktionen. Eksterne AI-svar bruges aldrig som træningsfacit.",
    body="""<h2>1. Dataansvarlig</h2>
<p>LandveX AB, org.nr 559141-7042, Antennvägen 2, 135 48 Tyresö, Sverige, er dataansvarlig for Cibello. Spørgsmål om privatliv sendes til <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>

<h2>2. Oplysninger og formål</h2>
<ul>
<li><strong>Konto:</strong> e-mailadresse, visningsnavn, autentificeringsidentitet og sikkerhedslogs for at oprette og beskytte kontoen.</li>
<li><strong>Mad- og husstandsdata:</strong> madlager, opskrifter, præferencer, allergier og egne rettelser til appens funktioner.</li>
<li><strong>Billeder:</strong> billeder, som brugeren vælger at scanne for at identificere madvarer eller kvitteringer.</li>
<li><strong>Betaling:</strong> abonnementsstatus og transaktionsreferencer. Kort- og betalingsoplysninger håndteres af Apple App Store eller Google Play.</li>
<li><strong>Tekniske data:</strong> fejl, ydeevne og produktanalyse, kun i overensstemmelse med brugerens valg og nødvendige sikkerhedsbehov.</li>
<li><strong>Beskyttelse mod misbrug af gratisperioden:</strong> et nøglet, pseudonymt HMAC-fingeraftryk af den normaliserede e-mailadresse opbevares i højst fem år. Det kan ikke bruges til login eller kontakt og indeholder hverken adressen i klartekst, bruger-id eller Firebase-identitet. Formålet er alene at forhindre gentagne gratisperioder efter sletning af kontoen og ny registrering.</li>
</ul>

<h2>3. Gemini i produktion</h2>
<p>Valgte billeder og den nødvendige instruktion sendes til Google Gemini API for at skabe det resultat, der vises i appen. Cibello bruger den betalte tjeneste inden for EØS. Ifølge Googles vilkår bruges data i den betalte tjeneste ikke til at forbedre Googles produkter, men begrænset logning kan forekomme af hensyn til sikkerhed og bekæmpelse af misbrug, medmindre en særlig nul-opbevaringstilstand gælder. Cibello lover derfor ikke nul-opbevaring uden for sit eget miljø uden teknisk bekræftelse fra leverandøren.</p>
<p>Gemini-resultater er automatiske skøn. Brugeren skal kontrollere indhold, allergener, datoer og mængder, før oplysningerne bruges.</p>

<h2>4. Cibellos egen AI-model: separat og frivillig træning</h2>
<p>Cibello udvikler sin egen AI-model. Træningsforløbet er teknisk og juridisk adskilt fra den eksterne AI-tjeneste, der giver brugeren de aktuelle resultater:</p>
<ul>
<li>Gemini-svar, ræsonnementer eller forslag eksporteres aldrig som træningsetiketter eller træningsfacit til Cibellos egen AI-model.</li>
<li><strong>Anonymiseret AI-forbedring</strong> tillader, at brugerens udtrykkelige rettelse eller manuelt bekræftede facit bruges uden billede.</li>
<li><strong>Billedtræning</strong> tillader, at en saneret kopi af brugerens billede knyttes til den egne rettelse. Metadata fjernes, og billedet begrænses i størrelse, før det gemmes.</li>
<li>Introduktionen viser ét fælles, tydeligt valg for disse to dele af samme træningsformål. Valget er ikke forudvalgt, og appen fungerer, også hvis brugeren ikke giver samtykke.</li>
<li>Samtykket kan trækkes tilbage med en knap under Profil. Så stoppes fremtidig brug, den appejede aktive træningsbank ryddes, og billedreferencer fjernes. Allerede fremstillede, aggregerede modelparametre kan normalt ikke føres tilbage til en person.</li>
<li>Cibello AI påvirker ikke produktionssvaret, før dokumenterede benchmark- og sikkerhedsgrænser er nået.</li>
</ul>

<h2>5. Retsgrundlag</h2>
<p>Konto og kernefunktioner behandles for at opfylde aftalen. Sikkerhedslogning og det begrænsede fingeraftryk til at modvirke gentagne gratisperioder behandles på grundlag af legitim interesse. Retlige forpligtelser kan kræve anden begrænset behandling. Frivillig produktanalyse, AI-forbedring og billedtræning bygger på separate samtykker, der kan trækkes tilbage.</p>

<h2>6. Opbevaring og modtagere</h2>
<p>Oplysninger opbevares i den tid, der kræves af hensyn til tjenesten, sikkerhed, retlige krav og dokumenteret backup-opbevaring. Leverandører kan omfatte AWS til drift og lagring, Firebase til autentificering, Google Gemini til valgt AI-analyse samt Apple eller Google til betaling. Cibello sælger ikke personoplysninger. Fingeraftrykket for gratisperioden slettes automatisk senest fem år efter, at prøveperioden begyndte.</p>

<h2>7. Dine rettigheder</h2>
<p>Du kan anmode om indsigt, berigtigelse, dataportabilitet, begrænsning eller sletning og gøre indsigelse mod visse former for behandling. Samtykker ændres under Profil. Kontoen kan slettes direkte i appen eller via <a href="/da/delete-account/">siden om sletning af konto</a>. Du kan også kontakte den svenske tilsynsmyndighed Integritetsskyddsmyndigheten.</p>

<h2>8. Alder</h2>
<p>Cibello er indtil videre beregnet til personer, der er mindst 18 år, fordi vilkårene for den anvendte Gemini API-tjeneste kræver voksne brugere. Alderskravet tages op til fornyet vurdering, hvis den tekniske leverandørløsning ændres.</p>

<h2>9. Ændringer</h2>
<p>Væsentlige ændringer får versionsnummer og kræver en ny accept i appen før fortsat brug.</p>""",
)

TERMS = dict(
    title="Brugervilkår – Cibello",
    desc="Brugervilkår for Cibello: konto, aldersgrænse, abonnement og 14 dages prøveperiode, AI-analyse og sikker brug. Dansk oversættelse af de svenske vilkår, version 2.0.",
    h1="Brugervilkår",
    body="""<h2>1. Aftale og aldersgrænse</h2>
<p>Disse vilkår gælder mellem brugeren og LandveX AB, org.nr 559141-7042. Cibello er indtil videre kun for personer, der er mindst 18 år. Ved at oprette en konto bekræfter brugeren sin alder og accepterer vilkårene samt <a href="/da/privacy/">privatlivspolitikken</a>.</p>

<h2>2. Tjenesten</h2>
<p>Cibello hjælper brugeren med at organisere mad, tolke valgte billeder og kvitteringer samt få opskrifts- og måltidsforslag. Resultater kan være ufuldstændige eller forkerte og skal gennemgås af brugeren.</p>

<h2>3. Ingen medicinsk eller professionel rådgivning</h2>
<p>Cibello giver inspiration og generel information, ikke medicinsk, diætetisk, allergi- eller anden professionel rådgivning. Brugeren er ansvarlig for at kontrollere ingredienser, allergener, portionsstørrelse, holdbarhed, tilberedning og fødevaresikkerhed. Ved sygdom, graviditet, svær allergi eller særlige behov skal kvalificeret sundhedspersonale rådspørges.</p>

<h2>4. AI og menneskelig kontrol</h2>
<p>En ekstern AI-tjeneste bruges til den nuværende produktionsanalyse. Cibellos egen AI-model udvikles parallelt, men må kun trænes i overensstemmelse med det samtykke og de begrænsninger, der beskrives i <a href="/da/privacy/">privatlivspolitikken</a>. Eksterne AI-svar bruges aldrig som træningsfacit. Automatiske resultater skal altid kunne rettes af brugeren.</p>

<h2>5. Frivillige træningssamtykker</h2>
<p>Adgang til Cibellos kernefunktioner må ikke gøres betinget af samtykke til AI-forbedring eller billedtræning. Valget er slået fra fra start, adskilt fra accepten af vilkårene og kan ændres under Profil.</p>

<h2>6. Konto og sikkerhed</h2>
<p>Brugeren skal give korrekte oplysninger, beskytte sit login og underrette Cibello om mistanke om misbrug. Kontoen kan slettes under Profil eller via <a href="/da/delete-account/">webforløbet</a>.</p>

<h2>7. Abonnement og betaling</h2>
<p>Digitale abonnementer i mobilappen købes og administreres via Apple App Store eller Google Play. Cibellos serverstyrede prøveperiode på 14 dage uden kort gælder én gang pr. e-mailidentitet inden for en femårsperiode. En slettet konto kan oprettes igen, men giver ikke automatisk en ny gratisperiode. Pris, periode, automatisk fornyelse og opsigelse vises af den respektive butik før køb. Refusioner håndteres efter butikkens regler og ufravigelig forbrugerlovgivning.</p>

<h2>8. Tilladt brug</h2>
<p>Tjenesten må ikke bruges til ulovligt indhold, krænkelser, chikane, automatiseret overbelastning, omgåelse af sikkerhed eller forsøg på at udtrække andre brugeres data. Cibello kan begrænse konti ved sikkerhedsrisiko eller væsentligt aftalebrud.</p>

<h2>9. Tilgængelighed og ændringer</h2>
<p>Tjenesten udvikles løbende og kan være midlertidigt utilgængelig. Funktioner kan ændres af sikkerhedsmæssige, retlige, kvalitetsmæssige eller tekniske grunde. Væsentlige ændringer af vilkårene får versionsnummer og kræver ny accept.</p>

<h2>10. Ansvar og ufravigelig lovgivning</h2>
<p>LandveX AB er ansvarlig i henhold til gældende ufravigelig lovgivning. Intet i vilkårene begrænser rettigheder, der ikke lovligt kan fraviges ved aftale. Svensk ret gælder, og en forbruger kan også påberåbe sig ufravigelige regler og den kompetente domstol i sit hjemland.</p>

<h2>11. Kontakt</h2>
<p>Support: <a href="mailto:support@cibello.app">support@cibello.app</a>. Privatliv: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>""",
)

DELETE = dict(
    title="Slet konto og data – Cibello",
    desc="Sådan sletter du din Cibello-konto og de tilhørende personoplysninger direkte i appen, eller via e-mail hvis du ikke kan åbne appen.",
    h1="Slet konto og data",
    body="""<h2>Direkte i appen</h2>
<ol>
<li>Log ind i Cibello.</li>
<li>Åbn <strong>Profil</strong>.</li>
<li>Vælg <strong>Slet konto</strong>, og bekræft.</li>
</ol>
<p>Kontoen, Firebase-identiteten, aktive billeder og personlige appdata slettes. Økonomiske transaktionsreferencer kan pseudonymiseres og gemmes, når loven kræver det. Backups roteres ud i henhold til dokumenteret opbevaringstid.</p>

<h2>Hvis du ikke kan åbne appen</h2>
<p>Send anmodningen fra den e-mailadresse, der er registreret på kontoen, til <a href="mailto:privacy@cibello.app?subject=Slet%20min%20Cibello-konto">privacy@cibello.app</a>. Skriv "Slet min Cibello-konto". Vi bekræfter, at du har kontrol over adressen, før sletningen gennemføres.</p>

<h2>Træningsdata</h2>
<p>Ved sletning fjernes brugerens rettelser og billedreferencer fra den aktive træningsbank. Gemini-svar er aldrig blevet eksporteret som træningsfacit til Cibello AI. Allerede aggregerede modelparametre kan normalt ikke føres tilbage til en person.</p>""",
)

UI = dict(
    faq_title="Ofte stillede spørgsmål",
    privacy_nav="Privatlivspolitik",
    terms_nav="Brugervilkår",
    delete_nav="Slet konto",
    legal_meta="Cibello · version 2.0 · gælder fra 30. august 2026 · dansk oversættelse",
    translation_label="Om denne oversættelse:",
    translation_note='Dette er en dansk oversættelse af den svenske original (<a href="{sv}" lang="sv">original</a>). Ved uoverensstemmelse gælder den svenske version.',
)
