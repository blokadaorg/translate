---
title: Werbung unter Windows mit DNS over HTTPS blockieren
description: Nutze das in Windows 11 eingebaute verschlüsselte DNS mit Blokada Cloud und blockiere Werbung und Tracker in allen Apps und Browsern, ohne Software.
updated: 2026-09-28
order: 8
---

Windows 11 kann alle DNS-Anfragen verschlüsselt über DNS over HTTPS senden. Stellst du es auf Blokada Cloud um, werden Werbung und Tracker in allen Apps und Browsern auf dem Computer blockiert, ohne dass du etwas installieren musst.

Du brauchst zwei Werte:

- DNS-Server (IP-Adresse): {% ip "doh" %}
- Dein DoH-Link: {% doh %}

## Windows 11

1. Öffne _Einstellungen → Netzwerk und Internet_ und dann _WLAN_ oder _Ethernet_, je nachdem, wie der Computer verbunden ist.
2. Öffne die _Hardwareeigenschaften_ deiner Verbindung. Wähle bei WLAN _Bekannte Netzwerke verwalten_ und dann das Netzwerk, oder oben auf der WLAN-Seite _Hardwareeigenschaften_.
3. Wähle neben _DNS-Serverzuweisung_ die Option _Bearbeiten_. Wähle _Manuell_ und schalte _IPv4_ ein.
4. Gib unter _Bevorzugter DNS_ den DNS-Server {% ip "doh" %} ein.
5. Stelle _DNS über HTTPS_ auf _Ein (manuelle Vorlage)_ und füge deinen DoH-Link {% doh %} als _DoH-Vorlage_ ein.
6. Schalte _Fallback auf Klartext_ aus und wähle _Speichern_.

Nutzt der Computer sowohl WLAN als auch Ethernet, wiederhole das für die andere Verbindung.

<div class="note">

Lass _Alternativer DNS_ leer. Windows nutzt beide Server, und jeder andere lässt Werbung durch.

Keine Option _Ein (manuelle Vorlage)_? Dann ist dein Windows 11 älter. Aktualisiere Windows, oder nutze solange die [Browser-Anleitung](../browser-dns-over-https/).

Kommt in einem Netzwerk mit IPv6 noch Werbung durch, fragt Windows womöglich auch den IPv6-DNS-Server deines Routers. Schalte _Internetprotokoll, Version 6 (TCP/IPv6)_ in den Eigenschaften des Adapters aus (_Systemsteuerung → Netzwerkverbindungen_), oder richte deinen [Router](../router-ad-blocking/) ein.

</div>

## Windows 10

Windows 10 hat kein eingebautes verschlüsseltes DNS. Richte stattdessen sicheres DNS in deinem Browser ein, wie in der [Browser-Anleitung](../browser-dns-over-https/) beschrieben, oder richte deinen [Router](../router-ad-blocking/) ein, um dein ganzes Zuhause abzudecken.

## Prüfen, ob es funktioniert

Öffne ein paar Websites und sieh dir dann die Seite _Aktivität_ im [Dashboard](https://app.blokada.org/stats?src=guides) an. Dort erscheinen die Anfragen dieses Computers.

Browser mit eigener Einstellung für _sicheres DNS_ umgehen Windows. Stelle sie in Chrome und Edge auf den aktuellen Dienstanbieter oder auf deinen DoH-Link ein.

<div class="note">

Du möchtest auf diesem Computer auch ein VPN? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) enthält eine WireGuard-Einrichtung, die den gesamten Datenverkehr verschlüsselt, mit derselben Blockierung.

</div>
