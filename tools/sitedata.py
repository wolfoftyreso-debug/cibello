# Shared labels + site structure for Cibello page patching/generation.
APP_STORE = "https://apps.apple.com/app/id6807100747"
PLAY_STORE = "https://play.google.com/store/apps/details?id=com.cibello.app"
TODAY = "2026-09-04"

MARK_SVG = '<svg width="18" height="18" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 6c4.4 0 8 3.4 8 8 0 5.6-8 12-8 12S8 19.6 8 14c0-4.6 3.6-8 8-8z" fill="#fff"/><circle cx="16" cy="14" r="2.6" fill="#2f7d51"/></svg>'
APPLE_SVG = '<svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M16.4 12.7c0-2 1.6-3 1.7-3.1-.9-1.4-2.4-1.6-2.9-1.6-1.2-.1-2.4.7-3 .7-.6 0-1.6-.7-2.6-.7-1.3 0-2.6.8-3.3 2-1.4 2.4-.4 6 1 8 .7 1 1.4 2 2.4 2 1 0 1.3-.6 2.5-.6 1.2 0 1.5.6 2.5.6 1 0 1.7-.9 2.3-1.9.7-1.1 1-2.2 1-2.3-.1 0-2-.8-2.1-3.1zM14.6 6.3c.5-.7.9-1.6.8-2.5-.8 0-1.7.5-2.3 1.2-.5.6-.9 1.5-.8 2.4.9.1 1.8-.4 2.3-1.1z"/></svg>'
PLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 3.5v17c0 .5.5.8.9.5l9.3-8.5-9.3-8.5c-.4-.3-.9 0-.9.5z" fill="#34d399"/><path d="M14.2 12.5l2.7-2.5 3.6 2c.6.4.6 1.2 0 1.6l-3.6 2-2.7-2.5z" fill="#fbbf24"/><path d="M4.9 20.5l9.3-8-2.7-2.5-6.6 6c-.4.3-.4.9 0 .5z" fill="#f87171"/><path d="M4.9 3.5l9.3 8-2.7 2.5-6.6-6c-.4-.3-.4-.9 0-.5z" fill="#60a5fa"/></svg>'

LANG_NAMES = {"sv":"Svenska","en":"English","de":"Deutsch","fr":"Français","es":"Español","it":"Italiano","nl":"Nederlands","pl":"Polski","da":"Dansk","nb":"Norsk","fi":"Suomi","pt":"Português"}
OG_LOCALE = {"sv":"sv_SE","en":"en_US","de":"de_DE","fr":"fr_FR","es":"es_ES","it":"it_IT","nl":"nl_NL","pl":"pl_PL","da":"da_DK","nb":"nb_NO","fi":"fi_FI","pt":"pt_PT"}

# UI strings per language
T = {
 "sv": dict(home="Startsida", guides="Guider", langs="Språk", company="Företag", privacy="Integritet", terms="Villkor", delete="Radera konto", contact="Kontakt", get_app="Skaffa appen", how="Så funkar det", features="Funktioner", dl_apple="Ladda ner på", dl_google="Hämta på", crumbs="Brödsmulor", nav="Huvudmeny", footnav="Sidfot", tagline="Din Food Twin. Appen som känner ditt kök och tar bort ”vad ska vi äta?”-stressen.", disclaimer="Recept och förslag är vägledning, inte medicinsk rådgivning. Har du en allergi – kontrollera alltid ingredienserna själv.", made="Byggd i Sverige.", cta_h="Prova Cibello gratis", cta_p="Fota kylen, få middagstips från det du har hemma och dela inköpslistan med hushållet.", more="Mer om smartare vardagsmat", other_langs="Andra språk", updated="Uppdaterad"),
 "en": dict(home="Home", guides="Guides", langs="Languages", company="Company", privacy="Privacy", terms="Terms", delete="Delete account", contact="Contact", get_app="Get the app", how="How it works", features="Features", dl_apple="Download on the", dl_google="Get it on", crumbs="Breadcrumb", nav="Main menu", footnav="Footer", tagline="Your Food Twin. The app that knows your kitchen and removes the “what should we eat?” stress.", disclaimer="Recipes and suggestions are guidance, not medical advice. If you have an allergy, always check the ingredients yourself.", made="Built in Sweden.", cta_h="Try Cibello for free", cta_p="Snap your fridge, get dinner ideas from what you already have and share the shopping list with your household.", more="Practical guides", other_langs="Other languages", updated="Updated"),
 "de": dict(home="Startseite", guides="Ratgeber", langs="Sprachen", company="Unternehmen", privacy="Datenschutz", terms="AGB", delete="Konto löschen", contact="Kontakt", get_app="App holen", how="So funktioniert es", features="Funktionen", dl_apple="Laden im", dl_google="Jetzt bei", crumbs="Brotkrumen", nav="Hauptmenü", footnav="Fußzeile", tagline="Dein Food Twin. Die App, die deine Küche kennt und die Frage „Was essen wir?“ entspannt.", disclaimer="Rezepte und Vorschläge sind Orientierung, keine medizinische Beratung. Bei Allergien immer selbst die Zutaten prüfen.", made="Entwickelt in Schweden.", cta_h="Cibello kostenlos testen", cta_p="Kühlschrank fotografieren, Rezeptideen aus dem erhalten, was du hast, und die Einkaufsliste mit dem Haushalt teilen.", more="Praktische Ratgeber", other_langs="Andere Sprachen", updated="Aktualisiert"),
 "fr": dict(home="Accueil", guides="Guides", langs="Langues", company="Entreprise", privacy="Confidentialité", terms="Conditions", delete="Supprimer le compte", contact="Contact", get_app="Télécharger l’app", how="Comment ça marche", features="Fonctionnalités", dl_apple="Télécharger dans l’", dl_google="Disponible sur", crumbs="Fil d’Ariane", nav="Menu principal", footnav="Pied de page", tagline="Votre Food Twin. L’app qui connaît votre cuisine et supprime le stress du « qu’est-ce qu’on mange ? ».", disclaimer="Les recettes et suggestions sont indicatives, pas un avis médical. En cas d’allergie, vérifiez toujours les ingrédients vous-même.", made="Conçu en Suède.", cta_h="Essayez Cibello gratuitement", cta_p="Photographiez votre frigo, recevez des idées de repas avec ce que vous avez et partagez la liste de courses avec votre foyer.", more="Guides pratiques", other_langs="Autres langues", updated="Mis à jour"),
 "es": dict(home="Inicio", guides="Guías", langs="Idiomas", company="Empresa", privacy="Privacidad", terms="Condiciones", delete="Eliminar cuenta", contact="Contacto", get_app="Descargar la app", how="Cómo funciona", features="Funciones", dl_apple="Descargar en", dl_google="Disponible en", crumbs="Ruta de navegación", nav="Menú principal", footnav="Pie de página", tagline="Tu Food Twin. La app que conoce tu cocina y elimina el estrés de «¿qué comemos?».", disclaimer="Las recetas y sugerencias son orientativas, no consejo médico. Si tienes alergia, comprueba siempre los ingredientes.", made="Creado en Suecia.", cta_h="Prueba Cibello gratis", cta_p="Fotografía tu nevera, recibe ideas de cena con lo que ya tienes y comparte la lista de la compra con tu hogar.", more="Guías prácticas", other_langs="Otros idiomas", updated="Actualizado"),
 "it": dict(home="Home", guides="Guide", langs="Lingue", company="Azienda", privacy="Privacy", terms="Termini", delete="Elimina account", contact="Contatti", get_app="Scarica l’app", how="Come funziona", features="Funzioni", dl_apple="Scarica su", dl_google="Disponibile su", crumbs="Percorso", nav="Menu principale", footnav="Piè di pagina", tagline="Il tuo Food Twin. L’app che conosce la tua cucina e toglie lo stress del «cosa mangiamo?».", disclaimer="Ricette e suggerimenti sono indicazioni, non consigli medici. In caso di allergie controlla sempre gli ingredienti.", made="Creato in Svezia.", cta_h="Prova Cibello gratis", cta_p="Fotografa il frigo, ricevi idee per la cena con quello che hai già e condividi la lista della spesa con la famiglia.", more="Guide pratiche", other_langs="Altre lingue", updated="Aggiornato"),
 "nl": dict(home="Home", guides="Gidsen", langs="Talen", company="Bedrijf", privacy="Privacy", terms="Voorwaarden", delete="Account verwijderen", contact="Contact", get_app="Download de app", how="Zo werkt het", features="Functies", dl_apple="Download in de", dl_google="Ontdek het op", crumbs="Kruimelpad", nav="Hoofdmenu", footnav="Voettekst", tagline="Je Food Twin. De app die je keuken kent en de ‘wat eten we?’-stress wegneemt.", disclaimer="Recepten en suggesties zijn richtlijnen, geen medisch advies. Heb je een allergie, controleer dan altijd zelf de ingrediënten.", made="Gemaakt in Zweden.", cta_h="Probeer Cibello gratis", cta_p="Fotografeer je koelkast, krijg ideeën voor het avondeten met wat je al hebt en deel de boodschappenlijst met je huishouden.", more="Praktische gidsen", other_langs="Andere talen", updated="Bijgewerkt"),
 "pl": dict(home="Start", guides="Poradniki", langs="Języki", company="Firma", privacy="Prywatność", terms="Regulamin", delete="Usuń konto", contact="Kontakt", get_app="Pobierz aplikację", how="Jak to działa", features="Funkcje", dl_apple="Pobierz w", dl_google="Pobierz z", crumbs="Okruszki", nav="Menu główne", footnav="Stopka", tagline="Twój Food Twin. Aplikacja, która zna Twoją kuchnię i zdejmuje stres pytania „co jemy?”.", disclaimer="Przepisy i sugestie to wskazówki, nie porada medyczna. Jeśli masz alergię, zawsze sprawdzaj składniki samodzielnie.", made="Stworzone w Szwecji.", cta_h="Wypróbuj Cibello za darmo", cta_p="Zrób zdjęcie lodówki, otrzymaj pomysły na obiad z tego, co masz, i dziel listę zakupów z domownikami.", more="Praktyczne poradniki", other_langs="Inne języki", updated="Zaktualizowano"),
 "da": dict(home="Forside", guides="Guider", langs="Sprog", company="Virksomhed", privacy="Privatliv", terms="Vilkår", delete="Slet konto", contact="Kontakt", get_app="Hent appen", how="Sådan virker det", features="Funktioner", dl_apple="Hent i", dl_google="Hent på", crumbs="Brødkrummer", nav="Hovedmenu", footnav="Sidefod", tagline="Din Food Twin. Appen der kender dit køkken og fjerner ”hvad skal vi spise?”-stressen.", disclaimer="Opskrifter og forslag er vejledende, ikke medicinsk rådgivning. Har du en allergi, så tjek altid ingredienserne selv.", made="Bygget i Sverige.", cta_h="Prøv Cibello gratis", cta_p="Tag et billede af køleskabet, få aftensmadsidéer ud fra det du allerede har, og del indkøbslisten med husstanden.", more="Praktiske guider", other_langs="Andre sprog", updated="Opdateret"),
 "nb": dict(home="Hjem", guides="Guider", langs="Språk", company="Selskap", privacy="Personvern", terms="Vilkår", delete="Slett konto", contact="Kontakt", get_app="Last ned appen", how="Slik fungerer det", features="Funksjoner", dl_apple="Last ned fra", dl_google="Få den på", crumbs="Brødsmuler", nav="Hovedmeny", footnav="Bunntekst", tagline="Din Food Twin. Appen som kjenner kjøkkenet ditt og fjerner «hva skal vi spise?»-stresset.", disclaimer="Oppskrifter og forslag er veiledende, ikke medisinske råd. Har du en allergi, sjekk alltid ingrediensene selv.", made="Bygget i Sverige.", cta_h="Prøv Cibello gratis", cta_p="Ta bilde av kjøleskapet, få middagsidéer fra det du allerede har, og del handlelisten med husstanden.", more="Praktiske guider", other_langs="Andre språk", updated="Oppdatert"),
 "fi": dict(home="Etusivu", guides="Oppaat", langs="Kielet", company="Yritys", privacy="Tietosuoja", terms="Käyttöehdot", delete="Poista tili", contact="Yhteystiedot", get_app="Hanki sovellus", how="Näin se toimii", features="Ominaisuudet", dl_apple="Lataa", dl_google="Hanki se", crumbs="Murupolku", nav="Päävalikko", footnav="Alatunniste", tagline="Sinun Food Twin. Sovellus, joka tuntee keittiösi ja poistaa ”mitä syötäisiin?” -stressin.", disclaimer="Reseptit ja ehdotukset ovat ohjeellisia, eivät lääketieteellisiä neuvoja. Jos sinulla on allergia, tarkista ainesosat aina itse.", made="Tehty Ruotsissa.", cta_h="Kokeile Cibelloa ilmaiseksi", cta_p="Kuvaa jääkaappi, saa ruokaideoita siitä mitä sinulla jo on, ja jaa ostoslista kotitalouden kanssa.", more="Käytännön oppaat", other_langs="Muut kielet", updated="Päivitetty"),
 "pt": dict(home="Início", guides="Guias", langs="Idiomas", company="Empresa", privacy="Privacidade", terms="Termos", delete="Eliminar conta", contact="Contacto", get_app="Obter a app", how="Como funciona", features="Funcionalidades", dl_apple="Descarregar na", dl_google="Disponível no", crumbs="Navegação estrutural", nav="Menu principal", footnav="Rodapé", tagline="O teu Food Twin. A app que conhece a tua cozinha e elimina o stress do «o que vamos comer?».", disclaimer="Receitas e sugestões são orientações, não aconselhamento médico. Se tens alergias, verifica sempre os ingredientes.", made="Criado na Suécia.", cta_h="Experimenta o Cibello grátis", cta_p="Fotografa o frigorífico, recebe ideias de jantar com o que já tens e partilha a lista de compras com a tua casa.", more="Guias práticos", other_langs="Outros idiomas", updated="Atualizado"),
}

# Guides per language: (path, short label). Swedish list includes the new pages.
GUIDES = {
 "sv": [("/middagstips/","Middagstips"),("/vad-ska-vi-ata/","Vad ska vi äta idag?"),("/veckomeny/","Veckomeny"),("/vardagsmat/","Vardagsmat"),("/snabb-middag/","Snabb &amp; enkel middag"),("/middagstips-barnfamilj/","Middagstips för barnfamiljen"),("/matlador/","Matlådor"),("/billig-mat/","Billig mat för en vecka"),("/inkopslista/","Inköpslista"),("/bast-fore-datum/","Bäst före-datum"),("/matsvinn/","Minska matsvinn"),("/matapp/","Matapp")],
 "en": [("/en/meal-planner/","Meal planner"),("/en/recipes-with-ingredients/","Recipes with ingredients you have"),("/en/what-to-eat-tonight/","What to eat tonight"),("/en/ai-meal-planner/","AI meal planner"),("/en/pantry-app/","Pantry app"),("/en/reduce-food-waste/","Reduce food waste")],
 "de": [("/de/essensplaner/","Essensplaner"),("/de/rezepte-mit-zutaten/","Rezepte mit Zutaten"),("/de/lebensmittelverschwendung-reduzieren/","Weniger Lebensmittelverschwendung")],
 "fr": [("/fr/planificateur-repas/","Planificateur de repas"),("/fr/recettes-avec-ingredients/","Recettes avec vos ingrédients"),("/fr/reduire-gaspillage-alimentaire/","Moins de gaspillage alimentaire")],
 "es": [("/es/planificador-comidas/","Planificador de comidas"),("/es/recetas-con-ingredientes/","Recetas con tus ingredientes"),("/es/reducir-desperdicio-alimentario/","Menos desperdicio alimentario")],
 "it": [("/it/pianificatore-pasti/","Pianificatore pasti"),("/it/ricette-con-ingredienti/","Ricette con ingredienti"),("/it/ridurre-spreco-alimentare/","Meno spreco alimentare")],
 "nl": [("/nl/maaltijdplanner/","Maaltijdplanner"),("/nl/recepten-met-ingredienten/","Recepten met ingrediënten"),("/nl/voedselverspilling-verminderen/","Minder voedselverspilling")],
 "pl": [("/pl/planer-posilkow/","Planer posiłków"),("/pl/przepisy-z-produktow/","Przepisy z produktów"),("/pl/ograniczanie-marnowania-zywnosci/","Mniej marnowania żywności")],
 "da": [("/da/madplan/","Madplan"),("/da/opskrifter-med-ingredienser/","Opskrifter med ingredienser"),("/da/mindske-madspild/","Mindre madspild")],
 "nb": [("/nb/matplanlegger/","Matplanlegger"),("/nb/oppskrifter-med-ingredienser/","Oppskrifter med ingredienser"),("/nb/redusere-matsvinn/","Mindre matsvinn")],
 "fi": [("/fi/ateriasuunnittelu/","Ateriasuunnittelu"),("/fi/reseptit-aineksista/","Reseptit aineksista"),("/fi/vahenna-ruokahavikkia/","Vähemmän ruokahävikkiä")],
 "pt": [("/pt/planeador-refeicoes/","Planeador de refeições"),("/pt/receitas-com-ingredientes/","Receitas com ingredientes"),("/pt/reduzir-desperdicio-alimentar/","Menos desperdício alimentar")],
}
def home_of(lang): return "/" if lang == "sv" else f"/{lang}/"

def store_badges(lang, cls="stores"):
    t = T[lang]
    return (f'<div class="{cls}">'
            f'<a href="{APP_STORE}" class="store" rel="noopener" hreflang="{lang}">{APPLE_SVG}<span><small>{t["dl_apple"]}</small><b>App Store</b></span></a>'
            f'<a href="{PLAY_STORE}" class="store" rel="noopener" hreflang="{lang}">{PLAY_SVG}<span><small>{t["dl_google"]}</small><b>Google Play</b></span></a>'
            f'</div>')

def header(lang):
    t = T[lang]; home = home_of(lang)
    nav_items = "".join(f'<a href="{p}">{l}</a>' for p, l in GUIDES[lang][:4])
    if lang != "sv":
        nav_items = f'<a href="{home}">{t["home"]}</a>' + nav_items[:0] + "".join(f'<a href="{p}">{l}</a>' for p, l in GUIDES[lang][:3])
    return (f'<header class="top"><div class="wrap">'
            f'<a class="brand" href="{home}"><span class="mark">{MARK_SVG}</span>Cibello</a>'
            f'<nav class="topnav" aria-label="{t["nav"]}">{nav_items}</nav>'
            f'<a class="cta" href="#app">{t["get_app"]}</a>'
            f'</div></header>')

def crumbs(lang, label):
    t = T[lang]; home = home_of(lang)
    home_label = "Cibello" if lang == "sv" else f"Cibello {LANG_NAMES[lang]}"
    return f'<nav class="crumbs" aria-label="{t["crumbs"]}"><a href="{home}">{home_label}</a><span aria-hidden="true">›</span><span aria-current="page">{label}</span></nav>'

SOCIAL = ('<div class="social">'
  '<a href="https://www.facebook.com/profile.php?id=61593336222919" aria-label="Facebook" target="_blank" rel="noopener noreferrer"><svg width="18" height="18" viewBox="0 0 24 24" fill="#fff"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5 3.66 9.15 8.44 9.94v-7.03H7.9v-2.9h2.54V9.85c0-2.51 1.49-3.9 3.78-3.9 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 2.9h-2.34V22c4.78-.79 8.44-4.94 8.44-9.94z"/></svg></a>'
  '<a href="https://www.instagram.com/cibelloapp/" aria-label="Instagram" target="_blank" rel="noopener noreferrer"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="#fff" stroke="none"/></svg></a>'
  '<a href="https://www.tiktok.com/@cibello73" aria-label="TikTok" target="_blank" rel="noopener noreferrer"><svg width="18" height="18" viewBox="0 0 24 24" fill="#fff"><path d="M21 8.5a6.3 6.3 0 0 1-3.7-1.2v6.9A5.6 5.6 0 1 1 11.7 8.6c.3 0 .6 0 .9.1v2.9a2.7 2.7 0 1 0 1.9 2.6V2h2.8A3.9 3.9 0 0 0 21 5.6V8.5z"/></svg></a>'
  '</div>')

def footer(lang):
    t = T[lang]; home = home_of(lang)
    guides = "".join(f'<a href="{p}">{l}</a>' for p, l in GUIDES[lang])
    langs = "".join(f'<a href="{home_of(c)}" lang="{c}" hreflang="{c}">{n}</a>' for c, n in LANG_NAMES.items())
    return (f'<footer class="foot"><div class="wrap foot-grid">'
            f'<div><a class="brand" href="{home}"><span class="mark">{MARK_SVG}</span>Cibello</a><p class="foot-tag">{t["tagline"]}</p>{SOCIAL}{store_badges(lang, "foot-stores")}</div>'
            f'<nav aria-label="{t["guides"]}"><h3>{t["guides"]}</h3>{guides}</nav>'
            f'<nav aria-label="{t["langs"]}"><h3>{t["langs"]}</h3>{langs}</nav>'
            f'<nav aria-label="{t["company"]}"><h3>{t["company"]}</h3><a href="/integritet.html">{t["privacy"]}</a><a href="/villkor.html">{t["terms"]}</a><a href="/delete-account.html">{t["delete"]}</a><a href="mailto:hello@cibello.app">{t["contact"]}</a></nav>'
            f'</div><div class="wrap foot-bottom"><p>{t["disclaimer"]}</p><p>© 2026 Cibello · LandveX AB · Org.nr 559141-7042 · Antennvägen 2, 135&nbsp;48 Tyresö · {t["made"]}</p></div></footer>')

def cta_block(lang, h=None, p=None):
    t = T[lang]
    return f'<section class="cta" id="app"><h2>{h or t["cta_h"]}</h2><p>{p or t["cta_p"]}</p>{store_badges(lang)}</section>'

def head_extras(lang, og_image=None):
    img = og_image or ("https://cibello.app/img/og.png" if lang == "sv" else "https://cibello.app/img/og-en.png")
    alt = "Cibello – vad ska vi äta imorgon?" if lang == "sv" else "Cibello – what should we eat tomorrow?"
    return ('<link rel="icon" href="/favicon.svg" type="image/svg+xml">'
            '<link rel="icon" href="/img/icon-192.png" type="image/png" sizes="192x192">'
            '<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">'
            '<link rel="manifest" href="/manifest.webmanifest">'
            '<meta name="apple-itunes-app" content="app-id=6807100747">'
            f'<meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{alt}">'
            f'<meta name="twitter:image" content="{img}">')

ORG = {"@type":"Organization","@id":"https://cibello.app/#organization","name":"LandveX AB","alternateName":"Cibello","url":"https://cibello.app/","logo":{"@type":"ImageObject","url":"https://cibello.app/img/icon-512.png","width":512,"height":512},"email":"hello@cibello.app","address":{"@type":"PostalAddress","streetAddress":"Antennvägen 2","postalCode":"135 48","addressLocality":"Tyresö","addressCountry":"SE"},"sameAs":["https://www.facebook.com/profile.php?id=61593336222919","https://www.instagram.com/cibelloapp/","https://www.tiktok.com/@cibello73",APP_STORE,PLAY_STORE],"brand":{"@type":"Brand","name":"Cibello"}}

def app_node(lang):
    desc = {
      "sv":"Matapp som skannar kyl och skafferi, föreslår recept från det du har hemma, bygger veckomeny och delar inköpslista med hushållet.",
      "en":"Meal planner and recipe app that scans your fridge and pantry, suggests recipes from what you have, builds a weekly meal plan and shares a shopping list with your household.",
    }.get(lang, "Meal planner and recipe app that scans your fridge and pantry, suggests recipes from what you have, builds a weekly meal plan and shares a shopping list with your household.")
    return {"@type":["SoftwareApplication","MobileApplication"],"@id":"https://cibello.app/#app","name":"Cibello","description":desc,"applicationCategory":"LifestyleApplication","operatingSystem":["iOS","Android"],"inLanguage":list(LANG_NAMES.keys()),"offers":{"@type":"Offer","price":"0","priceCurrency":"SEK","description":"Free trial; household features require a paid plan after the trial."},"installUrl":[APP_STORE,PLAY_STORE],"downloadUrl":[APP_STORE,PLAY_STORE],"screenshot":"https://cibello.app/img/og.png","image":"https://cibello.app/img/icon-512.png","author":{"@id":"https://cibello.app/#organization"},"publisher":{"@id":"https://cibello.app/#organization"},"featureList":["AI scanning of fridge, pantry, receipts and barcodes","Food inventory (Food Twin)","Recipes with ingredients you have (9,000+)","Weekly meal planner","Shared household shopping list","Expiry reminders to reduce food waste","12 languages","Data stored in the EU"]}

# --- Site structure additions (rounds 3-4) ---
GUIDES["sv"].insert(1, ("/middagstips-vardag/", "Middagstips för vardag"))
GUIDES["sv"].insert(2, ("/middagstips-helg/", "Middagstips för helg"))
GUIDES["sv"].insert(4, ("/vad-ska-jag-ata-till-middag/", "Vad ska jag äta till middag ikväll?"))
GUIDES["sv"].append(("/matsvinn-statistik/", "Matsvinn i Sverige: siffror"))
GUIDES["sv"].append(("/basta-matapp/", "Bästa matappen? Jämförelse"))
GUIDES["en"].append(("/en/best-meal-planning-app/", "Best meal planning app? Comparison"))
GUIDES["en"].append(("/en/best-recipe-app/", "Best recipe app? Comparison"))
ABOUT = {"sv":"Om Cibello","en":"About Cibello","de":"Über Cibello","fr":"À propos","es":"Sobre Cibello","it":"Chi siamo","nl":"Over Cibello","pl":"O Cibello","da":"Om Cibello","nb":"Om Cibello","fi":"Tietoa Cibellosta","pt":"Sobre o Cibello"}
PRESS = {"sv":"Press","en":"Press","de":"Presse","fr":"Presse","es":"Prensa","it":"Stampa","nl":"Pers","pl":"Prasa","da":"Presse","nb":"Presse","fi":"Media","pt":"Imprensa"}
SKIP = {"sv":"Hoppa till innehåll","en":"Skip to content","de":"Zum Inhalt springen","fr":"Aller au contenu","es":"Saltar al contenido","it":"Vai al contenuto","nl":"Naar inhoud","pl":"Przejdź do treści","da":"Spring til indhold","nb":"Hopp til innhold","fi":"Siirry sisältöön","pt":"Saltar para o conteúdo"}
HOME_UI = {
 "sv": dict(menu="Meny", close="Stäng", guides_kicker="Guider för en enklare matvardag", guides_h="Vad vill du ha hjälp med?", guides_p="Läs hur Cibello kan hjälpa med middagsidéer, veckoplanering, matlådor, inköpslista och mindre matsvinn.", stats="Cibello i siffror"),
 "en": dict(menu="Menu", close="Close", guides_kicker="Guides for an easier food routine", guides_h="What do you need help with?", guides_p="Read how Cibello helps with dinner ideas, weekly planning, your pantry and less food waste.", stats="Cibello in numbers"),
 "de": dict(menu="Menü", close="Schließen", guides_kicker="Ratgeber für einen einfacheren Küchenalltag", guides_h="Wobei brauchst du Hilfe?", guides_p="Lies, wie Cibello bei Rezeptideen, Wochenplanung, Vorrat und weniger Lebensmittelverschwendung hilft.", stats="Cibello in Zahlen"),
 "fr": dict(menu="Menu", close="Fermer", guides_kicker="Guides pour un quotidien plus simple en cuisine", guides_h="De quoi avez-vous besoin ?", guides_p="Découvrez comment Cibello aide pour les idées de repas, le planning de la semaine, le garde-manger et moins de gaspillage.", stats="Cibello en chiffres"),
 "es": dict(menu="Menú", close="Cerrar", guides_kicker="Guías para una cocina diaria más fácil", guides_h="¿Con qué necesitas ayuda?", guides_p="Lee cómo Cibello ayuda con ideas de cena, planificación semanal, despensa y menos desperdicio.", stats="Cibello en cifras"),
 "it": dict(menu="Menu", close="Chiudi", guides_kicker="Guide per una cucina quotidiana più semplice", guides_h="Con cosa ti serve aiuto?", guides_p="Scopri come Cibello aiuta con idee per la cena, pianificazione settimanale, dispensa e meno spreco.", stats="Cibello in cifre"),
 "nl": dict(menu="Menu", close="Sluiten", guides_kicker="Gidsen voor een makkelijker eetritme", guides_h="Waar heb je hulp bij nodig?", guides_p="Lees hoe Cibello helpt met ideeën voor het avondeten, weekplanning, voorraad en minder verspilling.", stats="Cibello in cijfers"),
 "pl": dict(menu="Menu", close="Zamknij", guides_kicker="Poradniki na prostszą codzienność w kuchni", guides_h="W czym potrzebujesz pomocy?", guides_p="Przeczytaj, jak Cibello pomaga z pomysłami na obiad, planowaniem tygodnia, spiżarnią i mniejszym marnowaniem.", stats="Cibello w liczbach"),
 "da": dict(menu="Menu", close="Luk", guides_kicker="Guider til en nemmere madhverdag", guides_h="Hvad vil du have hjælp til?", guides_p="Læs hvordan Cibello hjælper med aftensmadsidéer, ugeplanlægning, madlager og mindre madspild.", stats="Cibello i tal"),
 "nb": dict(menu="Meny", close="Lukk", guides_kicker="Guider til en enklere mathverdag", guides_h="Hva vil du ha hjelp med?", guides_p="Les hvordan Cibello hjelper med middagsidéer, ukeplanlegging, matlager og mindre matsvinn.", stats="Cibello i tall"),
 "fi": dict(menu="Valikko", close="Sulje", guides_kicker="Oppaat helpompaan ruoka-arkeen", guides_h="Missä tarvitset apua?", guides_p="Lue, miten Cibello auttaa ruokaideoissa, viikkosuunnittelussa, ruokavarastossa ja hävikin vähentämisessä.", stats="Cibello numeroina"),
 "pt": dict(menu="Menu", close="Fechar", guides_kicker="Guias para um dia a dia mais simples na cozinha", guides_h="Com o que precisas de ajuda?", guides_p="Lê como o Cibello ajuda com ideias de jantar, planeamento semanal, despensa e menos desperdício.", stats="Cibello em números"),
}
