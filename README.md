# mak-promo — locandine interattive

Versione web delle locandine promo: una cartella per campagna, pubblicata su GitHub Pages
(`stefanoserafin.github.io/mak-promo/<campagna>/`). Il link si manda su WhatsApp al posto
dell'immagine: l'anteprima mostra la locandina (`anteprima.jpg`, 1200×630, tag `og:image`),
il tocco apre la pagina con bottoni e ricerca.

## halloween-ruotino (25 ott – 1 nov 2026)

- `locandina.jpg`: la locandina originale (estratta dal PDF sulla Scrivania).
- `index.template.html`: la pagina da modificare a mano; `index.html` si genera.
- Ricerca vettura → ruotino dai dati del configuratore NPK (`../noproblemkit/dati/ruotini.csv`).
- In promo = ruotino in acciaio fino a 17" (regola in `PROMO` dentro la pagina).
- Bottone WhatsApp con l'ordine già scritto, conto alla rovescia, chiamata, B2B.

Rigenera: `python3 _build/build.py`

## kit-gomma-ruota (stagione invernale, montaggio gratuito fino al 31/12/2026)

- `locandina.jpg`: la locandina con il flash, da `../Locandine/kit-gomma-ruota-inverno/locandina-flash.html`.
- `index.template.html` da modificare a mano; `index.html` lo genera `_build/build.py` con dentro marche e modelli del configuratore NPK (`../noproblemkit/dati/veicoli.csv`).
- `kit.webp`: foto del kit Davinci scontornata (ruota che gira scorrendo la pagina).
- Richiesta kit guidata: foto del libretto oppure marca → modello → anno, misura, preferenze ruota (silver, nero, diamantato, prezzo promo; anche più di una), invernale/4 stagioni, TPMS, quantità → messaggio WhatsApp già scritto.
- Con il libretto il bottone verde apre il menu Condividi (foto + testo, poi WhatsApp e Stefano); dove non si possono condividere file apre la chat e chiede di allegarlo. La foto non passa da nessun server.
- Barra fissa in alto «Vuoi un preventivo? Compila la richiesta» che porta al form e sparisce quando lo si raggiunge.
- Conto alla rovescia al 31/12 in fondo alla pagina; a promo finita diventa «Chiedimi le offerte attive».
- Anteprima: `_build/anteprima-kit-gomma-ruota.html` → `anteprima.jpg` (Chrome senza finestra, 1200×630).

## prossima-fermata-futuro (storia sull'IA, senza scadenza)

- Storia in 8 scene: il treno «Intelligenza Artificiale», chi sale e chi resta sulla banchina; le stazioni cambiano nome (Futuro → Presente → Passato).
- Disegni SVG generati da `../Locandine/prossima-fermata-futuro/scene.py`; `build.py` nella stessa cartella scrive la locandina (clienti e colleghi) e `index.html` da `index.template.html` (le scene vanno al posto di `<!--__SCENE__-->`).
- Visore a storie: tocco a destra/sinistra, swipe, frecce; tabellone a palette nella scena 5, braccio animato nelle scene 6-7. Niente conto alla rovescia.
- Anteprima: `../Locandine/prossima-fermata-futuro/anteprima.html` → `anteprima.jpg`.

## fix-pack (Fix Pack 2026, 154,00 €, senza scadenza)

- `locandina.jpg`: la locandina ricevuta (853×1280, da Downloads il 2026-10-26).
- `index.html` scritto a mano (nessun dato incorporato): i 7 kit della locandina sono in `KIT` dentro la pagina, codici verificati sul database ordini.
- Schede dei kit da toccare per aggiungerli; ordine a righe (menu codice + quantità + togli), «+ Aggiungi riga», «+ Fix Pack completo», nome officina facoltativo → messaggio WhatsApp con codici e quantità.
- Niente conto alla rovescia (la locandina non ha scadenza). Barra in alto che porta all'ordine.
- Anteprima: `_build/anteprima-fix-pack.html` → `anteprima.jpg`; icona da `_build/icona-fix-pack.html`.

## refill-multisens (Refill 20 MATE MULTIsens MP6, 15,90 € cad. + IVA, senza scadenza)

- `locandina.jpg`: da `../Locandine/refill-multisens/locandina.html` (PNG/PDF clienti e colleghi nella stessa cartella).
- `index.html` scritto a mano: tre righe fisse (930000MP6R Rubber, 93000MP6BM Metal Black, 930000MP6M Silver) con il campo pezzi, barra verso i 20 minimi (anche misti), bottoni «20 Rubber», «20 Metal Silver», «Azzera», totale indicativo a 20,40 € sotto il minimo e a 15,90 € da 20 in su, risparmio, messaggio WhatsApp con codici e pezzi.
- Foto: sensori ritagliati dallo screenshot B2B, MA41 da `Video Avatar/Immagini/MATE/MATE MA41.png`, scontornati con `../Locandine/refill-multisens/scontorna.py`.
- Anteprima: `_build/anteprima-refill-multisens.html`; icona: `_build/icona-refill-multisens.html`.

## refill-autel-mx (Refill 20 AUTEL MX, 18,47 € cad. + IVA, senza scadenza)

- Stessa struttura di `refill-multisens/`: locandina da `../Locandine/refill-autel-mx/locandina.html` (disco nero perché lo strumento è rosso), tre righe fisse (93000000MXG Rubber, 9300000MXB Metal Black, 93000000MX Silver), da 22,45 € a 18,47 €, bottoni «20 Rubber», «20 Metal Silver», «Azzera».
- Foto: sensori ritagliati dallo screenshot B2B, AUTEL TS508 WF da `Video Avatar/Immagini/MATE/MATE/`.
- Anteprima: `_build/anteprima-refill-autel-mx.html`; icona: `_build/icona-refill-autel-mx.html`.

## riempicarrello (12 articoli «riempicarrello» del B2B, senza scadenza)

- Dati degli articoli in `prodotti.js` (codice, nome, descrizione, prezzo netto, listino barrato): la fonte è `../Locandine/riempicarrello/prodotti.js`, usata anche dalla locandina; se cambia, ricopiarla qui insieme alle foto.
- `foto/<codice>.png` ritagliate dagli screenshot del carrello B2B del 2026-10-26.
- Una scheda per articolo con quantità, riepilogo con totale + IVA e risparmio sui listini, messaggio WhatsApp con quantità, codici e prezzi.
- Anteprima: `_build/anteprima-riempicarrello.html`; icona: `_build/icona-riempicarrello.html`.

## adblue (AdBlue by Azotal, 4 confezioni, senza scadenza)

- Dati in `prodotti.js` (codice, litri, confezione, prezzo, trasporto 30 € a bancale Nord e Toscana): la fonte è `../Locandine/adblue/prodotti.js`, presi dalla locandina MAK ufficiale nell'eBook agenti (copia del 2026-10-03); se cambia, ricopiarla qui.
- `foto/`: fustino, fusto e cisterna da `Video Avatar/Immagini/MAK/` senza la scritta «ordine min.», più la foto di gruppo.
- Scala del prezzo al litro animata, una scheda per confezione con i bancali, riepilogo con merce, trasporto e totale + IVA, messaggio WhatsApp con codici, litri e totale; scheda «Perché Azotal» dalla scheda tecnica SP10.
- Anteprima: `_build/anteprima-adblue.html`; icona: `_build/icona-adblue.html`.

## calze-light-espositore (starter kit 10 paia Multigrip Light + espositore da banco, 188,40 € + IVA)

- `kit.js` generato da `../Locandine/calze-light-espositore/genera_dati.py`: le 483 misure → taglia Light dall'app `../mak-calze-neve/data/socks.json` e il «mix più ordinato» da 10 paia calcolato sulle righe d'ordine delle Light (nella pagina va solo il mix). Dopo averlo rigenerato, ricopiarlo qui.
- Ricerca taglia larghezza → serie → diametro, bottone «+ Al kit» che ricorda la misura; kit con 9 taglie, contatore x/10, «Mix più ordinato», «Azzera»; messaggio WhatsApp con taglie, codici 73000SSL0x, paia e misure.
- Foto vere: espositore da `Video Avatar/Immagini/NPK/espositore calze.jpg` (le altre due foto dell'espositore in quella cartella sono generate e non vanno usate), ruota con la Light ritagliata dalla promo push NPK di ottobre 2025 (eBook).
- Anteprima: `_build/anteprima-calze-light.html`; icona: `_build/icona-calze-light.html`.

## distanziali-xilema (pubblica, SENZA prezzi)

- `dati.js` generato da `../Locandine/distanziali-xilema/genera_dati.py` dal dataset in chiaro dell'app con PIN (`../mak-distanziali-xilema/data/distanziali.plain.json`, non versionato): vettura, anni, fissaggio, note, interasse, centraggio, spessore e i tre codici. I prezzi non escono mai (lo script lo controlla). Dopo un file Xilema nuovo: build dell'app con PIN, poi `genera_dati.py`, poi ricopiare qui.
- Marca → vettura → scheda con interasse, centraggio, fissaggio e note toccabili (testo del catalogo Xilema 2016), spessori con i codici delle tre varianti; un tocco sul codice lo aggiunge alla richiesta (coppie); messaggio WhatsApp con codici, spessori, varianti e vettura, che chiede prezzo e disponibilità.
- Foto: le 4 tipologie ritagliate dalla pagina del catalogo Xilema (`../mak-distanziali-xilema/assets/tipo-*.jpg`), schiarite. Avvertenza Xilema (non omologati per il codice della strada) nella locandina e nella pagina.
- Anteprima: `_build/anteprima-distanziali-xilema.html`; icona: `_build/icona-distanziali-xilema.html`.

## tergi-cora (kit spazzole tergi CO.RA. TotalFit con espositore da muro)

- Dati in `kit.js` (fonte: `../Locandine/tergi-cora/kit.js`), dal file «Promo KIT SPAZZOLE TERGI CORA - MAK Total Fit.xlsx» dell'eBook agenti (listino CO.RA. 1/5/2025, −60%; kit 140 −5% in più) e dalla campagna Mailchimp del 20/10/2026. Kit 70: 7 misure × 10 = 327,20 €; kit 140: 14 misure × 10 = 671,46 €; espositore EXPOTERGIMURO (listino 35 €) incluso.
- Foto: i due espositori da muro estratti dallo stesso Excel.
- Scelta promo 70 (−60%) o 140 (−60% −5%); tutti i 14 codici TF selezionabili in entrambe con la quantità modificabile, partendo dalla composizione della promo (`CODICI` e `PROMO` in `kit.js`, netti = listino × sconto, arrotondati come nel file CO.RA.); contatore verso 70/140, risparmio sul listino, messaggio WhatsApp con i codici scelti; pioggia animata sulla locandina.
- La foto `Video Avatar/Immagini/MAK/Espositore Tergi.png` (espositore a terra Tergiplus) non va usata: tolta su indicazione di Stefano il 2026-10-26.
- Anteprima: `_build/anteprima-tergi-cora.html`; icona: `_build/icona-tergi-cora.html`.

## canali-etrto (verifica pneumatico → canali ETRTO, senza prezzi)

- `dati.js` generato da `../Locandine/canali-etrto/genera_dati.py`, che usa la lettura dell'app `../mak-etrto-canali/data/build.py` su `Mak/Canali XLS.xlsx` (684 misure); il canale «9» senza lettera di 285/45 R19–R22 diventa «9J».
- Larghezza → serie → diametro, scala dei canali con quelli ammessi in verde, tendina «Hai già il cerchio?» con esito ammesso/fuori tabella (31 misure piccole ammettono sia J sia B: la scala usa la J, il controllo guarda la larghezza), messaggio WhatsApp con misura, canali e cerchio verificato.
- Anteprima: `_build/anteprima-canali-etrto.html`; icona: `_build/icona-canali-etrto.html`.
