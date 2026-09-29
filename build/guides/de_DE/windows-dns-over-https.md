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

1. Öffne *Einstellungen → Netzwerk und Internet* und dann *WLAN* oder *Ethernet*, je nachdem, wie der Computer verbunden ist.
2. Öffne die *Hardwareeigenschaften* deiner Verbindung. Wähle bei WLAN *Bekannte Netzwerke verwalten* und dann das Netzwerk, oder oben auf der WLAN-Seite *Hardwareeigenschaften*.
3. Wähle neben *DNS-Serverzuweisung* die Option *Bearbeiten*. Wähle *Manuell* und schalte *IPv4* ein.
4. Gib unter *Bevorzugter DNS* den DNS-Server {% ip "doh" %} ein.
5. Stelle *DNS über HTTPS* auf *Ein (manuelle Vorlage)* und füge deinen DoH-Link {% doh %} als *DoH-Vorlage* ein.
6. Schalte *Fallback auf Klartext* aus und wähle *Speichern*.

Nutzt der Computer sowohl WLAN als auch Ethernet, wiederhole das für die andere Verbindung.

<div class="note">

Lass *Alternativer DNS* leer. Windows nutzt beide Server, und jeder andere lässt Werbung durch.

Keine Option *Ein (manuelle Vorlage)*? Dann ist dein Windows 11 älter. Aktualisiere Windows, oder nutze solange die [Browser-Anleitung](../browser-dns-over-https/).

Kommt in einem Netzwerk mit IPv6 noch Werbung durch, fragt Windows womöglich auch den IPv6-DNS-Server deines Routers. Schalte *Internetprotokoll, Version 6 (TCP/IPv6)* in den Eigenschaften des Adapters aus (*Systemsteuerung → Netzwerkverbindungen*), oder richte deinen [Router](../router-ad-blocking/) ein.

</div>

## Windows 10

Windows 10 hat kein eingebautes verschlüsseltes DNS. Richte stattdessen sicheres DNS in deinem Browser ein, wie in der [Browser-Anleitung](../browser-dns-over-https/) beschrieben, oder richte deinen [Router](../router-ad-blocking/) ein, um dein ganzes Zuhause abzudecken.

## Prüfen, ob es funktioniert

Öffne ein paar Websites und sieh dir dann die Seite *Aktivität* im [Dashboard](https://app.blokada.org/stats?src=guides) an. Dort erscheinen die Anfragen dieses Computers.

Browser mit eigener Einstellung für *sicheres DNS* umgehen Windows. Stelle sie in Chrome und Edge auf den aktuellen Dienstanbieter oder auf deinen DoH-Link ein.

<div class="note">

Du möchtest auf diesem Computer auch ein VPN? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) enthält eine WireGuard-Einrichtung, die den gesamten Datenverkehr verschlüsselt, mit derselben Blockierung.

</div>
