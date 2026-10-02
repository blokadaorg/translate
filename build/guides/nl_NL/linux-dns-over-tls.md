---
title: Blokkeer advertenties op Linux met DNS over TLS
description: Stel systemd-resolved in om Blokada Cloud te gebruiken via versleutelde DNS over TLS, en blokkeer advertenties en trackers voor elke app op je Linux-computer.
updated: 2026-10-02
order: 9
---

De meeste huidige Linux-distributies, waaronder Ubuntu en Fedora, lossen namen op via _systemd-resolved_, dat DNS over TLS ondersteunt. Installeer het eerst op Debian met `sudo apt install systemd-resolved`. Wijs het toe aan Blokada Cloud, en advertenties en trackers worden voor elke app op de computer geblokkeerd.

## Stel systemd-resolved in

1. Maak de map aan met `sudo mkdir -p /etc/systemd/resolved.conf.d`, en daarna het bestand `/etc/systemd/resolved.conf.d/blokada.conf` met deze instellingen:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Herstart het: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Controleer het: <code>resolvectl status</code> laat <code>+DNSOverTLS</code> en de Blokada-server zien.</li>
</ol>

Het gedeelte na `#` is jouw Blokada DNS-naam: {% dot %} systemd-resolved controleert het certificaat van de server hiertegen, en Blokada gebruikt het om te weten welk apparaat vraagt.

<div class="note important">

**NetworkManager** geeft ook de DNS-servers van jouw netwerk door. `Domains=~.` stuurt alle zoekopdrachten naar Blokada, maar als `resolvectl status` toch een andere server bij een verbinding vermeldt, schakel dan de automatische DNS voor die verbinding uit (de _Automatisch_ schakelaar naast _DNS_ in de IPv4- en IPv6-instellingen).

</div>

## Zonder systemd-resolved

Als `resolvectl` niet gevonden wordt, lost jouw distributie namen op een andere manier op. Stel in plaats daarvan veilige DNS in je browser in zoals in de [browsergids](../browser-dns-over-https/), of stel je [router](../router-ad-blocking/) in voor bescherming over het hele thuisnetwerk.

## Controleer of het werkt

Open een paar websites en kijk dan op de pagina _Activiteit_ in het [dashboard](https://app.blokada.org/stats?src=guides). De zoekopdrachten van deze computer verschijnen daar.

<div class="note aside">

Wil je ook een VPN op deze computer? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) bevat een WireGuard-configuratie die al het verkeer versleutelt, met dezelfde blokkering.

</div>
