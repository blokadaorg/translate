---
title: Blochează reclamele pe Linux cu DNS over TLS
description: Configurează systemd-resolved pentru a utiliza Blokada Cloud prin DNS over TLS criptat și blochează reclamele și tracker-ele pentru fiecare aplicație de pe computerul tău Linux.
updated: 2026-10-02
order: 9​
---

Cele mai recente distribuții Linux, inclusiv Ubuntu și Fedora, rezolvă numele prin _systemd-resolved_, care suportă DNS over TLS. Pe Debian, instalează-l mai întâi cu `sudo apt install systemd-resolved`. Setează Blokada Cloud și reclamele și tracker-ele sunt blocate pentru fiecare aplicație de pe computer.

## Configurează systemd-resolved

1. Creează folderul cu `sudo mkdir -p /etc/systemd/resolved.conf.d`, apoi fișierul `/etc/systemd/resolved.conf.d/blokada.conf` cu aceste setări:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Repornește serviciul: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Verifică: <code>resolvectl status</code> afișează <code>+DNSOverTLS</code> și serverul Blokada.</li>
</ol>

Partea de după `#` este numele tău Blokada DNS: {% dot %} systemd-resolved verifică certificatul serverului față de acesta, iar Blokada îl folosește pentru a identifica dispozitivul care face solicitarea.

<div class="note important">

**NetworkManager** transmite și serverele DNS ale rețelei tale. `Domains=~.` trimite toate interogările către Blokada, dar dacă `resolvectl status` încă afișează un alt server pe o conexiune, dezactivează DNS-ul automat pentru acea conexiune (comutatorul _Automat_ de lângă _DNS_ în setările IPv4 și IPv6).

</div>

## Fără systemd-resolved

Dacă `resolvectl` nu este găsit, distribuția ta Linux folosește altă metodă pentru rezolvarea numelor. Configurează DNS securizat în browserul tău, conform [ghidului pentru browser](../browser-dns-over-https/), sau configurează [routerul](../router-ad-blocking/) pentru a acoperi întreaga locuință.

## Verifică funcționalitatea

Deschide câteva site-uri web, apoi verifică pagina _Activitate_ din [control panel](https://app.blokada.org/stats?src=guides). Interogările acestui computer vor apărea acolo.

<div class="note aside">

Vrei și un VPN pe acest computer? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) include o configurare WireGuard care criptează tot traficul și are același mecanism de blocare.

</div>
