"""Portuguese (European) content for cibello.app. Structure: see _schema.py."""

LANG = "pt"

GUIDES = {
    "/pt/planeador-refeicoes/": dict(
        title="Planeador de refeições e menu semanal | Cibello",
        desc="Como montar um menu semanal que varia os pratos, usa primeiro o que está a chegar ao prazo e termina numa lista de compras partilhada com a casa.",
        eyebrow="Menu semanal com menos esforço",
        h1="Planeador de refeições: um menu semanal que cabe na tua vida",
        lead="Decidir o que se come todos os dias, à hora do jantar, cansa mais do que cozinhar. Este guia explica como um menu semanal construído a partir do que já tens em casa tira essa decisão do fim do dia, e o que o Cibello faz para o tornar simples.",
        sections=[
            ("Porque é que um menu semanal alivia tanto", """<p>A pergunta “o que vamos comer?” chega quase sempre à hora errada: às cinco da tarde, com fome, cansaço e um frigorífico de que ninguém se lembra bem. Decidir todos os dias do zero gasta mais energia do que a própria refeição. Um menu semanal tira essa decisão do fim do dia e coloca-a num momento calmo, em que consegues olhar para a semana inteira de uma vez.</p><p>Não precisa de ser um plano rígido nem cheio de receitas novas. Precisa de responder a três coisas: o que há em casa, o que tem de ser usado primeiro e o que a tua casa gosta mesmo de comer. É exatamente por aí que o Cibello começa.</p>"""),
            ("Começa pela cozinha, não pelo livro de receitas", """<p>A maioria das apps de receitas parte das receitas. O Cibello parte do que tens. Fotografas o frigorífico, o congelador e a despensa, e a app reconhece os produtos e o sítio onde estão. Também podes digitalizar o talão das compras ou um código de barras. Antes de guardar, revês o resultado: a IA pode enganar-se num produto, numa data ou numa quantidade, e a palavra final é sempre tua.</p><p>Com essa despensa digital em ordem, o menu semanal deixa de ser um exercício de imaginação. Sabes o que já tens, o que está a chegar ao prazo e o que falta. Se queres perceber melhor esta parte, vê o guia sobre <a href="/pt/receitas-com-ingredientes/">receitas com os ingredientes que tens em casa</a>.</p>"""),
            ("Variedade sem complicar", """<p>Um bom plano não repete o mesmo prato ao almoço e ao jantar nem serve frango três dias seguidos. O Cibello propõe uma semana que varia pratos, ingredientes principais e tipos de refeição, e mostra para cada sugestão a percentagem de ingredientes que já tens em casa. Tu revês, trocas dias, riscas o que não te apetece e acrescentas os teus pratos de sempre.</p><p>Uma estrutura que funciona em muitas casas:</p><ul><li>dois ou três pratos de sempre, aqueles que toda a gente come sem discussão;</li><li>uma ou duas ideias novas, escolhidas entre as sugestões com mais ingredientes já em casa;</li><li>uma noite de sobras ou de marmitas;</li><li>uma refeição muito rápida para o dia mais caótico da semana;</li><li>espaço livre para um jantar fora ou uma mudança de planos.</li></ul>"""),
            ("Usa os alimentos pela ordem certa", """<p>Ligar a despensa ao plano semanal tem uma vantagem discreta: os frescos e as embalagens abertas entram nos primeiros dias, e o que dura mais, como o congelador e a despensa seca, fica para o fim da semana. As sugestões do Cibello têm em conta o que está a chegar ao prazo e explicam porquê, por exemplo “o iogurte natural e os espinafres devem ser usados até quarta-feira”.</p><p>Isto reduz duas coisas ao mesmo tempo: as compras por impulso e a comida que acaba no lixo. Se o desperdício é o teu principal motivo para planear, o guia sobre <a href="/pt/reduzir-desperdicio-alimentar/">reduzir o desperdício alimentar</a> vai mais fundo.</p>"""),
            ("Do plano à lista de compras", """<p>Quando o plano está fechado, a lista de compras reúne apenas o que falta. Não o que já está na despensa, não o que alguém comprou ontem. A lista é partilhada com a casa, por isso quem passa no supermercado a caminho de casa vê a mesma informação que quem fez o plano, e as compras em duplicado tornam-se raras.</p><p>Depois das compras, fotografas o talão e a despensa fica atualizada. O ciclo fecha-se sem que alguém tenha de escrever tudo à mão, e a semana seguinte começa com uma imagem fiel do que há em casa.</p>"""),
            ("Um plano para toda a casa", """<p>Quem planeia não tem de carregar tudo sozinho. No Cibello, as pessoas da casa partilham a mesma despensa, o mesmo plano e a mesma lista, durante o período de teste de 14 dias sem cartão e depois com um plano pago. Todos partem do mesmo ponto, mas cada receita continua a precisar de ser verificada contra alergias, ingredientes e embalagens. Os filtros de receitas e de alergénios são uma orientação, não uma garantia, e os valores nutricionais são estimativas.</p><p>Se estás a comparar planeadores de refeições, temos uma <a href="/en/best-meal-planning-app/">comparação em inglês</a> com outras apps. Na <a href="/pt/">página principal</a> encontras o resto do que o Cibello faz.</p>"""),
            ("Do rascunho à rotina", """<p>O plano é um rascunho, não um horário que tens de cumprir. Vais trocar dias, adiar receitas e repetir favoritos, e está tudo bem. Quanto mais a despensa e a lista se mantêm atualizadas, mais acertadas ficam as sugestões da semana seguinte, porque a app vai aprendendo o que a tua casa costuma escolher. O Cibello não decide por ti; dá-te uma base melhor para decidires mais depressa.</p>"""),
        ],
        faq=[
            ("O Cibello cria o menu semanal automaticamente?", "Propõe um plano com base na tua despensa, no que está a chegar ao prazo e nos gostos da casa. Tu revês, alteras e decides o que fica."),
            ("O menu tem em conta o que já tenho em casa?", "Sim. A despensa digital, revista por ti, é a base das sugestões, e cada receita mostra a percentagem de ingredientes que já tens."),
            ("Posso alterar uma refeição já planeada?", "Sim. Podes trocar dias, substituir pratos e acrescentar receitas próprias em qualquer momento. O plano é sempre uma proposta."),
            ("Toda a casa vê o mesmo plano e a mesma lista?", "Sim. A despensa, o plano e a lista de compras são partilhados durante o período de teste de 14 dias e depois com um plano pago."),
        ],
    ),
    "/pt/receitas-com-ingredientes/": dict(
        title="Receitas com os ingredientes que tens em casa | Cibello",
        desc="Fotografa o frigorífico e a despensa, revê o que a app reconheceu e recebe receitas ordenadas pelo que já tens. Com ideias para cada tipo de noite.",
        eyebrow="O que fazer para o jantar",
        h1="Receitas com os ingredientes que já tens em casa",
        lead="São seis da tarde, há coisas no frigorífico e nenhuma vontade de ir às compras. Este guia explica como o Cibello transforma o que tens numa lista curta de receitas possíveis, e o que continua a depender de ti.",
        sections=[
            ("O problema não é a falta de receitas", """<p>Na internet há milhões de receitas. O difícil é encontrar uma que consigas fazer hoje, com o que está mesmo na tua cozinha, sem descobrir a meio que faltam metade dos ingredientes. A pergunta certa não é “o que me apetece?”, é “o que consigo fazer com o que tenho?”.</p><p>O Cibello inverte a ordem habitual: primeiro olha para a tua despensa, depois procura receitas. Por isso as sugestões que aparecem no topo são as que podes começar a cozinhar já, e as que pedem uma ida ao supermercado mostram claramente o que falta.</p>"""),
            ("Da fotografia a uma despensa digital", """<p>Não precisas de escrever nada à mão. Fotografa o frigorífico, o congelador e a despensa, e a app reconhece os produtos e onde estão. Podes também digitalizar o talão das compras à chegada a casa ou o código de barras de uma embalagem. Antes de guardar, confirmas o que foi reconhecido: a IA pode falhar um produto escondido atrás de outro, ler mal uma data ou enganar-se na quantidade. Corrigir esses casos demora segundos e mantém a despensa fiável.</p><p>Uma despensa digital em ordem é o que torna útil tudo o resto: as receitas, o <a href="/pt/planeador-refeicoes/">plano semanal</a> e os lembretes antes de algo se estragar.</p>"""),
            ("Mais de 9 000 receitas, ordenadas pelo que tens", """<p>O Cibello compara a despensa revista com mais de 9 000 receitas e ordena-as pela percentagem de ingredientes que já tens em casa. Uma receita com “82% em casa” aparece antes de uma com metade dos ingredientes em falta, e cada uma mostra o que teria de ir para a lista de compras.</p><p>As sugestões também pesam o que está a chegar ao prazo e o que a tua casa costuma gostar, e explicam sempre o porquê, por exemplo “porque o frango e as natas estão a chegar à data, e costumas escolher pratos cremosos”. Se quiseres ver como isto se compara com outras apps de receitas, há uma <a href="/en/best-recipe-app/">comparação em inglês</a>.</p>"""),
            ("Sugestões à medida da tua casa", """<p>Podes indicar gostos, hábitos alimentares e alergias, e as sugestões ajustam-se. Com o tempo, a app aprende o que costumam escolher e propõe pratos parecidos com os favoritos, mas feitos com o que há em casa. Duas coisas continuam a ser responsabilidade tua. Os filtros de receitas e de alergénios são uma orientação, não uma garantia, por isso lês sempre os ingredientes e as embalagens, sobretudo em caso de alergia ou intolerância. E os valores nutricionais são estimativas para planear, não aconselhamento médico.</p>"""),
            ("Ideias para cada tipo de noite", """<p>O que faz sentido numa terça-feira cansada não é o mesmo que faz sentido num domingo com tempo. Alguns pontos de partida que funcionam bem com o que quase toda a gente tem em casa:</p><ul><li><strong>Semana, pouco tempo:</strong> massa com o que houver no frigorífico, omelete ou tortilha com legumes, arroz salteado com sobras, sopa de legumes com pão de ontem.</li><li><strong>Fim de semana:</strong> um prato de tacho que aproveita legumes mais moles, uma empada ou um assado, e algo que sobre para a marmita de segunda-feira.</li><li><strong>Sobras:</strong> regista-as como marmitas na despensa digital, para que entrem nas sugestões e não fiquem esquecidas no fundo do frigorífico.</li><li><strong>Com crianças:</strong> mostra duas ou três sugestões e deixa-as escolher. A app é para adultos, mas a decisão pode ser da família.</li></ul>"""),
            ("Da receita à lista de compras", """<p>Escolhida a receita, o que falta passa para a lista de compras partilhada. O objetivo não é comprar mais, é comprar só o que falta e evitar que duas pessoas tragam o mesmo pacote de arroz. Se quiseres, colocas a receita num dia da semana e deixas o plano crescer a partir daí. E quando os ingredientes são usados a tempo, o guia sobre <a href="/pt/reduzir-desperdicio-alimentar/">reduzir o desperdício alimentar</a> mostra o outro lado do mesmo hábito.</p>"""),
            ("Tu decides, a app organiza", """<p>O Cibello não toma decisões por ti. Revês os produtos reconhecidos, os ingredientes, as quantidades, as datas e a informação sobre alergénios antes de usar ou guardar o que for. Em troca, deixas de começar todos os dias do zero: a despensa, as receitas e a lista de compras vivem no mesmo sítio, e toda a casa vê o mesmo. Mais sobre o que a app faz na <a href="/pt/">página principal do Cibello</a>.</p>"""),
        ],
        faq=[
            ("O Cibello sugere receitas com sobras?", "Sim. Quando as sobras e as marmitas estão registadas na despensa digital, entram nas sugestões como qualquer outro ingrediente."),
            ("Tenho de escrever todos os produtos à mão?", "Não. Podes fotografar o frigorífico, o congelador e a despensa, e digitalizar talões e códigos de barras. O resultado é sempre revisto por ti antes de ser guardado."),
            ("O Cibello tem em conta alergias?", "Podes indicar alergias e hábitos alimentares, mas o filtro é uma orientação e não uma garantia. Lê sempre os ingredientes e a rotulagem das embalagens."),
            ("A app diz-me o que falta para uma receita?", "Sim. Cada receita mostra a percentagem de ingredientes que já tens e quais faltam, e podes passá-los para a lista de compras."),
        ],
    ),
    "/pt/reduzir-desperdicio-alimentar/": dict(
        title="Reduzir o desperdício alimentar em casa | Cibello",
        desc="Ver o que há em casa, usar primeiro o que está a chegar ao prazo e comprar só o que falta. Um guia prático para deitar menos comida ao lixo, sem culpa.",
        eyebrow="Menos comida no lixo",
        h1="Reduzir o desperdício alimentar em casa, sem culpa",
        lead="A maior parte da comida que deitamos fora em casa não se perde por descuido, perde-se por falta de visão geral. Este guia mostra como uma despensa digital, lembretes a tempo e receitas à volta do que tens ajudam a usar os alimentos antes que seja tarde.",
        sections=[
            ("O que é, afinal, o desperdício alimentar", """<p>Desperdício alimentar é comida que podia ter sido comida e acabou no lixo: as sobras esquecidas numa caixa ao fundo do frigorífico, os legumes que amoleceram antes de alguém se lembrar deles, o iogurte que passou da data sem que ninguém verificasse se ainda estava bom. Em Portugal, como no resto da Europa, uma parte importante desse desperdício acontece dentro de casa, e não por má vontade. Acontece porque ninguém consegue ter na cabeça, ao mesmo tempo, tudo o que há em três prateleiras, duas gavetas e um congelador.</p><p>É aqui que uma visão geral e um lembrete no momento certo fazem diferença. Não com sermões, com informação.</p>"""),
            ("Vê o que corre o risco de ser esquecido", """<p>Com o Cibello, fotografas o frigorífico, o congelador e a despensa, e a app reconhece os produtos e o sítio onde estão. Digitalizas o talão das compras ou um código de barras para atualizar. Revês o resultado antes de guardar, porque a IA pode enganar-se numa data ou num produto.</p><p>Quando as datas estão registadas, a app avisa com calma antes de algo se estragar e sugere receitas que usam precisamente esses ingredientes. Sem alarmes, sem contagem de calorias, sem vergonha. Uma data numa app nunca substitui os teus sentidos: cheira, olha e segue as indicações da embalagem, sobretudo quando cozinhas para crianças ou para alguém com o sistema imunitário fragilizado.</p>"""),
            ("Planeia receitas à volta dos ingredientes, não ao contrário", """<p>Em vez de escolher uma receita e comprar uma lista inteira de coisas novas, começa pelo que tem de sair primeiro. O Cibello ordena mais de 9 000 receitas pela percentagem de ingredientes que já tens e dá prioridade ao que está a chegar ao prazo. Alguns exemplos do que um ingrediente quase no fim pode virar:</p><table><thead><tr><th>Está a chegar ao prazo</th><th>Pode virar</th></tr></thead><tbody><tr><td>Natas ou iogurte natural</td><td>molho para massa, sopa cremosa, marinada, bolo</td></tr><tr><td>Legumes já moles</td><td>sopa, refogado para arroz, salteado, caldo</td></tr><tr><td>Pão de ontem</td><td>tostas, açorda, pão ralado, migas</td></tr><tr><td>Arroz ou massa cozidos</td><td>arroz de forno, salada fria, frittata</td></tr><tr><td>Frango ou carne já cozinhados</td><td>empadão, wrap, recheio de tarte, salada</td></tr></tbody></table><p>O guia sobre <a href="/pt/receitas-com-ingredientes/">receitas com os ingredientes que tens</a> explica como estas sugestões são construídas.</p>"""),
            ("Sobras e marmitas contam como comida", """<p>Uma das maiores fontes de desperdício é a refeição que sobrou e ninguém voltou a ver. No Cibello, as marmitas podem ficar registadas na despensa digital ao lado dos outros alimentos, para entrarem nas sugestões e nos lembretes. Um hábito simples ajuda muito: guardar as sobras em caixas transparentes, à frente e não ao fundo, e decidir logo se vão ser o almoço de amanhã ou se vão para o congelador. O <a href="/pt/planeador-refeicoes/">plano semanal</a> pode ter uma noite reservada para sobras, o que tira pressão à semana inteira.</p>"""),
            ("Compra o que falta, não o que já tens", """<p>Comprar em duplicado é desperdício adiado: o segundo pacote de queijo ralado chega quando o primeiro ainda está por abrir. Quando a lista de compras nasce da despensa e do plano, contém só o que falta, e é partilhada com toda a casa. Quem está no supermercado vê o mesmo que quem está em casa a abrir o frigorífico. Menos compras por impulso, menos surpresas na gaveta dos legumes.</p>"""),
            ("“Consumir até” não é “consumir de preferência antes de”", """<p>As duas indicações nas embalagens significam coisas diferentes. <strong>Consumir até</strong> é uma data de segurança, usada em alimentos perecíveis como carne fresca, peixe ou refeições prontas; depois dela, o alimento não deve ser consumido. <strong>Consumir de preferência antes de</strong> é uma data de qualidade: muitos alimentos secos, enlatados ou congelados continuam bons durante bastante tempo depois dela, desde que a embalagem esteja intacta e tenham sido bem guardados. Verifica sempre o aspeto, o cheiro e a textura, e em caso de dúvida não arrisques. O Cibello mostra as datas que registaste; não garante a segurança de nenhum alimento.</p>"""),
            ("Hábitos, não culpa", """<p>Desperdiçar menos é uma questão de rotina, não de força de vontade. Fotografa a despensa de vez em quando, deixa a app lembrar-te do que está a chegar ao fim e escolhe receitas a partir daí. Tu decides sempre o que se come, o que se congela e o que vai fora. Se quiseres ver como tudo isto se encaixa, a <a href="/pt/">página principal do Cibello</a> tem a visão geral.</p>"""),
        ],
        faq=[
            ("Uma app pode garantir que um alimento ainda está bom?", "Não. As datas e os resultados da IA podem estar errados. Verifica sempre a conservação, o cheiro, o aspeto e a informação da embalagem."),
            ("Como é que as receitas ajudam a reduzir o desperdício?", "Receitas construídas a partir da tua despensa tornam mais fácil usar o que já tens antes de comprar novo, e a app dá prioridade ao que está a chegar ao prazo."),
            ("Várias pessoas podem atualizar a mesma despensa?", "Sim. A despensa, o plano e a lista de compras são partilhados pela casa, durante o período de teste e depois com um plano pago."),
            ("As sobras também entram na despensa digital?", "Sim. As marmitas podem ficar registadas ao lado dos outros alimentos, para aparecerem nas sugestões e nos lembretes."),
        ],
    ),
}

HUBTEXT = """<section><h2>Começa pelo que tens, não pelo que falta</h2><p>As apps de receitas costumam começar por uma lista de pratos bonitos e acabar numa ida ao supermercado. O Cibello faz o caminho inverso: fotografas o frigorífico, o congelador e a despensa, revês o que a app reconheceu e só depois aparecem as receitas, ordenadas pela percentagem de ingredientes que já tens em casa. O guia sobre <a href="/pt/receitas-com-ingredientes/">receitas com os ingredientes que tens</a> explica como isso funciona numa terça-feira cansada e num domingo com tempo.</p></section>
<section><h2>Um menu semanal que a casa inteira vê</h2><p>Planear a semana não tem de significar sete receitas novas. Dois ou três pratos de sempre, uma ideia nova, uma noite de sobras e uma refeição rápida para o dia mais caótico costumam chegar. O Cibello propõe um plano que varia pratos e ingredientes, tu ajustas, e a lista de compras reúne apenas o que falta, partilhada com quem vive contigo. Lê o guia do <a href="/pt/planeador-refeicoes/">planeador de refeições</a> para montar um menu semanal sem stress.</p></section>
<section><h2>Menos comida no lixo, sem sermões</h2><p>A comida que se estraga em casa raramente se perde por descuido; perde-se porque ninguém consegue ter na cabeça tudo o que há em três prateleiras e um congelador. Com as datas registadas, a app avisa com calma antes de algo se estragar e sugere receitas que usam exatamente esses ingredientes. O guia sobre <a href="/pt/reduzir-desperdicio-alimentar/">reduzir o desperdício alimentar</a> junta os hábitos que fazem diferença, incluindo o que distingue “consumir até” de “consumir de preferência antes de”.</p></section>
<section><h2>Tu revês, tu decides</h2><p>A IA pode enganar-se num produto ou numa data, por isso o resultado de cada digitalização é confirmado por ti antes de ser guardado. Os filtros de receitas e de alergénios são uma orientação, não uma garantia, e os valores nutricionais são estimativas. Os teus dados ficam na UE, a conta apaga-se dentro da app e o teste de 14 dias não pede cartão. A app é para adultos a partir dos 18 anos.</p></section>"""

ABOUT = dict(
    title="Sobre o Cibello: a app e a empresa por trás dela | LandveX AB",
    desc="O Cibello é desenvolvido pela LandveX AB em Tyresö, na Suécia. Porque existe a app, como pensamos a IA, os dados e o desperdício alimentar, e como nos contactar.",
    h1="Sobre o Cibello",
    lead="O Cibello é uma app de comida sueca da LandveX AB. Nasceu para responder a uma pergunta que se faz em quase todas as casas, todos os dias: o que vamos comer? Esta página explica o que estamos a tentar fazer, como trabalhamos com IA e dados, e como nos podes contactar.",
    sections=[
        ("Porque existe o Cibello", """<p>A maioria das apps de receitas começa pelas receitas. Nós quisemos começar pela cozinha: o que está mesmo no frigorífico, no congelador e na despensa, o que está a chegar ao prazo e o que a casa costuma gostar. Por isso o núcleo do Cibello é uma despensa digital, o teu “Food Twin”, construída a partir de fotografias, talões e códigos de barras. As receitas, o plano semanal, a lista de compras e os lembretes assentam todos nos mesmos dados. O objetivo é menos stress no dia a dia e <a href="/pt/reduzir-desperdicio-alimentar/">menos desperdício alimentar</a>, sem sermões.</p>"""),
        ("Como pensamos a IA", """<p>A IA torna o Cibello possível, mas às vezes engana-se. Uma digitalização pode confundir um produto, não ver algo ao fundo ou adivinhar mal uma data. Por isso revês sempre os resultados antes de serem guardados, e as sugestões são apenas sugestões. Os filtros de receitas e de alergénios são uma orientação, nunca uma garantia, e os valores nutricionais são estimativas para planear, não aconselhamento alimentar. Os modelos próprios do Cibello treinam apenas com as tuas correções e, se o escolheres separadamente, com imagens depuradas. Ambas as opções estão desligadas por defeito. Vê a <a href="/pt/privacy/">política de privacidade</a>.</p>"""),
        ("Os teus dados", """<p>Tudo é guardado na UE. Podes consultar os teus dados na app e <a href="/pt/delete-account/">apagar a conta</a> quando quiseres, sem contactar o apoio. Não vendemos dados pessoais.</p>"""),
        ("A empresa", """<p>O Cibello é desenvolvido e detido pela LandveX AB, número de registo 559141-7042, Antennvägen 2, 135 48 Tyresö, Suécia. A app está disponível para iOS e Android em doze idiomas e é feita na Suécia. Por agora destina-se a pessoas com 18 anos ou mais, porque os termos do serviço de IA que utiliza exigem utilizadores adultos. O período de teste é de 14 dias, sem cartão.</p>"""),
        ("Contacto", """<p>Questões gerais e parcerias: <a href="mailto:hello@cibello.app">hello@cibello.app</a>. Apoio: <a href="mailto:support@cibello.app">support@cibello.app</a>. Privacidade e proteção de dados: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>. Os pedidos de imprensa são bem-vindos no primeiro endereço; normalmente respondemos em dois dias úteis. Há também uma <a href="/pt/press/">página de imprensa</a> com factos e imagens.</p><p>Segue-nos no <a href="https://www.instagram.com/cibelloapp/" rel="noopener">Instagram</a>, no <a href="https://www.tiktok.com/@cibello73" rel="noopener">TikTok</a> e no <a href="https://www.facebook.com/profile.php?id=61593336222919" rel="noopener">Facebook</a>.</p>"""),
    ],
)

PRESS = dict(
    title="Imprensa e media: factos, imagens e contacto | Cibello",
    desc="Kit de imprensa do Cibello: descrição curta, factos sobre a app, logótipo e imagens, e o contacto de imprensa na LandveX AB.",
    eyebrow="Para jornalistas e autores",
    h1="Imprensa e media",
    lead="Tudo o que precisas para escrever sobre o Cibello: uma descrição curta, factos, imagens e um contacto que responde depressa. Todo o conteúdo desta página pode ser usado livremente em contexto editorial.",
    sections=[
        ("O Cibello em resumo", """<p>O Cibello é uma app de comida sueca que fotografa o frigorífico e a despensa, mantém uma despensa digital com localização e datas, sugere receitas a partir do que há mesmo em casa, planeia a semana e partilha a lista de compras com a casa. Avisa com calma antes de a comida se estragar e nunca julga o que cada pessoa come. Disponível para iOS e Android em doze idiomas, com dados guardados na UE, desenvolvida pela LandveX AB em Tyresö, na Suécia.</p><p><strong>Numa frase:</strong> o Cibello é a app que vê o que tens em casa e responde à pergunta “o que vamos comer?”.</p>"""),
        ("Factos", """<ul><li>Disponível para iOS e Android. Idade mínima: 18 anos.</li><li>Período de teste: 14 dias sem cartão, depois subscrição através da App Store ou do Google Play.</li><li>Receitas: mais de 9 000, comparadas com a despensa digital de cada utilizador.</li><li>Idiomas: sueco, inglês, alemão, francês, espanhol, italiano, neerlandês, polaco, dinamarquês, norueguês, finlandês e português.</li><li>Dados: guardados na UE. A conta e os dados apagam-se dentro da app.</li><li>IA: digitalização de frigorífico, despensa, talões e códigos de barras. O utilizador revê sempre o resultado. Os modelos próprios do Cibello treinam apenas com as correções dos utilizadores e, com consentimento separado, com imagens depuradas.</li><li>Preço: período de teste gratuito, depois um plano pago para as funções de partilha em casa. Os preços atuais estão na App Store e no Google Play.</li><li>Empresa: LandveX AB, número de registo 559141-7042, Antennvägen 2, 135 48 Tyresö, Suécia.</li></ul>"""),
        ("Logótipo e imagens", """<ul><li><a href="/img/icon-512.png">Ícone da app, PNG 512×512</a></li><li><a href="/img/og-pt.png">Imagem de partilha, PNG 1200×630 (português)</a></li></ul><p>Capturas de ecrã da app disponíveis a pedido. As imagens podem ser usadas livremente em contexto editorial, com referência ao Cibello.</p>"""),
        ("Contacto de imprensa", """<p><a href="mailto:hello@cibello.app?subject=Pedido%20de%20imprensa">hello@cibello.app</a>. Normalmente respondemos a pedidos de imprensa num dia útil. O fundador está disponível para entrevistas sobre desperdício alimentar em casa, IA no dia a dia e porque é que “o que vamos comer?” é uma pergunta que vale a pena resolver.</p><p>Mais sobre a empresa: <a href="/pt/about/">Sobre o Cibello</a>.</p>"""),
    ],
)

NEWS = dict(
    title="Novidades no Cibello: atualizações e novos guias",
    desc="Novos guias, ferramentas e atualizações em cibello.app, com data. Subscreve por RSS.",
    h1="Novidades no Cibello",
    lead="O que foi acrescentado ao site e à app, do mais recente para o mais antigo. Também existe um feed RSS.",
    rss_label="Feed RSS",
    entries=[
        ("2026-09-04", "Novo guia: o desperdício alimentar na Suécia em números", "/matsvinn-statistik/", "Números oficiais da agência sueca do ambiente e da autoridade alimentar sueca numa só página, em sueco: 880 000 toneladas de desperdício alimentar, 16 kg de comida aproveitável por pessoa nas casas e 1 330 coroas por pessoa por ano, com fonte para cada número."),
        ("2026-09-04", "Três novos guias em inglês e duas comparações", "/en/best-meal-planning-app/", "O que comer hoje, planeador de refeições com IA e app de despensa, além de comparações honestas de apps de planeamento de refeições e de receitas com Mealime, Samsung Food, Plan to Eat, Paprika e SuperCook."),
        ("2026-09-04", "Páginas de entrada completas em doze idiomas", "/pt/", "Cada idioma passou a ter uma página de entrada completa em vez de uma página curta de texto, e nada é traduzido no browser."),
        ("2026-08-30", "Política de privacidade e termos de utilização, versão 2.0", "/pt/privacy/", "Textos atualizados sobre a análise Gemini, o treino voluntário da Cibello AI, o período de teste de 14 dias sem cartão e a idade mínima de 18 anos. Há traduções em português; em caso de divergência, prevalece a versão sueca."),
    ],
)

PRIVACY = dict(
    title="Política de privacidade – Cibello",
    desc="Como o Cibello trata dados pessoais, imagens, a análise Gemini e o treino voluntário da Cibello AI. Tradução portuguesa da política sueca, versão 2.0.",
    h1="Política de privacidade",
    notice="""<strong>Em resumo:</strong> um serviço de IA externo é usado para a análise de imagens atual. O modelo de IA próprio do Cibello só pode ser treinado com as correções do próprio utilizador e com imagens depuradas, após uma escolha separada, voluntária e ativa durante a introdução. As respostas de IA externas nunca são usadas como dados de referência para treino.""",
    body="""<h2>1. Responsável pelo tratamento</h2>
<p>A LandveX AB, número de registo 559141-7042, Antennvägen 2, 135 48 Tyresö, Suécia, é a responsável pelo tratamento de dados pessoais no Cibello. As questões de privacidade devem ser enviadas para <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>

<h2>2. Dados e finalidades</h2>
<ul>
<li><strong>Conta:</strong> endereço de e-mail, nome de apresentação, identidade de autenticação e registos de segurança, para criar e proteger a conta.</li>
<li><strong>Dados alimentares e do agregado:</strong> inventário, receitas, preferências, alergias e correções próprias, para as funções da app.</li>
<li><strong>Imagens:</strong> imagens que o utilizador escolhe digitalizar para identificar alimentos ou talões.</li>
<li><strong>Pagamento:</strong> estado da subscrição e referências de transação. Os dados de cartão e de pagamento são tratados pela Apple App Store ou pelo Google Play.</li>
<li><strong>Dados técnicos:</strong> erros, desempenho e análise de produto, apenas de acordo com as escolhas do utilizador e as necessidades de segurança indispensáveis.</li>
<li><strong>Proteção contra abuso do período de teste gratuito:</strong> uma impressão digital HMAC pseudónima, com chave, do endereço de e-mail normalizado, conservada durante no máximo cinco anos. Não pode ser usada para iniciar sessão nem para contacto e não contém o endereço em texto simples, o identificador de utilizador nem a identidade Firebase. A sua única finalidade é impedir períodos de teste gratuitos repetidos após a eliminação da conta e um novo registo.</li>
</ul>

<h2>3. Gemini em produção</h2>
<p>As imagens selecionadas e a instrução necessária são enviadas para a API Google Gemini para produzir o resultado apresentado na app. O Cibello utiliza o serviço pago dentro do EEE. Segundo os termos da Google, os dados no serviço pago não são usados para melhorar os produtos da Google, mas pode ocorrer um registo limitado por razões de segurança e de combate ao abuso, salvo se se aplicar um modo específico de retenção zero. Por isso, o Cibello não promete retenção zero fora do seu próprio ambiente sem confirmação técnica do fornecedor.</p>
<p>Os resultados do Gemini são estimativas automáticas. O utilizador deve verificar o conteúdo, os alergénios, as datas e as quantidades antes de usar a informação.</p>

<h2>4. Modelo de IA próprio do Cibello: treino separado e voluntário</h2>
<p>O Cibello está a desenvolver o seu próprio modelo de IA. O fluxo de treino está separado, técnica e juridicamente, do serviço de IA externo que dá ao utilizador os resultados atuais:</p>
<ul>
<li>As respostas, o raciocínio ou as sugestões do Gemini nunca são exportados como etiquetas de treino ou como dados de referência para o modelo de IA próprio do Cibello.</li>
<li>A <strong>melhoria anónima da IA</strong> permite usar a correção explícita do utilizador, ou a resposta confirmada manualmente, sem a imagem.</li>
<li>O <strong>treino com imagens</strong> permite associar uma cópia depurada da imagem do utilizador à sua própria correção. Os metadados são removidos e a imagem é reduzida em tamanho antes de ser guardada.</li>
<li>A introdução apresenta uma escolha conjunta e clara para estas duas partes da mesma finalidade de treino. A escolha não vem pré-selecionada e a app funciona mesmo que o utilizador não consinta.</li>
<li>O consentimento pode ser retirado com um botão em Perfil. A partir daí, a utilização futura é interrompida, o banco de treino ativo gerido pela app é limpo e as referências às imagens são removidas. Os parâmetros de modelo já produzidos e agregados normalmente não podem ser associados de novo a uma pessoa.</li>
<li>A Cibello AI não influencia a resposta em produção até serem atingidos limites documentados de desempenho e segurança.</li>
</ul>

<h2>5. Base jurídica</h2>
<p>A conta e as funções essenciais são tratadas para executar o contrato. O registo de segurança e a impressão digital limitada contra períodos de teste repetidos são tratados com base no interesse legítimo. Obrigações legais podem exigir outro tratamento limitado. A análise de produto voluntária, a melhoria da IA e o treino com imagens baseiam-se em consentimentos separados, que podem ser retirados.</p>

<h2>6. Conservação e destinatários</h2>
<p>Os dados são conservados durante o tempo necessário para o serviço, a segurança, os requisitos legais e a retenção documentada de cópias de segurança. Os fornecedores podem incluir a AWS para alojamento e armazenamento, o Firebase para autenticação, o Google Gemini para a análise de IA selecionada e a Apple ou a Google para pagamentos. O Cibello não vende dados pessoais. A impressão digital do período de teste é eliminada automaticamente, no máximo, cinco anos após o início do período de teste.</p>

<h2>7. Os teus direitos</h2>
<p>Podes pedir acesso, retificação, portabilidade dos dados, limitação ou apagamento, e opor-te a determinado tratamento. Os consentimentos alteram-se em Perfil. A conta pode ser eliminada diretamente na app ou através da <a href="/pt/delete-account/">página de eliminação de conta</a>. Podes também contactar a autoridade sueca de proteção de dados (Integritetsskyddsmyndigheten).</p>

<h2>8. Idade</h2>
<p>Até nova indicação, o Cibello destina-se a pessoas com pelo menos 18 anos, porque os termos do serviço da API Gemini utilizado exigem utilizadores adultos. O requisito de idade será reavaliado se a solução técnica do fornecedor mudar.</p>

<h2>9. Alterações</h2>
<p>As alterações substanciais recebem um número de versão e exigem uma nova aceitação na app antes de continuar a utilização.</p>""",
)

TERMS = dict(
    title="Termos de utilização – Cibello",
    desc="Termos de utilização do Cibello: conta, idade mínima, subscrições e período de teste de 14 dias, análise por IA e utilização segura. Tradução portuguesa, versão 2.0.",
    h1="Termos de utilização",
    body="""<h2>1. Contrato e idade mínima</h2>
<p>Estes termos aplicam-se entre o utilizador e a LandveX AB, número de registo 559141-7042. Até nova indicação, o Cibello destina-se apenas a pessoas com pelo menos 18 anos. Ao criar uma conta, o utilizador confirma a sua idade e aceita estes termos e a <a href="/pt/privacy/">política de privacidade</a>.</p>

<h2>2. O serviço</h2>
<p>O Cibello ajuda o utilizador a organizar alimentos, a interpretar imagens e talões selecionados e a receber sugestões de receitas e de refeições. Os resultados podem estar incompletos ou incorretos e devem ser revistos pelo utilizador.</p>

<h2>3. Sem aconselhamento médico ou profissional</h2>
<p>O Cibello oferece inspiração e informação geral, não aconselhamento médico, nutricional, sobre alergias ou outro aconselhamento profissional. O utilizador é responsável por verificar ingredientes, alergénios, tamanho das porções, prazos de validade, preparação e segurança alimentar. Em caso de doença, gravidez, alergia grave ou necessidades especiais, deve ser consultado um profissional de saúde qualificado.</p>

<h2>4. IA e controlo humano</h2>
<p>Um serviço de IA externo é usado para a análise em produção atual. O modelo de IA próprio do Cibello é desenvolvido em paralelo, mas só pode ser treinado de acordo com o consentimento e as limitações descritos na <a href="/pt/privacy/">política de privacidade</a>. As respostas de IA externas nunca são usadas como dados de referência para treino. Os resultados automáticos devem poder ser sempre corrigidos pelo utilizador.</p>

<h2>5. Consentimentos de treino voluntários</h2>
<p>O acesso às funções essenciais do Cibello não pode ser condicionado ao consentimento para a melhoria da IA ou para o treino com imagens. A escolha está desligada por defeito, é separada da aceitação dos termos e pode ser alterada em Perfil.</p>

<h2>6. Conta e segurança</h2>
<p>O utilizador deve fornecer dados corretos, proteger o seu acesso e informar o Cibello de qualquer suspeita de utilização indevida. A conta pode ser eliminada em Perfil ou através do <a href="/pt/delete-account/">fluxo web</a>.</p>

<h2>7. Subscrições e pagamento</h2>
<p>As subscrições digitais na app móvel são compradas e geridas através da Apple App Store ou do Google Play. O período de teste de 14 dias sem cartão, controlado pelo servidor do Cibello, aplica-se uma vez por identidade de e-mail num período de cinco anos. Uma conta eliminada pode ser criada de novo, mas não recebe automaticamente um novo período de teste gratuito. O preço, o período, a renovação automática e o cancelamento são apresentados pela respetiva loja antes da compra. Os reembolsos são tratados de acordo com as regras da loja e com o direito imperativo do consumidor.</p>

<h2>8. Utilização permitida</h2>
<p>O serviço não pode ser usado para conteúdos ilegais, violação de direitos, assédio, sobrecarga automatizada, contorno de mecanismos de segurança ou tentativas de extrair dados de outros utilizadores. O Cibello pode restringir contas em caso de risco de segurança ou de incumprimento substancial do contrato.</p>

<h2>9. Disponibilidade e alterações</h2>
<p>O serviço está em desenvolvimento contínuo e pode estar temporariamente indisponível. As funcionalidades podem ser alteradas por razões de segurança, legais, de qualidade ou técnicas. As alterações substanciais aos termos recebem um número de versão e exigem uma nova aceitação.</p>

<h2>10. Responsabilidade e direito imperativo</h2>
<p>A LandveX AB é responsável nos termos da lei imperativa aplicável. Nada nestes termos limita direitos que não possam ser legalmente afastados por acordo. Aplica-se a lei sueca, e o consumidor pode também invocar o direito imperativo e o tribunal competente do seu país de residência.</p>

<h2>11. Contacto</h2>
<p>Apoio: <a href="mailto:support@cibello.app">support@cibello.app</a>. Privacidade: <a href="mailto:privacy@cibello.app">privacy@cibello.app</a>.</p>""",
)

DELETE = dict(
    title="Apagar conta e dados – Cibello",
    desc="Como apagar a tua conta Cibello e os dados pessoais associados diretamente na app.",
    h1="Apagar conta e dados",
    body="""<h2>Diretamente na app</h2>
<ol>
<li>Inicia sessão no Cibello.</li>
<li>Abre <strong>Perfil</strong>.</li>
<li>Escolhe <strong>Apagar conta</strong> e confirma.</li>
</ol>
<p>A conta, a identidade Firebase, as imagens ativas e os dados pessoais da app são apagados. As referências de transações financeiras podem ser pseudonimizadas e conservadas quando a lei o exigir. As cópias de segurança são eliminadas por rotação de acordo com a retenção documentada.</p>

<h2>Se não conseguires abrir a app</h2>
<p>Envia o pedido a partir do endereço de e-mail registado na conta para <a href="mailto:privacy@cibello.app?subject=Apagar%20a%20minha%20conta%20Cibello">privacy@cibello.app</a>. Escreve “Apagar a minha conta Cibello”. Verificamos que controlas o endereço antes de apagar.</p>

<h2>Dados de treino</h2>
<p>Ao apagar a conta, as correções do utilizador e as referências às imagens são removidas do banco de treino ativo. As respostas do Gemini nunca foram exportadas como dados de referência para o treino da Cibello AI. Os parâmetros de modelo já agregados normalmente não podem ser associados de novo a uma pessoa.</p>""",
)

UI = dict(
    faq_title="Perguntas frequentes",
    privacy_nav="Política de privacidade",
    terms_nav="Termos de utilização",
    delete_nav="Apagar conta",
    legal_meta="Cibello · versão 2.0 · em vigor desde 30 de agosto de 2026 · tradução portuguesa",
    translation_label="Sobre esta tradução:",
    translation_note='Esta é uma tradução portuguesa do original sueco (<a href="{sv}" lang="sv">original</a>). Em caso de divergência, prevalece a versão sueca.',
)
