"""Contenu français pour cibello.app. Structure : voir _schema.py."""

LANG = "fr"

# ---------------------------------------------------------------------------
# Guides
# ---------------------------------------------------------------------------

GUIDES = {
    "/fr/planificateur-repas/": dict(
        title="Planificateur de repas pour une semaine variée | Cibello",
        desc="Un menu de la semaine qui part de votre frigo et de vos placards, varie les repas et remplit la liste de courses avec ce qui manque vraiment.",
        eyebrow="Votre menu de la semaine",
        h1="Planificateur de repas pour une semaine variée",
        lead="Décider quoi manger chaque soir coûte plus d’énergie que cuisiner. Cibello vous aide à composer un menu de la semaine à partir de ce qui est déjà dans votre cuisine, puis vous relisez, déplacez et validez chaque repas.",
        sections=[
            (
                "Pourquoi planifier la semaine plutôt que chaque soir",
                """<p>À 17&nbsp;h, la question «&nbsp;qu’est-ce qu’on mange ce soir&nbsp;?&nbsp;» tombe rarement au bon moment. On ouvre le frigo, on hésite, on finit par commander ou par refaire les mêmes pâtes. Un menu de la semaine déplace cette décision vers un moment plus calme, le dimanche soir par exemple, et la prend une seule fois pour sept jours. Le bénéfice ne tient pas à la perfection du planning, mais au fait de ne plus y réfléchir en rentrant du travail.</p><p>Un planificateur de repas comme Cibello ne vous impose rien. Il propose une semaine, vous la relisez et vous gardez ce qui vous convient. Le reste de cette page explique comment cette proposition se construit et comment en faire une habitude qui tient dans la durée.</p>""",
            ),
            (
                "Partir de ce qu’il y a déjà dans la cuisine",
                """<p>La plupart des applications de recettes commencent par les recettes. Cibello commence par votre cuisine. Vous photographiez le réfrigérateur, le congélateur et les placards&nbsp;; l’application reconnaît les produits et note où ils se trouvent. Vous pouvez aussi scanner un ticket de caisse après les courses ou un code-barres. Comme l’IA peut se tromper, vous vérifiez toujours le résultat avant qu’il soit enregistré&nbsp;: un yaourt mal lu ou une date incertaine se corrige en quelques secondes.</p><p>Cet inventaire devient la base du menu. Les recettes sont classées selon la part des ingrédients déjà présents chez vous, ce qui évite le scénario classique où l’on choisit un plat avant de découvrir qu’il manque la moitié des ingrédients. Pour aller plus loin sur ce point, lisez le guide <a href="/fr/recettes-avec-ingredients/">recettes avec les ingrédients déjà chez vous</a>.</p>""",
            ),
            (
                "De la variété sans complication",
                """<p>Un bon menu de la semaine ne sert pas le même plat au déjeuner et au dîner, et ne répète pas le même ingrédient principal trois jours de suite. Cibello varie les plats, les ingrédients et les types de repas quand il compose la proposition. Vous voyez ensuite pourquoi une recette a été suggérée&nbsp;: parce que les courgettes doivent être mangées cette semaine, parce que le foyer choisit souvent ce genre de plat, ou simplement parce que presque tout est déjà là.</p><p>Avant que la semaine commence, vous relisez le planning. Un plat ne vous inspire pas&nbsp;? Remplacez-le. Une soirée s’annonce chargée&nbsp;? Mettez-y quelque chose de rapide ou un reste. Le menu reste un brouillon jusqu’à ce que vous décidiez de le garder.</p>""",
            ),
            (
                "Utiliser les aliments dans le bon ordre",
                """<p>Les produits fragiles méritent une place en début de semaine, les produits qui se conservent peuvent attendre. Relier l’inventaire au planning rend cet ordre presque naturel, et c’est l’un des leviers les plus simples pour <a href="/fr/reduire-gaspillage-alimentaire/">réduire le gaspillage alimentaire</a> à la maison.</p><table><thead><tr><th>Moment de la semaine</th><th>À privilégier</th></tr></thead><tbody><tr><td>Lundi et mardi</td><td>Poisson frais, salades, herbes, produits déjà entamés</td></tr><tr><td>Milieu de semaine</td><td>Viande et volaille, légumes plus robustes, produits laitiers</td></tr><tr><td>Fin de semaine</td><td>Légumineuses, riz et pâtes, surgelés, conserves</td></tr></tbody></table><p>Ce tableau est une règle générale, pas une garantie. Regardez, sentez et suivez les indications de l’emballage avant de cuisiner un produit proche de sa date.</p>""",
            ),
            (
                "Un menu de la semaine pour toute la famille",
                """<p>Un menu hebdomadaire ne signifie pas sept nouvelles recettes. Les plannings qui tiennent dans une famille reposent le plus souvent sur une structure simple&nbsp;:</p><ul><li>trois ou quatre plats du quotidien que tout le monde accepte, en rotation&nbsp;;</li><li>une ou deux idées nouvelles pour ne pas tourner en rond&nbsp;;</li><li>une soirée «&nbsp;restes&nbsp;» ou boîtes-repas, souvent le jeudi&nbsp;;</li><li>une marge pour l’imprévu, le repas chez des amis ou la pizza du vendredi.</li></ul><p>Dans Cibello, vous placez les repas jour par jour, vous voyez ce qui est déjà dans l’inventaire et le reste rejoint la liste de courses. Les enfants peuvent donner leur avis entre deux plats proposés&nbsp;; l’application elle-même s’adresse aux adultes.</p>""",
            ),
            (
                "Un planning partagé, une seule liste de courses",
                """<p>La personne qui planifie ne devrait pas porter seule toute la logistique. Dans Cibello, les membres du foyer partagent l’inventaire, le menu et la liste de courses, pendant la période d’essai puis avec un abonnement. Celui qui passe au supermarché voit ce qui manque réellement, et l’autre n’achète pas une deuxième bouteille de lait. Quand un produit est utilisé ou acheté, la vue commune est mise à jour pour tout le monde.</p>""",
            ),
            (
                "Une proposition, jamais un emploi du temps",
                """<p>Le planning est un point de départ que vous adaptez à la réalité de la semaine. Échangez des jours, supprimez des plats, ajoutez vos propres favoris. Plus l’inventaire et la liste sont tenus à jour, plus la proposition suivante sera juste. Les filtres de recettes et d’allergènes restent une aide, pas une garantie&nbsp;: vérifiez toujours les ingrédients et les emballages, surtout en cas d’allergie. Pour comparer Cibello avec d’autres applications de planification, consultez le <a href="/en/best-meal-planning-app/">comparatif en anglais</a>, ou découvrez l’ensemble des fonctions sur la <a href="/fr/">page d’accueil en français</a>.</p>""",
            ),
        ],
        faq=[
            (
                "Cibello peut-il créer un menu de la semaine automatiquement ?",
                "Oui, l’application propose un planning à partir de votre inventaire et de vos habitudes. Vous le relisez, le modifiez et décidez ce qui est conservé.",
            ),
            (
                "Le menu tient-il compte de ce que j’ai déjà à la maison ?",
                "Oui. L’inventaire vérifié sert de base, et les produits qui doivent être mangés bientôt sont pris en compte dans les suggestions.",
            ),
            (
                "Puis-je modifier un repas prévu ?",
                "Bien sûr. Le planning est une proposition. Déplacez, remplacez ou supprimez n’importe quel repas, la liste de courses suit.",
            ),
            (
                "Toute la famille peut-elle voir le même planning ?",
                "Oui, les membres du foyer partagent l’inventaire, le menu et la liste de courses pendant la période d’essai, puis avec un abonnement. L’application est réservée aux adultes de 18 ans et plus.",
            ),
        ],
    ),
    "/fr/recettes-avec-ingredients/": dict(
        title="Recettes avec les ingrédients déjà chez vous | Cibello",
        desc="Que manger ce soir avec ce qu’il y a dans le frigo ? Cibello classe plus de 9 000 recettes selon les ingrédients déjà chez vous et indique ce qui manque.",
        eyebrow="Que manger ce soir",
        h1="Recettes avec les ingrédients déjà chez vous",
        lead="Chercher une recette, puis constater qu’il manque la moitié des ingrédients : tout le monde connaît. Cibello fait l’inverse et part de ce qui est déjà dans votre cuisine pour vous montrer ce que vous pouvez cuisiner ce soir.",
        sections=[
            (
                "Que manger ce soir&nbsp;? Commencez par votre cuisine",
                """<p>La question revient chaque jour, et la réponse se trouve rarement dans un livre de recettes. Elle se trouve dans le frigo&nbsp;: un demi-chou, trois œufs, un reste de riz, une brique de crème entamée. Une recette utile est d’abord une recette possible avec ce que vous avez. C’est pour cela que Cibello ne vous demande pas de choisir un plat avant de regarder vos placards, mais l’inverse.</p><p>L’application connaît les produits que vous avez enregistrés ou scannés, sait lesquels doivent être mangés bientôt et vous propose des recettes en conséquence. Vous n’avez plus qu’à choisir. Cette approche change aussi la façon de faire les courses&nbsp;: on achète pour compléter ce qui est là, pas pour repartir de zéro à chaque repas.</p>""",
            ),
            (
                "Du scan à un inventaire utile",
                """<p>Pour que les suggestions soient justes, l’inventaire doit ressembler à votre vraie cuisine. Trois façons de le remplir&nbsp;:</p><ul><li><strong>Photographier</strong> le réfrigérateur, le congélateur ou un placard&nbsp;: l’application reconnaît les produits et retient où ils se trouvent.</li><li><strong>Scanner le ticket de caisse</strong> en rentrant des courses pour ajouter tout ce qui vient d’être acheté.</li><li><strong>Scanner un code-barres</strong> pour un produit isolé.</li></ul><p>Dans les trois cas, vous relisez le résultat avant de l’enregistrer. L’IA peut confondre deux produits, oublier ce qui se cache au fond ou proposer une date incertaine. Corriger ces détails prend peu de temps et rend chaque suggestion suivante plus fiable.</p>""",
            ),
            (
                "Des recettes classées selon ce que vous avez",
                """<p>Cibello compare votre inventaire vérifié à plus de 9&nbsp;000 recettes et les classe selon la part des ingrédients déjà chez vous. Un plat pour lequel vous avez tout remonte en tête&nbsp;; un plat auquel il manque deux ingrédients apparaît avec la liste précise de ce qui manque, que vous pouvez envoyer dans la liste de courses.</p><p>Le classement ne se limite pas au pourcentage. Les suggestions tiennent compte de ce qui expire bientôt et de ce que votre foyer choisit souvent, et chaque proposition s’accompagne d’une courte explication. Vous comprenez pourquoi ce gratin arrive en premier ce soir, et vous restez libre de préférer autre chose. Les restes et les boîtes-repas enregistrés dans l’inventaire comptent eux aussi comme des ingrédients disponibles.</p>""",
            ),
            (
                "Les soirs de semaine&nbsp;: simple et faisable",
                """<p>Un mardi soir, les meilleures recettes sont rarement les plus ambitieuses. Ce sont celles qui se préparent en une demi-heure avec ce qui est déjà là&nbsp;:</p><ul><li>des pâtes avec une sauce à base de légumes entamés et d’un reste de fromage&nbsp;;</li><li>une omelette ou une frittata qui absorbe presque tout ce qui reste dans le bac à légumes&nbsp;;</li><li>une poêlée de riz ou de nouilles avec un reste de viande ou du tofu&nbsp;;</li><li>une soupe ou un potage à partir de légumes un peu fatigués&nbsp;;</li><li>un gratin qui donne une seconde vie aux pommes de terre de dimanche.</li></ul><p>Comme ces plats utilisent des produits courants, ils remontent naturellement dans les suggestions de Cibello quand le frigo est à moitié vide.</p>""",
            ),
            (
                "Le week-end, les restes et les boîtes-repas",
                """<p>Le week-end laisse plus de place à un plat mijoté, à une pâtisserie ou à un repas entre amis. Les suggestions peuvent alors mettre en avant des ingrédients qui méritent un peu plus de soin, ou des recettes que vous avez enregistrées en favori. Si vous planifiez le week-end dès la semaine, ce qui manque rejoint la liste de courses à temps.</p><p>Les restes du samedi ont aussi leur place&nbsp;: ajoutez-les à l’inventaire comme boîtes-repas, ils seront visibles pour toute la maison et pris en compte quand vous chercherez quoi manger lundi. C’est une façon simple de <a href="/fr/reduire-gaspillage-alimentaire/">réduire le gaspillage alimentaire</a> sans y penser.</p>""",
            ),
            (
                "Allergies et régimes&nbsp;: une aide, pas une garantie",
                """<p>Vous pouvez indiquer des allergies, des intolérances et des habitudes alimentaires pour orienter les suggestions. Ces filtres sont une aide au tri, jamais une garantie. Lisez toujours la liste des ingrédients et l’étiquette de l’emballage, surtout en cas d’allergie sévère. Les valeurs nutritionnelles affichées sont des estimations utiles pour se repérer, pas un avis médical. En cas de maladie, de grossesse ou de besoins particuliers, la référence reste un professionnel de santé, pas une application.</p>""",
            ),
            (
                "De l’idée à la liste de courses, puis au menu de la semaine",
                """<p>Une fois le plat choisi, la liste de courses partagée fait le reste&nbsp;: elle montre ce qui manque vraiment et évite à deux personnes d’acheter la même chose. Si vous voulez aller plus loin qu’un dîner à la fois, le <a href="/fr/planificateur-repas/">planificateur de repas</a> transforme ces idées en menu de la semaine. Pour comparer Cibello avec d’autres applications de recettes, consultez le <a href="/en/best-recipe-app/">comparatif en anglais</a>&nbsp;; la présentation complète est sur la <a href="/fr/">page d’accueil en français</a>.</p>""",
            ),
        ],
        faq=[
            (
                "Cibello peut-il proposer des recettes à partir de restes ?",
                "Oui. Quand les restes et les produits entamés figurent dans l’inventaire, ils sont pris en compte dans les suggestions.",
            ),
            (
                "Dois-je saisir tous les produits à la main ?",
                "Non. Vous pouvez photographier le frigo et les placards, scanner un ticket de caisse ou un code-barres. Le résultat doit toujours être vérifié avant l’enregistrement.",
            ),
            (
                "Cibello tient-il compte des allergies ?",
                "Vous pouvez indiquer allergies et habitudes alimentaires, mais le filtrage n’est pas une garantie. Lisez toujours les ingrédients et l’étiquetage vous-même.",
            ),
            (
                "Combien de recettes propose Cibello ?",
                "Plus de 9 000 recettes, classées selon la part des ingrédients déjà chez vous. L’application indique ce qui manque pour chacune.",
            ),
        ],
    ),
    "/fr/reduire-gaspillage-alimentaire/": dict(
        title="Réduire le gaspillage alimentaire à la maison | Cibello",
        desc="Voir ce qu’il y a dans la cuisine, comprendre DLC et DDM, cuisiner autour des produits fragiles et partager l’inventaire du foyer : des gestes concrets.",
        eyebrow="Moins jeter, sans culpabilité",
        h1="Réduire le gaspillage alimentaire à la maison",
        lead="La plupart des aliments jetés ne le sont pas par négligence, mais faute de vue d’ensemble. Ce guide donne des repères simples pour utiliser à temps ce que vous avez, et montre comment Cibello relie inventaire, recettes et courses pour y arriver.",
        sections=[
            (
                "Qu’est-ce que le gaspillage alimentaire&nbsp;?",
                """<p>Le gaspillage alimentaire, c’est de la nourriture qui aurait pu être mangée et qui finit à la poubelle&nbsp;: un reste oublié au fond du frigo, des légumes qui ont ramolli, un yaourt passé de date sans que personne n’ait vérifié s’il était encore bon. Selon Eurostat, les ménages représentent un peu plus de la moitié du gaspillage alimentaire dans l’Union européenne, soit environ 69&nbsp;kg par habitant en 2023, davantage que la production, la transformation, la restauration et la distribution réunies.</p><p>Ces chiffres n’ont rien d’une accusation. Ils décrivent surtout un problème de visibilité&nbsp;: on jette ce qu’on a oublié. C’est précisément là qu’un inventaire et des rappels au bon moment font la différence.</p>""",
            ),
            (
                "Voir ce qui risque d’être oublié",
                """<p>Un inventaire rend visible ce qui se trouve dans le réfrigérateur, le congélateur et les placards, et surtout où. Avec Cibello, vous photographiez ces espaces, l’application reconnaît les produits et leur emplacement, et vous corrigez ce qui a été mal lu avant d’enregistrer. Vous pouvez aussi scanner un ticket de caisse ou un code-barres.</p><p>Quand une date est renseignée, l’application vous rappelle en douceur ce qui doit être mangé bientôt. Pas d’alerte rouge, pas de reproche&nbsp;: juste un coup d’œil le matin pour savoir que les épinards ne passeront pas le week-end. Les dates et les lectures de l’IA peuvent être inexactes&nbsp;; regardez, sentez et suivez les indications de l’emballage.</p>""",
            ),
            (
                "DLC ou DDM&nbsp;: comprendre les dates",
                """<p>Beaucoup d’aliments sont jetés parce qu’une date a été mal comprise. Deux mentions coexistent sur les emballages en France&nbsp;:</p><table><thead><tr><th>Mention</th><th>Ce qu’elle signifie</th><th>Que faire après la date</th></tr></thead><tbody><tr><td>DLC, «&nbsp;à consommer jusqu’au&nbsp;»</td><td>Date limite de consommation, produits frais et sensibles (viande, poisson, plats préparés)</td><td>Ne pas consommer après la date</td></tr><tr><td>DDM, «&nbsp;à consommer de préférence avant&nbsp;»</td><td>Date de durabilité minimale, produits secs, conserves, café, surgelés</td><td>Souvent encore bon&nbsp;: vérifier l’aspect, l’odeur et le goût</td></tr></tbody></table><p>La différence est importante&nbsp;: une DDM dépassée n’est pas un motif de jeter, une DLC dépassée l’est. En cas de doute, en particulier pour de jeunes enfants, des femmes enceintes ou des personnes fragiles, restez prudent.</p>""",
            ),
            (
                "Cuisiner autour de ce qui est déjà là",
                """<p>Plutôt que d’acheter une nouvelle série d’ingrédients pour une recette repérée en ligne, partez de ce qui attend dans la cuisine. Cibello classe plus de 9&nbsp;000 recettes selon la part des ingrédients que vous avez et met en avant celles qui utilisent les produits proches de leur date. Seul ce qui manque vraiment rejoint la liste de courses.</p><p>Un demi-poivron, un fond de crème et trois œufs suffisent souvent pour une frittata&nbsp;; encore faut-il savoir qu’ils sont là. C’est exactement ce que l’inventaire rend possible. Le guide <a href="/fr/recettes-avec-ingredients/">recettes avec les ingrédients déjà chez vous</a> détaille ce fonctionnement.</p>""",
            ),
            (
                "Planifier la semaine dans le bon ordre",
                """<p>Un menu de la semaine bien pensé place les produits fragiles en début de semaine et garde les conserves, les légumineuses et les surgelés pour la fin. Il prévoit aussi une soirée pour finir les restes. Le <a href="/fr/planificateur-repas/">planificateur de repas</a> de Cibello propose une semaine qui varie les plats et tient compte de ce qui expire bientôt&nbsp;; vous relisez et adaptez.</p><p>Quelques habitudes qui aident, avec ou sans application&nbsp;:</p><ul><li>faire les courses avec une liste construite à partir de l’inventaire, pas de mémoire&nbsp;;</li><li>ranger les nouveaux achats derrière les anciens&nbsp;;</li><li>congeler le pain, la viande ou les restes dès qu’un doute apparaît sur le délai&nbsp;;</li><li>cuisiner de plus grandes portions et prévoir les boîtes-repas du lendemain.</li></ul>""",
            ),
            (
                "Restes, boîtes-repas et congélateur",
                """<p>Les restes se perdent surtout parce qu’on ne les voit plus. Dans Cibello, les boîtes-repas peuvent figurer dans l’inventaire comme n’importe quel produit&nbsp;: elles sont visibles pour toute la maison et peuvent être prises en compte quand vous cherchez quoi manger. Le congélateur fonctionne de la même manière&nbsp;: un sachet étiqueté et enregistré a bien plus de chances d’être mangé qu’un bloc anonyme découvert six mois plus tard.</p>""",
            ),
            (
                "Partager la vue d’ensemble, sans culpabilité",
                """<p>Quand le foyer partage l’inventaire et la liste de courses, les doubles achats diminuent et chacun voit ce qui doit être utilisé. La planification cesse d’être l’affaire d’une seule personne&nbsp;: chacun peut ajouter un produit acheté, retirer ce qui a été utilisé ou signaler un reste depuis son propre téléphone. Cibello ne pratique ni la honte ni la pression sur les calories&nbsp;: l’objectif est un quotidien plus calme et une poubelle moins pleine. L’application rappelle et propose, mais c’est vous qui décidez ce qui est mangé, congelé ou jeté. Retrouvez l’ensemble des fonctions sur la <a href="/fr/">page d’accueil en français</a>.</p>""",
            ),
        ],
        faq=[
            (
                "Une application peut-elle garantir qu’un aliment est encore sûr ?",
                "Non. Vérifiez toujours la date, la conservation, l’odeur, l’aspect et les indications de l’emballage. Les rappels de Cibello sont une aide, pas une garantie.",
            ),
            (
                "Comment des recettes aident-elles à moins gaspiller ?",
                "Des recettes proposées à partir de l’inventaire permettent d’utiliser les produits déjà présents avant d’en acheter de nouveaux, en priorité ceux proches de leur date.",
            ),
            (
                "Plusieurs personnes peuvent-elles mettre à jour le même inventaire ?",
                "Oui. La fonction foyer est conçue pour une vue commune de l’inventaire, du menu et de la liste de courses, pendant la période d’essai puis avec un abonnement.",
            ),
            (
                "Quelle est la différence entre DLC et DDM ?",
                "La DLC, « à consommer jusqu’au », est une limite de sécurité à respecter. La DDM, « à consommer de préférence avant », concerne la qualité : le produit est souvent encore bon après, à condition de vérifier son aspect et son odeur.",
            ),
        ],
    ),
}

# ---------------------------------------------------------------------------
# Landing page prose
# ---------------------------------------------------------------------------

HUBTEXT = """<section><h2>Une cuisine qui répond à «&nbsp;qu’est-ce qu’on mange&nbsp;?&nbsp;»</h2><p>Cibello ne commence pas par des recettes, mais par votre cuisine. Vous photographiez le frigo, le congélateur et les placards, et l’application dresse un inventaire que vous vérifiez avant de l’enregistrer. À partir de là, elle compare ce que vous avez à plus de 9&nbsp;000 recettes, classe les résultats selon la part des ingrédients déjà chez vous et vous montre ce qui manque. Le guide <a href="/fr/recettes-avec-ingredients/">recettes avec les ingrédients déjà chez vous</a> explique comment en tirer le meilleur un soir de semaine.</p></section>
<section><h2>Une semaine planifiée une fois, puis oubliée</h2><p>Quand décider chaque soir devient fatigant, un menu de la semaine change beaucoup de choses. Cibello propose sept jours variés, tient compte des produits à consommer rapidement et remplit la liste de courses avec ce qui manque vraiment. Vous relisez, déplacez et remplacez ce que vous voulez&nbsp;: la proposition reste un brouillon jusqu’à ce que vous la validiez. Voyez le <a href="/fr/planificateur-repas/">planificateur de repas</a> pour en faire une routine.</p></section>
<section><h2>Moins jeter, sans sermon</h2><p>Une grande partie de ce qui finit à la poubelle a simplement été oublié. Un inventaire avec l’emplacement et les dates, des rappels discrets avant qu’un produit ne se perde et des recettes qui utilisent les restes suffisent souvent à réduire le gaspillage. Cibello rappelle sans culpabiliser et vous laisse décider ce qui est mangé, congelé ou jeté. Le guide <a href="/fr/reduire-gaspillage-alimentaire/">réduire le gaspillage alimentaire</a> ajoute des repères concrets, notamment sur la différence entre DLC et DDM.</p></section>
<section><h2>Bon à savoir avant de commencer</h2><p>L’inventaire, le menu et la liste de courses se partagent dans le foyer pendant l’essai de 14&nbsp;jours sans carte bancaire, puis avec un abonnement. Vos données sont stockées dans l’Union européenne et le compte se supprime dans l’application. Cibello s’adresse aux adultes de 18&nbsp;ans et plus. Les filtres d’allergènes et les valeurs nutritionnelles sont des aides, pas des garanties&nbsp;: vérifiez toujours les emballages.</p></section>"""

# ---------------------------------------------------------------------------
# Shared pages
# ---------------------------------------------------------------------------

ABOUT = dict(
    title="À propos de Cibello – l’application et l’entreprise | LandveX AB",
    desc="Cibello est développé par LandveX AB à Tyresö, en Suède. Pourquoi l’application existe, comment nous abordons l’IA, les données et le gaspillage, et comment nous contacter.",
    h1="À propos de Cibello",
    lead="Cibello est une application alimentaire suédoise éditée par LandveX AB. Elle est née d’une question posée presque chaque jour dans tous les foyers : qu’est-ce qu’on mange ? Cette page explique ce que nous cherchons à faire, comment nous travaillons avec l’IA et les données, et comment nous joindre.",
    sections=[
        (
            "Pourquoi Cibello existe",
            """<p>La plupart des applications de recettes partent des recettes. Nous voulions partir de la cuisine&nbsp;: ce qui se trouve réellement dans le réfrigérateur, le congélateur et les placards, ce qui arrive bientôt à sa date et ce que le foyer aime manger. C’est pourquoi le cœur de Cibello est un inventaire alimentaire, votre «&nbsp;Food Twin&nbsp;», construit à partir de photos, de tickets de caisse et de codes-barres. Les recettes, le menu de la semaine, la liste de courses et les rappels reposent tous sur ces mêmes données. L’objectif est un quotidien moins stressant et <a href="/fr/reduire-gaspillage-alimentaire/">moins de gaspillage alimentaire</a>, sans sermon.</p>""",
        ),
        (
            "Notre approche de l’IA",
            """<p>L’IA rend Cibello possible, mais elle se trompe parfois. Un scan peut mal lire un produit, oublier ce qui se cache au fond ou deviner une mauvaise date. C’est pourquoi vous vérifiez toujours les résultats avant leur enregistrement, et pourquoi les suggestions ne sont que des suggestions. Les filtres de recettes et d’allergènes sont une aide, jamais une garantie, et les valeurs nutritionnelles sont des estimations pour planifier, pas des conseils diététiques. Les modèles propres à Cibello ne s’entraînent que sur vos corrections et, si vous l’acceptez séparément, sur des images assainies. Les deux options sont désactivées par défaut. Voir la <a href="/fr/privacy/">politique de confidentialité</a>.</p>""",
        ),
        (
            "Vos données",
            """<p>Tout est stocké dans l’Union européenne. Vous pouvez consulter vos données dans l’application et <a href="/fr/delete-account/">supprimer votre compte</a> quand vous le souhaitez, sans contacter le support. Nous ne vendons pas de données personnelles.</p>""",
        ),
        (
            "L’entreprise",
            """<p>Cibello est développé et détenu par LandveX AB, numéro d’immatriculation 559141-7042, Antennvägen 2, 135 48 Tyresö, Suède. L’application est disponible pour iOS et Android en douze langues et est conçue en Suède. Pour l’instant, elle s’adresse aux personnes de 18 ans et plus, parce que les conditions du service d’IA qu’elle utilise exigent des utilisateurs adultes. La période d’essai dure 14 jours, sans carte bancaire.</p>""",
        ),
        (
            "Contact",
            """<p>Questions générales et partenariats&nbsp;: <a href="mailto:hello@cibello.app">hello@cibello.app</a>. Support&nbsp;: <a href="mailto:support@cibello.app">support@cibello.app</a>. Confidentialité et protection des données&nbsp;: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>. Les demandes de la presse sont les bienvenues à la même adresse&nbsp;; nous répondons en général sous quelques jours ouvrés.</p><p>Suivez-nous sur <a href="https://www.instagram.com/cibelloapp/" rel="noopener">Instagram</a>, <a href="https://www.tiktok.com/@cibello73" rel="noopener">TikTok</a> et <a href="https://www.facebook.com/profile.php?id=61593336222919" rel="noopener">Facebook</a>.</p>""",
        ),
    ],
)

PRESS = dict(
    title="Presse et médias – faits, images et contact | Cibello",
    desc="Dossier de presse Cibello : présentation courte, faits sur l’application, logo et images, et le contact presse chez LandveX AB.",
    h1="Presse et médias",
    lead="Tout ce qu’il faut pour écrire sur Cibello : une description courte, des faits, des images et un contact qui répond vite. L’ensemble de cette page peut être utilisé librement dans un cadre éditorial.",
    sections=[
        (
            "Cibello en bref",
            """<p>Cibello est une application alimentaire suédoise qui photographie votre frigo et vos placards, tient un inventaire avec emplacement et dates, propose des recettes à partir de ce qui est réellement à la maison, planifie la semaine et partage la liste de courses avec le foyer. Elle rappelle en douceur avant qu’un aliment ne se perde et ne juge jamais ce que chacun mange. Disponible pour iOS et Android en douze langues, avec des données stockées dans l’Union européenne, développée par LandveX AB à Tyresö, en Suède.</p><p><strong>En une phrase&nbsp;:</strong> Cibello est l’application qui voit ce que vous avez chez vous et répond à «&nbsp;qu’est-ce qu’on mange&nbsp;?&nbsp;».</p>""",
        ),
        (
            "Faits",
            """<ul><li>Disponible pour iOS et Android. Réservée aux 18 ans et plus.</li><li>Essai&nbsp;: 14 jours sans carte bancaire, puis abonnement via l’App Store ou Google Play.</li><li>Recettes&nbsp;: plus de 9&nbsp;000, comparées à l’inventaire alimentaire de l’utilisateur.</li><li>Langues&nbsp;: suédois, anglais, allemand, français, espagnol, italien, néerlandais, polonais, danois, norvégien, finnois, portugais.</li><li>Données&nbsp;: stockées dans l’Union européenne. Le compte et les données se suppriment dans l’application.</li><li>IA&nbsp;: scan du frigo, des placards, des tickets de caisse et des codes-barres. L’utilisateur vérifie toujours le résultat. Les modèles propres à Cibello ne s’entraînent que sur les corrections des utilisateurs et, avec un consentement distinct, sur des images assainies.</li><li>Tarif&nbsp;: essai gratuit, puis formule payante pour les fonctions de foyer. Prix en vigueur dans l’App Store et sur Google Play.</li><li>Société&nbsp;: LandveX AB, n° d’immatriculation 559141-7042, Antennvägen 2, 135 48 Tyresö, Suède.</li></ul>""",
        ),
        (
            "Logo et images",
            """<ul><li><a href="/img/icon-512.png">Icône de l’application, PNG 512×512</a></li><li><a href="/img/og-fr.png">Image de partage, PNG 1200×630 (français)</a></li></ul><p>Des captures d’écran de l’application sont disponibles sur demande. Les images peuvent être utilisées librement dans un cadre éditorial, avec mention de Cibello.</p>""",
        ),
        (
            "Contact presse",
            """<p><a href="mailto:hello@cibello.app?subject=Demande%20presse">hello@cibello.app</a>. Nous répondons en général aux demandes de la presse sous un jour ouvré. Le fondateur est disponible pour des entretiens sur le gaspillage alimentaire des ménages, l’IA dans la vie quotidienne et les raisons pour lesquelles «&nbsp;qu’est-ce qu’on mange&nbsp;?&nbsp;» est une question qui mérite une réponse.</p><p>En savoir plus sur l’entreprise&nbsp;: <a href="/fr/about/">À propos de Cibello</a>.</p>""",
        ),
    ],
)

NEWS = dict(
    title="Nouveautés Cibello – mises à jour et nouveaux guides",
    desc="Nouveaux guides, outils et mises à jour sur cibello.app, avec leur date. Abonnement possible via RSS.",
    h1="Nouveautés chez Cibello",
    lead="Ce qui a été ajouté au site et à l’application, du plus récent au plus ancien. Un flux RSS est disponible.",
    rss_label="Flux RSS",
    entries=[
        (
            "2026-09-04",
            "Nouveau guide : le gaspillage alimentaire en Suède en chiffres",
            "/matsvinn-statistik/",
            "Les chiffres officiels de l’Agence suédoise de protection de l’environnement et de l’Agence suédoise de sécurité alimentaire sur une seule page, en suédois. Chaque chiffre est accompagné de sa source.",
        ),
        (
            "2026-09-04",
            "Trois nouveaux guides en anglais et deux comparatifs",
            "/en/best-meal-planning-app/",
            "Que manger ce soir, planificateur de repas IA et application de garde-manger, plus des comparaisons honnêtes des applications de planification et de recettes face à Mealime, Samsung Food, Plan to Eat, Paprika et SuperCook. En anglais.",
        ),
        (
            "2026-09-04",
            "Des pages d’accueil complètes en douze langues",
            "/fr/",
            "Chaque langue dispose désormais d’une page d’accueil complète à la place d’une courte page de texte. Plus rien n’est traduit à la volée dans le navigateur.",
        ),
        (
            "2026-08-30",
            "Politique de confidentialité et conditions d’utilisation version 2.0",
            "/fr/privacy/",
            "Textes mis à jour concernant l’analyse par Gemini, l’entraînement volontaire de Cibello AI, l’essai de 14 jours sans carte bancaire et la limite d’âge de 18 ans. Des traductions françaises sont disponibles, la version suédoise prévaut.",
        ),
    ],
)

# ---------------------------------------------------------------------------
# Legal (traductions de integritet.html, villkor.html et delete-account.html, v2.0)
# ---------------------------------------------------------------------------

PRIVACY = dict(
    title="Politique de confidentialité – Cibello",
    desc="Comment Cibello traite les données personnelles, les images, l’analyse par Gemini et l’entraînement volontaire de Cibello AI. Traduction française de la politique suédoise, version 2.0.",
    h1="Politique de confidentialité",
    notice="""<strong>En résumé&nbsp;:</strong> un service d’IA externe réalise aujourd’hui l’analyse des images. Le modèle d’IA propre à Cibello ne peut être entraîné que sur les corrections de l’utilisateur et sur des images assainies, après un choix distinct, volontaire et actif lors de l’introduction. Les réponses de l’IA externe ne servent jamais de référence d’entraînement.""",
    body="""<h2>1. Responsable du traitement</h2>
<p>LandveX AB, numéro d’immatriculation 559141-7042, Antennvägen 2, 135 48 Tyresö, Suède, est responsable du traitement des données personnelles pour Cibello. Les questions relatives à la confidentialité sont à adresser à <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>

<h2>2. Données et finalités</h2>
<ul>
<li><strong>Compte&nbsp;:</strong> adresse e-mail, nom d’affichage, identité d’authentification et journaux de sécurité, pour créer et protéger le compte.</li>
<li><strong>Données alimentaires et du foyer&nbsp;:</strong> inventaire, recettes, préférences, allergies et corrections propres à l’utilisateur, pour les fonctions de l’application.</li>
<li><strong>Images&nbsp;:</strong> images que l’utilisateur choisit de scanner pour identifier des produits alimentaires ou des tickets de caisse.</li>
<li><strong>Paiement&nbsp;:</strong> statut de l’abonnement et références de transaction. Les données de carte et de paiement sont traitées par Apple App Store ou Google Play.</li>
<li><strong>Données techniques&nbsp;:</strong> erreurs, performances et analyse produit, uniquement selon les choix de l’utilisateur et les besoins de sécurité nécessaires.</li>
<li><strong>Protection contre l’abus de la période d’essai gratuite&nbsp;:</strong> une empreinte HMAC pseudonyme, à clé, de l’adresse e-mail normalisée est conservée pendant cinq ans au maximum. Elle ne peut servir ni à la connexion ni à la prise de contact et ne contient ni l’adresse en clair, ni l’identifiant utilisateur, ni l’identité Firebase. Sa seule finalité est d’empêcher des périodes d’essai répétées après suppression du compte et nouvelle inscription.</li>
</ul>

<h2>3. Gemini en production</h2>
<p>Les images sélectionnées et l’instruction nécessaire sont envoyées à l’API Google Gemini pour produire le résultat affiché dans l’application. Cibello utilise le service payant au sein de l’EEE. Selon les conditions de Google, les données du service payant ne sont pas utilisées pour améliorer les produits de Google, mais une journalisation limitée peut avoir lieu à des fins de sécurité et de lutte contre les abus, sauf si un mode spécifique de conservation nulle s’applique. Cibello ne promet donc pas une conservation nulle en dehors de son propre environnement sans confirmation technique du fournisseur.</p>
<p>Les résultats de Gemini sont des estimations automatiques. L’utilisateur doit vérifier le contenu, les allergènes, les dates et les quantités avant d’utiliser ces informations.</p>

<h2>4. Le modèle d’IA propre à Cibello&nbsp;: un entraînement distinct et volontaire</h2>
<p>Cibello développe son propre modèle d’IA. Le flux d’entraînement est séparé, techniquement et juridiquement, du service d’IA externe qui fournit à l’utilisateur les résultats actuels&nbsp;:</p>
<ul>
<li>Les réponses, raisonnements ou suggestions de Gemini ne sont jamais exportés comme étiquettes ou référence d’entraînement vers le modèle d’IA propre à Cibello.</li>
<li>L’<strong>amélioration anonymisée de l’IA</strong> permet d’utiliser la correction explicite de l’utilisateur, ou la réponse confirmée manuellement, sans l’image.</li>
<li>L’<strong>entraînement sur images</strong> permet d’associer une copie assainie de l’image de l’utilisateur à sa propre correction. Les métadonnées sont supprimées et la taille de l’image est limitée avant stockage.</li>
<li>L’introduction présente un choix commun et clair pour ces deux volets d’une même finalité d’entraînement. Le choix n’est pas présélectionné et l’application fonctionne même si l’utilisateur ne consent pas.</li>
<li>Le consentement peut être retiré à l’aide d’un bouton dans Profil. Toute utilisation future cesse alors, la banque d’entraînement active détenue par l’application est vidée et les références d’images sont supprimées. Les paramètres de modèle déjà produits et agrégés ne peuvent normalement pas être rattachés à une personne.</li>
<li>Cibello AI n’influence pas la réponse en production tant que des seuils documentés de performance et de sécurité n’ont pas été atteints.</li>
</ul>

<h2>5. Base juridique</h2>
<p>Le compte et les fonctions essentielles sont traités pour l’exécution du contrat. La journalisation de sécurité et l’empreinte limitée destinée à empêcher des périodes d’essai répétées sont traitées sur la base de l’intérêt légitime. Des obligations légales peuvent exiger d’autres traitements limités. L’analyse produit volontaire, l’amélioration de l’IA et l’entraînement sur images reposent sur des consentements distincts qui peuvent être retirés.</p>

<h2>6. Conservation et destinataires</h2>
<p>Les données sont conservées aussi longtemps que l’exigent le service, la sécurité, les obligations légales et la rétention documentée des sauvegardes. Les prestataires peuvent inclure AWS pour l’hébergement et le stockage, Firebase pour l’authentification, Google Gemini pour l’analyse IA choisie, ainsi qu’Apple ou Google pour le paiement. Cibello ne vend pas de données personnelles. L’empreinte liée à la période d’essai est supprimée automatiquement au plus tard cinq ans après le début de l’essai.</p>

<h2>7. Vos droits</h2>
<p>Vous pouvez demander l’accès, la rectification, la portabilité, la limitation ou l’effacement de vos données, et vous opposer à certains traitements. Les consentements se modifient dans Profil. Le compte peut être supprimé directement dans l’application ou via la <a href="/fr/delete-account/">page de suppression du compte</a>. Vous pouvez également vous adresser à l’autorité suédoise de protection des données (Integritetsskyddsmyndigheten).</p>

<h2>8. Âge</h2>
<p>Pour l’instant, Cibello s’adresse aux personnes d’au moins 18 ans, parce que les conditions du service API Gemini utilisé exigent des utilisateurs adultes. Cette exigence d’âge sera réexaminée si la solution technique du fournisseur change.</p>

<h2>9. Modifications</h2>
<p>Les modifications substantielles reçoivent un numéro de version et exigent une nouvelle acceptation dans l’application avant toute utilisation ultérieure.</p>""",
)

TERMS = dict(
    title="Conditions d’utilisation – Cibello",
    desc="Conditions d’utilisation de Cibello : compte, limite d’âge, abonnements et essai de 14 jours, analyse par IA et usage sûr. Traduction française des conditions suédoises, version 2.0.",
    h1="Conditions d’utilisation",
    body="""<h2>1. Contrat et limite d’âge</h2>
<p>Les présentes conditions s’appliquent entre l’utilisateur et LandveX AB, numéro d’immatriculation 559141-7042. Pour l’instant, Cibello est réservé aux personnes d’au moins 18 ans. En créant un compte, l’utilisateur confirme son âge et accepte les présentes conditions ainsi que la <a href="/fr/privacy/">politique de confidentialité</a>.</p>

<h2>2. Le service</h2>
<p>Cibello aide l’utilisateur à organiser ses aliments, à interpréter les images et tickets de caisse sélectionnés et à recevoir des suggestions de recettes et de repas. Les résultats peuvent être incomplets ou erronés et doivent être vérifiés par l’utilisateur.</p>

<h2>3. Aucun conseil médical ou professionnel</h2>
<p>Cibello fournit de l’inspiration et des informations générales, et non des conseils médicaux, diététiques, allergologiques ou d’une autre nature professionnelle. L’utilisateur est responsable de la vérification des ingrédients, des allergènes, de la taille des portions, de la durée de conservation, de la préparation et de la sécurité alimentaire. En cas de maladie, de grossesse, d’allergie sévère ou de besoins particuliers, un professionnel de santé qualifié doit être consulté.</p>

<h2>4. IA et contrôle humain</h2>
<p>Un service d’IA externe est utilisé pour l’analyse actuelle en production. Le modèle d’IA propre à Cibello est développé en parallèle, mais ne peut être entraîné que selon le consentement et les limites décrits dans la <a href="/fr/privacy/">politique de confidentialité</a>. Les réponses de l’IA externe ne servent jamais de référence d’entraînement. Les résultats automatiques doivent toujours pouvoir être corrigés par l’utilisateur.</p>

<h2>5. Consentements volontaires à l’entraînement</h2>
<p>L’accès aux fonctions essentielles de Cibello ne peut être conditionné au consentement à l’amélioration de l’IA ou à l’entraînement sur images. Le choix est désactivé par défaut, distinct de l’acceptation des conditions, et peut être modifié dans Profil.</p>

<h2>6. Compte et sécurité</h2>
<p>L’utilisateur doit fournir des informations exactes, protéger ses identifiants de connexion et signaler à Cibello tout soupçon d’utilisation abusive. Le compte peut être supprimé dans Profil ou via la <a href="/fr/delete-account/">procédure en ligne</a>.</p>

<h2>7. Abonnements et paiement</h2>
<p>Les abonnements numériques de l’application mobile sont achetés et gérés via Apple App Store ou Google Play. La période d’essai de 14 jours sans carte bancaire, contrôlée par les serveurs de Cibello, s’applique une seule fois par identité e-mail sur une période de cinq ans. Un compte supprimé peut être créé à nouveau, mais ne donne pas automatiquement droit à une nouvelle période gratuite. Le prix, la durée, le renouvellement automatique et la résiliation sont affichés par la boutique concernée avant l’achat. Les remboursements sont traités selon les règles de la boutique et le droit impératif de la consommation.</p>

<h2>8. Utilisation autorisée</h2>
<p>Le service ne peut être utilisé pour des contenus illicites, des atteintes aux droits, du harcèlement, une surcharge automatisée, un contournement des mesures de sécurité ou des tentatives d’extraction des données d’autres utilisateurs. Cibello peut restreindre des comptes en cas de risque pour la sécurité ou de manquement substantiel au contrat.</p>

<h2>9. Disponibilité et modifications</h2>
<p>Le service est développé en continu et peut être temporairement indisponible. Les fonctions peuvent être modifiées pour des raisons de sécurité, légales, de qualité ou techniques. Les modifications substantielles des conditions reçoivent un numéro de version et exigent une nouvelle acceptation.</p>

<h2>10. Responsabilité et droit impératif</h2>
<p>LandveX AB est responsable conformément au droit impératif applicable. Rien dans les présentes conditions ne limite les droits auxquels il ne peut être légalement renoncé. Le droit suédois s’applique, et le consommateur peut également se prévaloir du droit impératif et des tribunaux compétents de son pays de résidence.</p>

<h2>11. Contact</h2>
<p>Support&nbsp;: <a href="mailto:support@cibello.app">support@cibello.app</a>. Confidentialité&nbsp;: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>""",
)

DELETE = dict(
    title="Supprimer le compte et les données – Cibello",
    desc="Comment supprimer votre compte Cibello et les données personnelles associées, directement dans l’application.",
    h1="Supprimer le compte et les données",
    body="""<h2>Directement dans l’application</h2>
<ol>
<li>Connectez-vous à Cibello.</li>
<li>Ouvrez <strong>Profil</strong>.</li>
<li>Choisissez <strong>Supprimer le compte</strong> et confirmez.</li>
</ol>
<p>Le compte, l’identité Firebase, les images actives et les données personnelles de l’application sont supprimés. Les références de transactions financières peuvent être pseudonymisées et conservées lorsque la loi l’exige. Les sauvegardes sont renouvelées selon la rétention documentée.</p>

<h2>Si vous ne pouvez pas ouvrir l’application</h2>
<p>Envoyez votre demande depuis l’adresse e-mail enregistrée sur le compte à <a href="mailto:privacy@cibello.app?subject=Supprimer%20mon%20compte%20Cibello">privacy@cibello.app</a>. Écrivez «&nbsp;Supprimer mon compte Cibello&nbsp;». Nous vérifions que vous contrôlez cette adresse avant la suppression.</p>

<h2>Données d’entraînement</h2>
<p>Lors de la suppression, les corrections de l’utilisateur et les références d’images sont retirées de la banque d’entraînement active. Les réponses de Gemini n’ont jamais été exportées comme référence d’entraînement pour Cibello AI. Les paramètres de modèle déjà agrégés ne peuvent normalement pas être rattachés à une personne.</p>""",
)

# ---------------------------------------------------------------------------
# UI strings
# ---------------------------------------------------------------------------

UI = dict(
    faq_title="Questions fréquentes",
    privacy_nav="Politique de confidentialité",
    terms_nav="Conditions d’utilisation",
    delete_nav="Supprimer le compte",
    legal_meta="Cibello · version 2.0 · en vigueur depuis le 30 août 2026 · traduction française",
    translation_label="À propos de cette traduction :",
    translation_note="""Ceci est une traduction française de l’original suédois (<a href="{sv}" lang="sv">original</a>). En cas de divergence, la version suédoise prévaut.""",
)
