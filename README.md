# mak-promo — locandine interattive

Versione web delle locandine promo: una cartella per campagna, pubblicata su GitHub Pages
(`stefanoserafin.github.io/mak-promo/<campagna>/`). Il link si manda su WhatsApp al posto
dell'immagine: l'anteprima mostra la locandina (`anteprima.jpg`, 1200×630, tag `og:image`),
il tocco apre la pagina con bottoni e ricerca.

## Dashboard (`_dashboard/`)

https://stefanoserafin.github.io/mak-promo/_dashboard/ — tutte le locandine di Stefano divise per argomento, con «Copia link», «WhatsApp» (testo «Ti mando questo modulo interattivo che spiega tutto:» + link) e «Apri», più i numeri del contatore per oggi, 7 giorni, settimana, mese, mese scorso e da sempre, con grafico per giorno, settimana o mese e dettaglio di ogni campagna. Solo le pagine di Stefano: i colleghi restano fuori.

- **Campagna nuova:** argomento in `_build/argomenti.json`, poi `python3 _build/dashboard.py` (scrive `_dashboard/campagne.js` e aggiorna `campagne.js?v=` nella pagina; si ferma se manca l'argomento o l'anteprima), commit insieme alla campagna.
- **Numeri:** in diretta dal Worker `mak-promo-conta` (`GET /serie` e `/riepilogo`). Servono la chiave di lettura, incollata una volta sul telefono e salvata solo lì (`localStorage`), mai nel codice.
- `_dashboard/` non ha `conta.js` di proposito (non conta sé stessa); `noindex`; icona da `_build/icona-dashboard.html`.

> **File di dati con la versione.** Le pagine caricano `dati.js` come `dati.js?v=AAAAMMGG` (o `-2`, `-3`…): a ogni modifica dei dati si cambia il numero nella pagina. Senza, Safari su iPhone può tenere il `dati.js` vecchio con la pagina nuova; il 2026-11-12 la pagina degli anelli non dava risultati per questo, perché il codice nuovo leggeva prezzi che nel file in cache non c'erano.

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

## calze-neve (calze da neve NPK, tutte le linee, senza promo, con i prezzi netti al paio)

- `dati.js` generato da `../Locandine/calze-neve/genera_dati.py` dalle tabelle di `../mak-calze-neve/data/socks.json`: 685 misure → taglia di The Original (TG.69–97, `73000SS0xx`), Re-Grip (1–9, `73000SSE0x`), Multigrip Light (1–9, `73000SSL0x`), EZ Urban (XS–XXXL, `73000EZ…`, XXXL `7300EZXXXL`). Codici verificati sul database ordini. Grip 3D esclusa: NPK la dà «fine linea». Prezzo netto al paio + IVA per linea (dal 2026-11-02, scelto da Stefano: listino al rivenditore −38%, come negli ordini da un paio): Original 32,24 €, Re-Grip 24,80 €, Light 18,60 €, EZ Urban 15,50 € (XXXL compresa). Dopo averlo rigenerato, ricopiarlo qui.
- Ricerca larghezza → serie → diametro con taglia e codice di tutte e 4 le linee e «+ Aggiungi» (due bottoni dove la tabella EZ dà XXL o XXXL); ordine a righe con paia, «+ Aggiungi» a mano (linea + taglia), officina, «Svuota l'ordine» → WhatsApp con linea, taglia, codice, paia e misura.
- Foto: prodotti ritagliati dalle schede del sito NPK (`../mak-calze-neve/assets/`), The Original grande da `Video Avatar/Immagini/NPK/NPK-calza da neve.png`.
- Locandina: `../Locandine/calze-neve/locandina.html` (PNG/PDF clienti e colleghi). Anteprima: `_build/anteprima-calze-neve.html`; icona: `_build/icona-calze-neve.html`.

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

## tergi-cora-sciolte (spazzole tergi CO.RA. TotalFit senza espositore, −60%)

- `dati.js` (fonte: `../Locandine/tergi-cora-sciolte/dati.js`): 16 codici TF300–TF800 con il listino CO.RA. del 1/5/2025; netto = listino × 0,40 (−60%), come in tutte le conferme d'ordine CO.RA. 2026 (`Mail Mak 2026/_estratti/CoRa`), anche a 5 pezzi per misura. TF300 e TF800 ci sono solo qui.
- Una riga per misura con quantità libera (anche 1), fasce di prezzo, totale, risparmio sul listino, stima del contributo trasporto CO.RA. (2,8%, minimo 11,20 €) e WhatsApp con codici, pezzi e prezzi. Link alla campagna con espositore (`../tergi-cora/`).
- Ricerca per vettura (dal 2026-11-12): marca → modello → anno → misure TotalFit lato guida, lato passeggero e posteriore, con «Aggiungi 1 per posizione all'ordine» e la vettura nel messaggio WhatsApp. Dati in `vetture.json` (67 marche, 2.383 vetture con almeno una TotalFit) generati da `_dati/vetture.py` dal prontuario pubblico CO.RA. (`../cora-portale/grezzi/prontuario-CORA.json`, scaricato con `cora-portale/scarica_prontuario.py`).
- Foto: la spazzola ritagliata da `Mak/Tergi Cora.png` (tabella promo CO.RA.), l'unica foto vera della spazzola sciolta.
- Locandina: `../Locandine/tergi-cora-sciolte/locandina.html` (PNG e PDF). Anteprima: `_build/anteprima-tergi-cora-sciolte.html`; icona: `_build/icona-tergi-cora-sciolte.html` (la stessa di tergi-cora).

## consumo-officina-cora (scorte d'officina dal catalogo CO.RA., fino a −50%)

- `dati.js` (fonte: `../Locandine/consumo-officina-cora/dati.js`): 10 prodotti, 17 codici (kit auto pulita, guanti nitrile Karbon/Onyx/Dynamite per taglia, pasta lavamani, pulitore freni, sbloccante e grasso spray Sigill, WD-40 Professionale, bobine Papernet) con listino CO.RA. del 1/5/2026 e **netti letti sul portale CO.RA. il 12/11/2026** con l'account cliente (`../cora-portale/ANALISI-PRODOTTI.md`, punto 4). Nuovi netti: rileggere il portale con `cora-portale/analizza_catalogo.py --cerca CODICE` e cambiare la versione `?v=` in `index.html`.
- Quantità (verificate il 2026-11-12): il **kit auto pulita va a multipli di 50** (campo `passo` in `dati.js`: + e − vanno di 50, un numero scritto a mano sale al multiplo); collo da 50 sul portale e conferme d'ordine dei clienti MAK solo a 50 e 100. Tutto il resto a pezzo: il multiplo del listino CO.RA. è il collo, non un minimo (66 righe su 97 delle conferme 2026 sono fuori multiplo, per esempio 1 pasta lavamani e 5 box di guanti).
- Una scheda per prodotto con foto, netto, listino barrato e sconto; una riga per taglia o per quantità; totale, risparmio sul listino, stima del contributo trasporto CO.RA. e WhatsApp con codici, pezzi e prezzi. Link a `../tergi-cora-sciolte/` (stesso ordine CO.RA., un solo trasporto).
- Foto: quelle del catalogo CO.RA. (`coraweb.coraitaly.com/dbweb/local/articoli/img/<codice>.jpg`, pubbliche), ridotte a 700 px; `kit-volante.jpg` è il riquadro del volante ritagliato dalla striscia del kit auto pulita. `logo-cora.png` (accanto al logo MAK su locandina, anteprima e fondo pagina, chiesto da Stefano) è `Video Avatar/Immagini/LOGHI/Logo Cora.jpg` ritagliato ai bordi.
- Locandina: `../Locandine/consumo-officina-cora/locandina.html` (PNG e PDF). Anteprima: `_build/anteprima-consumo-officina-cora.html`; icona: `_build/icona-consumo-officina-cora.html`. Vocale «Spiegamelo a voce» di 33 s con la voce clonata (testo in `../Locandine/testi-vocali.md`).

## canali-etrto (verifica pneumatico → canali ETRTO, senza prezzi)

- `dati.js` generato da `../Locandine/canali-etrto/genera_dati.py`, che usa la lettura dell'app `../mak-etrto-canali/data/build.py` su `Mak/Canali XLS.xlsx` (684 misure); il canale «9» senza lettera di 285/45 R19–R22 diventa «9J».
- Larghezza → serie → diametro, scala dei canali con quelli ammessi in verde, tendina «Hai già il cerchio?» con esito ammesso/fuori tabella (31 misure piccole ammettono sia J sia B: la scala usa la J, il controllo guarda la larghezza), messaggio WhatsApp con misura, canali e cerchio verificato.
- Anteprima: `_build/anteprima-canali-etrto.html`; icona: `_build/icona-canali-etrto.html`.

## trasformazioni-nad (guida alle trasformazioni NAD con i moduli da scaricare)

- Contenuti dalla pagina wiki «Omologazione delle ruote a libretto» (confermata da Stefano il 4/10/2026) e dai PDF dell'eBook agenti, sezione «Materiale supporto al cliente».
- `pdf/`: Allegato C (G.U. 13/2/2021), Allegato B (G.U. 24/6/2022) e fac-simile dei bollettini (16 € c/c 4028 + 25 € c/c 9001), copiati senza modifiche; `prev-*.png` sono le miniature della prima pagina.
- Scelta «misura non a libretto / già a libretto» che cambia il percorso (5 passi o 3), requisiti sì/no con esito (M1, libretto italiano, ruota NAD; N1 escluso), passi con il controllo del certificato NAD sul B2B e l'avviso (GS0), moduli da scaricare, richiesta WhatsApp con foto del libretto (menu Condividi su iPhone, la foto non passa da nessun server), vettura, misura e codice MCTC.
- Anteprima: `_build/anteprima-trasformazioni-nad.html`; icona: `_build/icona-trasformazioni-nad.html`.
- Sezione «Esempio di compilazione» (Allegato C / Allegato B con dati di fantasia, valori in blu e richiami numerati) e PDF `pdf/Esempio-compilazione-Allegati-B-C.pdf`: tutti e due generati da `../Locandine/trasformazioni-nad/genera_esempio.py`, che riscrive il blocco tra `<!--ESEMPIO-->` e `<!--/ESEMPIO-->` in `index.html`. Modificare l'esempio solo lì.

## anelli-centraggio (anelli di centraggio in plastica, prezzi netti cad. + IVA dal 2026-11-12)

- `dati.js` generato da `../Locandine/anelli-centraggio/genera_dati.py` (va lanciato con il venv di `mak-preventivi`): 63 anelli: i 48 della sezione «Anelli di centraggio Aftermarket» del B2B da «Anelli di Centraggio.xlsx» (codice, esterno × interno) più 15 da `anelli-72-b2b.csv` (14 da Ø 72 e il 72,6 × 63,4, sul B2B solo con la ricerca per codice; aggiunti il 2026-11-12, esclusi i «Non disponibile») e 5.282 vetture con il mozzo, ricavato dal Fitment MAK (`mak-preventivi/data/fitment.sqlite`: diametro interno dell'anello indicato, o foro ruota se l'anello non serve). Dalla pagina escono solo marca, modello, tipo e mozzo.
- Testo e foto dalla bozza Mailchimp «ANELLI CENTRAGGIO 26» (novità Ø 70,1, gamma completa), video YouTube shorts/1F4fZmop28o.
- Prezzi netti cadauno + IVA del listino SD da `../Locandine/anelli-centraggio/prezzi-netti-b2b.csv` (letti sul B2B con l'account cliente il 2026-11-12: 2,48 € gli aftermarket, 0,35–1,00 € gli anelli da 72, 0,65 e 0,80 € due da 72,6): nel risultato, nella gamma, nell'ordine con il totale e nel messaggio WhatsApp; nella locandina il prezzo o il «da» per ogni esterno. Da rileggere sul B2B quando cambia il listino.
- Foro della ruota (8 esterni; dal 2026-11-12 nei testi «ruota», mai «cerchio») → mozzo dalla vettura o dai bottoni → codice con quantità e «Aggiungi»; gamma completa per esterno con le quantità; ordine su WhatsApp con codici e pezzi. Se l'anello non c'è o non serve, la pagina lo dice e il messaggio chiede a Stefano.
- Anteprima: `_build/anteprima-anelli-centraggio.html`; icona: `_build/icona-anelli-centraggio.html`.

## Copie per i colleghi agenti (`<agente>/<campagna>/`)

> **Dal 2026-11-05 le copie per i colleghi non si fanno più.** Le locandine dei colleghi le cura Matteo Varietà sul suo GitHub, con i link alla pagina ufficiale makwheels. Le cartelle `<agente>/` qui sotto sono ferme al 2026-11-04 e `_build/agenti.py` non va lanciato, salvo richiesta esplicita di Stefano.

- `_build/agenti.py` copia ogni campagna in `<agente>/<campagna>/` con nome, numero, link `tel:` e `wa.me` dell'agente (anche «Ciao <nome>» nei messaggi WhatsApp) e rifà `locandina.jpg` con il suo nome dalla sorgente in `../Locandine/` (fix-pack e halloween-ruotino si copiano: l'immagine non ha nome né numero).
- Agenti in `AGENTI` dentro lo script: Angelo Magnotta (+39 392 450 1782) → `…/mak-promo/angelo/`, Alberto Pianta (+39 335 522 3011) → `…/mak-promo/alberto/`, Federico Gorgoglione (+39 335 638 4363) → `…/mak-promo/federico/`, Davide Mattaliano (+39 349 051 2550) → `…/mak-promo/davide/`, Oscar Padova (+39 349 071 7481) → `…/mak-promo/oscar/`, Gianluca Giamberardino (+39 339 143 6270) → `…/mak-promo/gianluca/`, Silvana Rinaldi (+39 338 680 0250) → `…/mak-promo/silvana/`, Francesco Parisi (+39 338 259 4763) → `…/mak-promo/francesco/`, Marco Mazzotti (+39 334 113 3956) → `…/mak-promo/marco/`, Marco Cesarini (+39 345 944 3886) → `…/mak-promo/marco-cesarini/`, Michele Bracchi (+39 347 540 6935) → `…/mak-promo/michele/`, Emil Colombani (+39 333 314 0092) → `…/mak-promo/emil/`, Gerardo Giacco (+39 320 223 2932) → `…/mak-promo/gerardo/`, Enrico Galante (+39 349 772 0865) → `…/mak-promo/enrico/`, Stefania Santiglia (+39 327 902 0929) → `…/mak-promo/stefania/`, Matteo Colzani (+39 393 250 5569) → `…/mak-promo/matteo/`, Elisa Rampon (+39 331 667 4100) → `…/mak-promo/elisa/`, Mauro Galante (+39 342 092 3719) → `…/mak-promo/mauro-galante/`, Marco Podda (+39 339 860 5989) → `…/mak-promo/marco-podda/`, Domenico Sorrentino (+39 389 463 2818) → `…/mak-promo/domenico/`, Francesco Di Cesare (+39 345 850 3816) → `…/mak-promo/francesco-dicesare/`, Sebastiano Fabrotti (+39 342 353 5576) → `…/mak-promo/sebastiano/`, Mauro Pallini (+39 339 878 1190) → `…/mak-promo/mauro-pallini/`, Ivan Parisi (+39 333 801 2609) → `…/mak-promo/ivan/`. Per un collega nuovo basta una riga in `AGENTI` e `python3 _build/agenti.py <chiave>`.
- Lo script non cancella le cartelle: riscrive solo i file cambiati e tiene i file temporanei della locandina fuori dalla Scrivania (su iCloud cancellare e ricreare crea doppioni « 2»). La pagina dell'agente (`<agente>/index.html`) elenca tutte le campagne con anteprima, titolo, link, «Copia link» e «Manda su WhatsApp».
- Le copie non si modificano a mano: dopo ogni cambio a una campagna, o per una campagna nuova, `python3 _build/agenti.py` e push (per rifare solo le campagne toccate: `python3 _build/agenti.py --solo=<campagna>,<campagna>`, ~1,5 minuti per tutti). Lo script si ferma se in una pagina resta il nome o il numero di Stefano.
- Frasi valide solo per Stefano (es. «il mio video») in `FRASI`.

## ts900-rinnovi (rinnovi AUTEL TS900, senza scadenza)

- Per i clienti con la TS900 in scadenza (elenco da `../scadenze-ts900/`): aggiornamento 12 mesi (7200000029, 270 €), sblocco Full SGW (7200000046, 390 €), sblocco FCA + Maserati (7200000012, 160 €), IVA esclusa, listino MATE set–dic 2026.
- `locandina.jpg` da `../Locandine/ts900-rinnovi/locandina.html`; `ts900.png` = foto ufficiale AUTEL ritagliata.
- Vademecum «Controlla la scadenza»: Supporto › Il mio account › Informazioni personali › Informazioni dispositivo (numero di serie, scadenza = «Expired time»), dal manuale MATE del TS900, con la schermata del manuale e i riquadri rossi. La scadenza SGW non è sullo strumento: la controlla Stefano dal seriale.
- `etichetta.jpg` (foto dell'etichetta sul retro, se c'è): il riquadro si nasconde da solo se manca.
- Modulo: voci con prezzo (Full SGW esclude FCA), «controllamelo tu», numero di serie con controllo delle 12 cifre, foto dell'etichetta (menu Condividi: foto + testo verso WhatsApp, nessun server), officina, totale + IVA → messaggio WhatsApp con codici.
- «Le tue scadenze» (dal 2026-10-30): il cliente scrive il numero di serie e vede aggiornamento, Full SGW e FCA con stato (scaduto / tra N giorni / attivo); le voci da rinnovare si spuntano da sole nel modulo. Dati in `scadenze.js`, generato da `../scadenze-ts900/seriali.py` (licenze DIAGMOTIVE + 24 mesi compresi dagli ordini): niente nomi né codici cliente, seriali solo come impronta SHA-256. Per aggiornarlo: nuovo export DIAGMOTIVE in `../scadenze-ts900/dati/diagmotive-licenze.xlsx`, poi `/usr/bin/python3 ../scadenze-ts900/seriali.py` e push.
- `index.html` scritto a mano. Anteprima: `_build/anteprima-ts900-rinnovi.html`; icona: `_build/icona-ts900-rinnovi.html`; prova a 390 px: `_build/prova-ts900.html`.


## cavalletto-ez-jack-45s (cavalletto ruota universale, 239,00 € + IVA, cod. 7600000CRU, senza scadenza)

- `locandina.jpg`: da `../Locandine/cavalletto-ez-jack-45s/locandina.html` (PNG/PDF clienti e colleghi nella stessa cartella).
- `index.html` scritto a mano; `dati.js` generato da `../Locandine/cavalletto-ez-jack-45s/genera_dati.py` (Fitment MAK: marca → modello, tipo, PCD, mozzo; PCD solo dalle righe senza bulloni flottanti «BV»).
- «Monta sulla vettura?»: vettura dal Fitment o PCD + mozzo a mano → verde (in tabella del costruttore e mozzo ≤ 77), giallo (dentro 98–130 ma fuori tabella, 4×135/137, più versioni), rosso (6 fori, fuori campo, mozzo > 77).
- «Regge il peso?»: massa a pieno carico (F.2) + quota dell'asse più carico (50–70%, 60% di base) → kg per ruota contro 1.587 kg.
- Ordine con pezzi e totale; il messaggio WhatsApp riporta anche vettura verificata e carico.
- Anteprima: `_build/anteprima-cavalletto-ez-jack-45s.html`; icona: `_build/icona-cavalletto-ez-jack-45s.html`; prova a 390 px: `_build/prova-cavalletto.html`.

## assistenza-mate (assistenza telefonica gratuita per i clienti con strumenti MATE e Autel, senza prezzi)

- Servizio Clienti MATE **392 098 1064**, dal lunedì al venerdì in orario d'ufficio, support@mate-tech.it (scelta di Stefano del 2026-11-03; il cellulare di Pepe non va pubblicato).
- **Chiama e WhatsApp vanno all'assistenza, non all'agente** («non facciamo assistenza»): `tel:+393920981064` e `wa.me/393920981064`. Nelle copie dei colleghi il numero resta quello; cambiano solo la firma e la riga «Il mio agente MAK» del messaggio.
- «La procedura della tua auto»: marca → modello → tipi di procedura e link all'app Apprendimento TPMS (`…/mak-tpms-relearn/#/<marca>/<modello>`) e alla scheda MATE in PDF. Dati in `marche.js`, generato da `_build/assistenza-mate-dati.py` da `../mak-tpms-relearn/data/brands.json`: rilanciarlo quando cambia l'app.
- «Prepara la richiesta»: strumento, di cosa hai bisogno, officina (il seriale non serve, tolto il 2026-11-03) → messaggio WhatsApp all'assistenza con anche la vettura e l'agente.
- Locandina: `../Locandine/assistenza-mate/locandina.html` (foto vera MA41 + TS508 da `Video Avatar/Immagini/MATE/`). Anteprima: `_build/anteprima-assistenza-mate.html`; icona: `_build/icona-assistenza-mate.html`.

## Vocali «Spiegamelo a voce»

- Bottone uguale su ogni pagina (stile e script copiati da `multisens-plus`), con `vocale.mp3` (o `vocale.m4a` su multisens-plus) e il testo in «Leggi il testo». Dal 2026-11-11 gli audio si generano con la voce clonata di Stefano su HeyGen («Stefano Voice»), testi in `../Locandine/testi-vocali.md`.
- Ce l'hanno: multisens-plus, calze-neve, assistenza-mate, bulloneria-auto («Spiegami come»), ts900-rinnovi, trasformazioni-nad, riempicarrello, kit-gomma-ruota (anche nel template), fix-pack, distanziali-xilema, canali-etrto, anelli-centraggio; dal 2026-11-12 anche adblue, calze-light-espositore, cap-originali, refill-autel-mx, refill-multisens, tergi-cora, tergi-cora-sciolte, tpms-tesla, consumo-officina-cora.
- Su calze-light-espositore e tergi-cora c'è un elemento `id="conta"` (contatore delle paia): il bottone controlla `typeof window.conta === "function"`, altrimenti senza `conta.js` darebbe errore.

## Monitoraggio (dal 2026-11-03)

- Ogni pagina include `conta.js` (`<script src="/mak-promo/conta.js" defer></script>` prima di `</body>`) e la riga «Conteggio anonimo delle visite, senza cookie.» nel footer. Le copie dei colleghi lo ereditano; la pagina elenco del collega lo include con `data-elenco`.
- Conta aperture e tocchi su WhatsApp, Chiama, B2B e mail. Le ricerche arrivano dal blocco «ricerche per il contatore anonimo» in fondo alle pagine che ne hanno una: calze-neve, calze-light-espositore, canali-etrto, anelli-centraggio, distanziali-xilema, halloween-ruotino, kit-gomma-ruota, cavalletto-ez-jack-45s, assistenza-mate.
- Il server è il Worker in `../mak-promo-conta/` (README con cosa si salva e cosa no). I numeri si leggono nel briefing del lunedì.
- Campagna nuova: script e riga nel footer, più l'aggancio della ricerca se c'è. `_build/agenti.py` si ferma se manca `conta.js`.

## multisens-plus (promo lancio MATE MULTIsens+, 9–22 novembre 2026)

- Fonte: email di Salvatore Pepe del 2026-11-04 «Arriva MATE MULTIsens+ e PROMO LANCIO 9–22 novembre» (Mail Mak 2026, id 106944) + presentazione PDF allegata (`../Locandine/multisens-plus/presentazione-mate-multisens-plus.pdf`).
- 14,00 € + IVA a sensore, minimo 40 pezzi (560,00 € + IVA, spedizione inclusa); Rubber, Metal Silver e Metal Black miscelabili a multipli di 10. Sul B2B dal 9/11, sezione Promozioni.
- Conto alla rovescia: prima del 9/11 conta alla partenza («lo inserisci appena parte»), poi alla fine del 22/11; dopo diventa «Chiedimi le offerte attive».
- Ordine a passi di 10 per versione, barra verso i 40, mix rapidi; messaggio WhatsApp con le versioni (i codici articolo non sono ancora stati comunicati).
- Dal 2026-11-04 (richiesta di Stefano) la pagina mostra il **volantino ufficiale MAK/MATE** (`../Locandine/multisens-plus/volantino-mate-multisens-plus.png` → `locandina.jpg`, copiato com'è anche nelle copie dei colleghi: `SORGENTE_LOCANDINA` = None). Le foto di Rubber, Metal Silver e Metal Black (`ms-*.png`) sono ritagliate dal volantino. MA41 e VT57 dalla presentazione. Sezione «Prima aggiorna l'ATEQ» e link all'assistenza MATE.
- Anteprima: `_build/anteprima-multisens-plus.html`; icona: `_build/icona-multisens-plus.html`.

## cap-originali (cap originali e cap neutro da 60 mm, senza prezzi)

- `dati.js` generato da `../Locandine/cap-originali/genera_dati.py` (dopo averlo rigenerato, ricopiarlo qui insieme a `foto/`). Fonti: «Codici Cap Originali.xlsx» di Stefano (`../Fitment List/`, 51 cap con la sede del cap MAK tra parentesi) + 8010008133 Fiat 51884863 dal PDF «cap OE per BSF Italy» dell'eBook; cap di serie di ogni codice ruota da `../NotebookLM/ETRTO/makart.csv` (dic 2024), poi dal file «RUOTE MAK - DATI TECNICI» dell'eBook per i codici fuori produzione, poi da `../Sito Mak/ricambi/ricambi.csv` per i modelli solo sul sito; vetture dalla Fitment più recente. Le funzioni di lettura stanno in `../Fitment List/estrazioni/cap_originali.py`. Prezzi e giacenze non escono mai (lo script lo controlla).
- `foto/<codice>.jpg`: foto vere dal B2B (`https://b2bshop.makwheels.it/SysInf/MAK/Prodotti/<codice>.jpg`), scaricate con `../Locandine/cap-originali/scarica_foto.py` e portate a 400 px.
- Tre ricerche: modello ruota → misura · PCD · foro; codice articolo (anche senza F, in minuscolo o incompleto: elenco di 10 codici); marca → modello dell'auto (cap originali della marca e ruote MAK omologate che li montano).
- Regola del cap neutro **8010002525** (CAP C001 MM60 CONVEX, grigio senza logo, decisa da Stefano il 2026-11-06): si propone quando nessun cap originale entra nella sede e il nome del cap di serie dice 60 mm (`MM60`, `60MM`, `CAP 60`).
- Richiesta a righe (pezzi predefiniti 4, 1 per gli emblemi) + officina → messaggio WhatsApp che chiede prezzo e disponibilità.
- Locandina: `../Locandine/cap-originali/locandina.html` (PNG e PDF nella stessa cartella). Anteprima: `_build/anteprima-cap-originali.html`; icona: `_build/icona-cap-originali.html` (cap neutro, nessun marchio d'auto).

## copriruota (kit da 4, prezzi netti + IVA)

- `prodotti.js`: 10 copriruota del B2B (sezione Copriruota, letta il 2026-11-06), prezzi dagli ordini 2025-26; `prezzo: null` = su richiesta (FARAD 233 17"). LAMPA Spark 14" escluso perché non disponibile.
- `foto/<codice>.jpg`: foto vere dal B2B, una per modello e colore (le misure dello stesso modello hanno la stessa foto).
- Bottoni delle misure che filtrano le schede (la misura va al contatore come ricerca), quantità in kit, totale, officina → WhatsApp.
- Locandina: `../Locandine/copriruota/locandina.html` (PNG e PDF nella stessa cartella). Anteprima: `_build/anteprima-copriruota.html`; icona: `_build/icona-copriruota.html`.

## accesso-b2b (primo accesso al B2B per i clienti nuovi, senza prezzi)

- Percorso vero da telefono: makwheels.it (banner cookie) → tre lineette in alto a destra → «Area rivenditori B2B» → banner cookie del B2B → Username e Password → password nuova al primo accesso (dato da Stefano, schermata non disponibile).
- `schermate/*.png` e `schermate/punti.json` (posizione in % dei punti da toccare) si rifanno con `../Locandine/accesso-b2b/schermate.py` (venv di `mak_quote_automation`) quando MAK cambia il sito; poi si aggiornano le percentuali dei cerchi in `index.html` e nella locandina. Lo script non scrive mai nei campi di accesso.
- Codice utente d'esempio **inventato**: `cl012345.xx` (tutto minuscolo, seconda lettera elle). Il campo «Prova a scriverlo qui» controlla la forma solo nel browser: il valore non va né a `conta.js` né su WhatsApp.
- «Non riesci a entrare?»: il messaggio WhatsApp contiene solo il passo e l'officina, mai codice o password. Il passo scelto va al contatore come ricerca («passo N»).
- Locandina: `../Locandine/accesso-b2b/locandina.html` (PNG e PDF nella stessa cartella). Anteprima: `_build/anteprima-accesso-b2b.html`; icona: `_build/icona-accesso-b2b.html` (tre lineette).

## bulloneria-auto (bulloneria originale e kit di montaggio per auto, prezzi netti SD + IVA)

- Marca → modello → anno (menu nativi) e due sezioni: **bulloneria originale** (sezione B2B «search-kitoe») e **kit di montaggio** aftermarket («search-kitm»), raggruppati per tipo con la riga «quando serve» e il PCD della ruota.
- `marche.json` (indice: marche, modelli, anni con tipo) e `dati/<codice marca>.json` (vetture → codici, articoli con descrizione, prezzo, foto, componenti), caricato solo quando si sceglie la marca. `foto/<codice>.jpg`: foto vere del B2B con lo sfondo ritagliato; le foto generiche (stessa foto su più di 3 codici) sono scartate.
- **I dati si rifanno da `../Locandine/bulloneria-auto/`** (README lì): `scarica_b2b.py` con l'account CLIENTE della webapp preventivi (listino SD, mai l'account da agente), `scarica_foto.py`, `genera_dati.py`. Poi commit e push di questa cartella.
- Quantità → riepilogo → WhatsApp con vettura, codici e quantità; la vettura scelta va al contatore come ricerca. Le quantità si azzerano quando cambia l'auto.
- **Cerca per misura** (dal 2026-11-11): dado o bullone → diametro × passo → chiave (o «a stella») → lunghezza per i bulloni; mostra tutti i kit che contengono quella misura, originali e aftermarket, con le marche abbinate sul portale. Dati in `misure.json` (caricato al primo uso). Gli articoli presi per misura restano nell'ordine anche cambiando ricerca o auto e nel WhatsApp sono segnati «cercato per misura»; la ricerca va al contatore («misura dado M14 × 1,5 CH21»).
- Bottone **«Spiegami come»** (dal 2026-11-11): `vocale.mp3`, 54 s, generato con la voce clonata di Stefano su HeyGen («Stefano Voice»), stesso bottone di multisens-plus con «Leggi il testo»; avvio e ascolto completo vanno al contatore.
- Locandina: `../Locandine/bulloneria-auto/locandina.html` (PNG e PDF nella stessa cartella). Anteprima: `_build/anteprima-bulloneria-auto.html`; icona: `_build/icona-bulloneria-auto.html`.

## tpms-tesla (sensori TPMS HUF Bluetooth per Tesla, 40,00 € cad. + IVA, senza scadenza)

- `locandina.jpg`: da `../Locandine/tpms-tesla/locandina.html` (PNG e PDF nella stessa cartella). Solo gli HUF (scelta di Stefano del 2026-11-12): 930HUFBLEM Metal Silver e 930HUFBLEB Metal Black a 40,00 €, prezzo del listino MATE B2B set-dic 2026. L'AUTEL Tesla BLE (45,00 €) non c'è.
- `index.html` scritto a mano: controllo «la tua Tesla ha il Bluetooth?» (modello con radio + label, periodo con select) dalla coverage list MATE di luglio 2026: Model 3 da 11/2020, Model Y dal 2020, Model S dal 2022, Model X da 10/2021; le altre → MULTIsens MP6 con link a `../refill-multisens/`. La scelta va al contatore come ricerca ed entra nel messaggio WhatsApp come «Vettura».
- Ordine: due righe con i pezzi, bottoni «4 Silver», «4 Black», «Azzera», totale a 40,00 €, officina. Poi «Come si montano» (relearn TESLA01: ferma 15 minuti, poi sopra i 32 km/h fino a 20 minuti) e i dati tecnici del sito MATE (Bluetooth 2,4 GHz: il sito scrive 433 MHz per errore).
- Foto: ufficiali del B2B (`SysInf/MAK/Prodotti/<codice>.jpg`, pubbliche), scontornate con `../Locandine/refill-multisens/scontorna.py`.
- Anteprima: `_build/anteprima-tpms-tesla.html`; icona: `_build/icona-tpms-tesla.html`.
- Bottone «Spiegamelo a voce» (dal 2026-11-12): `vocale.mp3`, 21 s, voce clonata di Stefano su HeyGen; rifatto lo stesso giorno con «tipiemmesse» attaccato, punti esclamativi ed espressività al massimo, poi montato con ffmpeg: «Ciao» −5 dB, pausa di 0,3 s dopo «l'anno», accelerato del 4% (atempo 1.039); 22 s.

## spese-trasporto (spese di trasporto zona Nord, regole B2B da ottobre 2026, senza scadenza)

- Fonte: banner «Spese di spedizione Italia» della home B2B (`SPESEDISPEDIZIONE_202610`, letto il 2026-11-12, copia in `../Locandine/spese-trasporto/`). Solo zona Nord: è quella di tutti i clienti di Stefano. Fasce IVA esclusa: fino a 199,99 € → 12 €; 200–549,99 € → 10 €; da 550 € gratis; calze e ruotini sotto le soglie 8 €; bancale + 7 € (non ruote truck).
- Calcolatore: totale dell'ordine (accetta «1.234,50») o bottoni 150/350/500/600, «Ordine normale» o «Solo calze o ruotini» → contributo, barra fino a 550 € con la tacca a 200, quanto manca alla fascia dopo e quanto si risparmia, link a `../riempicarrello/`. Le fasce sono nella costante `FASCE` dentro la pagina: se MAK cambia le regole si cambiano lì e nella locandina.
- Calze e ruotini: interpretato come ordine di sole calze o ruotini sotto 550 € → 8 €; un ordine misto lo conferma Stefano.
- WhatsApp: con un importo sotto 550 € il bottone diventa «Aiutami ad arrivare a 550 €» con importo e contributo nel messaggio. Al contatore va solo la fascia, mai l'importo.
- Anteprima: `_build/anteprima-spese-trasporto.html`; icona: `_build/icona-spese-trasporto.html`. Niente vocale per ora.

## bulloni-antifurto (kit bulloni antifurto NPK by Farad, 14,90 € + IVA, espositore con 10 kit, senza scadenza)

- Ricerca marca → modello → anno (menu nativi) sui dati della sezione B2B «Bulloneria Antifurto NPK by Farad» (`dati.js`, 2.045 vetture, 23 codici): scheda del kit con foto, filetto e lunghezza in parole, sede, chiave, scelta Cromato/Black (radio + label) quando ci sono le due finiture, netto + IVA e prezzo al pubblico IVA inclusa del listino NPK di ottobre 2026.
- **I dati si rifanno da `../Locandine/bulloni-antifurto/`** (README lì): `scarica_b2b.py` con l'account CLIENTE, poi `genera_dati.py`, poi alzare `dati.js?v=`.
- Avvisi: riquadro giallo sulle Mercedes con kit conico (le originali sono sferiche R14), nota verde sul kit M15 sferico R14 delle GLE/GLS tipo 167, «va su ruote con sede conica 60°» sugli altri, nota «abbinamento dal sito NPK, te lo confermo io» sulle 5 vetture che il B2B non ha.
- Gamma completa divisa bulloni/dadi, ordine con quantità e totale, barra «ti mancano N kit» fino all'espositore da banco in omaggio a 10 kit anche diversi (`SOGLIA_ESP`). WhatsApp con codici, quantità, totale, espositore, vettura, nota Mercedes e officina. La vettura va al contatore come ricerca.
- Obiezioni tolte dalla pagina (scelta di Stefano del 2026-11-13); «Perché proporli» con 4 punti.
- `foto/<codice>.jpg`: foto pubbliche del B2B (8050009180/185 non hanno foto e non sono nella sezione). `espositore.png` dal catalogo NPK 09-2026.
- Locandina: `../Locandine/bulloni-antifurto/locandina.html`. Anteprima: `_build/anteprima-bulloni-antifurto.html`; icona: `_build/icona-bulloni-antifurto.html`. Bottone «Spiegamelo a voce» (dal 2026-11-13): `vocale.mp3`, 24 s, voce clonata di Stefano su HeyGen; testo in `../Locandine/testi-vocali.md`.

## diagnosi-autel (quale tablet di diagnosi AUTEL, dalla TS900 alla MS Ultra S2, senza scadenza)

- **Revisione del 2026-11-13 con Salvatore Pepe (MATE)**: tolta la MS 919 S2 (mai venduta, uscirà dal B2B), gamma prima dei pacchetti, Haynes PRO solo Electronic + Tech, sulla locandina «Sblocco gateway SGW: 12 mesi da includere» al posto di «Renault illimitato». Pepe ha dato l'ok al suo numero in pagina.

- Test a 4 domande (radio/checkbox + label): lavoro, usi (anche più di uno), quante marche, diagnosi attuale. Il consiglio si aggiorna a ogni risposta: un solo modello con «Perché te lo consiglio», cosa fa, prezzo B2B + IVA, più «Se ti basta meno» / «Se vuoi di più» (assenti ai due estremi). Regole in chiaro nella tabella `REGOLE` in cima allo script: gradino più alto tra lavoro (gommista TS900, officina ed elettrauto MS 906 MAX, concessionaria MS 908S PRO3) e usi (codifiche → 908S PRO3, ADAS ed elettriche → 909 S2, test dei componenti e «il massimo» → Ultra S2).
- 5 modelli (niente MS 906 PRO 2 TS, MS 909 EV e MS 919 S2, niente strumenti TPMS): gamma con «Scegli questo», «Tutte le caratteristiche» a scomparsa e scheda PDF `pdf/scheda-<modello>.pdf`; link a manuale TS900, catalogo MATE 2026 (pagine 12–17) e schede del sito MATE.
- **I dati dei modelli non si toccano qui**: blocco `/*DATI*/` scritto da `../Locandine/diagnosi-autel/genera_schede.py` (unica fonte per pagina e PDF; si ferma se un prezzo non coincide con `prezzi-b2b.csv`). Prezzi dal B2B con `leggi_prezzi_b2b.py` (account CLIENTE, sola lettura). README lì.
- Servizi da aggiungere: Full SGW (toglie FCA), FCA + Maserati, assistenza AUTEL, Haynes PRO Electronic + Tech; totale indicativo + IVA. WhatsApp «Chiedimi l'offerta» con risposte, modello consigliato, eventuale modello scelto, servizi, totale e officina: chiede offerta o prova, non è un ordine.
- Bottone **«Info tecniche: scrivi a Salvatore Pepe»** (`wa.me/393270888678`, numero pubblicato su richiesta esplicita di Stefano del 2026-11-13) nel risultato e in ogni scheda, con il modello nel testo.
- Contatore: il modello consigliato come ricerca, «scelto <modello>» quando il cliente sceglie un altro modello, «Pepe <modello>» sul bottone di Pepe (il Worker accetta solo i suoi 6 tipi; lo stesso tocco conta anche come «whatsapp» senza righe d'ordine).
- Rimandi a `../ts900-rinnovi/` (anche nel risultato se «ho già la TS900») e `../assistenza-mate/`.
- Foto: B2B `SysInf/MAK/Prodotti/<codice>.jpg` ritagliate ai bordi (`foto/<modello>.jpg`, 480 px).
- Locandina: `../Locandine/diagnosi-autel/locandina.html`. Anteprima: `_build/anteprima-diagnosi-autel.html`; icona: `_build/icona-diagnosi-autel.html`. Bottone «Spiegamelo a voce» (dal 2026-11-14): `vocale.mp3`, 27 s, voce clonata di Stefano su HeyGen; testo in `../Locandine/testi-vocali.md`.

## tool8-ma41 (Tool 8: strumento MATE MA41 + 8 sensori MULTIsens, 280 € + IVA, senza scadenza)

- **Revisione di Stefano del 2026-11-14**: solo il totale di 280 € (niente prezzi separati, niente risparmio), cavo OBD compreso nel pacchetto, video tutorial con anteprima (https://youtu.be/Hncp8_1w31w, canale di Salvatore Pepe; miniatura `video-tutorial.jpg`, il tocco va al contatore come «video tutorial»), niente Tesla.
- Fonte: portale B2B, Promozioni › Promozioni Tool › MATE MULTIsens › Tool 8 (letto il 2026-11-14 con l'account cliente, carrello invariato): MA41 a 160 € (listino 200) + 8 MULTIsens a 15,00 € (listino 20,40) = 280 € invece di 363,20 € (−83,20 €, −23%). Sul B2B ci sono anche Tool 16/30 e le versioni HUF ECS e AUTEL: per scelta di Stefano solo il Tool 8 MULTIsens.
- Pagina: prezzo unico 280 € tutto compreso, 6 vantaggi (tutto in un prezzo, cavo OBD compreso, valvole miste, copertura 94%, 5 anni di aggiornamenti, assistenza MATE), «Cosa c'è dentro» senza prezzi separati, video tutorial, scelta delle valvole degli 8 sensori (+ si blocca a 8, mix rapidi), «Da sapere» (60–80 vetture a carica, aggiornamento da PC), rimandi a refill-multisens e assistenza-mate.
- WhatsApp con MA41 e righe dei sensori per codice (le valvole non scelte: «decidiamo insieme»), totale 280 € + IVA e officina. Al contatore il mix di valvole quando arriva a 8.
- Foto: MA41 e sensori MP6 scontornati della campagna refill-multisens. Locandina: `../Locandine/tool8-ma41/locandina.html`. Anteprima: `_build/anteprima-tool8-ma41.html`; icona: `_build/icona-tool8-ma41.html`. Bottone «Spiegamelo a voce» (dal 2026-11-14): `vocale.mp3`, 29 s, voce clonata HeyGen; testo in `../Locandine/testi-vocali.md`. Vantaggio «Assistenza telefonica gratuita» confermato da Stefano.

## autel-tool12 (Autel Tool 12: strumento AUTEL TS508 + 12 sensori AUTEL MX, 320 € + IVA, senza scadenza)

- Gemella di tool8-ma41, con le stesse scelte di Stefano: solo il totale di 320 € tutto compreso, niente prezzi separati, niente Tesla, video tutorial con anteprima (https://youtu.be/u7vXaYhk6bs «Autel TPMS TS508 — Tutorial», canale di Salvatore Pepe; `video-tutorial.jpg`).
- Fonte: B2B › Promozioni › Promozioni Tool › Autel › Tool 12 (letto il 2026-11-14, account cliente, carrello invariato): TS508 (`9300000309`) + 12 sensori universali, valvole a scelta. **Cavo OBD compreso** (confermato da Stefano il 2026-11-14).
- Vantaggi: tutto in un prezzo, **aggiornamenti gratuiti per sempre** (richiesta di Stefano), valvole miste, copertura MX dichiarata 96%, TS508 che riconosce TPMS diretto/indiretto, assistenza telefonica gratuita. Scelta delle valvole dei 12 sensori AUTEL MX (93000000MXG / 9300000MXB / 93000000MX) con blocco a 12; WhatsApp con codici e pezzi. Rimandi a refill-autel-mx e assistenza-mate.
- Foto: TS508 e sensori MX scontornati della campagna refill-autel-mx. Locandina: `../Locandine/autel-tool12/locandina.html`. Anteprima: `_build/anteprima-autel-tool12.html`; icona: `_build/icona-autel-tool12.html`. Nessun vocale per ora.
