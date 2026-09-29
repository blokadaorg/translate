---
title: Blokér annonser på Mac og Apple TV med en Blokada DNS-profil
description: Installer en Blokada Cloud DNS-profil for å blokere annonser og sporere på tvers av hele systemet på Mac eller Apple TV, med kryptert DNS og ingenting som kjører i bakgrunnen.
updated: 2026-09-28
order: 6
---

Apple-enheter kan bruke kryptert DNS for hele systemet via en konfigurasjonsprofil. Blokada-profilen peker enheten mot Blokada Cloud, som blokkerer annonser og sporere i alle apper og nettlesere.

Den fungerer på macOS 11 (Big Sur), tvOS 14, iOS og iPadOS 14 og nyere.

<div class="if-no-device">

Denne siden kjenner ikke enheten din ennå, så den kan ikke tilby profilen din. Logg inn på dashbordet, åpne _Oppsett_, velg enheten din, og åpne denne veiledningen med _Åpne på en annen enhet_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Hent min profillink</a></p>

</div>

## iPhone og iPad

Den enkleste måten er appen. [Blokada 6](https://go.blokada.org/appstore) setter opp alt for deg, slår blokkering av og på med ett trykk, og viser hva som er blokkert på telefonen. Logg inn med din konto-ID, så er du ferdig.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Få Blokada 6 i App Store</a></p>

### Uten appen

Du kan installere profilen i stedet. iPhone og iPad installerer profiler kun fra **Safari**.

<div class="if-device">
<div class="if-other-browser note">

Denne siden er åpen i en annen nettleser. Kopier lenken din og åpne den i Safari for å fortsette der: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. I Safari trykker du på knappen under, og deretter _Tillat_ for å laste ned profilen.
2. Åpne _Innstillinger_. Trykk på _Profil lastet ned_ øverst. Du finner den også under _Generelt → VPN og enhetsadministrasjon_.
3. Trykk på _Installer_, skriv inn din kode og bekreft.

</div>

<p class="if-device if-safari">{% appleProfile %}Last ned min profil{% endappleProfile %}</p>

## Mac

1. Klikk på knappen under for å laste ned profilen.
2. Åpne listen over profiler: _Systeminnstillinger → Generelt → Enhetsadministrasjon_ på macOS 15 og nyere, _Systeminnstillinger → Personvern og sikkerhet → Profiler_ på macOS 13 og 14, eller _Systemvalg → Profiler_ på macOS 12 og tidligere.
3. Dobbeltklikk på Blokada-profilen og klikk _Installer_.

<p class="if-device">{% appleProfile %}Last ned min profil{% endappleProfile %}</p>

## Apple TV

Apple TV kan ikke åpne nettsider, så du skriver inn profillinken din manuelt.

1. Din profillink: {% appleUrl %}
2. På Apple TV, åpne _Innstillinger → Generelt → Personvern og sikkerhet_.
3. Marker _Send til Apple_ (kalt _Del Apple TV-analyse_ på eldre tvOS). Ikke velg det. Trykk på Play/Pause-knappen på fjernkontrollen i stedet.
4. Velg _Legg til profil_ og skriv inn din profillink. Det er enklest å skrive med tastaturmeldingen på iPhone, hvor du kan lime inn lenken. Installer profilen og bekreft.

<div class="note">

**Apple TV og andre enheter hjemme:** Hvis du setter opp Blokada Cloud på din [ruter](../router-ad-blocking/), dekkes Apple TV sammen med alt annet.

</div>

## Sjekk at det fungerer

Surf i ett minutt, og åpne deretter _Aktivitet_-siden i [dashbordet](https://app.blokada.org/stats?src=guides). Søkehistorikken for denne enheten vises der.

For å fjerne Blokada senere, slett profilen der du installerte den.
