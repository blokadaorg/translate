---
title: Ett alternativ till NextDNS med samma inställning på alla enheter
description: Byt från NextDNS till Blokada Cloud. Ersätt NextDNS-namnet, DoH-länken eller profilen med Blokadas på telefon, dator och router och behåll reklamblockeringen.
updated: 2026-09-28
order: 3
---

NextDNS och Blokada Cloud fungerar på samma sätt: en krypterad DNS-tjänst som blockerar reklam och spårare utifrån namn, med dina egna inställningar bakom ett personligt DNS-namn. Att byta innebär att du ersätter NextDNS-värdena på varje enhet med dina Blokada-värden. Inget annat på enheten ändras.

## Det du använde och vad du väljer i Blokada

| I NextDNS | I Blokada Cloud |
|---|---|
| Ditt konfigurations-ID, t.ex. `abc123` | Din enhetstagg, en del av ditt Blokada-DNS-namn och din DoH-länk |
| Blocklistor under *Privacy* | *Blocklists* i dashboarden |
| *Security* (skadlig kod, nätfiske) | en lista mot skadlig kod under *Blocklists* |
| *Parental control* | listor för vuxeninnehåll och spel om pengar under *Blocklists* |
| *Allowlist* och *Denylist* | *Undantag* i dashboarden |
| *Logs* och *Analytics* | *Aktivitet* och *Stats* i dashboarden |

## Dina Blokada-uppgifter

- Ditt Blokada-DNS-namn, för DNS över TLS: {% dot %}
- Din DoH-länk, för DNS över HTTPS: {% doh %}

## Byt på varje enhet

### Android

Om du använde *Privat DNS* med `<your-id>.dns.nextdns.io` byter du ut det mot ditt Blokada-DNS-namn, enligt [Android-guiden](../android-private-dns/). Om du använde NextDNS-appen avinstallerar du den och installerar [Blokada 6](https://go.blokada.org/play_cloud) i stället.

### iPhone och iPad

Om du använde NextDNS-appen avinstallerar du den och installerar [Blokada 6](https://go.blokada.org/appstore). Om du i stället installerade en NextDNS-profil tar du bort den under *Inställningar → Allmänt → VPN och enhetshantering* och följer sedan [Apple-guiden](../apple-devices/).

### Mac och Apple TV

Ta bort NextDNS-profilen eller -appen och installera sedan Blokada-profilen enligt [Apple-guiden](../apple-devices/).

### Windows och Linux

Avinstallera NextDNS-appen om du använder den. I Windows ersätter du NextDNS-servern och DoH-mallen med Blokadas, enligt [Windows-guiden](../windows-dns-over-https/). I Linux ersätter du NextDNS-servern i systemd-resolved, enligt [Linux-guiden](../linux-dns-over-tls/).

### Webbläsare

Om du angav `https://dns.nextdns.io/…` som webbläsarens *säkra DNS* byter du ut den mot din DoH-länk, enligt [webbläsarguiden](../browser-dns-over-https/).

### Router

Om din router använder NextDNS via DNS över TLS eller DNS över HTTPS ersätter du NextDNS-namnet eller -länken med ditt Blokada-DNS-namn eller din DoH-länk, enligt [routerguiden](../router-ad-blocking/).

Om den använder NextDNS via vanliga IP-adresser med en *linked IP* kan Blokada inte ta över det än. Stöd för routrar med vanliga DNS-adresser är på väg. Till dess kan du ställa in dina enheter en i taget, eller använda en router som har stöd för krypterad DNS.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan *Aktivitet* i dashboarden. Där ser du dina enheters uppslag, och de blockerade är markerade. Om en enhet inte syns använder den fortfarande NextDNS.
