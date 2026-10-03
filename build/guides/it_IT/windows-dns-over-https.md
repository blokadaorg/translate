---
title: Blocca gli annunci su Windows con DNS over HTTPS
description: Utilizza il DNS crittografato integrato in Windows 11 con Blokada Cloud per bloccare annunci e tracker in ogni app e browser, senza dover installare altri software.
updated: 02/10/2026
order: 8
---

Windows 11 può inviare tutte le sue richieste DNS in modo crittografato, tramite DNS over HTTPS. Impostalo su Blokada Cloud e annunci e tracker verranno bloccati in ogni app e browser del computer, senza nulla da installare.

Hai bisogno dell'indirizzo IP del server DNS e del tuo link DoH, entrambi presenti nella sezione _I tuoi dettagli_ qui sopra.

## Windows 11

1. Apri _Impostazioni → Rete e Internet_, poi _Wi-Fi_ o _Ethernet_, a seconda di come il computer è connesso.
2. Apri le _Proprietà hardware_ della tua connessione. Per il Wi-Fi, seleziona _Gestisci reti conosciute_ e poi la rete, oppure _Proprietà hardware_ in alto nella pagina Wi-Fi.
3. Accanto a _Assegnazione server DNS_, seleziona _Modifica_. Scegli _Manuale_ e attiva _IPv4_.
4. In _DNS preferito_, inserisci il server DNS {% ip "doh" %}
5. Imposta _DNS over HTTPS_ su _Attivo (modello manuale)_ e incolla il tuo link DoH {% doh %} come _modello DoH_.
6. Disattiva _Ripristino a testo normale_ e seleziona _Salva_.

Se il computer utilizza sia Wi-Fi che Ethernet, ripeti questa procedura anche per l'altra connessione.

<div class="note important">

Lascia vuoto il campo _DNS alternativo_. Windows utilizza entrambi i server e qualsiasi altro consentirebbe il passaggio di annunci.

</div>

<div class="note tip">

Nessuna opzione _Attivo (modello manuale)_? La tua versione di Windows 11 è vecchia. Aggiorna Windows o, nel frattempo, utilizza la [guida per browser](../browser-dns-over-https/).

</div>

## Windows 10

Windows 10 non ha un sistema di DNS crittografati integrato. Configura il DNS sicuro nel tuo browser, come indicato nella [guida per browser](../browser-dns-over-https/), oppure configura il tuo [router](../router-ad-blocking/) per proteggere tutta la casa.

## Verifica che funzioni

Apri alcuni siti web e poi guarda la pagina _Attività_ nella [dashboard](https://app.blokada.org/stats?src=guides). Le richieste di questo computer saranno visibili lì.

<div class="note aside">

Vuoi anche una VPN su questo computer? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) include una configurazione WireGuard che cripta tutto il traffico, offrendo lo stesso blocco.

</div>

## Se qualcosa non va

Chrome ed Edge dispongono di una propria impostazione _DNS sicuro_, che bypassa Windows. Se lasciata su automatico, può tornare al DNS non crittografato, cosa che Blokada non accetta. Imposta invece il tuo link DoH:

- **Chrome:** apri `chrome://settings/security`, attiva _Usa DNS sicuro_ e sotto _Seleziona provider DNS_ scegli _Aggiungi provider di servizi DNS personalizzato_.
- **Edge:** apri `edge://settings/privacy`, attiva DNS sicuro e scegli _Scegli un provider di servizi_.

Poi incolla il tuo link DoH {% doh %}

Se alcuni annunci riescono ancora a passare su una rete con IPv6, Windows potrebbe anche richiedere il server DNS IPv6 del tuo router. Disattiva _Internet Protocol Version 6 (TCP/IPv6)_ nelle proprietà dell'adattatore (_Pannello di controllo → Connessioni di rete_), oppure configura il tuo [router](../router-ad-blocking/).
