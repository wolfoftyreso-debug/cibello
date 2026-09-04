#!/usr/bin/env python3
"""Render the Swedish home page (index.html) into eleven localized landing pages.

Sources: index.html (markup + Swedish copy), tools/i18n.json (translations keyed by
data-i18n), tools/sitedata.py (guide lists, footer labels), tools/hubtext/<lang>.html
(language-specific prose kept from the earlier hub pages).

Output: /<lang>/index.html for every language except sv.
Usage: python3 tools/build_home.py
"""
import re, json, pathlib, sys, html as H
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from sitedata import *

I18N = json.loads((ROOT / "tools" / "i18n.json").read_text(encoding="utf-8"))
SRC = (ROOT / "index.html").read_text(encoding="utf-8")

def guide_meta(path):
    f = ROOT / path.strip("/") / "index.html"
    h = f.read_text(encoding="utf-8")
    h1 = re.sub(r"<[^>]+>", "", re.search(r"<h1>(.*?)</h1>", h, re.S).group(1)).strip()
    d = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
    first = re.match(r"^(.*?[.!?])(\s|$)", d)
    return h1, (first.group(1) if first else d)

def translate(html, lang):
    d = I18N[lang]
    def rep(m):
        key = m.group(3)
        val = d.get(key)
        if val is None:
            return m.group(0)
        return m.group(1) + H.escape(val, quote=False) + m.group(5)
    return re.sub(r'(<(\w+)[^>]*\bdata-i18n="(\w+)"[^>]*>)(.*?)(</\2>)', rep, html, flags=re.S)

def build(lang):
    d = I18N[lang]; t = T[lang]; ui = HOME_UI[lang]; home = home_of(lang)
    hub_old = ROOT / lang / "index.html"
    # title/description: reuse the keyword-targeted ones from the existing hub page
    old = hub_old.read_text(encoding="utf-8") if hub_old.exists() else ""
    title = re.search(r"<title>(.*?)</title>", old, re.S).group(1).strip() if old else f"Cibello – {t['get_app']}"
    desc = re.search(r'<meta name="description" content="([^"]*)"', old).group(1) if old else d["meta"]
    url = f"https://cibello.app{home}"
    h = SRC
    h = h.replace('<html lang="sv">', f'<html lang="{lang}">', 1)
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, count=1)
    h = re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), h)
    h = re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")', lambda m: m.group(1) + title + m.group(2), h)
    h = h.replace('<link rel="canonical" href="https://cibello.app/" />', f'<link rel="canonical" href="{url}" />', 1)
    h = h.replace('<meta property="og:url" content="https://cibello.app/" />', f'<meta property="og:url" content="{url}" />', 1)
    h = h.replace('<meta property="og:locale" content="sv_SE" />', f'<meta property="og:locale" content="{OG_LOCALE[lang]}" />', 1)
    h = h.replace("https://cibello.app/img/og.png", f"https://cibello.app/img/og-{lang}.png")
    h = re.sub(r'<meta property="og:image:alt" content="[^"]*">', f'<meta property="og:image:alt" content="Cibello – {H.escape(d["hero_h1a"])} {H.escape(d["hero_h1b"])}">', h)
    # relative asset paths -> absolute
    for a in ["tokens.css", "home.css", "main.js"]:
        h = h.replace(f'href="{a}"', f'href="/{a}"').replace(f'src="{a}"', f'src="/{a}"')
    # JSON-LD
    faq = [(d[f"faq_q{i}"], d[f"faq_a{i}"]) for i in range(1, 7)]
    ld = {"@context":"https://schema.org","@graph":[
        ORG,
        {"@type":"WebSite","@id":"https://cibello.app/#website","name":"Cibello","url":"https://cibello.app/","inLanguage":list(LANG_NAMES.keys()),"publisher":{"@id":"https://cibello.app/#organization"}},
        app_node(lang),
        {"@type":"WebPage","@id":url+"#webpage","url":url,"name":title,"description":desc,"inLanguage":lang,"isPartOf":{"@id":"https://cibello.app/#website"},"about":{"@id":"https://cibello.app/#app"},"dateModified":TODAY,"primaryImageOfPage":{"@type":"ImageObject","url":f"https://cibello.app/img/og-{lang}.png","width":1200,"height":630}},
        {"@type":"FAQPage","@id":url+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},
    ]}
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False, separators=(",",":")) + '</script>', h, count=1, flags=re.S)
    # body strings
    h = translate(h, lang)
    h = h.replace(f'<a class="skip" href="#main">{SKIP["sv"]}</a>', f'<a class="skip" href="#main">{SKIP[lang]}</a>', 1)
    h = h.replace('aria-label="Meny"', f'aria-label="{ui["menu"]}"').replace('aria-label="Stäng"', f'aria-label="{ui["close"]}"')
    h = h.replace('aria-label="Cibello i siffror"', f'aria-label="{ui["stats"]}"').replace('aria-label="Huvudmeny"', f'aria-label="{t["nav"]}"')
    h = h.replace('aria-label="Cibello på andra språk"', f'aria-label="{t["other_langs"]}"')
    h = h.replace('<a href="#faq">FAQ</a>', f'<a href="#faq">{d.get("faq_kicker","FAQ")}</a>')
    h = re.sub(r'<option value="(\w+)"( selected)?>', lambda m: f'<option value="{m.group(1)}"' + (" selected" if m.group(1) == lang else "") + ">", h)
    # comparison link: English comparison for all non-Swedish languages
    h = h.replace('href="/basta-matapp/" data-href-en="/en/best-meal-planning-app/"', 'href="/en/best-meal-planning-app/"')
    # guides section
    cards = ""
    for pth, lbl in GUIDES[lang]:
        h1, first = guide_meta(pth)
        cards += f'<a class="f" href="{pth}"><h3>{lbl}</h3><p>{first}</p></a>'
    langrow = " · ".join(f'<a href="{home_of(c)}" lang="{c}" hreflang="{c}">{n}</a>' for c, n in LANG_NAMES.items() if c != lang)
    guides = f'''<section id="guider" aria-labelledby="upptack-cibello" class="guides">
  <div class="wrap center"><div class="kicker">{ui["guides_kicker"]}</div><h2 class="sec-h" id="upptack-cibello">{ui["guides_h"]}</h2><p class="sec-p">{ui["guides_p"]}</p></div>
  <div class="wrap feat guide-grid">{cards}</div>
  <nav class="wrap langrow" aria-label="{t["other_langs"]}">
    <strong>{t["other_langs"]}:</strong> {langrow}
  </nav>
</section>
'''
    h = re.sub(r'<section id="guider".*?</section>\n', guides, h, count=1, flags=re.S)
    # language-specific prose from the old hub, kept as its own section before the guides
    hub = ROOT / "tools" / "hubtext" / f"{lang}.html"
    if hub.exists():
        prose = hub.read_text(encoding="utf-8")
        h = h.replace('<section id="guider"', f'<section class="hubtext" aria-label="Cibello"><div class="wrap hubwrap article">{prose}</div></section>\n<section id="guider"', 1)
    # footer columns
    g = "".join(f'<a href="{p}">{l}</a>' for p, l in GUIDES[lang])
    langs = "".join(f'<a href="{home_of(c)}" lang="{c}" hreflang="{c}">{n}</a>' for c, n in LANG_NAMES.items())
    ap = "/om/" if lang == "sv" else "/en/about/"; pp = "/press/" if lang == "sv" else "/en/press/"
    cols = f'''<div class="wrap foot-cols">
    <nav aria-label="{t["guides"]}"><h3>{t["guides"]}</h3>{g}</nav>
    <nav aria-label="{t["langs"]}"><h3>{t["langs"]}</h3>{langs}</nav>
    <nav aria-label="{t["company"]}"><h3>{t["company"]}</h3><a href="{ap}">{ABOUT[lang]}</a><a href="{pp}">{PRESS[lang]}</a><a href="{news_path(lang)}">{NEWS[lang]}</a><a href="{legal_paths(lang)[0]}">{t["privacy"]}</a><a href="{legal_paths(lang)[1]}">{t["terms"]}</a><a href="/delete-account.html">{t["delete"]}</a><a href="mailto:hello@cibello.app">{t["contact"]}</a><a href="https://landvex.com" rel="noopener">LandveX AB</a></nav>
  </div>'''
    h = re.sub(r'<div class="wrap foot-cols">.*?</nav>\n  </div>', cols, h, count=1, flags=re.S)
    h = h.replace('<a href="/om/">Om Cibello</a><a href="/press/">Press</a>', f'<a href="{ap}">{ABOUT[lang]}</a><a href="{pp}">{PRESS[lang]}</a>')
    h = h.replace("utm_campaign%3Dhome", f"utm_campaign%3Dhome-{lang}")
    out = ROOT / lang / "index.html"
    out.write_text(h, encoding="utf-8")
    left = [k for k in re.findall(r'data-i18n="(\w+)"', h) if k not in d]
    print(f"/{lang}/  {len(h)//1024} kB  untranslated keys: {left or 'none'}")

for lang in LANG_NAMES:
    if lang != "sv":
        build(lang)
