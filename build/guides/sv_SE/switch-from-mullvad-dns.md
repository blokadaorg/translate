---
title: Mullvad DNS läggs ner. Behåll reklamblockeringen med Blokada Cloud
description: Mullvad stänger sin publika DNS den 2 november 2026. Så flyttar du telefon, dator och router till Blokada Cloud innan dess och behåller reklamblockeringen.
updated: 2026-09-23
order: 2
---

Mullvad stänger sin kostnadsfria publika DNS-tjänst den **2 november 2026** och rekommenderar Quad9 i stället. Quad9 blockerar skadlig kod men blockerar **inte** reklam eller spårare. Om du använde något av Mullvads filtrerande DNS-namn kommer reklamen tillbaka det datumet, om du inte byter.

Den här sidan gäller de publika DNS-namnen som slutar på `dns.mullvad.net`. Den gäller inte Mullvads VPN-app.

## Det du använde och vad du väljer i Blokada

| Mullvads DNS-namn | Det här blockerades | I Blokadas dashboard |
|---|---|---|
| `dns.mullvad.net` | ingenting | Blokada är en filtreringstjänst. Vill du inte ha någon filtrering är Quad9 eller din leverantörs DNS det enklare valet. |
| `adblock.dns.mullvad.net` | reklam, spårare | en blocklista för reklam och spårare |
| `base.dns.mullvad.net` | reklam, spårare, skadlig kod | lägg till en lista mot skadlig kod |
| `extended.dns.mullvad.net` | base plus sociala medier | lägg till en lista för sociala medier |
| `family.dns.mullvad.net` | base plus vuxeninnehåll och spel om pengar | lägg till listor för vuxeninnehåll och spel om pengar |
| `all.dns.mullvad.net` | allt ovan | aktivera alla |

Du väljer blocklistor i dashboarden under *Blocklists*. Du kan ändra dem när som helst, och ändringen gäller alla dina enheter.

## Dina Blokada-uppgifter

Blokada ger varje enhet ett eget namn, så att dashboarden kan visa aktivitet per enhet:

- Ditt Blokada-DNS-namn, för DNS över TLS (Android, routrar): {% dot %}
- Din DoH-länk, för DNS över HTTPS (webbläsare, vissa routrar): {% doh %}

## Byt på varje enhet

### Android

Enligt Mullvads guide angav du ett värdnamn under *Privat DNS*. Byt ut det mot ditt Blokada-DNS-namn. [Android-guiden](../android-private-dns/) visar stegen.

### iPhone, iPad och Mac

Mullvads installation använde en konfigurationsprofil. Ta bort den först:

- **iPhone och iPad:** *Inställningar → Allmänt → VPN och enhetshantering*, tryck på Mullvads DNS-profil och sedan på *Ta bort profil*.
- **Mac:** öppna listan med profiler (*Systeminställningar → Allmänt → Enhetshantering* på macOS 15 och senare, *Systeminställningar → Integritet och säkerhet → Profiler* på macOS 13 och 14, *Systeminställningar → Profiler* på macOS 12 och tidigare), markera Mullvads DNS-profil och klicka på *−*.

Installera sedan Blokada-profilen enligt [Apple-guiden](../apple-devices/).

### Webbläsare

Om du angav en Mullvad-DoH-länk som `https://adblock.dns.mullvad.net/dns-query` under *säker DNS* eller *DNS över HTTPS* byter du ut den mot din DoH-länk. [Webbläsarguiden](../browser-dns-over-https/) visar stegen för varje webbläsare.

### Router

Om din router använder Mullvad via DNS över TLS byter du ut Mullvads värdnamn mot ditt Blokada-DNS-namn och tar bort Mullvads IP-adresser. [Routerguiden](../router-ad-blocking/) tar upp vanliga modeller.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan *Aktivitet* i dashboarden. Där ser du dina enheters uppslag, och de blockerade är markerade. Om en enhet inte syns använder den fortfarande en annan DNS-server.
