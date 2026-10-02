---
title: Mullvad DNS wordt stopgezet. Behoud je advertentieblokkering met Blokada Cloud
description: Mullvad sluit zijn openbare DNS op 2 november 2026. Hier lees je hoe je je telefoon, computer en router vóór die datum naar Blokada Cloud kunt overzetten, zonder je advertentieblokkering te verliezen.
updated: 2026-10-02
order: 2
---

Mullvad stopt zijn gratis openbare DNS-dienst op **2 november 2026** en raadt Quad9 aan als alternatief. Quad9 blokkeert malware, maar blokkeert **geen** advertenties of trackers. Wanneer de DNS van Mullvad stopt, zullen apparaten die hierop zijn ingesteld geen websites en apps meer laden. Als een apparaat kan terugvallen op een andere DNS-server, komen advertenties terug. Schakel vóór die datum over.

Deze pagina gaat over de openbare DNS-namen die eindigen op `dns.mullvad.net`. Het gaat niet over de Mullvad VPN-app.

## Wat je gebruikte en wat je moet kiezen in Blokada

| Mullvad DNS naam           | Wat het blokkeerde                           | In het Blokada-dashboard                                                                                                                             |
| -------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | niets                                        | Blokada is een filterdienst. Als je geen filtering wilt, zijn Quad9 of de DNS van je provider de eenvoudigste keuze. |
| `adblock.dns.mullvad.net`  | advertenties, trackers                       | een advertentie- en tracker-blokkeerlijst                                                                                                            |
| `base.dns.mullvad.net`     | advertenties, trackers, malware              | voeg een malwarelijst toe                                                                                                                            |
| `extended.dns.mullvad.net` | basis plus sociale media                     | voeg een sociale-medialijst toe                                                                                                                      |
| `family.dns.mullvad.net`   | basis plus inhoud voor volwassenen en gokken | voeg lijsten voor volwassenen en gokken toe                                                                                                          |
| `all.dns.mullvad.net`      | al het bovenstaande                          | zet ze allemaal aan                                                                                                                                  |

Je kiest blokkeerlijsten in het dashboard onder _Blokkeerlijsten_. Je kunt ze op elk moment wijzigen, en de wijziging geldt voor al je apparaten.

## Schakel elk apparaat over

Blokada geeft elk apparaat een eigen naam, zodat het dashboard activiteit per apparaat kan weergeven. Afhankelijk van het apparaat heb je je DNS-naam of je DoH-link nodig, beide te vinden onder _Je gegevens_ hierboven.

### Android

De handleiding van Mullvad liet je een hostnaam invullen onder _Privé-DNS_. Vervang deze door je Blokada DNS-naam. De [Android-handleiding](../android-private-dns/) geeft de stappen.

### iPhone, iPad en Mac

De Mullvad-instructie gebruikte een configuratieprofiel. Verwijder het eerst:

- **iPhone en iPad:** _Instellingen → Algemeen → VPN & apparaatbeheer_, tik op het Mullvad DNS-profiel en kies vervolgens _Verwijder profiel_.
- **Mac:** open de lijst met profielen (_Systeeminstellingen → Algemeen → Apparaatbeheer_ op macOS 15 en later, _Systeeminstellingen → Privacy & beveiliging → Profielen_ op macOS 13 en 14, _Systeemvoorkeuren → Profielen_ op macOS 12 en eerder), selecteer het Mullvad DNS-profiel en klik op _−_.

Installeer vervolgens het Blokada-profiel via de [Apple-handleiding](../apple-devices/).

### Browsers

Als je een Mullvad DoH-link hebt ingevoerd zoals `https://adblock.dns.mullvad.net/dns-query` onder _beveiligde DNS_ of _DNS over HTTPS_, vervang die dan door je eigen DoH-link. De [browser-handleiding](../browser-dns-over-https/) noemt de stappen voor elke browser.

### Router

Als je router Mullvad over DNS over TLS gebruikt, vervang dan de Mullvad-hostnaam door je Blokada DNS-naam en verwijder de IP-adressen van Mullvad. De [router-handleiding](../router-ad-blocking/) behandelt veelgebruikte modellen.

## Controleer of het werkt

Open een aantal websites en kijk vervolgens op de pagina _Activiteit_ in het dashboard. Je ziet daar de opvragingen van je apparaten, waarbij geblokkeerde gemarkeerd zijn. Als een apparaat niet verschijnt, gebruikt het nog een andere DNS-server.
