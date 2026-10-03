---
title: Blocca le pubblicità su tutta la tua rete con il blocco degli annunci dal router.
description: Configura Blokada Cloud una sola volta sul tuo router e tutti i dispositivi di casa saranno protetti, inclusi TV, console di gioco e altoparlanti intelligenti che non possono eseguire un'app blocca pubblicità.
updated: 02/10/2026
order: 4
---

Ogni dispositivo sulla tua rete chiede al router quale server DNS utilizzare. Imposta il router su Blokada Cloud e pubblicità e tracker saranno bloccati per tutto ciò che si collega attraverso di esso. Questo include smart TV, console di gioco, chiavette di streaming e dispositivi per la casa intelligente, che non hanno spazio per un'app blocca pubblicità.

## Cosa serve al tuo router

Il tuo router deve supportare **DNS crittografato con nome host**, ossia DNS over TLS (DoT) oppure DNS over HTTPS (DoH). Molti router recenti lo supportano, inclusi i modelli qui sotto. A seconda della tecnologia supportata dal tuo router, avrai bisogno del tuo nome DNS o del tuo link DoH, entrambi disponibili sotto _I tuoi dati_ qui sopra.

<div class="note important">

**Solo indirizzi IP semplici?** Molti router forniti dai provider Internet accettano solo indirizzi IP semplici per il DNS. Il supporto per questi router è in arrivo. Fino ad allora, configura i tuoi dispositivi uno alla volta: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), e [browser](../browser-dns-over-https/). Puoi anche eseguire un piccolo inoltratore su un Raspberry Pi, come descritto nella [guida Pi-hole](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 o successivo.

1. Apri `http://fritz.box` e vai su _Internet → Informazioni account → Server DNS_.
2. Sotto _Risoluzione dei nomi crittografata su Internet (DNS over TLS)_, seleziona _Usa la risoluzione dei nomi crittografata_.
3. In _Nomi dei resolver_, inserisci solo {% dot %}. **Rimuovi ogni altra voce.** Il FRITZ!Box usa tutti i resolver inseriti, e qualsiasi altro permette alle pubblicità di passare.
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
2. Apri _Servizi → HTTPS DNS Proxy_. Elimina le istanze per altri provider.
3. Aggiungi un'istanza con un URL resolver personalizzato: {% doh %}
4. _Salva & Applica_. Il pacchetto imposta automaticamente dnsmasq su di esso.

## Altri router

Cerca un'impostazione chiamata _DNS over TLS_, _DNS privato_, _DNS crittografato_ o _DNS over HTTPS_. Inserisci il nome DNS di Blokada o il link DoH sopra indicato, e rimuovi gli altri server DNS, inclusi quelli di fallback.

## Verifica che funzioni

1. Riavvia un dispositivo, oppure spegni e riaccendi il Wi-Fi così da applicare la nuova configurazione.
2. Naviga per un minuto, poi apri la pagina _Attività_ nella dashboard. Le richieste della tua rete compaiono lì.

## Se alcuni dispositivi mostrano ancora pubblicità

Alcuni dispositivi aggirano il router: telefoni con _DNS privato_ impostato, browser con _DNS sicuro_ configurato su un altro provider e dispositivi che impostano un DNS proprio. Configura quelli direttamente dal dispositivo, oppure disattiva la rispettiva impostazione DNS.

<div class="note tip">

Dietro il router, tutti i dispositivi condividono un solo indirizzo, quindi la dashboard mostra la tua rete come un unico dispositivo. Configura telefoni e laptop con un nome DNS di Blokada dedicato se vuoi visualizzarli separatamente. Inoltre, continuano a bloccare le pubblicità quando lasciano casa.

</div>
