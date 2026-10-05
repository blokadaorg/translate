---
title: Blokér annonser på Windows med DNS over HTTPS
description: Bruk den innebygde krypterte DNS-funksjonen i Windows 11 med Blokada Cloud for å blokere annonser og sporere i alle apper og nettlesere, helt uten å installere ekstra programvare.
updated: 02.10.2026
order: 8
---

Windows 11 kan sende alle sine DNS-oppslag kryptert, over DNS over HTTPS. Pek den til Blokada Cloud, og annonser og sporere blir blokkert i alle apper og nettlesere på datamaskinen, uten at du trenger å installere noe.

Du trenger DNS-serverens IP-adresse og din DoH-lenke, begge under _Dine detaljer_ ovenfor.

## Windows 11

1. Åpne _Innstillinger → Nettverk og internett_, deretter _Wi-Fi_ eller _Ethernet_, avhengig av hvordan datamaskinen er tilkoblet.
2. Åpne tilkoblingens _Maskinvareegenskaper_. For Wi-Fi, velg _Administrer kjente nettverk_ og deretter nettverket, eller _Maskinvareegenskaper_ øverst på Wi-Fi-siden.
3. Ved siden av _DNS-serveroppgave_, velg _Rediger_. Velg _Manuell_ og aktiver _IPv4_.
4. I _Foretrukket DNS_, skriv inn DNS-serveren {% ip "doh" %}
5. Sett _DNS over HTTPS_ til _På (manuell mal)_, og lim inn din DoH-lenke {% doh %} som _DoH-mal_.
6. Slå av _Tilbakefall til klartekst_, og velg _Lagre_.

Hvis datamaskinen bruker både Wi-Fi og Ethernet, gjenta dette for den andre tilkoblingen.

<div class="note important">

La _Alternativ DNS_ stå tom. Windows bruker begge serverne, og enhver annen slipper annonser gjennom.

</div>

<div class="note tip">

Ingen _På (manuelt mal)_-alternativ? Windows 11-en din er eldre. Oppdater Windows, eller bruk [nettleserguiden](../browser-dns-over-https/) i mellomtiden.

</div>

## Windows 10

Windows 10 har ikke innebygd kryptert DNS. Konfigurer sikker DNS i nettleseren din, som i [nettleserguiden](../browser-dns-over-https/), eller konfigurer [ruteren](../router-ad-blocking/) for å dekke hele hjemmet.

## Sjekk at det fungerer

Åpne noen nettsteder, og se deretter på _Aktivitet_-siden i [dashbordet](https://app.blokada.org/stats?src=guides). Denne datamaskinens oppslag vises der.

<div class="note aside">

Vil du ha VPN på denne datamaskinen også? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) inkluderer en WireGuard-oppsett som krypterer all trafikk, med samme blokkering.

</div>

## Hvis noe ikke fungerer

Chrome og Edge har egne _sikre DNS_-innstillinger, som omgår Windows. Hvis det står på automatisk, kan det falle tilbake til vanlig DNS, noe Blokada nekter. Sett den til din DoH-lenke i stedet:

- **Chrome:** åpne `chrome://settings/security`, slå på _Bruk sikker DNS_, og under _Velg DNS-leverandør_ velg _Legg til egendefinert DNS-tjenesteleverandør_.
- **Edge:** åpne `edge://settings/privacy`, slå på sikker DNS, og velg _Velg en tjenesteleverandør_.

Lim så inn din DoH-lenke {% doh %}

Hvis noen annonser fortsatt slipper gjennom på et nettverk med IPv6, kan det være at Windows også spør ruterens IPv6 DNS-server. Slå av _Internet Protocol Version 6 (TCP/IPv6)_ i adapterens egenskaper (_Kontrollpanel → Nettverkstilkoblinger_), eller konfigurer [ruteren](../router-ad-blocking/).
