#!/usr/bin/env python3
"""Volto di Stefano che parla nel bottone «Spiegamelo a voce» di una campagna.

Uso (dalla cartella mak-promo):
    python3 _build/volto.py <campagna> <video-heygen.mp4> [--crop 860:860:110:100]

1. Ritaglia il video HeyGen verticale (1080×1920) in un quadrato sul viso → <campagna>/volto.mp4
   (320×320, H.264 + AAC, faststart) e prende la copertina a 2,5 s → <campagna>/volto.jpg.
2. Nella pagina (index.html, e index.template.html se c'è) toglie <audio> e conto alla rovescia,
   mette il cerchio con il video e l'anello rosso di avanzamento. Modello: tool8-ma41 (2026-11-14).

Il ritaglio predefinito va bene per il look ad7af22c2a2a4ee3944f2fbb302e176e; per un altro look
controllare il foglio dei fotogrammi (<campagna>/../_build/ non viene toccato) e passare --crop.
"""
import datetime, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
V = datetime.date.today().strftime("%Y%m%d")

CSS_OLD = ".voce .dur{font-family:var(--titolo);font-size:22px;padding-top:3px;position:relative;z-index:1}"
CSS_NEW = """.voce button{grid-template-columns:52px 1fr 116px;gap:10px;padding:10px 10px 10px 12px}
/* volto di Stefano che parla, con l'anello rosso dell'avanzamento */
.voce .volto{width:116px;height:116px;position:relative;z-index:1}
.voce .volto video{position:absolute;inset:7px;width:102px;height:102px;border-radius:50%;object-fit:cover;background:#2a2c31}
.voce .volto svg{position:absolute;inset:0;width:116px;height:116px;transform:rotate(-90deg)}
.voce .volto circle{fill:none;stroke-width:5}
.voce .volto .tr{stroke:rgba(255,255,255,.18)}
.voce .volto .av{stroke:var(--red);stroke-linecap:round;transition:stroke-dashoffset .25s linear}"""
VOLTO = f"""<span class="volto">
      <video id="voceAudio" src="volto.mp4?v={V}" poster="volto.jpg?v={V}" playsinline preload="metadata"></video>
      <svg viewBox="0 0 116 116" aria-hidden="true"><circle class="tr" cx="58" cy="58" r="55"/><circle class="av" id="voceAnello" cx="58" cy="58" r="55" stroke-dasharray="345.6" stroke-dashoffset="345.6"/></svg>
    </span>"""
JS = [
    ('dur = document.getElementById("voceDur")', 'anello = document.getElementById("voceAnello")'),
    ('const mmss = s => Math.floor(s / 60) + ":" + String(Math.floor(s % 60)).padStart(2, "0");',
     "const GIRO = 345.6; /* circonferenza dell'anello: 2π × 55 */"),
    ('bar.style.width = (a.currentTime / a.duration * 100) + "%";\n    dur.textContent = mmss(Math.max(0, a.duration - a.currentTime));',
     'const f = a.currentTime / a.duration;\n    bar.style.width = (f * 100) + "%";\n    anello.style.strokeDashoffset = GIRO * (1 - f);'),
    ('bar.style.width = "0"; dur.textContent = mmss(a.duration);',
     'bar.style.width = "0"; anello.style.strokeDashoffset = GIRO;'),
]


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def pagina(p: pathlib.Path):
    s = p.read_text()
    if 'id="voceAnello"' in s:
        print(f"  {p.name}: già col volto, non tocco")
        return
    def una(old, new, testo):
        n = testo.count(old)
        if n != 1:
            sys.exit(f"  {p.name}: atteso 1 volta, trovato {n}: {old[:70]}")
        return testo.replace(old, new)
    s = una(CSS_OLD, CSS_NEW, s)
    s, n = re.subn(r'<span class="dur" id="voceDur">[^<]*</span>', VOLTO, s)
    if n != 1: sys.exit(f"  {p.name}: conto alla rovescia trovato {n} volte")
    s, n = re.subn(r'\n\s*<audio id="voceAudio"[^>]*></audio>', "", s)
    if n != 1: sys.exit(f"  {p.name}: <audio> trovato {n} volte")
    for old, new in JS:
        s = una(old, new, s)
    p.write_text(s)
    print(f"  {p.name}: aggiornata")


def main():
    a = sys.argv[1:]
    crop = "860:860:110:100"
    if "--crop" in a:
        i = a.index("--crop"); crop = a[i + 1]; del a[i:i + 2]
    if len(a) != 2:
        sys.exit(__doc__)
    camp, src = ROOT / a[0], pathlib.Path(a[1]).expanduser()
    if not (camp / "index.html").exists():
        sys.exit(f"Campagna inesistente: {camp}")
    out = camp / "volto.mp4"
    ffmpeg("-i", str(src), "-vf", f"crop={crop},scale=320:320:flags=lanczos",
           "-c:v", "libx264", "-profile:v", "main", "-pix_fmt", "yuv420p", "-crf", "26", "-preset", "slow",
           "-r", "25", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", str(out))
    ffmpeg("-ss", "2.5", "-i", str(out), "-frames:v", "1", "-q:v", "3", str(camp / "volto.jpg"))
    foglio = src.with_name(src.stem + "-fotogrammi.jpg")
    ffmpeg("-i", str(out), "-vf", "fps=1,scale=96:96,tile=10x4", "-frames:v", "1", str(foglio))
    print(f"volto.mp4 {out.stat().st_size // 1024} KB; fotogrammi da guardare: {foglio}")
    for nome in ("index.template.html", "index.html"):
        if (camp / nome).exists():
            pagina(camp / nome)
    if (camp / "index.template.html").exists():
        print("  c'è index.template.html: rigenerare index.html con _build/build.py se la pagina lo richiede")


if __name__ == "__main__":
    main()
