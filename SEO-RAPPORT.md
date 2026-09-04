# SEO- och designgenomgång av cibello.app

Datum: 2026-09-04. Underlag: Semrush (databas SE och US) och Mobbin (webbsektioner för app-landningssidor).

## 1. Vad som var fel innan

| Problem | Effekt | Åtgärd |
|---|---|---|
| Startsidan byttes automatiskt till besökarens webbläsarspråk med JS | Googlebot renderar med engelsk locale och såg en engelsk sida på den svenska canonical-URL:en, i strid med `lang="sv"` och hreflang | Ingen automatisk översättning vid inläsning. Tidigare val sparas i localStorage; övriga får en banner med knappen "Switch to English" |
| Ingen `og:image`, ingen manifest, ingen apple-touch-icon | Delningar på sociala medier utan bild, ingen ikon på hemskärm, ingen Smart App Banner i Safari | Genererade OG-bilder (sv + en), ikoner 192/512/180, `manifest.webmanifest`, `apple-itunes-app`-meta |
| Guide-sidornas CTA länkade till `/#funktioner` i stället för till appbutikerna | Konverteringsläcka på alla 53 guide-sidor | CTA-block med App Store- och Google Play-knappar på alla guide-sidor, samt "Skaffa appen" i sidhuvudet |
| Tunn sidfot och sidhuvud på guide-sidorna ("Till startsidan" som enda länk) | Svag intern länkning, ingen navigering | Gemensamt sidhuvud med navigering, brödsmulor, sidfot med kolumnerna Guider / Språk / Företag på alla sidor |
| Ingen FAQ på startsidan | Missade frågeformulerade sökningar och rich results | FAQ-sektion med sex frågor, översatt till 12 språk, med `FAQPage`-schema |
| Ingen `SoftwareApplication`-markup | Google förstår inte att sajten handlar om en app | `SoftwareApplication`/`MobileApplication` med installUrl, plattformar, funktionslista; `Organization` med logo, adress och sameAs |
| Ingen mobilmeny på startsidan | Navigeringen försvann under 820 px | Hamburgermeny |
| Inga sidor för de största sökorden i nischen | Se tabellen nedan | Sju nya svenska och tre nya engelska guider |

## 2. Semrush – svenska nyckelord (volym/mån, KD = svårighet 0–100)

| Nyckelord | Volym | KD | Sida |
|---|---|---|---|
| middagstips | 40 500 | 23 | `/middagstips/` (förstärkt med vardag/helg/barn) |
| vardagsmat | 8 100 | 17 | `/vardagsmat/` NY |
| enkel middag | 8 100 | 30 | `/snabb-middag/` NY |
| matlådor | 8 100 | 29 | `/matlador/` NY |
| middagstips helg | 5 400 | 18 | `/middagstips/` |
| middagstips vardag | 5 400 | 22 | `/middagstips/` |
| snabb middag | 4 400 | 31 | `/snabb-middag/` NY |
| vad ska vi äta idag | 4 400 | 26 | `/vad-ska-vi-ata/` (ny title) |
| billig mat | 4 400 | 33 | `/billig-mat/` NY |
| veckomeny | 3 600 | 24 | `/veckomeny/` |
| veckomatsedel | 3 600 | 18 | `/veckomeny/` (ny title + sektion) |
| vardagsmat recept | 2 400 | 16 | `/vardagsmat/` |
| matlåda recept | 2 400 | 18 | `/matlador/` |
| vad ska jag äta till middag | 2 400 | 28 | `/vad-ska-vi-ata/` |
| enkla middagstips | 2 400 | 27 | `/middagstips/` |
| matsvinn | 1 300 | 37 | `/matsvinn/` (ny sektion "Vad är matsvinn?") |
| billiga recept | 1 300 | 26 | `/billig-mat/` |
| inköpslista | 1 000 | 28 | `/inkopslista/` NY |
| bäst före datum | 1 000 | 21 | `/bast-fore-datum/` NY |
| veckans matsedel | 1 000 | 17 | `/veckomeny/` |
| middagsförslag | 1 000 | 22 | `/middagstips/` |
| middagstips barn / barnfamilj | 880 + 880 | 21–23 | `/middagstips-barnfamilj/` NY |
| sista förbrukningsdag | 480 | 17 | `/bast-fore-datum/` |
| billig mat för en vecka | 480 | 20 | `/billig-mat/` |
| veckomatsedel familj | 390 | 13 | `/middagstips-barnfamilj/` |
| matapp / matsvinn app / svinnsmart | 170 var | 23–35 | `/matapp/`, `/matsvinn/` |
| matplanering / måltidsplanering / inköpslista app / recept app | 110 var | 12–28 | `/matapp/`, `/inkopslista/` |

Hoppat över: "matsedel" (22 200) domineras av skolmatsedlar och har fel intention.

Konkurrenter i SERP för "middagstips": koket.se, ica.se, zeinaskitchen.se, coop.se, recept.se. De vinner på receptvolym. Cibellos vinkel är "tips utifrån det du har hemma" plus appen, vilket ingen av dem erbjuder. För "matapp" rankar Play Store, Too Good To Go, Karma och mealview.se.

## 3. Semrush – engelska nyckelord (US)

| Nyckelord | Volym | KD | Sida |
|---|---|---|---|
| meal planning app | 40 500 | 50 | `/en/`, `/en/meal-planner/` |
| what should i eat | 14 800 | 74 | för svårt just nu |
| meal planner | 9 900 | 49 | `/en/meal-planner/` |
| what to eat tonight | 2 400 | 44 | `/en/what-to-eat-tonight/` NY |
| best recipe app | 1 900 | 18 | kandidat för nästa sida |
| what can i make with what i have | 1 300 | 45 | `/en/recipes-with-ingredients/` |
| ai recipe generator | 1 300 | 35 | `/en/ai-meal-planner/` NY |
| meal planner app | 1 000 | 36 | `/en/meal-planner/` |
| ai meal planner | 590 | 31 | `/en/ai-meal-planner/` NY |
| pantry app | 390 | 30 | `/en/pantry-app/` NY |
| pantry inventory app | 320 | 49 | `/en/pantry-app/` |

## 4. Mobbin – designmönster som applicerats

- Hero för app-landningssidor (Zipline, Partiful, Riverside): rubrik, underrubrik, båda butiksknapparna och telefonmockup. Cibello hade detta; kompletterat med en siffror-rad under heron (9 000+ recept, 12 språk, EU-lagring, gratis provperiod) enligt mönstret hos Cash App och Revolut. Inga påhittade betyg eller citat: bara fakta som redan finns på sajten.
- Funktionsgrid med ikonkort (Aboard, Fluz): behålls.
- FAQ som accordion i fullbredd (Airtable, Dropbox, Canva): tillagd på startsidan.
- Sidfot med länkkolumner, språk, sociala ikoner och butiksknappar (Miro, Notion, Sprout Social): tillagd på alla sidor.
- Guide-sidor: navigering och CTA i sidhuvudet, brödsmulor, butiksknappar i CTA-blocket.

## 5. Teknisk SEO som nu finns på alla sidor

- Canonical, hreflang (reciprokt, verifierat av `tools/check.py`), `x-default`.
- `og:image` 1200×630, `twitter:card summary_large_image`, `og:locale`.
- JSON-LD: `Organization` (logo, adress, sameAs), `WebSite`, `SoftwareApplication`, `WebPage` med `dateModified`, `BreadcrumbList`, `FAQPage` på alla guider och startsidan.
- `manifest.webmanifest`, `favicon.svg`, ikoner, `apple-itunes-app` (Smart App Banner).
- `sitemap.xml` med hreflang-alternates och lastmod från git; `robots.txt`; `llms.txt` för AI-sök.
- `404.html` (noindex) med länkar vidare.
- Säkerhets- och cache-headers via `_headers` eller `vercel.json`.
- `main.js` laddas med `defer`.

## 6. Genomgång 2: prestanda, tillgänglighet, validitet, duplicerat innehåll

Mätt med Playwright, axe-core 4 (WCAG 2.1 AA + best practice) och html-validate på lokal server.

| Fynd | Före | Efter |
|---|---|---|
| Allt innehåll med `.reveal` var `opacity:0` tills JavaScript kört | Osynligt utan JS, LCP fördröjd | Animationen gäller bara när `html.js` finns (inline-skript med CSP-hash), `prefers-reduced-motion` respekteras |
| `@import` i tre CSS-filer | Två seriella nätverksanrop innan rendering | `tokens.css` länkas direkt i HTML före övriga CSS |
| `main.js` 86 kB med alla översättningar | Laddades av alla besökare | `main.js` 4,7 kB; `i18n.js` 83 kB laddas bara när ett annat språk väljs eller sparats. Startsidan: 109 kB → 27 kB |
| Startsidan saknade `<main>`, hero låg utanför `<main>` på guide-sidor | axe: landmark-fel | `<main id="main">` på alla sidor, hopplänk, synliga fokusmarkeringar |
| Små DOCTYPE, råa `&` i text | 89 valideringsfel | 0 fel i html-validate |
| 102 identiska stycken mellan språkhubbar och deras guider | Internt duplicerat innehåll, kannibalisering | Engelska hubben omskriven med unikt innehåll. Övriga hubbar och guider behåller första meningen och länkar till sidan som äger texten. Fem svenska guider fick unika avslutningsstycken |
| Ingen "Om oss"-sida | Svag E-E-A-T-signal | `/om/` och `/en/about/` med företagsuppgifter, AI-hållning, kontakt; länkade från alla sidfötter; `AboutPage`-schema |
| Ingen CSP | – | Content-Security-Policy i `_headers` och `vercel.json`; `.well-known/security.txt`; `_redirects` för `/index.html` |
| Google Play-länkar utan attribution | Installationer kunde inte kopplas till sajt/sida | `referrer=utm_source=cibello.app&utm_medium=web&utm_campaign=<sida>` på alla Play-länkar. App Store-länkar behöver ett provider token (pt) från App Store Connect för motsvarande |
| Språkväljaren hade `aria-label="Language"` på svensk sida | – | "Språk / Language", språkbannern har landmark |
| `delete-account.html` blandade engelska i `lang="sv"` | – | Engelsk sektion har `lang="en"` |

axe-core efter fixarna: 0 överträdelser på startsida, guide, hubb, juridik och 404.

Domänläge enligt Semrush (2026-09-04): Authority Score 0, 8 bakåtlänkar från 8 domäner (7 nofollow), inga organiska rankningar i den svenska databasen. Sajten är alltså tekniskt klar men har ingen auktoritet ännu. Punkt 7 nedan avgör hur snabbt det ändras.

Tunna sidor som återstår (huvudinnehåll under 300 ord): de finska, polska, tyska, nederländska och danska guiderna, samt alla språkhubbar utom den svenska och engelska (efter avdupliceringen är hubbarna 150–190 ord och fungerar som navigering). De är korrekta men korta. Rekommendation: låt en modersmålstalare bygga ut till 500+ ord per sida med lokala sökord, eller prioritera de marknader appen faktiskt satsar på och låt övriga vara.

## 7. Genomgång 3: konkurrentlandskapet

Källor: Semrush (SERP-ägare, bakåtlänkar, auktoritet; API-enheterna tog slut mitt i omgången så vissa rapporter saknas), Firecrawl-webbsök av apparnas egna sidor och butiksbeskrivningar, Mobbin för jämförelsemönster.

### Vem äger sökresultaten i Sverige

| Sökord | Topp 3 | Vad de erbjuder |
|---|---|---|
| middagstips (40 500) | koket.se, ica.se, zeinaskitchen.se | Receptsamlingar med hög auktoritet |
| veckomeny (3 600) | koket.se, ica.se, citygross.se | Färdiga veckomenyer, ofta kopplade till matkasse/butik |
| vad ska vi äta idag (4 400) | koket.se, vadfanskajaglagatillmiddag.nu, Facebook-grupper | Listor och en slump-generator |
| matapp (170) | Google Play, App Store (Too Good To Go), toogoodtogo.com, mealview.se | Butikslistningar och en svensk planeringsapp |
| matsvinn app (170) | Karma, Too Good To Go, digitalare.se | Överskottsmat från butiker, roundup-artiklar |
| recept app (110) | Recipe Keeper, Reddit, smakshare.com, Arla-appen, matlistan.se | Receptsamlingar och inköpslistor |

Slutsats: receptvolym vinner de stora orden, och där kan Cibello inte konkurrera på bredd. Ingen svensk aktör äger positionen "recept utifrån det du faktiskt har hemma, från ett foto". vadfanskajaglagatillmiddag.nu rankar tvåa på "vad ska vi äta idag" med en ren slump-generator, vilket visar att ett interaktivt verktyg slår långa texter för den intentionen.

### Direkta appkonkurrenter

| App | Marknad | Vad den gör | Vad den saknar mot Cibello | Auktoritet (Semrush) |
|---|---|---|---|---|
| Matlistan | SE, sedan 2014 | Delad inköpslista, receptsamling, planering | Inget matlager, inga förslag utifrån det man har, ingen AI-skanning | AS 16, 259 länkar, 158 domäner |
| SmakShare | SE (Gotland) | Spara recept (även från Instagram), veckomatsedel, inköpslista | Inget matlager, inga datum/påminnelser | AS 15, 2 132 länkar, 227 domäner |
| Mealview | SE | Matplanering, blogg | Oklart; liten närvaro | AS 7, 201 länkar, 130 domäner |
| Matsedeln – Måltidsplanerare | SE | Veckomeny, receptbok, inköpslista, gratis + premium | Inget matlager | – |
| Too Good To Go / Karma | SE + int. | Överskottsmat från butiker | Löser inte svinnet i hemmet | Mycket hög |
| SuperCook | Int. (svensk översättning) | Recept från ingredienser du skriver/dikterar, 11 miljoner recept, gratis | Manuellt lager, ingen plan, ingen hushållsdelning, inga datum | Mycket hög |
| Mealime | Int. | Guidade veckoplaner, automatisk lista, gratis + Pro | Vet inte vad du har, katalogen upprepar sig, inga egna recept | Hög |
| Samsung Food (ex-Whisk) | Int. | Spara recept, planera, lista, gratis + Plus | Manuellt, apparat-fokus | Hög |
| Plan to Eat / Paprika | Int. | Receptbibliotek, kalender, listor; abonnemang resp. engångsköp | Inget lager, ingen AI | Hög |
| Fridge AI, Pantry Pic, KitchenPal | Int., nya | Foto av kylen ger recept | Sällan varaktigt lager, plan eller hushåll | Låg |

Cibello: AS 0, 8 länkar. Sajten ligger alltså långt efter även små svenska konkurrenter i länkar, vilket är den enskilt viktigaste faktorn att åtgärda.

### Vad som byggdes utifrån detta

- `/basta-matapp/` – ärlig jämförelse Cibello vs SuperCook, Matlistan, SmakShare, Too Good To Go/Karma, ICA/Coop. Fångar "matlistan" (590), "karma app" (720), "matapp", "recept app" och jämförelseintentionen. Tabell med Ja/Nej/Delvis och källnot; anger också vad Cibello inte gör.
- `/en/best-meal-planning-app/` – jämförelse mot Mealime, Samsung Food, Plan to Eat, Paprika, SuperCook och fotoappar. Riktar "best meal planning app" (1 000, KD 37), "best recipe app" (1 900, KD 18), "free meal planning app" (1 000).
- `/vad-ska-jag-ata-till-middag/` – frågesida med Middagsväljaren (slumpar bland 40 rätter efter protein, tid och läge, ingen inloggning). Riktar "vad ska jag äta till middag" (2 400), "vad fan ska jag laga till middag" (390), "vad kan man äta till middag" (320), "vad ska jag laga till middag" (260), "middag ikväll" (260), "vad ska jag äta ikväll" (210).
- Startsidan: sektionen "Receptappar vet inte vad du har hemma. Cibello gör det." (tre kort, översatt till tolv språk, länk till rätt jämförelse per språk).
- Jämförelsesidorna länkas från sidhuvud, sidfot och asides på alla sidor.

### Länkprospekt

Domäner som redan länkar till svenska matappar och därför sannolikt länkar till Cibello med rätt pitch: lchfarkivet.se (AS 39), theresematochbak.se (AS 18), digitalare.se (roundup "fem bra appar mot matsvinn"), warpnews.se (skrev om recept-från-ingredienser-appar), swedroid.se (forumtråd "tips på svensk matapp"), Sveriges Radio och SVT lokalt (har rapporterat om matappar mot svinn). Pitcha vinkeln "svensk app som fotar kylen" och siffror om hushållens matsvinn.

## 8. Genomgång 4: länkbart material, fler sökordssidor, press och outreach

- `/matsvinn-statistik/` – officiella siffror från Naturvårdsverket (livsmedelsavfall 2024: 880 000 ton, 84 kg/person, hushåll 72 %, matsvinn 16 kg/person, 190 000 ton i avloppet) och Livsmedelsverket (1 330 kr/person, 5 000–6 000 kr/familj, 14 miljarder kr) med länk till varje källa, tidsserie 2016–2024 och citeringsanvisning. Byggd för att bli länkad av media, kommuner och bloggar.
- `/middagstips-vardag/` (25 rätter sorterade på tid) och `/middagstips-helg/` (fredag, lördag, söndag) – egna sidor för "middagstips vardag" och "middagstips helg", 5 400 sökningar var med KD 18–22. Tidigare bara sektioner.
- `/en/best-recipe-app/` – "best recipe app" (1 900, KD 18) med jämförelse mot Paprika, Samsung Food, Yummly, SideChef och SuperCook.
- `/press/` och `/en/press/` – boilerplate, fakta, bilder, presskontakt. Länkade från alla sidfötter.
- `outreach/lankprospekt-och-pitchar.md` – prioriterad prospektlista (bloggar som länkar till svenska matappar, roundup-skribenter, kommunala avfallsbolag, föräldramedier, lokalmedia i Tyresö, ekonomipoddar), vilka sidor som pitchas till vem, och fyra färdiga mejlmallar.

Semrush-enheterna var fortfarande slut, så volymerna för "matsvinn statistik" och "hur mycket mat slängs i sverige" kunde inte hämtas. Sidan är motiverad av länkvärde oavsett volym.

## 9. Nästa steg som inte går att lösa i koden

0. Semrush-kontot behöver fler API-enheter innan nästa datakörning (organisk nyckelordslista per konkurrent och frågerapporter för veckomeny/matsvinn stoppades av tom balans).

1. Verifiera domänen i Google Search Console och Bing Webmaster Tools, skicka in `sitemap.xml`.
2. Skaffa riktiga betyg i App Store och Google Play. När det finns ett rimligt antal: lägg in `aggregateRating` i `SoftwareApplication`-noden och visa betygen på startsidan (mönstret från ExpressVPN/Varo). Lägg inte in påhittade siffror.
3. Länkar: pitcha "recept utifrån det du har hemma" till matbloggar, Livsmedelsverkets matsvinnsinitiativ, kommunala avfallsbolag och föräldraforum. Konkurrenterna på "middagstips" har hög auktoritet, så nya sidor kommer först att synas på long-tail.
4. Publicera 1–2 nya guider per månad från listan ovan: "best recipe app" (EN, KD 18), "middagstips helg" och "middagstips vardag" som egna sidor om `/middagstips/` inte tar dem, "enkel lyxig middag" (2 900), "nyttig veckomeny barnfamilj" (320).
5. Riktiga skärmdumpar från appen i heron och i OG-bilden ger bättre CTR än mockupen.
6. Mät: koppla Search Console och app-store-analys till landningssidorna så att ni ser vilka guider som driver installationer.
