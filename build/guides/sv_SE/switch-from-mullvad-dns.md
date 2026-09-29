---
title: Mullvad DNS stängs ner. Behåll din annonsblockering med Blokada Cloud
description: Mullvad stänger sin publika DNS den 2 november 2026. Så här flyttar du din telefon, dator och router till Blokada Cloud innan dess, utan att förlora annonsblockering.
updated: 2026-09-23
order: 2
---

Mullvad stänger sin kostnadsfria publika DNS-tjänst den **2 november 2026** och rekommenderar Quad9 istället. Quad9 blockerar skadlig kod men blockerar **inte** annonser eller spårare. Om du har använt ett av Mullvads filtrerande DNS-namn kommer annonser tillbaka det datumet om du inte byter.

Denna sida handlar om de publika DNS-namnen som slutar på `dns.mullvad.net`. Den täcker inte Mullvad VPN-appen.

## Vad du använde och vad du ska välja i Blokada

| Mullvad DNS-namn           | Vad den blockerade              | I Blokada-panelen                                                                                                                                        |
| -------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | inget                           | Blokada är en filtreringstjänst. Om du inte vill ha någon filtrering är Quad9 eller din leverantörs DNS ett enklare val. |
| `adblock.dns.mullvad.net`  | annonser, spårare               | en blocklista för annonser och spårare                                                                                                                   |
| `base.dns.mullvad.net`     | annonser, spårare, skadlig kod  | lägg till en lista för skadlig kod                                                                                                                       |
| `extended.dns.mullvad.net` | bas plus sociala medier         | lägg till en lista för sociala medier                                                                                                                    |
| `family.dns.mullvad.net`   | bas plus vuxeninnehåll och spel | lägg till listor för vuxeninnehåll och spel                                                                                                              |
| `all.dns.mullvad.net`      | alla ovanstående                | aktivera alla                                                                                                                                            |

Du väljer blocklistor i panelen under _Blocklistor_. Du kan ändra dem när som helst, och ändringarna gäller för alla dina enheter.

## Dina Blokada-detaljer

Blokada ger varje enhet ett eget namn så att panelen kan visa aktivitet per enhet:

- Ditt Blokada DNS-namn, för DNS över TLS (Android, routrar): {% dot %}
- Din DoH-länk, för DNS över HTTPS (webbläsare, vissa routrar): {% doh %}

## Byt varje enhet

### Android

Mullvads guide bad dig ange ett värdnamn under _Privat DNS_. Byt ut det mot ditt Blokada DNS-namn. [Android-guiden](../android-private-dns/) har stegen.

### iPhone, iPad och Mac

Mullvads installationsguide använde en konfigurationsprofil. Ta bort den först:

- **iPhone och iPad:** _Inställningar → Allmänt → VPN & enhetshantering_, tryck på Mullvad DNS-profilen och sedan _Ta bort profil_.
- **Mac:** öppna listan över profiler (_Systeminställningar → Allmänt → Enhetshantering_ på macOS 15 och senare, _Systeminställningar → Integritet & säkerhet → Profiler_ på macOS 13 och 14, _Systeminställningar → Profiler_ på macOS 12 och tidigare), välj Mullvad DNS-profilen och klicka på _−_.

Installera sedan Blokada-profilen från [Apple-guiden](../apple-devices/).

### Webbläsare

Om du har angett en Mullvad DoH-länk såsom `https://adblock.dns.mullvad.net/dns-query` under _säker DNS_ eller _DNS över HTTPS_, byt ut den mot din DoH-länk. [Webbläsarguiden](../browser-dns-over-https/) visar stegen för varje webbläsare.

### Router

Om din router använder Mullvad via DNS över TLS, byt ut Mullvads värdnamn mot ditt Blokada DNS-namn och ta bort Mullvads IP-adresser. [Router-guiden](../router-ad-blocking/) täcker vanliga modeller.

## Kontrollera att det fungerar

Öppna några webbsidor och titta sedan på sidan _Aktivitet_ i panelen. Du ser dina enheters uppslag där, med blockerade markerade. Om en enhet inte visas använder den fortfarande en annan DNS-server.
