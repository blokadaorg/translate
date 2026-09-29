---
title: Werbung unter Linux mit DNS over TLS blockieren
description: Richte systemd-resolved für Blokada Cloud über verschlüsseltes DNS over TLS ein und blockiere Werbung und Tracker für alle Apps auf deinem Linux-Computer.
updated: 2026-09-28
order: 9
---

Die meisten aktuellen Linux-Distributionen, darunter Ubuntu und Fedora, lösen Namen über *systemd-resolved* auf, das DNS over TLS unterstützt. Unter Debian installierst du es zuerst mit `sudo apt install systemd-resolved`. Stellst du es auf Blokada Cloud um, werden Werbung und Tracker für alle Apps auf dem Computer blockiert.

## systemd-resolved einrichten

1. Lege den Ordner mit `sudo mkdir -p /etc/systemd/resolved.conf.d` an und dann die Datei `/etc/systemd/resolved.conf.d/blokada.conf` mit diesen Einstellungen:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Starte den Dienst neu: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Prüfe ihn: <code>resolvectl status</code> zeigt <code>+DNSOverTLS</code> und den Blokada-Server.</li>
</ol>

Der Teil nach `#` ist dein Blokada-DNS-Name: {% dot %} systemd-resolved prüft das Zertifikat des Servers damit, und Blokada erkennt daran, welches Gerät fragt.

<div class="note">

**NetworkManager** gibt außerdem die DNS-Server deines Netzwerks weiter. `Domains=~.` schickt alle Anfragen an Blokada. Zeigt `resolvectl status` für eine Verbindung trotzdem noch einen anderen Server, schalte für diese Verbindung das automatische DNS aus (den Schalter *Automatisch* neben *DNS* in ihren IPv4- und IPv6-Einstellungen).

</div>

## Ohne systemd-resolved

Wird `resolvectl` nicht gefunden, löst deine Distribution Namen auf andere Weise auf. Richte stattdessen sicheres DNS in deinem Browser ein, wie in der [Browser-Anleitung](../browser-dns-over-https/) beschrieben, oder richte deinen [Router](../router-ad-blocking/) ein, um dein ganzes Zuhause abzudecken.

## Prüfen, ob es funktioniert

Öffne ein paar Websites und sieh dir dann die Seite *Aktivität* im [Dashboard](https://app.blokada.org/stats?src=guides) an. Dort erscheinen die Anfragen dieses Computers.

<div class="note">

Du möchtest auf diesem Computer auch ein VPN? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) enthält eine WireGuard-Einrichtung, die den gesamten Datenverkehr verschlüsselt, mit derselben Blockierung.

</div>
