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

## 6. Nästa steg som inte går att lösa i koden

1. Verifiera domänen i Google Search Console och Bing Webmaster Tools, skicka in `sitemap.xml`.
2. Skaffa riktiga betyg i App Store och Google Play. När det finns ett rimligt antal: lägg in `aggregateRating` i `SoftwareApplication`-noden och visa betygen på startsidan (mönstret från ExpressVPN/Varo). Lägg inte in påhittade siffror.
3. Länkar: pitcha "recept utifrån det du har hemma" till matbloggar, Livsmedelsverkets matsvinnsinitiativ, kommunala avfallsbolag och föräldraforum. Konkurrenterna på "middagstips" har hög auktoritet, så nya sidor kommer först att synas på long-tail.
4. Publicera 1–2 nya guider per månad från listan ovan: "best recipe app" (EN, KD 18), "middagstips helg" och "middagstips vardag" som egna sidor om `/middagstips/` inte tar dem, "enkel lyxig middag" (2 900), "nyttig veckomeny barnfamilj" (320).
5. Riktiga skärmdumpar från appen i heron och i OG-bilden ger bättre CTR än mockupen.
6. Mät: koppla Search Console och app-store-analys till landningssidorna så att ni ser vilka guider som driver installationer.
