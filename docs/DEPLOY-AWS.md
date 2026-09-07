# Deploy på AWS (S3 + CloudFront)

Sajten är helt statisk. Det som hostar den måste göra fyra saker som `vercel.json` och `_headers` gör på andra plattformar men som **inte** gäller på AWS: servera `index.html` för katalog-URL:er, ge riktig 404-status, sätta säkerhetsheaders och sätta cache-headers. Allt nedan är standard i CloudFront och tar ungefär en timme att sätta upp första gången.

## 1. Vad som ska laddas upp

Repo-roten minus verktyg och dokument. Lista på det som **inte** ska upp: `.git/`, `.github/`, `tools/`, `docs/`, `outreach/`, `*.md`, `_headers`, `_redirects`, `vercel.json`, `.vercelignore`, `.gitignore`.

```bash
BUCKET=cibello-app-site   # byt namn
# 1) allt utom bilder, css och js: kort cache så nya sidor syns direkt
aws s3 sync . s3://$BUCKET --delete \
  --exclude ".git/*" --exclude ".github/*" --exclude "tools/*" --exclude "docs/*" --exclude "outreach/*" \
  --exclude "*.md" --exclude "_headers" --exclude "_redirects" --exclude "vercel.json" --exclude ".vercelignore" --exclude ".gitignore" \
  --exclude "img/*" --exclude "*.css" --exclude "*.js" \
  --cache-control "public, max-age=0, must-revalidate"
# 2) bilder: ett år, immutable (byt filnamn om en bild ändras)
aws s3 sync img s3://$BUCKET/img --delete --cache-control "public, max-age=31536000, immutable"
# 3) css och js: ett dygn med stale-while-revalidate
aws s3 sync . s3://$BUCKET --exclude "*" --include "*.css" --include "*.js" --exclude "tools/*" \
  --cache-control "public, max-age=86400, stale-while-revalidate=604800"
# 4) content-type som S3 inte gissar rätt
aws s3 cp manifest.webmanifest s3://$BUCKET/manifest.webmanifest --content-type "application/manifest+json" --cache-control "public, max-age=86400"
for f in nytt/feed.xml en/news/feed.xml de/news/feed.xml fr/news/feed.xml es/news/feed.xml it/news/feed.xml nl/news/feed.xml pl/news/feed.xml da/news/feed.xml nb/news/feed.xml fi/news/feed.xml pt/news/feed.xml; do
  aws s3 cp $f s3://$BUCKET/$f --content-type "application/rss+xml; charset=utf-8" --cache-control "public, max-age=0, must-revalidate"
done
# 5) töm CloudFront-cachen
aws cloudfront create-invalidation --distribution-id DISTRIBUTION_ID --paths "/*"
```

Kontrollera att HTML-filerna får `Content-Type: text/html; charset=utf-8` (AWS CLI sätter `text/html`; charset finns i `<meta charset>` så det räcker, men `--content-type "text/html; charset=utf-8"` på HTML är ännu bättre om ni kör ett eget skript).

## 2. S3-bucket

- Privat bucket, blockera all public access. CloudFront läser via **Origin Access Control (OAC)**.
- Använd S3 som **REST-origin** (`bucket.s3.eu-north-1.amazonaws.com`), inte "static website hosting". Katalogindex löses i CloudFront-funktionen nedan.
- Region: gärna `eu-north-1` (Stockholm). Det påverkar inte besökare, bara lagring och admin.

## 3. CloudFront-distribution

- **Alternate domain names:** `cibello.app` och `www.cibello.app`. ACM-certifikat i `us-east-1` för båda.
- **Viewer protocol policy:** Redirect HTTP to HTTPS. **HTTP/2 och HTTP/3** på. **Compress objects automatically** på (Brotli och gzip).
- **Default root object:** `index.html`.
- **Price class:** Europe + North America räcker.

### CloudFront Function (viewer request): katalogindex, trailing slash, www

Kopplas som *Viewer request* på default behavior.

```js
function handler(event) {
  var request = event.request;
  var host = request.headers.host && request.headers.host.value;
  var uri = request.uri;
  // www -> apex, behåll sökväg
  if (host === 'www.cibello.app') {
    return { statusCode: 301, statusDescription: 'Moved Permanently',
             headers: { location: { value: 'https://cibello.app' + uri } } };
  }
  // /en/ -> /en/index.html
  if (uri.endsWith('/')) { request.uri = uri + 'index.html'; return request; }
  // /en -> /en/  (filer med ändelse lämnas orörda)
  var last = uri.split('/').pop();
  if (last.indexOf('.') === -1) {
    return { statusCode: 301, statusDescription: 'Moved Permanently',
             headers: { location: { value: uri + '/' } } };
  }
  return request;
}
```

Sajtens canonical-adresser är `/`, `/en/`, `/middagstips/` … (med avslutande snedstreck) samt `/integritet.html`, `/villkor.html`, `/delete-account.html` (med ändelse). Funktionen ovan bevarar exakt det, så inga canonicals pekar på omdirigeringar.

### Custom error responses: riktig 404

Med OAC och utan `s3:ListBucket` svarar S3 **403** för saknade objekt. Mappa båda:

| HTTP error code | Response page path | HTTP response code | TTL |
|---|---|---|---|
| 403 | `/404.html` | 404 | 10 s |
| 404 | `/404.html` | 404 | 10 s |

`404.html` har `noindex` och länkar vidare på alla tolv språk.

### Response headers policy: säkerhetsheaders

Skapa en egen policy och koppla till default behavior. Värdena är identiska med `vercel.json` och `_headers`; CSP-hashen hör till det lilla inline-skriptet i varje sidhuvud (`document.documentElement.classList.add("js")`). Ändra inte skriptet utan att räkna om hashen.

| Header | Värde |
|---|---|
| Content-Security-Policy | `default-src 'self'; script-src 'self' 'sha256-qOhFsq0QMV2REqNwk5hGH5bZE9SkX6gt6yeyKdYPv+U='; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'self'; base-uri 'self'; form-action 'self'; object-src 'none'; upgrade-insecure-requests` |
| Strict-Transport-Security | `max-age=31536000; includeSubDomains; preload` |
| X-Content-Type-Options | `nosniff` |
| X-Frame-Options | `SAMEORIGIN` |
| Referrer-Policy | `strict-origin-when-cross-origin` |
| Permissions-Policy | `camera=(), microphone=(), geolocation=()` |

När analys läggs till (Plausible, Fathom eller liknande) måste dess domän in i `script-src` och `connect-src`, annars blockeras skriptet tyst.

### Cache policy

Använd *CachingOptimized* i CloudFront. Cache-Control mot besökare kommer från S3-objektens metadata (steg 1), så CloudFront respekterar `max-age=0` på HTML och ett år på bilder. Kör alltid en invalidation efter deploy, annars kan gamla HTML-sidor ligga kvar i edge-cachen upp till den tid CachingOptimized tillåter.

## 4. DNS (Route 53 eller där domänen ligger)

- `cibello.app` A/AAAA som **alias** till CloudFront-distributionen.
- `www.cibello.app` A/AAAA alias till samma distribution (funktionen ovan omdirigerar till apex).
- Ta bort eventuella gamla poster som pekar på den tidigare hosten.

## 5. Kontroll efter deploy

```bash
curl -sI https://cibello.app/ | grep -iE "content-security|strict-transport|x-frame|cache-control|content-type"
curl -sI https://cibello.app/en            # 301 -> /en/
curl -sI https://cibello.app/en/           # 200
curl -sI https://cibello.app/integritet.html   # 200, ingen omdirigering
curl -sI https://cibello.app/finns-inte/   # 404 med 404-sidan
curl -sI https://www.cibello.app/middagstips/  # 301 -> https://cibello.app/middagstips/
curl -sI https://cibello.app/manifest.webmanifest | grep -i content-type   # application/manifest+json
curl -s https://cibello.app/sitemap.xml | grep -c "<loc>"   # 302
curl -sI https://cibello.app/tools/check.py    # 404 (interna filer ska inte finnas)
```

Öppna sedan i webbläsaren: `/`, `/en/`, `/de/`, `/vad-ska-jag-ata-till-middag/` (middagsväljaren ska ge förslag), `/nytt/` (RSS-knappen), och dela startsidan i Slack eller LinkedIn så OG-bilden syns.

## 6. Uppdateringar framöver

Varje ändring i repot: kör `python3 tools/sitemap.py && python3 tools/check.py` (0 errors), pusha, kör steg 1 igen. Om det ska automatiseras: en GitHub Action med `aws s3 sync` + invalidation på push till `main`, med AWS-credentials via OIDC. Arbetsflödet i `.github/workflows/site-checks.yml` kan byggas ut med ett deploy-jobb som körs efter kontrollerna.

## 7. Testmiljön på Vercel

Projektet `cibello` på Vercel (https://cibello.vercel.app) skapades bara för testdeploy och byggs fortfarande vid varje push till grenen. Pausa eller ta bort det när AWS är uppe, så det inte finns två kopior av sajten. Det är skyddat med Vercel-inloggning och indexeras inte, så det är ingen brådska.
