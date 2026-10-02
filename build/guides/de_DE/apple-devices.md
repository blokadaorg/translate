---
title: Werbung auf Mac und Apple TV mit einem Blokada-DNS-Profil blockieren
description: Installiere ein Blokada-Cloud-DNS-Profil und blockiere Werbung und Tracker systemweit auf Mac oder Apple TV, verschlüsselt und ohne Hintergrund-App.
updated: 2026-10-02
order: 6
---

Apple-Geräte können über ein Konfigurationsprofil verschlüsseltes DNS für das ganze System nutzen. Das Blokada-Profil stellt das Gerät auf Blokada Cloud um, das Werbung und Tracker in allen Apps und Browsern blockiert.

Das funktioniert ab macOS 11 (Big Sur), tvOS 14 sowie iOS und iPadOS 14.

<div class="if-no-device">

Diese Seite kennt dein Gerät noch nicht und kann dir deshalb dein Profil nicht anbieten. Melde dich im Dashboard an, öffne _Einrichtung_, wähle dein Gerät und öffne diese Anleitung über _Auf einem anderen Gerät öffnen_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Meinen Profil-Link holen</a></p>

</div>

## iPhone und iPad

Am einfachsten geht es mit der App. [Blokada 6](https://go.blokada.org/appstore) richtet alles für dich ein, schaltet die Blockierung mit einem Tippen ein und aus und zeigt direkt auf dem Handy, was blockiert wurde. Melde dich mit deiner Konto-ID an, und du bist fertig.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Blokada 6 im App Store holen</a></p>

### Ohne App

Du kannst stattdessen das Profil installieren. iPhone und iPad installieren Profile nur aus **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Diese Seite ist in einem anderen Browser geöffnet. Kopiere deinen Link und öffne ihn in Safari, um dort weiterzumachen: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. Tippe in Safari auf den Button unten und dann auf _Erlauben_, um das Profil zu laden.
2. Öffne die _Einstellungen_. Tippe oben auf _Profil geladen_. Du findest es auch unter _Allgemein → VPN und Geräteverwaltung_.
3. Tippe auf _Installieren_, gib deinen Code ein und bestätige.

</div>

<p class="if-device if-safari">{% appleProfile %}Mein Profil laden{% endappleProfile %}</p>

## Mac

1. Klicke auf den Button unten, um das Profil zu laden.
2. Öffne die Liste der Profile: _Systemeinstellungen → Allgemein → Geräteverwaltung_ ab macOS 15, _Systemeinstellungen → Datenschutz & Sicherheit → Profile_ unter macOS 13 und 14 oder _Systemeinstellungen → Profile_ unter macOS 12 und älter.
3. Doppelklicke auf das Blokada-Profil und klicke auf _Installieren_.

<p class="if-device">{% appleProfile %}Mein Profil laden{% endappleProfile %}</p>

## Apple TV

Das Apple TV kann keine Webseiten öffnen, deshalb tippst du deinen Profil-Link dort ein.

1. Dein Profil-Link: {% appleUrl %}
2. Öffne auf dem Apple TV _Einstellungen → Allgemein → Datenschutz & Sicherheit_.
3. Markiere _Share Apple TV Analytics_. Wähle es nicht aus. Drücke stattdessen die Play/Pause-Taste auf der Fernbedienung.
4. Wähle _Add Profile_ und gib deinen Profil-Link ein. Am einfachsten tippst du über die Tastatur-Mitteilung auf deinem iPhone, dort kannst du ihn einfügen. Installiere das Profil und bestätige.

<div class="note aside">

**Apple TV und andere Geräte zu Hause:** Richtest du Blokada Cloud auf deinem [Router](../router-ad-blocking/) ein, ist das Apple TV zusammen mit allem anderen abgedeckt.

</div>

## Prüfen, ob es funktioniert

Surfe eine Minute lang und öffne dann die Seite _Aktivität_ im [Dashboard](https://app.blokada.org/stats?src=guides). Dort erscheinen die Anfragen dieses Geräts.

Um Blokada später zu entfernen, lösche das Profil dort, wo du es installiert hast.
