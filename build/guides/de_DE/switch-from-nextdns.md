---
title: Eine NextDNS-Alternative mit derselben Einrichtung auf jedem Gerät
description: Wechsle von NextDNS zu Blokada Cloud. Tausche deinen NextDNS-DNS-Namen, DoH-Link oder Profil auf deinem Telefon, Computer und Router gegen die von Blokada aus und behalte deinen Werbeblocker.
updated: 2026-09-28
order: 3
---

NextDNS und Blokada Cloud funktionieren auf die gleiche Weise: ein verschlüsselter DNS-Dienst, der Werbung und Tracker anhand ihres Namens blockiert. Deine eigenen Einstellungen bleiben hinter einem persönlichen DNS-Namen. Der Wechsel bedeutet, auf jedem Gerät die NextDNS-Werte durch deine Blokada-Werte zu ersetzen. Alles andere auf dem Gerät bleibt unverändert.

## Was du verwendet hast und was du in Blokada auswählen solltest

| In NextDNS                                                              | In Blokada Cloud                                                    |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Deine Konfigurations-ID, z. B. `abc123` | Dein Gerätekürzel, Teil deines Blokada-DNS-Namens und DoH-Links     |
| _Privatsphäre_-Sperrlisten                                              | _Sperrlisten_ im Dashboard                                          |
| _Sicherheit_ (Malware, Phishing)                     | eine Malware-Liste unter _Sperrlisten_                              |
| _Elterliche Kontrolle_                                                  | Listen für Erwachsenen- und Glücksspiel-Inhalte unter _Sperrlisten_ |
| _Ausnahmeliste_ und _Sperrliste_                                        | _Ausnahmen_ im Dashboard                                            |
| _Protokolle_ und _Analysen_                                             | _Aktivität_ und _Statistiken_ im Dashboard                          |

## Deine Blokada-Details

- Dein Blokada-DNS-Name für DNS über TLS: {% dot %}
- Dein DoH-Link für DNS über HTTPS: {% doh %}

## Jedes Gerät umstellen

### Android

Wenn du _Privates DNS_ mit `<dein-id>.dns.nextdns.io` verwendet hast, ersetze es durch deinen Blokada-DNS-Namen, wie im [Android-Leitfaden](../android-private-dns/). Wenn du die NextDNS-App verwendet hast, deinstalliere sie und installiere stattdessen [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone und iPad

Wenn du die NextDNS-App verwendet hast, deinstalliere sie und installiere [Blokada 6](https://go.blokada.org/appstore). Wenn du stattdessen ein NextDNS-Profil installiert hast, entferne es unter _Einstellungen → Allgemein → VPN & Geräteverwaltung_ und folge danach dem [Apple-Leitfaden](../apple-devices/).

### Mac und Apple TV

Entferne das NextDNS-Profil oder die App und installiere dann das Blokada-Profil aus dem [Apple-Leitfaden](../apple-devices/).

### Windows und Linux

Deinstalliere die NextDNS-App, falls du sie verwendest. Ersetze unter Windows den NextDNS-Server und die DoH-Vorlage durch die von Blokada, wie im [Windows-Leitfaden](../windows-dns-over-https/). Ersetze unter Linux den NextDNS-Server in systemd-resolved, wie im [Linux-Leitfaden](../linux-dns-over-tls/).

### Browser

Wenn du `https://dns.nextdns.io/…` als _sicheren DNS_ deines Browsers gesetzt hast, ersetze dies durch deinen DoH-Link, wie im [Browser-Leitfaden](../browser-dns-over-https/).

### Router

Wenn dein Router NextDNS über DNS über TLS oder DNS über HTTPS nutzt, ersetze den NextDNS-Namen oder Link durch deinen von Blokada, wie im [Router-Leitfaden](../router-ad-blocking/).

Wenn NextDNS über einfache IP-Adressen mit _verknüpfter IP_ genutzt wird, kann Blokada das derzeit noch nicht übernehmen. Die Unterstützung für Router mit einfachen DNS-Adressen ist in Vorbereitung. Bis dahin richte deine Geräte einzeln ein oder verwende einen Router, der verschlüsseltes DNS unterstützt.

## Überprüfen, ob alles funktioniert

Öffne ein paar Webseiten und sieh dir dann die Seite _Aktivität_ im Dashboard an. Dort siehst du die Abfragen deiner Geräte, wobei blockierte als solche markiert sind. Falls ein Gerät nicht erscheint, verwendet es noch immer NextDNS.
