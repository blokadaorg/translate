---
title: Mullvad DNS wird eingestellt. Behalte deine Werbeblockierung mit Blokada Cloud
description: Mullvad stellt seinen öffentlichen DNS-Dienst am 2. November 2026 ein. So stellst du dein Handy, deinen Computer und deinen Router rechtzeitig auf Blokada Cloud um – ohne dass die Werbeblockierung verloren geht.
updated: 2026-09-23
order: 2
---

Mullvad stellt seinen kostenlosen öffentlichen DNS-Dienst am **2. November 2026** ein und empfiehlt stattdessen Quad9. Quad9 blockiert Malware, blockiert aber **keine** Werbung oder Tracker. Wenn du einen der filternden DNS-Namen von Mullvad verwendet hast, werden ab diesem Datum wieder Werbung angezeigt, sofern du nichts änderst.

Diese Seite behandelt die öffentlichen DNS-Namen, die auf `dns.mullvad.net` enden. Die Mullvad VPN-App wird hier nicht behandelt.

## Was du genutzt hast und was du in Blokada auswählen solltest

| Mullvad DNS-Name           | Was blockiert wurde                              | Im Blokada-Dashboard                                                                                                                                          |
| -------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | nichts                                           | Blokada ist ein Filter-Dienst. Wenn du keine Filterung wünschst, ist Quad9 oder der DNS deines Anbieters die einfachere Wahl. |
| `adblock.dns.mullvad.net`  | Werbung, Tracker                                 | eine Sperrliste für Werbung und Tracker                                                                                                                       |
| `base.dns.mullvad.net`     | Werbung, Tracker, Malware                        | eine Malware-Sperrliste hinzufügen                                                                                                                            |
| `extended.dns.mullvad.net` | Base plus soziale Medien                         | eine Sperrliste für soziale Medien hinzufügen                                                                                                                 |
| `family.dns.mullvad.net`   | Base plus Inhalte für Erwachsene und Glücksspiel | Sperrlisten für Inhalte für Erwachsene und Glücksspiel hinzufügen                                                                                             |
| `all.dns.mullvad.net`      | alles oben genannte                              | alle aktivieren                                                                                                                                               |

Du wählst Sperrlisten im Dashboard unter _Sperrlisten_ aus. Du kannst sie jederzeit ändern und die Änderung gilt für all deine Geräte.

## Deine Blokada-Details

Blokada gibt jedem Gerät einen eigenen Namen, sodass das Dashboard die Aktivitäten pro Gerät anzeigen kann:

- Dein Blokada-DNS-Name, für DNS über TLS (Android, Router): {% dot %}
- Dein DoH-Link, für DNS über HTTPS (Browser, einige Router): {% doh %}

## Jedes Gerät umstellen

### Android

Die Anleitung von Mullvad hat dich aufgefordert, einen Hostnamen unter _Privates DNS_ einzugeben. Ersetze ihn durch deinen Blokada-DNS-Namen. Die [Android-Anleitung](../android-private-dns/) enthält die einzelnen Schritte.

### iPhone, iPad und Mac

Die Einrichtung bei Mullvad verwendete ein Konfigurationsprofil. Entferne dieses zuerst:

- **iPhone und iPad:** _Einstellungen → Allgemein → VPN & Geräteverwaltung_, das Mullvad-DNS-Profil antippen und dann _Profil entfernen_.
- **Mac:** Öffne die Liste der Profile (_Systemeinstellungen → Allgemein → Geräteverwaltung_ ab macOS 15, _Systemeinstellungen → Datenschutz & Sicherheit → Profile_ bei macOS 13 und 14, _Systemeinstellungen → Profile_ bei macOS 12 und früher), wähle das Mullvad-DNS-Profil aus und klicke auf _−_.

Installiere danach das Blokada-Profil aus der [Apple-Anleitung](../apple-devices/).

### Browser

Wenn du einen Mullvad-DoH-Link wie `https://adblock.dns.mullvad.net/dns-query` unter _sicheres DNS_ oder _DNS über HTTPS_ eingegeben hast, ersetze ihn durch deinen DoH-Link. Die [Browser-Anleitung](../browser-dns-over-https/) enthält die Schritte für jeden Browser.

### Router

Wenn dein Router Mullvad über DNS über TLS nutzt, ersetze den Mullvad-Hostnamen durch deinen Blokada-DNS-Namen und entferne die IP-Adressen von Mullvad. Die [Router-Anleitung](../router-ad-blocking/) behandelt gängige Modelle.

## Teste, ob es funktioniert

Öffne ein paar Webseiten und schaue dann auf die Seite _Aktivität_ im Dashboard. Dort siehst du die Anfragen deiner Geräte – blockierte werden markiert. Wenn ein Gerät nicht angezeigt wird, verwendet es noch einen anderen DNS-Server.
