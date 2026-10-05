---
title: Stel Private DNS in op Android met Blokada Cloud.
description: Gebruik de ingebouwde Private DNS-instelling van Android met Blokada Cloud om advertenties en trackers in elke app te blokkeren, zowel op Wi-Fi als mobiele data. Of laat de Blokada 6-app het voor je doen.
updated: 2026-10-02
order: 5
---

## De makkelijkste manier: de app

[Blokada 6](https://go.blokada.org/play_cloud) stelt alles voor je in, schakelt blokkeren met één tik in of uit en laat zien wat op de telefoon zelf is geblokkeerd. Log in met je account-ID en je bent klaar.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">Blokada 6 ophalen op Google Play</a></p>

## Zonder de app: Private DNS

Android 9 en nieuwer heeft een _Private DNS_-instelling. Stel deze in op Blokada Cloud, en advertenties en trackers worden in alle apps en op elk netwerk geblokkeerd, zonder dat er iets op de achtergrond draait.

1. Open _Instellingen → Netwerk & internet_. Op sommige telefoons heet dit _Verbindingen_ of _Verbinding & delen_.
2. Tik op _Private DNS_. Op Samsung-telefoons staat dit onder _Meer verbindingsinstellingen_.
3. Kies _Private DNS-provider hostnaam_.
4. Voer je Blokada DNS-naam {% dot %} in en tik op _Opslaan_.

Als je het niet kunt vinden, zoek dan in de Instellingen-app op "Private DNS".

## Controleer of het werkt

Open enkele apps of websites en bekijk vervolgens de _Activiteit_-pagina in het [dashboard](https://app.blokada.org/stats?src=guides). De zoekopdrachten van deze telefoon verschijnen daar.

## Als iets niet werkt

- **"Kan geen verbinding maken" of geen internet:** controleer je Blokada DNS-naam op typefouten. Deze moet exact zijn zoals hierboven weergegeven, zonder `https://`.
- **Een andere VPN-app is actief:** sommige VPN-apps gebruiken hun eigen DNS en omzeilen Private DNS. Zet de DNS- of advertentieblokkeringsinstelling van de VPN uit, of gebruik in plaats daarvan Blokada 6.
- **Chrome toont nog steeds advertenties:** Chrome kan ingesteld zijn op een eigen beveiligde DNS-provider, waardoor Private DNS wordt omzeild. Open in Chrome _Instellingen → Privacy en beveiliging → Beveiligde DNS gebruiken_ en kies _Je huidige serviceprovider gebruiken_. Chrome volgt dan Private DNS.
