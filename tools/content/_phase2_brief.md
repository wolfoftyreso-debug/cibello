# Phase 2 brief: page parity for every language

You write ONE Python file `tools/content/<lang>_extra_a.py` or `<lang>_extra_b.py` following `tools/content/_schema_extra.py` exactly. Read that schema first, then `docs/OVERSATTNINGSBRIEF.md` (tone, rules) and `docs/FAKTAKONTROLL.md` (the only product facts allowed).

## Sources per family (read the <article> of each; adapt structure and depth, write natively, never word for word)

| Family | Swedish source | English source |
|---|---|---|
| everyday-food | vardagsmat/index.html | – |
| quick-dinner | snabb-middag/index.html | – |
| family-dinner | middagstips-barnfamilj/index.html | – |
| meal-boxes | matlador/index.html | – |
| shopping-list | inkopslista/index.html | – |
| best-before | bast-fore-datum/index.html | – |
| weekday-dinners | middagstips-vardag/index.html | – |
| weekend-dinners | middagstips-helg/index.html | – |
| what-to-eat-tonight | vad-ska-jag-ata-till-middag/index.html | en/what-to-eat-tonight/index.html |
| budget-food | billig-mat/index.html | – |
| eu-food-waste-stats | (facts only) tools/content/_facts_eu_food_waste.md; format like matsvinn-statistik/index.html | – |
| ai-meal-planner | – | en/ai-meal-planner/index.html |
| pantry-app | – | en/pantry-app/index.html |
| app-comparison | – | en/best-meal-planning-app/index.html |
| recipe-app-comparison | – | en/best-recipe-app/index.html |

## Rules

- 600–900 words per page in `sections` (comparisons and the statistics page may follow the source length). 5–7 sections. 4 FAQ items with plain-text answers.
- `title` under 60 characters ending " | Cibello"; `desc` 120–155 characters; `label` 1–4 words for menus.
- Slug: short, natural, keyword-bearing, lowercase ASCII, under the language prefix, unique. Swedish files use no prefix (e.g. "/ai-matplanerare/").
- Tables: copy the markup pattern of the source: `<div class="table-wrap"><table class="cmp"><caption>…</caption><thead><tr><th scope="col">…</th></tr></thead><tbody><tr><th scope="row">…</th><td>…</td></tr></tbody></table></div>`. Yes/No/Partly cells use `<span class="y">…</span>`, `<span class="n">…</span>`, `<span class="p">…</span>` with the words in your language. Keep the "based on the apps' own store listings, September 2026, verify yourself" caption.
- best-before: date marking ("best before" vs "use by") is EU-wide law; describe it for your country's wording. Replace the Swedish agency with "the national food safety authority" or your country's actual authority name if you are certain of it. Keep the shelf-life table as guidance.
- budget-food: no currency amounts, no store names. eu-food-waste-stats: only the Eurostat figures in the facts file, with the Eurostat link; say national statistics offices publish country data; sv is excluded from this family.
- Internal links allowed: your language's landing page (/xx/), its three existing guides (see `tools/sitedata.py` GUIDES), the phase-1 pages /xx/about/, /xx/press/, /xx/news/, /xx/privacy/, /xx/terms/, /xx/delete-account/, and the slugs you yourself define in this file. Do not link to slugs the other file of your language defines unless you know them (you do not), and never to other languages' pages except /en/best-meal-planning-app/ and /en/best-recipe-app/.
- Product facts: only from FAKTAKONTROLL. Never: ingredient substitutions, time filters, automatic leftover planning, recipe import, ads, prices, launch dates, ratings, user numbers. Adults 18+. 14-day trial without a card. AI can misread; user reviews scans. Filters are guidance; nutrition values are estimates.
- Style: warm, concrete, no exclamation marks, no superlatives, no em-dashes. Escape & as &amp; in HTML. Python triple-quoted strings.

## TOOL (file A only, family what-to-eat-tonight)

Fill every key in the schema. `dishes`: exactly 40 everyday dishes natural to the language's food culture, each `(name, protein_key, minutes, [mode_tags])` with protein_key in any/chicken/meat/fish/veg, minutes in 15–60, 1–3 tags from quick/leftovers/pantry/budget/kids/mealbox/friday. Mix proteins and times so every filter combination finds something.

## Verify before finishing

```
cd /home/user/cibello && python3 -c "import sys; sys.path.insert(0,'tools'); import content.<FILE> as c; print(c.LANG, list(c.GUIDES2)); [print(k, v['slug'], len(''.join(b for _,b in v['sections']).split())) for k,v in c.GUIDES2.items()]; t=getattr(c,'TOOL',None); print('tool dishes', len(t['dishes']) if t else 'n/a')"
```
Report slugs and word counts. Do not modify any other file.
