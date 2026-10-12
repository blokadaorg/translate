---
title: Blocca le pubblicità su tutta la tua rete con il blocco degli annunci dal router.
description: Configura Blokada Cloud una sola volta sul tuo router e tutti i dispositivi di casa saranno protetti, inclusi TV, console di gioco e altoparlanti intelligenti che non possono eseguire un'app blocca pubblicità.
updated: 09/10/2026
order: 4
---

Ogni dispositivo nella tua rete chiede al router quale server DNS utilizzare. Punta il router su Blokada Cloud e pubblicità e tracker saranno bloccati per tutto ciò che si trova dietro di esso. Questo include smart TV, console di gioco, stick per lo streaming e dispositivi smart home, che non hanno spazio per un'app blocca-pubblicità.

## Cosa serve al tuo router

Ci sono due modi per configurare un router:

- **DNS crittografato con un nome host**, ovvero DNS over TLS (DoT) o DNS over HTTPS (DoH). Molti router recenti lo supportano, inclusi i modelli indicati qui sotto. A seconda di ciò che supporta il tuo router, ti servirà il nome DNS o il link DoH, entrambi disponibili in _I tuoi dettagli_ sopra.
- **Un indirizzo DNS IPv6 semplice.** Molti router dei provider Internet accettano solo indirizzi IP semplici per il DNS. Se il tuo è così e la tua connessione dispone di IPv6, Blokada ti fornisce un indirizzo IPv6 da inserire. Vedi [Router che accettano solo un indirizzo IP](#routers-that-only-take-an-ip-address).

Usa DNS crittografato se il tuo router lo supporta. Le risoluzioni rimarranno private durante il passaggio verso Blokada.

## FRITZ!Box

FRITZ!OS 7.20 o successivo.

1. Apri `http://fritz.box` e vai su _Internet → Informazioni account → Server DNS_.
2. Sotto _Risoluzione dei nomi crittografata su Internet (DNS over TLS)_, seleziona _Usa la risoluzione dei nomi crittografata_.
3. In _Nomi risolti del server DNS_, inserisci solo {% dot %}. **Rimuovi ogni altra voce.** Il FRITZ!Box usa tutti i resolver inseriti, e qualsiasi altro permette alle pubblicità di passare.
4. Seleziona l'opzione che impone la verifica del certificato e deseleziona quella che permette il fallback alla risoluzione dei nomi non criptata.
5. Se vedi _Failover verso server DNS pubblici quando il DNS è interrotto_, disattivalo.
6. Fai clic su _Applica_.

## ASUS

Firmware ASUS recente (3.0.0.4.388 o successivo) e Asuswrt-Merlin.

1. Accedi alla pagina di amministrazione del router e vai su _WAN → Connessione Internet_.
2. Sotto _Impostazioni DNS WAN_, imposta _Protocollo di privacy DNS_ su _DNS-over-TLS (DoT)_ e _Profili DNS-over-TLS_ su _Strict_.
3. Rimuovi tutte le voci da _Elenco server DNS-over-TLS_, poi aggiungine una:
   - Indirizzo: {% ip "dot" %}
   - Hostname TLS: {% dot %}
4. Fai clic su _Applica_.

## OpenWrt

1. In _Sistema → Software_, aggiorna gli elenchi e installa `luci-app-https-dns-proxy`.
2. Apri _Servizi → HTTPS DNS Proxy_. Elimina le istanze di altri provider.
3. Aggiungi un'istanza con un URL resolver personalizzato: {% doh %}
4. _Salva e applica_. Il pacchetto imposta automaticamente dnsmasq su di esso.

## Altri router

Cerca un'impostazione chiamata _DNS over TLS_, _DNS privato_, _DNS crittografato_ o _DNS over HTTPS_. Inserisci il nome DNS di Blokada o il link DoH fornito sopra e rimuovi tutti gli altri server DNS, inclusi quelli di fallback. Se non esiste questa impostazione, utilizza un semplice indirizzo IPv6 come indicato sotto.

## Router che accettano solo un indirizzo IP

Per questo, il tuo router e la tua connessione Internet devono supportare IPv6. Il supporto per indirizzi IPv4 semplici arriverà in futuro.

1. Nel [dashboard](https://app.blokada.org/setup?src=guides), apri _Setup_ e scegli _Router, TV, console di gioco_.
2. Dai un nome al router, ad esempio _Router di casa_, e seleziona _Ottieni indirizzo_. Il nome apparirà nella tua attività e non potrà essere cambiato in seguito.
3. Nelle impostazioni del router, trova i server DNS per IPv6, spesso sotto _Internet_, _WAN_ o _IPv6_, e inserisci l'indirizzo come unico server DNS.
4. **Rimuovi tutti gli altri server DNS, inclusi quelli IPv4.** I dispositivi che ricevono ancora un server DNS IPv4 dal router invieranno alcune richieste fuori da Blokada. Se il router non consente di lasciare vuoto il campo DNS IPv4, configura i tuoi dispositivi uno alla volta invece: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [browser](../browser-dns-over-https/).

La stessa configurazione funziona per una TV o una console di gioco che consente l'inserimento manuale di un server DNS. Assegna ad ognuna un proprio indirizzo, in modo che sia visibile per nome nella tua attività.

<div class="note aside">

Queste richieste viaggiano in chiaro verso Blokada, come con qualsiasi server DNS non crittografato. Se il tuo router supporta DNS over TLS o DNS over HTTPS, usa quella modalità invece.

</div>

## Verifica che funzioni

1. Riavvia un dispositivo, oppure spegni e riaccendi il Wi-Fi così da applicare la nuova configurazione.
2. Su quel dispositivo, disattiva Blokada se attiva, poi visita [go.blokada.org/test](https://go.blokada.org/test). Ti mostrerà se il tuo DNS passa tramite Blokada.
3. Naviga per un minuto, poi apri la pagina _Attività_ nella [dashboard](https://app.blokada.org/stats?src=guides). Le richieste della tua rete saranno visibili lì.

## Se alcuni dispositivi mostrano ancora pubblicità

Alcuni dispositivi aggirano il router: telefoni con _DNS privato_ impostato, browser con _DNS sicuro_ configurato su un altro provider e dispositivi che impostano un DNS proprio. Configura questi dispositivi manualmente, o disattiva la loro impostazione DNS.

<div class="note tip">

Dietro il router, tutti i dispositivi condividono un solo indirizzo, quindi la dashboard mostra la tua rete come un unico dispositivo. Configura telefoni e laptop con il proprio nome DNS di Blokada se vuoi visualizzarli separatamente. In questo modo manterranno il blocco anche quando sono fuori casa.

</div>
