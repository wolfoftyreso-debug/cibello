"""Contenu français, phase 2, fichier B. Structure : voir _schema_extra.py.
Familles : weekend-dinners, budget-food, eu-food-waste-stats, ai-meal-planner, pantry-app, app-comparison, recipe-app-comparison.
"""

LANG = "fr"

CAPTION_CMP = "D’après les fiches App Store et Google Play des applications, leurs sites et les tests publiés, septembre 2026. Les fonctionnalités évoluent, vérifiez avant de choisir."

GUIDES2 = {
    # -----------------------------------------------------------------------
    "weekend-dinners": dict(
        slug="/fr/idees-repas-week-end/",
        label="Repas du week-end",
        title="Idées repas week-end : du vendredi au dimanche | Cibello",
        desc="Idées de repas pour le week-end : un vendredi soir sans stress, un samedi simple mais soigné et un dimanche mijoté qui remplit les boîtes-repas de la semaine.",
        eyebrow="Cuisiner le week-end",
        h1="Idées de repas pour le week-end : vendredi détendu, samedi soigné, dimanche mijoté",
        lead="Le week-end n’a pas les mêmes règles que la semaine&nbsp;: plus de temps, souvent des invités et l’envie de cuisiner avec un peu plus de soin. Voici des idées de repas pour le vendredi, le samedi et le dimanche, et une façon de laisser la cuisine du week-end donner de l’avance à la semaine qui suit.",
        sections=[
            (
                "Vendredi soir : convivial et sans stress",
                """<p>Le vendredi, personne n’a envie d’une recette en douze étapes. Ce qui marche, ce sont les plats où chacun compose son assiette et où la table reste le centre de la soirée.</p><ul><li><strong>Tacos ou fajitas</strong>&nbsp;: chacun garnit le sien, les enfants comme les invités s’y retrouvent.</li><li><strong>Pizza maison</strong>&nbsp;: préparez la pâte le matin, ou partez d’une pâte toute prête et concentrez-vous sur la garniture.</li><li><strong>Burgers et pommes de terre au four</strong>&nbsp;: simple, généreux, prêt en quarante minutes.</li><li><strong>Pâtes aux crevettes, citron et ail</strong>&nbsp;: vingt minutes de préparation pour un air de fête.</li><li><strong>Soirée bowls</strong>&nbsp;: riz, saumon ou tofu, avocat, oignon rouge mariné, et ce qui reste dans le bac à légumes.</li><li><strong>Planche apéro dînatoire</strong>&nbsp;: fromages, charcuterie, crudités, houmous et un bon pain. Rien à cuire, tout à partager.</li><li><strong>Raclette ou tartiflette</strong> dès que les soirées se rafraîchissent.</li></ul>""",
            ),
            (
                "Samedi : un plat soigné sans être compliqué",
                """<p>Un repas un peu plus élégant n’a pas besoin d’être difficile. Choisissez un produit qui tient le rôle principal et gardez les accompagnements simples&nbsp;: une purée, des légumes rôtis, une salade bien assaisonnée.</p><ul><li><strong>Poulet rôti aux herbes</strong> avec pommes de terre et gousses d’ail en chemise.</li><li><strong>Saumon au four, aneth et citron</strong>, servi avec des légumes rôtis.</li><li><strong>Cuisses de poulet rôties aux légumes racines et au thym</strong>, tout sur une seule plaque.</li><li><strong>Soupe de poisson au safran</strong> avec croûtons et rouille.</li><li><strong>Risotto aux champignons ou aux asperges</strong>, selon la saison.</li><li><strong>Pavé de bœuf, sauce au poivre et pommes grenailles</strong>.</li><li><strong>Lasagnes végétariennes aux épinards et à la ricotta</strong>.</li><li><strong>Table de tapas</strong> composée de petites choses déjà présentes dans le frigo et les placards.</li></ul><p>Vous recevez&nbsp;? Choisissez un plat que vous avez déjà cuisiné et qui se prépare en avance, puis consacrez le temps gagné aux accompagnements et au dessert. Le stress vient rarement du plat principal, plutôt de la nouveauté testée devant des invités.</p>""",
            ),
            (
                "Dimanche : le mijoté qui remplit les boîtes-repas du lundi",
                """<p>Le dimanche est le jour des plats qui prennent leur temps. Ils demandent peu d’attention une fois lancés et se réchauffent encore mieux le lendemain.</p><ul><li><strong>Bœuf bourguignon</strong> ou <strong>pot-au-feu</strong>.</li><li><strong>Blanquette de veau</strong> avec du riz.</li><li><strong>Curry de poulet</strong> en grande quantité.</li><li><strong>Chili con ou sin carne</strong>.</li><li><strong>Lasagnes ou gratin de pâtes</strong> dans deux plats plutôt qu’un.</li><li><strong>Sauce bolognaise</strong>&nbsp;: une moitié pour les pâtes du soir, l’autre pour les tacos de vendredi.</li></ul><p>Cuisinez en double, refroidissez rapidement et répartissez dans des boîtes entre le réfrigérateur et le congélateur. Dans Cibello, les boîtes-repas peuvent figurer dans l’inventaire, si bien qu’elles ne finissent pas oubliées au fond du frigo.</p>""",
            ),
            (
                "Partir de ce qui est déjà là",
                """<p>Les meilleures idées de repas du week-end commencent souvent par un coup d’œil dans le frigo. La crème dont la date approche devient la sauce du dimanche, le reste de poulet rôti se glisse dans un risotto, le demi-chou devient une salade croquante pour accompagner les burgers. Cibello photographie le réfrigérateur, le congélateur et les placards, reconnaît les produits et classe plus de 9&nbsp;000 recettes selon la part des ingrédients déjà chez vous. Chaque suggestion vient avec une explication&nbsp;: parce que tel produit doit être utilisé bientôt, parce que votre foyer choisit souvent ce genre de plat, ou parce que presque tout est déjà là. Le guide <a href="/fr/recettes-avec-ingredients/">recettes avec les ingrédients déjà chez vous</a> détaille cette façon de faire.</p>""",
            ),
            (
                "Planifier le week-end dès le milieu de semaine",
                """<p>Les repas du week-end demandent souvent un petit extra&nbsp;: un morceau de viande, un fromage, un bon pain. Si vous placez le vendredi, le samedi et le dimanche dans le <a href="/fr/planificateur-repas/">planificateur de repas</a> dès le mercredi, ce qui manque rejoint la liste de courses partagée et ce qui est déjà à la maison est utilisé en premier. Celui qui passe au marché samedi matin voit exactement ce qu’il reste à acheter. Vous relisez la proposition, déplacez un plat, en remplacez un autre&nbsp;: le menu reste un brouillon jusqu’à ce que vous décidiez de le garder.</p>""",
            ),
            (
                "Le week-end, allié contre le gaspillage",
                """<p>Le samedi et le dimanche sont les jours où l’on a le temps de cuisiner ce qui n’a pas été mangé pendant la semaine&nbsp;: les légumes fatigués partent dans une soupe ou un gratin, le pain rassis devient pain perdu ou chapelure, les restes de fromage finissent dans une quiche. C’est une manière concrète de <a href="/fr/reduire-gaspillage-alimentaire/">réduire le gaspillage alimentaire</a> sans changer ses habitudes. Cibello envoie un rappel discret quand un produit approche de sa date, sans jamais culpabiliser, et propose des recettes qui l’utilisent.</p>""",
            ),
        ],
        faq=[
            ("Que manger le vendredi soir sans se compliquer la vie ?", "Tacos, pizza maison, burgers, pâtes aux crevettes, bowls ou planche apéro dînatoire conviennent aux enfants comme aux invités et prennent moins de quarante minutes."),
            ("Qu’est-ce qu’un repas simple mais soigné pour le samedi ?", "Laissez un produit tenir le rôle principal : poulet rôti, saumon au four, cuisses de poulet aux légumes racines, risotto, soupe de poisson ou pavé de bœuf. Gardez les accompagnements simples."),
            ("Comment faire en sorte que la cuisine du week-end aide la semaine ?", "Cuisinez le double du mijoté du dimanche, congelez des boîtes-repas et planifiez le week-end dans le menu de la semaine pour que les courses tiennent dans une seule liste."),
            ("Cibello aide-t-il à choisir un repas pour des invités ?", "L’application propose des recettes classées selon ce que vous avez déjà chez vous et explique chaque suggestion. Vous choisissez, vous relisez, et ce qui manque rejoint la liste de courses."),
        ],
    ),
    # -----------------------------------------------------------------------
    "budget-food": dict(
        slug="/fr/manger-pas-cher/",
        label="Manger pas cher",
        title="Manger pas cher toute la semaine sans se lasser | Cibello",
        desc="Manger pas cher sans manger triste : un menu de la semaine économique, des courses limitées à ce qui manque et des produits utilisés jusqu’au bout. Exemple de menu inclus.",
        eyebrow="Budget et cuisine",
        h1="Manger pas cher toute la semaine : planifier, acheter moins, utiliser ce que vous avez",
        lead="Le repas le moins cher est celui que vous avez déjà acheté. La plupart des foyers jettent chaque année une quantité surprenante de nourriture, et une bonne partie vient d’achats en double et de produits oubliés. Voici une méthode concrète pour manger pas cher qui repose sur la visibilité de votre cuisine, pas sur le même plat tous les soirs.",
        sections=[
            (
                "Pourquoi la note grimpe",
                """<ul><li><strong>Les achats impulsifs</strong> quand le dîner n’est pas décidé avant d’entrer dans le magasin.</li><li><strong>Les doublons</strong>&nbsp;: un troisième pot de moutarde, un deuxième paquet de riz, parce que personne ne savait ce qu’il y avait dans le placard.</li><li><strong>Le gaspillage</strong>&nbsp;: légumes, produits laitiers et restes qui attendent trop longtemps.</li><li><strong>Des protéines coûteuses tous les jours</strong> au lieu d’une alternance entre viande, poisson, œufs et légumineuses.</li><li><strong>La livraison</strong> les soirs où l’énergie manque et où rien n’était prévu.</li></ul><p>Ces cinq causes ont le même remède&nbsp;: savoir ce que vous avez, décider à l’avance et faire les courses avec une liste.</p>""",
            ),
            (
                "Un menu de la semaine économique qui part du placard",
                """<p>Le placard est la base d’une cuisine pas chère&nbsp;: pâtes, riz, boulgour, lentilles, haricots, tomates concassées, flocons d’avoine, œufs et légumes surgelés. Avec cette réserve, il reste relativement peu de produits frais à acheter. Un <a href="/fr/planificateur-repas/">menu de la semaine</a> économique peut ressembler à ceci&nbsp;:</p><div class="table-wrap"><table class="cmp"><caption>Exemple de semaine économique. Les quantités et les plats s’adaptent à votre foyer et à la saison.</caption><thead><tr><th scope="col">Jour</th><th scope="col">Plat</th><th scope="col">Ce qui rend le plat économique</th></tr></thead><tbody><tr><th scope="row">Lundi</th><td>Soupe de lentilles corail et pain</td><td>Lentilles sèches, carottes, épices du placard</td></tr><tr><th scope="row">Mardi</th><td>Pâtes à la sauce tomate et haricots blancs</td><td>Tomates concassées, haricots en conserve</td></tr><tr><th scope="row">Mercredi</th><td>Omelette aux restes de légumes</td><td>Œufs, tout ce qui doit être utilisé</td></tr><tr><th scope="row">Jeudi</th><td>Curry de poulet et riz, en double quantité</td><td>Hauts de cuisse, lait de coco, légumes surgelés</td></tr><tr><th scope="row">Vendredi</th><td>Tacos à la viande hachée ou aux haricots</td><td>Moitié viande, moitié haricots</td></tr><tr><th scope="row">Samedi</th><td>Restes&nbsp;: curry en boîte-repas ou wraps</td><td>Aucun nouvel achat</td></tr><tr><th scope="row">Dimanche</th><td>Plaque au four de saucisses, pommes de terre et légumes racines</td><td>Légumes racines de saison</td></tr></tbody></table></div>""",
            ),
            (
                "N’acheter que ce qui manque",
                """<p>La plus grosse économie consiste à arrêter d’acheter ce que vous avez déjà. Une fois l’inventaire enregistré dans Cibello, chaque plat prévu est comparé à ce qui se trouve à la maison, et seule la différence rejoint la liste de courses partagée du foyer. Après les courses, une photo du ticket de caisse met l’inventaire à jour. C’est un cycle simple&nbsp;: planifier, acheter la liste, cuisiner, recommencer. La personne qui fait les courses voit la même liste que celle qui a planifié, et le troisième pot de moutarde ne rentre plus à la maison.</p>""",
            ),
            (
                "Varier les protéines pour alléger la note",
                """<p>Le poste protéines pèse lourd dans un panier. Il n’est pas nécessaire de le supprimer, seulement de l’alterner. Deux ou trois repas par semaine autour des œufs, des lentilles, des pois chiches ou des haricots changent déjà beaucoup la note, et ce sont des plats que l’on aime pour eux-mêmes&nbsp;: dahl, chili, salade de pois chiches, omelette garnie. Pour la viande, les morceaux à mijoter et les hauts de cuisse de poulet reviennent moins cher que les pièces nobles et supportent très bien la cuisson longue du dimanche. Les sardines et le maquereau en conserve font un dîner en dix minutes avec des pâtes ou des pommes de terre. Les valeurs nutritionnelles affichées dans l’application sont des estimations, une aide pour équilibrer la semaine, pas un conseil médical.</p>""",
            ),
            (
                "Tout utiliser : restes, dates courtes et congélateur",
                """<p>Les plats qui utilisent des produits à date courte se placent en début de semaine, et les restes sont prévus comme boîtes-repas ou comme dîner du lendemain. Cibello signale les produits qui approchent de leur date et propose des recettes qui les mettent à profit, avec une explication à chaque fois. Le congélateur est le second placard du foyer&nbsp;: la moitié du pain dès l’achat, les herbes hachées dans un peu d’huile, les blancs d’œufs, les restes de sauce. Ainsi, <a href="/fr/reduire-gaspillage-alimentaire/">moins de gaspillage</a> devient une conséquence de la planification, pas un combat à mener à part.</p>""",
            ),
            (
                "Les habitudes qui font la différence",
                """<ul><li><strong>Décidez avant d’avoir faim.</strong> Un menu écrit le dimanche vaut mieux qu’une décision prise à 19&nbsp;h devant le rayon traiteur.</li><li><strong>Regardez le frigo avant la liste.</strong> Une photo suffit pour que Cibello sache ce qu’il y a, et où.</li><li><strong>Cuisinez en double une fois par semaine.</strong> Le second repas ne coûte que le temps de le réchauffer.</li><li><strong>Gardez une soirée «&nbsp;restes&nbsp;».</strong> Elle absorbe ce qui n’a pas trouvé sa place.</li><li><strong>Acceptez les répétitions.</strong> Un plat apprécié qui revient toutes les deux semaines n’est pas de la monotonie, c’est une base.</li></ul><p>Pour des idées qui partent de ce que vous avez déjà, voyez le guide <a href="/fr/recettes-avec-ingredients/">recettes avec les ingrédients déjà chez vous</a>.</p>""",
            ),
        ],
        faq=[
            ("Comment manger pas cher pendant toute une semaine ?", "Partez du placard, planifiez cinq à sept plats en comptant les restes, placez les produits à date courte en début de semaine et n’achetez que ce qui manque."),
            ("Quels aliments sont les moins chers pour construire des repas ?", "Pâtes, riz, boulgour, lentilles, haricots, œufs, tomates concassées, flocons d’avoine, légumes racines de saison, poissons en conserve et légumes surgelés."),
            ("Comment Cibello aide-t-il à dépenser moins pour la nourriture ?", "L’application sait ce que vous avez, propose des recettes qui l’utilisent et ne met dans la liste de courses que ce qui manque, ce qui réduit les doublons et le gaspillage."),
            ("Un menu économique peut-il aussi être équilibré ?", "Oui. Légumineuses, légumes, œufs et céréales complètes sont à la fois économiques et nourrissants. Les valeurs nutritionnelles dans l’application sont des estimations, pas un conseil diététique."),
        ],
    ),
    # -----------------------------------------------------------------------
    "eu-food-waste-stats": dict(
        slug="/fr/gaspillage-alimentaire-chiffres/",
        label="Chiffres du gaspillage",
        title="Gaspillage alimentaire en Europe : les chiffres | Cibello",
        desc="Combien de nourriture est gaspillée dans l’Union européenne ? Les chiffres Eurostat 2023 : 58,2 millions de tonnes, environ 130 kg par habitant, plus de la moitié dans les foyers.",
        eyebrow="Statistiques",
        h1="Gaspillage alimentaire en Europe : les chiffres clés",
        lead="Combien de nourriture jette-t-on en Europe, et qui en est responsable&nbsp;? Cette page rassemble les estimations officielles d’Eurostat pour l’Union européenne, avec leur source, et explique ce qu’elles signifient pour un foyer ordinaire.",
        sections=[
            (
                "Le gaspillage alimentaire dans l’UE en bref (2023)",
                """<div class="table-wrap"><table class="cmp"><caption>Déchets alimentaires = tous les déchets d’origine alimentaire, parties comestibles et non comestibles comprises (épluchures, os, marc de café). Chiffres Eurostat, année de référence 2023, masse fraîche.</caption><thead><tr><th scope="col">Indicateur</th><th scope="col">Valeur</th><th scope="col">Source</th></tr></thead><tbody><tr><th scope="row">Déchets alimentaires dans l’UE, total</th><td>58,2 millions de tonnes par an</td><td>Eurostat, estimations 2023</td></tr><tr><th scope="row">Par habitant</th><td>environ 130 kg par an</td><td>Eurostat</td></tr><tr><th scope="row">Part des ménages</th><td>53 %, soit environ 31 millions de tonnes</td><td>Eurostat</td></tr><tr><th scope="row">Déchets alimentaires des ménages par habitant</th><td>69 kg par an</td><td>Eurostat</td></tr><tr><th scope="row">Évolution par rapport à 2022</th><td>57,8 millions de tonnes en 2022, soit +0,7 %</td><td>Eurostat</td></tr></tbody></table></div><p>Source&nbsp;: <a href="https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Food_waste_and_food_waste_prevention_-_estimates" rel="noopener">Eurostat, Food waste and food waste prevention, estimates</a> (Statistics Explained), et le communiqué Eurostat du 16 octobre 2025 sur les 130 kg de nourriture gaspillés par personne et par an dans l’UE.</p>""",
            ),
            (
                "Qui gaspille quoi : la répartition par maillon de la chaîne",
                """<div class="table-wrap"><table class="cmp"><caption>Répartition des déchets alimentaires de l’UE par étape de la chaîne alimentaire, 2023. Source&nbsp;: Eurostat.</caption><thead><tr><th scope="col">Maillon</th><th scope="col">Part du total</th><th scope="col">Par habitant et par an</th></tr></thead><tbody><tr><th scope="row">Ménages</th><td>53 %</td><td>69 kg</td></tr><tr><th scope="row">Fabrication de produits alimentaires et de boissons</th><td>19 %</td><td>24 kg</td></tr><tr><th scope="row">Restaurants et services de restauration</th><td>11 %</td><td>14 kg</td></tr><tr><th scope="row">Production primaire</th><td>10 %</td><td>12 kg</td></tr><tr><th scope="row">Commerce de détail et autre distribution</th><td>8 %</td><td>10 kg</td></tr></tbody></table></div><p>Le chiffre qui surprend le plus est celui des ménages. On imagine volontiers que le gaspillage se produit surtout dans les champs, les usines ou les supermarchés. En réalité, plus de la moitié des déchets alimentaires de l’Union européenne naît dans les cuisines des particuliers. Cela signifie aussi que le levier le plus important est à portée de main.</p>""",
            ),
            (
                "Une tendance qui ne recule pas encore",
                """<p>Entre 2022 et 2023, le total est passé de 57,8 à 58,2 millions de tonnes, une hausse de 0,7 %. La courbe ne s’effondre pas, et les gains faciles semblent déjà réalisés. Ce qui reste, ce sont les habitudes du quotidien&nbsp;: acheter sans savoir ce qu’il y a déjà à la maison, oublier un produit au fond du réfrigérateur, cuisiner trop et ne pas prévoir les restes. Ces gestes ne se corrigent pas par une campagne d’affichage, mais par une meilleure visibilité de sa propre cuisine.</p>""",
            ),
            (
                "L’objectif européen pour 2030",
                """<p>Dans la révision de la directive-cadre sur les déchets adoptée en 2025, l’Union européenne s’est fixé deux objectifs contraignants à l’horizon 2030, par rapport à la moyenne 2021-2023&nbsp;:</p><ul><li>réduire de <strong>10 %</strong> les déchets alimentaires dans la transformation et la fabrication&nbsp;;</li><li>réduire de <strong>30 % par habitant</strong> les déchets alimentaires dans le commerce de détail, les restaurants, les services de restauration et les ménages.</li></ul><p>Il s’agit de l’objectif de l’Union&nbsp;; chaque État membre le décline ensuite dans sa propre politique. Pour un foyer, l’ordre de grandeur est parlant&nbsp;: passer de 69 kg à moins de 50 kg par personne et par an, c’est à peu près ce que représentent les légumes oubliés, le pain rassis et les restes jetés d’une semaine ordinaire, mois après mois.</p>""",
            ),
            (
                "Que signifient ces chiffres pour un foyer",
                """<p>Avec 69 kg par personne, un foyer de quatre personnes jette en moyenne plus de 275 kg de déchets alimentaires par an, dont une bonne partie aurait pu être mangée. Les enquêtes convergent sur les mêmes causes&nbsp;: fruits et légumes achetés en trop grande quantité, pain qui sèche, restes sans plan et produits laitiers jetés à la date indicative alors qu’ils étaient encore bons. Elles convergent aussi sur les mêmes remèdes&nbsp;: planifier quelques dîners à la fois, faire les courses avec une liste, ranger correctement et utiliser d’abord ce qui a la date la plus courte.</p><p>C’est exactement ce que Cibello rend plus facile&nbsp;: vous photographiez le frigo et les placards, l’application reconnaît les produits, rappelle discrètement ce qui doit être utilisé bientôt et propose des recettes qui le mettent à profit. Le guide <a href="/fr/reduire-gaspillage-alimentaire/">réduire le gaspillage alimentaire à la maison</a> détaille les gestes concrets, et le <a href="/fr/planificateur-repas/">planificateur de repas</a> montre comment en faire une habitude plutôt qu’un projet.</p>""",
            ),
            (
                "Les données par pays",
                """<p>Cette page reste volontairement au niveau de l’Union européenne. Les offices statistiques nationaux et les agences environnementales publient les données propres à chaque pays, avec des méthodes et des années de référence qui peuvent différer. Les tableaux d’Eurostat permettent de comparer les États membres à partir d’une méthode commune. Avant de citer un chiffre national, vérifiez l’année et le périmètre&nbsp;: déchets alimentaires au sens large ou seulement la part comestible.</p>""",
            ),
            (
                "Pour citer cette page",
                """<p>Vous pouvez reprendre ces chiffres en citant Eurostat comme source. Pour renvoyer à cette synthèse&nbsp;: «&nbsp;Cibello, Gaspillage alimentaire en Europe&nbsp;: les chiffres clés, cibello.app/fr/gaspillage-alimentaire-chiffres/, mis à jour en septembre 2026&nbsp;». Questions sur la page&nbsp;: <a href="mailto:hello@cibello.app">hello@cibello.app</a>.</p>""",
            ),
        ],
        faq=[
            ("Combien de nourriture est gaspillée dans l’Union européenne chaque année ?", "Environ 58,2 millions de tonnes de déchets alimentaires en 2023 selon Eurostat, soit environ 130 kg par habitant."),
            ("Quelle part du gaspillage alimentaire vient des ménages ?", "Environ 53 % du total, soit près de 31 millions de tonnes ou 69 kg par habitant et par an, d’après Eurostat."),
            ("Quel est l’objectif de l’UE en matière de gaspillage alimentaire ?", "Réduire d’ici 2030 les déchets alimentaires de 10 % dans la transformation et la fabrication, et de 30 % par habitant dans le commerce, la restauration et les ménages, par rapport à la moyenne 2021-2023."),
            ("Où trouver les chiffres pour mon pays ?", "Les offices statistiques nationaux et les agences environnementales publient les données par pays. Eurostat propose aussi des tableaux comparables entre États membres."),
        ],
    ),
    # -----------------------------------------------------------------------
    "ai-meal-planner": dict(
        slug="/fr/planificateur-repas-ia/",
        label="Planificateur IA",
        title="Planificateur de repas IA qui part du frigo | Cibello",
        desc="Un planificateur de repas à base d’IA qui scanne votre frigo, apprend les goûts du foyer et planifie la semaine avec ce que vous avez déjà. Comment ça marche, et où l’IA peut se tromper.",
        eyebrow="IA et planification",
        h1="Un planificateur de repas IA qui part de ce qu’il y a dans votre cuisine",
        lead="La plupart des planificateurs de repas à base d’IA génèrent un menu à partir de rien et vous tendent une longue liste de courses. Cibello part de votre vraie cuisine&nbsp;: l’application reconnaît ce que vous avez, apprend ce que votre foyer aime et planifie des repas qui l’utilisent. Voici comment cela fonctionne, honnêtement, y compris là où l’IA se trompe.",
        sections=[
            (
                "Ce que fait vraiment l’IA",
                """<ol><li><strong>Elle reconnaît les aliments sur une photo.</strong> Pointez l’appareil vers une étagère du frigo, un placard, un ticket de caisse ou un code-barres&nbsp;; l’application identifie les produits et l’endroit où ils sont rangés. Vous vérifiez le résultat avant qu’il soit enregistré.</li><li><strong>Elle tient un inventaire vivant.</strong> Votre «&nbsp;Food Twin&nbsp;» est une image de la cuisine qui se met à jour au fil des courses et des repas.</li><li><strong>Elle propose des repas avec une raison.</strong> Les suggestions tiennent compte de ce que vous avez, de ce qui approche de sa date et des goûts du foyer, et expliquent toujours pourquoi.</li><li><strong>Elle planifie la semaine.</strong> Le <a href="/fr/planificateur-repas/">planificateur de repas</a> varie les ingrédients et les types de plats, et remplit une liste de courses partagée avec uniquement ce qui manque.</li></ol>""",
            ),
            (
                "Ce qu’elle ne fait pas",
                """<p>L’IA peut mal lire une étiquette, rater un produit au fond de l’étagère ou deviner une date erronée. C’est pourquoi chaque scan est relu par vous avant d’être enregistré, et pourquoi les suggestions sont une aide, pas une décision. Les filtres de recettes et d’allergènes ne sont pas une garantie&nbsp;; les valeurs nutritionnelles sont des estimations pour planifier, pas un avis médical. Cibello ne juge jamais ce que vous mangez ni en quelle quantité, et n’utilise pas la culpabilité comme moteur.</p><p>L’application ne remplace pas non plus votre jugement en cuisine. Elle indique quels ingrédients manquent pour une recette, elle ne décide pas à votre place de les remplacer. Elle propose une semaine, vous la relisez, déplacez un plat, en retirez un autre. Le menu reste un brouillon jusqu’à ce que vous le validiez.</p>""",
            ),
            (
                "Vos données et l’IA",
                """<p>Les images sont analysées pour reconnaître les aliments. Les propres modèles de Cibello ne sont entraînés que sur vos corrections et, si vous l’activez séparément, sur des images anonymisées&nbsp;; ces deux options sont désactivées par défaut. Les données sont stockées dans l’Union européenne, vous pouvez voir ce qui est conservé et supprimer votre compte dans l’application à tout moment. Cibello ne vend pas de données personnelles. Le détail figure dans la <a href="/fr/privacy/">politique de confidentialité</a>.</p>""",
            ),
            (
                "Pourquoi partir de la cuisine plutôt que des recettes",
                """<p>Un planning qui ignore ce que vous possédez produit du gaspillage et de longues courses. Partir de l’inventaire signifie moins d’achats, des aliments utilisés avant qu’ils ne s’abîment et moins de décisions à prendre le soir. C’est aussi ce qui rend les suggestions crédibles&nbsp;: une recette dont vous avez 80 % des ingrédients est faisable ce soir, une recette générée à partir de rien demande d’abord un passage au magasin. Si vous voulez surtout une réponse pour ce soir, commencez par le guide <a href="/fr/recettes-avec-ingredients/">recettes avec les ingrédients déjà chez vous</a>&nbsp;; si c’est l’inventaire lui-même qui vous intéresse, voyez l’<a href="/fr/application-garde-manger/">application garde-manger</a>.</p>""",
            ),
            (
                "Une semaine que vous relisez, pas un menu imposé",
                """<p>Quand vous demandez une semaine, Cibello compose une proposition qui alterne les plats et les produits, met en avant ce qui doit être consommé bientôt et tient compte de ce que le foyer a l’habitude de choisir. Chaque plat porte une explication courte. Vous gardez ce qui vous convient, remplacez le reste, puis la liste de courses se remplit avec ce qui manque réellement. Les membres du foyer voient le même inventaire, le même menu et la même liste, pendant la période d’essai puis avec un abonnement. Les restes rangés en boîtes-repas peuvent figurer dans l’inventaire et entrer dans la planification comme n’importe quel autre produit.</p>""",
            ),
            (
                "Pour commencer",
                """<p>Cibello est disponible sur iOS et Android, en douze langues dont le français. La période d’essai dure quatorze jours, sans carte bancaire. L’application s’adresse aux adultes de 18 ans et plus. Le premier pas tient en une photo du frigo&nbsp;: quelques secondes de vérification, et les premières suggestions arrivent. Inutile de tout inventorier le premier jour&nbsp;; commencez par le réfrigérateur, ajoutez les placards quand vous en avez le temps, et laissez les tickets de caisse faire le reste au fil des courses. Pour une vue d’ensemble des fonctionnalités, voyez la <a href="/fr/">page d’accueil</a>.</p>""",
            ),
        ],
        faq=[
            ("Cibello est-il un planificateur de repas IA ?", "Oui. Cibello utilise l’IA pour reconnaître les aliments sur des photos, tenir un inventaire de la cuisine et proposer des repas et des menus de la semaine à partir de ce que vous avez et de ce que votre foyer aime."),
            ("L’IA peut-elle se tromper ?", "Oui. Le scan peut mal lire ou oublier des produits, c’est pourquoi vous vérifiez le résultat avant de l’enregistrer. Les suggestions sont une aide, pas une décision."),
            ("L’IA s’entraîne-t-elle sur mes photos ?", "Par défaut, seulement sur vos corrections. L’entraînement sur des images anonymisées est une option séparée, désactivée tant que vous ne l’activez pas."),
            ("Est-ce gratuit ?", "Cibello propose quatorze jours d’essai gratuit sans carte bancaire. Les fonctions de partage dans le foyer sont disponibles pendant l’essai puis avec un abonnement. Le prix est indiqué dans les boutiques d’applications."),
        ],
    ),
    # -----------------------------------------------------------------------
    "pantry-app": dict(
        slug="/fr/application-garde-manger/",
        label="Inventaire de cuisine",
        title="Application garde-manger pour votre cuisine | Cibello",
        desc="Une application garde-manger qui remplit l’inventaire à partir de photos, tickets de caisse et codes-barres, suit les dates et propose des recettes avec ce que vous avez déjà.",
        eyebrow="Inventaire",
        h1="Application garde-manger : sachez ce qu’il y a dans votre cuisine, et où",
        lead="Une application garde-manger n’a d’intérêt que si elle demande moins d’effort qu’elle n’en économise. Cibello construit l’inventaire à partir de photos, de tickets de caisse et de codes-barres, le partage avec le foyer et le transforme en dîners. Voici comment.",
        sections=[
            (
                "Remplir l’inventaire sans rien taper",
                """<p>Photographiez une étagère du réfrigérateur, un tiroir du congélateur ou un placard&nbsp;: l’application reconnaît les produits et l’endroit où ils se trouvent. Après les courses, scannez le ticket de caisse pour tout ajouter d’un coup, ou scannez un code-barres pour un produit isolé. L’IA peut se tromper, vous relisez donc le résultat et corrigez avant d’enregistrer. Chaque correction améliore le scan suivant. La saisie manuelle reste possible, mais elle n’est plus la règle&nbsp;: c’est ce qui fait la différence avec les listes d’inventaire que l’on abandonne au bout de deux semaines.</p><p>Un conseil pour bien démarrer&nbsp;: photographiez une étagère à la fois, avec un bon éclairage, plutôt que tout le réfrigérateur d’un coup. Les produits sont mieux reconnus, et la vérification prend quelques secondes au lieu de quelques minutes.</p>""",
            ),
            (
                "Savoir ce que vous avez, et où",
                """<p>L’inventaire est organisé par emplacement&nbsp;: réfrigérateur, congélateur, placard, et même «&nbsp;porte du frigo&nbsp;». Tous les membres du foyer voient la même image, si bien que personne n’achète un troisième pot de moutarde. Les quantités et les dates sont attachées aux produits, et vous pouvez les vérifier ou les ajuster en quelques secondes. Le résultat ressemble à ce que vous auriez en tête si vous aviez une mémoire parfaite de vos placards, sans avoir à ouvrir chaque porte.</p><p>Cette visibilité change la façon de faire les courses. On n’achète plus «&nbsp;au cas où&nbsp;», on achète pour compléter. Et quand une recette vous tente, vous savez tout de suite si elle est faisable ce soir ou si elle attendra le prochain passage au magasin.</p>""",
            ),
            (
                "Des dates suivies avec douceur",
                """<p>Les produits qui approchent de leur date sont signalés avant qu’il ne soit trop tard, par un rappel discret plutôt qu’une alerte culpabilisante. L’application propose en même temps des recettes qui utilisent ces produits, avec une explication. Rappel utile&nbsp;: une date «&nbsp;à consommer de préférence avant&nbsp;» est une indication de qualité, pas une limite de sécurité. Regardez, sentez, goûtez avant de jeter. Les dates enregistrées sont celles que vous avez vérifiées&nbsp;; l’application ne remplace pas votre jugement.</p>""",
            ),
            (
                "Transformer l’inventaire en dîner",
                """<p>Un inventaire de cuisine ne sert que s’il vous fait gagner du temps. Cibello le compare à plus de 9&nbsp;000 recettes et affiche les <a href="/fr/recettes-avec-ingredients/">recettes avec les ingrédients déjà chez vous</a>, classées selon la part des ingrédients présents. Une recette dont vous avez presque tout remonte en tête, et l’application indique ce qui manque. Le <a href="/fr/planificateur-repas/">planificateur de repas</a> construit la semaine autour de ce qui doit être utilisé, et la liste de courses ne contient que le reste. C’est ainsi que l’inventaire aide à <a href="/fr/reduire-gaspillage-alimentaire/">réduire le gaspillage alimentaire</a> sans travail supplémentaire.</p>""",
            ),
            (
                "Partagé avec tout le foyer",
                """<p>Inventaire, menu et liste de courses sont partagés entre les membres du foyer pendant la période d’essai, puis avec un abonnement. Quand quelqu’un utilise ou achète un produit, tout le monde voit la mise à jour. La personne qui fait les courses n’a plus besoin d’appeler pour demander s’il reste du lait. Les boîtes-repas préparées le dimanche peuvent figurer dans l’inventaire comme n’importe quel autre produit, si bien qu’elles ne sont pas oubliées derrière les yaourts.</p><p>Le partage a une autre vertu&nbsp;: la charge mentale de la cuisine ne repose plus sur une seule personne. Celui qui rentre le premier ouvre l’application, voit ce qu’il y a et ce qui doit être utilisé, et peut lancer le dîner sans attendre d’instructions. Chacun peut ajouter un produit à la liste au moment où il remarque qu’il manque, plutôt que de s’en souvenir au magasin.</p>""",
            ),
            (
                "Vos données, votre compte",
                """<p>Les images servent à reconnaître les aliments. Les modèles de Cibello ne s’entraînent que sur vos corrections et, si vous l’activez séparément, sur des images anonymisées&nbsp;; ces options sont désactivées par défaut. Les données sont stockées dans l’Union européenne et le compte peut être supprimé dans l’application à tout moment. L’application s’adresse aux adultes de 18 ans et plus, et la période d’essai de quatorze jours ne demande pas de carte bancaire. Le détail se trouve dans la <a href="/fr/privacy/">politique de confidentialité</a>.</p>""",
            ),
        ],
        faq=[
            ("Comment ajouter des produits dans l’application garde-manger ?", "Photographiez les étagères, scannez les tickets de caisse ou les codes-barres. Relisez les produits détectés avant d’enregistrer, car l’IA peut mal lire un produit ou une date."),
            ("L’application suit-elle les dates de péremption ?", "Oui. Les dates sont attachées aux produits, l’application signale ce qui doit être utilisé bientôt et propose des recettes qui l’utilisent."),
            ("Mon foyer peut-il partager le même inventaire ?", "Oui. Les membres du foyer partagent l’inventaire, le menu de la semaine et la liste de courses pendant la période d’essai, puis avec un abonnement."),
            ("Propose-t-elle des recettes à partir de ce que j’ai ?", "Oui. Votre inventaire est comparé à plus de 9 000 recettes, classées selon la part des ingrédients que vous avez déjà."),
        ],
    ),
    # -----------------------------------------------------------------------
    "app-comparison": dict(
        slug="/fr/meilleure-application-repas/",
        label="Comparatif applis repas",
        title="Quelle application pour planifier ses repas ? | Cibello",
        desc="Comparatif honnête des applications de planification de repas : Cibello, Mealime, Samsung Food, Plan to Eat, Paprika, SuperCook et les applis photo-recettes. Inventaire, planning, listes, prix.",
        eyebrow="Comparatif",
        h1="Quelle est la meilleure application de planification de repas ? Cibello face à Mealime, Samsung Food, Plan to Eat, Paprika et SuperCook",
        lead="«&nbsp;Application de planification de repas&nbsp;» recouvre des outils très différents&nbsp;: menus guidés, gestionnaires de recettes, listes de courses partagées, moteurs de recettes par ingrédients et, plus récemment, applications qui transforment une photo du frigo en recettes. Ils ne résolvent pas le même problème. Cette page compare les options les plus courantes, y compris ce que Cibello ne fait pas.",
        sections=[
            (
                "Cinq familles d’applications de planification de repas",
                """<ul><li><strong>Les planificateurs guidés</strong> (Mealime, eMeals)&nbsp;: vous choisissez parmi une sélection de recettes et obtenez une liste triée par rayon. Rapides à prendre en main, mais ils ignorent ce qu’il y a déjà dans votre cuisine et leurs catalogues tournent en rond.</li><li><strong>Les gestionnaires de recettes</strong> (Paprika, Plan to Eat, Samsung Food)&nbsp;: enregistrez des recettes de n’importe quel site, planifiez sur un calendrier, générez des listes. Parfaits si vous avez déjà une bibliothèque de recettes&nbsp;; l’inventaire est manuel ou absent.</li><li><strong>Les moteurs par ingrédients</strong> (SuperCook)&nbsp;: tapez ou dictez ce que vous avez et recevez des recettes correspondantes parmi des millions. Puissant pour ce soir, mais sans planning, sans partage dans le foyer ni suivi des dates.</li><li><strong>Les applications photo-recettes</strong> (Fridge AI, Pantry Pic)&nbsp;: photographiez le frigo et obtenez des idées. C’est ce qui se rapproche le plus du scan de Cibello, mais généralement sans inventaire durable, sans menu de la semaine ni liste partagée.</li><li><strong>Les applications anti-gaspi</strong> (Too Good To Go, Phenix)&nbsp;: achetez les invendus des commerces et restaurants. Utile pour la planète, sans rapport avec ce qui se trouve dans votre propre frigo.</li></ul><p>Cibello se situe à l’intersection de ces familles&nbsp;: un inventaire construit à partir de photos, de tickets de caisse et de codes-barres, des recettes classées selon ce que vous avez, un <a href="/fr/planificateur-repas/">menu de la semaine</a> qui utilise les aliments avant leur date, et une liste de courses du foyer qui ne contient que ce qui manque. Voyez comment fonctionnent l’<a href="/fr/application-garde-manger/">application garde-manger</a> et le <a href="/fr/planificateur-repas-ia/">planificateur de repas IA</a>.</p>""",
            ),
            (
                "Tableau comparatif",
                """<div class="table-wrap"><table class="cmp"><caption>""" + CAPTION_CMP + """</caption><thead><tr><th scope="col">Fonctionnalité</th><th scope="col">Cibello</th><th scope="col">SuperCook</th><th scope="col">Mealime</th><th scope="col">Samsung Food</th><th scope="col">Plan to Eat</th><th scope="col">Paprika</th><th scope="col">Fridge AI / Pantry Pic</th></tr></thead><tbody><tr><th scope="row">Inventaire construit à partir de photos, tickets de caisse et codes-barres</th><td><span class="y">Oui</span></td><td><span class="n">Non</span> (saisie ou dictée)</td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="p">En partie</span> (photo, par session)</td></tr><tr><th scope="row">Recettes classées selon ce que vous avez déjà</th><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="y">Oui</span></td></tr><tr><th scope="row">Menu de la semaine qui utilise d’abord les produits à date courte</th><td><span class="y">Oui</span></td><td><span class="n">Non</span></td><td><span class="p">En partie</span> (menu guidé)</td><td><span class="p">En partie</span> (calendrier simple)</td><td><span class="p">En partie</span> (calendrier manuel)</td><td><span class="p">En partie</span> (calendrier manuel)</td><td><span class="n">Non</span></td></tr><tr><th scope="row">Liste de courses partagée avec uniquement ce qui manque</th><td><span class="y">Oui</span></td><td><span class="n">Non</span></td><td><span class="p">En partie</span> (liste automatique, partage limité)</td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="p">En partie</span> (partage limité)</td><td><span class="n">Non</span></td></tr><tr><th scope="row">Rappels avant la date</th><td><span class="y">Oui</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td></tr><tr><th scope="row">Importer vos propres recettes depuis le web</th><td>Pas une priorité&nbsp;: les recettes sont mises en regard de votre inventaire</td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="n">Non</span></td></tr><tr><th scope="row">Données nutritionnelles</th><td><span class="p">En partie</span> (estimations)</td><td><span class="n">Non</span></td><td><span class="p">En partie</span> (offre payante)</td><td><span class="p">En partie</span> (offre payante)</td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="p">En partie</span></td></tr><tr><th scope="row">Modèle tarifaire</th><td>Essai gratuit, puis abonnement</td><td>Gratuit</td><td>Gratuit + abonnement</td><td>Gratuit + abonnement</td><td>Abonnement</td><td>Achat unique</td><td>Freemium</td></tr><tr><th scope="row">Langues</th><td>12</td><td>Plusieurs</td><td>Anglais</td><td>Plusieurs</td><td>Anglais</td><td>Anglais</td><td>Anglais</td></tr><tr><th scope="row">Données stockées dans l’UE, suppression du compte dans l’app</th><td><span class="y">Oui</span></td><td>Non précisé</td><td>Non précisé</td><td>Non précisé</td><td>Non précisé</td><td>Non précisé</td><td>Non précisé</td></tr></tbody></table></div>""",
            ),
            (
                "Ce que Cibello ne fait pas",
                """<p>Cibello n’importe pas de recettes depuis n’importe quel site, ne vend ni nourriture ni bons de réduction, et n’est pas un compteur de calories&nbsp;: les valeurs nutritionnelles sont des estimations pour planifier. Son IA peut mal lire une étiquette ou rater un produit au fond de l’étagère, c’est pourquoi vous relisez chaque scan avant qu’il soit enregistré. Si vous voulez surtout un gestionnaire de recettes payé une fois pour toutes, Paprika conviendra mieux&nbsp;; si vous voulez des dîners guidés gratuits sans aucune mise en place, Mealime.</p>""",
            ),
            (
                "Pourquoi l’inventaire change la comparaison",
                """<p>La plupart des applications de ce tableau partent des recettes et vous demandent d’adapter votre cuisine. Une application qui part de l’inventaire renverse la logique&nbsp;: elle sait ce qui est là, ce qui doit être mangé bientôt et ce que le foyer aime, puis elle propose. La liste de courses en découle au lieu de la précéder. C’est ce qui permet de réduire les doublons et le gaspillage sans discipline supplémentaire, à condition que l’inventaire reste à jour, et c’est là que le scan de photos, de tickets et de codes-barres fait la différence par rapport à une saisie manuelle.</p>""",
            ),
            (
                "Comment choisir",
                """<ul><li><strong>Vous avez une grande collection de recettes</strong> et aimez planifier à la main&nbsp;: Plan to Eat ou Paprika.</li><li><strong>Vous voulez des dîners choisis pour vous</strong>, sans rien configurer&nbsp;: Mealime.</li><li><strong>Vous voulez une réponse pour ce soir à partir de l’étagère</strong>, sans compte&nbsp;: SuperCook.</li><li><strong>Vous voulez que la cuisine se planifie elle-même</strong>&nbsp;: un inventaire depuis une photo, des recettes avec ce que vous avez, une semaine qui utilise les aliments avant qu’ils ne s’abîment et une seule liste pour le foyer. C’est Cibello. Commencez par les <a href="/fr/recettes-avec-ingredients/">recettes avec les ingrédients déjà chez vous</a>.</li></ul><p>Pour les applications centrées sur les recettes elles-mêmes, voyez le <a href="/fr/meilleure-application-recettes/">comparatif des applications de recettes</a>.</p>""",
            ),
        ],
        faq=[
            ("Quelle est la meilleure application de planification de repas ?", "Cela dépend du problème. Pour des dîners guidés : Mealime. Pour votre propre bibliothèque de recettes : Plan to Eat ou Paprika. Pour des recettes à partir d’ingrédients tapés : SuperCook. Pour un inventaire depuis des photos, des recettes avec ce que vous avez, un menu de la semaine et une liste partagée : Cibello."),
            ("Existe-t-il une application de planification de repas gratuite ?", "Mealime, Samsung Food et SuperCook ont une offre gratuite. Cibello propose quatorze jours d’essai sans carte bancaire ; les fonctions de partage dans le foyer continuent avec un abonnement."),
            ("Quelle application sait ce qu’il y a dans mon frigo ?", "Cibello construit un inventaire à partir de photos, de tickets de caisse et de codes-barres et le tient à jour. SuperCook demande de taper ou dicter les ingrédients ; les applications photo-recettes reconnaissent une photo mais conservent rarement un inventaire."),
            ("Cibello fonctionne-t-il en France et en Belgique ?", "Oui. L’application est disponible sur iOS et Android en douze langues, dont le français, avec des données stockées dans l’Union européenne."),
        ],
    ),
    # -----------------------------------------------------------------------
    "recipe-app-comparison": dict(
        slug="/fr/meilleure-application-recettes/",
        label="Comparatif applis recettes",
        title="Meilleure application de recettes : comparatif | Cibello",
        desc="Quelle application de recettes choisir ? Cibello face à Paprika, Samsung Food, Yummly, SideChef et SuperCook : recettes avec ce que vous avez, inventaire, menu de la semaine, liste partagée.",
        eyebrow="Comparatif",
        h1="Quelle est la meilleure application de recettes ? Cibello face à Paprika, Samsung Food, Yummly, SideChef et SuperCook",
        lead="Les applications de recettes ne répondent pas toutes à la même question. Certaines archivent vos recettes, d’autres vous inspirent, d’autres vous guident pas à pas, et quelques-unes partent de ce qu’il y a dans votre cuisine. Ce comparatif classe les options les plus courantes et dit clairement où Cibello se place, et où il ne se place pas.",
        sections=[
            (
                "Quatre familles d’applications de recettes",
                """<ul><li><strong>Les gestionnaires de recettes</strong> (Paprika, Samsung Food, Plan to Eat)&nbsp;: enregistrez des recettes depuis n’importe quel site, organisez-les, ajustez les portions, générez des listes. Idéal si vous avez déjà une collection.</li><li><strong>Les bibliothèques et la découverte</strong> (Yummly, Tasty, Kitchen Stories, et en France les grands sites communautaires comme Marmiton)&nbsp;: vastes catalogues, vidéos, fils personnalisés. Parfait pour l’inspiration, faible sur ce qu’il y a dans votre frigo.</li><li><strong>La cuisine guidée</strong> (SideChef, Kitchen Stories)&nbsp;: instructions pas à pas avec minuteurs, parfois connectées à des appareils.</li><li><strong>Les applications qui partent des ingrédients</strong> (SuperCook, Cibello)&nbsp;: commencez par ce que vous avez. SuperCook vous demande de taper ou dicter les ingrédients&nbsp;; Cibello construit l’inventaire à partir de photos, de tickets de caisse et de codes-barres et le tient à jour.</li></ul>""",
            ),
            (
                "Tableau comparatif",
                """<div class="table-wrap"><table class="cmp"><caption>""" + CAPTION_CMP + """</caption><thead><tr><th scope="col">Fonctionnalité</th><th scope="col">Cibello</th><th scope="col">Paprika</th><th scope="col">Samsung Food</th><th scope="col">Yummly</th><th scope="col">SideChef</th><th scope="col">SuperCook</th></tr></thead><tbody><tr><th scope="row">Recettes avec ce que vous avez à la maison</th><td><span class="y">Oui</span> (classées par part d’ingrédients présents)</td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="p">En partie</span> (filtre garde-manger)</td><td><span class="n">Non</span></td><td><span class="y">Oui</span> (ingrédients tapés)</td></tr><tr><th scope="row">Inventaire construit à partir de photos, tickets, codes-barres</th><td><span class="y">Oui</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td></tr><tr><th scope="row">Enregistrer des recettes depuis n’importe quel site</th><td>Pas une priorité&nbsp;: les recettes sont mises en regard de votre inventaire</td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="p">En partie</span></td><td><span class="n">Non</span></td></tr><tr><th scope="row">Catalogue de recettes intégré</th><td>9&nbsp;000+</td><td><span class="n">Non</span> (les vôtres)</td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td>11 millions (agrégées)</td></tr><tr><th scope="row">Menu de la semaine</th><td><span class="y">Oui</span></td><td><span class="y">Oui</span> (calendrier)</td><td><span class="p">En partie</span></td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="n">Non</span></td></tr><tr><th scope="row">Liste de courses partagée dans le foyer</th><td><span class="y">Oui</span></td><td><span class="p">En partie</span></td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="n">Non</span></td></tr><tr><th scope="row">Rappels avant la date</th><td><span class="y">Oui</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td><td><span class="n">Non</span></td></tr><tr><th scope="row">Mode cuisine pas à pas</th><td><span class="p">En partie</span></td><td><span class="p">En partie</span></td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="y">Oui</span></td><td><span class="n">Non</span></td></tr><tr><th scope="row">Prix</th><td>Essai gratuit, puis abonnement</td><td>Achat unique</td><td>Gratuit + abonnement</td><td>Gratuit + abonnement</td><td>Gratuit + abonnement</td><td>Gratuit</td></tr><tr><th scope="row">Langues</th><td>12</td><td>Plusieurs</td><td>Plusieurs</td><td>Anglais</td><td>Anglais</td><td>Plusieurs</td></tr></tbody></table></div>""",
            ),
            (
                "Ce que Cibello ne fait pas",
                """<p>Cibello n’importe pas de recettes depuis n’importe quel site, et son catalogue est plus petit que celui de Yummly ou que l’index agrégé de SuperCook. Si votre besoin principal est une archive personnelle de recettes, Paprika ou Samsung Food conviendront mieux. Cibello est le bon choix quand la question n’est pas «&nbsp;où ranger mes recettes&nbsp;?&nbsp;» mais «&nbsp;qu’est-ce qu’on peut cuisiner avec ce qu’il y a ici, et comment arrêter de jeter&nbsp;?&nbsp;». Voyez l’<a href="/fr/application-garde-manger/">application garde-manger</a>, les <a href="/fr/recettes-avec-ingredients/">recettes avec les ingrédients déjà chez vous</a> et le <a href="/fr/meilleure-application-repas/">comparatif plus large des applications de planification de repas</a>.</p>""",
            ),
            (
                "Recettes avec ce que vous avez : la différence concrète",
                """<p>Dans une bibliothèque classique, vous cherchez une recette puis vous constatez ce qui manque. Dans Cibello, l’inventaire est comparé à plus de 9&nbsp;000 recettes et le résultat est classé selon la part des ingrédients déjà chez vous&nbsp;: une recette dont vous avez tout remonte en tête, une recette à laquelle il manque deux produits est affichée avec ces deux produits. Les suggestions tiennent aussi compte de ce qui approche de sa date et de ce que le foyer choisit d’habitude, avec une explication à chaque fois. Les filtres de régime et d’allergènes sont une aide, pas une garantie&nbsp;: vérifiez toujours les ingrédients vous-même. Une fois le plat choisi, ce qui manque rejoint la liste de courses partagée du foyer, et le produit utilisé disparaît de l’inventaire au prochain passage.</p>""",
            ),
            (
                "Comment choisir",
                """<ul><li><strong>Vous collectionnez des recettes</strong> trouvées sur le web et voulez les retrouver facilement&nbsp;: Paprika ou Samsung Food.</li><li><strong>Vous cherchez l’inspiration</strong> et aimez feuilleter&nbsp;: Yummly, Tasty ou un grand site communautaire.</li><li><strong>Vous voulez être guidé pas à pas</strong> pendant la cuisson&nbsp;: SideChef.</li><li><strong>Vous voulez une réponse pour ce soir</strong> à partir d’ingrédients tapés, sans compte&nbsp;: SuperCook.</li><li><strong>Vous voulez que les recettes partent de votre cuisine</strong>, avec un inventaire tenu à jour, un menu de la semaine et une liste partagée&nbsp;: Cibello. Quatorze jours d’essai sans carte bancaire, pour les adultes de 18 ans et plus.</li></ul>""",
            ),
        ],
        faq=[
            ("Quelle est la meilleure application de recettes ?", "Pour archiver vos propres recettes : Paprika ou Samsung Food. Pour l’inspiration : Yummly ou Tasty. Pour la cuisine guidée : SideChef. Pour des recettes avec ce que vous avez déjà, un menu de la semaine et une liste partagée : Cibello."),
            ("Existe-t-il une application de recettes qui utilise les ingrédients que j’ai déjà ?", "SuperCook associe des recettes aux ingrédients que vous tapez ou dictez. Cibello construit l’inventaire à partir de photos, de tickets de caisse et de codes-barres et classe les recettes selon la part des ingrédients que vous avez."),
            ("Puis-je importer mes propres recettes dans Cibello ?", "L’import de recettes depuis le web n’est pas la priorité. Cibello propose plus de 9 000 recettes et se concentre sur leur correspondance avec votre inventaire."),
            ("Y a-t-il une application de recettes gratuite ?", "SuperCook est gratuit, Samsung Food, Yummly et SideChef ont une offre gratuite. Cibello propose quatorze jours d’essai gratuit sans carte bancaire, puis un abonnement dont le prix est indiqué dans les boutiques d’applications."),
        ],
    ),
}
