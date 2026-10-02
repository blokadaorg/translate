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
- **Un solo pannello di controllo.** Liste di blocco, domini consentiti e bloccati, e attività per dispositivo, su [app.blokada.org](https://app.blokada.org/?src=guides).

Ci sono due modi per passare. Sostituisci completamente il Pi-hole, oppure tienilo e utilizza Blokada Cloud come upstream.

## Opzione 1: sostituisci il Pi-hole

1. **Ottieni Blokada Cloud** e apri il pannello di controllo. Il tuo nome DNS e il link DoH si trovano sotto _Configurazione_ lì, e sotto _I tuoi dettagli_ sopra.
2. **Imposta il tuo router su Blokada invece del Pi-hole.** Segui la [guida per il router](../router-ad-blocking/). Se il tuo router accetta solo un indirizzo IP semplice come server DNS, configura i tuoi dispositivi uno per uno invece: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [browser](../browser-dns-over-https/).
3. **Se il tuo Pi-hole era il server DHCP,** riattiva il DHCP nel tuo router _prima_ di spegnere il Pi. Altrimenti i tuoi dispositivi smetteranno di ricevere indirizzi di rete.
4. **Trasferisci le tue liste.** Nel pannello di controllo, scegli blocklists sotto _Blocklists_ e aggiungi i tuoi domini consentiti o bloccati sotto _Eccezioni_.
5. **Spegni il Pi-hole,** oppure tienilo per altri scopi.

<div class="note aside">

Il tuo Pi-hole mostrava ogni dispositivo della rete tramite il suo indirizzo IP. Con Blokada ogni dispositivo appare con il proprio nome, purché utilizzi il proprio nome DNS di Blokada. Un router configurato con un nome DNS di Blokada apparirà come un solo dispositivo.

</div>

## Opzione 2: mantieni il Pi-hole, usa Blokada Cloud come upstream

Se vuoi mantenere la tua configurazione locale, come nomi host locali, DHCP o le tue liste personali, lascia che il Pi-hole inoltri le proprie richieste a Blokada tramite una connessione criptata. Il Pi-hole non può effettuare inoltri criptati direttamente, quindi un piccolo forwarder viene eseguito a fianco. Questa guida utilizza [dnsproxy](https://github.com/AdguardTeam/dnsproxy), un forwarder open source che consiste in un unico file.

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
5. Controlla la pagina _Attività_ sul pannello di controllo. Le richieste dalla tua rete appaiono ora lì.

Puoi disattivare le blocklists proprie del Pi-hole e gestire il blocco dal pannello di controllo, oppure mantenere entrambe.

## Domande frequenti

**Ho bisogno di Blokada Plus?** No. Blokada Cloud gestisce il blocco DNS per tutta la tua casa. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) aggiunge una VPN in più.

**Cosa succede se Blokada non è raggiungibile?** I tuoi dispositivi non potranno risolvere i nomi fino al ripristino, proprio come quando un Pi-hole si spegne. Non aggiungere un secondo server DNS non filtrato come fallback. La maggior parte dei dispositivi utilizza tutti i server a caso, quindi gli annunci riuscirebbero a passare.
