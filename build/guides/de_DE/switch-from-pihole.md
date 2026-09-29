---
title: Eine Pi-hole-Alternative, die keine Hardware benötigt.
description: Verschiebe das Werbeblocking deines Zuhauses von einem Pi-hole zu Blokada Cloud oder behalte dein Pi-hole und leite dessen Anfragen über Blokada.
updated: 2026-09-23
order: 1
---

Ein Pi-hole blockiert Werbung für jedes Gerät in deinem Netzwerk, solange der Raspberry Pi läuft, aktualisiert ist und zu Hause steht. Blokada Cloud übernimmt die gleiche Aufgabe von unseren Servern:

- **Keine Box zu warten.** Keine SD-Karten, keine Updates, kein Ausfall, wenn der Pi abstürzt.
- **Funktioniert auch unterwegs.** Smartphones und Laptops blockieren weiterhin Werbung über mobile Daten und andere Wi-Fi-Netzwerke.
- **Verschlüsselt.** Geräte kommunizieren mit Blokada über DNS-over-TLS oder DNS-over-HTTPS, sodass dein Anbieter deine Anfragen nicht lesen oder verändern kann.
- **Ein zentrales Dashboard.** Sperrlisten, erlaubte und gesperrte Domains sowie Aktivitäten pro Gerät unter [app.blokada.org](https://app.blokada.org/?src=guides).

Es gibt zwei Möglichkeiten zu wechseln. Ersetze das Pi-hole vollständig oder behalte es und verwende Blokada Cloud als Upstream.

## Option 1: Pi-hole ersetzen

1. **Blokada Cloud beziehen** und das Dashboard öffnen. Unter _Setup_ findest du deine Details:
   - Dein Blokada-DNS-Name für DNS-over-TLS: {% dot %}
   - Dein DoH-Link für DNS-over-HTTPS: {% doh %}
2. **Stelle deinen Router auf Blokada statt auf das Pi-hole ein.** Folge der [Router-Anleitung](../router-ad-blocking/). Wenn dein Router nur eine einfache IP-Adresse als DNS-Server akzeptiert, richte deine Geräte einzeln ein: [Android](../android-private-dns/), [Mac und Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) und [Browser](../browser-dns-over-https/).
3. **Falls dein Pi-hole als DHCP-Server fungiert**, aktiviere DHCP im Router _bevor_ du den Pi ausschaltest. Andernfalls erhalten deine Geräte keine Netzwerkadressen mehr.
4. **Übertrage deine Listen.** Wähle im Dashboard Sperrlisten unter _Sperrlisten_ und trage eigene erlaubte oder gesperrte Domains unter _Ausnahmen_ ein.
5. **Schalte das Pi-hole aus** oder nutze es für andere Aufgaben.

<div class="note">

Dein Pi-hole zeigte jedes Gerät im Netzwerk über dessen IP-Adresse an. Mit Blokada wird jedes Gerät mit seinem eigenen Namen angezeigt, solange es seinen eigenen Blokada-DNS-Namen nutzt. Ein Router, der mit einem Blokada-DNS-Namen konfiguriert ist, erscheint als ein einzelnes Gerät.

</div>

## Option 2: Pi-hole behalten, Blokada Cloud als Upstream nutzen

Wenn du deine lokale Konfiguration behalten willst, z. B. lokale Hostnamen, DHCP oder eigene Listen, lasse das Pi-hole seine Anfragen verschlüsselt an Blokada weiterleiten. Pi-hole kann keine verschlüsselte Weiterleitung selbst übernehmen, daher läuft ein kleiner Forwarder daneben. Diese Anleitung verwendet [dnsproxy](https://github.com/AdguardTeam/dnsproxy), einen Open-Source-Forwarder, der nur aus einer Datei besteht.

1. Lade auf dem Pi-hole-Gerät das `dnsproxy`-Release für deine CPU ("linux-arm64" für ein aktuelles Raspberry Pi) von der Releases-Seite herunter und kopiere die `dnsproxy`-Binary nach `/usr/local/bin/`.
2. Erstelle `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Verschlüsselter DNS-Forwarder zu Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Starte ihn: `sudo systemctl enable --now dnsproxy`
4. Im Pi-hole-Admin _Einstellungen → DNS_ öffnen. Entferne alle Upstream-Server und füge `127.0.0.1#5054` als benutzerdefinierten Upstream-Server hinzu. Speichern.
5. Prüfe die Seite _Aktivität_ im Dashboard. Anfragen aus deinem Netzwerk werden dort nun angezeigt.

Du kannst die eigenen Sperrlisten des Pi-hole deaktivieren und die Blockierung im Dashboard verwalten oder beides nutzen.

## Häufig gestellte Fragen

**Brauche ich Blokada Plus?** Nein. Blokada Cloud deckt das DNS-Blocking für dein ganzes Zuhause ab. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) fügt eine VPN-Funktion hinzu.

**Was passiert, wenn Blokada nicht erreichbar ist?** Deine Geräte können keine Namen auflösen, bis es wiederhergestellt ist – genauso, wie wenn ein Pi-hole ausfällt. Füge keinen zweiten, ungefilterten DNS-Server als Fallback hinzu. Die meisten Geräte nutzen alle ihre Server zufällig, sodass Werbung durchkommen würde.
