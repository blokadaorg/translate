---
title: Mullvad DNS stopt ermee. Blijf advertenties blokkeren met Blokada Cloud
description: Mullvad sluit zijn publieke DNS op 2 november 2026. Zo kun je je telefoon, computer en router vóór die tijd overzetten naar Blokada Cloud, zonder advertentieblokkering te verliezen.
updated: 2026-10-02
order: 2
---

Mullvad sluit zijn gratis publieke DNS-dienst op **2 november 2026** en raadt in plaats daarvan Quad9 aan. Quad9 blokkeert malware, maar blokkeert **geen** advertenties of trackers. Zodra de DNS van Mullvad stopt, laden apparaten die daarop ingesteld zijn geen websites en apps meer. Als een apparaat automatisch overschakelt naar een andere DNS-server, komen advertenties weer terug. Schakel daarom vóór die datum over.

Deze pagina gaat over de publieke DNS-namen die eindigen op `dns.mullvad.net`. Het behandelt niet de Mullvad VPN-app.

## Wat je gebruikte en wat je moet kiezen in Blokada

| Mullvad DNS naam           | Wat het blokkeerde                           | In het Blokada-dashboard                                                                                                                   |
| -------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `dns.mullvad.net`          | niets                                        | Blokada is een filterdienst. Als je geen filtering wilt, zijn Quad9 of de DNS van je provider eenvoudiger. |
| `adblock.dns.mullvad.net`  | advertenties, trackers                       | een advertentie- en tracker-blokkeerlijst                                                                                                  |
| `base.dns.mullvad.net`     | advertenties, trackers, malware              | voeg een malwarelijst toe                                                                                                                  |
| `extended.dns.mullvad.net` | basis plus sociale media                     | voeg een sociale-medialijst toe                                                                                                            |
| `family.dns.mullvad.net`   | basis plus inhoud voor volwassenen en gokken | voeg lijsten voor volwassenen en gokken toe                                                                                                |
| `all.dns.mullvad.net`      | al het bovenstaande                          | zet ze allemaal aan                                                                                                                        |

Je kiest blokkeerlijsten in het dashboard onder _Blokkeerlijsten_. Je kunt ze op elk moment wijzigen, en de wijziging geldt voor al je apparaten.

## Schakel elk apparaat over

Blokada geeft elk apparaat een eigen naam, zodat het dashboard activiteit per apparaat kan tonen. Afhankelijk van het apparaat heb je je DNS-naam of DoH-link nodig, beide te vinden onder _Jouw gegevens_ hierboven.

### Android

In de handleiding van Mullvad vulde je een hostnaam in onder _Private DNS_. Vervang deze door je Blokada DNS-naam. De [Android handleiding](../android-private-dns/) legt de stappen uit.

### iPhone, iPad en Mac

De configuratie van Mullvad gebruikte een configuratieprofiel. Verwijder dit eerst:

- **iPhone en iPad:** _Instellingen → Algemeen → VPN & apparaatbeheer_, tik op het Mullvad DNS-profiel en kies vervolgens _Verwijder profiel_.
- **Mac:** open de lijst met profielen (_Systeeminstellingen → Algemeen → Apparaatbeheer_ op macOS 15 en later, _Systeeminstellingen → Privacy & beveiliging → Profielen_ op macOS 13 en 14, _Systeemvoorkeuren → Profielen_ op macOS 12 en eerder), selecteer het Mullvad DNS-profiel en klik op _−_.

Installeer vervolgens het Blokada-profiel via de [Apple-handleiding](../apple-devices/).

### Browsers

Als je een Mullvad DoH-link hebt ingevuld zoals `https://adblock.dns.mullvad.net/dns-query` onder _secure DNS_ of _DNS over HTTPS_, vervang deze dan door je DoH-link. De [browser handleiding](../browser-dns-over-https/) beschrijft de stappen voor elke browser.

### Router

Als je router Mullvad gebruikt via DNS over TLS, vervang dan de Mullvad-hostnaam door je Blokada DNS-naam en verwijder de IP-adressen van Mullvad. De [router handleiding](../router-ad-blocking/) behandelt veelvoorkomende modellen.

## Controleer of het werkt

Open een paar websites en kijk dan op de pagina _Activiteit_ in het dashboard. Je ziet daar de zoekopdrachten van je apparaten, waarbij geblokkeerde duidelijk zijn gemarkeerd. Zie je een apparaat niet, dan gebruikt het nog een andere DNS-server.
