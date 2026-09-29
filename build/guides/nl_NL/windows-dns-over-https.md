---
title: Blokkeer advertenties op Windows met DNS over HTTPS.
description: Gebruik de ingebouwde versleutelde DNS van Windows 11 met Blokada Cloud om advertenties en trackers in elke app en browser te blokkeren, zonder dat je software hoeft te installeren.
updated: 2026-09-28
order: 8
---

Windows 11 kan al zijn DNS-opvragingen versleuteld verzenden via DNS over HTTPS. Wijs hem naar Blokada Cloud en advertenties en trackers worden geblokkeerd in elke app en browser op de computer, zonder installatie van extra software.

Je hebt twee waarden nodig:

- DNS-server (IP-adres): {% ip "doh" %}
- Jouw DoH-link: {% doh %}

## Windows 11

1. Open _Instellingen → Netwerk & internet_ en vervolgens _Wi-Fi_ of _Ethernet_, afhankelijk van hoe de computer verbonden is.
2. Open de _Hardware-eigenschappen_ van je verbinding. Voor Wi-Fi, selecteer _Bekende netwerken beheren_ en dan het netwerk, of _Hardware-eigenschappen_ bovenaan de Wi-Fi pagina.
3. Selecteer naast _DNS-servertoewijzing_ de optie _Bewerken_. Kies _Handmatig_ en zet _IPv4_ aan.
4. Voer bij _Voorkeurs-DNS_ de DNS-server {% ip "doh" %} in.
5. Zet _DNS over HTTPS_ op _Aan (handmatig sjabloon)_ en plak jouw DoH-link {% doh %} als het _DoH-sjabloon_.
6. Zet _Terugvallen naar platte tekst_ uit en selecteer _Opslaan_.

Als de computer zowel Wi-Fi als Ethernet gebruikt, herhaal dit dan voor de andere verbinding.

<div class="note">

Laat _Alternatief DNS_ leeg. Windows gebruikt beide servers, en elke andere laat advertenties door.

Geen optie _Aan (handmatig sjabloon)_? Jouw Windows 11 is ouder. Update Windows, of gebruik intussen de [browservoorschriften](../browser-dns-over-https/).

Als er toch advertenties verschijnen op een netwerk met IPv6, vraagt Windows mogelijk ook de IPv6 DNS-server van je router. Schakel _Internet Protocol Versie 6 (TCP/IPv6)_ uit in de adaptereigenschappen (_Configuratiescherm → Netwerkverbindingen_), of stel je [router](../router-ad-blocking/) in.

</div>

## Windows 10

Windows 10 heeft geen ingebouwde versleutelde DNS. Stel in plaats daarvan veilige DNS in via je browser, zoals in de [browservoorschriften](../browser-dns-over-https/), of stel je [router](../router-ad-blocking/) in om het hele huis te dekken.

## Controleer of het werkt

Open een paar websites en bekijk dan de pagina _Activiteit_ in het [dashboard](https://app.blokada.org/stats?src=guides). De opvragingen van deze computer verschijnen daar.

Browsers met een eigen _veilige DNS_-instelling omzeilen Windows. Stel in Chrome en Edge in dat deze de huidige dienstverlener gebruikt, of jouw DoH-link.

<div class="note">

Wil je ook een VPN op deze computer? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) bevat een WireGuard-installatie die al het verkeer versleutelt, met dezelfde blokkering.

</div>
