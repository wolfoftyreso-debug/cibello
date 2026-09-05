"""Contenu français, phase 2, fichier A. Structure : voir _schema_extra.py."""

LANG = "fr"

GUIDES2 = {
    # ------------------------------------------------------------------
    "everyday-food": dict(
        slug="/fr/repas-du-quotidien/",
        label="Repas du quotidien",
        title="Repas du quotidien sans se compliquer la vie | Cibello",
        desc="Des repas du quotidien qui tiennent toute la semaine : partir du frigo, varier sans effort et cuisiner dans le temps dont vous disposez.",
        eyebrow="Cuisine de tous les jours",
        h1="Repas du quotidien : cuisiner simple toute la semaine",
        lead="La cuisine de tous les jours n’a pas besoin d’idées neuves chaque soir. Elle a besoin de plats faisables avec ce qu’il y a, dans le temps qu’il reste, et d’assez de variété pour que personne ne se lasse.",
        sections=[
            (
                "Qu’est-ce qu’un bon repas du quotidien&nbsp;?",
                """<p>Un bon repas du quotidien remplit trois conditions. Il se prépare dans le temps réellement disponible, souvent trente minutes entre le retour à la maison et le moment où tout le monde a faim. Il repose sur des produits que vous avez déjà ou que vous trouvez sans détour. Et il supporte la variation, pour que le mardi ne ressemble pas trop au lundi.</p><p>Il n’est presque jamais question de recettes inédites. La plupart des foyers tournent sur dix à quinze plats, et c’est parfaitement raisonnable. Ce qui sépare une semaine tendue d’une semaine calme, ce n’est pas le talent en cuisine, c’est la vue d’ensemble&nbsp;: savoir ce qu’il y a dans le frigo et avoir une idée de ce qu’on en fera.</p>""",
            ),
            (
                "Des recettes qui partent du frigo, pas du livre",
                """<p>La plupart des sites de recettes commencent par le mauvais bout&nbsp;: vous choisissez un plat, puis vous découvrez qu’il manque la moitié des ingrédients. Cibello inverse l’ordre. Une fois le réfrigérateur, le congélateur et les placards enregistrés, en les photographiant ou en scannant un ticket de caisse, l’application compare votre inventaire à plus de 9&nbsp;000 recettes et affiche pour chacune la part des ingrédients déjà chez vous. Les plats à 80 ou 100&nbsp;% sont en haut de la liste. Les idées deviennent des dîners faisables le soir même, pas seulement de l’inspiration. L’IA peut se tromper en lisant une photo ou un ticket, vous vérifiez donc le résultat avant de l’enregistrer.</p><p>Quelques familles de plats qui reviennent toute l’année&nbsp;:</p><ul><li>Pâtes, riz et semoule&nbsp;: presque toujours dans le placard, à combiner avec ce que le frigo contient.</li><li>Omelette, quiche sans pâte et crêpes salées&nbsp;: sauvent les œufs, le lait et les légumes à date courte.</li><li>Soupes, potages et plats mijotés&nbsp;: acceptent les restes et deviennent le déjeuner du lendemain.</li><li>Poêlées et salades composées&nbsp;: utilisent les demi-légumes et le riz ou le boulgour déjà cuits.</li><li>Plats au four&nbsp;: légumes racines, poulet ou poisson, avec très peu de manipulation.</li></ul>""",
            ),
            (
                "Planifier cinq soirs plutôt qu’un",
                """<p>Planifier cinq soirs d’affilée rend chaque soir plus simple. Un bon menu de la semaine tient compte du temps disponible chaque jour, de ce qui doit être consommé en premier et des plats qui laissent des restes pour le lendemain. Cibello varie les produits et les types de repas pour éviter que la même chose revienne plusieurs jours de suite, et rassemble ce qui manque dans une <a href="/fr/liste-de-courses/">liste de courses partagée</a> avec le foyer. Vous relisez et modifiez la proposition avant que la semaine commence&nbsp;: les suggestions sont une aide, pas une obligation. Le guide sur le <a href="/fr/planificateur-repas/">planificateur de repas</a> détaille comment construire cette habitude.</p>""",
            ),
            (
                "Rapide, économique ou adapté aux enfants selon la semaine",
                """<p>Le quotidien ne se ressemble pas d’une semaine à l’autre. Quand le temps manque, un <a href="/fr/diner-rapide/">dîner rapide en vingt à trente minutes</a> est le bon point de départ. Quand le budget est serré, on cuisine à partir du placard et on planifie les restes. Quand des enfants sont à table, on varie à l’intérieur des plats qu’ils connaissent&nbsp;: voir nos <a href="/fr/idees-repas-famille/">idées de repas en famille</a>. Cibello part de ce qui est chez vous, de vos allergies déclarées et de vos habitudes, et l’application apprend avec le temps ce que le foyer choisit d’habitude. Les filtres d’allergènes restent une aide à la décision, pas une garantie&nbsp;: la lecture de l’étiquette vous revient.</p>""",
            ),
            (
                "Réduire le gaspillage sans y penser",
                """<p>Une grande partie de ce qui finit à la poubelle dans une cuisine familiale est simplement oublié&nbsp;: la crème entamée, le demi-poireau, le reste de riz. Quand l’inventaire porte les dates, Cibello vous prévient discrètement quand un produit devrait être utilisé bientôt, et fait remonter les recettes qui l’utilisent. Le repas du soir devient le moyen le plus simple de <a href="/fr/reduire-gaspillage-alimentaire/">réduire le gaspillage alimentaire</a>, sans effort supplémentaire ni culpabilité. Pour savoir ce qui se mange encore après la date, lisez notre page sur la <a href="/fr/date-de-peremption/">date de péremption</a>.</p>""",
            ),
            (
                "Cinq habitudes qui tiennent dans la durée",
                """<ol><li>Enregistrez ce que vous avez une fois, puis mettez à jour après les courses en photographiant le ticket.</li><li>Laissez les suggestions partir de l’inventaire plutôt que d’une page blanche.</li><li>Planifiez trois à cinq dîners à la fois, pas sept. Laissez de la place aux restes et à l’imprévu.</li><li>Doublez les plats qui s’y prêtent et congelez la moitié en portions, comme expliqué dans le guide <a href="/fr/batch-cooking/">batch cooking</a>.</li><li>Vérifiez toujours vous-même les ingrédients, les allergènes et les dates&nbsp;: l’application est un soutien, pas une garantie.</li></ol>""",
            ),
        ],
        faq=[
            ("Qu’appelle-t-on repas du quotidien ?", "Des plats faisables un soir de semaine ordinaire : rapides, avec des produits que vous avez chez vous ou trouvez facilement, et qui se déclinent au fil de la semaine."),
            ("Comment trouver des recettes avec ce que j’ai dans le frigo ?", "Dans Cibello, vous photographiez le réfrigérateur, le congélateur et les placards ou scannez un ticket. L’application compare cet inventaire aux recettes et indique la part des ingrédients déjà chez vous. Vous vérifiez la lecture avant de l’enregistrer."),
            ("Cibello peut-il planifier toute la semaine ?", "Oui. Cibello propose un menu de la semaine qui varie les plats et les produits et place ce qui manque dans une liste de courses partagée. Vous relisez et modifiez la proposition vous-même."),
            ("Les suggestions tiennent-elles compte des allergies ?", "Vous pouvez indiquer vos allergies et habitudes alimentaires, mais le filtrage est une aide, pas une garantie. Vérifiez toujours les ingrédients et les emballages."),
        ],
    ),
    # ------------------------------------------------------------------
    "quick-dinner": dict(
        slug="/fr/diner-rapide/",
        label="Dîner rapide",
        title="Dîner rapide : à table en 20 à 30 minutes | Cibello",
        desc="Un dîner rapide avec ce que vous avez déjà : tableau de plats prêts en 15 à 30 minutes et méthode pour choisir en moins d’une minute.",
        eyebrow="Repas du soir en 20 à 30 minutes",
        h1="Dîner rapide : quoi cuisiner en 20 à 30 minutes avec ce que vous avez",
        lead="Le vrai frein d’un dîner rapide, ce n’est pas la recette, c’est l’ingrédient qui manque. Voici des plats qui se préparent presque toujours, et une méthode pour choisir en moins d’une minute.",
        sections=[
            (
                "Pourquoi les dîners rapides échouent",
                """<p>La plupart des recettes «&nbsp;express&nbsp;» supposent que tout est déjà dans la cuisine. En réalité, il manque souvent une ou deux choses, et les vingt minutes annoncées deviennent cinquante avec un passage au supermarché. L’autre problème classique, c’est la monotonie&nbsp;: les plats rapides finissent par se ressembler, pâtes, pâtes et encore pâtes. La solution tient en deux points&nbsp;: partir de ce que vous avez réellement, et confier la variété à autre chose que votre mémoire.</p><p>Il y a aussi la fatigue. À 19&nbsp;h, chercher une recette demande souvent plus d’énergie que la cuisiner. Un tableau de plats de secours affiché dans la cuisine et une application qui connaît le contenu de votre frigo enlèvent cette étape, et la soirée commence par un geste plutôt que par une hésitation.</p>""",
            ),
            (
                "Des plats simples que l’on peut presque toujours faire",
                """<div class="table-wrap"><table class="cmp"><caption>Dîners rapides et ce sur quoi ils reposent</caption><thead><tr><th scope="col">Plat</th><th scope="col">Temps</th><th scope="col">Base</th></tr></thead><tbody><tr><th scope="row">Pâtes avec ce qu’il y a dans le frigo</th><td>15 à 20 min</td><td>Pâtes, fromage, légumes, éventuellement lardons ou pois chiches</td></tr><tr><th scope="row">Omelette ou frittata</th><td>15 min</td><td>Œufs, restes de légumes, fromage</td></tr><tr><th scope="row">Poêlée de riz ou de nouilles</th><td>20 min</td><td>Demi-légumes, une protéine, sauce soja</td></tr><tr><th scope="row">Wraps ou tacos</th><td>20 min</td><td>Viande hachée, haricots ou poulet, galettes</td></tr><tr><th scope="row">Croque-monsieur et salade</th><td>15 min</td><td>Pain, jambon, fromage, salade verte</td></tr><tr><th scope="row">Soupe de légumes ou de lentilles</th><td>25 à 30 min</td><td>Placard et ce qui doit être consommé</td></tr><tr><th scope="row">Poisson au four avec légumes</th><td>25 min</td><td>Poisson surgelé, pommes de terre, citron</td></tr><tr><th scope="row">Curry rapide de poulet ou de pois chiches</th><td>25 à 30 min</td><td>Tomates concassées, lait de coco, épices</td></tr></tbody></table></div><p>Ce que ces plats ont en commun, c’est leur souplesse. Pas de poulet&nbsp;? Des haricots feront l’affaire. Pas de poivron&nbsp;? Une carotte convient. Cibello affiche les ingrédients que vous avez et ceux qui manquent, pour que vous voyiez tout de suite si la recette se fait telle quelle ou demande une adaptation de votre part.</p>""",
            ),
            (
                "Une idée de dîner en moins d’une minute",
                """<ol><li>Photographiez le frigo et les placards&nbsp;: l’application reconnaît les produits et construit votre inventaire. Vous vérifiez la lecture, car l’IA peut se tromper.</li><li>Demandez «&nbsp;qu’est-ce qu’on mange&nbsp;?&nbsp;» et parcourez des propositions qui partent de ce qui est chez vous et de ce qui doit être utilisé en premier.</li><li>Choisissez parmi les recettes qui ont la plus grande part d’ingrédients déjà présents.</li><li>Ajoutez les éventuels compléments à la <a href="/fr/liste-de-courses/">liste de courses</a>.</li></ol><p>Les suggestions tiennent aussi compte de ce qui arrive bientôt à sa date. Un dîner rapide qui sauve en même temps la crème entamée vaut double. Pour en savoir plus, lisez le guide sur la <a href="/fr/date-de-peremption/">date de péremption</a> et celui sur la <a href="/fr/reduire-gaspillage-alimentaire/">réduction du gaspillage alimentaire</a>.</p>""",
            ),
            (
                "Dîner rapide avec des enfants",
                """<p>Avec des enfants, le dîner rapide doit souvent aussi être familier. Pâtes à la sauce tomate, croque-monsieur, crêpes salées, poisson pané maison et gratin express fonctionnent pour une raison. L’astuce consiste à varier l’accompagnement et la protéine plutôt que le plat lui-même&nbsp;: les mêmes wraps avec du poulet une semaine, des haricots la suivante. D’autres pistes dans nos <a href="/fr/idees-repas-famille/">idées de repas en famille</a>, et pour ceux qui veulent voir plus loin qu’un soir, le <a href="/fr/planificateur-repas/">planificateur de repas</a> compose une semaine de plats rapides.</p>""",
            ),
            (
                "Le placard qui sauve la soirée",
                """<p>Un dîner rapide dépend moins du frigo que d’un fond de placard fiable&nbsp;: pâtes, riz, semoule, lentilles, tomates concassées, haricots en boîte, thon, œufs, oignons, ail, légumes surgelés et un fromage à râper. Avec cela, cinq dîners différents sont toujours possibles sans courses. Enregistrez ce placard dans Cibello une fois pour toutes&nbsp;: l’application saura ce qu’il reste, y compris la boîte oubliée au fond. Vous trouverez d’autres plats classés par temps dans nos <a href="/fr/idees-repas-semaine/">idées de repas pour la semaine</a>.</p>""",
            ),
            (
                "Rapide ne veut pas dire pressé",
                """<p>Le gain de temps ne vient pas de cuisiner plus vite, mais de ne plus chercher. Décider en une minute, cuisiner en vingt, et ne pas retourner au magasin&nbsp;: voilà la vraie économie. Quand l’inventaire est à jour, chaque soir commence par une réponse plutôt que par une question, et le passage à table devient un moment calme au lieu d’une négociation. La question «&nbsp;<a href="/fr/quoi-manger-ce-soir/">qu’est-ce qu’on mange ce soir&nbsp;?</a>&nbsp;» trouve ainsi une réponse avant même de se poser.</p>""",
            ),
        ],
        faq=[
            ("Qu’est-ce qu’un dîner rapide ?", "Un plat qui se prépare en vingt à trente minutes avec des produits déjà chez vous, sans passer par le magasin."),
            ("Comment trouver un dîner rapide avec ce que j’ai ?", "Photographiez le frigo et les placards dans Cibello. L’application compare l’inventaire aux recettes et montre les plats faisables maintenant, avec en tête ceux qui utilisent les produits à date courte."),
            ("Est-ce que je vois ce qui manque dans une recette ?", "Oui. Cibello indique pour chaque recette les ingrédients manquants. Vérifiez toujours les ingrédients et les allergènes vous-même."),
            ("Quels dîners rapides plaisent aux enfants ?", "Les pâtes à la sauce tomate, les croque-monsieur, les crêpes salées, les wraps et les gratins fonctionnent souvent. Variez l’accompagnement et la protéine plutôt que le plat."),
        ],
    ),
    # ------------------------------------------------------------------
    "family-dinner": dict(
        slug="/fr/idees-repas-famille/",
        label="Repas en famille",
        title="Idées repas famille : ce que les enfants mangent | Cibello",
        desc="Des idées de repas en famille que les enfants acceptent, un menu de la semaine sans négociation à 18 h et une liste de courses partagée.",
        eyebrow="Dîner avec des enfants",
        h1="Idées de repas en famille : des plats que les enfants acceptent",
        lead="Les enfants aiment ce qu’ils connaissent. Cela ne condamne pas la famille à manger la même chose chaque semaine : il suffit de varier à l’intérieur des plats qu’ils reconnaissent, et de décider à l’avance plutôt qu’à 18 h devant le frigo.",
        sections=[
            (
                "Des plats familiers qui se déclinent",
                """<p>Plutôt que de chercher des recettes une par une, raisonnez par familles de plats. Les enfants retrouvent une forme connue, vous changez la garniture, la sauce ou la protéine.</p><ul><li>Pâtes&nbsp;: sauce tomate, bolognaise, poulet à la crème, pesto, gratin au fromage et aux brocolis.</li><li>Wraps et tacos&nbsp;: viande hachée, poulet, haricots, poisson, chacun compose le sien.</li><li>Crêpes et galettes&nbsp;: jambon-fromage, épinards, ou en version sucrée-salée avec un peu de compote.</li><li>Boulettes et steaks&nbsp;: bœuf, volaille ou végétaux, avec purée, pommes de terre ou pâtes.</li><li>Plaque au four&nbsp;: saucisses ou poulet avec des légumes racines, tout sur la même plaque.</li><li>Soupes avec du pain&nbsp;: tomate, carotte, potiron, mixées pour les plus petits.</li><li>Gratins&nbsp;: pommes de terre, courgettes, pâtes, avec ou sans jambon.</li></ul>""",
            ),
            (
                "Un menu de la semaine pour la famille",
                """<p>Un menu de la semaine réduit les négociations dans les deux sens&nbsp;: les enfants savent ce qui arrive, et vous n’improvisez plus à 18&nbsp;h. Une structure qui fonctionne pour beaucoup de foyers&nbsp;: deux plats rapides que tout le monde aime, un plat nouveau, un soir de restes et un «&nbsp;dîner du vendredi&nbsp;» que chacun attend. Dans Cibello, vous placez les plats jour par jour, et ce qui manque rejoint la <a href="/fr/liste-de-courses/">liste de courses partagée</a>. Celui qui passe au magasin en rentrant voit la même liste que celui qui a planifié. Le <a href="/fr/planificateur-repas/">planificateur de repas</a> décrit la démarche en détail.</p>""",
            ),
            (
                "Rapide et économique sans sacrifier l’équilibre",
                """<p>Les familles ont rarement le temps de cuisiner longtemps en semaine, et l’alimentation pèse lourd dans le budget. La base est la même pour un <a href="/fr/diner-rapide/">dîner rapide</a> et pour une semaine économique&nbsp;: utiliser ce qu’il y a, planifier les restes et n’acheter que ce qui manque. Cibello affiche des valeurs nutritionnelles à titre indicatif au moment de planifier. Ce sont des estimations, pas un conseil diététique&nbsp;: pour des besoins particuliers, parlez-en au pédiatre ou à un professionnel de santé.</p><p>Concrètement, choisissez un soir de la semaine pour cuisiner en double un plat qui supporte la boîte, une bolognaise ou un curry doux, et gardez la moitié pour le lendemain ou le congélateur. Les soirs de sport ou de réunion tardive trouvent ainsi une réponse sans passer par la livraison. Et n’achetez que ce qui manque&nbsp;: un inventaire à jour évite les doublons de pâtes et de yaourts qui s’accumulent au fond du placard et finissent par dépasser leur date.</p>""",
            ),
            (
                "Allergies et enfants",
                """<p>Si un enfant a une allergie ou une intolérance, vous pouvez l’indiquer dans le profil du foyer pour que les suggestions soient filtrées. Ce filtrage est une aide, jamais une garantie. Lisez toujours la liste des ingrédients et vérifiez l’emballage, surtout quand une recette est modifiée ou qu’un produit est remplacé par un autre. Les informations affichées par l’application s’appuient sur ce que vous avez enregistré, et une lecture d’étiquette par l’IA peut contenir une erreur. La même vigilance vaut pour le goûter et le déjeuner emporté à l’école, où l’on pioche souvent dans le placard sans relire l’emballage.</p>""",
            ),
            (
                "Laisser les enfants participer",
                """<p>Un enfant qui choisit entre deux plats ou qui garnit lui-même son wrap arrive plus souvent de bonne humeur à table. L’application est réservée aux adultes, à partir de 18&nbsp;ans, mais le choix peut très bien se faire ensemble autour de la table de la cuisine, en montrant deux propositions. Cibello est conçu pour tout le foyer&nbsp;: chacun voit le même inventaire, le même menu et la même liste de courses, et les suggestions apprennent ce que vous aimez sans que quelqu’un doive tout garder en tête.</p>""",
            ),
            (
                "Le soir où rien n’est prévu",
                """<p>Il y aura toujours des soirs sans plan. Pour ceux-là, gardez trois plats de secours dont les ingrédients sont toujours à la maison&nbsp;: pâtes au thon et à la tomate, omelette avec du pain, crêpes salées. Et si l’inventaire est à jour dans Cibello, la question «&nbsp;<a href="/fr/quoi-manger-ce-soir/">qu’est-ce qu’on mange ce soir&nbsp;?</a>&nbsp;» trouve une réponse à partir de ce qu’il y a réellement dans le frigo, avec en premier ce qui doit être consommé. Les restes du dîner, rangés en boîtes, deviennent le déjeuner du lendemain&nbsp;: voir notre guide <a href="/fr/batch-cooking/">batch cooking</a>.</p>""",
            ),
        ],
        faq=[
            ("Quels repas plaisent généralement aux enfants ?", "Les pâtes, les wraps, les crêpes salées, les boulettes, les gratins et les plaques au four fonctionnent pour beaucoup d’enfants. Variez les sauces, les accompagnements et la protéine plutôt que le plat entier."),
            ("Comment faire un menu de la semaine pour la famille ?", "Choisissez deux plats rapides que tout le monde aime, un plat nouveau, un soir de restes et un dîner du week-end. Dans Cibello, vous placez les plats par jour et obtenez ce qui manque dans une liste de courses partagée."),
            ("Cibello peut-il tenir compte des allergies des enfants ?", "Vous pouvez indiquer les allergies dans le profil du foyer, mais le filtrage est une aide, pas une garantie. Vérifiez toujours les ingrédients et les emballages vous-même."),
            ("Les valeurs nutritionnelles sont-elles adaptées aux enfants ?", "Ce sont des estimations données à titre indicatif pour planifier, pas un conseil diététique. Pour des besoins particuliers, consultez un pédiatre ou un professionnel de santé."),
        ],
    ),
    # ------------------------------------------------------------------
    "meal-boxes": dict(
        slug="/fr/batch-cooking/",
        label="Batch cooking",
        title="Batch cooking : préparer ses repas de la semaine | Cibello",
        desc="Batch cooking simple : les plats qui supportent la boîte, les portions à planifier, la conservation au frigo et au congélateur, le suivi dans l’app.",
        eyebrow="Repas préparés à l’avance",
        h1="Batch cooking : des repas préparés à l’avance qui restent bons",
        lead="Cuisiner en double le dimanche pour manger tranquille le mardi : le batch cooking n’a rien de compliqué, à condition de choisir des plats qui supportent la boîte et de ne pas les oublier au fond du frigo.",
        sections=[
            (
                "Les plats qui supportent la boîte",
                """<p>Une bonne boîte-repas tient une journée ou deux au réfrigérateur et quelques minutes au micro-ondes sans devenir triste. Les plats mijotés, les currys, le chili, les salades de boulgour, de riz ou de lentilles, les lasagnes, les gratins de pâtes et les légumes racines rôtis avec une protéine sont des valeurs sûres. Ce qui est croustillant, la salade verte ou l’œuf au plat se transportent à part et s’ajoutent au moment de servir. Le geste le plus simple reste de doubler un plat ordinaire&nbsp;: les boîtes se remplissent sans effort supplémentaire. Notre page sur les <a href="/fr/repas-du-quotidien/">repas du quotidien</a> liste les plats qui s’y prêtent.</p><p>Pensez aussi aux céréales cuites à l’avance. Une grande casserole de riz, de quinoa ou de boulgour le dimanche devient la base de trois boîtes différentes dans la semaine, avec un légume rôti, une protéine et une sauce qui change à chaque fois. Le résultat ne ressemble pas à un reste, et le temps passé en cuisine se limite à l’assemblage.</p>""",
            ),
            (
                "Planifier les boîtes de la semaine",
                """<ol><li>Choisissez deux plats qui supportent la boîte et cuisinez-les en double le dimanche ou le lundi.</li><li>Variez l’accompagnement&nbsp;: le même curry avec du riz un jour, avec de la semoule et un yaourt le lendemain.</li><li>Congelez la moitié tout de suite. Les boîtes au frigo se mangent en deux ou trois jours&nbsp;; au congélateur, elles tiennent bien plus longtemps.</li><li>Enregistrez les boîtes dans l’inventaire de Cibello, pour savoir ce qu’il y a et ce qui doit être mangé en premier.</li></ol><p>Les restes saisis comme boîtes-repas font partie de l’inventaire quand vous planifiez les repas suivants&nbsp;: ils deviennent un élément du menu de la semaine au lieu d’une surprise découverte trop tard. Le <a href="/fr/planificateur-repas/">planificateur de repas</a> explique comment composer cette semaine.</p>""",
            ),
            (
                "Garder un œil sur le frigo et le congélateur",
                """<p>Le premier poste de gaspillage dans un foyer, c’est ce qu’on oublie. La boîte tout au fond du frigo est un classique. Dans Cibello, les boîtes-repas peuvent figurer dans votre inventaire, et l’application vous rappelle discrètement quand quelque chose devrait être consommé, sans jamais culpabiliser. Un doute sur la durée de conservation&nbsp;? Le guide sur la <a href="/fr/date-de-peremption/">date de péremption</a> explique la différence entre DLC et DDM&nbsp;; pour un plat cuisiné maison, l’odeur, l’aspect et le bon sens restent vos meilleurs alliés. Le rappel arrive avant que la boîte devienne un problème, pas après&nbsp;; à vous de décider si elle passe au congélateur ou dans l’assiette du soir.</p>""",
            ),
            (
                "Conservation et sécurité",
                """<ul><li>Refroidissez rapidement après cuisson et mettez au réfrigérateur dans les deux heures.</li><li>Réchauffez à cœur, jusqu’à ce que la boîte fume dans son ensemble.</li><li>Le riz et les pâtes cuits se refroidissent vite et se consomment dans les quelques jours.</li><li>Étiquetez les boîtes congelées avec le contenu et la date, ou laissez l’application s’en souvenir.</li><li>Ne recongelez pas un plat déjà décongelé.</li></ul><p>Les dates et les lectures de l’IA dans l’application sont un soutien. Vérifiez toujours par vous-même avant de manger, en particulier pour les enfants, les femmes enceintes et les personnes immunodéprimées.</p>""",
            ),
            (
                "Les boîtes et le budget",
                """<p>Le batch cooking coûte moins cher que les repas achetés le midi, mais son vrai avantage est ailleurs&nbsp;: il utilise les produits avant qu’ils ne se perdent. Un sac de carottes, un reste de poulet et une boîte de pois chiches deviennent quatre déjeuners. En planifiant la semaine dans Cibello, les ingrédients manquants sont ajoutés à la <a href="/fr/liste-de-courses/">liste de courses partagée</a>, et les boîtes préparées comptent dans l’inventaire. Vous achetez ce qui manque, pas ce que vous avez déjà, et vous contribuez sans y penser à <a href="/fr/reduire-gaspillage-alimentaire/">réduire le gaspillage alimentaire</a>.</p>""",
            ),
            (
                "Trois erreurs fréquentes",
                """<p>Préparer sept boîtes identiques et se lasser le mercredi&nbsp;: deux plats en alternance suffisent. Remplir le congélateur sans étiqueter&nbsp;: trois semaines plus tard, personne ne sait ce que contient la boîte givrée. Et oublier de compter les boîtes dans la planification&nbsp;: si le menu ignore les restes, ils finiront à la poubelle. Un inventaire partagé par tout le foyer règle ces trois points d’un seul geste, et chacun sait ce qu’il peut emporter le matin.</p>""",
            ),
        ],
        faq=[
            ("Quels plats se prêtent au batch cooking ?", "Plats mijotés, currys, chili, gratins, salades de boulgour, de riz ou de lentilles, et légumes rôtis avec une protéine supportent bien le frigo et le micro-ondes."),
            ("Combien de temps se conserve une boîte-repas au frigo ?", "Comptez deux à trois jours au réfrigérateur et bien plus longtemps au congélateur. Refroidissez vite, réchauffez à cœur et vérifiez toujours l’odeur et l’aspect."),
            ("Cibello peut-il suivre mes boîtes-repas ?", "Oui. Les boîtes peuvent être enregistrées dans l’inventaire, et l’application rappelle quand quelque chose devrait être mangé."),
            ("Les restes comptent-ils dans la planification ?", "Oui. Les restes saisis comme boîtes-repas font partie de l’inventaire et peuvent être pris en compte quand vous planifiez les repas suivants."),
        ],
    ),
    # ------------------------------------------------------------------
    "shopping-list": dict(
        slug="/fr/liste-de-courses/",
        label="Liste de courses",
        title="Liste de courses partagée avec tout le foyer | Cibello",
        desc="Une liste de courses partagée qui ne contient que ce qui manque, remplie depuis vos recettes et le menu de la semaine, visible par tout le foyer.",
        eyebrow="Courses sans doublons",
        h1="Liste de courses partagée : seulement ce qui manque vraiment",
        lead="La liste de courses classique s’écrit de mémoire, par une seule personne, et finit soit trop longue soit incomplète. Une liste qui part de votre inventaire et de vos recettes règle les deux problèmes.",
        sections=[
            (
                "Le problème des listes ordinaires",
                """<p>La plupart des listes de courses sont écrites de tête, souvent par une seule personne du foyer. Résultat&nbsp;: elles sont trop longues, avec des doublons de produits déjà dans le placard, ou trop courtes, avec l’ingrédient qui manque au moment de cuisiner. Les applications de listes partagées résolvent le partage, mais pas le lien avec ce qu’il y a réellement à la maison ni avec ce qui va être cuisiné. Quelqu’un doit encore tout garder en tête.</p>""",
            ),
            (
                "Comment fonctionne la liste de courses dans Cibello",
                """<ul><li><strong>Elle part de l’inventaire.</strong> Quand vous planifiez un plat, ses ingrédients sont comparés à ce qui est déjà dans le frigo, le congélateur et les placards. Seul ce qui manque est ajouté.</li><li><strong>Elle se remplit depuis le menu de la semaine.</strong> Quand vous planifiez les dîners de la semaine, tous les compléments se rassemblent dans une seule liste.</li><li><strong>Elle est partagée avec le foyer.</strong> Tous les membres voient la même liste et cochent les articles en magasin.</li><li><strong>Elle met l’inventaire à jour.</strong> Photographiez le ticket de caisse après les courses, et les produits reviennent dans l’inventaire.</li></ul><p>Vous pouvez bien sûr ajouter des articles à la main&nbsp;: lessive, café, ou ce qui «&nbsp;doit toujours être à la maison&nbsp;». Comme pour toute lecture par l’IA, vous vérifiez le ticket scanné avant de l’enregistrer.</p>""",
            ),
            (
                "Partager la liste dans le foyer",
                """<p>La fonction foyer de Cibello permet à plusieurs personnes de travailler sur le même inventaire, le même menu de la semaine et la même liste de courses. Celui qui rentre voit ce qui manque, celui qui planifie n’a plus à envoyer la liste par message. Chacun voit les modifications des autres, qu’il s’agisse d’un article ajouté à la dernière minute ou d’un produit déjà coché en rayon, ce qui évite les doubles achats du samedi. Pendant la période d’essai de 14 jours, puis avec un abonnement, le foyer partage cette vue d’ensemble. Les données sont stockées dans l’Union européenne, et le compte peut être supprimé depuis l’application&nbsp;; les détails figurent dans notre <a href="/fr/privacy/">politique de confidentialité</a>.</p>""",
            ),
            (
                "Une liste qui réduit le gaspillage et la dépense",
                """<p>Quand la liste ne contient que ce qui manque, la plupart des doublons disparaissent. Quand les plats qui utilisent les produits à date courte sont planifiés en premier, le gaspillage recule. C’est le même principe que dans notre guide pour <a href="/fr/reduire-gaspillage-alimentaire/">réduire le gaspillage alimentaire</a>&nbsp;: la vue d’ensemble avant les courses. Un tour au magasin avec une liste précise est aussi plus court, et laisse moins de place aux achats que l’on regrette une fois rentré.</p><p>Un exemple concret&nbsp;: le menu de la semaine prévoit un curry de pois chiches, une omelette et des pâtes au thon. L’inventaire montre déjà les pois chiches, le lait de coco, les œufs et le thon&nbsp;; la liste ne réclame que les épinards, un citron et de la crème. Sans cette comparaison, la moitié de ces produits aurait été rachetée, et la boîte de pois chiches déjà en stock aurait attendu encore un an.</p>""",
            ),
            (
                "Une routine de courses en quatre gestes",
                """<ol><li>Le dimanche, ou le jour qui vous convient, relisez le menu de la semaine proposé par le <a href="/fr/planificateur-repas/">planificateur de repas</a> et ajustez-le.</li><li>Laissez la liste se compléter avec ce qui manque, puis ajoutez les produits hors alimentation.</li><li>Au magasin, chacun coche ce qu’il met dans le panier&nbsp;; la liste se met à jour pour tous.</li><li>De retour, photographiez le ticket. L’inventaire est à jour pour les suggestions du lendemain.</li></ol>""",
            ),
            (
                "Ce que la liste ne fait pas",
                """<p>Elle ne devine pas ce que vous n’avez pas enregistré&nbsp;: si le frigo n’a pas été photographié depuis trois semaines, la liste proposera peut-être un produit que vous avez déjà. Elle ne remplace pas non plus la lecture de l’étiquette&nbsp;: les filtres d’allergènes sont une aide, pas une garantie. Un inventaire à jour et un coup d’œil avant de valider suffisent à en tirer le meilleur. Pour voir comment la liste s’articule avec les <a href="/fr/repas-du-quotidien/">repas du quotidien</a>, commencez par une semaine simple de quatre dîners.</p>""",
            ),
        ],
        faq=[
            ("Tout le foyer peut-il voir la même liste de courses ?", "Oui. La fonction foyer de Cibello partage l’inventaire, le menu de la semaine et la liste de courses entre les membres."),
            ("La liste se remplit-elle automatiquement ?", "Oui. Quand vous planifiez des recettes ou un menu de la semaine, les ingrédients absents de l’inventaire sont ajoutés à la liste."),
            ("Puis-je ajouter mes propres articles ?", "Oui, tout peut être ajouté à la main, y compris ce qui n’est pas alimentaire."),
            ("L’inventaire est-il mis à jour après les courses ?", "Vous pouvez photographier le ticket de caisse ou scanner des codes-barres pour que les produits entrent dans l’inventaire. Vérifiez le résultat, car l’IA peut se tromper."),
        ],
    ),
    # ------------------------------------------------------------------
    "best-before": dict(
        slug="/fr/date-de-peremption/",
        label="DLC et DDM",
        title="Date de péremption : DLC ou DDM, que faire ? | Cibello",
        desc="DLC et DDM : la différence entre « à consommer jusqu’au » et « de préférence avant », un tableau de durées indicatives et une méthode pour ne rien oublier.",
        eyebrow="Comprendre les dates sur l’emballage",
        h1="Date de péremption : DLC, DDM et ce que vous pouvez encore manger",
        lead="Deux mentions se côtoient sur les emballages et ne veulent pas dire la même chose. L’une est une limite de sécurité, l’autre une indication de qualité. Les confondre remplit la poubelle ou, à l’inverse, fait prendre des risques inutiles.",
        sections=[
            (
                "La DDM&nbsp;: «&nbsp;à consommer de préférence avant&nbsp;» est une indication de qualité",
                """<p>La date de durabilité minimale, ou DDM, indique jusqu’à quand le fabricant garantit toutes les qualités du produit&nbsp;: goût, texture, valeur nutritionnelle. Elle se lit «&nbsp;à consommer de préférence avant le&nbsp;» ou «&nbsp;avant fin&nbsp;». Après cette date, le produit reste souvent tout à fait consommable, à condition d’avoir été conservé correctement et que l’emballage soit intact. C’est le cas des pâtes, du riz, des conserves, du café, des biscuits, du chocolat, des produits surgelés, mais aussi de beaucoup de yaourts, de fromages à pâte dure et du lait UHT. Regardez, sentez, goûtez&nbsp;: c’est la méthode que rappellent les autorités sanitaires françaises. Depuis 2022, certains emballages ajoutent une mention du type «&nbsp;ce produit peut être consommé après cette date&nbsp;», précisément pour limiter le gaspillage.</p>""",
            ),
            (
                "La DLC&nbsp;: «&nbsp;à consommer jusqu’au&nbsp;» est une limite de sécurité",
                """<p>La date limite de consommation, ou DLC, figure sur les produits sensibles où des bactéries peuvent se développer sans que l’aliment sente ou paraisse mauvais&nbsp;: viande fraîche, viande hachée, poisson frais, charcuterie à la coupe, plats préparés frais, certains produits laitiers frais. Elle se lit «&nbsp;à consommer jusqu’au&nbsp;». Passé cette date, le produit ne doit pas être consommé. Le plus sûr est de le cuisiner ou de le congeler au plus tard le jour indiqué. La congélation arrête l’horloge&nbsp;: un produit congelé avant sa DLC peut être cuisiné après décongélation. Ces règles de marquage sont fixées par le règlement européen sur l’information des consommateurs et s’appliquent donc de la même manière dans toute l’Union.</p>""",
            ),
            (
                "Combien de temps se conservent les aliments courants&nbsp;?",
                """<div class="table-wrap"><table class="cmp"><caption>Repères de conservation après la DDM, emballage intact et bien conservé</caption><thead><tr><th scope="col">Aliment</th><th scope="col">Repère après la DDM</th><th scope="col">Remarque</th></tr></thead><tbody><tr><th scope="row">Lait UHT</th><td>Quelques jours à une semaine</td><td>Sentez et goûtez&nbsp;; le lait tourné se reconnaît</td></tr><tr><th scope="row">Yaourts et fromage blanc</th><td>Souvent une à plusieurs semaines</td><td>L’acidité protège&nbsp;; vérifiez l’absence de moisissure</td></tr><tr><th scope="row">Œufs</th><td>Plusieurs semaines</td><td>Un œuf qui flotte dans l’eau se jette</td></tr><tr><th scope="row">Fromage à pâte dure</th><td>Des semaines à des mois</td><td>Retirez la partie moisie en surface</td></tr><tr><th scope="row">Conserves et produits secs</th><td>Des mois à des années</td><td>Jetez les boîtes bombées ou cabossées</td></tr><tr><th scope="row">Produits surgelés</th><td>Des mois</td><td>La qualité baisse, la sécurité reste</td></tr><tr><th scope="row">Viande hachée ou poulet cuits</th><td>2 à 3 jours au réfrigérateur</td><td>Plat cuisiné&nbsp;: refroidir vite, réchauffer à cœur</td></tr><tr><th scope="row">Riz et pâtes cuits</th><td>Quelques jours au réfrigérateur</td><td>Refroidir rapidement après cuisson</td></tr></tbody></table></div><p>Ce tableau donne des repères, pas des règles. Suivez toujours les indications de l’emballage et vos propres sens, et soyez plus prudent pour les aliments destinés aux enfants, aux femmes enceintes et aux personnes immunodéprimées. Les produits marqués d’une DLC ne relèvent pas de ce tableau.</p>""",
            ),
            (
                "Le vrai problème, c’est la mémoire",
                """<p>La difficulté n’est pas la règle, c’est de se souvenir. Dans Cibello, les produits de votre inventaire portent leur date, saisie depuis un ticket de caisse, un code-barres ou ce que vous avez photographié, et l’application vous prévient discrètement quand quelque chose devrait être utilisé bientôt. Les suggestions de repas font alors remonter les recettes qui utilisent justement ces produits. <a href="/fr/reduire-gaspillage-alimentaire/">Réduire le gaspillage</a> devient un effet secondaire du dîner. Une date peut être mal lue par l’IA, vous vérifiez donc toujours vous-même. Le rappel est discret et ne juge pas&nbsp;: il signale qu’un produit approche de sa date et propose un plat pour l’utiliser, la décision vous appartient. L’application ne se substitue pas à l’emballage&nbsp;; c’est à vous de distinguer une DLC d’une DDM au moment de trancher.</p>""",
            ),
            (
                "Ranger pour ne rien perdre",
                """<p>Quelques gestes simples complètent l’application. Placez les produits à date courte devant, les nouveaux achats derrière. Gardez la viande et le poisson dans la zone la plus froide du réfrigérateur. Transvasez les restes dans des boîtes transparentes et notez la date&nbsp;; notre guide <a href="/fr/batch-cooking/">batch cooking</a> détaille la conservation des plats maison. Et faites un rapide inventaire avant de partir en courses plutôt qu’après&nbsp;: c’est là que se décident les doublons. La <a href="/fr/liste-de-courses/">liste de courses partagée</a> s’appuie justement sur ce que vous avez déjà. Enfin, ouvrez le congélateur avec la même logique&nbsp;: un sac de légumes surgelés entamé depuis des mois reste sûr mais perd du goût, autant le finir dans une soupe ou une poêlée cette semaine.</p>""",
            ),
        ],
        faq=[
            ("Quelle est la différence entre DLC et DDM ?", "La DDM (« à consommer de préférence avant ») est une indication de qualité : le produit reste souvent consommable après, s’il a été bien conservé. La DLC (« à consommer jusqu’au ») est une limite de sécurité pour les produits sensibles comme la viande et le poisson frais, à ne pas dépasser."),
            ("Peut-on manger un produit après la DDM ?", "Souvent oui. Regardez, sentez, goûtez. Cela ne vaut pas pour les produits marqués d’une DLC."),
            ("Combien de temps le lait se conserve-t-il après la date ?", "Le lait UHT non ouvert et conservé au frais reste souvent bon quelques jours à une semaine après la DDM. L’odeur et le goût décident. Le lait frais pasteurisé porte généralement une DLC, à respecter."),
            ("Une application peut-elle me prévenir avant que la nourriture se perde ?", "Oui. Cibello garde les dates dans l’inventaire, vous prévient quand un produit devrait être utilisé et propose des recettes qui l’emploient. Vérifiez toujours les dates vous-même."),
        ],
    ),
    # ------------------------------------------------------------------
    "weekday-dinners": dict(
        slug="/fr/idees-repas-semaine/",
        label="Idées repas semaine",
        title="Idées repas semaine : 25 dîners classés par temps | Cibello",
        desc="25 idées de repas pour la semaine, classées par temps : prêts en 15, 25 ou 30 minutes avec des produits que vous avez souvent déjà chez vous.",
        eyebrow="Du lundi au jeudi",
        h1="Idées repas de la semaine : 25 dîners classés par temps",
        lead="Un soir de semaine, la question n’est pas « quoi de nouveau ? » mais « qu’est-ce qui se fait en trente minutes avec ce qu’il y a ? ». Voici 25 réponses, du plus rapide au plus tranquille.",
        sections=[
            (
                "Prêt en 15 minutes",
                """<p>Ces plats reposent sur un fond de placard et deux ou trois produits frais. Pas de découpe longue, pas de cuisson à surveiller&nbsp;: le temps indiqué compte du premier geste à l’assiette.</p><ul><li>Pâtes au thon, crème et citron.</li><li>Riz sauté aux œufs et légumes surgelés, sauce soja.</li><li>Pizza sur tortilla&nbsp;: galette, sauce tomate, fromage et ce qu’il reste.</li><li>Pâtes au pesto et au poulet, avec un reste de poulet ou un rôti du commerce.</li><li>Omelette au fromage et aux légumes&nbsp;: sauve les œufs et les demi-légumes.</li><li>Croque-monsieur et salade verte.</li><li>Tartines chaudes au chèvre, miel et noix, avec une salade.</li></ul>""",
            ),
            (
                "Prêt en 20 à 25 minutes",
                """<p>Ici, une cuisson démarre pendant que le reste se prépare&nbsp;: l’eau des pâtes, le four qui chauffe, le riz. Le geste clé est de lancer en premier ce qui prend le plus de temps.</p><ul><li>Saucisses à la moutarde et purée.</li><li>Poêlée de poulet aux nouilles et légumes.</li><li>Wraps à la viande hachée, au poulet ou aux haricots.</li><li>Pâtes à la carbonara.</li><li>Saumon au four, pommes de terre et citron.</li><li>Falafels en pain pita avec sauce au yaourt.</li><li>Soupe de tomate et tartines grillées au fromage.</li><li>Pois chiches mijotés aux épinards.</li><li>Poêlée de restes&nbsp;: pommes de terre, oignon, reste de viande ou de légumes.</li><li>Bowl de saumon, riz et avocat.</li></ul>""",
            ),
            (
                "Prêt en 30 minutes",
                """<p>Trente minutes suffisent pour un mijoté court, un gratin ou une soupe complète, et pour cuisiner en double si vous voulez des boîtes pour le lendemain.</p><ul><li>Poulet à la crème et aux champignons.</li><li>Soupe de lentilles et pain grillé.</li><li>Chili sin carne.</li><li>Curry de poulet au lait de coco, à doubler pour des boîtes-repas.</li><li>Boulettes de viande et purée.</li><li>Plaque au four de saucisses et légumes racines.</li><li>Gratin de pâtes aux brocolis et au fromage.</li><li>Galettes de haricots rouges et pommes de terre.</li></ul><p>D’autres plats rapides, avec un tableau des temps et des ingrédients, dans le guide <a href="/fr/diner-rapide/">dîner rapide</a>. Des enfants à table&nbsp;? Voir les <a href="/fr/idees-repas-famille/">idées de repas en famille</a>.</p>""",
            ),
            (
                "L’astuce&nbsp;: laisser le frigo choisir",
                """<p>Tous les plats ci-dessus supposent que les ingrédients sont bien à la maison. C’est là que le dîner de semaine déraille d’habitude&nbsp;: on choisit le plat, puis on découvre qu’il n’y a plus de poivron. Cibello inverse l’ordre. Photographiez le frigo et les placards, l’application sait ce qu’il y a, et les idées de repas sont classées selon la part des ingrédients que vous possédez, avec en tête ce qui arrive bientôt à sa date. Quatre soirs de semaine deviennent un menu dans le <a href="/fr/planificateur-repas/">planificateur de repas</a>, et ce qui manque rejoint une <a href="/fr/liste-de-courses/">liste de courses partagée</a>. Vous vérifiez la lecture de la photo, car l’IA peut se tromper, et vous restez maître du menu.</p>""",
            ),
            (
                "La rotation vaut mieux que l’inspiration",
                """<p>La plupart des foyers font tourner dix à quinze plats, et ce n’est pas un problème. Pour varier, changez la protéine et l’accompagnement plutôt que le plat entier&nbsp;: le même mijoté avec du poulet une semaine et des pois chiches la suivante, les mêmes wraps avec du poisson à la place de la viande hachée. Cibello apprend ce que vous choisissez d’habitude et propose des variantes proches de vos favoris, à partir de ce qui est chez vous en ce moment. Pour l’approche complète, lisez la page sur les <a href="/fr/repas-du-quotidien/">repas du quotidien</a>.</p>""",
            ),
            (
                "Un soir de restes chaque semaine",
                """<p>Prévoyez un soir sans recette, où l’on finit ce qui reste&nbsp;: le fond de curry, le riz cuit, les légumes rôtis, une omelette pour lier le tout. Ce soir-là allège le budget, vide le frigo avant les courses et évite qu’une boîte oubliée finisse à la poubelle. Si les restes sont enregistrés dans l’inventaire de Cibello, l’application les compte quand elle propose la suite, et vous prévient en douceur quand ils doivent être mangés. Le guide <a href="/fr/batch-cooking/">batch cooking</a> explique comment les conserver correctement.</p><p>Et le vendredi&nbsp;? Ce soir-là mérite un peu plus de temps et un plat que tout le monde attend&nbsp;: burgers maison, raclette improvisée ou lasagnes. Le reste de la semaine peut rester simple précisément parce qu’un soir sort de l’ordinaire.</p>""",
            ),
        ],
        faq=[
            ("Quelles sont de bonnes idées de repas pour la semaine ?", "Des plats en 15 à 30 minutes avec des produits souvent déjà là : pâtes, omelette, poêlées, wraps, soupes, mijotés et plaques au four. La liste ci-dessus en donne 25."),
            ("Comment trouver des idées de repas avec ce que j’ai ?", "Photographiez le frigo et les placards dans Cibello. L’application classe plus de 9 000 recettes selon la part des ingrédients déjà chez vous."),
            ("Comment varier les repas de la semaine ?", "Changez la protéine et l’accompagnement plutôt que le plat, planifiez trois ou quatre dîners à la fois et gardez un soir de restes."),
            ("Cibello propose-t-il un menu pour toute la semaine ?", "Oui. Cibello peut proposer un menu de la semaine qui varie les plats et les produits et place ce qui manque dans une liste de courses partagée. Vous le relisez et le modifiez."),
        ],
    ),
    # ------------------------------------------------------------------
    "what-to-eat-tonight": dict(
        slug="/fr/quoi-manger-ce-soir/",
        label="Quoi manger ce soir&nbsp;?",
        title="Qu’est-ce qu’on mange ce soir ? Réponse rapide | Cibello",
        desc="Qu’est-ce qu’on mange ce soir ? Un sélecteur de dîner gratuit parmi quarante plats du quotidien et une méthode pour ne plus se poser la question.",
        eyebrow="La question de 18 h",
        h1="Qu’est-ce qu’on mange ce soir ?",
        lead="Décider quoi cuisiner, c’est jongler avec quatre choses à la fois : ce qu’il y a, le temps disponible, ce que chacun mangera et ce qui doit être consommé avant de se perdre. Le sélecteur ci-dessous tranche en dix secondes ; le reste de la page explique comment ne plus avoir à y penser.",
        sections=[
            (
                "Pourquoi la question est si difficile",
                """<p>Choisir le dîner suppose de tenir quatre variables en même temps&nbsp;: ce qu’il y a dans la cuisine, le temps et l’énergie qui restent, ce que les personnes à table accepteront, et ce qui doit être utilisé avant de se gâter. Faire ce calcul de tête tous les soirs est une vraie charge mentale. La plupart des gens retombent sur les mêmes trois plats ou sur la livraison, non par manque d’idées, mais parce que décider fatigue. Le sélecteur ci-dessus tire au sort parmi quarante plats du quotidien&nbsp;; il ne demande aucun compte et ne sait rien de votre frigo. Dans l’application, les suggestions partent au contraire de ce que vous avez réellement.</p>""",
            ),
            (
                "Trois questions qui donnent la réponse",
                """<ol><li><strong>Qu’y a-t-il à la maison qui doit être utilisé&nbsp;?</strong> Commencez par le frigo, pas par le livre de recettes. Le produit à date courte oriente le choix.</li><li><strong>Combien de temps et d’énergie reste-t-il&nbsp;?</strong> Moins de vingt minutes&nbsp;: pâtes, omelette, poêlée, wraps. Plus de temps&nbsp;: mijoté, plaque au four, soupe.</li><li><strong>Qui mange&nbsp;?</strong> Des enfants, des invités ou vous seul&nbsp;: cela décide du degré de familiarité ou d’ambition du plat.</li></ol><p>Cibello pose ces trois questions à votre place. L’application sait ce que vous avez, vous indiquez le contexte, et chaque proposition vient avec son explication&nbsp;: «&nbsp;parce que vous avez du poulet et de la crème qui arrivent à leur date&nbsp;». Voyez aussi comment les familles s’en sortent avec nos <a href="/fr/idees-repas-famille/">idées de repas en famille</a> et le guide du <a href="/fr/diner-rapide/">dîner rapide en 20 à 30 minutes</a>.</p>""",
            ),
            (
                "Partir du frigo, pas de la recette",
                """<p>Photographiez le réfrigérateur, le congélateur et les placards, ou scannez un ticket de caisse&nbsp;: l’application reconnaît les produits, note où ils se trouvent et construit votre inventaire, que vous relisez avant d’enregistrer parce que l’IA peut mal lire. Quand vous demandez «&nbsp;qu’est-ce qu’on mange&nbsp;?&nbsp;», cet inventaire est comparé à plus de 9&nbsp;000 recettes, classées selon la part des ingrédients déjà chez vous. Un plat dont vous avez 90&nbsp;% des ingrédients arrive en tête. Pour chaque recette, vous voyez ce qui manque, et vous décidez si elle se fait telle quelle ou avec une adaptation. Le guide <a href="/fr/recettes-avec-ingredients/">recettes avec vos ingrédients</a> approfondit ce fonctionnement.</p>""",
            ),
            (
                "Quoi cuisiner quand «&nbsp;il n’y a rien&nbsp;»",
                """<p>Vous avez presque toujours plus que vous ne le pensez. Des pâtes, du riz ou de la semoule, des œufs, une boîte de tomates concassées, une boîte de haricots ou de pois chiches, un oignon, des légumes surgelés et un morceau de fromage suffisent à cinq dîners&nbsp;: pâtes à la tomate et aux haricots, omelette, riz sauté, soupe de lentilles, pizza sur tortilla. Nos <a href="/fr/idees-repas-semaine/">idées de repas pour la semaine</a> en donnent vingt-cinq, classées par temps. Un inventaire enregistré dans Cibello montre en plus exactement ce qu’il reste, y compris ce que vous aviez oublié au fond du placard.</p>""",
            ),
            (
                "Quoi servir quand on reçoit",
                """<p>Avec des invités, les règles changent&nbsp;: choisissez un plat qui se prépare à l’avance (mijoté, lasagnes, poulet rôti), qui supporte d’attendre et que vous avez déjà cuisiné. Gardez votre énergie pour les accompagnements et la table. Un plat que vous connaissez laisse aussi le temps de discuter au lieu de surveiller la casserole, et une entrée simple, une salade ou une soupe froide, suffit à marquer l’occasion. Si vous planifiez déjà la semaine dans l’application, ce qui manque part dans la <a href="/fr/liste-de-courses/">liste de courses partagée</a>, et les restes deviennent les <a href="/fr/batch-cooking/">boîtes-repas</a> du lundi.</p>""",
            ),
            (
                "Ne plus se poser la question",
                """<p>Celui qui planifie trois à cinq dîners à la fois ne se retrouve plus devant le frigo à 18&nbsp;h. Un menu de la semaine qui utilise les produits dans le bon ordre, une liste de courses partagée et des rappels discrets avant qu’un aliment se perde suppriment à la fois la décision et le gaspillage. C’est ce que fait Cibello, avec un essai de 14 jours sans carte bancaire, pour les adultes à partir de 18&nbsp;ans. Le <a href="/fr/planificateur-repas/">planificateur de repas</a> explique comment démarrer, et la page <a href="/fr/repas-du-quotidien/">repas du quotidien</a> montre comment en faire une habitude.</p>""",
            ),
        ],
        faq=[
            ("Que manger ce soir quand on n’a aucune inspiration ?", "Utilisez le sélecteur ci-dessus ou partez de ce qu’il y a : pâtes, omelette, poêlée, wraps, soupe ou plaque au four couvrent la plupart des soirs. Cibello propose des plats à partir de votre inventaire."),
            ("Que manger ce soir en version végétarienne ?", "Soupe de lentilles, chili sin carne, pois chiches mijotés, galettes de haricots, salade de boulgour et feta, gratin de pâtes aux brocolis ou falafels en pita. Tous se font en moins de trente minutes avec des produits de placard."),
            ("Que cuisiner ce soir avec ce que j’ai chez moi ?", "Enregistrez le frigo et les placards dans Cibello en les photographiant. L’application classe plus de 9 000 recettes selon la part des ingrédients déjà chez vous et indique ce qui manque."),
            ("Comment arrêter de réfléchir au dîner chaque jour ?", "Planifiez trois à cinq dîners à la fois dans un menu de la semaine, laissez la liste de courses se compléter avec ce qui manque et utilisez d’abord les produits à date courte."),
        ],
    ),
}

# Sélecteur de dîner (rendu par le générateur, alimenté par middag.js).
TOOL = dict(
    heading="Le sélecteur de dîner : une idée en 10 secondes",
    protein_label="Protéine",
    time_label="Temps",
    mode_label="Envie",
    protein={"any": "Peu importe", "chicken": "Poulet", "meat": "Viande", "fish": "Poisson", "veg": "Végétarien"},
    time={"20": "20 min max", "30": "30 min max", "45": "45 min max", "90": "Peu importe"},
    mode={
        "all": "Tout",
        "quick": "Rapide",
        "leftovers": "Avec des restes",
        "pantry": "Placard seulement",
        "budget": "Économique",
        "kids": "Pour les enfants",
        "mealbox": "Donne des boîtes-repas",
        "friday": "Soir de fête",
    },
    button="Tirer un dîner au sort",
    no_match="Aucun plat ne correspond. Essayez d’assouplir un filtre.",
    minutes="min",
    any_protein="protéine au choix",
    tip="Vous avez ça chez vous ? Dans l’application, les suggestions partent de ce qui est réellement dans votre frigo.",
    note="Le sélecteur tire au sort parmi quarante plats du quotidien et ne demande aucun compte. Dans l’application, les propositions partent de ce qu’il y a vraiment dans votre frigo.",
    dishes=[
        ("Pâtes à la sauce tomate et aux haricots blancs", "veg", 20, ["pantry", "budget", "kids"]),
        ("Poulet à la crème et aux champignons", "chicken", 30, ["kids", "leftovers"]),
        ("Omelette aux restes de légumes", "veg", 15, ["leftovers", "budget", "quick"]),
        ("Poêlée de nouilles avec ce qu’il y a dans le frigo", "any", 20, ["leftovers", "quick"]),
        ("Wraps à la viande hachée ou aux haricots", "any", 20, ["kids", "friday"]),
        ("Soupe de lentilles et pain grillé", "veg", 30, ["pantry", "budget", "mealbox"]),
        ("Saumon au four, pommes de terre et citron", "fish", 25, ["quick"]),
        ("Curry de poulet au lait de coco et riz", "chicken", 30, ["mealbox", "leftovers"]),
        ("Crêpes salées jambon-fromage", "meat", 25, ["kids", "budget"]),
        ("Boulettes de viande et purée", "meat", 30, ["kids"]),
        ("Plaque au four de saucisses et légumes racines", "meat", 30, ["budget", "kids"]),
        ("Gratin de poisson aux poireaux et pommes de terre", "fish", 35, ["kids"]),
        ("Chili sin carne", "veg", 30, ["pantry", "mealbox", "budget"]),
        ("Pâtes à la carbonara", "meat", 20, ["quick", "kids", "pantry"]),
        ("Salade de boulgour au poulet ou à la feta", "any", 20, ["quick", "mealbox"]),
        ("Poêlée de pommes de terre aux restes", "any", 20, ["leftovers", "budget"]),
        ("Soupe de tomate et tartines grillées au fromage", "veg", 25, ["kids", "budget"]),
        ("Wraps de poulet, sauce au yaourt", "chicken", 20, ["quick", "kids"]),
        ("Lasagnes (double portion pour des boîtes-repas)", "meat", 60, ["mealbox", "kids"]),
        ("Riz sauté aux œufs et légumes", "veg", 15, ["leftovers", "quick", "budget"]),
        ("Soupe de poisson au safran et croûtons", "fish", 30, ["friday"]),
        ("Pois chiches mijotés aux épinards et yaourt", "veg", 25, ["pantry", "budget"]),
        ("Gratin de pâtes aux brocolis et au fromage", "veg", 35, ["kids", "mealbox"]),
        ("Burgers maison et potatoes au four", "meat", 35, ["friday", "kids"]),
        ("Pâtes aux crevettes, ail et citron", "fish", 20, ["quick", "friday"]),
        ("Saucisses à la moutarde et riz", "meat", 25, ["kids", "budget", "quick"]),
        ("Pizza sur tortilla avec ce qu’il reste", "any", 15, ["leftovers", "pantry", "kids"]),
        ("Poulet rôti aux légumes racines", "chicken", 45, ["friday"]),
        ("Falafels en pain pita", "veg", 20, ["quick", "budget"]),
        ("Bowl de saumon, riz et avocat", "fish", 20, ["quick"]),
        ("Galettes de haricots rouges et pommes de terre", "veg", 30, ["budget", "kids"]),
        ("Pâtes au pesto et au poulet", "chicken", 15, ["quick", "kids"]),
        ("Hachis parmentier", "meat", 45, ["mealbox", "kids", "leftovers"]),
        ("Pâtes au thon, crème et citron", "fish", 15, ["pantry", "quick", "budget"]),
        ("Croque-monsieur et salade verte", "meat", 15, ["quick", "kids", "budget"]),
        ("Quiche sans pâte aux légumes du frigo", "veg", 35, ["leftovers", "budget"]),
        ("Soupe de poulet aux vermicelles", "chicken", 25, ["leftovers", "quick"]),
        ("Raclette improvisée avec ce qu’il y a dans le frigo", "any", 30, ["friday", "leftovers"]),
        ("Lasagnes de légumes", "veg", 50, ["mealbox", "friday"]),
        ("Dos de cabillaud, beurre citronné et pommes de terre vapeur", "fish", 25, ["kids"]),
    ],
)
