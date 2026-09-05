"""Schema for tools/content/<lang>_extra_a.py and <lang>_extra_b.py (phase 2: full page parity).

Each file defines LANG and GUIDES2: a dict keyed by FAMILY (fixed keys below) whose values describe one page.
File A carries the first eight families and TOOL; file B the rest. Keys not written are simply skipped.

Families and their Swedish/English source pages (read them for structure, depth and the allowed facts):
  everyday-food        sv /vardagsmat/                 (everyday cooking that works all week)
  quick-dinner         sv /snabb-middag/               (dinner in 20–30 minutes from what you have; table of dishes)
  family-dinner        sv /middagstips-barnfamilj/     (family dinners kids accept; adults 18+ use the app)
  meal-boxes           sv /matlador/                   (meal-prep boxes, fridge/freezer, safety)
  shopping-list        sv /inkopslista/                (shared household shopping list filled from recipes)
  best-before          sv /bast-fore-datum/            (best-before vs use-by; EU date marking; table of shelf lives)
  weekday-dinners      sv /middagstips-vardag/         (25 weekday dishes sorted by time)
  weekend-dinners      sv /middagstips-helg/           (Friday, Saturday, Sunday)
  what-to-eat-tonight  sv /vad-ska-jag-ata-till-middag/ and en /en/what-to-eat-tonight/  (question page WITH the dinner picker tool; needs TOOL)
  budget-food          sv /billig-mat/                 (budget cooking for a week; example weekly menu table; no currency amounts)
  eu-food-waste-stats  (new for all) facts in _facts_eu_food_waste.md; sv has its own Swedish page and is excluded
  ai-meal-planner      en /en/ai-meal-planner/
  pantry-app           en /en/pantry-app/
  app-comparison       en /en/best-meal-planning-app/  (international comparison; sv has its own Swedish one)
  recipe-app-comparison en /en/best-recipe-app/

Slugs: choose a short, natural, keyword-bearing slug in the target language, lowercase ASCII only
(ä→a, ö→o, ü→u, é→e, ß→ss …), under the language prefix, e.g. "/de/schnelles-abendessen/". Never reuse an existing path.
"""

LANG = "xx"

GUIDES2 = {
    "everyday-food": dict(
        slug="/xx/slug/",
        label="Short nav label",             # 1–4 words, used in menus, footers and asides
        title="… | Cibello",                 # under 60 characters
        desc="…",                            # 120–155 characters
        eyebrow="…",
        h1="…",
        lead="…",
        sections=[("Heading", "<p>…</p>")], # 5–7 sections, 600–900 words in total; tables welcome where the source has one
        faq=[("Question?", "Plain-text answer.")],   # 4 items
    ),
}

# Only in file A, for the what-to-eat-tonight family. The generator renders the form and feeds middag.js.
TOOL = dict(
    heading="…",                             # h2 above the tool
    protein_label="…", time_label="…", mode_label="…",
    protein={"any": "…", "chicken": "…", "meat": "…", "fish": "…", "veg": "…"},
    time={"20": "…", "30": "…", "45": "…", "90": "…"},          # "Max 20 min" … "Doesn't matter"
    mode={"all": "…", "quick": "…", "leftovers": "…", "pantry": "…", "budget": "…", "kids": "…", "mealbox": "…", "friday": "…"},
    button="…",                              # "Pick a dinner"
    no_match="…",                            # "Nothing matched. Try loosening a filter."
    minutes="…",                             # word for "min"
    any_protein="…",                         # "any protein"
    tip="…",                                 # one sentence: in the app, suggestions start from what is in your fridge
    note="…",                                # one sentence under the tool: picks from forty everyday dishes, no account needed
    dishes=[                                 # exactly 40, everyday dishes natural to the language's food culture
        ("Dish name", "veg", 20, ["pantry", "budget", "kids"]),   # protein key, minutes, mode tags (1–3)
    ],
)
