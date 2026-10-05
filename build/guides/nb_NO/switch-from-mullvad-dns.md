---
title: Mullvad DNS legges ned. Behold annonseblokkering med Blokada Cloud.
description: Mullvad stenger sin offentlige DNS 2. november 2026. Slik bytter du telefon, datamaskin og ruter til Blokada Cloud før denne datoen, uten å miste annonseblokkering.
updated: 2026-10-02
order: 2
---

Mullvad stenger sin gratis, offentlige DNS-tjeneste **2. november 2026** og anbefaler Quad9 i stedet. Quad9 blokkerer skadevare, men blokkerer **ikke** annonser eller sporere. Når Mullvads DNS stopper, vil enheter satt til den slutte å laste nettsteder og apper. Der en enhet får falle tilbake til en annen DNS-tjener, vil annonser komme tilbake. Bytt før denne datoen.

Denne siden gjelder de offentlige DNS-navnene som slutter på `dns.mullvad.net`. Den dekker ikke Mullvad VPN-appen.

## Hva du brukte, og hva du skal velge i Blokada

| Mullvad DNS-navn           | Hva den blokkerte                           | I Blokada-dashboardet                                                                                                                                  |
| -------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `dns.mullvad.net`          | ingenting                                   | Blokada er en filtreringstjeneste. Hvis du ikke ønsker filtrering, er Quad9 eller din leverandørs DNS et enklere valg. |
| `adblock.dns.mullvad.net`  | annonser, sporere                           | en blokk-liste for annonser og sporere                                                                                                                 |
| `base.dns.mullvad.net`     | annonser, sporere, skadevare                | legg til en skadevare-liste                                                                                                                            |
| `extended.dns.mullvad.net` | base pluss sosiale medier                   | legg til en liste for sosiale medier                                                                                                                   |
| `family.dns.mullvad.net`   | base pluss innhold for voksne og pengespill | legg til lister for innhold for voksne og pengespill                                                                                                   |
| `all.dns.mullvad.net`      | alle ovenfor                                | aktiver alle sammen                                                                                                                                    |

Du velger blokkeringslister i dashbordet under _Blocklists_. Du kan endre disse når som helst, og endringen gjelder for alle enhetene dine.

## Bytt hver enhet

Blokada gir hver enhet sitt eget navn, slik at dashbordet kan vise aktivitet per enhet. Avhengig av enheten trenger du ditt DNS-navn eller DoH-link, begge under _Dine detaljer_ over.

### Android

Mullvads veiledning ba deg oppgi et vertsnavn under _Privat DNS_. Bytt det ut med ditt Blokada DNS-navn. [Android-veiledningen](../android-private-dns/) viser trinnene.

### iPhone, iPad og Mac

Mullvads oppsett brukte en konfigurasjonsprofil. Fjern den først:

- **iPhone og iPad:** _Innstillinger → Generelt → VPN og Enhetsadministrasjon_, trykk på Mullvad DNS-profilen, deretter _Fjern profil_.
- **Mac:** åpne listen over profiler (_Systeminnstillinger → Generelt → Enhetsadministrasjon_ på macOS 15 og nyere, _Systeminnstillinger → Personvern og sikkerhet → Profiler_ på macOS 13 og 14, _Systemvalg → Profiler_ på macOS 12 og tidligere), velg Mullvad DNS-profilen og klikk _−_.

Installer deretter Blokada-profilen fra [Apple-veiledningen](../apple-devices/).

### Nettlesere

Hvis du la inn en Mullvad DoH-link som `https://adblock.dns.mullvad.net/dns-query` under _Sikker DNS_ eller _DNS over HTTPS_, bytt den ut med din DoH-link. [Nettleserveiledningen](../browser-dns-over-https/) har trinnene for hver nettleser.

### Ruter

Hvis ruteren din bruker Mullvad over DNS over TLS, bytt ut Mullvad-vertsnavnet med ditt Blokada DNS-navn, og fjern Mullvads IP-adresser. [Ruter-veiledningen](../router-ad-blocking/) dekker vanlige modeller.

## Sjekk at det virker

Åpne noen nettsteder, og se deretter på siden _Aktivitet_ i dashbordet. Du ser dine enheters oppslag der, med blokkerte markert. Hvis en enhet ikke vises, bruker den fortsatt en annen DNS-tjener.
