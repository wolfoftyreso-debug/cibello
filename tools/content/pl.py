"""Polish content for cibello.app. Structure follows tools/content/_schema.py.

All strings are HTML fragments where noted. Legal texts are faithful translations of
integritet.html, villkor.html and delete-account.html (version 2.0); the Swedish version
prevails and the page says so.
"""

LANG = "pl"

# ---------------------------------------------------------------------------
# The three guides. Order: planner, recipes, waste.
# ---------------------------------------------------------------------------

GUIDES = {
    "/pl/planer-posilkow/": dict(
        title="Planer posiłków: jadłospis na tydzień | Cibello",
        desc="Jak ułożyć jadłospis na tydzień, który da się utrzymać: zacznij od tego, co masz w kuchni, zadbaj o różnorodność i kupuj tylko to, czego brakuje.",
        eyebrow="Planowanie posiłków na tydzień",
        h1="Planer posiłków na spokojniejszy tydzień",
        lead="Pytanie „co dzisiaj na obiad?” wraca codziennie około siedemnastej, zwykle wtedy, gdy masz najmniej siły na decyzje. Plan posiłków na tydzień przenosi tę decyzję na spokojniejszy moment. Cibello pomaga go ułożyć na podstawie tego, co już masz w lodówce, zamrażarce i spiżarni.",
        sections=[
            ("Dlaczego jadłospis na tydzień naprawdę pomaga", """<p>Większość codziennego stresu w kuchni nie bierze się z gotowania, tylko z wybierania. Kiedy plan na tydzień jest gotowy, po powrocie do domu wiesz, co jesz, wiesz, że składniki są na miejscu, i nie musisz niczego wymyślać na głodno. Zakupy stają się krótsze, bo lista wynika z planu, a nie z impulsu przy półce.</p><p>Drugi zysk jest mniej oczywisty: mniej zmarnowanego jedzenia. Gdy posiłki są zaplanowane wokół produktów, które już masz, otwarte opakowania i warzywa z końca tygodnia dostają swoją szansę, zamiast czekać w lodówce na lepsze czasy. Więcej o tym piszemy w poradniku <a href="/pl/ograniczanie-marnowania-zywnosci/">jak ograniczyć marnowanie żywności w domu</a>.</p>"""),
            ("Zacznij od tego, co już masz w kuchni", """<p>Dobry planer posiłków nie zaczyna od przepisów, ale od Twojej kuchni. W Cibello robisz zdjęcie lodówki, zamrażarki i spiżarni, a aplikacja rozpoznaje produkty i zapamiętuje, gdzie stoją. Możesz też zeskanować paragon po zakupach albo kod kreskowy z opakowania. Rozpoznawanie oparte na AI czasem się myli, dlatego wynik zawsze sprawdzasz przed zapisaniem: poprawiasz nazwę, ilość czy datę, jeśli coś się nie zgadza.</p><p>Tak powstaje Twój spis zapasów. Na jego podstawie Cibello proponuje przepisy uszeregowane według tego, jaka część składników jest już w domu, i podpowiada, co warto zużyć w pierwszej kolejności. Produkty z krótkim terminem mają wtedy naturalne miejsce na początku tygodnia, a te trwalsze mogą poczekać.</p>"""),
            ("Jak ułożyć plan tygodnia krok po kroku", """<ol><li><strong>Przejrzyj zapasy.</strong> Zaktualizuj spis po zakupach lub po większym gotowaniu. Zajmuje to chwilę, a cała reszta opiera się na tym kroku.</li><li><strong>Wybierz dni, które planujesz.</strong> Nie musisz planować siedmiu obiadów. Cztery lub pięć dań plus miejsce na resztki i jeden luźny wieczór to plan, który da się utrzymać.</li><li><strong>Dodaj dania do dni.</strong> Cibello proponuje posiłki na podstawie zapasów, terminów i tego, co Twój dom zwykle lubi. Każdą propozycję możesz przyjąć, zamienić lub usunąć.</li><li><strong>Sprawdź listę zakupów.</strong> Na liście lądują tylko składniki, których faktycznie brakuje. Dopisz to, co potrzebne poza planem, i podziel się listą z domownikami.</li><li><strong>Po kilku dniach spójrz na plan jeszcze raz.</strong> Coś zostało z wtorku? Zamień środową kolację na resztki i przesuń danie na czwartek.</li></ol>"""),
            ("Różnorodność, o którą nie musisz się starać", """<p>Kiedy planujesz z głowy, łatwo wpaść w pętlę tych samych czterech dań. Cibello dba o zmienność między potrawami i głównymi składnikami, żeby kurczak nie pojawiał się trzy dni z rzędu, a makaron nie wracał na obiad i kolację. Ty nadal decydujesz: jeśli w Twoim domu wtorek jest zawsze dniem naleśników, po prostu je wpisz.</p><table><thead><tr><th>Dzień</th><th>Rodzaj posiłku</th><th>Dlaczego to działa</th></tr></thead><tbody><tr><td>Poniedziałek</td><td>Danie z warzyw o krótkim terminie</td><td>Zużywasz najpierw to, co najszybciej się psuje</td></tr><tr><td>Środa</td><td>Sprawdzony rodzinny klasyk</td><td>Zero ryzyka w środku tygodnia</td></tr><tr><td>Czwartek</td><td>Resztki lub pudełko z zamrażarki</td><td>Krótszy wieczór, mniej gotowania</td></tr><tr><td>Sobota</td><td>Coś nowego z listy propozycji</td><td>Więcej czasu na próbowanie</td></tr></tbody></table><p>To tylko przykład szkieletu. Najlepszy jadłospis na tydzień to ten, który odpowiada Twojemu rytmowi, a nie odwrotnie.</p>"""),
            ("Jeden plan dla całego domu", """<p>Osoba, która planuje posiłki, nie musi trzymać wszystkiego w głowie. W Cibello domownicy widzą te same zapasy, ten sam plan i tę samą listę zakupów. Kto wraca ze sklepu, odhacza kupione rzeczy; kto zjadł ostatni jogurt, może to odnotować. Dzięki temu unikacie podwójnych zakupów i sytuacji, w której dwie osoby przynoszą do domu ten sam ser.</p><p>Wspólny dostęp działa w okresie próbnym, a później w planie płatnym. Niezależnie od tego, kto dodał danie do planu, każda osoba sprawdza składniki i informacje o alergenach na własną rękę, szczególnie jeśli ktoś w domu ma alergię lub nietolerancję.</p>"""),
            ("Plan to szkic, nie rozkład jazdy", """<p>Życie rzadko trzyma się planu i planer posiłków powinien to wytrzymać. Przesuwaj dania między dniami, wykreślaj to, na co nie masz ochoty, dodawaj własne ulubione przepisy. Resztki z sobotniej kolacji możesz zapisać w zapasach jako pudełko na lunch, a Cibello delikatnie przypomni, zanim jedzenie zacznie się psuć. Bez wyrzutów sumienia i bez liczenia kalorii pod presją.</p><p>Im częściej zapasy i lista zakupów są aktualne, tym trafniejsze będą propozycje na kolejny tydzień. Aplikacja jest wsparciem, decyzje należą do Ciebie. Jeśli szukasz pomysłu na dziś wieczór, zajrzyj do poradnika o <a href="/pl/przepisy-z-produktow/">przepisach z produktów, które masz w domu</a>, a przegląd wszystkich funkcji znajdziesz na <a href="/pl/">stronie głównej Cibello po polsku</a>. Porównanie z innymi aplikacjami do planowania posiłków jest dostępne po angielsku: <a href="/en/best-meal-planning-app/">best meal planning app</a>.</p>"""),
        ],
        faq=[
            ("Czy Cibello układa jadłospis na tydzień automatycznie?", "Cibello proponuje plan na podstawie Twoich zapasów, terminów i preferencji domu. Ty go przeglądasz, zmieniasz i zatwierdzasz, więc ostatnie słowo zawsze należy do Ciebie."),
            ("Czy plan uwzględnia to, co już mam w lodówce?", "Tak. Spis zapasów jest podstawą propozycji, a produkty z krótkim terminem mogą trafić do planu wcześniej, żeby się nie zmarnowały."),
            ("Czy mogę zmienić zaplanowany posiłek?", "Tak. Plan jest szkicem: przesuwasz dania między dniami, usuwasz je lub dodajesz własne przepisy w dowolnym momencie."),
            ("Czy domownicy widzą ten sam plan i listę zakupów?", "Tak. W okresie próbnym i w planie płatnym cały dom korzysta z tych samych zapasów, planu tygodnia i listy zakupów."),
        ],
    ),

    "/pl/przepisy-z-produktow/": dict(
        title="Przepisy z tego, co masz w lodówce | Cibello",
        desc="Co ugotować z tego, co masz w domu? Zeskanuj lodówkę i spiżarnię, a Cibello dopasuje ponad 9 000 przepisów do Twoich zapasów i pokaże, czego brakuje.",
        eyebrow="Co na obiad z tego, co mam",
        h1="Przepisy z produktów, które masz w domu",
        lead="Otwierasz lodówkę, patrzysz na pół brokuła, trzy jajka i resztkę fety i pytasz: co z tego ugotować? Cibello odwraca zwykłą kolejność: najpierw sprawdza, co masz, a dopiero potem proponuje przepisy. Pokazuje też, których składników brakuje, zanim zaczniesz gotować.",
        sections=[
            ("Co ugotować z tego, co mam w lodówce?", """<p>Większość aplikacji z przepisami zaczyna od przepisu. Wybierasz ładne zdjęcie, czytasz listę składników i odkrywasz, że połowy nie masz. Kończy się dodatkowym wyjściem do sklepu albo zamówieniem jedzenia, a brokuł zostaje w lodówce na kolejny dzień.</p><p>Cibello zaczyna od Twojej kuchni. Podstawą jest spis zapasów, który budujesz ze zdjęć, paragonów i kodów kreskowych. Na jego tle aplikacja przegląda ponad 9 000 przepisów i pokazuje na górze te, do których masz najwięcej składników. Zamiast szukać dania i sprawdzać, czy da się je zrobić, widzisz od razu, co realnie możesz ugotować dziś wieczorem.</p><p>To zmienia sposób myślenia o gotowaniu w tygodniu. Przepis przestaje być listą zakupów do zrobienia, a staje się sposobem na to, co już masz. Pół brokuła i trzy jajka to nie problem do rozwiązania, tylko punkt wyjścia.</p>"""),
            ("Od zdjęcia do spisu zapasów", """<p>Zrób zdjęcie otwartej lodówki, półki w spiżarni albo zamrażarki. Cibello rozpoznaje produkty i zapamiętuje, gdzie stoją, więc później wiesz, że ser jest na drugiej półce, a mrożony groszek w dolnej szufladzie. Po zakupach możesz zeskanować paragon, a pojedyncze opakowanie dodać po kodzie kreskowym.</p><p>Rozpoznawanie obrazu to nadal AI i zdarza mu się pomylić: nie zobaczy słoika schowanego z tyłu, źle odczyta datę albo pomyli jogurt naturalny z greckim. Dlatego każdy wynik przeglądasz przed zapisaniem i poprawiasz to, co się nie zgadza. Kilka sekund uwagi przy skanowaniu sprawia, że propozycje przepisów są później dużo trafniejsze.</p>"""),
            ("Ponad 9 000 przepisów posortowanych według Twojej kuchni", """<p>Każdy przepis w Cibello ma widoczną informację, jaka część składników jest już w domu. Danie, do którego masz wszystko, trafia na górę listy; to, do którego brakuje dwóch rzeczy, pokazuje dokładnie, czego. Nie musisz porównywać list składników z zawartością lodówki w głowie.</p><p>Kolejność nie zależy tylko od liczby składników. Aplikacja bierze pod uwagę, co wkrótce traci termin, i to, co Twój dom zwykle wybiera, a przy każdej propozycji wyjaśnia, dlaczego ją pokazuje: na przykład dlatego, że szpinak trzeba zużyć do jutra albo że podobne dania często u Was wracają. Z czasem, kiedy zapisujesz posiłki i poprawiasz zapasy, propozycje coraz lepiej pasują do Waszych zwyczajów.</p><p>Ważne: to nadal propozycje. Aplikacja nie wie, że masz dziś ochotę na coś ciepłego albo że wczoraj był już makaron. Ty przeglądasz listę i wybierasz; Cibello robi tylko tę żmudną część, czyli porównuje setki przepisów z tym, co stoi w Twojej lodówce.</p>"""),
            ("Szybkie pomysły na zwykły wieczór", """<p>W dzień powszedni rzadko wygrywa najbardziej wyszukany przepis. Wygrywa ten, który da się zrobić z tego, co jest, w rozsądnym czasie. Kilka typów dań, które niemal zawsze wychodzą z zawartości przeciętnej lodówki:</p><ul><li><strong>Makaron z tym, co zostało:</strong> warzywa, ser, resztka śmietanki lub pomidorów z puszki.</li><li><strong>Omlet, frittata lub jajecznica na bogato:</strong> ratunek dla pojedynczych warzyw i końcówek wędliny.</li><li><strong>Zupa krem:</strong> zmiękłe warzywa, cebula, bulion i blender.</li><li><strong>Zapiekanka lub danie jednogarnkowe z piekarnika:</strong> ziemniaki, kasza albo ryż, warzywa i to, co trzeba zużyć.</li><li><strong>Sałatka z kaszą lub ryżem:</strong> resztki z wczoraj plus coś świeżego i chrupiącego.</li><li><strong>Placki:</strong> z cukinii, ziemniaków, marchewki lub kalafiora.</li></ul><p>Kiedy zapasy są aktualne, Cibello podsuwa dokładnie takie dania na samej górze listy, bo to do nich masz najwięcej składników.</p>"""),
            ("Alergie, dieta i wartości odżywcze: filtry to wskazówka", """<p>W profilu możesz zapisać alergie, nietolerancje i sposób odżywiania, a przepisy będą do tego dopasowywane. Ważne zastrzeżenie: filtry przepisów i alergenów są pomocą w wyszukiwaniu, nie gwarancją. Skład produktów się zmienia, a przepis może zawierać składnik, którego nie spodziewasz się w danej potrawie. Zawsze czytaj etykiety i listę składników samodzielnie, zwłaszcza przy poważnej alergii lub gdy gotujesz dla kogoś innego.</p><p>Wartości odżywcze podawane przy przepisach to szacunki przydatne w planowaniu, nie porada dietetyczna. Cibello nie zastępuje lekarza ani dietetyka. Jeśli masz szczególne potrzeby zdrowotne, skonsultuj jadłospis ze specjalistą.</p>"""),
            ("Z przepisu na listę zakupów i do planu tygodnia", """<p>Kiedy wybierzesz danie, brakujące składniki możesz jednym ruchem dodać do listy zakupów, którą widzą wszyscy w domu. Celem nie jest kupowanie więcej, ale kupowanie tylko tego, czego naprawdę nie ma, i unikanie podwójnych zakupów. Ta sama lista działa też, gdy zaplanujesz kilka dni naprzód: jak to zrobić, opisujemy w poradniku o <a href="/pl/planer-posilkow/">planerze posiłków na tydzień</a>.</p><p>Resztki z większego gotowania możesz zapisać w zapasach jako pudełko na lunch. Wtedy są widoczne tak samo jak inne produkty, a Cibello przypomni o nich, zanim zaczną się psuć. Danie na dwa dni zamiast na jeden to często najprostsza odpowiedź na pytanie o jutrzejszy obiad.</p><p>Gotowanie z tego, co masz, to również najprostszy sposób, żeby mniej wyrzucać. Więcej o tym w tekście <a href="/pl/ograniczanie-marnowania-zywnosci/">jak ograniczyć marnowanie żywności w domu</a>. Przegląd wszystkich funkcji znajdziesz na <a href="/pl/">polskiej stronie Cibello</a>, a porównanie aplikacji z przepisami, w tym SuperCook i Samsung Food, po angielsku: <a href="/en/best-recipe-app/">best recipe app</a>.</p>"""),
        ],
        faq=[
            ("Czy muszę wpisywać wszystkie produkty ręcznie?", "Nie. Możesz zeskanować lodówkę, spiżarnię, paragon lub kod kreskowy, a Cibello rozpozna produkty. Wynik zawsze sprawdzasz i poprawiasz przed zapisaniem."),
            ("Czy Cibello podpowie, co ugotować z resztek?", "Tak. Gdy resztki i pudełka z jedzeniem są zapisane w zapasach, mogą być brane pod uwagę w propozycjach przepisów."),
            ("Co, jeśli brakuje mi jednego składnika?", "Cibello pokazuje przy każdym przepisie, których składników nie masz. Możesz dodać je do wspólnej listy zakupów albo wybrać inne danie z listy."),
            ("Czy Cibello uwzględnia alergie?", "Możesz zapisać alergie i preferencje żywieniowe, ale filtrowanie nie jest gwarancją. Zawsze czytaj etykiety i listę składników samodzielnie."),
        ],
    ),

    "/pl/ograniczanie-marnowania-zywnosci/": dict(
        title="Jak nie marnować jedzenia w domu | Cibello",
        desc="Skąd bierze się marnowanie żywności w domu i co pomaga: przegląd zapasów, gotowanie od tego, co trzeba zużyć, plan tygodnia i wspólna lista zakupów.",
        eyebrow="Mniej jedzenia w koszu",
        h1="Jak ograniczyć marnowanie żywności w domu",
        lead="Zwiędły szpinak, zapomniana śmietana na dnie lodówki, chleb, którego nikt nie zdążył zjeść. Marnowanie żywności rzadko wynika ze złej woli, prawie zawsze z braku przeglądu. Cibello pomaga zobaczyć, co masz, zużyć to na czas i kupować tylko to, czego brakuje.",
        sections=[
            ("Marnowanie żywności zaczyna się w domu", """<p>Marnowanie żywności to jedzenie, które można było zjeść, a które trafiło do kosza: resztki po obiedzie, warzywa, które zmiękły w szufladzie, produkty po terminie, których nikt nie sprawdził. W Europie największa część zmarnowanej żywności pochodzi nie ze sklepów ani restauracji, ale z gospodarstw domowych. To dobra wiadomość, bo oznacza, że najwięcej możesz zmienić we własnej kuchni, bez czekania na kogokolwiek.</p><p>Do kosza trafia przy tym nie tylko jedzenie, ale też pieniądze wydane w sklepie, czas spędzony na zakupach i woda oraz energia zużyte przy produkcji. Każde opakowanie, które udaje się zjeść zamiast wyrzucić, to realna oszczędność w domowym budżecie, bez zmiany diety i bez rezygnowania z czegokolwiek.</p><p>Nie chodzi o perfekcję ani o poczucie winy. Chodzi o kilka nawyków, które sprawiają, że jedzenie jest widoczne, a decyzje o tym, co ugotować, zapadają, zanim coś zacznie się psuć.</p>"""),
            ("Dlaczego jedzenie ląduje w koszu", """<p>Kiedy przyjrzysz się temu, co wyrzucasz, zwykle powtarza się kilka schematów:</p><ul><li><strong>Brak przeglądu.</strong> Nie wiesz, co jest z tyłu lodówki, więc kupujesz ponownie to, co już masz.</li><li><strong>Zakupy bez planu.</strong> Kupujesz na wszelki wypadek, a potem nie masz pomysłu, w czym to wykorzystać.</li><li><strong>Zapomniane resztki.</strong> Pudełko z niedzieli odkrywasz w czwartek.</li><li><strong>Niezrozumiane daty.</strong> Produkt po dacie „najlepiej spożyć przed” wyrzucasz odruchowo, choć często jest w porządku.</li><li><strong>Dwie osoby, jeden ser.</strong> W domu bez wspólnej listy zakupy się dublują.</li></ul><p>Każdy z tych punktów ma proste rozwiązanie, a większość z nich sprowadza się do jednego: wiedzieć, co się ma.</p>"""),
            ("Zobacz, co masz, zanim pójdziesz na zakupy", """<p>Spis zapasów to najprostsze narzędzie przeciw marnowaniu. W Cibello powstaje ze zdjęć lodówki, zamrażarki i spiżarni; aplikacja rozpoznaje produkty i zapamiętuje, gdzie stoją. Paragon po zakupach lub kod kreskowy uzupełniają listę. Ponieważ AI może źle odczytać nazwę lub datę, wynik zawsze sprawdzasz przed zapisaniem.</p><p>Największą różnicę robi zamrażarka i spiżarnia, bo to tam jedzenie znika z pola widzenia na najdłużej. Kiedy w spisie widać, że w zamrażarce leżą już dwie paczki mrożonego szpinaku, a w spiżarni trzy puszki ciecierzycy, po prostu ich nie kupujesz. Zamiast kolejnej wyprawy do sklepu, rzut oka na telefon.</p><p>Kiedy daty są w systemie, Cibello delikatnie przypomni, że coś warto zużyć w najbliższych dniach. Bez alarmów i bez zawstydzania. Przypomnienie to podpowiedź, a nie wyrok: zawsze powąchaj, obejrzyj i kieruj się informacją na opakowaniu, szczególnie przy jedzeniu dla dzieci lub osób z obniżoną odpornością.</p>"""),
            ("Gotuj od tego, co trzeba zużyć najpierw", """<p>Zamiast kupować komplet nowych składników do wybranego przepisu, odwróć kolejność: zacznij od tego, co masz. Cibello przegląda ponad 9 000 przepisów i pokazuje na górze te, do których masz najwięcej składników, a propozycje uwzględniają produkty z krótkim terminem. Kiedy szpinak ma dzień zapasu, danie ze szpinakiem pojawia się wysoko, z wyjaśnieniem dlaczego.</p><p>Brakujące składniki trafiają na listę zakupów, więc kupujesz tylko to, czego naprawdę nie ma. Więcej o tym podejściu w poradniku o <a href="/pl/przepisy-z-produktow/">przepisach z produktów, które masz w domu</a>.</p>"""),
            ("Planuj tydzień i kupuj tylko to, czego brakuje", """<p>Plan posiłków na kilka dni naprzód porządkuje zakupy i daje produktom z krótkim terminem miejsce na początku tygodnia. Nie musi być sztywny: kilka dań, miejsce na resztki i jeden luźny wieczór wystarczą. Jak go ułożyć, opisujemy w poradniku <a href="/pl/planer-posilkow/">planer posiłków na spokojniejszy tydzień</a>.</p><p>Wspólna lista zakupów domyka obieg. Domownicy widzą te same zapasy i tę samą listę, więc nikt nie kupuje drugiego masła, a osoba w sklepie wie, czego faktycznie nie ma w domu. Wspólny dostęp działa w okresie próbnym, a później w planie płatnym.</p><p>Warto też zmienić rytm zakupów. Jedne większe zakupy z listą i jedno, dwa krótkie uzupełnienia w tygodniu zwykle dają mniej strat niż codzienne wpadanie do sklepu „po drodze”, bo to właśnie wtedy kupujemy rzeczy, których nikt nie planował zjeść.</p>"""),
            ("Resztki, daty i mrożenie: kilka praktycznych zasad", """<p>Dwie daty na opakowaniach znaczą co innego i warto je rozróżniać:</p><table><thead><tr><th>Oznaczenie</th><th>Co oznacza</th><th>Co robić</th></tr></thead><tbody><tr><td>Należy spożyć do</td><td>Data dotyczy bezpieczeństwa, stosowana na produktach łatwo psujących się</td><td>Po tej dacie nie jedz</td></tr><tr><td>Najlepiej spożyć przed</td><td>Data dotyczy jakości, nie bezpieczeństwa</td><td>Oceń wygląd, zapach i smak; często produkt jest w porządku</td></tr></tbody></table><p>Resztki z obiadu zapisz w Cibello jako pudełko na lunch, wtedy są widoczne w zapasach razem z innymi produktami i łatwiej o nich pamiętać. Co nie zostanie zjedzone w dwa, trzy dni, zamroź od razu, zamiast czekać na decyzję. Mroź w porcjach na jeden posiłek i opisuj pudełka datą, bo nieopisany pojemnik na dnie zamrażarki to jedzenie, którego nikt już nie rozpozna. Chleb, zupy, sosy, gotowana kasza i ryż, a nawet miękkie banany na ciasto znoszą mrożenie bez problemu. I pamiętaj: aplikacja przypomina i proponuje, ale to Ty oceniasz, czy coś zjeść, zamrozić czy wyrzucić. Przegląd wszystkich funkcji znajdziesz na <a href="/pl/">polskiej stronie Cibello</a>.</p>"""),
        ],
        faq=[
            ("Czy aplikacja może zagwarantować, że jedzenie jest bezpieczne?", "Nie. Daty i wyniki rozpoznawania AI mogą być błędne. Zawsze sprawdzaj samodzielnie datę, sposób przechowywania, zapach, wygląd i informacje na opakowaniu."),
            ("Jak przepisy pomagają ograniczyć marnowanie żywności?", "Przepisy dobierane na podstawie zapasów ułatwiają zużycie tego, co już masz, zanim kupisz coś nowego. Cibello wyróżnia dania z produktów, którym kończy się termin."),
            ("Czy kilka osób może aktualizować te same zapasy?", "Tak. Funkcja domu jest przeznaczona do wspólnego przeglądu zapasów, planu i listy zakupów, w okresie próbnym i w planie płatnym."),
            ("Czy Cibello przypomni mi o produktach, których termin się kończy?", "Tak, gdy data jest zapisana w zapasach, aplikacja wysyła delikatne przypomnienie, zanim jedzenie zacznie się psuć. To podpowiedź, a nie ocena."),
        ],
    ),
}

# ---------------------------------------------------------------------------
# Landing-page prose for /pl/
# ---------------------------------------------------------------------------

HUBTEXT = """<section><h2>Co dzisiaj na obiad? Zacznij od lodówki</h2><p>Cibello to aplikacja, która zaczyna od Twojej kuchni, a nie od książki kucharskiej. Robisz zdjęcie lodówki, zamrażarki i spiżarni, a ona rozpoznaje produkty i zapamiętuje, gdzie stoją. Możesz też zeskanować paragon lub kod kreskowy. Wynik zawsze sprawdzasz przed zapisaniem, bo AI czasem się myli. Na tej podstawie aplikacja przegląda ponad 9 000 przepisów i pokazuje najpierw te, do których masz najwięcej składników. Jak to działa w praktyce, opisujemy w poradniku o <a href="/pl/przepisy-z-produktow/">przepisach z produktów, które masz w domu</a>.</p></section>
<section><h2>Plan na tydzień, który nie rozpada się we wtorek</h2><p>Jadłospis na tydzień to nie tabela do wypełnienia, tylko sposób na to, żeby decyzja o obiedzie zapadała wtedy, gdy masz na nią siłę. Cibello proponuje plan z uwzględnieniem zapasów, produktów z krótkim terminem i tego, co Wasz dom lubi, dbając o różnorodność dań i składników. Ty przesuwasz, zamieniasz i zatwierdzasz. Brakujące składniki trafiają na listę zakupów wspólną dla całego domu. Więcej w poradniku <a href="/pl/planer-posilkow/">planer posiłków na spokojniejszy tydzień</a>.</p></section>
<section><h2>Mniej jedzenia w koszu, bez wyrzutów sumienia</h2><p>Większość marnowanej żywności ginie nie dlatego, że ktoś jej nie chciał, tylko dlatego, że o niej zapomniał. Kiedy zapasy są widoczne, a daty zapisane, Cibello delikatnie przypomina, co warto zużyć w najbliższych dniach, i podsuwa przepisy, które to wykorzystają. Bez zawstydzania i bez liczenia kalorii pod presją. Przeczytaj, <a href="/pl/ograniczanie-marnowania-zywnosci/">jak ograniczyć marnowanie żywności w domu</a>.</p></section>
<section><h2>Uczciwie o tym, czym Cibello jest</h2><p>Cibello jest wsparciem, nie automatem do decyzji. Filtry alergenów są wskazówką, wartości odżywcze szacunkiem, a każdy skan i każda propozycja czekają na Twoje potwierdzenie. Aplikacja działa w 12 językach, dane są przechowywane w UE, a konto możesz usunąć bezpośrednio w aplikacji. Okres próbny trwa 14 dni i nie wymaga karty. Aplikacja jest przeznaczona dla osób pełnoletnich.</p></section>"""

# ---------------------------------------------------------------------------
# Shared pages: about, press, news
# ---------------------------------------------------------------------------

ABOUT = dict(
    title="O Cibello: aplikacja i firma, która za nią stoi | LandveX AB",
    desc="Cibello tworzy LandveX AB z Tyresö w Szwecji. Dlaczego aplikacja powstała, jak podchodzimy do AI, danych i marnowania żywności oraz jak się z nami skontaktować.",
    h1="O Cibello",
    lead="Cibello to szwedzka aplikacja kulinarna od LandveX AB. Powstała, żeby odpowiedzieć na pytanie zadawane niemal w każdym domu każdego dnia: co jemy? Na tej stronie wyjaśniamy, co chcemy osiągnąć, jak pracujemy z AI i danymi oraz jak się z nami skontaktować.",
    sections=[
        ("Dlaczego Cibello istnieje", """<p>Większość aplikacji z przepisami zaczyna od przepisów. My chcieliśmy zacząć od kuchni: od tego, co naprawdę jest w lodówce, zamrażarce i spiżarni, co wkrótce traci termin i co dom zwykle lubi. Dlatego sercem Cibello jest spis zapasów, Twój „Food Twin”, budowany ze zdjęć, paragonów i kodów kreskowych. Przepisy, plan tygodnia, lista zakupów i przypomnienia opierają się na tych samych danych. Celem jest mniej codziennego stresu i <a href="/pl/ograniczanie-marnowania-zywnosci/">mniej marnowanej żywności</a>, bez pouczania.</p>"""),
        ("Jak myślimy o AI", """<p>AI sprawia, że Cibello jest możliwe, ale czasem się myli. Skanowanie może źle odczytać produkt, pominąć coś z tyłu półki albo zgadnąć niewłaściwą datę. Dlatego zawsze przeglądasz wyniki przed zapisaniem, a propozycje są tylko propozycjami. Filtry przepisów i alergenów są wskazówką, nigdy gwarancją, a wartości odżywcze to szacunki do planowania, nie porada dietetyczna. Własne modele Cibello uczą się wyłącznie na Twoich poprawkach oraz, jeśli osobno wyrazisz na to zgodę, na oczyszczonych zdjęciach. Obie opcje są domyślnie wyłączone. Szczegóły w <a href="/pl/privacy/">polityce prywatności</a>.</p>"""),
        ("Twoje dane", """<p>Wszystko jest przechowywane w UE. Możesz przeglądać swoje dane w aplikacji i <a href="/pl/delete-account/">usunąć konto</a>, kiedy chcesz, bez kontaktu z pomocą techniczną. Nie sprzedajemy danych osobowych.</p>"""),
        ("Firma", """<p>Cibello jest rozwijane przez LandveX AB i należy do tej spółki: numer rejestrowy 559141-7042, Antennvägen 2, 135 48 Tyresö, Szwecja. Aplikacja jest dostępna na iOS i Androida w dwunastu językach i powstaje w Szwecji. Na razie jest przeznaczona dla osób, które ukończyły 18 lat, ponieważ warunki usługi AI, z której korzysta, wymagają pełnoletnich użytkowników. Okres próbny trwa 14 dni i nie wymaga karty.</p>"""),
        ("Kontakt", """<p>Pytania ogólne i współpraca: <a href="mailto:hello@cibello.app">hello@cibello.app</a>. Pomoc techniczna: <a href="mailto:support@cibello.app">support@cibello.app</a>. Prywatność i ochrona danych: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>. Zapytania prasowe kieruj na ten sam adres; zwykle odpowiadamy w ciągu kilku dni roboczych.</p><p>Obserwuj nas na <a href="https://www.instagram.com/cibelloapp/" rel="noopener">Instagramie</a>, <a href="https://www.tiktok.com/@cibello73" rel="noopener">TikToku</a> i <a href="https://www.facebook.com/profile.php?id=61593336222919" rel="noopener">Facebooku</a>.</p>"""),
    ],
)

PRESS = dict(
    title="Prasa i media: fakty, grafiki i kontakt | Cibello",
    desc="Materiały prasowe Cibello: krótki opis aplikacji, najważniejsze fakty, logo i grafiki do pobrania oraz kontakt dla mediów w LandveX AB.",
    eyebrow="Dla dziennikarzy i autorów",
    h1="Prasa i media",
    lead="Wszystko, czego potrzebujesz, żeby napisać o Cibello: krótki opis, fakty, grafiki i kontakt, który szybko odpowiada. Materiały z tej strony można swobodnie wykorzystywać w kontekście redakcyjnym.",
    sections=[
        ("Cibello w skrócie", """<p>Cibello to szwedzka aplikacja kulinarna, która fotografuje lodówkę i spiżarnię, prowadzi spis zapasów z miejscem i datami, proponuje przepisy z tego, co faktycznie jest w domu, planuje tydzień i dzieli listę zakupów z domownikami. Delikatnie przypomina, zanim jedzenie się zepsuje, i nigdy nie ocenia, co kto je. Dostępna na iOS i Androida w dwunastu językach, z danymi przechowywanymi w UE, rozwijana przez LandveX AB z Tyresö w Szwecji.</p><p><strong>Jednym zdaniem:</strong> Cibello to aplikacja, która widzi, co masz w domu, i odpowiada na pytanie „co jemy?”.</p>"""),
        ("Fakty", """<ul><li>Dostępna na iOS i Androida: <a href="https://apps.apple.com/app/id6807100747" rel="noopener">App Store</a> i <a href="https://play.google.com/store/apps/details?id=com.cibello.app" rel="noopener">Google Play</a>. Ograniczenie wiekowe 18+.</li><li>Okres próbny: 14 dni bez karty, następnie subskrypcja przez App Store lub Google Play.</li><li>Przepisy: ponad 9 000, dopasowywane do zapasów użytkownika.</li><li>Języki: szwedzki, angielski, niemiecki, francuski, hiszpański, włoski, niderlandzki, polski, duński, norweski, fiński, portugalski.</li><li>Dane: przechowywane w UE. Konto i dane można usunąć w aplikacji.</li><li>AI: skanowanie lodówki, spiżarni, paragonów i kodów kreskowych. Użytkownik zawsze sprawdza wynik. Własne modele Cibello uczą się wyłącznie na poprawkach użytkowników oraz, za osobną zgodą, na oczyszczonych zdjęciach.</li><li>Ceny: bezpłatny okres próbny, potem plan płatny z funkcjami dla domu. Aktualne ceny w App Store i Google Play.</li><li>Firma: LandveX AB, nr rej. 559141-7042, Antennvägen 2, 135 48 Tyresö, Szwecja.</li></ul>"""),
        ("Logo i grafiki", """<ul><li><a href="/img/icon-512.png">Ikona aplikacji, PNG 512×512</a></li><li><a href="/img/og-pl.png">Grafika do udostępniania, PNG 1200×630 (polska)</a></li><li><a href="/img/og.png">Grafika do udostępniania, PNG 1200×630 (szwedzka)</a></li><li><a href="/favicon.svg">Symbol, SVG</a></li></ul><p>Zrzuty ekranu z aplikacji udostępniamy na życzenie. Grafiki można swobodnie wykorzystywać w kontekście redakcyjnym z podaniem źródła: Cibello.</p>"""),
        ("Kontakt dla mediów", """<p><a href="mailto:hello@cibello.app?subject=Zapytanie%20prasowe">hello@cibello.app</a>. Na zapytania prasowe odpowiadamy zwykle w ciągu jednego dnia roboczego. Założyciel jest dostępny do rozmów o marnowaniu żywności w domach, o AI w codziennym życiu i o tym, dlaczego pytanie „co jemy?” warto rozwiązać.</p><p>Więcej o firmie: <a href="/pl/about/">O Cibello</a>.</p>"""),
    ],
)

NEWS = dict(
    title="Co nowego w Cibello: aktualizacje i nowe poradniki",
    desc="Nowe poradniki, narzędzia i aktualizacje na cibello.app, z datami. Subskrybuj przez RSS.",
    h1="Co nowego w Cibello",
    lead="Co pojawiło się na stronie i w aplikacji, od najnowszych. Dostępny jest kanał RSS.",
    rss_label="Kanał RSS",
    entries=[
        ("2026-09-04", "Nowy poradnik: marnowanie żywności w Szwecji w liczbach", "/matsvinn-statistik/",
         "Oficjalne dane szwedzkiej Agencji Ochrony Środowiska i Szwedzkiego Urzędu ds. Żywności na jednej stronie (po szwedzku): 880 000 ton zmarnowanej żywności, 16 kg jadalnego jedzenia na osobę w gospodarstwach domowych i 1 330 koron na osobę rocznie. Przy każdej liczbie podane jest źródło."),
        ("2026-09-04", "Trzy nowe poradniki po angielsku i dwa porównania", "/en/#guider",
         "Co zjeść dziś wieczorem, planer posiłków z AI i aplikacja do spiżarni, po angielsku. Do tego uczciwe porównania aplikacji do planowania posiłków i aplikacji z przepisami z Mealime, Samsung Food, Plan to Eat, Paprika i SuperCook."),
        ("2026-09-04", "Pełne strony główne w dwunastu językach", "/pl/",
         "Każdy język, w tym polski, ma teraz kompletną stronę główną zamiast krótkiej strony tekstowej. Nic nie jest już tłumaczone w przeglądarce."),
        ("2026-08-30", "Polityka prywatności i regulamin w wersji 2.0", "/pl/privacy/",
         "Zaktualizowane teksty obejmują analizę Gemini, dobrowolne trenowanie Cibello AI, 14-dniowy okres próbny bez karty i ograniczenie wiekowe 18+. Dostępne jest polskie tłumaczenie; w razie rozbieżności obowiązuje wersja szwedzka."),
    ],
)

# ---------------------------------------------------------------------------
# Legal: faithful translations of integritet.html, villkor.html, delete-account.html (v2.0)
# ---------------------------------------------------------------------------

PRIVACY = dict(
    title="Polityka prywatności – Cibello",
    desc="Jak Cibello przetwarza dane osobowe, zdjęcia, analizę Gemini i dobrowolne trenowanie Cibello AI. Polskie tłumaczenie szwedzkiej polityki, wersja 2.0.",
    h1="Polityka prywatności",
    notice="<strong>W skrócie:</strong> Do dzisiejszej analizy obrazu wykorzystywana jest zewnętrzna usługa AI. Własny model AI Cibello może być trenowany wyłącznie na własnych poprawkach użytkownika i oczyszczonych zdjęciach, po osobnym, dobrowolnym i aktywnym wyborze podczas wprowadzenia do aplikacji. Odpowiedzi zewnętrznej AI nigdy nie służą jako wzorzec treningowy.",
    body="""<h2>1. Administrator danych</h2>
<p>LandveX AB, nr rej. 559141-7042, Antennvägen 2, 135 48 Tyresö, Szwecja, jest administratorem danych osobowych w Cibello. Pytania dotyczące prywatności prosimy kierować na adres <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>

<h2>2. Dane i cele</h2>
<ul>
<li><strong>Konto:</strong> adres e-mail, wyświetlana nazwa, tożsamość uwierzytelniająca i dzienniki bezpieczeństwa, aby utworzyć i chronić konto.</li>
<li><strong>Dane o żywności i gospodarstwie domowym:</strong> zapasy, przepisy, preferencje, alergie i własne poprawki użytkownika, na potrzeby funkcji aplikacji.</li>
<li><strong>Zdjęcia:</strong> zdjęcia, które użytkownik decyduje się zeskanować w celu rozpoznania produktów spożywczych lub paragonów.</li>
<li><strong>Płatności:</strong> status subskrypcji i odniesienia do transakcji. Dane karty i dane płatnicze obsługuje Apple App Store lub Google Play.</li>
<li><strong>Dane techniczne:</strong> błędy, wydajność i analityka produktowa wyłącznie zgodnie z wyborem użytkownika i niezbędnymi potrzebami bezpieczeństwa.</li>
<li><strong>Ochrona przed nadużywaniem bezpłatnego okresu próbnego:</strong> kluczowany, pseudonimowy odcisk HMAC znormalizowanego adresu e-mail, przechowywany najwyżej pięć lat. Nie można go użyć do logowania ani do kontaktu i nie zawiera adresu w postaci jawnej, identyfikatora użytkownika ani tożsamości Firebase. Jego jedynym celem jest zapobieganie wielokrotnym bezpłatnym okresom próbnym po usunięciu konta i ponownej rejestracji.</li>
</ul>

<h2>3. Gemini w środowisku produkcyjnym</h2>
<p>Wybrane zdjęcia i niezbędna instrukcja są przesyłane do interfejsu Google Gemini API w celu wygenerowania wyniku wyświetlanego w aplikacji. Cibello korzysta z płatnej usługi w obrębie EOG. Zgodnie z warunkami Google dane w płatnej usłudze nie są wykorzystywane do ulepszania produktów Google, ale może występować ograniczone logowanie w celach bezpieczeństwa i zwalczania nadużyć, o ile nie obowiązuje szczególny tryb zerowego przechowywania. Cibello nie obiecuje zatem zerowego przechowywania poza własnym środowiskiem bez technicznego potwierdzenia od dostawcy.</p>
<p>Wyniki Gemini to automatyczne szacunki. Użytkownik powinien sprawdzić zawartość, alergeny, daty i ilości, zanim skorzysta z tych informacji.</p>

<h2>4. Własny model AI Cibello – osobne i dobrowolne trenowanie</h2>
<p>Cibello rozwija własny model AI. Proces trenowania jest technicznie i prawnie oddzielony od zewnętrznej usługi AI, która dostarcza użytkownikowi dzisiejsze wyniki:</p>
<ul>
<li>Odpowiedzi, rozumowanie ani propozycje Gemini nigdy nie są eksportowane jako etykiety treningowe ani wzorzec treningowy do własnego modelu AI Cibello.</li>
<li><strong>Anonimowe ulepszanie AI</strong> pozwala wykorzystać wyraźną poprawkę użytkownika lub ręcznie potwierdzoną odpowiedź bez zdjęcia.</li>
<li><strong>Trenowanie na zdjęciach</strong> pozwala powiązać oczyszczoną kopię zdjęcia użytkownika z jego własną poprawką. Przed zapisaniem metadane są usuwane, a rozmiar zdjęcia ograniczany.</li>
<li>Wprowadzenie do aplikacji pokazuje jeden wspólny, wyraźny wybór dla tych dwóch części tego samego celu treningowego. Wybór nie jest domyślnie zaznaczony, a aplikacja działa także wtedy, gdy użytkownik nie wyrazi zgody.</li>
<li>Zgodę można wycofać przyciskiem w Profilu. Wówczas dalsze wykorzystanie zostaje wstrzymane, aktywny zbiór treningowy należący do aplikacji jest czyszczony, a odniesienia do zdjęć usuwane. Już wytworzonych, zagregowanych parametrów modelu zwykle nie da się powiązać z konkretną osobą.</li>
<li>Cibello AI nie wpływa na wynik produkcyjny, dopóki nie zostaną osiągnięte udokumentowane progi jakościowe (benchmark) i progi bezpieczeństwa.</li>
</ul>

<h2>5. Podstawa prawna</h2>
<p>Konto i podstawowe funkcje są przetwarzane w celu wykonania umowy. Logowanie zdarzeń bezpieczeństwa oraz ograniczony odcisk chroniący przed wielokrotnymi okresami próbnymi są przetwarzane na podstawie uzasadnionego interesu. Obowiązki prawne mogą wymagać innego, ograniczonego przetwarzania. Dobrowolna analityka produktowa, ulepszanie AI i trenowanie na zdjęciach opierają się na osobnych zgodach, które można wycofać.</p>

<h2>6. Przechowywanie i odbiorcy</h2>
<p>Dane są przechowywane tak długo, jak wymaga tego usługa, bezpieczeństwo, przepisy prawa i udokumentowana retencja kopii zapasowych. Dostawcy mogą obejmować AWS (hosting i przechowywanie), Firebase (uwierzytelnianie), Google Gemini (wybrana analiza AI) oraz Apple lub Google (płatności). Cibello nie sprzedaje danych osobowych. Odcisk chroniący okres próbny jest automatycznie usuwany najpóźniej pięć lat po rozpoczęciu okresu próbnego.</p>

<h2>7. Twoje prawa</h2>
<p>Możesz żądać dostępu do danych, ich sprostowania, przeniesienia, ograniczenia przetwarzania lub usunięcia oraz wnieść sprzeciw wobec określonego przetwarzania. Zgody zmieniasz w Profilu. Konto można usunąć bezpośrednio w aplikacji lub przez <a href="/pl/delete-account/">stronę usuwania konta</a>. Możesz również skontaktować się ze szwedzkim organem ochrony danych (Integritetsskyddsmyndigheten).</p>

<h2>8. Wiek</h2>
<p>Cibello jest na razie przeznaczone dla osób, które ukończyły 18 lat, ponieważ warunki wykorzystywanej usługi Gemini API wymagają pełnoletnich użytkowników. Wymóg wiekowy zostanie ponownie rozważony, jeśli zmieni się techniczne rozwiązanie dostawcy.</p>

<h2>9. Zmiany</h2>
<p>Istotne zmiany otrzymują numer wersji i wymagają ponownej akceptacji w aplikacji przed dalszym korzystaniem.</p>""",
)

TERMS = dict(
    title="Regulamin – Cibello",
    desc="Regulamin korzystania z Cibello: konto, ograniczenie wiekowe, subskrypcje i 14-dniowy okres próbny, analiza AI i bezpieczne korzystanie. Polskie tłumaczenie szwedzkiego regulaminu, wersja 2.0.",
    h1="Regulamin",
    body="""<h2>1. Umowa i ograniczenie wiekowe</h2>
<p>Niniejszy regulamin obowiązuje między użytkownikiem a LandveX AB, nr rej. 559141-7042. Cibello jest na razie przeznaczone wyłącznie dla osób, które ukończyły 18 lat. Tworząc konto, użytkownik potwierdza swój wiek oraz akceptuje regulamin i <a href="/pl/privacy/">politykę prywatności</a>.</p>

<h2>2. Usługa</h2>
<p>Cibello pomaga użytkownikowi organizować żywność, interpretować wybrane zdjęcia i paragony oraz otrzymywać propozycje przepisów i posiłków. Wyniki mogą być niepełne lub błędne i powinny zostać sprawdzone przez użytkownika.</p>

<h2>3. Brak porad medycznych i profesjonalnych</h2>
<p>Cibello dostarcza inspiracje i informacje ogólne, a nie porady medyczne, dietetyczne, alergologiczne ani inne porady profesjonalne. Użytkownik odpowiada za sprawdzenie składników, alergenów, wielkości porcji, terminu przydatności, sposobu przygotowania i bezpieczeństwa żywności. W przypadku choroby, ciąży, ciężkiej alergii lub szczególnych potrzeb należy skonsultować się z wykwalifikowanym personelem medycznym.</p>

<h2>4. AI i kontrola człowieka</h2>
<p>Do bieżącej analizy produkcyjnej wykorzystywana jest zewnętrzna usługa AI. Własny model AI Cibello jest rozwijany równolegle, ale może być trenowany wyłącznie zgodnie ze zgodą i ograniczeniami opisanymi w <a href="/pl/privacy/">polityce prywatności</a>. Odpowiedzi zewnętrznej AI nigdy nie służą jako wzorzec treningowy. Użytkownik musi zawsze mieć możliwość poprawienia automatycznych wyników.</p>

<h2>5. Dobrowolne zgody na trenowanie</h2>
<p>Dostęp do podstawowych funkcji Cibello nie może być uzależniony od zgody na ulepszanie AI ani trenowanie na zdjęciach. Wybór jest domyślnie wyłączony, oddzielony od akceptacji regulaminu i można go zmienić w Profilu.</p>

<h2>6. Konto i bezpieczeństwo</h2>
<p>Użytkownik powinien podawać prawidłowe dane, chronić swoje dane logowania i informować Cibello o podejrzeniu nadużycia. Konto można usunąć w Profilu lub przez <a href="/pl/delete-account/">procedurę na stronie internetowej</a>.</p>

<h2>7. Subskrypcje i płatności</h2>
<p>Cyfrowe subskrypcje w aplikacji mobilnej są kupowane i zarządzane przez Apple App Store lub Google Play. Sterowany po stronie serwera 14-dniowy okres próbny Cibello bez karty przysługuje jeden raz na tożsamość e-mail w okresie pięciu lat. Usunięte konto można założyć ponownie, ale nie daje to automatycznie nowego bezpłatnego okresu próbnego. Cena, okres, automatyczne odnawianie i sposób rezygnacji są wyświetlane przez odpowiedni sklep przed zakupem. Zwroty są rozpatrywane zgodnie z zasadami sklepu i bezwzględnie obowiązującymi przepisami prawa konsumenckiego.</p>

<h2>8. Dozwolone korzystanie</h2>
<p>Usługi nie można wykorzystywać do treści niezgodnych z prawem, naruszeń, nękania, zautomatyzowanego przeciążania, obchodzenia zabezpieczeń ani prób pozyskania danych innych użytkowników. Cibello może ograniczyć konta w przypadku zagrożenia bezpieczeństwa lub istotnego naruszenia umowy.</p>

<h2>9. Dostępność i zmiany</h2>
<p>Usługa jest stale rozwijana i może być tymczasowo niedostępna. Funkcje mogą ulegać zmianom ze względów bezpieczeństwa, prawnych, jakościowych lub technicznych. Istotne zmiany regulaminu otrzymują numer wersji i wymagają ponownej akceptacji.</p>

<h2>10. Odpowiedzialność i przepisy bezwzględnie obowiązujące</h2>
<p>LandveX AB odpowiada zgodnie z mającymi zastosowanie bezwzględnie obowiązującymi przepisami prawa. Nic w regulaminie nie ogranicza praw, których nie można zgodnie z prawem wyłączyć umową. Stosuje się prawo szwedzkie, a konsument może również powołać się na bezwzględnie obowiązujące przepisy i właściwy sąd w swoim kraju zamieszkania.</p>

<h2>11. Kontakt</h2>
<p>Pomoc techniczna: <a href="mailto:support@cibello.app">support@cibello.app</a>. Prywatność: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>""",
)

DELETE = dict(
    title="Usuwanie konta i danych – Cibello",
    desc="Jak usunąć konto Cibello i powiązane z nim dane osobowe bezpośrednio w aplikacji, a także co zrobić, jeśli nie możesz otworzyć aplikacji.",
    h1="Usuń konto i dane",
    body="""<h2>Bezpośrednio w aplikacji</h2>
<ol>
<li>Zaloguj się do Cibello.</li>
<li>Otwórz <strong>Profil</strong>.</li>
<li>Wybierz <strong>Usuń konto</strong> i potwierdź.</li>
</ol>
<p>Konto, tożsamość Firebase, aktywne zdjęcia i osobiste dane aplikacji zostają usunięte. Odniesienia do transakcji finansowych mogą zostać spseudonimizowane i zachowane, gdy wymaga tego prawo. Kopie zapasowe są usuwane rotacyjnie zgodnie z udokumentowaną retencją.</p>

<h2>Jeśli nie możesz otworzyć aplikacji</h2>
<p>Wyślij prośbę z adresu e-mail zarejestrowanego na koncie na adres <a href="mailto:privacy@cibello.app?subject=Usu%C5%84%20moje%20konto%20Cibello">privacy@cibello.app</a>. Napisz „Usuń moje konto Cibello”. Przed usunięciem weryfikujemy, że masz kontrolę nad tym adresem.</p>

<h2>Dane treningowe</h2>
<p>Przy usunięciu konta poprawki użytkownika i odniesienia do zdjęć są usuwane z aktywnego zbioru treningowego. Odpowiedzi Gemini nigdy nie były eksportowane jako wzorzec treningowy Cibello AI. Już zagregowanych parametrów modelu zwykle nie da się powiązać z konkretną osobą.</p>""",
)

# ---------------------------------------------------------------------------
# UI strings
# ---------------------------------------------------------------------------

UI = dict(
    faq_title="Najczęstsze pytania",
    privacy_nav="Polityka prywatności",
    terms_nav="Regulamin",
    delete_nav="Usuń konto",
    legal_meta="Cibello · wersja 2.0 · obowiązuje od 30 sierpnia 2026 · tłumaczenie na polski",
    translation_label="O tym tłumaczeniu:",
    translation_note='To jest polskie tłumaczenie szwedzkiego oryginału (<a href="{sv}" lang="sv">oryginał</a>). W razie rozbieżności obowiązuje wersja szwedzka.',
)
