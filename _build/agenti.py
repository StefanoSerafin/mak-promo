#!/usr/bin/env python3
"""Copie delle locandine interattive per i colleghi agenti.

Per ogni agente in AGENTI e ogni campagna crea <agente>/<campagna>/ con:
- index.html con nome, numero, link tel: e wa.me dell'agente;
- gli stessi file della campagna (foto, dati, anteprima, icona);
- locandina.jpg rifatta con nome e numero dell'agente (dove la locandina li ha).

Link: stefanoserafin.github.io/mak-promo/<agente>/<campagna>/
Si rilancia dopo ogni modifica a una campagna o quando se ne aggiunge una:
    python3 _build/agenti.py            # tutti gli agenti
    python3 _build/agenti.py angelo     # uno solo
"""
import re
import shutil
import subprocess
import sys
from urllib.parse import quote
from pathlib import Path

PROMO = Path(__file__).resolve().parent.parent
LOCANDINE = PROMO.parent / "Locandine"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE_URL = "https://stefanoserafin.github.io/mak-promo/"

AGENTI = {
    "angelo": {"nome": "Angelo", "cognome": "Magnotta", "tel": "393924501782", "tel_vis": "392 450 1782"},
    "alberto": {"nome": "Alberto", "cognome": "Pianta", "tel": "393355223011", "tel_vis": "335 522 3011"},
}

# Sorgente della locandina con nome e numero; None = l'immagine non li ha, si copia com'è.
SORGENTE_LOCANDINA = {
    "fix-pack": None,
    "halloween-ruotino": None,
    "kit-gomma-ruota": "kit-gomma-ruota-inverno/locandina-flash.html",
    "ts900-rinnovi": "ts900-rinnovi/locandina.html",
}

STEFANO = {"nome": "Stefano", "cognome": "Serafin", "tel": "393316798961", "tel_vis": "331 679 8961"}

# Frasi che hanno senso solo per Stefano (campagna → [(vecchio, nuovo)]).
FRASI = {
    "anelli-centraggio": [
        ("Il mio video breve sugli anelli di centraggio MAK.", "Video breve sugli anelli di centraggio MAK."),
        ("Stefano con gli anelli di centraggio sul tavolo", "Anelli di centraggio sul tavolo"),
    ],
    "kit-gomma-ruota": [("poi WhatsApp e Stefano */", "poi WhatsApp e l'agente */")],
    "ts900-rinnovi": [("poi WhatsApp e Stefano */", "poi WhatsApp e l'agente */")],
}


def campagne():
    return sorted(p.name for p in PROMO.iterdir()
                  if p.is_dir() and (p / "index.html").exists()
                  and not p.name.startswith(("_", ".")) and p.name not in AGENTI)


def sostituisci(testo, a, c, frasi=True):
    s = STEFANO
    for vecchio, nuovo in (FRASI.get(c, []) if frasi else []):
        assert vecchio in testo, f"{c}: frase non trovata: {vecchio}"
        testo = testo.replace(vecchio, nuovo)
    testo = testo.replace(f"{s['nome']} {s['cognome']}", f"{a['nome']} {a['cognome']}")
    testo = testo.replace(s["tel"], a["tel"]).replace(s["tel_vis"], a["tel_vis"])
    testo = testo.replace("Ciao Stefano", f"Ciao {a['nome']}")
    return testo


def pagina(chiave, a, c):
    t = sostituisci((PROMO / c / "index.html").read_text(encoding="utf-8"), a, c)
    t = t.replace(f"{BASE_URL}{c}/", f"{BASE_URL}{chiave}/{c}/")  # og:url e og:image
    rimasti = re.findall(r"Stefano|Serafin|3316798961|331 679 8961", t)
    assert not rimasti, f"{c}: restano riferimenti a Stefano: {set(rimasti)}"
    return t


def locandina(a, c, dest):
    rel = SORGENTE_LOCANDINA.get(c, f"{c}/locandina.html")
    if rel is None:
        return "copiata"
    src = LOCANDINE / rel
    tmp = src.with_name("_agente_tmp.html")
    png = src.with_name("_agente_tmp.png")
    testo = src.read_text(encoding="utf-8")
    assert STEFANO["tel_vis"] in testo, f"{c}: la locandina non ha il numero di Stefano"
    tmp.write_text(sostituisci(testo, a, c, frasi=False), encoding="utf-8")
    try:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=2", "--window-size=1080,1350",
                        "--virtual-time-budget=3000", f"--screenshot={png}", tmp.as_uri()],
                       check=True, capture_output=True)
        subprocess.run(["sips", "-Z", "1620", "-s", "format", "jpeg", "-s", "formatOptions", "85",
                        str(png), "--out", str(dest / "locandina.jpg")], check=True, capture_output=True)
    finally:
        tmp.unlink(missing_ok=True)
        png.unlink(missing_ok=True)
    return "rifatta"


def genera(chiave):
    a = AGENTI[chiave]
    radice = PROMO / chiave
    for c in campagne():
        dest = radice / c
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(PROMO / c, dest, ignore=shutil.ignore_patterns("index.template.html", ".DS_Store"))
        (dest / "index.html").write_text(pagina(chiave, a, c), encoding="utf-8")
        print(f"{chiave}/{c}: pagina ok, locandina {locandina(a, c, dest)}")
    elenco(chiave, a, radice)


def elenco(chiave, a, radice):
    """Pagina dell'agente con tutti i link: anteprima, titolo, Copia link, Manda su WhatsApp."""
    voci = []
    for c in campagne():
        h = (radice / c / "index.html").read_text(encoding="utf-8")
        m = re.search(r'<meta property="og:title" content="([^"]*)"', h)
        titolo = m.group(1) if m else c
        m = re.search(r'<meta property="og:description" content="([^"]*)"', h)
        desc = m.group(1) if m else ""
        url = f"{BASE_URL}{chiave}/{c}/"
        voci.append(
            f'<div class="v"><a href="{c}/" class="img"><img src="{c}/anteprima.jpg" alt="" loading="lazy" width="1200" height="630"></a>'
            f'<div class="t"><b>{titolo}</b><small>{desc}</small><code>{url}</code>'
            f'<div class="bt"><button type="button" data-url="{url}">Copia link</button>'
            f'<a class="wa" href="https://wa.me/?text={quote(url)}" target="_blank" rel="noopener">Manda su WhatsApp</a></div></div></div>')
    n = len(voci)
    (radice / "index.html").write_text(f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Locandine MAK · {a["nome"]} {a["cognome"]}</title>
<style>
:root{{--red:#da2128;--ink:#14161a;--mute:#5d626b;--card:#f3f4f6;--verde:#25d366}}
*{{box-sizing:border-box}}
body{{margin:0;background:#fff;color:var(--ink);font-family:"Avenir Next",-apple-system,system-ui,sans-serif;line-height:1.4}}
.wrap{{max-width:560px;margin:0 auto;padding:24px 16px 40px}}
h1{{font-family:"DIN Condensed","Arial Narrow",sans-serif;font-size:40px;line-height:1;text-transform:uppercase;margin:6px 0 4px}}
h1 span{{color:var(--red)}}
.k{{font-size:13px;letter-spacing:3px;color:var(--red);font-weight:700;text-transform:uppercase}}
p.sub{{color:var(--mute);font-size:15px;margin:6px 0 20px}}
.v{{background:var(--card);border-radius:16px;overflow:hidden;margin-bottom:14px}}
.v .img{{display:block;line-height:0}}
.v img{{width:100%;height:auto;display:block}}
.t{{padding:12px 14px 14px}}
.t b{{display:block;font-size:17px}}
.t small{{display:block;color:var(--mute);font-size:13px;margin-top:3px}}
.t code{{display:block;font-size:12px;color:var(--mute);margin-top:8px;word-break:break-all}}
.bt{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px}}
.bt button,.bt a{{font:inherit;font-size:14px;font-weight:700;border:0;border-radius:12px;padding:12px 8px;text-align:center;text-decoration:none}}
.bt button{{background:var(--ink);color:#fff}}
.bt a{{background:var(--verde);color:#062e16}}
.bt button.ok{{background:#14833b}}
</style></head><body><div class="wrap">
<div class="k">Locandine interattive MAK</div>
<h1>{a["nome"]} <span>{a["cognome"]}</span></h1>
<p class="sub">{n} locandine con il tuo numero ({a["tel_vis"]}): «Chiamami» e WhatsApp arrivano a te. Copia il link e mandalo ai clienti: in chat compare l'anteprima.</p>
{chr(10).join(voci)}
</div>
<script>
document.addEventListener("DOMContentLoaded", () => {{
  document.querySelectorAll("button[data-url]").forEach(b => b.addEventListener("click", () => {{
    const u = b.dataset.url, fatto = () => {{ b.textContent = "Copiato ✓"; b.classList.add("ok"); setTimeout(() => {{ b.textContent = "Copia link"; b.classList.remove("ok"); }}, 1800); }};
    if (navigator.clipboard) navigator.clipboard.writeText(u).then(fatto, () => vecchio(u, fatto)); else vecchio(u, fatto);
  }}));
  function vecchio(u, fatto) {{ const t = document.createElement("textarea"); t.value = u; document.body.appendChild(t); t.select(); try {{ document.execCommand("copy"); fatto(); }} catch (e) {{}} t.remove(); }}
}});
</script></body></html>
""", encoding="utf-8")

if __name__ == "__main__":
    for k in (sys.argv[1:] or AGENTI):
        genera(k)
