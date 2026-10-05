---
title: Ett alternativ till NextDNS med samma inställning på alla enheter
description: Byt från NextDNS till Blokada Cloud. Ersätt NextDNS-namnet, DoH-länken eller profilen med Blokadas på telefon, dator och router och behåll reklamblockeringen.
updated: 2026-10-02
order: 3
---

NextDNS och Blokada Cloud fungerar på samma sätt: en krypterad DNS-tjänst som blockerar reklam och spårare utifrån namn, med dina egna inställningar bakom ett personligt DNS-namn. Att byta innebär att du ersätter NextDNS-värdena på varje enhet med dina Blokada-värden. Inget annat på enheten ändras.

## Det du använde och vad du väljer i Blokada

| I NextDNS                                                              | I Blokada Cloud                                                  |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Ditt konfigurations-ID, t.ex. `abc123` | Din enhetstagg, en del av ditt Blokada-DNS-namn och din DoH-länk |
| Blocklistor under _Privacy_                                            | _Blocklistor_ i dashboarden                                      |
| _Security_ (skadlig kod, nätfiske)                  | en lista mot skadlig kod under _Blocklistor_                     |
| _Parental control_                                                     | listor för vuxeninnehåll och spel om pengar under _Blocklistor_  |
| _Allowlist_ och _Denylist_                                             | _Undantag_ i dashboarden                                         |
| _Logs_ och _Analytics_                                                 | _Aktivitet_ och _Statistik_ i dashboarden                        |

## Byt på varje enhet

Beroende på enheten behöver du ditt DNS-namn eller din DoH-länk, båda finns under _Dina uppgifter_ ovan.

### Android

Om du använde _Privat DNS_ med `<your-id>.dns.nextdns.io` byter du ut det mot ditt Blokada-DNS-namn, enligt [Android-guiden](../android-private-dns/). Om du använde NextDNS-appen avinstallerar du den och installerar [Blokada 6](https://go.blokada.org/play_cloud) i stället.

### iPhone och iPad

Om du använde NextDNS-appen avinstallerar du den och installerar [Blokada 6](https://go.blokada.org/appstore). Om du i stället installerade en NextDNS-profil tar du bort den under _Inställningar → Allmänt → VPN och enhetshantering_ och följer sedan [Apple-guiden](../apple-devices/).

### Mac och Apple TV

Ta bort NextDNS-profilen eller -appen och installera sedan Blokada-profilen enligt [Apple-guiden](../apple-devices/).

### Windows och Linux

Avinstallera NextDNS-appen om du använder den. I Windows ersätter du NextDNS-servern och DoH-mallen med Blokadas, enligt [Windows-guiden](../windows-dns-over-https/). I Linux ersätter du NextDNS-servern i systemd-resolved, enligt [Linux-guiden](../linux-dns-over-tls/).

### Webbläsare

Om du angav `https://dns.nextdns.io/…` som webbläsarens _säkra DNS_ byter du ut den mot din DoH-länk, enligt [webbläsarguiden](../browser-dns-over-https/).

### Router

Om din router använder NextDNS via DNS över TLS eller DNS över HTTPS ersätter du NextDNS-namnet eller -länken med ditt Blokada-DNS-namn eller din DoH-länk, enligt [routerguiden](../router-ad-blocking/).

Om den använder NextDNS via vanliga IP-adresser med en _linked IP_ kan Blokada inte ta över det än. Stöd för routrar med vanliga DNS-adresser är på väg. Till dess kan du ställa in dina enheter en i taget, eller använda en router som har stöd för krypterad DNS.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan _Aktivitet_ i dashboarden. Där ser du dina enheters uppslag, och de blockerade är markerade. Om en enhet inte syns använder den fortfarande NextDNS.
