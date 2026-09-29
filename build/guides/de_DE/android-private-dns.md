---
title: Privates DNS auf Android mit Blokada Cloud einrichten
description: Mit Androids Einstellung „Privates DNS“ und Blokada Cloud Werbung und Tracker in allen Apps blockieren, im WLAN und mobil. Oder die App Blokada 6 nutzen.
updated: 2026-09-28
order: 5
---

## Am einfachsten: die App

[Blokada 6](https://go.blokada.org/play_cloud) richtet alles für dich ein, schaltet die Blockierung mit einem Tippen ein und aus und zeigt direkt auf dem Handy, was blockiert wurde. Melde dich mit deiner Konto-ID an, und du bist fertig.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Blokada 6 bei Google Play holen</a></p>

## Ohne App: Privates DNS

Android 9 und neuer hat die Einstellung *Privates DNS*. Trägst du dort Blokada Cloud ein, werden Werbung und Tracker in allen Apps und in jedem Netz blockiert, ohne dass etwas im Hintergrund läuft.

Dein Blokada-DNS-Name: {% dot %}

1. Öffne *Einstellungen → Netzwerk & Internet*. Auf manchen Handys heißt das *Verbindungen* oder *Connection & sharing*.
2. Tippe auf *Privates DNS*. Auf Samsung-Handys findest du es unter *Weitere Verbindungseinstellungen*.
3. Wähle *Hostname des privaten DNS-Anbieters*.
4. Gib deinen Blokada-DNS-Namen {% dot %} ein und tippe auf *Speichern*.

Findest du die Einstellung nicht, suche in den Einstellungen nach „Privates DNS“.

## Prüfen, ob es funktioniert

Öffne ein paar Apps oder Websites und sieh dir dann die Seite *Aktivität* im [Dashboard](https://app.blokada.org/stats?src=guides) an. Dort erscheinen die Anfragen dieses Handys.

## Wenn etwas nicht klappt

- **„Verbindung nicht möglich“ oder kein Internet:** Prüfe deinen Blokada-DNS-Namen auf Tippfehler. Er muss genau wie oben angezeigt eingegeben werden, ohne `https://`.
- **Eine andere VPN-App ist aktiv:** Manche VPN-Apps nutzen ihr eigenes DNS und umgehen Privates DNS. Schalte das DNS oder den Werbeblocker in der VPN-App aus oder nutze stattdessen Blokada 6.
- **Chrome zeigt weiter Werbung:** Öffne in Chrome *Einstellungen → Datenschutz und Sicherheit → Sicheres DNS verwenden* und wähle *Use current service provider*.
