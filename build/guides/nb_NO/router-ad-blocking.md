---
title: Blokker annonser på hele nettverket ditt med rutermodus for annonseblokkering
description: Sett opp Blokada Cloud på ruteren din én gang, og alle enheter hjemme er beskyttet, inkludert TV-er, spillkonsoller og smarte høyttalere som ikke kan kjøre en annonseblokker.
updated: 2026-10-02
order: 4
---

Hver enhet på nettverket ditt spør ruteren hvilken DNS-server som skal brukes. Pek ruteren mot Blokada Cloud, og annonser og sporere blir blokkert for alt bak den. Dette inkluderer smart-TVer, spillkonsoller, strømmeenheter og smarthus-enheter, som ikke har plass til en annonseblokkeringsapp.

## Dette trenger ruteren din

Ruteren din må støtte **kryptert DNS med vertsnavn**, altså DNS over TLS (DoT) eller DNS over HTTPS (DoH). Mange nyere rutere gjør det, inkludert modellene nedenfor. Avhengig av hva ruteren din støtter, trenger du enten DNS-navnet ditt eller DoH-lenken din, begge finner du under _Dine detaljer_ ovenfor.

<div class="note important">

**Kun vanlige IP-adresser?** Mange rutere fra internettleverandører godtar bare vanlige IP-adresser for DNS. Støtte for dette er på vei. Inntil da, sett opp enhetene dine én etter én: [Android](../android-private-dns/), [Mac og Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) og [nettlesere](../browser-dns-over-https/). Du kan også kjøre en liten videresender på en Raspberry Pi, som beskrevet i [Pi-hole-guiden](../switch-from-pihole/).

</div>

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

Se etter en innstilling som heter _DNS over TLS_, _Privat DNS_, _Kryptert DNS_ eller _DNS over HTTPS_. Skriv inn ditt Blokada DNS-navn eller DoH-lenke fra ovenfor, og fjern alle andre DNS-servere, inkludert reserve-servere.

## Sjekk at det fungerer

1. Start én enhet på nytt, eller slå Wi-Fi av og på, slik at den henter inn endringen.
2. Surf i ett minutt, og åpne deretter _Aktivitet_-siden i dashbordet. Forespørslene fra nettverket ditt vises der.

## Hvis noen enheter fortsatt viser annonser

Noen enheter omgår ruteren: telefoner med _Privat DNS_ aktivert, nettlesere med _sikker DNS_ satt til en annen tilbyder, og enheter som har hardkodet sin egen DNS. Sett opp disse direkte på enheten, eller slå av egen DNS-innstilling.

<div class="note tip">

Bak ruteren deler alle enheter én adresse, så dashbordet viser nettverket ditt som én enhet. Sett opp telefoner og bærbare med egne Blokada DNS-navn hvis du vil se dem hver for seg. De beholder også blokkeringen når de forlater hjemmet.

</div>
