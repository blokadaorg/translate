---
title: Hirdetések blokkolása Linuxon DNS over TLS segítségével
description: Állítsd be a systemd-resolved szolgáltatást, hogy a Blokada Cloud-ot használja titkosított DNS over TLS-sel, és blokkolja a hirdetéseket és követőket minden alkalmazásban a Linux számítógépeden.
updated: 2026-10-02
order: 9
---

A legtöbb modern Linux disztribúció, köztük az Ubuntu és a Fedora, a _systemd-resolved_ szolgáltatással oldja fel a neveket, amely támogatja a DNS over TLS-t. Debianon először telepítsd ezt: `sudo apt install systemd-resolved`. Állítsd be a Blokada Cloud-ot, és a hirdetések, valamint a követők minden alkalmazásban blokkolva lesznek a számítógépen.

## Systemd-resolved beállítása

1. Hozd létre a mappát ezzel: `sudo mkdir -p /etc/systemd/resolved.conf.d`, majd a `/etc/systemd/resolved.conf.d/blokada.conf` fájlt ezekkel a beállításokkal:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Indítsd újra: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Ellenőrizd: a <code>resolvectl status</code> mutatja, hogy <code>+DNSOverTLS</code> és a Blokada szerver szerepel.</li>
</ol>

A `#` utáni rész a Blokada DNS neved: {% dot %} a systemd-resolved ehhez ellenőrzi a szerver tanúsítványát, és a Blokada ezt használja annak meghatározására, melyik eszköz kérdez.

<div class="note important">

A **NetworkManager** is továbbítja a hálózatod DNS szervereit. A `Domains=~.` beállítás minden feloldást a Blokadahoz küld, de ha a `resolvectl status` még mindig egy másik szervert mutat egy kapcsolaton, kapcsold ki az automatikus DNS-t annál a kapcsolatnál (az _Automatikus_ kapcsoló az _DNS_ mellett az IPv4 és IPv6 beállításoknál).

</div>

## Systemd-resolved nélkül

Ha a `resolvectl` nem található, a disztribúciód másképp oldja fel a neveket. Állíts be biztonságos DNS-t a böngésződben, ahogyan a [böngésző útmutatóban](../browser-dns-over-https/) látható, vagy állítsd be az [útválasztódat](../router-ad-blocking/), hogy az egész házat lefedje.

## Ellenőrizd, hogy működik-e

Nyiss meg néhány weboldalt, majd nézd meg a _Tevékenység_ oldalt a [dashboardon](https://app.blokada.org/stats?src=guides). Ennek a számítógépnek a lekérdezései ott fognak megjelenni.

<div class="note aside">

Szeretnéd, hogy ezen a számítógépen is legyen VPN? A [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) tartalmaz egy WireGuard beállítást, amely minden forgalmat titkosít, a blokkolás változatlan marad.

</div>
