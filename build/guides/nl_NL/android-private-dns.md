---
title: Stel Private DNS in op Android met Blokada Cloud.
description: Gebruik de ingebouwde Private DNS-instelling van Android met Blokada Cloud om advertenties en trackers in elke app te blokkeren, zowel op wifi als mobiele data. Of laat de Blokada 6-app het voor je doen.
updated: 2026-09-28
order: 5
---

## De makkelijkste manier: de app

[Blokada 6](https://go.blokada.org/play_cloud) stelt alles voor je in, schakelt blokkeren met één tik in of uit en laat zien wat op de telefoon zelf is geblokkeerd. Log in met je account-ID en je bent klaar.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">Blokada 6 ophalen op Google Play</a></p>

## Zonder de app: Private DNS

Android 9 en later heeft een instelling voor _Private DNS_. Stel deze in op Blokada Cloud, en advertenties en trackers worden in alle apps en op elk netwerk geblokkeerd, zonder dat er iets op de achtergrond draait.

Je Blokada DNS-naam: {% dot %}

1. Open _Instellingen → Netwerk & internet_. Op sommige telefoons heet dit _Verbindingen_ of _Verbinding & delen_.
2. Tik op _Private DNS_. Op Samsung-telefoons staat dit onder _Meer verbindingsinstellingen_.
3. Kies _Private DNS-provider hostnaam_.
4. Voer je Blokada DNS-naam {% dot %} in en tik op _Opslaan_.

Als je het niet kunt vinden, zoek dan in de Instellingen-app op "Private DNS".

## Controleer of het werkt

Open enkele apps of websites en bekijk vervolgens de _Activiteit_-pagina in het [dashboard](https://app.blokada.org/stats?src=guides). De zoekopdrachten van deze telefoon worden daar weergegeven.

## Als iets niet werkt

- **"Kon geen verbinding maken" of geen internet:** controleer je Blokada DNS-naam op spelfouten. Deze moet precies worden ingevoerd zoals hierboven weergegeven, zonder `https://`.
- **Een andere VPN-app is actief:** sommige VPN-apps gebruiken hun eigen DNS en omzeilen Private DNS. Schakel de DNS- of advertentieblokkering van de VPN uit, of gebruik Blokada 6 in plaats daarvan.
- **Chrome toont nog steeds advertenties:** open in Chrome _Instellingen → Privacy en beveiliging → Beveiligde DNS gebruiken_ en kies _Huidige serviceprovider gebruiken_.
