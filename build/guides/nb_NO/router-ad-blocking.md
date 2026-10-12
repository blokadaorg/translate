---
title: Blokker annonser på hele nettverket ditt med rutermodus for annonseblokkering
description: Sett opp Blokada Cloud på ruteren din én gang, og alle enheter hjemme er beskyttet, inkludert TV-er, spillkonsoller og smarte høyttalere som ikke kan kjøre en annonseblokker.
updated: 2026-10-09
order: 4
---

Hver enhet på nettverket ditt spør ruteren hvilken DNS-server som skal brukes. Pek ruteren mot Blokada Cloud, og annonser og sporere blir blokkert for alt bak den. Dette inkluderer smart-TVer, spillkonsoller, strømmeenheter og smarthus-enheter, som ikke har plass til en annonseblokkeringsapp.

## Dette trenger ruteren din

Det finnes to måter å sette opp en ruter på:

- **Kryptert DNS med vertsnavn**, det vil si DNS over TLS (DoT) eller DNS over HTTPS (DoH). Mange nyere rutere støtter dette, inkludert modellene nedenfor. Avhengig av hva ruteren din støtter, trenger du ditt DNS-navn eller din DoH-lenke, begge finner du under _Dine detaljer_ ovenfor.
- **En ren IPv6 DNS-adresse.** Mange rutere fra internettleverandører aksepterer bare rene IP-adresser for DNS. Hvis din gjør det og forbindelsen har IPv6, gir Blokada deg en IPv6-adresse du kan skrive inn. Se [Rutere som kun tar en IP-adresse](#routers-that-only-take-an-ip-address).

Bruk kryptert DNS hvis ruteren din støtter det. Oppslag forblir private på vei til Blokada.

## FRITZ!Box

FRITZ!OS 7.20 eller nyere.

1. Åpne `http://fritz.box` og gå til _Internett → Kontoinformasjon → DNS-server_.
2. Under _Kryptert navneoppløsning på Internett (DNS over TLS)_, huk av for _Bruk kryptert navneoppløsning_.
3. I _Oppløste navn for DNS-serveren_, skriv inn kun {% dot %}. **Fjern alle andre oppføringer.** FRITZ!Box bruker alle listede resolverne, og enhver annen vil slippe inn annonser.
4. Fjern avhuking for _Tillat fallback til ukryptert navneoppløsning_.
5. Hvis du ser _Overgang til offentlige DNS-servere ved DNS-avbrudd_, slå det av.
6. Klikk på _Bruk_.

## ASUS

Nyere ASUS-fastvare (3.0.0.4.388 eller nyere) og Asuswrt-Merlin.

1. Åpne ruterens administrasjonsside og gå til _WAN → Internettforbindelse_.
2. Under _WAN DNS-innstilling_, sett _DNS Privacy Protocol_ til _DNS-over-TLS (DoT)_ og _DNS-over-TLS-profil_ til _Strict_.
3. Fjern alle oppføringer fra _DNS-over-TLS-serverliste_, og legg deretter til én:
   - Adresse: {% ip "dot" %}
   - TLS-vertsnavn: {% dot %}
4. Klikk på _Bruk_.

## OpenWrt

1. I _System → Programvare_, oppdater listene og installer `luci-app-https-dns-proxy`.
2. Åpne _Tjenester → HTTPS DNS Proxy_. Slett instansene for andre tilbydere.
3. Legg til en instans med egendefinert resolver-URL: {% doh %}
4. _Lagre og bruk_. Pakken peker dnsmasq mot den automatisk.

## Andre rutere

Se etter en innstilling kalt _DNS over TLS_, _Privat DNS_, _Kryptert DNS_ eller _DNS over HTTPS_. Skriv inn Blokada DNS-navnet ditt eller DoH-lenken fra ovenfor, og fjern alle andre DNS-servere, inkludert reserve-servere. Hvis det ikke finnes en slik innstilling, bruk en enkel IPv6-adresse som nedenfor.

## Rutere som kun godtar en IP-adresse {:#routers-that-only-take-an-ip-address}

Ruteren din og internettforbindelsen din må støtte IPv6 for dette. Støtte for rene IPv4-adresser kommer senere.

1. I [dashboardet](https://app.blokada.org/setup?src=guides), åpne _Oppsett_ og velg _Ruter, TV, spillkonsoll_.
2. Gi ruteren et navn, for eksempel _Hjemmeruter_, og velg _Hent adresse_. Navnet vises i aktiviteten din og kan ikke endres senere.
3. I ruterens innstillinger, finn DNS-serverne for IPv6, ofte under _Internett_, _WAN_ eller _IPv6_, og skriv inn adressen som den eneste DNS-serveren.
4. **Fjern alle andre DNS-servere, også de for IPv4.** Enheter som fortsatt får en IPv4 DNS-server fra ruteren sender noen oppslag utenom Blokada. Hvis ruteren ikke kan la feltet for IPv4 DNS stå tomt, må du sette opp enhetene dine én og én i stedet: [Android](../android-private-dns/), [Mac og Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) og [nettlesere](../browser-dns-over-https/).

Det samme oppsettet fungerer for en TV eller spillkonsoll som lar deg skrive inn en DNS-server manuelt. Gi hver enhet sin egen adresse, slik at den vises med navn i din aktivitet.

<div class="note aside">

Disse oppslagene sendes ukryptert til Blokada, akkurat som med en vanlig DNS-server. Hvis ruteren din støtter DNS over TLS eller DNS over HTTPS, bruk det i stedet.

</div>

## Sjekk at det fungerer

1. Start én enhet på nytt, eller slå Wi-Fi av og på, slik at den henter inn endringen.
2. På den enheten, slå av Blokada hvis den kjører det, og åpne [go.blokada.org/test](https://go.blokada.org/test). Der kan du se om DNS-trafikken din går gjennom Blokada.
3. Surf i et minutt, og åpne deretter _Aktivitet_-siden i [dashboardet](https://app.blokada.org/stats?src=guides). Nettverkets oppslag vises der.

## Hvis noen enheter fortsatt viser annonser

Noen enheter omgår ruteren: telefoner med _Privat DNS_ aktivert, nettlesere med _sikker DNS_ satt til en annen tilbyder, og enheter som har hardkodet sin egen DNS. Sett opp disse direkte på enheten, eller slå av egen DNS-innstilling.

<div class="note tip">

Bak ruteren deler alle enheter én adresse, så dashbordet viser nettverket ditt som én enhet. Sett opp telefoner og bærbare med egne Blokada DNS-navn hvis du vil se dem hver for seg. De beholder også blokkeringen når de forlater hjemmet.

</div>
