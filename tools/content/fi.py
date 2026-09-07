"""Finnish content for cibello.app. Structure follows tools/content/_schema.py."""

LANG = "fi"

GUIDES = {
    "/fi/ateriasuunnittelu/": dict(
        title="Ateriasuunnittelu ja viikon ruokalista | Cibello",
        desc="Viikon ruokalista siitä, mitä kotona jo on. Cibello ehdottaa vaihtelevan suunnitelman, sinä muokkaat sen, ja puuttuvat ainekset siirtyvät ostoslistalle.",
        eyebrow="Viikko kerrallaan, ilman stressiä",
        h1="Ateriasuunnittelu ja viikon ruokalista, joka joustaa arjessa",
        lead="Viikon ruokalista ei tarkoita seitsemää uutta reseptiä. Cibello ehdottaa vaihtelevan suunnitelman sen mukaan, mitä jääkaapissa, pakastimessa ja kaapeissa jo on, ja sinä tarkistat ja muokkaat sen ennen viikon alkua. Puuttuvat ainekset kertyvät yhteiselle ostoslistalle.",
        sections=[
            ("Miksi viikon ruokalista helpottaa arkea", """<p>Kysymys ”mitä tänään syötäisiin” osuu yleensä huonoimpaan hetkeen: kello on viisi, kaikilla on nälkä ja jääkaapin ovi on jo auki. Ateriasuunnittelu siirtää päätöksen rauhallisempaan hetkeen. Kun viikon ruokalista on kerran mietitty, arki-illat sujuvat ilman jokapäiväistä neuvottelua, ja kauppaan mennään yhden listan kanssa sen sijaan, että joka päivä käydään hakemassa jotain.</p><p>Suunnitelman ei tarvitse olla täydellinen. Riittää, että se antaa suunnan ja jättää tilaa muutoksille. Kestävä viikkosuunnitelma rakentuu useimmissa perheissä muutamasta tutusta arkiruoasta, yhdestä tai kahdesta uudesta ideasta ja tilasta tähteille.</p><p>Viikon ruokalistan voi tehdä viidessä vaiheessa:</p><ol><li>Katso, mitä kotona jo on ja mikä pitäisi käyttää ensin.</li><li>Merkitse viikon poikkeukset: harrastusillat, vieraat ja päivät, jolloin joku syö muualla.</li><li>Valitse pari tuttua arkiruokaa ja korkeintaan yksi tai kaksi uutta reseptiä.</li><li>Jätä yksi päivä tähteille tai ruokalaatikoille.</li><li>Kokoa puuttuvat ainekset yhdelle ostoslistalle.</li></ol>"""),
            ("Aloita siitä, mitä kotona jo on", """<p>Cibellossa suunnittelu ei ala reseptikirjasta vaan omasta keittiöstä. Kuvaa jääkaappi, pakastin ja kaapit, niin sovellus tunnistaa tuotteet ja sen, missä ne ovat. Kuitit ja viivakoodit voi skannata samalla tavalla. Tekoäly voi tulkita jotain väärin, joten tarkistat tuloksen ennen tallennusta ja korjaat sen tarvittaessa.</p><p>Kun ruokavarasto on ajan tasalla, Cibello vertaa sitä yli 9 000 reseptiin ja järjestää ne sen mukaan, kuinka suuri osa aineksista löytyy kotoa. Viikon ruokalistan pohja syntyy siis ruoasta, joka on jo ostettu, ei ruoasta, joka pitäisi vielä hakea. Lue lisää oppaasta <a href="/fi/reseptit-aineksista/">reseptejä aineksista, joita sinulla jo on</a>.</p>"""),
            ("Vaihtelua ilman turhaa vaivaa", """<p>Automaattisen suunnitelman heikkous on toisto: sama pääraaka-aine kolmena päivänä peräkkäin tai sama ruoka lounaaksi ja päivälliseksi. Cibellon viikkosuunnitelma vaihtelee ruokalajeja, raaka-aineita ja ateriatyyppejä, ja jokaisen ehdotuksen kohdalla näet, miksi se on mukana: ehkä kerma vanhenee pian tai talous on aiemmin pitänyt samantyyppisestä ruoasta.</p><p>Käytännössä se näkyy niin, että jos maanantaina on kanaa, tiistaille ehdotetaan jotain muuta, ja keittopäivän jälkeen tulee ruoka, jossa on eri rakenne. Kasvisruoat, kala, liha ja pastaruoat vuorottelevat sen mukaan, mitä ruokavarastossa on ja mistä taloutenne on pitänyt. Jos ehdotus ei osu, vaihdat sen, ja sovellus oppii valinnastasi ensi kertaa varten.</p><p>Ehdotus on luonnos. Vaihda päiviä, poista ruokia ja lisää omia suosikkejasi ennen kuin viikko alkaa.</p>"""),
            ("Käytä ruoka oikeassa järjestyksessä", """<p>Lyhyen säilyvyyden tuotteet ansaitsevat paikan viikon alussa. Kun ruokavarasto ja viikkosuunnitelma ovat samassa sovelluksessa, on helpompi laittaa tuore kala tai avattu kermapurkki maanantaille ja säästää säilyvät ainekset loppuviikkoon. Cibello muistuttaa lempeästi, kun jokin pitäisi käyttää pian, mutta päiväykset ja tekoälyn tulkinnat voivat olla vääriä, joten katso, haista ja noudata pakkauksen ohjeita.</p><p>Pakastin on tässä hyvä apuri. Jos huomaat, ettei jokin ehdi käyttöön, pakasta se ja kirjaa ruokavarastoon, niin se on mukana seuraavan viikon ehdotuksissa eikä katoa pakastimen pohjalle.</p><p>Myös ruokalaatikot voivat olla mukana ruokavarastossa, jolloin ne eivät jää pakastimen perälle unohduksiin. Miten tämä vähentää hävikkiä, kerrotaan oppaassa <a href="/fi/vahenna-ruokahavikkia/">vähennä ruokahävikkiä</a>.</p>"""),
            ("Esimerkki viikon rungosta", """<p>Näin monen perheen viikko voisi näyttää. Runko on vain lähtökohta, jonka sovitat omaan arkeenne.</p><table><thead><tr><th scope="col">Päivä</th><th scope="col">Ajatus</th></tr></thead><tbody><tr><td>Maanantai</td><td>Käytä pian vanhenevat tuotteet, esimerkiksi tuore kala tai avattu pakkaus</td></tr><tr><td>Tiistai</td><td>Tuttu arkiruoka, jonka kaikki syövät</td></tr><tr><td>Keskiviikko</td><td>Uusi resepti, jonka ainekset ovat pääosin jo kotona</td></tr><tr><td>Torstai</td><td>Nopea ruoka pakastimen ja kaapin aineksista</td></tr><tr><td>Perjantai</td><td>Rennompi ruoka, jota lapsetkin odottavat</td></tr><tr><td>Lauantai</td><td>Enemmän aikaa: pata, uuniruoka tai leivonta</td></tr><tr><td>Sunnuntai</td><td>Tähteet ja ruokalaatikot, kaappi tyhjäksi ennen uutta viikkoa</td></tr></tbody></table>"""),
            ("Yhteinen suunnitelma koko taloudelle", """<p>Se, joka suunnittelee, ei tarvitse pitää kaikkea päässään. Talouden jäsenet näkevät saman viikkosuunnitelman ja saman ostoslistan, ja kun joku ostaa tai käyttää jotain, muutos näkyy kaikille. Yhteinen näkymä kuuluu kokeilujaksoon ja sen jälkeen maksulliseen tilaukseen.</p><p>Käytännössä se tarkoittaa, että kaupassa käyvä näkee listan puhelimestaan, kokkaava näkee suunnitelman, eikä kumpikaan tarvitse viestiä siitä, onko maitoa vielä jäljellä.</p><p>Jaettu suunnitelma ei poista omaa tarkistusta: jokainen resepti kannattaa lukea läpi allergioiden, ainesosien ja pakkausmerkintöjen osalta. Resepti- ja allergiasuodattimet ovat ohjeellisia, eivät takuu.</p>"""),
            ("Ehdotuksesta arjen rutiiniksi", """<p>Hyvä suunnitelma on sellainen, jota oikeasti käytetään. Kun ruokavarasto ja ostoslista pysyvät ajan tasalla, seuraavan viikon ehdotukset osuvat paremmin, ja päätökset siirtyvät arki-illoista siihen hetkeen, jolloin sinulla on aikaa ajatella. Cibello ei päätä puolestasi; se kokoaa tiedot yhteen paikkaan ja ehdottaa, ja sinä valitset.</p><p>Aloita pienestä. Suunnittele ensin kolme tai neljä päivää, ei koko viikkoa. Kun se tuntuu luontevalta, laajenna. Moni huomaa, että jo puolikas viikko riittää poistamaan suurimman osan iltapäivän arvailusta.</p><p>Jos mietit, miten Cibello eroaa muista ateriasuunnittelusovelluksista, katso englanninkielinen <a href="/en/best-meal-planning-app/">vertailu</a>. Kaikki suomenkieliset oppaat löytyvät <a href="/fi/">Cibellon etusivulta</a>.</p>"""),
        ],
        faq=[
            ("Voiko Cibello tehdä viikon ruokalistan automaattisesti?", "Cibello ehdottaa vaihtelevan viikkosuunnitelman ruokavaraston, päiväysten ja talouden tottumusten perusteella. Sinä tarkistat ja muokkaat sen ennen tallentamista."),
            ("Ottaako suunnitelma huomioon kotona olevan ruoan?", "Kyllä. Ruokavarasto toimii suunnittelun pohjana, ja pian vanhenevat tuotteet voidaan nostaa viikon alkuun."),
            ("Voinko muuttaa suunniteltua ateriaa?", "Kyllä. Suunnitelma on ehdotus: voit vaihtaa päiviä, poistaa ruokia ja lisätä omia suosikkeja milloin tahansa."),
            ("Näkevätkö muut taloudessa saman suunnitelman?", "Kyllä. Talouden jäsenet jakavat viikkosuunnitelman ja ostoslistan kokeilujaksolla ja sen jälkeen maksullisella tilauksella."),
        ],
    ),
    "/fi/reseptit-aineksista/": dict(
        title="Reseptejä aineksista, joita sinulla jo on | Cibello",
        desc="Mitä tänään syötäisiin? Cibello vertaa ruokavarastoasi yli 9 000 reseptiin, nostaa kärkeen ne, joihin ainekset jo löytyvät, ja näyttää puuttuvat.",
        eyebrow="Mitä tänään syötäisiin",
        h1="Reseptejä aineksista, joita sinulla jo on",
        lead="Kello on viisi, jääkaapissa on jotain ja kysymys on tuttu: mitä tänään syötäisiin? Cibello vertaa tarkistettua ruokavarastoasi yli 9 000 reseptiin ja nostaa kärkeen ne, joihin ainekset löytyvät kotoa. Puuttuvat ainekset näet heti.",
        sections=[
            ("Aloita jääkaapista, ei reseptikirjasta", """<p>Tavallinen tapa etsiä ruokaideoita menee näin: valitset houkuttelevan reseptin, luet ainesluettelon ja huomaat, että puolet puuttuu. Sitten joko lähdet kauppaan tai aloitat alusta. Cibello kääntää järjestyksen: ensin katsotaan, mitä kotona on, ja vasta sitten, mitä siitä voi tehdä.</p><p>Se tekee ehdotuksista mahdollisia toteuttaa arki-iltana. Ruokaidea, jonka ainekset ovat jo kaapissa, on lähempänä lautasta kuin idea, joka vaatii kauppareissun.</p><p>Tätä useimmat tarkoittavat, kun he etsivät reseptejä aineksilla tai kysyvät, mitä voisi tehdä jauhelihasta, kananmunista ja siitä puolikkaasta paprikasta. Vastaus riippuu siitä, mitä muuta kaapissa on, ja juuri sen sovellus tietää. Tässä oppaassa kerrotaan, miten ruokavarasto syntyy, miten reseptit järjestetään sen mukaan ja mitä sinun on syytä tarkistaa itse.</p>"""),
            ("Kuvasta ruokavarastoksi", """<p>Ruokavarastoa ei tarvitse näppäillä käsin. Kuvaa jääkaappi, pakastin tai kaappi, niin sovellus tunnistaa tuotteet ja muistaa, missä ne ovat: juusto jääkaapin ovessa, linssit ylähyllyllä. Kauppakuitin voi kuvata kotiin tullessa, ja viivakoodit voi skannata yksitellen. Sama toimii pakastimelle: kun pussit ja rasiat on kuvattu kerran, ne eivät enää unohdu pohjalle.</p><p>Tekoäly ei näe kaikkea. Tuote voi jäädä piiloon toisen taakse tai päiväys tulkitaan väärin. Siksi tarkistat tunnistetut tuotteet ennen tallennusta ja korjaat epävarmat kohdat. Muutama sekunti tarkistusta pitää ruokavaraston luotettavana, ja luotettava varasto on kaiken muun perusta.</p>"""),
            ("Reseptit järjestyksessä sen mukaan, mitä on kotona", """<p>Cibellossa on yli 9 000 reseptiä, ja ne järjestetään sen mukaan, kuinka suuri osa aineksista löytyy ruokavarastostasi. Resepti, johon on 82 prosenttia aineksista kotona, näkyy ennen reseptiä, johon on puolet. Puuttuvat ainekset näet suoraan, joten voit päättää, riittääkö se mitä on vai lähdetkö hakemaan yhden asian.</p><p>Ehdotukset painottavat myös sitä, mikä pitäisi käyttää pian, ja sitä, mistä taloutenne on aiemmin pitänyt. Jokaisen ehdotuksen yhteydessä kerrotaan syy, esimerkiksi ”kana ja kerma vanhenevat pian”. Sinä näet perustelun ja päätät itse.</p><p>Hakua voi käyttää myös suoraan: kirjoita ”lettuja” tai ”linssikeitto”, niin näet, mitä reseptiin tarvitaan ja mikä siitä on jo kotona. Reseptejä voi selata myös ryhmittäin, esimerkiksi aamiainen, lounas, päivällinen, välipala, jälkiruoka ja leivonta.</p>"""),
            ("Ehdotukset, jotka sopivat teidän talouteenne", """<p>Makutottumukset, ruokavaliot ja allergiat vaikuttavat siihen, mikä oikeasti toimii tiistai-iltana. Cibello kokoaa nämä tiedot yhteen paikkaan ja oppii ajan myötä, millaisia ruokia teillä valitaan. Resepti- ja allergiasuodattimet ovat kuitenkin ohjeellisia, eivät takuu: lue ainesosat ja pakkausmerkinnät aina itse, varsinkin jos taloudessa on allergia tai intoleranssi. Ravintoarvot ovat arvioita suunnittelun tueksi, eivät ravitsemusneuvontaa.</p><p>Jos taloudessa on esimerkiksi laktoositon ruokavalio tai pähkinäallergia, kirjaat sen sovellukseen, ja ehdotukset ottavat sen huomioon. Lopullinen tarkistus jää silti sinulle, koska reseptin aines ja kaupan hyllyltä otettu tuote eivät ole sama asia.</p>"""),
            ("Arki, viikonloppu ja lapsiperhe", """<p>Sama ruokavarasto palvelee erilaisia iltoja.</p><ul><li><strong>Arkena</strong> kärkeen nousevat usein pasta, munakas, wokki tai keitto, koska niiden ainekset ovat jo kotona ja ruoka valmistuu ilman erikoisostoksia. Kun ruokavarasto on ajan tasalla, näet heti, mihin näistä ainekset riittävät tänään.</li><li><strong>Viikonloppuna</strong> on aikaa padalle, uuniruoalle tai leivonnalle. Silloin voit valita reseptin, joka tekee kunniaa hyvälle raaka-aineelle tai jonka olette tallentaneet suosikiksi. Lauantain tähteet voi kirjata ruokalaatikoiksi, ja ne ovat mukana ruokavarastossa maanantaina.</li><li><strong>Lasten kanssa</strong> ruoan pitää usein olla tuttua ja silti vaihtelevaa. Cibello voi ehdottaa ruokia, jotka muistuttavat suosikkejanne mutta käyttävät sitä, mitä kotona on. Sovellus on tarkoitettu täysi-ikäisille, joten aikuinen käyttää sitä ja lapset saavat valita vaihtoehdoista.</li></ul>"""),
            ("Ideasta ostoslistaan", """<p>Kun ruoka on valittu, puuttuvat ainekset siirtyvät ostoslistalle, jonka koko talous näkee. Tarkoitus ei ole saada sinua ostamaan enemmän vaan tekemään näkyväksi, mitä oikeasti puuttuu, ja välttämään tuplaostokset. Jos haluat suunnitella useamman päivän kerralla, lue <a href="/fi/ateriasuunnittelu/">opas ateriasuunnitteluun ja viikon ruokalistaan</a>. Reseptisovellusten englanninkielinen <a href="/en/best-recipe-app/">vertailu</a> kertoo, miten Cibello eroaa muista.</p><p>Kun kauppa on käyty, kuvaa kuitti, niin ruokavarasto päivittyy ja seuraava ehdotus lähtee taas oikeasta tilanteesta.</p>"""),
            ("Sinä päätät, sovellus ehdottaa", """<p>Cibello ei tee päätöksiä puolestasi. Tarkistat aina ainekset, määrät, päiväykset ja allergiatiedot ennen kuin jotain käytetään tai tallennetaan. Kun ruokavarasto, suunnitelma ja ostoslista pysyvät ajan tasalla, koko talous saa käyttökelpoisemman pohjan päätöksille, ja ruoka tulee käytetyksi ennen kuin se pilaantuu. Muistutukset tulevat lempeästi ennen kuin jokin ehtii pilaantua, eikä sovellus koskaan arvostele sitä, mitä tai kuinka paljon syötte. Siitä kerromme lisää oppaassa <a href="/fi/vahenna-ruokahavikkia/">vähennä ruokahävikkiä</a>. Muut suomenkieliset oppaat löydät <a href="/fi/">etusivulta</a>.</p>"""),
        ],
        faq=[
            ("Pitääkö kaikki tuotteet kirjata käsin?", "Ei. Voit kuvata jääkaapin, pakastimen ja kaapit sekä skannata kuitteja ja viivakoodeja. Tunnistetut tuotteet tarkistat itse ennen tallennusta."),
            ("Voiko Cibello ehdottaa reseptejä tähteistä?", "Kyllä. Kun tähteet ja ruokalaatikot on kirjattu ruokavarastoon, ne voidaan ottaa huomioon ehdotuksissa."),
            ("Ottaako Cibello allergiat huomioon?", "Voit ilmoittaa allergiat ja ruokavaliot, mutta suodatus ei ole takuu. Lue ainesosat ja pakkausmerkinnät aina itse."),
            ("Mitä jos reseptistä puuttuu jokin aines?", "Cibello näyttää puuttuvat ainekset ja voi lisätä ne ostoslistalle. Sinä päätät, haetko ne kaupasta vai valitsetko reseptin, jonka ainekset ovat jo kotona."),
        ],
    ),
    "/fi/vahenna-ruokahavikkia/": dict(
        title="Vähennä ruokahävikkiä: käytä ruoka ajoissa | Cibello",
        desc="Näe, mitä kotona on, saa muistutus ennen kuin jokin pilaantuu ja löydä reseptit, joissa ruoka tulee käytetyksi. Vähemmän hävikkiä ilman syyllisyyttä.",
        eyebrow="Vähemmän hävikkiä, vähemmän stressiä",
        h1="Vähennä ruokahävikkiä: käytä ruoka ajoissa",
        lead="Suurin osa kotien ruokahävikistä ei synny välinpitämättömyydestä vaan siitä, että ruoka unohtuu. Cibello näyttää, mitä jääkaapissa, pakastimessa ja kaapeissa on, muistuttaa lempeästi ennen kuin jokin pilaantuu ja ehdottaa reseptejä, joissa ruoka tulee käytetyksi.",
        sections=[
            ("Mitä ruokahävikki on", """<p>Ruokahävikki on ruokaa, joka olisi voitu syödä mutta joka päätyy roskiin: tähteet, jotka jäävät jääkaapin perälle, vihannekset, jotka nahistuvat ennen käyttöä, tai pakkaukset, joiden päiväys menee ohi ilman että kukaan tarkistaa, olisiko sisältö vielä syömäkelpoista. Tutkimusten mukaan huomattava osa syömäkelpoisen ruoan hävikistä syntyy kodeissa, ja useimmiten syynä on puuttuva yleiskuva, ei haluttomuus.</p><p>Se on hyvä uutinen, sillä yleiskuvaa voi parantaa. Kun tiedät, mitä kotona on ja mikä pitäisi käyttää ensin, päätökset helpottuvat ja roskiin menee vähemmän.</p><p>Hävikin vähentäminen ei vaadi suuria elämänmuutoksia. Useimmat kodit tuntevat samat kolme tilannetta: ostettiin liikaa, unohdettiin, mitä oli, tai tähteet jäivät syömättä. Tämä opas käy ne läpi ja kertoo, missä sovellus voi auttaa ja missä päätös jää sinulle.</p>"""),
            ("Näe, mikä on unohtumassa", """<p>Ruokavarasto sovelluksessa tekee näkyväksi sen, mikä muuten katoaa oven taakse. Kuvaa jääkaappi, pakastin ja kaapit, niin Cibello tunnistaa tuotteet ja sen, missä ne ovat. Kun tuotteilla on päiväys, sovellus voi muistuttaa lempeästi, että jokin pitäisi käyttää pian. Muistutus on vinkki, ei moite.</p><p>Päiväykset ja tekoälyn tulkinnat voivat olla vääriä. Tarkista tunnistetut tiedot ennen tallennusta, ja arvioi ruoka aina itse: katso, haista ja noudata pakkauksen ohjeita.</p><p>Ruokavarastoon kuuluvat myös ruokalaatikot. Kun kirjaat lauantain tähteet rasioihin ja rasiat sovellukseen, ne ovat mukana maanantain ehdotuksissa sen sijaan, että ne löytyvät pakastimen pohjalta keväällä.</p>"""),
            ("Suunnittele reseptit raaka-aineiden ympärille", """<p>Sen sijaan, että ostat kokonaan uuden setin aineksia, voit etsiä reseptejä, jotka käyttävät kotona olevaa ruokaa. Cibello järjestää yli 9 000 reseptiä sen mukaan, kuinka suuri osa aineksista on jo kotona, ja painottaa sitä, mikä vanhenee pian. Vain oikeasti puuttuvat ainekset siirtyvät ostoslistalle.</p><p>Käytännön esimerkki: jääkaapissa on puolikas purjo, avattu kermarasia ja pari perunaa. Sovellus nostaa kärkeen keiton tai gratiinin, johon nämä riittävät, ja näyttää, puuttuuko jotain. Sinä päätät, tehdäänkö se tänään vai huomenna. Lue lisää oppaasta <a href="/fi/reseptit-aineksista/">reseptejä aineksista, joita sinulla jo on</a>.</p><p>Viikkosuunnitelma vie saman ajatuksen pidemmälle: pian vanhenevat tuotteet saavat paikan viikon alussa ja säilyvät ainekset loppuviikosta. Siitä kerrotaan oppaassa <a href="/fi/ateriasuunnittelu/">ateriasuunnittelu ja viikon ruokalista</a>.</p>"""),
            ("Tavallisimmat hävikin syyt ja mikä auttaa", """<p>Suurin osa hävikistä palautuu muutamaan toistuvaan tilanteeseen. Taulukko näyttää tavallisimmat ja sen, mikä kussakin auttaa.</p><table><thead><tr><th scope="col">Miksi ruokaa menee roskiin</th><th scope="col">Mikä auttaa</th></tr></thead><tbody><tr><td>Avattu pakkaus unohtuu jääkaapin perälle</td><td>Ruokavarasto, jossa näkyy sijainti, ja muistutus ennen päiväystä</td></tr><tr><td>Ostetaan sitä, mitä kotona on jo</td><td>Yhteinen ostoslista, jossa on vain oikeasti puuttuvat tuotteet</td></tr><tr><td>Viikkoon mahtuu liikaa uusia reseptejä</td><td>Viikkosuunnitelma, joka lähtee kotona olevasta ruoasta</td></tr><tr><td>Tähteet jäävät syömättä</td><td>Ruokalaatikot kirjataan ruokavarastoon, jolloin ne muistetaan</td></tr><tr><td>Päiväys menee ohi huomaamatta</td><td>Pian vanhenevat tuotteet nostetaan reseptiehdotuksissa kärkeen</td></tr></tbody></table>"""),
            ("Parasta ennen ja viimeinen käyttöpäivä", """<p>Kaksi merkintää sekoitetaan usein. <strong>Parasta ennen</strong> kertoo, mihin asti valmistaja lupaa parhaan laadun. Moni tuote, kuten jogurtti, juusto tai kuivatuotteet, on usein syömäkelpoista päiväyksen jälkeenkin, kun se on säilytetty oikein ja näyttää, tuoksuu ja maistuu normaalilta. <strong>Viimeinen käyttöpäivä</strong> koskee turvallisuutta, ja se merkitään helposti pilaantuviin tuotteisiin, kuten tuoreeseen lihaan ja kalaan. Sen jälkeen tuotetta ei pidä syödä.</p><p>Ole erityisen tarkka, jos ruokaa tarjotaan lapsille, raskaana oleville, iäkkäille tai henkilöille, joiden vastustuskyky on heikentynyt. Sovellus ei voi taata, että ruoka on turvallista.</p><p>Hyvä nyrkkisääntö: parasta ennen -tuotteen kohdalla luota aisteihin, viimeinen käyttöpäivä -tuotteen kohdalla luota päiväykseen. Säilytä ruoka pakkauksen ohjeen mukaan, pidä jääkaappi riittävän kylmänä ja jäähdytä tähteet nopeasti ennen kuin laitat ne rasioihin.</p>"""),
            ("Jaa näkymä taloudessa", """<p>Kun talous jakaa ruokavaraston ja ostoslistan, tuplaostoksia tulee vähemmän ja useampi huomaa, mikä pitäisi käyttää. Se, joka käy kaupassa, näkee, mitä oikeasti puuttuu, ja se, joka kokkaa, näkee, mikä pitäisi käyttää ensin. Yhteinen näkymä kuuluu kokeilujaksoon ja sen jälkeen maksulliseen tilaukseen.</p><p>Cibello ei käytä häpeää eikä kaloripainetta. Tavoite on rauhallisempi ja käytännöllisempi ruoka-arki, jossa ruoka tulee syödyksi. Sovellus ei laske, kuinka paljon heitit pois, eikä muistuta epäonnistumisista. Muistutus on aina neutraali: tämä olisi hyvä käyttää pian.</p>"""),
            ("Tavat, ei syyllisyys", """<p>Vähemmän hävikkiä syntyy tavoista, ei syyllisyydestä. Pieni rutiini riittää: kuvaa kaapit, kun tulet kaupasta, katso ehdotukset ennen kuin päätät ruoan ja kirjaa tähteet ruokalaatikoiksi. Cibello muistuttaa ja ehdottaa, mutta sinä päätät, mitä syödään, pakastetaan tai heitetään pois. Aloita yhdestä tavasta, esimerkiksi siitä, että katsot ruokavaraston ennen kauppaan lähtöä. Kun se sujuu, lisää seuraava. Kaikki suomenkieliset oppaat löytyvät <a href="/fi/">Cibellon etusivulta</a>.</p>"""),
        ],
        faq=[
            ("Voiko sovellus taata, että ruoka on vielä syömäkelpoista?", "Ei. Tarkista aina päiväys, säilytys, haju, ulkonäkö ja pakkauksen ohjeet itse. Sovelluksen muistutukset ja päiväystiedot ovat apuväline, eivät takuu."),
            ("Miten reseptit auttavat vähentämään hävikkiä?", "Ruokavarastoon perustuvat reseptit tekevät helpommaksi käyttää kotona jo olevat ainekset ennen uusien ostamista, ja pian vanhenevat tuotteet nostetaan ehdotuksissa esiin."),
            ("Voiko useampi henkilö päivittää samaa ruokavarastoa?", "Kyllä. Talouden jäsenet jakavat saman ruokavaraston, viikkosuunnitelman ja ostoslistan kokeilujaksolla ja sen jälkeen maksullisella tilauksella."),
            ("Pitääkö päiväykset kirjata itse?", "Tunnistetut tiedot, myös päiväykset, ovat tekoälyn tulkintoja, jotka tarkistat ja tarvittaessa korjaat tai täydennät ennen tallennusta."),
        ],
    ),
}

HUBTEXT = """<section><h2>Mitä tänään syötäisiin?</h2><p>Kysymys toistuu joka ilta, ja vastaus löytyy harvoin reseptikirjasta. Cibello lähtee liikkeelle omasta keittiöstäsi: kuvaa jääkaappi, pakastin ja kaapit, tarkista tunnistetut tuotteet ja anna sovelluksen näyttää, mitä niistä voi tehdä. Yli 9 000 reseptiä järjestetään sen mukaan, kuinka suuri osa aineksista on jo kotona, ja puuttuvat näet heti. Kuitit ja viivakoodit voi skannata samalla tavalla, ja ruokalaatikot pysyvät mukana varastossa. Lue, miten se toimii: <a href="/fi/reseptit-aineksista/">reseptejä aineksista, joita sinulla jo on</a>.</p></section>
<section><h2>Viikon ruokalista, joka joustaa</h2><p>Kun päätökset tehdään kerran viikossa rauhassa, arki-illat kevenevät. Cibello ehdottaa vaihtelevan viikkosuunnitelman, jossa pian vanhenevat tuotteet käytetään ensin eikä sama pääraaka-aine toistu päivästä toiseen. Sinä vaihdat päiviä, poistat ja lisäät, ja puuttuvat ainekset kertyvät ostoslistalle, jonka koko talous näkee. Suunnitelma on luonnos, ei aikataulu, ja se elää viikon mukana. Katso <a href="/fi/ateriasuunnittelu/">opas ateriasuunnitteluun ja viikon ruokalistaan</a>.</p></section>
<section><h2>Ruoka käytetyksi, ei roskiin</h2><p>Suurin osa kotien hävikistä syntyy siitä, että ruoka unohtuu. Kun ruokavarasto näyttää, mitä kotona on ja missä, ja sovellus muistuttaa lempeästi ennen päiväystä, ruoka tulee syödyksi ajoissa. Ruokalaatikotkin voivat olla mukana varastossa, ja talous jakaa saman näkymän, joten tuplaostoksia tulee vähemmän. Ei häpeää eikä kaloripoliisia, vain apua. Lue lisää: <a href="/fi/vahenna-ruokahavikkia/">vähennä ruokahävikkiä</a>.</p></section>
<section><h2>Sinä päätät, Cibello ehdottaa</h2><p>Tekoäly voi tulkita tuotteen väärin tai ohittaa jotain, ja siksi tarkistat aina tuloksen ennen tallennusta. Resepti- ja allergiasuodattimet ovat ohjeellisia, ravintoarvot arvioita. Tietosi tallennetaan EU:n alueelle, ja tilin voi poistaa suoraan sovelluksessa. Kokeilujakso on 14 päivää ilman maksukorttia, ja sovellus on tarkoitettu täysi-ikäisille. Cibello on saatavilla iOS- ja Android-laitteille kahdellatoista kielellä, ja sen kehittää LandveX AB Ruotsissa.</p></section>"""

ABOUT = dict(
    title="Tietoa Cibellosta: sovellus ja yritys sen takana | LandveX AB",
    desc="Cibellon kehittää LandveX AB Tyresössä, Ruotsissa. Miksi sovellus on olemassa, miten ajattelemme tekoälystä ja ruokahävikistä, ja yhteystiedot.",
    h1="Tietoa Cibellosta",
    lead="Cibello on ruotsalainen ruokasovellus, jonka takana on LandveX AB. Se rakennettiin vastaamaan kysymykseen, joka esitetään lähes joka kodissa joka päivä: mitä syötäisiin? Tällä sivulla kerromme, mitä yritämme tehdä, miten työskentelemme tekoälyn ja tietojen kanssa ja miten meihin saa yhteyden.",
    sections=[
        ("Miksi Cibello on olemassa", """<p>Useimmat reseptisovellukset lähtevät resepteistä. Me halusimme lähteä keittiöstä: siitä, mitä jääkaapissa, pakastimessa ja kaapeissa oikeasti on, mikä on vanhenemassa ja mistä talous yleensä pitää. Siksi Cibellon ydin on ruokavarasto, sinun Food Twin, joka syntyy kuvista, kuiteista ja viivakoodeista. Reseptit, viikkosuunnitelma, ostoslista ja muistutukset nojaavat kaikki samaan tietoon. Tavoite on vähemmän arjen stressiä ja <a href="/fi/vahenna-ruokahavikkia/">vähemmän ruokahävikkiä</a>, ilman saarnaamista.</p>"""),
        ("Miten ajattelemme tekoälystä", """<p>Tekoäly tekee Cibellon mahdolliseksi, mutta se on välillä väärässä. Skannaus voi tunnistaa tuotteen väärin, ohittaa jotain hyllyn perältä tai arvata päiväyksen pieleen. Siksi tarkistat tulokset aina ennen tallennusta, ja siksi ehdotukset ovat vain ehdotuksia. Resepti- ja allergiasuodattimet ovat ohjeellisia, eivät takuu, ja ravintoarvot ovat suunnittelun tueksi tarkoitettuja arvioita, eivät ravitsemusneuvontaa. Cibellon omat mallit koulutetaan vain sinun korjauksillasi ja, jos annat siihen erillisen suostumuksen, puhdistetuilla kuvilla. Molemmat valinnat ovat oletuksena pois päältä. Lue lisää <a href="/fi/privacy/">tietosuojakäytännöstä</a>.</p>"""),
        ("Sinun tietosi", """<p>Kaikki tallennetaan EU:n alueelle. Voit katsoa tietosi sovelluksessa ja <a href="/fi/delete-account/">poistaa tilisi</a> milloin tahansa ottamatta yhteyttä tukeen. Emme myy henkilötietoja.</p>"""),
        ("Yritys", """<p>Cibellon kehittää ja omistaa LandveX AB, yritystunnus (org.nr) 559141-7042, Antennvägen 2, 135 48 Tyresö, Ruotsi. Sovellus on saatavilla iOS- ja Android-laitteille kahdellatoista kielellä, ja se on rakennettu Ruotsissa. Toistaiseksi se on tarkoitettu 18 vuotta täyttäneille, koska sovelluksen käyttämän tekoälypalvelun ehdot edellyttävät täysi-ikäisiä käyttäjiä. Kokeilujakso on 14 päivää ilman maksukorttia.</p>"""),
        ("Yhteystiedot", """<p>Yleiset kysymykset ja yhteistyö: <a href="mailto:hello@cibello.app">hello@cibello.app</a>. Tuki: <a href="mailto:support@cibello.app">support@cibello.app</a>. Tietosuoja: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>. Mediakyselyt ovat tervetulleita samaan osoitteeseen; vastaamme yleensä parin arkipäivän kuluessa.</p><p>Seuraa meitä: <a href="https://www.instagram.com/cibelloapp/" rel="noopener">Instagram</a>, <a href="https://www.tiktok.com/@cibello73" rel="noopener">TikTok</a> ja <a href="https://www.facebook.com/profile.php?id=61593336222919" rel="noopener">Facebook</a>.</p>"""),
    ],
)

PRESS = dict(
    title="Media: faktat, kuvat ja yhteystiedot | Cibello",
    desc="Cibellon mediapaketti: lyhyt kuvaus, faktat sovelluksesta, logo ja kuvat sekä LandveX AB:n mediayhteystiedot toimittajille ja kirjoittajille.",
    eyebrow="Toimittajille ja kirjoittajille",
    h1="Media",
    lead="Kaikki, mitä tarvitset kirjoittaaksesi Cibellosta: lyhyt kuvaus, faktat, kuvat ja yhteyshenkilö, joka vastaa nopeasti. Kaikkea tällä sivulla saa käyttää vapaasti toimituksellisessa yhteydessä.",
    sections=[
        ("Cibello lyhyesti", """<p>Cibello on ruotsalainen ruokasovellus, joka kuvaa jääkaapin ja kaapit, pitää ruokavarastoa sijainteineen ja päiväyksineen, ehdottaa reseptejä siitä, mitä kotona oikeasti on, suunnittelee viikon ja jakaa ostoslistan talouden kanssa. Se muistuttaa lempeästi ennen kuin ruoka pilaantuu eikä koskaan arvostele sitä, mitä joku syö. Saatavilla iOS- ja Android-laitteille kahdellatoista kielellä, tiedot tallennetaan EU:n alueelle, kehittäjänä LandveX AB Tyresöstä, Ruotsista.</p><p><strong>Yhdellä lauseella:</strong> Cibello on sovellus, joka näkee, mitä kotona on, ja vastaa kysymykseen ”mitä syötäisiin?”.</p>"""),
        ("Faktat", """<ul><li>Saatavilla iOS- ja Android-laitteille: <a href="https://apps.apple.com/app/id6807100747" rel="noopener">App Store</a> ja <a href="https://play.google.com/store/apps/details?id=com.cibello.app" rel="noopener">Google Play</a>. Ikäraja 18 vuotta.</li><li>Kokeilujakso: 14 päivää ilman maksukorttia, sen jälkeen tilaus App Storen tai Google Playn kautta.</li><li>Reseptit: yli 9 000, sovitetaan käyttäjän ruokavarastoon.</li><li>Kielet: ruotsi, englanti, saksa, ranska, espanja, italia, hollanti, puola, tanska, norja, suomi, portugali.</li><li>Tiedot: tallennetaan EU:n alueelle. Tilin ja tiedot voi poistaa sovelluksessa.</li><li>Tekoäly: jääkaapin, kaappien, kuittien ja viivakoodien skannaus. Käyttäjä tarkistaa tuloksen aina. Cibellon omat mallit koulutetaan vain käyttäjien korjauksilla ja erillisellä suostumuksella puhdistetuilla kuvilla.</li><li>Hinnoittelu: ilmainen kokeilujakso, sen jälkeen maksullinen tilaus talouden ominaisuuksille. Ajantasaiset hinnat App Storessa ja Google Playssa.</li><li>Yritys: LandveX AB, org.nr 559141-7042, Antennvägen 2, 135 48 Tyresö, Ruotsi.</li></ul>"""),
        ("Logo ja kuvat", """<ul><li><a href="/img/icon-512.png">Sovelluskuvake, 512×512 PNG</a></li><li><a href="/img/og-fi.png">Jakokuva, 1200×630 PNG (suomi)</a></li><li><a href="/img/og.png">Jakokuva, 1200×630 PNG (ruotsi)</a></li><li><a href="/favicon.svg">Symboli, SVG</a></li></ul><p>Kuvakaappauksia sovelluksesta saa pyynnöstä. Kuvia saa käyttää vapaasti toimituksellisessa yhteydessä, kun lähteeksi mainitaan Cibello.</p>"""),
        ("Mediayhteystiedot", """<p><a href="mailto:hello@cibello.app?subject=Mediakysely">hello@cibello.app</a>. Vastaamme mediakyselyihin yleensä yhden arkipäivän kuluessa. Perustaja on tavoitettavissa haastatteluihin kotitalouksien ruokahävikistä, tekoälystä arjessa ja siitä, miksi ”mitä syötäisiin?” on kysymys, joka kannattaa ratkaista.</p><p>Lisää yrityksestä: <a href="/fi/about/">Tietoa Cibellosta</a>.</p>"""),
    ],
)

NEWS = dict(
    title="Uutta Cibellossa: päivitykset ja uudet oppaat",
    desc="Uudet oppaat, työkalut ja päivitykset cibello.app-sivustolla päivämäärineen. Tilaa RSS-syötteenä.",
    h1="Uutta Cibellossa",
    lead="Mitä sivustolle ja sovellukseen on lisätty, uusin ensin. Saatavilla myös RSS-syötteenä.",
    rss_label="RSS-syöte",
    entries=[
        ("2026-09-04", "Uusi opas: ruokahävikki Ruotsissa numeroina", "/matsvinn-statistik/", "Ruotsin ympäristöviraston ja elintarvikeviraston viralliset luvut yhdellä sivulla (ruotsiksi): 880 000 tonnia ruokahävikkiä, 16 kg syömäkelpoista ruokaa henkeä kohti kotitalouksissa ja 1 330 kruunua henkeä kohti vuodessa, jokaiselle luvulle lähde."),
        ("2026-09-04", "Kolme uutta englanninkielistä opasta ja kaksi vertailua", "/en/", "Mitä syödä tänä iltana, tekoälyavusteinen ateriasuunnittelu ja ruokavarastosovellus sekä rehelliset vertailut ateriasuunnittelu- ja reseptisovelluksista Mealimen, Samsung Foodin, Plan to Eatin, Paprikan ja SuperCookin kanssa."),
        ("2026-09-04", "Täydet aloitussivut kahdellatoista kielellä", "/fi/", "Jokaisella kielellä on nyt kokonainen aloitussivu lyhyen tekstisivun sijaan, eikä mitään käännetä enää selaimessa."),
        ("2026-08-30", "Tietosuojakäytäntö ja käyttöehdot, versio 2.0", "/fi/privacy/", "Päivitetyt tekstit kattavat Gemini-analyysin, vapaaehtoisen Cibello AI:n koulutuksen, 14 päivän kokeilujakson ilman maksukorttia ja 18 vuoden ikärajan. Suomennokset ovat saatavilla; ruotsinkielinen versio on pätevä."),
    ],
)

PRIVACY = dict(
    title="Tietosuojakäytäntö – Cibello",
    desc="Näin Cibello käsittelee henkilötietoja, kuvia, Gemini-analyysia ja vapaaehtoista Cibello AI:n koulutusta. Suomennos ruotsinkielisestä käytännöstä, versio 2.0.",
    h1="Tietosuojakäytäntö",
    notice="<strong>Lyhyesti:</strong> Ulkoista tekoälypalvelua käytetään nykyiseen kuva-analyysiin. Cibellon omaa tekoälymallia saa kouluttaa vain käyttäjän omilla korjauksilla ja puhdistetuilla kuvilla erillisen, vapaaehtoisen ja aktiivisen valinnan jälkeen, joka tehdään käyttöönoton yhteydessä. Ulkoisen tekoälyn vastauksia ei koskaan käytetä koulutuksen mallivastauksina.",
    body="""<h2>1. Rekisterinpitäjä</h2>
<p>LandveX AB, org.nr 559141-7042, Antennvägen 2, 135 48 Tyresö, Ruotsi, on Cibellon rekisterinpitäjä. Tietosuojaa koskevat kysymykset lähetetään osoitteeseen <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>

<h2>2. Tiedot ja käyttötarkoitukset</h2>
<ul>
<li><strong>Tili:</strong> sähköpostiosoite, näyttönimi, tunnistautumisidentiteetti ja turvalokit tilin luomista ja suojaamista varten.</li>
<li><strong>Ruoka- ja kotitaloustiedot:</strong> ruokavarasto, reseptit, mieltymykset, allergiat ja omat korjaukset sovelluksen toimintoja varten.</li>
<li><strong>Kuvat:</strong> kuvat, jotka käyttäjä päättää skannata elintarvikkeiden tai kuittien tunnistamista varten.</li>
<li><strong>Maksut:</strong> tilauksen tila ja tapahtumaviitteet. Kortti- ja maksutietoja käsittelee Apple App Store tai Google Play.</li>
<li><strong>Tekniset tiedot:</strong> virheet, suorituskyky ja tuoteanalytiikka vain käyttäjän valintojen ja välttämättömien turvallisuustarpeiden mukaan.</li>
<li><strong>Suoja kokeilujakson väärinkäyttöä vastaan:</strong> normalisoidusta sähköpostiosoitteesta muodostettu avaimellinen, pseudonyymi HMAC-sormenjälki tallennetaan enintään viideksi vuodeksi. Sitä ei voi käyttää kirjautumiseen tai yhteydenottoon, eikä se sisällä selväkielistä osoitetta, käyttäjätunnusta tai Firebase-identiteettiä. Sen ainoa tarkoitus on estää toistuvat kokeilujaksot tilin poistamisen ja uudelleenrekisteröitymisen jälkeen.</li>
</ul>

<h2>3. Gemini tuotannossa</h2>
<p>Valitut kuvat ja tarvittava ohjeistus lähetetään Google Gemini API -rajapintaan sovelluksessa näytettävän tuloksen muodostamista varten. Cibello käyttää maksullista palvelua ETA-alueella. Googlen ehtojen mukaan maksullisen palvelun tietoja ei käytetä Googlen tuotteiden parantamiseen, mutta rajoitettua lokitusta voi esiintyä turvallisuuden ja väärinkäytösten torjunnan vuoksi, ellei erityinen nollasäilytystila ole käytössä. Cibello ei siksi lupaa nollasäilytystä oman ympäristönsä ulkopuolella ilman palveluntarjoajan teknistä vahvistusta.</p>
<p>Gemini-tulokset ovat automaattisia arvioita. Käyttäjän on tarkistettava sisältö, allergeenit, päiväykset ja määrät ennen tietojen käyttöä.</p>

<h2>4. Cibellon oma tekoälymalli: erillinen ja vapaaehtoinen koulutus</h2>
<p>Cibello kehittää omaa tekoälymallia. Koulutusprosessi on teknisesti ja oikeudellisesti erotettu siitä ulkoisesta tekoälypalvelusta, joka tuottaa käyttäjän nykyiset tulokset:</p>
<ul>
<li>Geminin vastauksia, päättelyä tai ehdotuksia ei koskaan viedä koulutusmerkinnöiksi tai mallivastauksiksi Cibellon omaan tekoälymalliin.</li>
<li><strong>Anonymisoitu tekoälyn parantaminen</strong> sallii käyttäjän nimenomaisen korjauksen tai manuaalisesti vahvistetun vastauksen käytön ilman kuvaa.</li>
<li><strong>Kuvakoulutus</strong> sallii käyttäjän kuvan puhdistetun kopion yhdistämisen käyttäjän omaan korjaukseen. Metatiedot poistetaan ja kuvan kokoa rajoitetaan ennen tallennusta.</li>
<li>Käyttöönotossa näytetään yksi yhteinen, selkeä valinta näille saman koulutustarkoituksen kahdelle osalle. Valintaa ei ole esivalittu, ja sovellus toimii, vaikka käyttäjä ei anna suostumusta.</li>
<li>Suostumuksen voi peruuttaa Profiili-osiossa olevalla painikkeella. Tällöin tuleva käyttö lopetetaan, sovelluksen hallinnoima aktiivinen koulutuspankki tyhjennetään ja kuvaviittaukset poistetaan. Jo muodostettuja, yhdistettyjä malliparametreja ei yleensä voi yhdistää takaisin henkilöön.</li>
<li>Cibello AI ei vaikuta tuotannon vastauksiin, ennen kuin dokumentoidut vertailu- ja turvallisuusrajat on saavutettu.</li>
</ul>

<h2>5. Oikeusperuste</h2>
<p>Tiliä ja ydintoimintoja käsitellään sopimuksen täyttämiseksi. Turvalokitusta ja toistuvien kokeilujaksojen estämiseen tarkoitettua rajoitettua sormenjälkeä käsitellään oikeutetun edun perusteella. Lakisääteiset velvoitteet voivat edellyttää muuta rajoitettua käsittelyä. Vapaaehtoinen tuoteanalytiikka, tekoälyn parantaminen ja kuvakoulutus perustuvat erillisiin suostumuksiin, jotka voi peruuttaa.</p>

<h2>6. Säilytys ja vastaanottajat</h2>
<p>Tietoja säilytetään niin kauan kuin palvelu, turvallisuus, lakisääteiset vaatimukset ja dokumentoitu varmuuskopioiden säilytysaika edellyttävät. Palveluntarjoajia voivat olla AWS käyttöä ja tallennusta varten, Firebase tunnistautumista varten, Google Gemini valittua tekoälyanalyysia varten sekä Apple tai Google maksuja varten. Cibello ei myy henkilötietoja. Kokeilujakson sormenjälki poistetaan automaattisesti viimeistään viisi vuotta kokeilujakson alkamisesta.</p>

<h2>7. Sinun oikeutesi</h2>
<p>Voit pyytää pääsyä tietoihin, niiden oikaisua, siirtoa järjestelmästä toiseen, käsittelyn rajoittamista tai poistamista sekä vastustaa tiettyä käsittelyä. Suostumuksia muutetaan Profiili-osiossa. Tilin voi poistaa suoraan sovelluksessa tai <a href="/fi/delete-account/">tilin poistamisen verkkosivulla</a>. Voit myös ottaa yhteyttä Ruotsin tietosuojaviranomaiseen (Integritetsskyddsmyndigheten).</p>

<h2>8. Ikä</h2>
<p>Cibello on toistaiseksi tarkoitettu vähintään 18-vuotiaille, koska käytetyn Gemini API -palvelun ehdot edellyttävät täysi-ikäisiä käyttäjiä. Ikävaatimusta arvioidaan uudelleen, jos tekninen palveluntarjoajaratkaisu muuttuu.</p>

<h2>9. Muutokset</h2>
<p>Olennaiset muutokset numeroidaan versioiksi ja edellyttävät uutta hyväksyntää sovelluksessa ennen käytön jatkamista.</p>""",
)

TERMS = dict(
    title="Käyttöehdot – Cibello",
    desc="Cibellon käyttöehdot: tili, ikäraja, tilaukset ja 14 päivän kokeilujakso, tekoälyanalyysi ja turvallinen käyttö. Suomennos ruotsinkielisistä ehdoista, versio 2.0.",
    h1="Käyttöehdot",
    body="""<h2>1. Sopimus ja ikäraja</h2>
<p>Nämä ehdot ovat voimassa käyttäjän ja LandveX AB:n (org.nr 559141-7042) välillä. Cibello on toistaiseksi tarkoitettu vain vähintään 18-vuotiaille. Luomalla tilin käyttäjä vahvistaa ikänsä ja hyväksyy ehdot sekä <a href="/fi/privacy/">tietosuojakäytännön</a>.</p>

<h2>2. Palvelu</h2>
<p>Cibello auttaa käyttäjää järjestämään ruokaa, tulkitsemaan valittuja kuvia ja kuitteja sekä saamaan resepti- ja ateriaehdotuksia. Tulokset voivat olla puutteellisia tai virheellisiä, ja käyttäjän on tarkistettava ne.</p>

<h2>3. Ei lääketieteellistä tai muuta ammatillista neuvontaa</h2>
<p>Cibello tarjoaa inspiraatiota ja yleistä tietoa, ei lääketieteellistä, ravitsemusterapeutin, allergia- tai muuta ammatillista neuvontaa. Käyttäjä vastaa ainesosien, allergeenien, annoskoon, säilyvyyden, valmistuksen ja elintarviketurvallisuuden tarkistamisesta. Sairauden, raskauden, vakavan allergian tai erityistarpeiden yhteydessä on käännyttävä pätevän terveydenhuollon ammattilaisen puoleen.</p>

<h2>4. Tekoäly ja ihmisen valvonta</h2>
<p>Ulkoista tekoälypalvelua käytetään nykyiseen tuotantoanalyysiin. Cibellon omaa tekoälymallia kehitetään rinnalla, mutta sitä saa kouluttaa vain <a href="/fi/privacy/">tietosuojakäytännössä</a> kuvatun suostumuksen ja rajoitusten mukaisesti. Ulkoisen tekoälyn vastauksia ei koskaan käytetä koulutuksen mallivastauksina. Käyttäjän on aina voitava korjata automaattisia tuloksia.</p>

<h2>5. Vapaaehtoiset koulutussuostumukset</h2>
<p>Cibellon ydintoimintojen käyttöä ei saa asettaa ehdolliseksi tekoälyn parantamista tai kuvakoulutusta koskevalle suostumukselle. Valinta on alusta alkaen pois päältä, erillinen ehtojen hyväksymisestä, ja sitä voi muuttaa Profiili-osiossa.</p>

<h2>6. Tili ja turvallisuus</h2>
<p>Käyttäjän on annettava oikeat tiedot, suojattava kirjautumistietonsa ja ilmoitettava Cibellolle epäillystä väärinkäytöstä. Tilin voi poistaa Profiili-osiossa tai <a href="/fi/delete-account/">verkkosivun kautta</a>.</p>

<h2>7. Tilaus ja maksaminen</h2>
<p>Mobiilisovelluksen digitaaliset tilaukset ostetaan ja hallinnoidaan Apple App Storen tai Google Playn kautta. Cibellon palvelinohjattu 14 päivän kokeilujakso ilman maksukorttia on käytettävissä kerran sähköposti-identiteettiä kohti viiden vuoden ajanjaksolla. Poistetun tilin voi luoda uudelleen, mutta se ei automaattisesti anna uutta kokeilujaksoa. Hinta, jakso, automaattinen uusiminen ja irtisanominen näytetään kussakin kaupassa ennen ostoa. Hyvitykset käsitellään kaupan sääntöjen ja pakottavan kuluttajansuojalainsäädännön mukaisesti.</p>

<h2>8. Sallittu käyttö</h2>
<p>Palvelua ei saa käyttää laittomaan sisältöön, oikeudenloukkauksiin, häirintään, automatisoituun ylikuormitukseen, turvatoimien kiertämiseen tai yrityksiin poimia muiden käyttäjien tietoja. Cibello voi rajoittaa tilejä turvallisuusriskin tai olennaisen sopimusrikkomuksen yhteydessä.</p>

<h2>9. Saatavuus ja muutokset</h2>
<p>Palvelua kehitetään jatkuvasti, ja se voi olla tilapäisesti poissa käytöstä. Toimintoja voidaan muuttaa turvallisuuteen, lainsäädäntöön, laatuun tai tekniikkaan liittyvistä syistä. Olennaiset ehtomuutokset numeroidaan versioiksi ja edellyttävät uutta hyväksyntää.</p>

<h2>10. Vastuu ja pakottava lainsäädäntö</h2>
<p>LandveX AB vastaa sovellettavan pakottavan lainsäädännön mukaisesti. Mikään näissä ehdoissa ei rajoita oikeuksia, joista ei voi lain mukaan sopia toisin. Sovelletaan Ruotsin lakia, ja kuluttaja voi lisäksi vedota kotimaansa pakottavaan lainsäädäntöön ja toimivaltaiseen tuomioistuimeen.</p>

<h2>11. Yhteystiedot</h2>
<p>Tuki: <a href="mailto:support@cibello.app">support@cibello.app</a>. Tietosuoja: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>""",
)

DELETE = dict(
    title="Poista tili ja tiedot – Cibello",
    desc="Näin poistat Cibello-tilisi ja siihen liittyvät henkilötiedot suoraan sovelluksessa.",
    h1="Poista tili ja tiedot",
    body="""<h2>Suoraan sovelluksessa</h2>
<ol>
<li>Kirjaudu Cibelloon.</li>
<li>Avaa <strong>Profiili</strong>.</li>
<li>Valitse <strong>Poista tili</strong> ja vahvista.</li>
</ol>
<p>Tili, Firebase-identiteetti, aktiiviset kuvat ja henkilökohtaiset sovellustiedot poistetaan. Taloudellisten tapahtumien viitteet voidaan pseudonymisoida ja säilyttää, kun laki sitä edellyttää. Varmuuskopiot poistuvat kierrosta dokumentoidun säilytysajan mukaan.</p>

<h2>Jos et pääse sovellukseen</h2>
<p>Lähetä pyyntö tilin rekisteröidystä sähköpostiosoitteesta osoitteeseen <a href="mailto:privacy@cibello.app?subject=Poista%20Cibello-tilini">privacy@cibello.app</a>. Kirjoita ”Poista Cibello-tilini”. Varmistamme ennen poistamista, että osoite on hallinnassasi.</p>

<h2>Koulutusdata</h2>
<p>Poistamisen yhteydessä käyttäjän korjaukset ja kuvaviittaukset poistetaan aktiivisesta koulutuspankista. Geminin vastauksia ei ole koskaan viety Cibello AI:n koulutuksen mallivastauksiksi. Jo yhdistettyjä malliparametreja ei yleensä voi yhdistää takaisin henkilöön.</p>""",
)

UI = dict(
    faq_title="Usein kysyttyä",
    privacy_nav="Tietosuoja",
    terms_nav="Käyttöehdot",
    delete_nav="Poista tili",
    legal_meta="Cibello · versio 2.0 · voimassa 30.8.2026 alkaen · suomennos",
    translation_label="Tietoa tästä suomennoksesta:",
    translation_note='Tämä on suomennos ruotsinkielisestä alkuperäistekstistä (<a href="{sv}" lang="sv">alkuperäinen</a>). Ristiriitatilanteessa ruotsinkielinen versio on pätevä.',
)
