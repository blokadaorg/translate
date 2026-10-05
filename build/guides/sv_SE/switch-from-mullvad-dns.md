---
title: Mullvad DNS läggs ner. Behåll reklamblockeringen med Blokada Cloud
description: Mullvad stänger sin publika DNS den 2 november 2026. Så flyttar du telefon, dator och router till Blokada Cloud innan dess och behåller reklamblockeringen.
updated: 2026-10-02
order: 2
---

Mullvad stänger sin kostnadsfria publika DNS-tjänst den **2 november 2026** och rekommenderar Quad9 i stället. Quad9 blockerar skadlig kod men blockerar **inte** reklam eller spårare. När Mullvads DNS stängs slutar enheter som är inställda på den att ladda webbplatser och appar. Om en enhet får falla tillbaka på en annan DNS-server kommer reklamen tillbaka i stället. Byt före det datumet.

Den här sidan gäller de publika DNS-namnen som slutar på `dns.mullvad.net`. Den gäller inte Mullvads VPN-app.

## Det du använde och vad du väljer i Blokada

| Mullvads DNS-namn          | Det här blockerades                        | I Blokadas dashboard                                                                                                                                     |
| -------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | ingenting                                  | Blokada är en filtreringstjänst. Om du inte vill ha någon filtrering är Quad9 eller din leverantörs DNS ett enklare val. |
| `adblock.dns.mullvad.net`  | reklam, spårare                            | en blocklista för reklam och spårare                                                                                                                     |
| `base.dns.mullvad.net`     | reklam, spårare, skadlig kod               | lägg till en lista mot skadlig kod                                                                                                                       |
| `extended.dns.mullvad.net` | base plus sociala medier                   | lägg till en lista för sociala medier                                                                                                                    |
| `family.dns.mullvad.net`   | base plus vuxeninnehåll och spel om pengar | lägg till listor för vuxeninnehåll och spel om pengar                                                                                                    |
| `all.dns.mullvad.net`      | allt ovan                                  | aktivera alla                                                                                                                                            |

Du väljer blocklistor i dashboarden under _Blocklistor_. Du kan ändra dem när som helst, och ändringen gäller alla dina enheter.

## Byt på varje enhet

Blokada ger varje enhet ett eget namn, så att dashboarden kan visa aktivitet per enhet. Beroende på enhet behöver du ditt DNS-namn eller din DoH-länk. Båda finns under _Dina uppgifter_ ovan.

### Android

Enligt Mullvads guide angav du ett värdnamn under _Privat DNS_. Byt ut det mot ditt Blokada-DNS-namn. [Android-guiden](../android-private-dns/) visar stegen.

### iPhone, iPad och Mac

Mullvads installation använde en konfigurationsprofil. Ta bort den först:

- **iPhone och iPad:** _Inställningar → Allmänt → VPN och enhetshantering_, tryck på Mullvads DNS-profil och sedan på _Ta bort profil_.
- **Mac:** öppna listan med profiler (_Systeminställningar → Allmänt → Enhetshantering_ på macOS 15 och senare, _Systeminställningar → Integritet och säkerhet → Profiler_ på macOS 13 och 14, _Systeminställningar → Profiler_ på macOS 12 och tidigare), markera Mullvads DNS-profil och klicka på _−_.

Installera sedan Blokada-profilen enligt [Apple-guiden](../apple-devices/).

### Webbläsare

Om du angav en Mullvad-DoH-länk som `https://adblock.dns.mullvad.net/dns-query` under _säker DNS_ eller _DNS över HTTPS_ byter du ut den mot din DoH-länk. [Webbläsarguiden](../browser-dns-over-https/) visar stegen för varje webbläsare.

### Router

Om din router använder Mullvad via DNS över TLS byter du ut Mullvads värdnamn mot ditt Blokada-DNS-namn och tar bort Mullvads IP-adresser. [Routerguiden](../router-ad-blocking/) tar upp vanliga modeller.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan _Aktivitet_ i dashboarden. Där ser du dina enheters uppslag, och de blockerade är markerade. Om en enhet inte syns använder den fortfarande en annan DNS-server.
