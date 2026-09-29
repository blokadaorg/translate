---
title: Werbung auf Mac und Apple TV mit einem Blokada DNS-Profil blockieren
description: Installiere ein Blokada Cloud DNS-Profil, um Werbung und Tracker systemweit auf einem Mac oder Apple TV zu blockieren – mit verschlüsseltem DNS und ohne dass etwas im Hintergrund läuft.
updated: 2026-09-28
order: 6
---

Apple-Geräte können verschlüsselten DNS für das gesamte System über ein Konfigurationsprofil verwenden. Das Blokada-Profil leitet das Gerät zu Blokada Cloud, wodurch Werbung und Tracker in jeder App und jedem Browser blockiert werden.

Es funktioniert unter macOS 11 (Big Sur), tvOS 14, iOS und iPadOS 14 und neuer.

<div class="if-no-device">

Diese Seite kennt dein Gerät noch nicht und kann dein Profil daher nicht anbieten. Melde dich im Dashboard an, öffne _Setup_, wähle dein Gerät aus und öffne diese Anleitung mit _Auf anderem Gerät öffnen_.

<p><a class=\"btn btn-outline\" href=\"https://app.blokada.org/setup?src=guides\">Profil-Link abrufen</a></p>

</div>

## iPhone und iPad

Am einfachsten geht es mit der App. [Blokada 6](https://go.blokada.org/appstore) richtet alles für dich ein, aktiviert und deaktiviert das Blockieren mit einem Fingertipp und zeigt, was direkt auf dem Handy blockiert wurde. Melde dich mit deiner Konto-ID an, und schon bist du fertig.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/appstore\">Blokada 6 im App Store herunterladen</a></p>

### Ohne die App

Du kannst stattdessen das Profil installieren. iPhone und iPad installieren Profile ausschließlich über **Safari**.

<div class="if-device">
<div class="if-other-browser note">

Diese Seite ist in einem anderen Browser geöffnet. Kopiere deinen Link und öffne ihn in Safari, um dort fortzufahren: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. Tippe in Safari auf die Schaltfläche unten und erlaube den Download des Profils mit _Zulassen_.
2. Einstellungen öffnen. Tippe oben auf _Profil geladen_. Du findest es auch unter _Allgemein → VPN & Geräteverwaltung_.
3. Tippe auf _Installieren_, gib deinen Code ein und bestätige.

</div>

<p class="if-device if-safari">{% appleProfile %}Mein Profil herunterladen{% endappleProfile %}</p>

## Mac

1. Klicke auf die Schaltfläche unten, um das Profil herunterzuladen.
2. Öffne die Liste der Profile: _Systemeinstellungen → Allgemein → Geräteverwaltung_ ab macOS 15, _Systemeinstellungen → Datenschutz & Sicherheit → Profile_ auf macOS 13 und 14 oder _Systemeinstellungen → Profile_ auf macOS 12 und älter.
3. Doppelklicke auf das Blokada-Profil und klicke auf _Installieren_.

<p class="if-device">{% appleProfile %}Mein Profil herunterladen{% endappleProfile %}</p>

## Apple TV

Der Apple TV kann keine Webseiten öffnen, deshalb gibst du deinen Profil-Link dort ein.

1. Dein Profil-Link: {% appleUrl %}
2. Öffne auf dem Apple TV _Einstellungen → Allgemein → Datenschutz & Sicherheit_.
3. Markiere _An Apple senden_ (auf älterem tvOS heißt es _Apple TV Analytics teilen_). Nicht auswählen. Drücke stattdessen die Wiedergabe/Pause-Taste auf der Fernbedienung.
4. Wähle _Profil hinzufügen_ und gib deinen Profil-Link ein. Das Tippen geht am einfachsten über die Tastatur-Eingabeaufforderung auf deinem iPhone, wo du ihn einfügen kannst. Installiere das Profil und bestätige.

<div class="note">

**Apple TV und andere Geräte zu Hause:** Wenn du Blokada Cloud auf deinem [Router](../router-ad-blocking/) einrichtest, ist der Apple TV ebenso wie alle anderen Geräte abgedeckt.

</div>

## Überprüfen, ob es funktioniert

Surfe eine Minute, dann öffne die _Aktivitäts_-Seite im [Dashboard](https://app.blokada.org/stats?src=guides). Die Anfragen dieses Geräts werden dort angezeigt.

Um Blokada später zu entfernen, lösche das Profil, wo du es installiert hast.
