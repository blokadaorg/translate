---
title: Ett alternativ till NextDNS med samma inställning på alla enheter
description: Flytta från NextDNS till Blokada Cloud. Byt ut ditt NextDNS DNS-namn, DoH-länk eller profil mot Blokadas på din telefon, dator och router, och behåll din annonsblockering.
updated: 2026-09-28
order: 3
---

NextDNS och Blokada Cloud fungerar på samma sätt: en krypterad DNS-tjänst som blockerar annonser och spårare med namn, med dina egna inställningar bakom ett personligt DNS-namn. Att byta innebär att ersätta NextDNS-värdena på varje enhet med dina Blokada-värden. Inget annat på enheten ändras.

## Det du använde och vad du väljer i Blokada

| I NextDNS                                                             | I Blokada Cloud                                                  |
| --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Din konfigurations-ID, t.ex. `abc123` | Din enhetstagg, en del av ditt Blokada-DNS-namn och din DoH-länk |
| Blocklistor under _Privacy_                                           | _Blocklists_ i dashboarden                                       |
| _Security_ (skadlig kod, nätfiske)                 | en lista mot skadlig kod under _Blocklists_                      |
| _Föräldrakontroll_                                                    | listor för vuxeninnehåll och spel om pengar under _Blocklists_   |
| _Allowlist_ och _Denylist_                                            | _Undantag_ i dashboarden                                         |
| _Logs_ och _Analytics_                                                | _Aktivitet_ och _Stats_ i dashboarden                            |

## Dina Blokada-uppgifter

- Ditt Blokada-DNS-namn, för DNS över TLS: {% dot %}
- Din DoH-länk, för DNS över HTTPS: {% doh %}

## Byt på varje enhet

### Android

Om du använde _Privat DNS_ med `<your-id>.dns.nextdns.io`, ersätt den med ditt Blokada DNS-namn, enligt [Android-guiden](../android-private-dns/). Om du använde NextDNS-appen, avinstallera den och installera istället [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone och iPad

Om du använde NextDNS-appen, avinstallera den och installera istället [Blokada 6](https://go.blokada.org/appstore). Om du istället installerade en NextDNS-profil, ta bort den under _Inställningar → Allmänt → VPN & enhetshantering_, följ sedan [Apple-guiden](../apple-devices/).

### Mac och Apple TV

Ta bort NextDNS-profilen eller -appen och installera sedan Blokada-profilen enligt [Apple-guiden](../apple-devices/).

### Windows och Linux

Avinstallera NextDNS-appen om du använder den. På Windows, ersätt NextDNS-servern och DoH-mall med Blokadas, enligt [Windows-guiden](../windows-dns-over-https/). På Linux, ersätt NextDNS-servern i systemd-resolved, enligt [Linux-guiden](../linux-dns-over-tls/).

### Webbläsare

Om du angav `https://dns.nextdns.io/…` som webbläsarens _säkra DNS_ byter du ut den mot din DoH-länk, enligt [webbläsarguiden](../browser-dns-over-https/).

### Router

Om din router använder NextDNS via DNS över TLS eller DNS över HTTPS ersätter du NextDNS-namnet eller -länken med ditt Blokada-DNS-namn eller din DoH-länk, enligt [routerguiden](../router-ad-blocking/).

Om den använder NextDNS via vanliga IP-adresser med en _länkad IP_, kan Blokada ännu inte ta över det. Stöd för routrar med vanliga DNS-adresser är på väg. Tills dess, konfigurera dina enheter en och en, eller använd en router som stöder krypterad DNS.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan _Aktivitet_ i instrumentpanelen. Du ser dina enheters uppslag där, med blockerade markerade. Om en enhet inte visas där används fortfarande NextDNS.
