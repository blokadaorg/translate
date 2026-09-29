---
title: Mullvad DNS wird eingestellt. Werbung weiter blockieren mit Blokada Cloud
description: Mullvad schaltet sein öffentliches DNS am 2. November 2026 ab. So stellst du Handy, Computer und Router rechtzeitig um und blockierst weiter Werbung.
updated: 2026-09-23
order: 2
---

Mullvad stellt seinen kostenlosen öffentlichen DNS-Dienst am **2. November 2026** ein und empfiehlt stattdessen Quad9. Quad9 blockiert Malware, aber **keine** Werbung und keine Tracker. Hast du einen der filternden DNS-Namen von Mullvad genutzt, kommt die Werbung an diesem Tag zurück, wenn du nicht wechselst.

Diese Seite behandelt die öffentlichen DNS-Namen, die auf `dns.mullvad.net` enden. Um die Mullvad-VPN-App geht es hier nicht.

## Was du genutzt hast und was du in Blokada wählst

| Mullvad-DNS-Name | Was sie blockiert hat | Im Blokada-Dashboard |
|---|---|---|
| `dns.mullvad.net` | nichts | Blokada ist ein Filterdienst. Wenn du keine Filterung möchtest, ist Quad9 oder das DNS deines Anbieters die einfachere Wahl. |
| `adblock.dns.mullvad.net` | Werbung, Tracker | eine Blockliste für Werbung und Tracker |
| `base.dns.mullvad.net` | Werbung, Tracker, Malware | zusätzlich eine Malware-Liste |
| `extended.dns.mullvad.net` | base plus soziale Medien | zusätzlich eine Liste für soziale Medien |
| `family.dns.mullvad.net` | base plus Inhalte für Erwachsene und Glücksspiel | zusätzlich Listen für Erwachseneninhalte und Glücksspiel |
| `all.dns.mullvad.net` | alles oben Genannte | alle diese Listen einschalten |

Blocklisten wählst du im Dashboard unter *Blocklists*. Du kannst sie jederzeit ändern, und die Änderung gilt für alle deine Geräte.

## Deine Blokada-Daten

Blokada gibt jedem Gerät einen eigenen Namen, damit das Dashboard die Aktivität pro Gerät zeigen kann:

- Dein Blokada-DNS-Name, für DNS over TLS (Android, Router): {% dot %}
- Dein DoH-Link, für DNS over HTTPS (Browser, manche Router): {% doh %}

## Jedes Gerät umstellen

### Android

Laut der Mullvad-Anleitung hast du einen Hostnamen unter *Privates DNS* eingetragen. Ersetze ihn durch deinen Blokada-DNS-Namen. Die Schritte stehen in der [Android-Anleitung](../android-private-dns/).

### iPhone, iPad und Mac

Die Mullvad-Einrichtung nutzte ein Konfigurationsprofil. Entferne es zuerst:

- **iPhone und iPad:** *Einstellungen → Allgemein → VPN und Geräteverwaltung*, tippe auf das Mullvad-DNS-Profil und dann auf *Profil entfernen*.
- **Mac:** öffne die Liste der Profile (*Systemeinstellungen → Allgemein → Geräteverwaltung* ab macOS 15, *Systemeinstellungen → Datenschutz & Sicherheit → Profile* unter macOS 13 und 14, *Systemeinstellungen → Profile* unter macOS 12 und älter), wähle das Mullvad-DNS-Profil aus und klicke auf *−*.

Installiere dann das Blokada-Profil aus der [Apple-Anleitung](../apple-devices/).

### Browser

Hast du unter *sicheres DNS* oder *DNS over HTTPS* einen Mullvad-DoH-Link wie `https://adblock.dns.mullvad.net/dns-query` eingetragen, ersetze sie durch deinen DoH-Link. Die [Browser-Anleitung](../browser-dns-over-https/) enthält die Schritte für jeden Browser.

### Router

Nutzt dein Router Mullvad über DNS over TLS, ersetze den Mullvad-Hostnamen durch deinen Blokada-DNS-Namen und entferne die IP-Adressen von Mullvad. Die [Router-Anleitung](../router-ad-blocking/) behandelt gängige Modelle.

## Prüfen, ob es funktioniert

Öffne ein paar Websites und sieh dir dann die Seite *Aktivität* im Dashboard an. Dort siehst du die Anfragen deiner Geräte, blockierte sind markiert. Taucht ein Gerät nicht auf, nutzt es noch einen anderen DNS-Server.
