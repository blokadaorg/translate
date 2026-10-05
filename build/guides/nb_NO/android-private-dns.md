---
title: Sett opp Privat DNS på Android med Blokada Cloud
description: Bruk Androids innebygde funksjon for Privat DNS med Blokada Cloud for å blokkere annonser og sporere i alle apper, både på Wi-Fi og mobildata. Eller la Blokada 6-appen gjøre det for deg.
updated: 02.10.2026
order: 5
---

## Den enkleste metoden: appen

[Blokada 6](https://go.blokada.org/play_cloud) setter opp alt for deg, slår blokkering av eller på med ett trykk, og viser hva som har blitt blokkert direkte på telefonen. Logg inn med din kontoinformasjon, så er du ferdig.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Last ned Blokada 6 fra Google Play</a></p>

## Uten appen: Privat DNS

Android 9 og nyere har en _Privat DNS_-innstilling. Sett den til Blokada Cloud, og annonser og sporere blir blokkert i alle apper, på alle nettverk, uten at noe kjører i bakgrunnen.

1. Åpne _Innstillinger → Nettverk og internett_. På noen telefoner heter det _Tilkoblinger_ eller _Tilkobling og deling_.
2. Trykk på _Privat DNS_. På Samsung-telefoner finner du det under _Flere tilkoblingsinnstillinger_.
3. Velg <i>Privat DNS-leverandørs vertsnavn</i>.
4. Skriv inn ditt Blokada DNS-navn {% dot %} og trykk på <i>Lagre</i>.

Hvis du ikke finner det, søk i Innstillinger-appen etter "Privat DNS".

## Sjekk at det fungerer

Åpne noen apper eller nettsider, og se deretter på _Aktivitet_-siden i [dashboardet](https://app.blokada.org/stats?src=guides). Denne telefonens oppslag vises der.

## Hvis noe ikke fungerer

- **"Kunne ikke koble til" eller ingen internett:** sjekk om ditt Blokada DNS-navn har skrivefeil. Det må være nøyaktig som vist over, uten `https://`.
- **En annen VPN-app er aktiv:** noen VPN-apper bruker egen DNS og omgår Privat DNS. Slå av VPN-appens DNS- eller annonseblokkeringsinnstilling, eller bruk Blokada 6 i stedet.
- **Chrome viser fortsatt annonser:** Chrome kan være satt til sin egen sikre DNS-leverandør, som omgår Privat DNS. Åpne _Innstillinger → Personvern og sikkerhet → Bruk sikker DNS_ i Chrome og velg _Bruk din nåværende tjenesteleverandør_. Da følger Chrome Privat DNS.
