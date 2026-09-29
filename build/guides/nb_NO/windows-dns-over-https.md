---
title: Blokér annonser på Windows med DNS over HTTPS
description: Bruk den innebygde krypterte DNS-funksjonen i Windows 11 med Blokada Cloud for å blokere annonser og sporere i alle apper og nettlesere, helt uten å installere ekstra programvare.
updated: 2026-09-28
order: 8
---

Windows 11 kan sende alle sine DNS-oppslag kryptert, via DNS over HTTPS. Pek den mot Blokada Cloud, og annonser og sporere blokkeres i alle apper og nettlesere på datamaskinen, uten noe å installere.

Du trenger to verdier:

- DNS-server (IP-adresse): {% ip "doh" %}
- Din DoH-lenke: {% doh %}

## Windows 11

1. Åpne _Innstillinger → Nettverk og internett_, deretter _Wi-Fi_ eller _Ethernet_, avhengig av hvordan datamaskinen er tilkoblet.
2. Åpne tilkoblingens _Maskinvareegenskaper_. For Wi-Fi, velg _Administrer kjente nettverk_ og deretter nettverket, eller _Maskinvareegenskaper_ øverst på Wi-Fi-siden.
3. Ved siden av _DNS-servertilordning_, velg _Rediger_. Velg _Manuell_ og slå på _IPv4_.
4. I _Foretrukket DNS_, skriv inn DNS-serveren {% ip "doh" %}
5. Sett _DNS over HTTPS_ til _På (manuell mal)_, og lim inn din DoH-lenke {% doh %} som _DoH-mal_.
6. Slå av _Tilbakefall til klartekst_, og velg _Lagre_.

Hvis datamaskinen bruker både Wi-Fi og Ethernet, gjenta dette for den andre tilkoblingen.

<div class="note">

La _Alternativ DNS_ stå tom. Windows bruker begge serverne, og enhver annen slipper gjennom annonser.

Ingen _På (manuell mal)_-valg? Din Windows 11 er eldre. Oppdater Windows, eller bruk [nettleserguiden](../browser-dns-over-https/) i mellomtiden.

Hvis noen annonser fortsatt slipper gjennom på et nettverk med IPv6, kan det hende Windows også spør om IPv6-DNS-serveren på ruteren din. Slå av _Internet Protocol Version 6 (TCP/IPv6)_ i adapterens egenskaper (_Kontrollpanel → Nettverkstilkoblinger_), eller konfigurer [ruteren](../router-ad-blocking/).

</div>

## Windows 10

Windows 10 har ikke innebygd kryptert DNS. Konfigurer sikker DNS i nettleseren din i stedet, som i [nettleserguiden](../browser-dns-over-https/), eller konfigurer [ruteren](../router-ad-blocking/) for å dekke hele hjemmet.

## Sjekk at det fungerer

Åpne noen nettsider, og se deretter på _Aktivitet_-siden i [dashbordet](https://app.blokada.org/stats?src=guides). Denne datamaskinens oppslag vises der.

Nettlesere med egen _sikker DNS_-innstilling omgår Windows. I Chrome og Edge, sett det til å bruke nåværende tjenesteleverandør eller din DoH-lenke.

<div class="note">

Ønsker du også VPN på denne datamaskinen? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) inkluderer en WireGuard-konfigurasjon som krypterer all trafikk, med samme blokkering.

</div>
