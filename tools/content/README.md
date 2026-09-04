# Innehållsfiler per språk

En fil per språk, `tools/content/<lang>.py`, som `tools/build_lang.py` renderar till alla språkspecifika sidor. Se `_schema.py` för exakt struktur. Kör `python3 tools/build_lang.py de` (eller `all`) efter ändring, sedan `python3 tools/check.py`.

Regler för texten står i `docs/OVERSATTNINGSBRIEF.md`. Endast fakta ur `docs/FAKTAKONTROLL.md` får användas. Juridiska texter är översättningar av `integritet.html`, `villkor.html` och `delete-account.html`; den svenska versionen gäller vid avvikelse och det ska stå på sidan.
