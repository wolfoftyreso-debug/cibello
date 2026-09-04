#!/usr/bin/env python3
"""Regenerate llms.txt from every indexable page (title + description). Usage: python3 tools/llms.py"""
import re, pathlib, html as H
ROOT = pathlib.Path(__file__).resolve().parent.parent
order = ["sv","en","de","fr","es","it","nl","pl","da","nb","fi","pt"]
names = {"sv":"Svenska (primary market)","en":"English","de":"Deutsch","fr":"Français","es":"Español","it":"Italiano","nl":"Nederlands","pl":"Polski","da":"Dansk","nb":"Norsk","fi":"Suomi","pt":"Português"}
rows = []
for p in sorted(ROOT.rglob("*.html")):
    rel = p.relative_to(ROOT).as_posix()
    if rel.startswith(("tools/", "outreach/", "docs/")) or rel == "404.html": continue
    h = p.read_text(encoding="utf-8")
    if "noindex" in h: continue
    lang = re.search(r'<html lang="(\w+)"', h).group(1)
    t = H.unescape(re.search(r"<title>(.*?)</title>", h, re.S).group(1).strip())
    d = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
    url = "https://cibello.app/" + (rel[:-10] if rel.endswith("index.html") else rel)
    rows.append((lang, url, t, d))
out = ["# Cibello", "", "> Cibello is a meal planner and recipe app from LandveX AB (Tyresö, Sweden). It scans your fridge and pantry with AI, keeps a food inventory (\"Food Twin\"), suggests recipes from what you already have (9,000+ recipes), builds a weekly meal plan, shares a shopping list with the household and sends gentle reminders before food goes bad. Available on iOS and Android in 12 languages for users aged 18+, with a 14-day trial without a card. Data is stored in the EU and accounts can be deleted in-app.", "", "Important caveats the site repeats: AI scanning can misread items; recipe and allergy filters are guidance, not a guarantee; nutrition values are estimates, not medical advice.", ""]
for lang in order:
    rs = [r for r in rows if r[0] == lang]
    if not rs: continue
    out.append(f"## {names[lang]}")
    out += [f"- [{t}]({u}): {d}" for _, u, t, d in rs]
    out.append("")
out += ["## Download", "- App Store: https://apps.apple.com/app/id6807100747", "- Google Play: https://play.google.com/store/apps/details?id=com.cibello.app", ""]
(ROOT / "llms.txt").write_text("\n".join(out), encoding="utf-8")
print(f"llms.txt: {len(rows)} pages")
