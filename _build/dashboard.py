#!/usr/bin/env python3
"""Rigenera l'elenco delle locandine per la dashboard (_dashboard/campagne.js).

Va lanciato a ogni campagna nuova (o quando cambia un og:title), dalla cartella mak-promo:
    python3 _build/dashboard.py

Prende le campagne con la stessa regola di agenti.campagne() (cartelle con index.html, senza «_»/«.»,
escluse le copie dei colleghi), legge og:title e og:description, la data del primo commit e
l'argomento (e le «parole» facoltative per la ricerca) da _build/argomenti.json. Si ferma se una campagna non ha l'argomento, se manca
l'anteprima o se argomenti.json cita una campagna che non c'è più. Aggiorna anche il numero di
versione di campagne.js dentro _dashboard/index.html (cache di Safari) e scrive _dashboard/filtri.json,
le regole con cui il contatore toglie le prove di Stefano dai numeri (data di partenza di ogni
locandina, invii di massa, giorni di modifica fino a «_mio_dal»).
"""
import hashlib
import html
import json
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

PROMO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROMO / "_build"))
from agenti import campagne  # noqa: E402  (stessa regola delle copie dei colleghi)

BASE_URL = "https://stefanoserafin.github.io/mak-promo/"
ARG = PROMO / "_build" / "argomenti.json"
DASH = PROMO / "_dashboard"
OUT = DASH / "campagne.js"
INIZIO_CONTATORE = "2026-11-03"   # primo giorno del contatore mak-promo-conta
COMMIT_DI_MASSA = 5               # un commit su più cartelle di così non è una modifica da provare
GIORNO = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def meta(h, prop):
    m = re.search(r'<meta property="og:' + prop + r'" content="([^"]*)"', h)
    return html.unescape(m.group(1)).strip() if m else ""


def primo_commit(c):
    r = subprocess.run(["git", "log", "--diff-filter=A", "--format=%as", "--", f"{c}/index.html"],
                       cwd=PROMO, capture_output=True, text=True)
    righe = r.stdout.split()
    return righe[-1] if righe else date.today().isoformat()  # non ancora committata: oggi


def giorni_lavoro(elenco):
    """{campagna: giorni con almeno un commit nella sua cartella}. I commit che toccano più di
    COMMIT_DI_MASSA cartelle insieme (es. l'aggiunta di conta.js) sono modifiche meccaniche: non contano."""
    r = subprocess.run(["git", "log", "--format=%x00%ad", "--date=format:%Y-%m-%d", "--name-only"],
                       cwd=PROMO, capture_output=True, text=True)
    noti, out = set(elenco), {c: set() for c in elenco}
    for blocco in r.stdout.split("\x00")[1:]:
        righe = [x.strip() for x in blocco.strip().splitlines() if x.strip()]
        if not righe:
            continue
        toccate = {x.split("/")[0] for x in righe[1:] if "/" in x} & noti
        if len(toccate) <= COMMIT_DI_MASSA:
            for c in toccate:
                out[c].add(righe[0])
    return out


def filtri(voci, giorni, mio_dal):
    """Regole delle prove per il Worker (vedi Mak/mak-promo-conta/README.md, «Prove escluse dai numeri»)."""
    oggi = date.today().isoformat()
    regole, esclusi = {}, set()
    for v in voci:
        c, pub, massa = v["c"], v["dal"], v["invio_massa"]
        mod = sorted(g for g in giorni.get(c, ()) if pub < g < (mio_dal or "9999") and g != massa and g <= oggi)
        regole[c] = {"pubblicata": pub, "conta_dal": v["conta_dal"], "invio_massa": massa, "giorni_modifica": mod}
        g = INIZIO_CONTATORE
        while g < v["conta_dal"]:
            esclusi.add(f"{c}|{g}")
            g = (date.fromisoformat(g) + timedelta(days=1)).isoformat()
        esclusi.update(f"{c}|{x}" for x in mod)
    return {"generato": oggi,
            "regola": "Conta dal giorno dopo la pubblicazione (le locandine mandate in massa dal giorno dell'invio); "
                      "prima di «mio_dal» si saltano anche i giorni di modifica; dal primo invio WhatsApp dalla "
                      "dashboard le aperture contano comunque; mai gli eventi «mio».",
            "mio_dal": mio_dal, "inizio_contatore": INIZIO_CONTATORE,
            "campagne": regole, "esclusi": sorted(esclusi)}


def main():
    conf = json.loads(ARG.read_text(encoding="utf-8"))
    argomenti, mappa = conf["argomenti"], conf["campagne"]
    mio_dal = conf.get("_mio_dal")
    elenco = campagne()
    errori = []
    if mio_dal is not None and not GIORNO.match(str(mio_dal)):
        errori.append(f"«_mio_dal» deve essere AAAA-MM-GG oppure null, non «{mio_dal}»")
    for c in elenco:
        massa = mappa.get(c, {}).get("invio_massa")
        if massa is not None and not GIORNO.match(str(massa)):
            errori.append(f"«{c}»: «invio_massa» deve essere AAAA-MM-GG, non «{massa}»")
    for c in elenco:
        if c not in mappa:
            errori.append(f"«{c}» non ha l'argomento: aggiungila in _build/argomenti.json")
        elif mappa[c].get("argomento") not in argomenti:
            errori.append(f"«{c}»: argomento «{mappa[c].get('argomento')}» non è fra {argomenti}")
        if not (PROMO / c / "anteprima.jpg").exists():
            errori.append(f"«{c}» non ha anteprima.jpg")
        parole = mappa.get(c, {}).get("parole", [])
        if not isinstance(parole, list) or not all(isinstance(x, str) and x.strip() for x in parole):
            errori.append(f"«{c}»: «parole» deve essere una lista di parole, es. [\"ruotino\", \"npk\"]")
    for c in mappa:
        if c not in elenco:
            errori.append(f"«{c}» è in argomenti.json ma la cartella non c'è più")
    if errori:
        sys.exit("dashboard.py si ferma:\n- " + "\n- ".join(errori))

    voci = []
    for c in elenco:
        h = (PROMO / c / "index.html").read_text(encoding="utf-8")
        dal, massa = primo_commit(c), mappa[c].get("invio_massa")
        if massa and massa < dal:
            sys.exit(f"dashboard.py si ferma: «{c}» ha invio_massa {massa} prima della pubblicazione {dal}")
        voci.append({"c": c, "titolo": meta(h, "title") or c, "desc": meta(h, "description"),
                     "argomento": mappa[c]["argomento"], "archiviata": bool(mappa[c].get("archiviata")),
                     "dal": dal, "url": mappa[c].get("url") or BASE_URL + c + "/", "privata": bool(mappa[c].get("privata")),
                     "parole": [x.strip() for x in mappa[c].get("parole", [])],
                     "invio_massa": massa,
                     "conta_dal": massa or (date.fromisoformat(dal) + timedelta(days=1)).isoformat()})

    f = filtri(voci, giorni_lavoro(elenco), mio_dal)
    (DASH / "filtri.json").write_text(json.dumps(f, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    vecchie = set(re.findall(r'"c":\s*"([^"]+)"', OUT.read_text(encoding="utf-8"))) if OUT.exists() else set()
    corpo = ("const ARGOMENTI = " + json.dumps(argomenti, ensure_ascii=False) + ";\n"
             "const MIO_DAL = " + json.dumps(mio_dal) + ";\n"
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
    massa = [f"{v['c']} {v['invio_massa']}" for v in voci if v["invio_massa"]]
    print(f"filtri.json: {len(f['esclusi'])} giorni-locandina esclusi; invii di massa: {', '.join(massa) or 'nessuno'}; "
          f"giorni di modifica " + (f"fino al {mio_dal}" if mio_dal else "esclusi tutti (marchio «mio» non ancora attivo)"))


if __name__ == "__main__":
    main()
