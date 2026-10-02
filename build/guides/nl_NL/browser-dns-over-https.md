---
title: Blokkeer advertenties in Chrome, Firefox, Edge en Brave met DNS over HTTPS.
description: Stel Blokada Cloud in als de beveiligde DNS-provider in je browser om advertenties en trackers te blokkeren, op elke computer, inclusief werk-laptops waarop je geen apps kunt installeren.
updated: 2026-10-02
order: 7
---

Moderne browsers kunnen hun eigen versleutelde DNS-provider gebruiken, genaamd _beveiligde DNS_ of _DNS over HTTPS_. Stel deze in op Blokada Cloud, en de browser blokkeert advertenties en trackers op elk netwerk, zonder dat je een extensie hoeft te installeren.

Deze instelling geldt alleen voor deze browser. Om de hele computer te beschermen, gebruik je het [Apple-profiel](../apple-devices/) op een Mac, of stel je je [router](../router-ad-blocking/) in.

## Chrome

1. Open `chrome://settings/security`.
2. Schakel _Beveiligde DNS gebruiken_ in en kies dan voor _Aangepaste DNS-serviceprovider toevoegen_.
3. Voer {% doh %} in

## Edge

1. Open `edge://settings/privacy`.
2. Schakel onder _Beveiliging_ de optie _Beveiligde DNS gebruiken om te bepalen hoe het netwerkadres van websites wordt opgezocht_ in.
3. Kies _Serviceprovider kiezen_ en voer {% doh %} in

## Firefox

1. Open _Instellingen → Privacy & Beveiliging_ en scrol naar _DNS over HTTPS_.
2. Kies _Maximale bescherming_.
3. Kies onder _Provider kiezen_ voor _Aangepast_ en voer {% doh %} in

## Brave

1. Open `brave://settings/security`.
2. Schakel _Beveiligde DNS gebruiken_ in en kies dan voor _Aangepaste DNS-serviceprovider toevoegen_.
3. Voer {% doh %} in

## Safari

Safari heeft geen eigen instelling voor beveiligde DNS. Safari gebruikt het DNS van het systeem, installeer daarom het [Apple-profiel](../apple-devices/).

## Controleer of het werkt

Blader een minuut rond en open dan de pagina _Activiteit_ in het [dashboard](https://app.blokada.org/stats?src=guides). De opvragingen van deze browser zijn daar zichtbaar.

## Als iets niet werkt

<div class="note tip">

Als je browser wordt beheerd door werk of school, kan het zijn dat de instelling voor beveiligde DNS is vergrendeld. Vraag je beheerder om hulp.

</div>
