# Brief till skribenter och översättare: guiderna på de tio övriga språken

Gäller de tre guiderna per språk under `/de/`, `/fr/`, `/es/`, `/it/`, `/nl/`, `/pl/`, `/da/`, `/nb/`, `/fi/` och `/pt/`, samt landningssidornas egen textsektion (`tools/hubtext/<språk>.html`). Landningssidorna i sig är färdiga och behöver inte skrivas om.

## Läget

| Språk | Guider | Ord per guide i dag | Landningssidans egen text |
|---|---|---|---|
| de, fr, es, it, nl, pl, da, nb, fi, pt | 3 var | 210–310 | 150–190 ord, delvis kortade sammanfattningar |

Målet är 600–900 ord per guide, skrivna på målspråket av någon som har det som modersmål, inte översatta ord för ord från svenska eller engelska. Använd de svenska guiderna som förlaga för struktur och djup: `/vardagsmat/`, `/snabb-middag/`, `/matlador/` och `/bast-fore-datum/` är de bästa exemplen.

## De tre guiderna per språk

1. **Måltidsplanering / veckomeny** (`…/essensplaner/`, `…/planificateur-repas/` osv.). Motsvarar `/veckomeny/`.
2. **Recept med det du har hemma** (`…/rezepte-mit-zutaten/` osv.). Motsvarar `/middagstips/` och `/en/recipes-with-ingredients/`.
3. **Minska matsvinn** (`…/lebensmittelverschwendung-reduzieren/` osv.). Motsvarar `/matsvinn/`.

## Struktur som ska behållas

Filen är färdigt uppmärkt. Skriv om innehållet inne i `<article class="article">`: rubriker (`<h2>`), stycken, gärna en punktlista eller tabell, avslutande FAQ med tre till fem frågor i `<details>`. Ändra inte sidhuvud, sidfot, `<aside>`, CTA-blocket eller `<head>`, förutom `<title>` och `<meta name="description">` som ska matcha den nya texten. FAQ-frågorna och svaren upprepas i JSON-LD-blocket i `<head>`; uppdatera båda ställena.

## Sökord

Semrush-data finns bara för Sverige och USA. För övriga språk: utgå från hur människor i landet faktiskt formulerar "vad ska vi äta ikväll", "veckomeny", "recept med det jag har hemma" och "minska matsvinn", och lägg in de formuleringarna naturligt i rubrik, första stycket och FAQ. Kontrollera gärna Google Trends eller Semrush för landet innan texten skrivs. Titeln ska vara under 60 tecken och sluta med " | Cibello".

## Fakta om appen som får användas

Endast dessa, hämtade ur `docs/FAKTAKONTROLL.md`:

- Fota kyl, frys och skafferi; appen känner igen varor och var de står. Kvitton och streckkoder kan skannas. Resultatet granskas av användaren innan det sparas eftersom AI kan tolka fel.
- Fler än 9 000 recept, rankade efter hur stor andel av ingredienserna som finns hemma. Förslag väger in vad som snart går ut och vad hushållet brukar gilla, med en förklaring.
- Veckomeny som varierar rätter och råvaror och som användaren granskar och ändrar.
- Inköpslista med det som saknas, delad i hushållet (under provperioden och därefter med betalplan).
- Matlådor kan finnas med i matlagret. Mjuka påminnelser innan maten blir dålig.
- 12 språk. Data lagras inom EU. Kontot raderas i appen.
- 14 dagars provperiod utan kort. Åldersgräns 18 år.
- Recept- och allergenfilter är vägledning, inte garanti. Näringsvärden är uppskattningar. Ingen medicinsk rådgivning.

Påstå inte: ingrediensbyten, tidsfilter, automatisk restplanering, receptimport, annonser, priser, lanseringsdatum, betyg eller antal användare.

## Ton

Konkret, varm, utan pekpinnar. Skriv för en vuxen som är trött klockan 17 och vill ha ett svar, inte en föreläsning. Använd "du". Undvik utropstecken och superlativ. Var ärlig om att appen är ett stöd och att människan bestämmer.

## Leverans och kontroll

Lämna filerna som HTML på samma sökväg. Innan merge kör den som tar emot texten:

```
python3 tools/check.py
npx html-validate --config tools/.htmlvalidate.json "**/*.html"
```

Om beslutet i stället blir att vänta: sätt `<meta name="robots" content="noindex,follow">` på de 30 guiderna (inte landningssidorna) tills texterna finns, så drar de inte ner helhetsintrycket. `tools/check.py` och `tools/sitemap.py` hanterar noindex automatiskt.
