---
title: Werbung auf Windows mit DNS über HTTPS blockieren
description: Nutze den in Windows 11 integrierten verschlüsselten DNS zusammen mit Blokada Cloud, um Werbung und Tracker in jeder App und jedem Browser zu blockieren – ganz ohne zusätzliche Softwareinstallation.
updated: 2026-09-28
order: 8
---

Windows 11 kann alle seine DNS-Abfragen verschlüsselt über DNS über HTTPS senden. Stelle auf Blokada Cloud um, und Werbung sowie Tracker werden in jeder App und jedem Browser auf dem Computer blockiert – ganz ohne Installation.

Du benötigst zwei Werte:

- DNS-Server (IP-Adresse): {% ip "doh" %}
- Dein DoH-Link: {% doh %}

## Windows 11

1. Öffne _Einstellungen → Netzwerk & Internet_, dann _WLAN_ oder _Ethernet_, je nachdem, wie der Computer verbunden ist.
2. Öffne die _Hardwareeigenschaften_ deiner Verbindung. Bei WLAN wähle _Bekannte Netzwerke verwalten_ und dann das Netzwerk oder _Hardwareeigenschaften_ oben auf der WLAN-Seite.
3. Wähle neben _DNS-Serverzuweisung_ die Option _Bearbeiten_. Wähle _Manuell_ und aktiviere _IPv4_.
4. Gib unter _Bevorzugter DNS_ den DNS-Server {% ip "doh" %} ein.
5. Stelle _DNS über HTTPS_ auf _Ein (manuelle Vorlage)_ und füge deinen DoH-Link {% doh %} als _DoH-Vorlage_ ein.
6. Schalte _Fallback auf Klartext_ aus und wähle _Speichern_.

Wenn der Computer sowohl WLAN als auch Ethernet verwendet, wiederhole dies auch für die andere Verbindung.

<div class="note">

Lass _Alternativer DNS_ leer. Windows verwendet beide Server, und jeder andere lässt Werbung durch.

Keine Option _Ein (manuelle Vorlage)_? Dein Windows 11 ist älter. Aktualisiere Windows oder nutze in der Zwischenzeit die [Browser-Anleitung](../browser-dns-over-https/).

Wenn trotz allem auf einem Netzwerk mit IPv6 noch Werbung durchkommt, fragt Windows möglicherweise auch den IPv6-DNS-Server deines Routers ab. Deaktiviere _Internetprotokoll Version 6 (TCP/IPv6)_ in den Adaptereigenschaften (_Systemsteuerung → Netzwerkverbindungen_) oder konfiguriere deinen [Router](../router-ad-blocking/).

</div>

## Windows 10

Windows 10 besitzt keinen integrierten verschlüsselten DNS. Richte stattdessen sicheres DNS in deinem Browser ein, wie in der [Browser-Anleitung](../browser-dns-over-https/), oder konfiguriere deinen [Router](../router-ad-blocking/) für den gesamten Haushalt.

## Teste, ob alles funktioniert

Öffne einige Webseiten und sieh dann auf der _Aktivitäten_-Seite im [Dashboard](https://app.blokada.org/stats?src=guides) nach. Die Abfragen dieses Computers erscheinen dort.

Browser mit eigener _sicherer DNS_-Einstellung umgehen Windows. Stelle in Chrome und Edge ein, dass der aktuelle Dienstanbieter oder dein DoH-Link verwendet wird.

<div class="note">

Möchtest du diesen Computer ebenfalls mit einem VPN schützen? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) enthält eine WireGuard-Konfiguration, die den gesamten Datenverkehr verschlüsselt – mit derselben Blockierung.

</div>
