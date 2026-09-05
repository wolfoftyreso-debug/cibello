"""German content for cibello.app. See _schema.py for the structure.

Rules: docs/OVERSATTNINGSBRIEF.md. Facts: docs/FAKTAKONTROLL.md only.
Legal texts are translations of integritet.html, villkor.html and delete-account.html (v2.0);
the Swedish version applies if they differ.
"""

LANG = "de"

GUIDES = {
    "/de/essensplaner/": dict(
        title="Essensplaner: Wochenplan für den Alltag | Cibello",
        desc="Ein Wochenplan, der zu eurem Haushalt passt: Cibello schlägt abwechslungsreiche Mahlzeiten aus dem Vorrat vor, du prüfst und änderst sie.",
        eyebrow="Wochenplan ohne Kopfzerbrechen",
        h1="Essensplaner: die Woche einmal planen, jeden Abend entspannter kochen",
        lead="Die Frage „Was essen wir heute?“ muss nicht jeden Abend neu beantwortet werden. Mit einem Wochenplan, der auf eurem Vorrat aufbaut, steht die Antwort schon fest, bevor der Hunger kommt. Cibello schlägt den Plan vor, du entscheidest, was daraus wird.",
        sections=[
            ("Warum ein Wochenplan den Abend entspannt", """<p>Um 17 Uhr ist die Energie für Entscheidungen meist aufgebraucht. Genau dann stellt sich die Frage, was auf den Tisch kommt, was noch im Kühlschrank liegt und ob dafür etwas fehlt. Ein Essensplan verlegt diese Entscheidung in einen ruhigen Moment, zum Beispiel auf den Sonntagabend. Unter der Woche musst du dann nur noch nachsehen, was für heute vorgesehen ist.</p><p>Ein guter Plan ist dabei kein starres Schema. Er ist ein Entwurf, der Platz lässt für Reste, spontane Einladungen und Tage, an denen einfach Brot mit Käse reicht. Cibello ist so gebaut, dass du den Vorschlag prüfst und anpasst, nicht umgekehrt.</p><p>Was ein Wochenplan im Alltag tatsächlich spart, ist weniger die Zeit am Herd als die Zeit davor: das Grübeln, der dritte Gang zum Supermarkt in einer Woche und die Spontankäufe, die dann doch niemand verwendet. Wer einmal in der Woche plant, kauft in der Regel gezielter ein und hat abends eine Antwort parat, auch wenn die Antwort nur „Reste“ heißt.</p>"""),
            ("So entsteht der Plan in Cibello", """<p>Der Wochenplan beginnt nicht bei Rezepten, sondern bei deiner Küche. Der Ablauf ist kurz:</p><ol><li>Fotografiere Kühlschrank, Gefrierfach und Vorratsschrank. Die App erkennt die Produkte und merkt sich, wo sie stehen. Kassenbons und Barcodes lassen sich ebenfalls scannen.</li><li>Prüfe das Ergebnis, bevor du es speicherst. KI kann Dinge übersehen oder falsch deuten, deshalb hast du immer das letzte Wort.</li><li>Lass dir einen Wochenplan vorschlagen. Cibello achtet auf Abwechslung bei Gerichten und Zutaten und berücksichtigt, was bald verbraucht werden sollte.</li><li>Verschiebe, streiche und ergänze Mahlzeiten, bis der Plan zu eurer Woche passt.</li><li>Die Einkaufsliste sammelt nur das, was wirklich fehlt.</li></ol><p>Mehr zur Rezeptsuche aus dem Vorrat liest du im Ratgeber <a href="/de/rezepte-mit-zutaten/">Rezepte mit Zutaten, die du zu Hause hast</a>.</p>"""),
            ("Abwechslung, ohne dass es kompliziert wird", """<p>Ein automatischer Plan sollte nicht dreimal in der Woche Hähnchen vorschlagen oder mittags und abends dasselbe Gericht einplanen. Cibello variiert zwischen Gerichten, Hauptzutaten und Mahlzeitentypen, sodass die Woche abwechslungsreich bleibt, ohne dass du sieben neue Rezepte lernen musst. Die App lernt mit der Zeit, was euer Haushalt gern isst, und erklärt bei jedem Vorschlag, warum er auftaucht: weil die Sahne bald abläuft, weil das Gericht zu euren Favoriten passt oder weil fast alle Zutaten schon da sind.</p><p>Mehr als 9.000 Rezepte stehen dafür zur Verfügung, sortiert danach, wie groß der Anteil der Zutaten ist, die du bereits zu Hause hast.</p>"""),
            ("Erst das Empfindliche, dann das Haltbare", """<p>Frischer Fisch, Salat und geöffnete Milchprodukte gehören an den Anfang der Woche, Nudeln, Konserven und Tiefgekühltes können warten. Weil der Essensplan mit dem Vorrat verbunden ist, fällt es leichter, empfindliche Lebensmittel zuerst zu verwenden und haltbare für später aufzuheben. Das spart Spontankäufe und ist der einfachste Weg, <a href="/de/lebensmittelverschwendung-reduzieren/">Lebensmittelverschwendung zu reduzieren</a>. Datumsangaben und KI-Ergebnisse können trotzdem falsch sein. Sieh hin, rieche und folge den Hinweisen auf der Verpackung.</p>"""),
            ("Ein Plan für den ganzen Haushalt", """<p>Wer plant, muss nicht alles allein im Kopf behalten. In Cibello teilen die Mitglieder eines Haushalts denselben Vorrat, denselben Wochenplan und dieselbe Einkaufsliste. Wenn jemand auf dem Heimweg Milch kauft oder die letzten Eier verbraucht, sehen es alle. Doppelkäufe werden seltener, und die Frage „Haben wir noch …?“ lässt sich vom Supermarkt aus beantworten. Während der 14-tägigen Testphase und danach mit einem Bezahlabo steht die gemeinsame Übersicht dem ganzen Haushalt zur Verfügung. Jedes Rezept wird trotzdem von euch selbst gegen aktuelle Allergien, Zutaten und Verpackungen geprüft.</p>"""),
            ("Essensplan für die Familie", """<p>Ein Wochenplan für eine Familie bedeutet nicht sieben neue Gerichte. Was sich im Alltag bewährt, ist eine Mischung aus einigen verlässlichen Standardgerichten, ein oder zwei neuen Ideen und bewusst freien Tagen für Reste. Kinder dürfen zwischen zwei Vorschlägen wählen, das erhöht die Chance, dass wirklich gegessen wird. Eine typische Woche könnte so aussehen: Montag Reste vom Wochenende, Dienstag Pasta mit dem Gemüse, das bald weg muss, Mittwoch ein bekanntes Lieblingsgericht, Donnerstag etwas Neues aus den Vorschlägen, Freitag ein einfaches Gericht ohne großen Aufwand, und das Wochenende bleibt offen. Cibello lässt dich Mahlzeiten pro Tag eintragen, zeigt, welche Zutaten schon vorhanden sind, und sammelt den Rest in der Einkaufsliste. Wenn du Apps für die Essensplanung vergleichen möchtest, hilft der englische <a href="/en/best-meal-planning-app/">Vergleich von Meal-Planning-Apps</a>.</p>"""),
            ("Vom Vorschlag zur Routine", """<p>Der Plan ist ein Angebot, kein Stundenplan. Tausche Tage, streiche Gerichte und trage eigene Favoriten ein. Je öfter Vorrat und Einkaufsliste aktuell gehalten werden, desto besser treffen die Vorschläge für die nächste Woche. Und jedes Gericht prüfst am Ende du: gegen Zutaten, Allergene und das, worauf ihr heute Lust habt.</p><p>Ein Tipp für den Anfang: Plane in der ersten Woche nur vier Abende und lass den Rest frei. So merkst du, wie viel Struktur euch guttut, ohne dass der Plan zur Pflicht wird. Was Cibello sonst noch kann, steht auf der <a href="/de/">deutschen Startseite</a>.</p>"""),
        ],
        faq=[
            ("Kann Cibello einen Wochenplan automatisch erstellen?", "Ja. Cibello schlägt einen Plan vor, der auf eurem Vorrat, bald ablaufenden Lebensmitteln und euren Vorlieben aufbaut. Du prüfst den Vorschlag und passt ihn an den Haushalt an."),
            ("Berücksichtigt der Essensplan, was schon zu Hause ist?", "Ja. Der geprüfte Vorrat ist die Grundlage der Vorschläge, damit vorhandene Lebensmittel zuerst verwendet werden und die Einkaufsliste nur das Fehlende enthält."),
            ("Kann ich eine geplante Mahlzeit ändern?", "Jederzeit. Der Plan ist ein Vorschlag. Du entscheidest, was gespeichert, verschoben oder ersetzt wird."),
            ("Können mehrere Personen denselben Plan nutzen?", "Ja. Haushaltsmitglieder teilen Vorrat, Wochenplan und Einkaufsliste, während der Testphase und danach mit einem Bezahlabo."),
        ],
    ),
    "/de/rezepte-mit-zutaten/": dict(
        title="Rezepte mit dem, was du zu Hause hast | Cibello",
        desc="Fotografiere Kühlschrank und Vorrat, prüfe das Ergebnis und erhalte Rezeptideen aus dem, was schon da ist. Cibello zeigt, was fehlt, du entscheidest.",
        eyebrow="Kochen mit dem Vorrat",
        h1="Rezepte mit Zutaten, die du zu Hause hast",
        lead="Die beste Rezeptidee ist die, die du heute Abend tatsächlich kochen kannst. Cibello beginnt deshalb nicht mit einer Rezeptsammlung, sondern mit dem, was in deinem Kühlschrank und Vorratsschrank liegt. Aus mehr als 9.000 Rezepten zeigt die App zuerst die, für die fast alles schon da ist.",
        sections=[
            ("Anfangen bei Kühlschrank und Vorrat", """<p>Viele Rezepte-Apps funktionieren andersherum: Du wählst ein schönes Gericht und stellst im Laden fest, dass die Hälfte der Zutaten fehlt. Cibello geht von den Lebensmitteln aus, die du selbst erfasst oder gescannt hast. Die Vorschläge bevorzugen, was bald verbraucht werden sollte, und zeigen ehrlich, welche Zutaten eventuell noch fehlen. So wird aus „Was essen wir heute?“ eine Frage, die sich in einer Minute beantworten lässt.</p><p>Das klingt nach einer kleinen Umstellung, verändert den Abend aber spürbar. Statt in Rezeptsammlungen zu blättern und Zutatenlisten mit dem Kühlschrank abzugleichen, öffnest du die App und siehst, was mit dem geht, was da ist. Die Rezepte reichen von schnellen Alltagsgerichten bis zu Backideen und Nachtisch, und alle werden nach demselben Prinzip sortiert.</p>"""),
            ("Vom Foto zum brauchbaren Vorrat", """<p>Damit die Rezeptsuche funktioniert, muss die App wissen, was da ist. Dafür musst du nichts eintippen:</p><ul><li>Fotografiere Kühlschrank, Gefrierfach oder Vorratsschrank. Cibello erkennt die Produkte und merkt sich, wo sie stehen, etwa den Käse in der Kühlschranktür.</li><li>Scanne den Kassenbon nach dem Einkauf, damit die neuen Produkte im Vorrat landen.</li><li>Nutze den Barcode für einzelne Packungen.</li><li>Prüfe erkannte Produkte, Mengen und Daten, bevor du speicherst. KI kann sich irren, und ein korrigierter Eintrag ist mehr wert als zehn ungeprüfte.</li></ul><p>Der Vorrat ist die Grundlage für alles Weitere, auch für den <a href="/de/essensplaner/">Essensplaner</a> und die gemeinsame Einkaufsliste.</p>"""),
            ("Wie die Reihenfolge der Vorschläge entsteht", """<p>Cibello sortiert Rezepte nicht nach Beliebtheit, sondern danach, wie gut sie zu deiner Küche passen. Drei Dinge spielen zusammen:</p><table><tbody><tr><th>Kriterium</th><th>Was es bedeutet</th></tr><tr><td>Anteil zu Hause</td><td>Wie viele der Zutaten schon im Vorrat sind. Ein Rezept mit 80 Prozent vorhandenen Zutaten steht weiter oben als eines mit 30 Prozent.</td></tr><tr><td>Bald ablaufend</td><td>Lebensmittel, die in den nächsten Tagen verbraucht werden sollten, bekommen Vorrang.</td></tr><tr><td>Euer Geschmack</td><td>Was der Haushalt bisher gern gekocht und gespeichert hat, sowie eure Ernährungsweise und Allergien.</td></tr></tbody></table><p>Zu jedem Vorschlag gehört eine kurze Begründung, zum Beispiel: weil die Sahne bald abläuft und ihr cremige Gerichte mögt. Du siehst also nicht nur, was vorgeschlagen wird, sondern auch, warum.</p>"""),
            ("Was essen wir heute Abend?", """<p>An einem Dienstag sind die besten Rezepte selten die aufwendigsten. Es sind Pasta, Omelett, Pfannengerichte oder ein einfacher Eintopf mit dem, was ohnehin im Kühlschrank liegt. Weil Cibello nach dem Anteil vorhandener Zutaten sortiert, stehen genau diese Gerichte oben, wenn sie das sind, was sich heute Abend kochen lässt. Fehlt eine Zutat, zeigt die App das an, und du entscheidest, ob es trotzdem passt oder ob du das Rezept für den nächsten Einkauf aufhebst.</p><p>Ein Beispiel: Im Kühlschrank liegen Eier, ein Rest Spinat, etwas Feta und eine halbe Zwiebel. Statt für ein aufwendiges Gericht einzukaufen, steht in Cibello ein Omelett oder eine schnelle Pfanne ganz oben, weil fast alles dafür vorhanden ist und der Spinat bald verbraucht werden sollte. Am nächsten Tag, mit anderem Vorrat, sieht die Liste anders aus. Genau das unterscheidet Vorschläge aus der eigenen Küche von einer festen Rezeptsammlung.</p>"""),
            ("Wochenende, Reste und Essensboxen", """<p>Am Wochenende ist mehr Zeit für Schmorgerichte, Backen oder Gäste. Dann darf ein Vorschlag auch etwas verlangen, das erst noch eingekauft wird. Planst du das Wochenende schon unter der Woche, landet das Fehlende in der Einkaufsliste. Übrig gebliebene Portionen kannst du als Essensboxen im Vorrat führen, sodass sie am Montag nicht vergessen werden. Auch Reste gehören zum Vorrat und können in die Vorschläge einfließen. Wie das im Alltag hilft, weniger wegzuwerfen, steht im Ratgeber <a href="/de/lebensmittelverschwendung-reduzieren/">Lebensmittelverschwendung reduzieren</a>.</p>"""),
            ("Allergien und Ernährungsweisen", """<p>Du kannst Allergien, Unverträglichkeiten und Ernährungsweisen im Profil hinterlegen, damit die Vorschläge dazu passen. Wichtig ist dabei Ehrlichkeit: Rezept- und Allergenfilter sind eine Orientierung, keine Garantie. Lies Zutatenlisten und Verpackungen immer selbst, besonders bei schweren Allergien. Nährwertangaben sind Schätzungen für die Planung, keine Ernährungsberatung. Cibello ersetzt keine ärztliche Beratung.</p><p>Das gilt auch für erkannte Produkte. Wenn die App ein Glas als „Pesto“ erkennt, sagt sie nichts darüber, ob Nüsse enthalten sind. Die Verpackung bleibt die einzige verlässliche Quelle, und die Korrektur eines falsch erkannten Produkts dauert nur einen Moment.</p>"""),
            ("Von der Idee zur Einkaufsliste", """<p>Ist das Gericht gewählt, macht eine gemeinsame Einkaufsliste den nächsten Schritt einfacher. Ziel ist nicht, dass du mehr kaufst, sondern dass klar ist, was fehlt, und dass niemand im Haushalt dasselbe doppelt besorgt. Wer nach dem Einkauf den Kassenbon scannt, hat den Vorrat gleich wieder auf dem aktuellen Stand, und die nächsten Vorschläge bauen darauf auf. Cibello verbindet Rezepte, Wochenplan, Vorrat und Haushalt in einer App, während der Testphase und danach mit einem Bezahlabo auch für alle im Haushalt gemeinsam. Einen Überblick über alle Funktionen findest du auf der <a href="/de/">Startseite</a>. Wer Rezepte-Apps vergleichen möchte, etwa mit SuperCook oder Samsung Food, findet einen englischen <a href="/en/best-recipe-app/">Vergleich von Rezepte-Apps</a>.</p>"""),
        ],
        faq=[
            ("Kann Cibello Rezepte aus Resten vorschlagen?", "Ja. Wenn Reste und Zutaten im Vorrat erfasst sind, fließen sie in die Vorschläge ein wie jedes andere Lebensmittel."),
            ("Muss ich alle Lebensmittel von Hand eintragen?", "Nein. Cibello kann Kühlschrank, Vorrat, Kassenbons und Barcodes scannen. Das Ergebnis prüfst du kurz, bevor es gespeichert wird."),
            ("Berücksichtigt Cibello Allergien?", "Du kannst Allergien und Ernährungsweisen angeben, aber die Filter sind keine Garantie. Lies Zutaten und Verpackungen immer selbst."),
            ("Wie viele Rezepte gibt es?", "Mehr als 9.000, sortiert danach, wie groß der Anteil der Zutaten ist, die du bereits zu Hause hast."),
        ],
    ),
    "/de/lebensmittelverschwendung-reduzieren/": dict(
        title="Lebensmittelverschwendung reduzieren im Alltag | Cibello",
        desc="Weniger wegwerfen ohne schlechtes Gewissen: Überblick über Kühlschrank und Vorrat, Rezepte aus dem, was da ist, und eine Liste, die nur Fehlendes enthält.",
        eyebrow="Weniger wegwerfen, mehr Überblick",
        h1="Lebensmittelverschwendung reduzieren: mit Überblick statt schlechtem Gewissen",
        lead="Das meiste, was zu Hause im Müll landet, war nie als Abfall gedacht. Es wurde nur vergessen: hinten im Kühlschrank, in der angebrochenen Packung, in der Essensbox vom Sonntag. Dieser Ratgeber zeigt, wie ein wenig Überblick den Unterschied macht und wie Cibello dabei hilft.",
        sections=[
            ("Was Lebensmittelverschwendung eigentlich ist", """<p>Lebensmittelverschwendung ist Essen, das noch hätte gegessen werden können, aber weggeworfen wird: Reste, an die sich niemand erinnert, Gemüse, das im Gemüsefach weich wird, oder Joghurt, der das Mindesthaltbarkeitsdatum überschritten hat, ohne dass jemand geprüft hat, ob er noch gut ist. In Privathaushalten geht es dabei selten um Gleichgültigkeit. Meist fehlt schlicht der Überblick darüber, was da ist und was zuerst verbraucht werden sollte. Genau hier setzt ein Vorrat mit Ort und Datum an, ergänzt um rechtzeitige Erinnerungen.</p><p>Weniger wegzuwerfen lohnt sich doppelt. Jedes Lebensmittel, das gegessen statt entsorgt wird, ist Geld, das nicht zweimal ausgegeben wurde, und Aufwand für Anbau, Transport und Kühlung, der nicht umsonst war. Der wichtigste Effekt ist aber ein ruhigerer Alltag: Wer weiß, was da ist, muss weniger entscheiden und ärgert sich seltener.</p>"""),
            ("Sehen, was in Vergessenheit gerät", """<p>Ein digitaler Vorrat ist die einfachste Art, den Kühlschrank auch dann im Blick zu haben, wenn du im Supermarkt stehst. Mit Cibello fotografierst du Kühlschrank, Gefrierfach und Vorratsschrank. Die App erkennt die Produkte und merkt sich, wo sie stehen. Kassenbons und Barcodes lassen sich ebenfalls scannen, und du prüfst jedes Ergebnis, bevor es gespeichert wird. Wenn Haltbarkeitsangaben hinterlegt sind, erinnert Cibello dich freundlich, bevor etwas schlecht wird. Ohne Vorwürfe und ohne Kalorienzählen. Datumsangaben und KI-Ergebnisse können falsch sein, deshalb gilt immer: ansehen, riechen und die Hinweise auf der Verpackung beachten.</p>"""),
            ("Mindesthaltbarkeitsdatum ist kein Wegwerfdatum", """<p>Zwei Angaben werden oft verwechselt. „Mindestens haltbar bis“ sagt, bis wann der Hersteller Geschmack und Konsistenz garantiert. Viele Produkte sind danach noch tagelang oder wochenlang in Ordnung, etwa Nudeln, Reis, Konserven, Joghurt oder Hartkäse. „Zu verbrauchen bis“ steht auf leicht verderblichen Lebensmitteln wie Hackfleisch oder frischem Fisch und sollte ernst genommen werden. Eine kleine Orientierung:</p><ul><li>Trockenwaren wie Reis, Nudeln, Mehl und Konserven: meist lange über das Mindesthaltbarkeitsdatum hinaus genießbar, wenn die Packung unbeschädigt ist.</li><li>Joghurt, Quark, Hartkäse, Eier: oft noch einige Tage bis Wochen nach dem Datum gut. Aussehen, Geruch und Geschmack prüfen.</li><li>Fleisch, Fisch und Geflügel mit Verbrauchsdatum: nach Ablauf nicht mehr verwenden.</li><li>Für Kinder, Schwangere und Menschen mit geschwächtem Immunsystem: im Zweifel vorsichtiger sein.</li></ul>"""),
            ("Rezepte rund um das planen, was da ist", """<p>Statt für jedes Gericht einen neuen Satz Zutaten zu kaufen, kannst du von dem ausgehen, was ohnehin verbraucht werden muss. Cibello gleicht deinen Vorrat mit mehr als 9.000 Rezepten ab und stellt die nach oben, für die fast alles da ist. Vorschläge bevorzugen Lebensmittel, die bald ablaufen, und erklären, warum sie auftauchen. Was wirklich fehlt, wandert in die Einkaufsliste. Wie das im Detail funktioniert, liest du im Ratgeber <a href="/de/rezepte-mit-zutaten/">Rezepte mit Zutaten, die du zu Hause hast</a>. Und wer die ganze Woche im Voraus denkt, verbraucht empfindliche Lebensmittel zuerst: dafür gibt es den <a href="/de/essensplaner/">Essensplaner</a>.</p>"""),
            ("Einkaufen mit Liste statt aus dem Bauch", """<p>Ein großer Teil der Verschwendung beginnt im Laden: die zweite Packung Frischkäse, weil niemand wusste, dass noch eine da ist, oder der Salat, für den es dann doch keinen Plan gab. Wenn der Haushalt Vorrat und Einkaufsliste teilt, sieht jeder dasselbe Bild. Die Liste enthält nur, was für die geplanten Gerichte fehlt, und wer unterwegs etwas kauft, kann es für alle sichtbar machen. Während der Testphase und danach mit einem Bezahlabo steht diese gemeinsame Übersicht allen im Haushalt offen.</p><p>Hilfreich ist auch, mit dem Wocheneinkauf nicht bei null anzufangen. Ein kurzer Blick in den Vorrat vor dem Einkauf zeigt, was noch da ist und was in den nächsten Tagen ohnehin gekocht werden sollte. Wer dann zuerst plant und danach einkauft, kommt mit weniger Tüten nach Hause und wirft am Ende der Woche weniger weg.</p>"""),
            ("Reste und Essensboxen mitdenken", """<p>Reste sind kein Problem, sondern Vorrat. Übrig gebliebene Portionen kannst du als Essensboxen in Cibello führen, damit sie nicht hinter der Milch verschwinden. Ein gefüllter Behälter, der im Vorrat steht, wird eher am nächsten Tag zum Mittagessen als einer, an den sich nur die Person erinnert, die ihn eingeräumt hat. Bewährt hat sich auch ein fester Restetag pro Woche, an dem nichts Neues gekocht wird.</p>"""),
            ("Gewohnheiten statt schlechtes Gewissen", """<p>Weniger wegzuwerfen ist eine Frage der Routine, nicht der Moral. Cibello erinnert sanft und schlägt Rezepte vor, doch was gegessen, eingefroren oder entsorgt wird, entscheidest du. Ein paar Gewohnheiten, die im Alltag viel bewirken:</p><ul><li>Einmal pro Woche den Vorrat aktualisieren, zum Beispiel vor dem Wocheneinkauf.</li><li>Empfindliche Lebensmittel am Anfang der Woche einplanen.</li><li>Angebrochene Packungen und Reste im Kühlschrank nach vorn stellen.</li><li>Übrige Portionen sofort als Essensbox erfassen, nicht erst am nächsten Tag.</li><li>Beim Einkauf nur mitnehmen, was auf der Liste steht oder wofür es einen Plan gibt.</li></ul><p>Keine dieser Gewohnheiten muss perfekt sitzen. Schon zwei davon machen einen Unterschied, den du am Ende des Monats im Mülleimer und im Portemonnaie merkst. Mehr über die App erfährst du auf der <a href="/de/">Startseite</a>.</p>"""),
        ],
        faq=[
            ("Kann eine App garantieren, dass Lebensmittel noch sicher sind?", "Nein. Prüfe Datum, Lagerung, Geruch, Aussehen und die Hinweise auf der Verpackung immer selbst. Cibello erinnert und schlägt vor, entscheidet aber nicht."),
            ("Wie helfen Rezepte dabei, weniger wegzuwerfen?", "Rezepte aus dem Vorrat machen es leichter, vorhandene Zutaten zu verbrauchen, bevor Neues gekauft wird. Cibello stellt Gerichte nach oben, für die fast alles da ist."),
            ("Können mehrere Personen denselben Vorrat pflegen?", "Ja. Die Haushaltsfunktion ist für einen gemeinsamen Überblick gedacht, während der Testphase und danach mit einem Bezahlabo."),
            ("Darf ich Lebensmittel nach dem Mindesthaltbarkeitsdatum noch essen?", "Häufig ja, wenn Aussehen, Geruch und Geschmack in Ordnung sind und die Packung unbeschädigt war. Bei einem Verbrauchsdatum, etwa auf Hackfleisch oder Fisch, gilt das nicht."),
        ],
    ),
}

HUBTEXT = """<section><h2>Was essen wir heute? Die Antwort steht schon in deiner Küche</h2><p>Die meisten Rezepte-Apps beginnen bei Rezepten. Cibello beginnt bei dem, was tatsächlich in Kühlschrank, Gefrierfach und Vorratsschrank liegt. Du fotografierst, die App erkennt die Produkte und merkt sich, wo sie stehen. Aus mehr als 9.000 Rezepten zeigt sie dann zuerst die, für die fast alles schon da ist, und erklärt, warum ein Vorschlag auftaucht. Wie das im Alltag funktioniert, liest du im Ratgeber <a href="/de/rezepte-mit-zutaten/">Rezepte mit Zutaten, die du zu Hause hast</a>.</p></section>
<section><h2>Einmal planen, eine Woche lang entspannter kochen</h2><p>Ein Wochenplan nimmt die Entscheidung aus dem müden Moment um 17 Uhr heraus. Cibello schlägt eine Woche vor, die zwischen Gerichten und Zutaten variiert und empfindliche Lebensmittel zuerst einplant. Du verschiebst, streichst und ergänzt, bis der Plan zu euch passt, und die Einkaufsliste sammelt nur das, was fehlt. Mehr dazu im Ratgeber <a href="/de/essensplaner/">Essensplaner</a>.</p></section>
<section><h2>Weniger wegwerfen, ohne erhobenen Zeigefinger</h2><p>Was zu Hause im Müll landet, wurde meist nur vergessen. Ein Vorrat mit Ort und Datum, freundliche Erinnerungen, bevor etwas schlecht wird, und Rezepte, die bald ablaufende Zutaten bevorzugen, ändern das Stück für Stück. Wie du <a href="/de/lebensmittelverschwendung-reduzieren/">Lebensmittelverschwendung reduzieren</a> kannst, ohne deinen Alltag umzukrempeln, steht im dritten Ratgeber.</p></section>
<section><h2>Ehrlich über KI, klar bei deinen Daten</h2><p>Cibello ist ein Hilfsmittel, keine Instanz. Die KI kann Produkte übersehen oder Daten falsch lesen, deshalb prüfst du jedes Scanergebnis, bevor es gespeichert wird. Rezept- und Allergenfilter sind Orientierung, keine Garantie. Deine Daten liegen in der EU, und das Konto löschst du jederzeit selbst in der App. Testen kannst du 14 Tage lang ohne Karte. Die App richtet sich an Erwachsene ab 18 Jahren.</p></section>"""

ABOUT = dict(
    title="Über Cibello: die App und das Unternehmen dahinter | LandveX AB",
    desc="Cibello wird von LandveX AB in Tyresö, Schweden, entwickelt. Warum es die App gibt, wie wir über KI, Daten und Lebensmittelverschwendung denken und wie du uns erreichst.",
    h1="Über Cibello",
    lead="Cibello ist eine schwedische Food-App von LandveX AB. Sie wurde gebaut, um eine Frage zu beantworten, die in fast jedem Haushalt jeden Tag gestellt wird: Was essen wir? Diese Seite erklärt, was wir vorhaben, wie wir mit KI und Daten umgehen und wie du uns erreichst.",
    sections=[
        ("Warum es Cibello gibt", """<p>Die meisten Rezepte-Apps beginnen bei Rezepten. Wir wollten bei der Küche beginnen: bei dem, was wirklich im Kühlschrank, im Gefrierfach und im Vorratsschrank liegt, was bald abläuft und was der Haushalt gern isst. Deshalb ist der Kern von Cibello ein Vorrat, dein „Food Twin“, der aus Fotos, Kassenbons und Barcodes entsteht. Rezepte, Wochenplan, Einkaufsliste und Erinnerungen bauen alle auf denselben Daten auf. Das Ziel ist weniger Alltagsstress und <a href="/de/lebensmittelverschwendung-reduzieren/">weniger Lebensmittelverschwendung</a>, ohne Bevormundung.</p>"""),
        ("Wie wir über KI denken", """<p>KI macht Cibello möglich, aber sie irrt sich manchmal. Beim Scannen kann ein Produkt falsch erkannt, etwas hinten im Regal übersehen oder ein Datum falsch geraten werden. Deshalb prüfst du Ergebnisse immer, bevor sie gespeichert werden, und deshalb sind Vorschläge nur Vorschläge. Rezept- und Allergenfilter sind eine Orientierung, nie eine Garantie, und Nährwerte sind Schätzungen für die Planung, keine Ernährungsberatung. Cibellos eigene Modelle werden nur mit deinen Korrekturen trainiert und, wenn du separat zustimmst, mit bereinigten Bildern. Beide Optionen sind standardmäßig aus. Mehr dazu in der <a href="/de/privacy/">Datenschutzerklärung</a>.</p>"""),
        ("Deine Daten", """<p>Alles wird in der EU gespeichert. Du kannst deine Daten in der App einsehen und dein <a href="/de/delete-account/">Konto jederzeit löschen</a>, ohne den Support zu kontaktieren. Wir verkaufen keine personenbezogenen Daten.</p>"""),
        ("Das Unternehmen", """<p>Cibello wird von LandveX AB entwickelt und betrieben, Organisationsnummer 559141-7042, Antennvägen 2, 135 48 Tyresö, Schweden. Die App ist für iOS und Android in zwölf Sprachen verfügbar und wird in Schweden entwickelt. Vorerst richtet sie sich an Personen ab 18 Jahren, weil die Bedingungen des verwendeten KI-Dienstes erwachsene Nutzer verlangen. Die Testphase dauert 14 Tage und erfordert keine Karte.</p>"""),
        ("Kontakt", """<p>Allgemeine Fragen und Kooperationen: <a href="mailto:hello@cibello.app">hello@cibello.app</a>. Support: <a href="mailto:support@cibello.app">support@cibello.app</a>. Datenschutz: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>. Presseanfragen sind unter derselben Adresse willkommen; wir antworten normalerweise innerhalb weniger Werktage.</p><p>Folge uns auf <a href="https://www.instagram.com/cibelloapp/" rel="noopener">Instagram</a>, <a href="https://www.tiktok.com/@cibello73" rel="noopener">TikTok</a> und <a href="https://www.facebook.com/profile.php?id=61593336222919" rel="noopener">Facebook</a>.</p>"""),
    ],
)

PRESS = dict(
    title="Presse und Medien: Fakten, Bilder und Kontakt | Cibello",
    desc="Pressemappe zu Cibello: Kurzbeschreibung, Fakten zur App, Logo und Bilder sowie der Pressekontakt bei LandveX AB in Tyresö, Schweden. Frei verwendbar im redaktionellen Kontext.",
    eyebrow="Für Journalistinnen und Journalisten",
    h1="Presse und Medien",
    lead="Alles, was du brauchst, um über Cibello zu schreiben: eine kurze Beschreibung, Fakten, Bilder und ein Kontakt, der schnell antwortet. Alles auf dieser Seite darf im redaktionellen Kontext frei verwendet werden.",
    sections=[
        ("Cibello in Kürze", """<p>Cibello ist eine schwedische Food-App, die Kühlschrank und Vorrat fotografiert, einen Vorrat mit Ort und Datum führt, Rezepte aus dem vorschlägt, was tatsächlich zu Hause ist, die Woche plant und die Einkaufsliste mit dem Haushalt teilt. Sie erinnert freundlich, bevor Lebensmittel schlecht werden, und bewertet nie, was jemand isst. Verfügbar für iOS und Android in zwölf Sprachen, mit Datenspeicherung in der EU, entwickelt von LandveX AB in Tyresö, Schweden.</p><p><strong>In einem Satz:</strong> Cibello ist die App, die sieht, was du zu Hause hast, und die Frage „Was essen wir?“ beantwortet.</p>"""),
        ("Fakten", """<ul><li>Verfügbar für iOS und Android. Altersgrenze 18+.</li><li>Testphase: 14 Tage ohne Karte, danach ein Abonnement über den App Store oder Google Play.</li><li>Rezepte: mehr als 9.000, abgeglichen mit dem Vorrat der Nutzerin oder des Nutzers.</li><li>Sprachen: Schwedisch, Englisch, Deutsch, Französisch, Spanisch, Italienisch, Niederländisch, Polnisch, Dänisch, Norwegisch, Finnisch, Portugiesisch.</li><li>Daten: Speicherung in der EU. Konto und Daten können in der App gelöscht werden.</li><li>KI: Scannen von Kühlschrank, Vorrat, Kassenbons und Barcodes. Das Ergebnis wird immer von der Nutzerin oder dem Nutzer geprüft. Cibellos eigene Modelle werden nur mit Korrekturen der Nutzer trainiert und, mit separater Einwilligung, mit bereinigten Bildern.</li><li>Preise: kostenlose Testphase, danach ein Bezahlabo für die Haushaltsfunktionen. Aktuelle Preise im App Store und bei Google Play.</li><li>Download: <a href="https://apps.apple.com/app/id6807100747" rel="noopener">App Store</a> und <a href="https://play.google.com/store/apps/details?id=com.cibello.app" rel="noopener">Google Play</a>.</li><li>Unternehmen: LandveX AB, Org.-Nr. 559141-7042, Antennvägen 2, 135 48 Tyresö, Schweden.</li></ul>"""),
        ("Logo und Bilder", """<ul><li><a href="/img/icon-512.png">App-Icon, 512×512 PNG</a></li><li><a href="/img/og-de.png">Teilen-Bild, 1200×630 PNG (Deutsch)</a></li><li><a href="/favicon.svg">Symbol, SVG</a></li></ul><p>Screenshots der App gibt es auf Anfrage. Bilder dürfen im redaktionellen Kontext mit Nennung von Cibello frei verwendet werden.</p>"""),
        ("Pressekontakt", """<p><a href="mailto:hello@cibello.app?subject=Presseanfrage">hello@cibello.app</a>. Auf Presseanfragen antworten wir normalerweise innerhalb eines Werktags. Der Gründer steht für Interviews über Lebensmittelverschwendung in Haushalten, KI im Alltag und die Frage, warum „Was essen wir?“ eine Frage ist, die es zu lösen lohnt, zur Verfügung.</p><p>Mehr über das Unternehmen: <a href="/de/about/">Über Cibello</a>.</p>"""),
    ],
)

NEWS = dict(
    title="Neu bei Cibello: Updates und neue Ratgeber",
    desc="Neue Ratgeber, Werkzeuge und Updates auf cibello.app, mit Datum. Abonnieren per RSS.",
    h1="Neu bei Cibello",
    lead="Was auf der Website und in der App hinzugekommen ist, das Neueste zuerst. Ein RSS-Feed ist verfügbar.",
    rss_label="RSS-Feed",
    entries=[
        ("2026-09-04", "Neuer Ratgeber: Lebensmittelverschwendung in Schweden in Zahlen", "/matsvinn-statistik/",
         "Offizielle Zahlen der schwedischen Umwelt- und Lebensmittelbehörden auf einer Seite (auf Schwedisch): 880.000 Tonnen Lebensmittelabfall, 16 kg essbare Lebensmittel pro Person in Haushalten und 1.330 Kronen pro Person und Jahr, mit Quelle für jede Zahl."),
        ("2026-09-04", "Drei neue englische Ratgeber und zwei Vergleiche", "/en/best-meal-planning-app/",
         "Was heute Abend essen, KI-Essensplaner und Vorrats-App, dazu ehrliche Vergleiche von Essensplanungs-Apps und Rezepte-Apps mit Mealime, Samsung Food, Plan to Eat, Paprika und SuperCook."),
        ("2026-09-04", "Vollständige Landingpages in zwölf Sprachen", "/de/",
         "Jede Sprache hat jetzt eine vollständige Landingpage statt einer kurzen Textseite, und nichts wird mehr im Browser übersetzt."),
        ("2026-08-30", "Datenschutzerklärung und Nutzungsbedingungen Version 2.0", "/de/privacy/",
         "Aktualisierte Texte zur Gemini-Analyse, zum freiwilligen Training der Cibello-KI, zur 14-tägigen Testphase ohne Karte und zur Altersgrenze 18+. Deutsche Übersetzungen sind verfügbar; die schwedische Fassung gilt."),
    ],
)

PRIVACY = dict(
    title="Datenschutzerklärung | Cibello",
    desc="So verarbeitet Cibello personenbezogene Daten, Bilder, die Gemini-Analyse und das freiwillige Training der Cibello-KI. Deutsche Übersetzung der schwedischen Datenschutzerklärung, Version 2.0.",
    h1="Datenschutzerklärung",
    notice="<strong>Kurz gesagt:</strong> Für die heutige Bildanalyse wird ein externer KI-Dienst genutzt. Cibellos eigenes KI-Modell darf nur mit den eigenen Korrekturen und bereinigten Bildern der Nutzerin oder des Nutzers trainiert werden, und nur nach einer separaten, freiwilligen und aktiven Entscheidung in der Einführung. Antworten externer KI werden nie als Trainingsgrundlage verwendet.",
    body="""<h2>1. Verantwortlicher</h2>
<p>LandveX AB, Org.-Nr. 559141-7042, Antennvägen 2, 135 48 Tyresö, Schweden, ist der für die Verarbeitung personenbezogener Daten Verantwortliche für Cibello. Datenschutzfragen richtest du an <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>

<h2>2. Daten und Zwecke</h2>
<ul>
<li><strong>Konto:</strong> E-Mail-Adresse, Anzeigename, Authentifizierungsidentität und Sicherheitsprotokolle, um das Konto anzulegen und zu schützen.</li>
<li><strong>Lebensmittel- und Haushaltsdaten:</strong> Vorrat, Rezepte, Vorlieben, Allergien und eigene Korrekturen für die Funktionen der App.</li>
<li><strong>Bilder:</strong> Bilder, die der Nutzer zum Scannen auswählt, um Lebensmittel oder Kassenbons zu erkennen.</li>
<li><strong>Zahlung:</strong> Abonnementstatus und Transaktionsreferenzen. Karten- und Zahlungsdaten werden vom Apple App Store oder von Google Play verarbeitet.</li>
<li><strong>Technische Daten:</strong> Fehler, Leistung und Produktanalyse, nur entsprechend der Wahl des Nutzers und notwendiger Sicherheitsanforderungen.</li>
<li><strong>Schutz vor Missbrauch der Testphase:</strong> Ein mit einem Schlüssel erzeugter, pseudonymer HMAC-Fingerabdruck der normalisierten E-Mail-Adresse wird höchstens fünf Jahre gespeichert. Er kann weder zur Anmeldung noch zur Kontaktaufnahme genutzt werden und enthält weder die Klartextadresse noch eine Nutzer-ID oder Firebase-Identität. Sein einziger Zweck ist es, wiederholte Testphasen nach Kontolöschung und Neuregistrierung zu verhindern.</li>
</ul>

<h2>3. Gemini im Produktivbetrieb</h2>
<p>Ausgewählte Bilder und die notwendige Anweisung werden an die Google Gemini API gesendet, um das Ergebnis zu erzeugen, das in der App angezeigt wird. Cibello nutzt den kostenpflichtigen Dienst innerhalb des EWR. Nach den Bedingungen von Google werden Daten im kostenpflichtigen Dienst nicht zur Verbesserung der Produkte von Google verwendet; eine begrenzte Protokollierung zur Sicherheit und Missbrauchsbekämpfung kann jedoch vorkommen, sofern kein besonderer Modus ohne Speicherung gilt. Cibello verspricht daher keine speicherfreie Verarbeitung außerhalb der eigenen Umgebung ohne technische Bestätigung des Anbieters.</p>
<p>Gemini-Ergebnisse sind automatische Schätzungen. Der Nutzer muss Inhalt, Allergene, Daten und Mengen prüfen, bevor die Informationen verwendet werden.</p>

<h2>4. Cibellos eigenes KI-Modell: separates und freiwilliges Training</h2>
<p>Cibello entwickelt ein eigenes KI-Modell. Der Trainingsablauf ist technisch und rechtlich von dem externen KI-Dienst getrennt, der dem Nutzer die heutigen Ergebnisse liefert:</p>
<ul>
<li>Antworten, Schlussfolgerungen oder Vorschläge von Gemini werden nie als Trainingslabels oder Trainingsgrundlage in Cibellos eigenes KI-Modell exportiert.</li>
<li><strong>Anonymisierte KI-Verbesserung</strong> erlaubt, dass die ausdrückliche Korrektur des Nutzers oder eine manuell bestätigte Antwort ohne Bild verwendet wird.</li>
<li><strong>Bildtraining</strong> erlaubt, dass eine bereinigte Kopie des Bildes des Nutzers mit dessen eigener Korrektur verknüpft wird. Metadaten werden entfernt, und das Bild wird vor der Speicherung in der Größe begrenzt.</li>
<li>Die Einführung zeigt eine gemeinsame, klare Wahl für diese beiden Teile desselben Trainingszwecks. Die Wahl ist nicht vorausgewählt, und die App funktioniert auch, wenn der Nutzer nicht zustimmt.</li>
<li>Die Einwilligung kann über eine Schaltfläche im Profil widerrufen werden. Dann wird die künftige Nutzung gestoppt, die app-eigene aktive Trainingsdatenbank wird bereinigt und Bildreferenzen werden entfernt. Bereits erzeugte, aggregierte Modellparameter lassen sich normalerweise nicht mehr einer Person zuordnen.</li>
<li>Cibello AI beeinflusst die Produktivantwort erst, wenn dokumentierte Benchmark- und Sicherheitsgrenzen erreicht wurden.</li>
</ul>

<h2>5. Rechtsgrundlage</h2>
<p>Konto und Kernfunktionen werden zur Erfüllung des Vertrags verarbeitet. Sicherheitsprotokollierung und der begrenzte Fingerabdruck gegen wiederholte Testphasen werden auf Grundlage des berechtigten Interesses verarbeitet. Rechtliche Verpflichtungen können eine andere begrenzte Verarbeitung erfordern. Freiwillige Produktanalyse, KI-Verbesserung und Bildtraining beruhen auf separaten Einwilligungen, die widerrufen werden können.</p>

<h2>6. Speicherung und Empfänger</h2>
<p>Daten werden so lange gespeichert, wie es für den Dienst, die Sicherheit, rechtliche Anforderungen und die dokumentierte Aufbewahrung von Backups erforderlich ist. Zu den Anbietern können AWS für Betrieb und Speicherung, Firebase für die Authentifizierung, Google Gemini für die gewählte KI-Analyse sowie Apple oder Google für die Zahlung gehören. Cibello verkauft keine personenbezogenen Daten. Der Fingerabdruck für die Testphase wird spätestens fünf Jahre nach Beginn der Testphase automatisch gelöscht.</p>

<h2>7. Deine Rechte</h2>
<p>Du kannst Auskunft, Berichtigung, Datenübertragbarkeit, Einschränkung oder Löschung verlangen und bestimmten Verarbeitungen widersprechen. Einwilligungen änderst du im Profil. Das Konto kann direkt in der App oder über die <a href="/de/delete-account/">Seite zur Kontolöschung</a> gelöscht werden. Du kannst dich außerdem an die schwedische Datenschutzbehörde (Integritetsskyddsmyndigheten) wenden.</p>

<h2>8. Alter</h2>
<p>Cibello richtet sich bis auf Weiteres an Personen, die mindestens 18 Jahre alt sind, weil die Bedingungen des verwendeten Gemini-API-Dienstes erwachsene Nutzer verlangen. Die Altersanforderung wird überprüft, wenn sich die technische Anbieterlösung ändert.</p>

<h2>9. Änderungen</h2>
<p>Wesentliche Änderungen erhalten eine Versionsnummer und erfordern vor der weiteren Nutzung eine erneute Zustimmung in der App.</p>""",
)

TERMS = dict(
    title="Nutzungsbedingungen | Cibello",
    desc="Nutzungsbedingungen für Cibello: Konto, Altersgrenze, Abonnements und die 14-tägige Testphase, KI-Analyse und sichere Nutzung. Deutsche Übersetzung der schwedischen Bedingungen, Version 2.0.",
    h1="Nutzungsbedingungen",
    body="""<h2>1. Vertrag und Altersgrenze</h2>
<p>Diese Bedingungen gelten zwischen dem Nutzer und LandveX AB, Org.-Nr. 559141-7042. Cibello ist bis auf Weiteres nur für Personen, die mindestens 18 Jahre alt sind. Mit dem Anlegen eines Kontos bestätigt der Nutzer sein Alter und akzeptiert diese Bedingungen sowie die <a href="/de/privacy/">Datenschutzerklärung</a>.</p>

<h2>2. Der Dienst</h2>
<p>Cibello hilft dem Nutzer, Lebensmittel zu organisieren, ausgewählte Bilder und Kassenbons auszuwerten sowie Rezept- und Mahlzeitenvorschläge zu erhalten. Ergebnisse können unvollständig oder fehlerhaft sein und müssen vom Nutzer geprüft werden.</p>

<h2>3. Keine medizinische oder professionelle Beratung</h2>
<p>Cibello bietet Inspiration und allgemeine Informationen, keine medizinische, ernährungswissenschaftliche, allergologische oder sonstige professionelle Beratung. Der Nutzer ist dafür verantwortlich, Zutaten, Allergene, Portionsgröße, Haltbarkeit, Zubereitung und Lebensmittelsicherheit zu prüfen. Bei Krankheit, Schwangerschaft, schwerer Allergie oder besonderen Bedürfnissen ist qualifiziertes medizinisches Fachpersonal zu befragen.</p>

<h2>4. KI und menschliche Kontrolle</h2>
<p>Für die derzeitige Produktivanalyse wird ein externer KI-Dienst genutzt. Cibellos eigenes KI-Modell wird parallel entwickelt, darf aber nur gemäß der Einwilligung und den Einschränkungen trainiert werden, die in der <a href="/de/privacy/">Datenschutzerklärung</a> beschrieben sind. Antworten externer KI werden nie als Trainingsgrundlage verwendet. Automatische Ergebnisse müssen vom Nutzer immer korrigiert werden können.</p>

<h2>5. Freiwillige Trainingseinwilligungen</h2>
<p>Der Zugang zu Cibellos Kernfunktionen darf nicht von einer Einwilligung in KI-Verbesserung oder Bildtraining abhängig gemacht werden. Die Wahl ist von Anfang an ausgeschaltet, von der Zustimmung zu den Bedingungen getrennt und kann im Profil geändert werden.</p>

<h2>6. Konto und Sicherheit</h2>
<p>Der Nutzer muss korrekte Angaben machen, seine Anmeldedaten schützen und Cibello über vermuteten Missbrauch informieren. Das Konto kann im Profil oder über den <a href="/de/delete-account/">Ablauf im Web</a> gelöscht werden.</p>

<h2>7. Abonnement und Zahlung</h2>
<p>Digitale Abonnements in der mobilen App werden über den Apple App Store oder Google Play gekauft und verwaltet. Cibellos servergesteuerte 14-tägige Testphase ohne Karte gilt einmal pro E-Mail-Identität innerhalb eines Zeitraums von fünf Jahren. Ein gelöschtes Konto kann neu angelegt werden, erhält aber nicht automatisch eine neue kostenlose Testphase. Preis, Laufzeit, automatische Verlängerung und Kündigung werden vom jeweiligen Store vor dem Kauf angezeigt. Erstattungen werden nach den Regeln des Stores und nach zwingendem Verbraucherrecht abgewickelt.</p>

<h2>8. Zulässige Nutzung</h2>
<p>Der Dienst darf nicht für rechtswidrige Inhalte, Rechtsverletzungen, Belästigung, automatisierte Überlastung, die Umgehung von Sicherheitsmaßnahmen oder Versuche, Daten anderer Nutzer zu extrahieren, verwendet werden. Cibello darf Konten bei Sicherheitsrisiken oder wesentlichen Vertragsverstößen einschränken.</p>

<h2>9. Verfügbarkeit und Änderungen</h2>
<p>Der Dienst wird laufend weiterentwickelt und kann vorübergehend nicht verfügbar sein. Funktionen dürfen aus Sicherheits-, Rechts-, Qualitäts- oder technischen Gründen geändert werden. Wesentliche Änderungen der Bedingungen erhalten eine Versionsnummer und erfordern eine erneute Zustimmung.</p>

<h2>10. Haftung und zwingendes Recht</h2>
<p>LandveX AB haftet nach dem anwendbaren zwingenden Recht. Nichts in diesen Bedingungen beschränkt Rechte, die nicht rechtswirksam abbedungen werden können. Es gilt schwedisches Recht; Verbraucher können sich zusätzlich auf zwingendes Recht und das zuständige Gericht in ihrem Wohnsitzland berufen.</p>

<h2>11. Kontakt</h2>
<p>Support: <a href="mailto:support@cibello.app">support@cibello.app</a>. Datenschutz: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>""",
)

DELETE = dict(
    title="Konto und Daten löschen | Cibello",
    desc="So löschst du dein Cibello-Konto und die zugehörigen personenbezogenen Daten direkt in der App oder per E-Mail. Deutsche Übersetzung der schwedischen Anleitung.",
    h1="Konto und Daten löschen",
    body="""<h2>Direkt in der App</h2>
<ol>
<li>Melde dich in Cibello an.</li>
<li>Öffne <strong>Profil</strong>.</li>
<li>Wähle <strong>Konto löschen</strong> und bestätige.</li>
</ol>
<p>Konto, Firebase-Identität, aktive Bilder und persönliche App-Daten werden gelöscht. Finanzielle Transaktionsreferenzen können pseudonymisiert und aufbewahrt werden, wenn das Gesetz es verlangt. Backups werden gemäß der dokumentierten Aufbewahrungsfrist ausgetauscht.</p>

<h2>Wenn du die App nicht öffnen kannst</h2>
<p>Sende die Anfrage von der im Konto registrierten E-Mail-Adresse an <a href="mailto:privacy@cibello.app?subject=Mein%20Cibello-Konto%20l%C3%B6schen">privacy@cibello.app</a>. Schreibe „Mein Cibello-Konto löschen“. Wir prüfen, dass du die Adresse kontrollierst, bevor wir löschen.</p>

<h2>Trainingsdaten</h2>
<p>Bei der Löschung werden die Korrekturen und Bildreferenzen des Nutzers aus der aktiven Trainingsdatenbank entfernt. Gemini-Antworten wurden nie als Trainingsgrundlage für Cibello AI exportiert. Bereits aggregierte Modellparameter lassen sich normalerweise nicht mehr einer Person zuordnen.</p>""",
)

UI = dict(
    faq_title="Häufige Fragen",
    privacy_nav="Datenschutz",
    terms_nav="Nutzungsbedingungen",
    delete_nav="Konto löschen",
    legal_meta="Cibello · Version 2.0 · gültig ab 30. August 2026 · deutsche Übersetzung",
    translation_label="Zu dieser Übersetzung:",
    translation_note='Dies ist eine deutsche Übersetzung des schwedischen Originals (<a href="{sv}" lang="sv">Original auf Schwedisch</a>). Bei Abweichungen gilt die schwedische Fassung.',
)
