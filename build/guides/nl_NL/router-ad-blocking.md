---
title: Blokkeer advertenties op je hele netwerk met router-advertentieblokkering.
description: Stel Blokada Cloud één keer in op je router en elk apparaat thuis is beschermd, inclusief tv's, spelcomputers en slimme speakers die geen advertentieblokker kunnen uitvoeren.
updated: 2026-09-23
order: 4
---

Elk apparaat op je netwerk vraagt de router welke DNS-server gebruikt moet worden. Wijs de router naar Blokada Cloud en advertenties en trackers worden voor alles erachter geblokkeerd. Daarbij horen slimme tv's, spelcomputers, streamingsticks en slimme apparaten voor thuis, waarvoor geen advertentieblokker-app beschikbaar is.

## Wat je router nodig heeft

Je router moet **versleutelde DNS met een hostnaam** ondersteunen, oftewel DNS over TLS (DoT) of DNS over HTTPS (DoH). Veel recente routers ondersteunen dit, waaronder de onderstaande modellen. Afhankelijk van wat je router ondersteunt, heb je het volgende nodig:

- Voor DNS over TLS, je Blokada DNS-naam: {% dot %}
- Voor DNS over HTTPS, je DoH-link: {% doh %}

<div class="note">

**Alleen platte IP-adressen?** Veel routers van internetproviders accepteren alleen platte IP-adressen voor DNS. Ondersteuning daarvoor is onderweg. Tot die tijd stel je je apparaten één voor één in: [Android](../android-private-dns/), [Mac en Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) en [browsers](../browser-dns-over-https/). Je kunt ook een kleine forwarder op een Raspberry Pi draaien, zoals beschreven in de [Pi-hole handleiding](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 of nieuwer.

1. Open `http://fritz.box` en ga naar _Internet → Accountgegevens → DNS-server_.
2. Vink bij _Versleutelde naamomzetting op internet (DNS over TLS)_ de optie _Versleutelde naamomzetting gebruiken_ aan.
3. Voer onder _Resolvernamen_ alleen {% dot %} in. **Verwijder alle andere vermeldingen.** De FRITZ!Box gebruikt alle vermelde resolvers; elke andere laat advertenties door.
4. Vink de optie aan die certificaatverificatie afdwingt, en vink de optie uit waarmee terugval op niet-versleutelde naamsomzetting is toegestaan.
5. Als je _Failover naar openbare DNS-servers wanneer DNS wordt onderbroken_ ziet, schakel deze dan uit.
6. Klik op _Toepassen_.

## ASUS

Recente ASUS-firmware (3.0.0.4.388 of nieuwer) en Asuswrt-Merlin.

1. Open de routerbeheerpagina en ga naar _WAN → Internetverbinding_.
2. Stel bij _WAN DNS-instelling_ de optie _DNS Privacy Protocol_ in op _DNS-over-TLS (DoT)_ en _DNS-over-TLS-profiel_ op _Strict_.
3. Verwijder alle vermeldingen uit de _DNS-over-TLS Serverlijst_ en voeg er dan één toe:
   - Adres: {% ip "dot" %}
   - TLS-hostnaam: {% dot %}
4. Klik op _Toepassen_.

## OpenWrt

1. Werk in _Systeem → Software_ de lijsten bij en installeer `luci-app-https-dns-proxy`.
2. Open _Diensten → HTTPS DNS Proxy_. Verwijder de instanties voor andere providers.
3. Voeg een instantie toe met een aangepaste resolver-URL: {% doh %}
4. _Opslaan & Toepassen_. Het pakket wijst dnsmasq er automatisch naar toe.

## Andere routers

Zoek naar een instelling genaamd _DNS over TLS_, _Private DNS_, _Versleutelde DNS_ of _DNS over HTTPS_. Voer je Blokada DNS-naam of DoH-link van hierboven in en verwijder elke andere DNS-server, ook fallback-servers.

## Controleer of het werkt

1. Herstart één apparaat of zet de wifi uit en weer aan, zodat het de wijziging oppikt.
2. Navigeer één minuut op internet en open dan de pagina _Activiteit_ in het dashboard. De opvragingen van je netwerk verschijnen daar.

Sommige apparaten omzeilen de router: telefoons met _Private DNS_ ingesteld, browsers met _beveiligde DNS_ ingesteld bij een andere provider en apparaten die hun eigen DNS hard-coderen. Stel deze in op het apparaat zelf of schakel hun eigen DNS-instelling uit.

<div class="note">

Achter de router delen alle apparaten één adres, dus het dashboard toont je netwerk als één apparaat. Stel telefoons en laptops in met hun eigen Blokada DNS-naam als je ze apart wilt zien. Ze behouden hun blokkering ook als ze thuis weg zijn.

</div>
