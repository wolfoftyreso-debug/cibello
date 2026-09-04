"""Schema for tools/content/<lang>.py. Copy this file, fill every field in the target language.

All strings are HTML fragments where noted (may contain <a>, <ul>, <ol>, <strong>, <table>).
Keep the guide paths exactly as listed for the language (they already exist and carry hreflang).
"""

LANG = "xx"

# The three existing guides for this language, keyed by their path. Order: planner, recipes, waste.
GUIDES = {
    "/xx/planner-slug/": dict(
        title="… | Cibello",             # under 60 characters, ends with " | Cibello"
        desc="…",                        # 120–155 characters
        eyebrow="…",                     # 3–6 words
        h1="…",
        lead="…",                        # 2–3 sentences
        sections=[                       # 5–7 sections, 600–900 words in total, HTML fragments
            ("Heading", "<p>…</p><ul><li>…</li></ul>"),
        ],
        faq=[("Question?", "Answer in one to three sentences, plain text.")],   # 4 items
    ),
    "/xx/recipes-slug/": dict(),
    "/xx/waste-slug/": dict(),
}

# Landing-page prose: 3–4 <section><h2>…</h2><p>…</p></section>, 220–320 words, links to the three guides.
HUBTEXT = """<section><h2>…</h2><p>…</p></section>"""

ABOUT = dict(title="…", desc="…", h1="…", lead="…", sections=[("…", "<p>…</p>")])   # 5 sections, like /en/about/
PRESS = dict(title="…", desc="…", h1="…", lead="…", sections=[("…", "<p>…</p>")])   # like /en/press/ incl. facts list and images
NEWS = dict(title="…", desc="…", h1="…", lead="…", rss_label="RSS",
            entries=[("2026-09-04", "Title", "/link/", "Two sentences.")])            # 4 entries, like /en/news/

# Legal: faithful translations of integritet.html, villkor.html and delete-account.html (v2.0).
PRIVACY = dict(title="…", desc="…", h1="…", notice="<strong>In short:</strong> …", body="<h2>1. …</h2><p>…</p>…")
TERMS = dict(title="…", desc="…", h1="…", body="<h2>1. …</h2><p>…</p>…")
DELETE = dict(title="…", desc="…", h1="…", body="<h2>…</h2><ol><li>…</li></ol><p>…</p>…")

UI = dict(
    faq_title="…",                       # "Frequently asked questions"
    privacy_nav="…", terms_nav="…", delete_nav="…",
    legal_meta="Cibello · version 2.0 · … 30 … 2026 · …",   # effective date + "translation" in the language
    translation_label="…",               # "About this translation:"
    translation_note="… (<a href=\"{sv}\" lang=\"sv\">…</a>). …",  # says: translation of the Swedish original; Swedish version applies if they differ. Keep {sv} placeholder.
)
