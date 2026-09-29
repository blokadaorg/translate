---
title: Eine NextDNS-Alternative mit derselben Einrichtung auf jedem Gerät
description: Wechsle von NextDNS zu Blokada Cloud. Ersetze NextDNS-DNS-Name, DoH-Link oder Profil auf Handy, Computer und Router und blockiere weiter Werbung.
updated: 2026-09-28
order: 3
---

NextDNS und Blokada Cloud funktionieren gleich: ein verschlüsselter DNS-Dienst, der Werbung und Tracker anhand ihres Namens blockiert, mit deinen eigenen Einstellungen hinter einem persönlichen DNS-Namen. Beim Wechsel ersetzt du auf jedem Gerät die NextDNS-Werte durch deine Blokada-Werte. Sonst ändert sich auf dem Gerät nichts.

## Was du genutzt hast und was du in Blokada wählst

| In NextDNS | In Blokada Cloud |
|---|---|
| Deine Konfigurations-ID, z. B. `abc123` | Dein Geräte-Tag, Teil deines Blokada-DNS-Namens und deines DoH-Links |
| *Privacy*-Blocklisten | *Blocklists* im Dashboard |
| *Security* (Malware, Phishing) | eine Malware-Liste unter *Blocklists* |
| *Parental control* | Listen für Erwachseneninhalte und Glücksspiel unter *Blocklists* |
| *Allowlist* und *Denylist* | *Ausnahmen* im Dashboard |
| *Logs* und *Analytics* | *Aktivität* und *Stats* im Dashboard |

## Deine Blokada-Daten

- Dein Blokada-DNS-Name, für DNS over TLS: {% dot %}
- Dein DoH-Link, für DNS over HTTPS: {% doh %}

## Jedes Gerät umstellen

### Android

Hast du *Privates DNS* mit `<your-id>.dns.nextdns.io` genutzt, ersetze es durch deinen Blokada-DNS-Namen, wie in der [Android-Anleitung](../android-private-dns/) beschrieben. Hast du die NextDNS-App genutzt, deinstalliere sie und installiere stattdessen [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone und iPad

Hast du die NextDNS-App genutzt, deinstalliere sie und installiere [Blokada 6](https://go.blokada.org/appstore). Hast du stattdessen ein NextDNS-Profil installiert, entferne es unter *Einstellungen → Allgemein → VPN und Geräteverwaltung* und folge dann der [Apple-Anleitung](../apple-devices/).

### Mac und Apple TV

Entferne das NextDNS-Profil oder die App und installiere dann das Blokada-Profil aus der [Apple-Anleitung](../apple-devices/).

### Windows und Linux

Deinstalliere die NextDNS-App, falls du sie nutzt. Ersetze unter Windows den NextDNS-Server und die DoH-Vorlage durch die von Blokada, wie in der [Windows-Anleitung](../windows-dns-over-https/) beschrieben. Ersetze unter Linux den NextDNS-Server in systemd-resolved, wie in der [Linux-Anleitung](../linux-dns-over-tls/) beschrieben.

### Browser

Hast du `https://dns.nextdns.io/…` als *sicheres DNS* in deinem Browser eingetragen, ersetze es durch deinen DoH-Link, wie in der [Browser-Anleitung](../browser-dns-over-https/) beschrieben.

### Router

Nutzt dein Router NextDNS über DNS over TLS oder DNS over HTTPS, ersetze den NextDNS-Namen oder -Link durch deinen von Blokada, wie in der [Router-Anleitung](../router-ad-blocking/) beschrieben.

Nutzt er NextDNS über einfache IP-Adressen mit einer *verknüpften IP* (*linked IP*), kann Blokada das noch nicht übernehmen. Unterstützung für Router mit einfachen DNS-Adressen ist in Arbeit. Bis dahin richtest du deine Geräte einzeln ein oder nutzt einen Router, der verschlüsseltes DNS unterstützt.

## Prüfen, ob es funktioniert

Öffne ein paar Websites und sieh dir dann die Seite *Aktivität* im Dashboard an. Dort siehst du die Anfragen deiner Geräte, blockierte sind markiert. Taucht ein Gerät nicht auf, nutzt es noch NextDNS.
