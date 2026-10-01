---
title: Et NextDNS-alternativ med samme oppsett på alle enheter
description: Bytt fra NextDNS til Blokada Cloud. Bytt ut NextDNS DNS-navnet, DoH-lenken eller profilen din med Blokadas på telefonen, datamaskinen og ruteren, og behold annonseblokkeringen.
updated: 2026-09-23
order: 3
---

NextDNS og Blokada Cloud fungerer på samme måte: en kryptert DNS-tjeneste som blokkerer annonser og sporere ved navn, med dine egne innstillinger bak et personlig DNS-navn. Å bytte betyr å erstatte NextDNS-verdiene på hver enhet med dine Blokada-verdier. Ingenting annet på enheten endres.

## Hva du brukte, og hva du skal velge i Blokada

| I NextDNS                                                                 | I Blokada Cloud                                                    |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Konfigurasjons-ID-en din, f.eks. `abc123` | Enhetstagen din, del av Blokada DNS-navnet ditt og DoH-lenken      |
| _Personvern_-blokklister                                                  | _Blokklister_ i dashbordet                                         |
| _Sikkerhet_ (skadelig programvare, phishing)           | en skadelig programvare-liste under _Blokklister_                  |
| _Foreldrekontroll_                                                        | innholdsfilter for vokseninnhold og pengespill under _Blokklister_ |
| _Tillatelsesliste_ og _Blokkeringsliste_                                  | _Unntak_ i dashbordet                                              |
| _Logger_ og _Analyse_                                                     | _Aktivitet_ og _Statistikk_ i dashbordet                           |

## Dine Blokada-detaljer

- Ditt Blokada DNS-navn, for DNS over TLS: {% dot %}
- Din DoH-lenke, for DNS over HTTPS: {% doh %}

## Bytt hver enhet

### Android

Hvis du brukte _Privat DNS_ med `<your-id>.dns.nextdns.io`, bytt det ut med ditt Blokada DNS-navn, som i [Android-veiledningen](../android-private-dns/). Hvis du brukte NextDNS-appen, avinstaller den og installer [Blokada 6](https://go.blokada.org/play_cloud) i stedet.

### iPhone og iPad

Hvis du brukte NextDNS-appen, avinstaller den og installer [Blokada 6](https://go.blokada.org/appstore). Hvis du i stedet installerte en NextDNS-profil, fjern den under _Innstillinger → Generelt → VPN og enhetsadministrasjon_, og følg deretter [Apple-veiledningen](../apple-devices/).

### Mac og Apple TV

Fjern NextDNS-profilen eller appen, og installer deretter Blokada-profilen fra [Apple-veiledningen](../apple-devices/).

### Windows og Linux

Avinstaller NextDNS-appen hvis du bruker den. På Windows, erstatt NextDNS-serveren og DoH-malen med Blokadas, som i [Windows-veiledningen](../windows-dns-over-https/). På Linux, bytt ut NextDNS-serveren i systemd-resolved, som i [Linux-veiledningen](../linux-dns-over-tls/).

### Nettlesere

Hvis du har satt `https://dns.nextdns.io/…` som _sikker DNS_ i nettleseren din, bytt den ut med DoH-lenken din, som i [nettleser-veiledningen](../browser-dns-over-https/).

### Ruter

Hvis ruteren din bruker NextDNS via DNS over TLS eller DNS over HTTPS, bytt ut NextDNS-navnet eller lenken med din Blokada, som i [ruter-veiledningen](../router-ad-blocking/).

Hvis den bruker NextDNS via vanlige IP-adresser med en _tilkoblet IP_, kan Blokada foreløpig ikke overta det. Støtte for rutere med vanlige DNS-adresser er på vei. Inntil da, konfigurer enhetene dine én etter én, eller bruk en ruter som støtter kryptert DNS.

## Sjekk at det fungerer

Åpne noen nettsteder, og se deretter på _Aktivitet_-siden i dashbordet. Du ser oppslagene til enhetene dine der, med blokkerte markert. Hvis en enhet ikke vises der, bruker den fortsatt NextDNS.
