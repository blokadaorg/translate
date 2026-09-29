---
title: Ett NextDNS-alternativ med samma konfiguration på alla enheter
description: Flytta från NextDNS till Blokada Cloud. Byt ut ditt NextDNS DNS-namn, DoH-länk eller profil mot Blokadas på din telefon, dator och router, och behåll din annonsblockering.
updated: 2026-09-28
order: 3
---

NextDNS och Blokada Cloud fungerar på samma sätt: en krypterad DNS-tjänst som blockerar annonser och spårare med namn, med dina egna inställningar bakom ett personligt DNS-namn. Att byta innebär att ersätta NextDNS-värdena på varje enhet med dina Blokada-värden. Inget annat på enheten ändras.

## Vad du brukade använda, och vad du ska välja i Blokada

| I NextDNS                                                             | I Blokada Cloud                                                 |
| --------------------------------------------------------------------- | --------------------------------------------------------------- |
| Din konfigurations-ID, t.ex. `abc123` | Din enhetsetikett, en del av ditt Blokada DNS-namn och DoH-länk |
| _Integritet_ blocklistor                                              | _Blocklistor_ i instrumentpanelen                               |
| _Säkerhet_ (skadlig kod, nätfiske)                 | en skadlig kod-lista under _Blocklistor_                        |
| _Föräldrakontroll_                                                    | listor för vuxeninnehåll och spel under _Blocklistor_           |
| _Tillåtslista_ och _Nekalista_                                        | _Undantag_ i instrumentpanelen                                  |
| _Loggar_ och _Analys_                                                 | _Aktivitet_ och _Statistik_ i instrumentpanelen                 |

## Dina Blokada-detaljer

- Ditt Blokada DNS-namn, för DNS över TLS: {% dot %}
- Din DoH-länk, för DNS över HTTPS: {% doh %}

## Byt varje enhet

### Android

Om du använde _Privat DNS_ med `<your-id>.dns.nextdns.io`, ersätt den med ditt Blokada DNS-namn, enligt [Android-guiden](../android-private-dns/). Om du använde NextDNS-appen, avinstallera den och installera istället [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone och iPad

Om du använde NextDNS-appen, avinstallera den och installera istället [Blokada 6](https://go.blokada.org/appstore). Om du istället installerade en NextDNS-profil, ta bort den under _Inställningar → Allmänt → VPN & enhetshantering_, följ sedan [Apple-guiden](../apple-devices/).

### Mac och Apple TV

Ta bort NextDNS-profilen eller -appen, installera sedan Blokada-profilen enligt [Apple-guiden](../apple-devices/).

### Windows och Linux

Avinstallera NextDNS-appen om du använder den. På Windows, ersätt NextDNS-servern och DoH-mall med Blokadas, enligt [Windows-guiden](../windows-dns-over-https/). På Linux, ersätt NextDNS-servern i systemd-resolved, enligt [Linux-guiden](../linux-dns-over-tls/).

### Webbläsare

Om du har ställt in `https://dns.nextdns.io/…` som din webbläsares _säker DNS_, ersätt den med din DoH-länk, enligt [webbläsarguiden](../browser-dns-over-https/).

### Router

Om din router använder NextDNS via DNS över TLS eller DNS över HTTPS, ersätt NextDNS-namnet eller länken med din Blokada, enligt [router-guiden](../router-ad-blocking/).

Om den använder NextDNS via vanliga IP-adresser med en _länkad IP_, kan Blokada ännu inte ta över det. Stöd för routrar med vanliga DNS-adresser är på väg. Tills dess, konfigurera dina enheter en och en, eller använd en router som stöder krypterad DNS.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan _Aktivitet_ i instrumentpanelen. Du ser dina enheters uppslag där, med blockerade markerade. Om en enhet inte visas där används fortfarande NextDNS.
