---
title: Blokkeer advertenties op Windows met DNS over HTTPS.
description: Gebruik de ingebouwde versleutelde DNS van Windows 11 met Blokada Cloud om advertenties en trackers in elke app en browser te blokkeren, zonder dat je software hoeft te installeren.
updated: 2026-10-02
order: 8
---

Windows 11 kan al zijn DNS-opvragingen versleuteld verzenden via DNS over HTTPS. Richt het op Blokada Cloud, en advertenties en trackers worden in elke app en browser op de computer geblokkeerd, zonder dat er iets geïnstalleerd hoeft te worden.

Je hebt het IP-adres van de DNS-server en je DoH-link nodig, beide te vinden onder _Jouw gegevens_ hierboven.

## Windows 11

1. Open _Instellingen → Netwerk & internet_ en vervolgens _Wi-Fi_ of _Ethernet_, afhankelijk van hoe de computer verbonden is.
2. Open de _Hardware-eigenschappen_ van je verbinding. Voor Wi-Fi: selecteer _Beheer bekende netwerken_ en vervolgens het netwerk, of _Hardware-eigenschappen_ bovenaan de Wi-Fi-pagina.
3. Kies naast _DNS-servertoewijzing_ voor _Bewerken_. Kies _Handmatig_ en zet _IPv4_ aan.
4. Voer bij _Voorkeurs-DNS_ de DNS-server {% ip "doh" %} in.
5. Zet _DNS over HTTPS_ op _Aan (handmatig sjabloon)_ en plak jouw DoH-link {% doh %} als het _DoH-sjabloon_.
6. Zet _Terugvallen naar platte tekst_ uit en selecteer _Opslaan_.

Als de computer zowel Wi-Fi als Ethernet gebruikt, herhaal dit dan voor de andere verbinding.

<div class="note important">

Laat _Alternatieve DNS_ leeg. Windows gebruikt beide servers, en elke andere laat advertenties door.

</div>

<div class="note tip">

Geen optie _Aan (handmatige sjabloon)_? Jouw Windows 11 is ouder. Werk Windows bij, of gebruik ondertussen de [browsergids](../browser-dns-over-https/).

</div>

## Windows 10

Windows 10 heeft geen ingebouwde versleutelde DNS. Stel in plaats daarvan veilige DNS in je browser in zoals in de [browsergids](../browser-dns-over-https/), of stel je [router](../router-ad-blocking/) in voor bescherming over het hele thuisnetwerk.

## Controleer of het werkt

Open een paar websites en kijk dan op de pagina _Activiteit_ in het [dashboard](https://app.blokada.org/stats?src=guides). De opvragingen van deze computer verschijnen daar.

<div class="note aside">

Wil je ook een VPN op deze computer? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) bevat een WireGuard-configuratie die al het verkeer versleutelt, met dezelfde blokkering.

</div>

## Als iets niet werkt

Chrome en Edge hebben hun eigen _veilige DNS_-instelling, die Windows omzeilt. Als deze op automatisch staat, kan het terugvallen op gewone DNS, wat Blokada weigert. Stel in plaats daarvan je DoH-link in:

- **Chrome:** open `chrome://settings/security`, zet _Beveiligde DNS gebruiken_ aan en kies bij _DNS-provider selecteren_ voor _Aangepaste DNS-serviceprovider toevoegen_.
- **Edge:** open `edge://settings/privacy`, zet beveiligde DNS aan en kies _Een serviceprovider kiezen_.

Plak daarna je DoH-link {% doh %}

Als sommige advertenties toch nog doorkomen op een netwerk met IPv6, vraagt Windows mogelijk ook de IPv6-DNS-server van je router. Zet _Internet Protocol versie 6 (TCP/IPv6)_ uit in de eigenschappen van de adapter (_Configuratiescherm → Netwerkverbindingen_), of stel je [router](../router-ad-blocking/) in.
