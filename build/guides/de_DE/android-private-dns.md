---
title: Private DNS auf Android mit Blokada Cloud einrichten.
description: Verwende die integrierte Private DNS-Einstellung von Android mit Blokada Cloud, um Werbung und Tracker in jeder App sowohl über WLAN als auch mobile Daten zu blockieren. Oder lasse die Blokada 6 App das übernehmen.
updated: 2026-09-28
order: 5
---

## Der einfachste Weg: Die App

[Blokada 6](https://go.blokada.org/play_cloud) richtet alles für dich ein, schaltet die Blockierung mit einem Tippen an und aus und zeigt direkt auf dem Handy, was blockiert wurde. Melde dich mit deiner Account-ID an und du bist fertig.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">Blokada 6 bei Google Play herunterladen</a></p>

## Ohne die App: Privates DNS

Android 9 und neuer verfügt über eine Einstellung für _Privates DNS_. Stelle sie auf Blokada Cloud ein, und Werbung sowie Tracker werden in allen Apps und in jedem Netzwerk blockiert, ohne dass etwas im Hintergrund läuft.

Dein Blokada DNS-Name: {% dot %}

1. Öffne _Einstellungen → Netzwerk & Internet_. Auf einigen Geräten heißt dies _Verbindungen_ oder _Verbindung & Teilen_.
2. Tippe auf _Privates DNS_. Auf Samsung-Geräten befindet sich dies unter _Weitere Verbindungseinstellungen_.
3. Wähle _Privater DNS-Anbieter-Hostname_.
4. Gib deinen Blokada DNS-Namen {% dot %} ein und tippe auf _Speichern_.

Wenn du es nicht finden kannst, suche in der Einstellungen-App nach "Privates DNS".

## Prüfe, ob es funktioniert

Öffne ein paar Apps oder Webseiten und sieh dir dann auf der _Aktivität_-Seite im [Dashboard](https://app.blokada.org/stats?src=guides) nach. Die Anfragen dieses Geräts werden dort angezeigt.

## Wenn etwas nicht funktioniert

- **"Konnte keine Verbindung herstellen" oder kein Internet:** Überprüfe deinen Blokada DNS-Namen auf Tippfehler. Er muss genau wie oben angezeigt eingetragen werden, ohne `https://`.
- **Eine andere VPN-App ist aktiv:** Einige VPN-Apps nutzen eigene DNS und umgehen das Private DNS. Schalte die DNS- oder Werbeblocker-Einstellung des VPN aus oder verwende stattdessen Blokada 6.
- **Chrome zeigt weiterhin Werbung an:** Öffne in Chrome _Einstellungen → Datenschutz und Sicherheit → Sicheren DNS verwenden_ und wähle _Aktuellen Dienstanbieter verwenden_.
