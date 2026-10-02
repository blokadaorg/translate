---
title: Blokker annonser i Chrome, Firefox, Edge og Brave med DNS over HTTPS
description: Sett Blokada Cloud som sikker DNS-leverandør i nettleseren din for å blokkere annonser og sporere, på enhver datamaskin, inkludert jobb-PCer hvor du ikke kan installere apper.
updated: 2026-10-02
order: 7
---

Moderne nettlesere kan bruke sin egen krypterte DNS-leverandør, kalt _sikker DNS_ eller _DNS over HTTPS_. Sett den til Blokada Cloud, og nettleseren blokkerer annonser og sporere på alle nettverk, uten at du trenger å installere utvidelser.

Denne innstillingen gjelder bare for denne nettleseren. For å dekke hele datamaskinen, bruk [Apple-profilen](../apple-devices/) på Mac, eller konfigurer [ruteren](../router-ad-blocking/).

## Chrome

1. Åpne `chrome://settings/security`.
2. Slå på _Bruk sikker DNS_, og velg deretter _Legg til egendefinert DNS-leverandør_.
3. Skriv inn {% doh %}

## Edge

1. Åpne `edge://settings/privacy`.
2. Under _Sikkerhet_, slå på _Bruk sikker DNS for å angi hvordan nettverksadresser for nettsteder skal slås opp_.
3. Velg _Velg en leverandør_ og skriv inn {% doh %}

## Firefox

1. Åpne _Innstillinger → Personvern og sikkerhet_ og bla til _DNS over HTTPS_.
2. Velg _Maks beskyttelse_.
3. Under _Velg leverandør_, velg _Egendefinert_ og skriv inn {% doh %}

## Brave

1. Åpne `brave://settings/security`.
2. Slå på _Bruk sikker DNS_, og velg deretter _Legg til egendefinert DNS-leverandør_.
3. Skriv inn {% doh %}

## Safari

Safari har ingen egen innstilling for sikker DNS. Den bruker systemets DNS, så installer [Apple-profilen](../apple-devices/).

## Sjekk at det fungerer

Bla i et minutt, og åpne så _Aktivitet_-siden i [dashbordet](https://app.blokada.org/stats?src=guides). Denne nettleserens oppslag vises der.

## Hvis noe ikke fungerer

<div class="note tip">

Hvis nettleseren din administreres av jobben eller skolen, kan innstillingen for sikker DNS være låst. Spør administratoren din.

</div>
