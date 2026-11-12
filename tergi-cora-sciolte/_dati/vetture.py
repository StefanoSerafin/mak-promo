"""Dal prontuario pubblico CO.RA. (Mak/cora-portale/grezzi/prontuario-CORA.json, scarica_prontuario.py)
alle misure TotalFit per vettura della pagina: tergi-cora-sciolte/vetture.json.
Uso (da Mak/mak-promo/): python3 tergi-cora-sciolte/_dati/vetture.py"""
import json, re, datetime
from pathlib import Path
QUI = Path(__file__).resolve().parent.parent
SRC = QUI.parents[1] / "cora-portale/grezzi/prontuario-CORA.json"
POS = {"ANTERIORE LATO GUIDA": 0, "ANTERIORE LATO PASSEGGERO": 1, "POSTERIORE": 2}

def anno(t):  # "03.80" -> "03/1980", "92" -> "1992"
    m = re.fullmatch(r"(?:(\d\d)\.)?(\d\d)", t.strip())
    if not m: return t.strip()
    y = int(m.group(2)); y += 1900 if y >= 30 else 2000
    return (m.group(1) + "/" if m.group(1) else "") + str(y)

def anni(t):
    t = t.strip()
    m = re.fullmatch(r"([0-9.]*)\s*[>-]\s*([0-9.]*)", t)
    if not m: return t
    a, b = m.group(1), m.group(2)
    if a and b: return anno(a) + " → " + anno(b)
    if a: return "dal " + anno(a)
    if b: return "fino al " + anno(b)
    return t

d = json.loads(SRC.read_text())
out, n = [], 0
for x in d:
    mod = {}
    for r in x["righe"]:
        p = POS.get(r["posizione"])
        if p is None: continue
        mm = sorted({int(a["cod"][2:]) for a in r["articoli"] if re.fullmatch(r"TF\d+", a["cod"])})
        mod.setdefault(r["modello"], [[], [], []])[p] = mm
    ms = {}
    for nome in x["modelli"]:
        if nome not in mod or not any(mod[nome]): continue
        nm, sep, coda = nome.rpartition(" - ")
        if not sep or not re.match(r"[>\d]", coda): nm, coda = nome, ""
        ms.setdefault(nm.strip(), []).append([anni(coda) if coda else "tutti gli anni"] + mod[nome]); n += 1
    def inizio(v):
        y = re.findall(r"(?:(\d\d)/)?(\d{4})", v[0])
        return (int(y[0][1]), int(y[0][0] or 0)) if y and not v[0].startswith("fino") else (0, 0)
    for v in ms.values(): v.sort(key=inizio)
    if ms:
        out.append({"n": x["marca"], "m": [[k, v] for k, v in sorted(ms.items(), key=lambda kv: kv[0].lower())]})
out.sort(key=lambda m: m["n"])
(QUI / "vetture.json").write_text(json.dumps({"data": datetime.date.today().isoformat(), "marche": out}, ensure_ascii=False, separators=(",", ":")))
print(len(out), "marche,", n, "vetture con almeno una TotalFit")
