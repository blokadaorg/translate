---
title: Sett opp Privat DNS på Android med Blokada Cloud
description: Bruk Androids innebygde Privat DNS-innstilling med Blokada Cloud for å blokkere annonser og sporere i alle apper, både på Wi-Fi og mobildata. Eller la Blokada 6-appen gjøre det.
updated: 2026-09-28
order: 5
---

## Den enkleste metoden: appen

[Blokada 6](https://go.blokada.org/play_cloud) setter opp alt for deg, slår blokkeringen av og på med ett trykk, og viser hva som er blokkert direkte på telefonen. Logg inn med din konto-ID og du er ferdig.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Last ned Blokada 6 fra Google Play</a></p>

## Uten appen: Privat DNS

Android 9 og nyere har en innstilling for <i>Privat DNS</i>. Sett denne til Blokada Cloud, og annonser og sporere blokkeres i alle apper, på alle nettverk, uten noe som kjører i bakgrunnen.

Ditt Blokada DNS-navn: {% dot %}

1. Åpne <i>Innstillinger → Nettverk og internett</i>. På noen telefoner heter dette <i>Tilkoblinger</i> eller <i>Tilkobling og deling</i>.
2. Trykk på <i>Privat DNS</i>. På Samsung-telefoner finner du det under <i>Mer tilkoblingsinnstillinger</i>.
3. Velg <i>Privat DNS-leverandørs vertsnavn</i>.
4. Skriv inn ditt Blokada DNS-navn {% dot %} og trykk på <i>Lagre</i>.

Hvis du ikke finner det, søk i Innstillinger-appen etter "Privat DNS".

## Sjekk at det fungerer

Åpne noen apper eller nettsider, og se deretter på <i>Aktivitet</i>-siden i <a href="https://app.blokada.org/stats?src=guides">dashbordet</a>. Denne telefonens oppslag vil vises der.

## Hvis noe ikke fungerer

- <b>"Kunne ikke koble til" eller ingen internett:</b> sjekk ditt Blokada DNS-navn for skrivefeil. Det må være nøyaktig som vist ovenfor, uten `https://`.
- <b>En annen VPN-app er aktiv:</b> noen VPN-apper bruker egen DNS og omgår Privat DNS. Skru av VPN-appens DNS-innstillinger eller reklameblokkering, eller bruk Blokada 6 i stedet.
- <b>Chrome viser fortsatt annonser:</b> åpne <i>Innstillinger → Personvern og sikkerhet → Bruk sikker DNS</i> i Chrome, og velg <i>Bruk gjeldende tjenesteleverandør</i>.
