#!/usr/bin/env python3
"""Rigenera l'elenco delle locandine per la dashboard (_dashboard/campagne.js).

Va lanciato a ogni campagna nuova (o quando cambia un og:title), dalla cartella mak-promo:
    python3 _build/dashboard.py

Prende le campagne con la stessa regola di agenti.campagne() (cartelle con index.html, senza «_»/«.»,
escluse le copie dei colleghi), legge og:title e og:description, la data del primo commit e
l'argomento da _build/argomenti.json. Si ferma se una campagna non ha l'argomento, se manca
l'anteprima o se argomenti.json cita una campagna che non c'è più. Aggiorna anche il numero di
versione di campagne.js dentro _dashboard/index.html (cache di Safari).
"""
import hashlib
import html
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

PROMO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROMO / "_build"))
from agenti import campagne  # noqa: E402  (stessa regola delle copie dei colleghi)

BASE_URL = "https://stefanoserafin.github.io/mak-promo/"
ARG = PROMO / "_build" / "argomenti.json"
DASH = PROMO / "_dashboard"
OUT = DASH / "campagne.js"


def meta(h, prop):
    m = re.search(r'<meta property="og:' + prop + r'" content="([^"]*)"', h)
    return html.unescape(m.group(1)).strip() if m else ""


def primo_commit(c):
    r = subprocess.run(["git", "log", "--diff-filter=A", "--format=%as", "--", f"{c}/index.html"],
                       cwd=PROMO, capture_output=True, text=True)
    righe = r.stdout.split()
    return righe[-1] if righe else date.today().isoformat()  # non ancora committata: oggi


def main():
    conf = json.loads(ARG.read_text(encoding="utf-8"))
    argomenti, mappa = conf["argomenti"], conf["campagne"]
    elenco = campagne()
    errori = []
    for c in elenco:
        if c not in mappa:
            errori.append(f"«{c}» non ha l'argomento: aggiungila in _build/argomenti.json")
        elif mappa[c].get("argomento") not in argomenti:
            errori.append(f"«{c}»: argomento «{mappa[c].get('argomento')}» non è fra {argomenti}")
        if not (PROMO / c / "anteprima.jpg").exists():
            errori.append(f"«{c}» non ha anteprima.jpg")
    for c in mappa:
        if c not in elenco:
            errori.append(f"«{c}» è in argomenti.json ma la cartella non c'è più")
    if errori:
        sys.exit("dashboard.py si ferma:\n- " + "\n- ".join(errori))

    voci = []
    for c in elenco:
        h = (PROMO / c / "index.html").read_text(encoding="utf-8")
        voci.append({"c": c, "titolo": meta(h, "title") or c, "desc": meta(h, "description"),
                     "argomento": mappa[c]["argomento"], "archiviata": bool(mappa[c].get("archiviata")),
                     "dal": primo_commit(c), "url": BASE_URL + c + "/"})

    vecchie = set(re.findall(r'"c":\s*"([^"]+)"', OUT.read_text(encoding="utf-8"))) if OUT.exists() else set()
    corpo = ("const ARGOMENTI = " + json.dumps(argomenti, ensure_ascii=False) + ";\n"
             "const CAMPAGNE = " + json.dumps(voci, ensure_ascii=False, indent=1) + ";\n")
    versione = hashlib.sha1(corpo.encode()).hexdigest()[:8]
    DASH.mkdir(exist_ok=True)
    OUT.write_text("/* Generato da _build/dashboard.py: non modificare a mano. */\n"
                   f'const GENERATO = "{date.today().isoformat()}";\n' + corpo, encoding="utf-8")

    pagina = DASH / "index.html"
    if pagina.exists():
        t = pagina.read_text(encoding="utf-8")
        t2 = re.sub(r'campagne\.js\?v=[\w-]*', f"campagne.js?v={versione}", t)
        if t2 != t:
            pagina.write_text(t2, encoding="utf-8")

    for a in argomenti:
        n = [v["c"] for v in voci if v["argomento"] == a]
        print(f"{a}: {len(n)}  ({', '.join(n)})")
    nuove = [v["c"] for v in voci if vecchie and v["c"] not in vecchie]
    print(f"{len(voci)} campagne, campagne.js?v={versione}" + (f"; nuove: {', '.join(nuove)}" if nuove else ""))


if __name__ == "__main__":
    main()
