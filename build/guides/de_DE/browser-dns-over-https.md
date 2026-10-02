---
title: Werbung in Chrome, Firefox, Edge und Brave mit DNS over HTTPS blockieren
description: Stelle Blokada Cloud als sicheres DNS im Browser ein und blockiere Werbung und Tracker auf jedem Computer, auch auf Arbeitslaptops ohne App-Installation.
updated: 2026-09-23
order: 7
---

Moderne Browser können einen eigenen verschlüsselten DNS-Anbieter nutzen, genannt *sicheres DNS* oder *DNS over HTTPS*. Stellst du dort Blokada Cloud ein, blockiert der Browser Werbung und Tracker in jedem Netz, ganz ohne Erweiterung.

Diese Einstellung gilt nur für diesen Browser. Für den ganzen Computer nutzt du auf dem Mac das [Apple-Profil](../apple-devices/) oder richtest deinen [Router](../router-ad-blocking/) ein.

Dein DoH-Link: {% doh %}

## Chrome

1. Öffne `chrome://settings/security`.
2. Schalte *Sicheres DNS verwenden* ein und wähle dann *Add custom DNS service provider*.
3. Gib {% doh %} ein.

## Edge

1. Öffne `edge://settings/privacy`.
2. Schalte unter *Sicherheit* die Option *Use secure DNS to specify how to look up the network address for websites* ein.
3. Wähle *Choose a service provider* und gib {% doh %} ein.

## Firefox

1. Öffne *Einstellungen → Datenschutz & Sicherheit* und scrolle zu *DNS über HTTPS*.
2. Wähle *Maximaler Schutz*.
3. Wähle unter *Anbieter auswählen* die Option *Benutzerdefiniert* und gib {% doh %} ein.

## Brave

1. Öffne `brave://settings/security`.
2. Schalte *Sicheres DNS verwenden* ein und wähle dann *Add custom DNS service provider*.
3. Gib {% doh %} ein.

## Safari

Safari hat keine eigene Einstellung für sicheres DNS. Es nutzt das DNS des Systems, installiere also das [Apple-Profil](../apple-devices/).

## Prüfen, ob es funktioniert

Surfe eine Minute lang und öffne dann die Seite *Aktivität* im [Dashboard](https://app.blokada.org/stats?src=guides). Dort erscheinen die Anfragen dieses Browsers.

<div class="note">

Wird dein Browser von deiner Arbeit oder Schule verwaltet, ist die Einstellung für sicheres DNS eventuell gesperrt. Frag deinen Administrator.

</div>
