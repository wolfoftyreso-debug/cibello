# Faktakontroll av produktpåståenden på cibello.app

Datum: 2026-09-04. Alla sidor som skrivits under SEO-arbetet har granskats mot tre källor: den ursprungliga startsidan (texter i `index.html`/`main.js`), `integritet.html` och `villkor.html`. Ingen ny funktion har lagts till som inte finns i källorna. Där belägg saknades har texten ändrats.

Status: **Belagt** = står i källan. **Rimligt** = följer av källan men ordalydelsen är vår. **Ändrat** = saknade belägg och har skrivits om.

## Belagt

| Påstående | Källa |
|---|---|
| Fota kyl och skafferi, appen känner igen varor och var de står | Startsidan: "Fota kylen & skafferiet … AI:n ser vad du har och var det står", "räkosten står i kyldörren" |
| Skanna kvitton och streckkoder | Ursprunglig middagstips-FAQ: "skanna bland annat kyl, skafferi, kvitton och streckkoder"; integritetspolicy: "bilder … för att identifiera matvaror eller kvitton" |
| 9 000+ recept, matchade mot matlagret, andel hemma visas | Startsidan: "9 000+ recept", mockup "82 % hemma", "Toppval" |
| Förslag väger in vad som snart går ut, smak och hushållets behov, med förklaring | Startsidan: steg 2 och "Personliga förslag … Förklarar alltid varför" |
| Veckomeny som varierar rätter och råvaror, granskas av användaren | Ursprunglig veckomeny-sida |
| Inköpslista på det som faktiskt saknas | Startsidan: "Inköpslista på det som faktiskt saknas" |
| Matlådor du håller koll på | Startsidan: "matlådor du håller koll på" |
| Mjuka påminnelser innan maten blir dålig, aldrig skam | Startsidan: steg 3, "Mindre svinn" |
| Hushållet delar överblick under provperiod eller med betalplan | Startsidan: "Hela hushållet" |
| Data lagras inom EU, konto kan raderas i appen | Startsidan: "Dina data i EU"; integritetspolicy §7; delete-account.html |
| 12 språk | Startsidan |
| Gemini analyserar bilder; Cibello AI tränas bara på rättelser och, efter separat val, sanerade bilder; av från början | Startsidan: "Du bestämmer över AI-träningen"; integritetspolicy §3–4; villkor §4–5 |
| AI kan tolka fel, användaren granskar; allergenfilter är vägledning; näringsvärden är uppskattningar | Startsidan: "Bra att veta"; villkor §2–3 |
| Provperiod 14 dagar utan kort, en gång per e-postidentitet | Villkor §7 |
| Åldersgräns 18 år | Villkor §1, integritetspolicy §8 |
| Säljer inte personuppgifter | Integritetspolicy §6 |
| Abonnemang via App Store / Google Play; pris visas i butiken | Villkor §7 |
| LandveX AB, org.nr 559141-7042, Antennvägen 2, Tyresö; hello@, privacy@, support@ | Sidfot, integritetspolicy §1, villkor §11 |

## Rimligt (följer av källan, ordalydelsen är vår)

| Påstående | Motivering |
|---|---|
| Matlager "med plats och datum" (press, om) | Plats: "var det står". Datum: påminnelser före bäst före förutsätter datum; policyn ber användaren kontrollera "datum och mängder" |
| Mängder finns på varor (en/pantry-app) | Integritetspolicy §3: "kontrollera innehåll, allergener, datum och mängder" |
| Fota kvittot efter inköp så uppdateras lagret | Kvitton skannas enligt FAQ och policy |
| Lägga till varor manuellt i inköpslistan | Standardfunktion i alla inköpslistor; bör bekräftas |
| Appen lär sig vad hushållet brukar välja | "Lär känna dig med tiden" |
| Rester som matlådor finns med i matlagret och kan vägas in i planeringen | Följer av "matlådor du håller koll på" + förslag utifrån matlagret |
| Näringsvärden visas som riktvärden | "Näring är en uppskattning" |

## Ändrat (saknade belägg)

| Tidigare påstående | Var | Nu |
|---|---|---|
| Appen föreslår ersättningsingredienser | snabb-middag, en/what-to-eat-tonight | Appen visar vilka ingredienser som saknas |
| Filtrera förslag på tid | vardagsmat, snabb-middag, en/what-to-eat-tonight | Förslagen utgår från matlager, datum, allergier och matvanor |
| Byt ut saknade ingredienser direkt i receptet | snabb-middag | Borttaget |
| Veckomenyn planerar automatiskt in rester som lunch dagen efter | matlador | Rester läggs in som matlådor och finns med i matlagret |
| Matlådor har "datum och plats" | matlador, middagstips-helg | Matlådor kan finnas med i matlagret |
| Barn fotar kylen med appen | middagstips-barnfamilj | Barn väljer mellan rätter; appen är för vuxna (18 år) |
| "Inga annonser i appen" | om, en/about | Borttaget (står inte i policyn) |
| "Lansering: 2026" | press, en/press | "Tillgänglig för iOS och Android" |
| "Not yet" om receptimport | en/best-recipe-app, en/best-meal-planning-app | "Inte fokus" |

## Att bekräfta av LandveX

Dessa formuleringar är rimliga men bör bekräftas av någon som känner appen:

1. Att matlådor läggs in i matlagret på samma sätt som andra varor och omfattas av påminnelser.
2. Att inköpslistan fylls på automatiskt från planerade recept (startsidan säger "på det som faktiskt saknas", men inte uttryckligen "från veckomenyn").
3. Att förslagen kan väga in tillgänglig tid (mockupen visar "in 25 min"; texterna säger det inte längre).
4. Att egna varor kan läggas till manuellt i inköpslistan.
5. Jämförelsetabellernas rader om konkurrenter bygger på deras butiksbeskrivningar i september 2026 och bör ses över var sjätte månad.

Om något av detta inte stämmer: sök efter formuleringen i repot (`grep -rn "…" --include=*.html .`) och ändra på alla ställen, inklusive JSON-LD-blocket i sidhuvudet där FAQ-svaren upprepas.
