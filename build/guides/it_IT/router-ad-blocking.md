---
title: Blocca le pubblicità su tutta la tua rete con il blocco degli annunci dal router.
description: Configura Blokada Cloud una sola volta sul tuo router e tutti i dispositivi di casa saranno protetti, inclusi TV, console di gioco e altoparlanti intelligenti che non possono eseguire un'app blocca pubblicità.
updated: 02/10/2026
order: 4
---

Ogni dispositivo nella tua rete chiede al router quale server DNS utilizzare. Punta il router su Blokada Cloud e pubblicità e tracker saranno bloccati per tutto ciò che si trova dietro di esso. Questo include smart TV, console di gioco, stick per lo streaming e dispositivi smart home, che non hanno spazio per un'app blocca-pubblicità.

## Cosa serve al tuo router

Il tuo router deve supportare **DNS crittografato con un nome host**, ovvero DNS over TLS (DoT) o DNS over HTTPS (DoH). Molti router recenti lo fanno, inclusi i modelli sottoelencati. A seconda di ciò che il tuo router supporta, ti serviranno il tuo nome DNS o il tuo link DoH, entrambi sotto _I tuoi dettagli_ sopra.

<div class="note important">

**Solo indirizzi IP semplici?** Molti router dei provider internet accettano solo indirizzi IP semplici per il DNS. Il supporto per questi sarà presto disponibile. Fino ad allora, configura i tuoi dispositivi uno alla volta: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [browser](../browser-dns-over-https/). Puoi anche eseguire un piccolo forwarder su un Raspberry Pi, come descritto nella [guida Pi-hole](../switch-from-pihole/).

</div>

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

Cerca una voce chiamata _DNS over TLS_, _DNS privato_, _DNS crittografato_ o _DNS over HTTPS_. Inserisci il tuo nome DNS di Blokada o il link DoH da sopra e rimuovi ogni altro server DNS, inclusi i server di fallback.

## Verifica che funzioni

1. Riavvia un dispositivo, oppure spegni e riaccendi il Wi-Fi così da applicare la nuova configurazione.
2. Naviga per un minuto, poi apri la pagina _Attività_ nella dashboard. Le query della tua rete verranno mostrate lì.

## Se alcuni dispositivi mostrano ancora pubblicità

Alcuni dispositivi aggirano il router: telefoni con _DNS privato_ impostato, browser con _DNS sicuro_ configurato su un altro provider e dispositivi che impostano un DNS proprio. Configura questi dispositivi manualmente, o disattiva la loro impostazione DNS.

<div class="note tip">

Dietro il router, tutti i dispositivi condividono un solo indirizzo, quindi la dashboard mostra la tua rete come un unico dispositivo. Configura telefoni e laptop con il proprio nome DNS di Blokada se vuoi visualizzarli separatamente. In questo modo manterranno il blocco anche quando sono fuori casa.

</div>
