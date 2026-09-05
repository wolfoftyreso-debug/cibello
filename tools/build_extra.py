#!/usr/bin/env python3
"""Phase 2: render the extra guide families for every language from tools/content/<lang>_extra_*.py.

Builds a registry of slugs per family across languages (fixed Swedish/English source pages plus
the slugs the content files declare), writes tools/guides_extra.json (picked up by sitedata for
menus, footers, asides and landing pages), renders every page with a full hreflang set, injects the
dinner picker where TOOL is defined, then relinks footers and rebuilds the landing pages.

Usage: python3 tools/build_extra.py
"""
import re, json, glob, pathlib, sys, importlib, html as H, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_lang as B
from sitedata import *

FAMILIES = {
    "everyday-food": {"sv": "/vardagsmat/"},
    "quick-dinner": {"sv": "/snabb-middag/"},
    "family-dinner": {"sv": "/middagstips-barnfamilj/"},
    "meal-boxes": {"sv": "/matlador/"},
    "shopping-list": {"sv": "/inkopslista/"},
    "best-before": {"sv": "/bast-fore-datum/"},
    "weekday-dinners": {"sv": "/middagstips-vardag/"},
    "weekend-dinners": {"sv": "/middagstips-helg/"},
    "what-to-eat-tonight": {"sv": "/vad-ska-jag-ata-till-middag/", "en": "/en/what-to-eat-tonight/"},
    "budget-food": {"sv": "/billig-mat/"},
    "eu-food-waste-stats": {},
    "ai-meal-planner": {"en": "/en/ai-meal-planner/"},
    "pantry-app": {"en": "/en/pantry-app/"},
    "app-comparison": {"sv": "/basta-matapp/", "en": "/en/best-meal-planning-app/"},
    "recipe-app-comparison": {"en": "/en/best-recipe-app/"},
}
FIXED = {fam: dict(v) for fam, v in FAMILIES.items()}

def load_all():
    content = {}   # lang -> {family: page}
    tools = {}     # lang -> TOOL
    for f in sorted(glob.glob(str(ROOT / "tools" / "content" / "*_extra_*.py"))):
        mod = importlib.import_module("content." + pathlib.Path(f).stem)
        lang = mod.LANG
        content.setdefault(lang, {}).update(getattr(mod, "GUIDES2", {}))
        if hasattr(mod, "TOOL"):
            tools[lang] = mod.TOOL
    return content, tools

def registry(content):
    reg = {fam: dict(v) for fam, v in FIXED.items()}
    for lang, fams in content.items():
        for fam, page in fams.items():
            if fam not in reg: raise SystemExit(f"unknown family {fam} in {lang}")
            reg[fam][lang] = page["slug"]
    return reg

def alt_links_for(fam, reg):
    slugs = reg[fam]
    alts = [(l, "https://cibello.app" + slugs[l]) for l in LANG_NAMES if l in slugs]
    xd = slugs.get("en") or slugs.get("sv") or next(slugs[l] for l in LANG_NAMES if l in slugs)
    alts.append(("x-default", "https://cibello.app" + xd))
    return "\n".join(f'<link rel="alternate" hreflang="{l}" href="{u}">' for l, u in alts)

def tool_html(lang, tool):
    def opts(d, keys): return "".join(f'<option value="{k}">{d[k]}</option>' for k in keys if k in d)
    data = {"minutes": tool["minutes"], "any_protein": tool["any_protein"], "no_match": tool["no_match"], "tip": tool["tip"],
            "protein_names": {k: v for k, v in tool["protein"].items() if k != "any"},
            "dishes": [[n, p, m, tags] for n, p, m, tags in tool["dishes"]]}
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f'''<section class="tool" aria-labelledby="valj-h"><h2 id="valj-h">{tool["heading"]}</h2>
<form id="middagsval" class="middagsval">
<div class="fld"><label for="protein">{tool["protein_label"]}</label><select id="protein" name="protein">{opts(tool["protein"], ["any","chicken","meat","fish","veg"])}</select></div>
<div class="fld"><label for="tid">{tool["time_label"]}</label><select id="tid" name="tid">{opts(tool["time"], ["20"])}{opts(tool["time"], ["30"]).replace('<option value="30">', '<option value="30" selected>')}{opts(tool["time"], ["45","90"])}</select></div>
<div class="fld"><label for="tag">{tool["mode_label"]}</label><select id="tag" name="tag">{opts(tool["mode"], ["all","quick","leftovers","pantry","budget","kids","mealbox","friday"])}</select></div>
<button type="submit" id="middag-knapp" class="btn">{tool["button"]}</button>
</form>
<div id="middag-ut" class="middag-ut" tabindex="-1" aria-live="polite" hidden></div>
<p class="tool-note">{tool["note"]}</p>
<script type="application/json" id="middag-data">{js}</script></section>'''

TOOL_CSS = '<style>.middagsval{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;align-items:end;background:rgba(255,255,255,.6);border:1px solid rgba(255,255,255,.8);border-radius:var(--radius);padding:20px}.fld label{display:block;font-size:.85rem;font-weight:700;margin-bottom:4px}.fld select{width:100%;padding:10px 12px;border-radius:10px;border:1px solid var(--line);background:#fff;font:inherit}.middagsval .btn{background:linear-gradient(180deg,#3d9163,var(--green) 55%,#2a7049);color:#fff;border:none;border-radius:11px;padding:12px 18px;font:inherit;font-weight:600;cursor:pointer;box-shadow:0 3px 0 #1e5236}.middag-ut{margin-top:16px;padding:20px 22px;border-radius:var(--radius);background:var(--green-l);border:1px solid #d5e5da}.middag-namn{font-size:1.5rem;font-weight:700;color:var(--green-x);margin:0}.middag-meta{margin:.3em 0 0;color:var(--green-d);font-weight:600}.middag-tips{margin:.8em 0 0;color:var(--muted);font-size:.95rem}.tool-note{font-size:.9rem;color:var(--muted)}</style>'

def render_page(lang, fam, page, reg, tool=None):
    path = page["slug"]; url = f"https://cibello.app{path}"; t = T[lang]
    c = dict(page)
    sections = list(c["sections"])
    extra_head = ""; extra_scripts = ""
    body_prefix = ""
    if fam == "what-to-eat-tonight" and tool:
        body_prefix = tool_html(lang, tool); extra_head = TOOL_CSS; extra_scripts = '<script src="/middag.js" defer></script>'
    graph = [ORG, B.webpage(url, c["h1"], c["desc"], lang), B.crumbs_ld(lang, c["h1"], url)]
    if c.get("faq"): graph.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in c["faq"]]})
    graph.append(app_node(lang))
    ld = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False, separators=(",",":"))
    body = "".join(f"<section><h2>{h2}</h2>{b}</section>" for h2, b in sections)
    faq_title = "Vanliga frågor" if lang == "sv" else ("Frequently asked questions" if lang == "en" else importlib.import_module(f"content.{lang}").UI["faq_title"])
    faq_html = (f'<section class="faq"><h2>{faq_title}</h2>' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in c["faq"]) + "</section>") if c.get("faq") else ""
    wide = fam in ("app-comparison", "recipe-app-comparison")
    html = B.head(lang, url, c["title"], c["desc"], alt_links_for(fam, reg), ld, "article", extra_head)
    html += f'''<body{' class="wide"' if wide else ''}><a class="skip" href="#main">{SKIP[lang]}</a>{header(lang)}
<main id="main"><div class="hero"><div class="wrap">{crumbs(lang, c["h1"])}<div class="eyebrow">{c.get("eyebrow","")}</div><h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p></div></div>
<div class="wrap content"><article class="article">{body_prefix}{body}{faq_html}{cta_block(lang)}<p class="updated"><small>{t["updated"]} {TODAY}</small></p></article>{B.aside(lang, path)}</div></main>
{B.footer(lang)}{extra_scripts}</body></html>
'''
    html = html.replace('href="https://play.google.com/store/apps/details?id=com.cibello.app"', 'href="https://play.google.com/store/apps/details?id=com.cibello.app&amp;referrer=utm_source%3Dcibello.app%26utm_medium%3Dweb%26utm_campaign%3D' + path.strip("/").replace("/", "-") + '"')
    B.write(path, html)

def refresh_fixed_hreflang(reg):
    """Existing Swedish/English pages in a family get the full hreflang set; EN tonight page gets the tool."""
    for fam, slugs in reg.items():
        for lang in ("sv", "en"):
            p = FIXED[fam].get(lang)
            if not p: continue
            f = ROOT / p.strip("/") / "index.html"
            if not f.exists(): continue
            h = f.read_text(encoding="utf-8")
            block = alt_links_for(fam, reg)
            h2 = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]+">\s*)+', block + "\n", h, count=1)
            if h2 != h: f.write_text(h2, encoding="utf-8")

def inject_tool_en(tool):
    f = ROOT / "en/what-to-eat-tonight/index.html"; h = f.read_text(encoding="utf-8")
    if 'id="middagsval"' in h: return
    h = h.replace('<article class="article">', '<article class="article">' + tool_html("en", tool), 1)
    h = h.replace("</head>", TOOL_CSS + "</head>", 1).replace("</body>", '<script src="/middag.js" defer></script></body>', 1)
    f.write_text(h, encoding="utf-8"); print("tool injected into /en/what-to-eat-tonight/")

def main():
    content, tools = load_all()
    reg = registry(content)
    extra = {}
    for lang, fams in content.items():
        extra[lang] = [(page["slug"], page["label"]) for fam, page in fams.items()]
    (ROOT / "tools" / "guides_extra.json").write_text(json.dumps(extra, ensure_ascii=False, indent=1), encoding="utf-8")
    importlib.reload(sys.modules["sitedata"])
    import sitedata; globals().update({k: getattr(sitedata, k) for k in dir(sitedata) if not k.startswith("_")})
    for lang, fams in content.items():
        for fam, page in fams.items():
            render_page(lang, fam, page, reg, tools.get(lang))
    refresh_fixed_hreflang(reg)
    if "en" in tools: inject_tool_en(tools["en"])
    B.relink_all()
    subprocess.run([sys.executable, str(ROOT / "tools" / "build_home.py")], check=True)

if __name__ == "__main__":
    main()
