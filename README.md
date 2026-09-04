# cibello.app

Statisk marknadssajt för Cibello (LandveX AB). Ren HTML/CSS/JS utan byggsteg – ladda upp repo-roten som den är till valfri statisk host (Netlify, Cloudflare Pages, Vercel, S3 m.fl.).

## Struktur
- `index.html` – svensk startsida (`home.css`, `main.js`). Källa för alla språkversioner.
- `/en/`, `/de/`, … `index.html` – **genererade** landningssidor. Ändra aldrig dem direkt: ändra `index.html` (markup), `tools/i18n.json` (översättningar per `data-i18n`-nyckel), `tools/sitedata.py` (guider, etiketter) eller `tools/hubtext/<lang>.html` (språkspecifik text) och kör `python3 tools/build_home.py`. Ingen text byts i webbläsaren; språkväljaren navigerar till rätt sida och besökare med annat webbläsarspråk får en banner.
- `/om/`, `/en/about/` – om företaget (E-E-A-T, kontakt). `/press/`, `/en/press/` – pressmaterial.
- `/basta-matapp/`, `/en/best-meal-planning-app/`, `/en/best-recipe-app/` – jämförelsesidor. `/vad-ska-jag-ata-till-middag/` har Middagsväljaren (`middag.js`).
- `/matsvinn-statistik/` – officiella siffror med källor; uppdatera när Naturvårdsverket publicerar ny statistik (december varje år).
- `outreach/` – länkprospekt och pitchmallar (publiceras inte, ligger utanför sitemap).
- Alla sidor har ett litet inline-skript som sätter `html.js`; reveal-animationer körs bara då, så innehållet syns utan JavaScript. Skriptets CSP-hash finns i `_headers`/`vercel.json` – ändra inte skriptet utan att uppdatera hashen.
- `/middagstips/`, `/veckomeny/`, … – svenska guider (`seo.css`).
- `/en/`, `/de/`, … – språkhubbar med guider per språk.
- `integritet.html`, `villkor.html`, `delete-account.html` – juridik (`legal.css`). `/en/privacy/`, `/en/terms/` – engelska översättningar; alla icke-svenska sidor länkar dit. Svensk version gäller vid avvikelse.
- `tools/build_home.py` – renderar startsidan till elva språkversioner (`/en/`, `/de/` …) från `tools/i18n.json`, `tools/sitedata.py` och `tools/hubtext/`. Kör efter varje ändring av `index.html`. `tools/llms.py` – regenererar `llms.txt`.
- `tokens.css` – enda källan för färg, typografi och form.
- `img/` – OG-bilder och ikoner. `manifest.webmanifest`, `favicon.svg`, `robots.txt`, `llms.txt`, `sitemap.xml`.
- `_headers` (Netlify/Cloudflare) och `vercel.json` (Vercel) – säkerhets- och cache-headers. Använd den som passar hosten.
- `tools/sitemap.py` – regenererar `sitemap.xml` från HTML-filerna (hreflang läses från sidorna, lastmod från git).
- `tools/check.py` – validerar länkar, canonical, hreflang-reciprocitet, JSON-LD, titlar, beskrivningar och sitemap-täckning.

- `img/og/` – en OG-bild per svensk och engelsk guide. Regenerera vid nya sidor eller ändrade rubriker (mallen ligger i `og.html` i genereringsskriptet; kräver Playwright).
- `.github/workflows/site-checks.yml` – kör `tools/check.py`, html-validate och JS-syntaxkontroll vid varje push.
- `docs/LANSERING.md` – lanseringschecklista. `docs/FAKTAKONTROLL.md` – register över produktpåståenden och deras källor.

## Arbetsflöde
1. Redigera HTML direkt. Ny guide: kopiera en befintlig sida i samma språk, byt canonical/hreflang/title/description/innehåll och lägg till sidan i sidfotens och asidens länklistor.
2. Kör `python3 tools/sitemap.py && python3 tools/check.py` innan push. Checken ska ge 0 errors.
3. Se `SEO-RAPPORT.md` för nyckelordsdata, prioriteringar och nästa steg.

Lokal förhandsvisning: `npx http-server -p 8080 .`
