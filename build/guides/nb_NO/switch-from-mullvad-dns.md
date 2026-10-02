---
title: Mullvad DNS legges ned. Behold annonseblokkering med Blokada Cloud
description: Mullvad stenger sin offentlige DNS 2. november 2026. Her ser du hvordan du flytter telefon, datamaskin og ruter til Blokada Cloud innen den tid, uten å miste annonseblokkering.
updated: 2026-10-02
order: 2
---

Mullvad legger ned sin gratis, offentlige DNS-tjeneste **2. november 2026** og anbefaler Quad9 i stedet. Quad9 blokkerer skadevare men blokkerer **ikke** annonser eller sporere. Når Mullvads DNS stopper, slutter enheter satt opp til den å laste inn nettsteder og apper. Hvis en enhet får lov til å falle tilbake til en annen DNS-server, kommer annonser tilbake i stedet. Bytt før den datoen.

Denne siden handler om offentlige DNS-navn som slutter med `dns.mullvad.net`. Den gjelder ikke Mullvad VPN-appen.

## Hva du brukte, og hva du skal velge i Blokada

| Mullvad DNS-navn           | Hva den blokkerte                           | I Blokada-dashboardet                                                                                                                                      |
| -------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | ingenting                                   | Blokada er en filtreringstjeneste. Hvis du ikke vil ha filtrering, er Quad9 eller din leverandørs DNS det enkleste valget. |
| `adblock.dns.mullvad.net`  | annonser, sporere                           | en blokk-liste for annonser og sporere                                                                                                                     |
| `base.dns.mullvad.net`     | annonser, sporere, skadevare                | legg til en skadevare-liste                                                                                                                                |
| `extended.dns.mullvad.net` | base pluss sosiale medier                   | legg til en liste for sosiale medier                                                                                                                       |
| `family.dns.mullvad.net`   | base pluss innhold for voksne og pengespill | legg til lister for innhold for voksne og pengespill                                                                                                       |
| `all.dns.mullvad.net`      | alle ovenfor                                | aktiver alle sammen                                                                                                                                        |

Du velger blokk-lister i dashboardet under _Blokk-lister_. Du kan endre dem når som helst, og endringen gjelder for alle enhetene dine.

## Bytt hver enhet

Blokada gir hver enhet sitt eget navn, slik at dashbordet kan vise aktivitet per enhet. Avhengig av enheten trenger du enten DNS-navnet ditt eller DoH-lenken din, begge under _Dine detaljer_ ovenfor.

### Android

Mullvads veiledning fikk deg til å legge inn et vertsnavn under _Privat DNS_. Bytt det ut med ditt Blokada DNS-navn. [Android-veiledningen](../android-private-dns/) viser stegene.

### iPhone, iPad og Mac

Mullvads oppsett brukte en konfigurasjonsprofil. Fjern den først:

- **iPhone og iPad:** _Innstillinger → Generelt → VPN og Enhetsadministrasjon_, trykk på Mullvad DNS-profilen, deretter _Fjern profil_.
- **Mac:** åpne listen over profiler (_Systeminnstillinger → Generelt → Enhetsadministrasjon_ på macOS 15 og nyere, _Systeminnstillinger → Personvern og sikkerhet → Profiler_ på macOS 13 og 14, _Systemvalg → Profiler_ på macOS 12 og tidligere), velg Mullvad DNS-profilen og klikk _−_.

Installer deretter Blokada-profilen fra [Apple-veiledningen](../apple-devices/).

### Nettlesere

Hvis du la inn en Mullvad DoH-lenke som `https://adblock.dns.mullvad.net/dns-query` under _sikker DNS_ eller _DNS over HTTPS_, erstatt den med din DoH-lenke. [Nettleser-veiledningen](../browser-dns-over-https/) har stegene for hver nettleser.

### Ruter

Hvis ruteren din bruker Mullvad over DNS over TLS, bytt ut Mullvad-vertsnavnet med ditt Blokada DNS-navn, og fjern Mullvads IP-adresser. [Ruter-veiledningen](../router-ad-blocking/) dekker vanlige modeller.

## Sjekk at det virker

Åpne noen nettsteder, og se deretter på _Aktivitet_-siden i dashboardet. Du ser dine enheters oppslag der, med blokkerte markert. Hvis en enhet ikke vises, bruker den fortsatt en annen DNS-server.
