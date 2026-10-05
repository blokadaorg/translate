---
title: Werbung unter Windows mit DNS over HTTPS blockieren
description: Nutze das in Windows 11 eingebaute verschlüsselte DNS mit Blokada Cloud und blockiere Werbung und Tracker in allen Apps und Browsern, ohne Software.
updated: 2026-10-02
order: 8
---

Windows 11 kann alle DNS-Anfragen verschlüsselt über DNS over HTTPS senden. Stellst du es auf Blokada Cloud um, werden Werbung und Tracker in allen Apps und Browsern auf dem Computer blockiert, ohne dass du etwas installieren musst.

Du brauchst die IP-Adresse des DNS-Servers und deinen DoH-Link. Beide stehen oben unter _Deine Daten_.

## Windows 11

1. Öffne _Einstellungen → Netzwerk & Internet_ und dann _WLAN_ oder _Ethernet_, je nachdem, wie der Computer verbunden ist.
2. Öffne die _Hardwareeigenschaften_ (_Hardware properties_) deiner Verbindung. Wähle bei WLAN _Bekannte Netzwerke verwalten_ und dann das Netzwerk, oder oben auf der WLAN-Seite _Hardwareeigenschaften_.
3. Wähle neben _DNS-Serverzuweisung_ (_DNS server assignment_) die Option _Bearbeiten_. Wähle _Manuell_ und schalte _IPv4_ ein.
4. Gib unter _Bevorzugter DNS-Server_ den DNS-Server {% ip "doh" %} ein.
5. Stelle _DNS über HTTPS_ auf _An (manuelle Vorlage)_ und füge deinen DoH-Link {% doh %} in das Vorlagenfeld _DNS über HTTPS_ ein.
6. Schalte _Fallback auf Nurtext_ aus und wähle _Speichern_.

Nutzt der Computer sowohl WLAN als auch Ethernet, wiederhole das für die andere Verbindung.

<div class="note important">

Lass _Alternativer DNS-Server_ leer. Windows nutzt beide Server, und jeder andere lässt Werbung durch.

</div>

<div class="note tip">

Keine Option _An (manuelle Vorlage)_? Dann ist dein Windows 11 älter. Aktualisiere Windows, oder nutze solange die [Browser-Anleitung](../browser-dns-over-https/).

</div>

## Windows 10

Windows 10 hat kein eingebautes verschlüsseltes DNS. Richte stattdessen sicheres DNS in deinem Browser ein, wie in der [Browser-Anleitung](../browser-dns-over-https/) beschrieben, oder richte deinen [Router](../router-ad-blocking/) ein, um dein ganzes Zuhause abzudecken.

## Prüfen, ob es funktioniert

Öffne ein paar Websites und sieh dir dann die Seite _Aktivität_ im [Dashboard](https://app.blokada.org/stats?src=guides) an. Dort erscheinen die Anfragen dieses Computers.

<div class="note aside">

Du möchtest auf diesem Computer auch ein VPN? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) enthält eine WireGuard-Einrichtung, die den gesamten Datenverkehr verschlüsselt, mit derselben Blockierung.

</div>

## Wenn etwas nicht klappt

Chrome und Edge haben eine eigene Einstellung für _sicheres DNS_, die Windows umgeht. Im automatischen Modus kann sie auf unverschlüsseltes DNS zurückfallen, das Blokada ablehnt. Stelle sie stattdessen auf deinen DoH-Link:

- **Chrome:** Öffne `chrome://settings/security`, schalte _Sicheres DNS verwenden_ ein und wähle unter _DNS-Anbieter auswählen_ die Option _Benutzerdefinierten DNS-Dienstanbieter hinzufügen_.
- **Edge:** Öffne `edge://settings/privacy`, schalte sicheres DNS ein und wähle _Dienstanbieter auswählen_ (_Choose a service provider_).

Füge dann deinen DoH-Link {% doh %} ein.

Kommt in einem Netzwerk mit IPv6 noch Werbung durch, fragt Windows womöglich auch den IPv6-DNS-Server deines Routers. Schalte _Internetprotokoll Version 6 (TCP/IPv6)_ in den Eigenschaften des Adapters aus (_Systemsteuerung → Netzwerkverbindungen_), oder richte deinen [Router](../router-ad-blocking/) ein.
