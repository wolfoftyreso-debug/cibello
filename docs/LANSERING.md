# Lanseringschecklista för cibello.app

Ordningen spelar roll. Punkt 1–4 samma dag, resten inom veckan.

## 1. Innan merge
- [ ] Läs `docs/FAKTAKONTROLL.md`, avsnittet "Att bekräfta av LandveX", och rätta det som inte stämmer.
- [ ] Låt någon med juridiskt ansvar läsa `/en/privacy/` och `/en/terms/`. De är översättningar av de svenska v2.0-texterna och anger att den svenska versionen gäller vid avvikelse. Om de svenska texterna ändras måste de engelska uppdateras samtidigt.
- [ ] Kör `python3 tools/check.py` lokalt. Ska ge 0 errors. CI (`.github/workflows/site-checks.yml`) gör samma sak vid push.
- [ ] Välj host-konfiguration: behåll `_headers` + `_redirects` (Netlify, Cloudflare Pages) **eller** `vercel.json` (Vercel). Ta bort den andra så ingen undrar.
- [ ] Bestäm om `outreach/` och `docs/` ska ligga i det publika repot. De publiceras inte som sidor men syns om repot är publikt.

## 2. Deploy
- [ ] Merge `claude/sharp-mccarthy-9zypyb` till main och deploya.
- [ ] Kontrollera i webbläsaren: `https://cibello.app/` (svenska, ingen automatisk språkväxling), `/en/`, `/middagstips/`, `/vad-ska-jag-ata-till-middag/` (middagsväljaren), `/404-test` (404-sidan), `/sitemap.xml`, `/robots.txt`, `/manifest.webmanifest`, `/.well-known/security.txt`.
- [ ] Kontrollera headers med `curl -sI https://cibello.app/ | grep -iE "content-security|strict-transport|x-frame"`.
- [ ] Testa att `www.cibello.app` och `http://` omdirigerar till `https://cibello.app` (görs i hostens DNS/inställningar, inte i repot).
- [ ] Dela startsidan i Slack/LinkedIn/Facebook-förhandsvisning och kontrollera att OG-bilden syns. Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/

## 3. Sökmotorer
- [ ] Google Search Console: verifiera domänen (DNS TXT), skicka in `https://cibello.app/sitemap.xml`. Begär indexering av startsidan och de fem viktigaste guiderna manuellt.
- [ ] Bing Webmaster Tools: importera från Search Console, skicka in sitemap.
- [ ] Kontrollera "Sidor" i Search Console efter 7 dagar: alla 74 URL:er ska vara indexerade eller på väg. Titta efter "Duplicerad, Google valde annan kanonisk" på språkhubbarna.
- [ ] Rich results-test på en guide och startsidan: https://search.google.com/test/rich-results (FAQ, Breadcrumb, SoftwareApplication).

## 4. Mätning
- [ ] Analys: välj ett integritetsvänligt alternativ som inte kräver cookie-banner (Plausible, Fathom, Umami) eller GA4 med samtycke. Lägg till skriptet i alla sidor och lägg till dess domän i `Content-Security-Policy` (`script-src` och `connect-src`) i `_headers`/`vercel.json`.
- [ ] Google Play: kampanjparametern `utm_campaign=<sida>` finns redan på alla Play-länkar. Se rapporten "Butiksresultat → Förvärv" i Play Console.
- [ ] App Store: skapa ett provider token i App Store Connect (App Analytics → Kampanjer) och lägg till `?pt=<token>&ct=<sida>&mt=8` på App Store-länkarna. Utan pt spåras inget.

## 5. Länkar och press
- [ ] Skicka mejlen i `outreach/lankprospekt-och-pitchar.md`, grupp A först. Max fem per dag, personliga.
- [ ] Lägg upp `/press/` i LinkedIn-profilen och app-butikernas supportlänk.
- [ ] Be de första nöjda användarna om betyg i butikerna. När det finns fler än ~50 betyg: lägg in `aggregateRating` i `SoftwareApplication`-noden (`labels.py` → `app_node`) och visa betygen på startsidan.

## 6. Underhåll
- [ ] `/matsvinn-statistik/`: uppdatera när Naturvårdsverket publicerar ny statistik (december).
- [ ] Jämförelsesidorna: kontrollera konkurrenternas funktioner var sjätte månad.
- [ ] Nya guider: kopiera en befintlig sida, lägg till i `GUIDES` i genereringsskriptet eller manuellt i sidfot/aside, kör `tools/sitemap.py` och `tools/check.py`.
- [ ] Semrush: fyll på API-enheter och kör frågerapporterna för "veckomeny", "matsvinn", "matlådor" samt konkurrenternas nyckelordslistor. Skapa ett Position Tracking-projekt med de 40 sökorden i `SEO-RAPPORT.md`.
