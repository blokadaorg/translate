---
title: Un'alternativa a Pi-hole che non richiede hardware
description: Trasferisci il blocco della pubblicità di casa tua da un Pi-hole a Blokada Cloud, oppure mantieni il tuo Pi-hole e invia le sue richieste attraverso Blokada.
updated: 02/10/2026
order: 1
---

Un Pi-hole blocca le pubblicità su ogni dispositivo nella tua rete, purché il Raspberry Pi sia acceso, aggiornato e a casa. Blokada Cloud svolge lo stesso compito dai nostri server:

- **Nessun box da mantenere.** Nessuna scheda SD, nessun aggiornamento, nessuna interruzione quando il Pi si spegne.
- **Funziona anche fuori casa.** Telefoni e laptop mantengono il blocco anche con dati mobili e altre reti Wi-Fi.
- **Criptato.** I dispositivi comunicano con Blokada tramite DNS over TLS o DNS over HTTPS, quindi il tuo provider non può leggere o modificare le tue richieste.
- **Un'unica dashboard.** Liste di blocco, domini consentiti e bloccati, e attività per dispositivo, su [app.blokada.org](https://app.blokada.org/?src=guides).

Ci sono due modi per cambiare. Sostituisci completamente il Pi-hole, oppure tienilo e utilizza Blokada Cloud come upstream.

## Opzione 1: sostituisci il Pi-hole

1. **Ottieni Blokada Cloud** e apri il dashboard. Il tuo nome DNS e il link DoH si trovano sotto _Configurazione_ lì, e sotto _I tuoi dettagli_ sopra.
2. **Configura il tuo router su Blokada invece che sul Pi-hole.** Segui la [guida per il router](../router-ad-blocking/). Se il tuo router accetta solo un indirizzo IP semplice come server DNS, configura i dispositivi singolarmente: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [browser](../browser-dns-over-https/).
3. **Se il tuo Pi-hole era il server DHCP,** riattiva il DHCP nel tuo router _prima_ di spegnere il Pi. Altrimenti i tuoi dispositivi smetteranno di ottenere indirizzi di rete.
4. **Trasferisci le tue liste.** Nel pannello di controllo, scegli blocklists sotto _Blocklists_ e aggiungi i tuoi domini consentiti o bloccati sotto _Eccezioni_.
5. **Spegni il Pi-hole,** oppure tienilo per altri scopi.

<div class="note aside">

Il tuo Pi-hole mostrava ogni dispositivo nella rete tramite l'indirizzo IP. Con Blokada ogni dispositivo viene visualizzato con il proprio nome, a condizione che utilizzi il proprio nome DNS Blokada. Un router configurato con un solo nome DNS Blokada viene visualizzato come un solo dispositivo.

</div>

## Opzione 2: mantieni il Pi-hole, usa Blokada Cloud come upstream

Se vuoi mantenere la tua configurazione locale, come i nomi host locali, il DHCP o le tue liste personali, lascia che il Pi-hole inoltri le richieste a Blokada tramite una connessione criptata. Pi-hole non può inoltrare criptato da solo, quindi accanto ad esso viene eseguito un piccolo forwarder. Questa guida utilizza [dnsproxy](https://github.com/AdguardTeam/dnsproxy), un forwarder open source contenuto in un singolo file.

1. Sulla macchina Pi-hole, scarica la release di `dnsproxy` per la tua CPU (`linux-arm64` per un Raspberry Pi recente) dalla sua pagina delle release, e copia il binario `dnsproxy` in `/usr/local/bin/`.
2. Crea `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Encrypted DNS forwarder to Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Avvialo: `sudo systemctl enable --now dnsproxy`
4. Nell'admin di Pi-hole, apri _Impostazioni → DNS_. Deseleziona tutti i server upstream e aggiungi `127.0.0.1#5054` come server upstream personalizzato. Salva.
5. Verifica la pagina _Attività_ del dashboard. Le richieste dalla tua rete ora appaiono lì.

Puoi disattivare le blocklists proprie del Pi-hole e gestire il blocco dal pannello di controllo, oppure mantenere entrambe.

## Domande frequenti

**Ho bisogno di Blokada Plus?** No. Blokada Cloud fornisce il blocco DNS per tutta la tua casa. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) aggiunge una VPN in più.

**E se Blokada non fosse raggiungibile?** I tuoi dispositivi non potranno risolvere i nomi finché non tornerà disponibile, proprio come accade quando un Pi-hole va giù. Non aggiungere un secondo server DNS non filtrato come backup. La maggior parte dei dispositivi usa tutti i server disponibili in modo casuale, quindi le pubblicità passerebbero.
