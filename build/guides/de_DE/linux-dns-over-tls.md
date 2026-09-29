---
title: Werbeeinblendungen unter Linux mit DNS über TLS blockieren
description: Richte systemd-resolved so ein, dass Blokada Cloud über verschlüsseltes DNS über TLS verwendet wird, um Werbung und Tracker für jede App auf deinem Linux-Computer zu blockieren.
updated: 2026-09-28
order: 9
---

Die meisten aktuellen Linux-Distributionen, einschließlich Ubuntu und Fedora, lösen Namen über _systemd-resolved_ auf, das DNS über TLS unterstützt. Installiere es auf Debian zuerst mit `sudo apt install systemd-resolved`. Richte es auf Blokada Cloud aus, und Werbung sowie Tracker werden für jede App auf dem Computer blockiert.

## systemd-resolved einrichten

1. Erstelle den Ordner mit `sudo mkdir -p /etc/systemd/resolved.conf.d`, dann die Datei `/etc/systemd/resolved.conf.d/blokada.conf` mit diesen Einstellungen:

<pre><code>[Resolve]\nDNS={{ site.dnsIps.dot }}#<span data-dns=\"dot\">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>\nDNSOverTLS=yes\nDomains=~.</code></pre>

<ol start="2">
<li>Starte den Dienst neu: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Überprüfe es: <code>resolvectl status</code> zeigt <code>+DNSOverTLS</code> und den Blokada-Server an.</li>
</ol>

Der Teil nach `#` ist dein Blokada-DNS-Name: {% dot %} systemd-resolved prüft das Zertifikat des Servers dagegen, und Blokada verwendet ihn, um zu wissen, welches Gerät anfragt.

<div class="note">

**NetworkManager** gibt ebenfalls die DNS-Server deines Netzwerks weiter. `Domains=~.` leitet alle Anfragen an Blokada weiter. Wenn jedoch `resolvectl status` dennoch einen anderen Server für eine Verbindung anzeigt, deaktiviere das automatische DNS für diese Verbindung (der _Automatisch_-Schalter neben _DNS_ in den IPv4- und IPv6-Einstellungen).

</div>

## Ohne systemd-resolved

Wenn `resolvectl` nicht gefunden wird, löst deine Distribution Namen auf eine andere Weise auf. Richte stattdessen sicheres DNS in deinem Browser ein, wie im [Browser-Leitfaden](../browser-dns-over-https/) beschrieben, oder konfiguriere deinen [Router](../router-ad-blocking/) für die netzwerkweite Abdeckung.

## Überprüfe, ob es funktioniert

Öffne einige Webseiten und sieh dir dann die _Aktivität_-Seite im [Dashboard](https://app.blokada.org/stats?src=guides) an. Die Anfragen dieses Computers erscheinen dort.

<div class="note">

Möchtest du auch ein VPN auf diesem Computer? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) beinhaltet eine WireGuard-Einrichtung, die den gesamten Datenverkehr verschlüsselt, mit derselben Blockierung.

</div>
