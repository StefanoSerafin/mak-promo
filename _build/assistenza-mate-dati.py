#!/usr/bin/env python3
"""marche.js per la pagina assistenza-mate: marche, modelli e procedure dall'app Apprendimento TPMS.

Fonte: ../mak-tpms-relearn/data/brands.json (schede MATE). Rilanciare dopo ogni aggiornamento dell'app.
"""
import json
from pathlib import Path

PROMO = Path(__file__).resolve().parent.parent
SRC = PROMO.parent / "mak-tpms-relearn" / "data" / "brands.json"

marche = []
for b in json.load(open(SRC, encoding="utf-8"))["brands"]:
    proc = []
    for p in b["procedures"]:
        t = p["title"] + (" · " + p["applies"] if p.get("applies") else "")
        if t not in proc:
            proc.append(t)
    marche.append({"n": b["name"], "s": b["slug"], "pdf": b["pdf"], "m": b["models"], "p": proc})
js = ("/* Generato da _build/assistenza-mate-dati.py dall'app Apprendimento TPMS: non modificare a mano. */\n"
      "const MARCHE = " + json.dumps(marche, ensure_ascii=False, separators=(",", ":")) + ";\n")
(PROMO / "assistenza-mate" / "marche.js").write_text(js, encoding="utf-8")
print(len(marche), "marche,", len(js) // 1024, "KB")
