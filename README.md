# cibello.app

Statisk marknadssajt för Cibello (LandveX AB). Ren HTML/CSS/JS utan byggsteg – ladda upp repo-roten som den är till valfri statisk host (Netlify, Cloudflare Pages, Vercel, S3 m.fl.).

## Struktur
- `index.html` – svensk startsida (`home.css`, `main.js`). Texten byts på klientsidan per språk, men sidan serveras alltid på svenska (SEO-säkert). Andra språk erbjuds via banner/väljare.
- `/middagstips/`, `/veckomeny/`, … – svenska guider (`seo.css`).
- `/en/`, `/de/`, … – språkhubbar med guider per språk.
- `integritet.html`, `villkor.html`, `delete-account.html` – juridik (`legal.css`).
- `tokens.css` – enda källan för färg, typografi och form.
- `img/` – OG-bilder och ikoner. `manifest.webmanifest`, `favicon.svg`, `robots.txt`, `llms.txt`, `sitemap.xml`.
- `_headers` (Netlify/Cloudflare) och `vercel.json` (Vercel) – säkerhets- och cache-headers. Använd den som passar hosten.
- `tools/sitemap.py` – regenererar `sitemap.xml` från HTML-filerna (hreflang läses från sidorna, lastmod från git).
- `tools/check.py` – validerar länkar, canonical, hreflang-reciprocitet, JSON-LD, titlar, beskrivningar och sitemap-täckning.

## Arbetsflöde
1. Redigera HTML direkt. Ny guide: kopiera en befintlig sida i samma språk, byt canonical/hreflang/title/description/innehåll och lägg till sidan i sidfotens och asidens länklistor.
2. Kör `python3 tools/sitemap.py && python3 tools/check.py` innan push. Checken ska ge 0 errors.
3. Se `SEO-RAPPORT.md` för nyckelordsdata, prioriteringar och nästa steg.

Lokal förhandsvisning: `npx http-server -p 8080 .`
