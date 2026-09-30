---
title: Werbung in Chrome, Firefox, Edge und Brave mit DNS over HTTPS blockieren
description: Stelle Blokada Cloud als sicheres DNS im Browser ein und blockiere Werbung und Tracker auf jedem Computer, auch auf Arbeitslaptops ohne App-Installation.
updated: 2026-09-23
order: 7
---

Moderne Browser können einen eigenen verschlüsselten DNS-Anbieter nutzen, genannt _sicheres DNS_ oder _DNS over HTTPS_. Stellst du dort Blokada Cloud ein, blockiert der Browser Werbung und Tracker in jedem Netz, ganz ohne Erweiterung.

Diese Einstellung gilt nur für diesen Browser. Für den ganzen Computer nutzt du auf dem Mac das [Apple-Profil](../apple-devices/) oder richtest deinen [Router](../router-ad-blocking/) ein.

Dein DoH-Link: {% doh %}

## Chrome

1. Öffne `chrome://settings/security`.
2. Schalte _Sicheres DNS verwenden_ ein und wähle dann _Add custom DNS service provider_.
3. Gib {% doh %} ein.

## Edge

1. Öffne `edge://settings/privacy`.
2. Schalte unter _Sicherheit_ die Option _Use secure DNS to specify how to look up the network address for websites_ ein.
3. Wähle _Choose a service provider_ und gib {% doh %} ein.

## Firefox

1. Öffne _Einstellungen → Datenschutz & Sicherheit_ und scrolle zu _DNS über HTTPS_.
2. Wähle _Maximaler Schutz_.
3. Wähle unter _Anbieter auswählen_ die Option _Benutzerdefiniert_ und gib {% doh %} ein.

## Brave

1. Öffne `brave://settings/security`.
2. Schalte _Sicheres DNS verwenden_ ein und wähle dann _Add custom DNS service provider_.
3. Gib {% doh %} ein.

## Safari

Safari hat keine eigene Einstellung für sicheres DNS. Es nutzt das DNS des Systems, installiere also das [Apple-Profil](../apple-devices/).

## Prüfen, ob es funktioniert

Surfe eine Minute lang und öffne dann die Seite _Aktivität_ im [Dashboard](https://app.blokada.org/stats?src=guides). Dort erscheinen die Anfragen dieses Browsers.

<div class="note">

Wird dein Browser von deiner Arbeit oder Schule verwaltet, ist die Einstellung für sicheres DNS eventuell gesperrt. Frag deinen Administrator.

</div>
