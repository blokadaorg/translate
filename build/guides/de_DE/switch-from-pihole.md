---
title: Eine Pi-hole Alternative ohne eigene Hardware
description: Verlege den Werbeblocker für dein Zuhause vom Pi-hole zu Blokada Cloud, oder behalte den Pi-hole und leite seine Anfragen über Blokada.
updated: 2026-09-23
order: 1
---

Ein Pi-hole blockiert Werbung für jedes Gerät in deinem Netzwerk, solange der Raspberry Pi läuft, aktuell ist und zu Hause steht. Blokada Cloud erledigt dasselbe von unseren Servern aus:

- **Keine Box, um die du dich kümmern musst.** Keine SD-Karten, keine Updates, kein Ausfall, wenn der Pi ausfällt.
- **Funktioniert auch unterwegs.** Handys und Laptops blockieren weiter, auch mobil und in anderen WLANs.
- **Verschlüsselt.** Geräte sprechen mit Blokada über DNS over TLS oder DNS over HTTPS, dein Anbieter kann deine Anfragen also weder lesen noch verändern.
- **Ein Dashboard.** Blocklisten, erlaubte und blockierte Domains und die Aktivität pro Gerät, unter [app.blokada.org](https://app.blokada.org/?src=guides).

Es gibt zwei Wege zum Wechsel: Ersetze den Pi-hole ganz, oder behalte ihn und nutze Blokada Cloud als Upstream.

## Option 1: den Pi-hole ersetzen

1. **Hol dir Blokada Cloud** und öffne das Dashboard. Unter *Einrichtung* findest du deine Daten:
   - Dein Blokada-DNS-Name, für DNS over TLS: {% dot %}
   - Dein DoH-Link, für DNS over HTTPS: {% doh %}
2. **Stelle deinen Router auf Blokada statt auf den Pi-hole um.** Folge der [Router-Anleitung](../router-ad-blocking/). Akzeptiert dein Router als DNS-Server nur eine einfache IP-Adresse, richte stattdessen deine Geräte einzeln ein: [Android](../android-private-dns/), [Mac und Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) und [Browser](../browser-dns-over-https/).
3. **War dein Pi-hole der DHCP-Server,** schalte DHCP in deinem Router wieder ein, *bevor* du den Pi ausschaltest. Sonst bekommen deine Geräte keine Netzwerkadressen mehr.
4. **Übertrage deine Listen.** Wähle im Dashboard unter *Blocklists* deine Blocklisten und füge unter *Ausnahmen* eigene erlaubte oder blockierte Domains hinzu.
5. **Schalte den Pi-hole aus,** oder nutze ihn für etwas anderes.

<div class="note">

Dein Pi-hole zeigte jedes Gerät im Netzwerk mit seiner IP-Adresse. Bei Blokada erscheint jedes Gerät mit seinem eigenen Namen, solange es seinen eigenen Blokada-DNS-Namen nutzt. Ein Router, der mit einem Blokada-DNS-Namen eingerichtet ist, erscheint als ein Gerät.

</div>

## Option 2: den Pi-hole behalten, Blokada Cloud als Upstream

Möchtest du deine lokale Einrichtung behalten, etwa lokale Hostnamen, DHCP oder eigene Listen, lass den Pi-hole seine Anfragen über eine verschlüsselte Verbindung an Blokada weiterleiten. Pi-hole kann selbst nicht verschlüsselt weiterleiten, deshalb läuft daneben eine kleine Weiterleitung. Diese Anleitung nutzt [dnsproxy](https://github.com/AdguardTeam/dnsproxy), eine Open-Source-Weiterleitung, die aus einer einzigen Datei besteht.

1. Lade auf dem Pi-hole-Rechner die `dnsproxy`-Version für deine CPU (`linux-arm64` für einen aktuellen Raspberry Pi) von der Release-Seite herunter und kopiere die Datei `dnsproxy` nach `/usr/local/bin/`.
2. Lege `/etc/systemd/system/dnsproxy.service` an:

<pre><code>[Unit]
Description=Encrypted DNS forwarder to Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Starte sie: `sudo systemctl enable --now dnsproxy`
4. Öffne im Pi-hole-Admin *Settings → DNS*. Entferne die Haken bei allen Upstream-Servern und füge `127.0.0.1#5054` als eigenen Upstream-Server hinzu. Speichere.
5. Sieh dir die Seite *Aktivität* im Dashboard an. Anfragen aus deinem Netzwerk erscheinen jetzt dort.

Du kannst die Blocklisten des Pi-hole ausschalten und die Blockierung im Dashboard verwalten, oder beides behalten.

## Häufige Fragen

**Brauche ich Blokada Plus?** Nein. Blokada Cloud deckt die DNS-Blockierung für dein ganzes Zuhause ab. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) ergänzt ein VPN.

**Was, wenn Blokada nicht erreichbar ist?** Deine Geräte können keine Namen auflösen, bis es wieder erreichbar ist, genau wie bei einem ausgefallenen Pi-hole. Trage keinen zweiten, ungefilterten DNS-Server als Fallback ein. Die meisten Geräte nutzen alle ihre Server zufällig, und so käme Werbung durch.
