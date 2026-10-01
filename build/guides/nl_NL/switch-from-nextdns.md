---
title: Een NextDNS-alternatief met dezelfde configuratie op elk apparaat.
description: Stap over van NextDNS naar Blokada Cloud. Vervang je NextDNS-DNS-naam, DoH-link of profiel op je telefoon, computer en router door die van Blokada en behoud je advertentieblokkering.
updated: 2026-09-23
order: 3
---

NextDNS en Blokada Cloud werken op dezelfde manier: een versleutelde DNS-dienst die advertenties en trackers op naam blokkeert, met je eigen instellingen achter een persoonlijke DNS-naam. Overschakelen betekent dat je de NextDNS-gegevens op ieder apparaat vervangt door die van Blokada. Verder verandert er niets op het apparaat.

## Wat je gebruikte, en wat je moet kiezen in Blokada

| In NextDNS                                           | In Blokada Cloud                                                  |
| ---------------------------------------------------- | ----------------------------------------------------------------- |
| Je configuratie-ID, bijvoorbeeld `abc123`            | Je apparaattag, onderdeel van je Blokada DNS-naam en DoH-link     |
| _Privacy_-blocklists                                 | _Blocklists_ in het dashboard                                     |
| _Beveiliging_ (malware, phishing) | een malwarelijst onder _Blocklists_                               |
| _Ouderlijk toezicht_                                 | lijsten voor inhoud voor volwassenen en gokken onder _Blocklists_ |
| _Allowlist_ en _Denylist_                            | _Uitzonderingen_ in het dashboard                                 |
| _Logboeken_ en _Analytics_                           | _Activiteit_ en _Statistieken_ in het dashboard                   |

## Je Blokada-gegevens

- Je Blokada DNS-naam, voor DNS over TLS: {% dot %}
- Je DoH-link, voor DNS over HTTPS: {% doh %}

## Schakel elk apparaat om

### Android

Als je _Privé DNS_ gebruikte met `<your-id>.dns.nextdns.io`, vervang deze dan door je Blokada DNS-naam, zoals uitgelegd in de [Android-gids](../android-private-dns/). Als je de NextDNS-app gebruikte, verwijder deze en installeer in plaats daarvan [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone en iPad

Als je de NextDNS-app gebruikte, verwijder deze en installeer [Blokada 6](https://go.blokada.org/appstore). Als je in plaats daarvan een NextDNS-profiel hebt geïnstalleerd, verwijder het dan onder _Instellingen → Algemeen → VPN & Apparaatbeheer_ en volg daarna de [Apple-gids](../apple-devices/).

### Mac en Apple TV

Verwijder het NextDNS-profiel of de app en installeer daarna het Blokada-profiel via de [Apple-gids](../apple-devices/).

### Windows en Linux

Verwijder de NextDNS-app als je deze gebruikt. Vervang op Windows de NextDNS-server en DoH-sjabloon door die van Blokada, zoals in de [Windows-gids](../windows-dns-over-https/). Vervang op Linux de NextDNS-server in systemd-resolved, zoals in de [Linux-gids](../linux-dns-over-tls/).

### Browsers

Als je `https://dns.nextdns.io/…` als _beveiligde DNS_ in je browser hebt ingesteld, vervang die dan door je DoH-link, zoals in de [browsergids](../browser-dns-over-https/).

### Router

Als je router NextDNS gebruikt via DNS over TLS of DNS over HTTPS, vervang dan de NextDNS-naam of -link door die van Blokada volgens de [routergids](../router-ad-blocking/).

Als hij NextDNS gebruikt via gewone IP-adressen met een _gekoppeld IP_, kan Blokada dat nog niet overnemen. Ondersteuning voor routers met gewone DNS-adressen komt eraan. Tot die tijd stel je je apparaten één voor één in, of gebruik je een router die versleutelde DNS ondersteunt.

## Controleer of het werkt

Open een paar websites en bekijk daarna de pagina _Activiteit_ in het dashboard. Je ziet daar de opvragingen van je apparaten, waarbij geblokkeerde zijn gemarkeerd. Als een apparaat niet zichtbaar is, gebruikt het nog steeds NextDNS.
