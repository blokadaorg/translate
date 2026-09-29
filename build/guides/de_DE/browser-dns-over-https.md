---
title: Werbeeinblendungen in Chrome, Firefox, Edge und Brave mit DNS über HTTPS blockieren.
description: Setze Blokada Cloud als sicheren DNS-Anbieter in deinem Browser, um Werbung und Tracker auf jedem Computer zu blockieren – auch auf Arbeitslaptops, auf denen du keine Apps installieren kannst.
updated: 2026-09-23
order: 7
---

Moderne Browser können ihren eigenen verschlüsselten DNS-Anbieter verwenden, der als _sicheres DNS_ oder _DNS über HTTPS_ bezeichnet wird. Stelle ihn auf Blokada Cloud ein, und der Browser blockiert Werbung und Tracker in jedem Netzwerk – ganz ohne Erweiterung.

Diese Einstellung gilt nur für diesen Browser. Um den gesamten Computer zu schützen, verwende das [Apple-Profil](../apple-devices/) auf einem Mac oder richte deinen [Router](../router-ad-blocking/) ein.

Dein DoH-Link: {% doh %}

## Chrome

1. Öffne `chrome://settings/security`.
2. Aktiviere _Sicheres DNS verwenden_ und wähle dann _Benutzerdefinierten DNS-Dienstanbieter hinzufügen_.
3. Gib {% doh %} ein

## Edge

1. Öffne `edge://settings/privacy`.
2. Aktiviere unter _Sicherheit_ die Option _Sicheres DNS verwenden, um festzulegen, wie die Netzwerkadresse für Webseiten gesucht wird_.
3. Wähle _Dienstanbieter auswählen_ und gib {% doh %} ein

## Firefox

1. Öffne _Einstellungen → Datenschutz & Sicherheit_ und scrolle zu _DNS über HTTPS_.
2. Wähle _Maximaler Schutz_.
3. Unter _Anbieter auswählen_ wähle _Benutzerdefiniert_ und gib {% doh %} ein

## Brave

1. Öffne `brave://settings/security`.
2. Aktiviere _Sicheres DNS verwenden_ und wähle dann _Benutzerdefinierten DNS-Dienstanbieter hinzufügen_.
3. Gib {% doh %} ein

## Safari

Safari hat keine eigene Einstellung für sicheres DNS. Es verwendet das System-DNS, daher installiere das [Apple-Profil](../apple-devices/).

## Überprüfen, ob es funktioniert

Surfe eine Minute und öffne dann die _Aktivitäts_-Seite im [Dashboard](https://app.blokada.org/stats?src=guides). Die Anfragen dieses Browsers erscheinen dort.

<div class="note">

Wenn dein Browser von der Arbeit oder Schule verwaltet wird, kann die Einstellung für sicheres DNS gesperrt sein. Frage deinen Administrator.

</div>
