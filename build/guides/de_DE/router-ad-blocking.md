---
title: Blockiere Werbung in deinem gesamten Netzwerk mit Router-basiertem Werbeblocker
description: Richte Blokada Cloud einmal auf deinem Router ein, und jedes Gerät zu Hause ist geschützt – einschließlich Fernsehern, Spielkonsolen und intelligenten Lautsprechern, die keinen Werbeblocker ausführen können.
updated: 2026-09-23
order: 4
---

Jedes Gerät in deinem Netzwerk fragt den Router, welchen DNS-Server es verwenden soll. Weise den Router an, Blokada Cloud zu nutzen, und Werbung und Tracker werden für alle dahinter liegenden Geräte blockiert. Dazu gehören Smart-TVs, Spielkonsolen, Streaming-Sticks und Smart-Home-Geräte, für die keine Werbeblocker-App verfügbar ist.

## Was dein Router benötigt

Dein Router muss **verschlüsseltes DNS mit Hostname** unterstützen, also DNS over TLS (DoT) oder DNS over HTTPS (DoH). Viele aktuelle Router unterstützen dies, einschließlich der unten aufgeführten Modelle. Je nachdem, was dein Router unterstützt, benötigst du:

- Für DNS over TLS, dein Blokada DNS-Name: {% dot %}
- Für DNS over HTTPS, dein DoH-Link: {% doh %}

<div class="note">

**Nur einfache IP-Adressen?** Viele Router von Internetanbietern akzeptieren nur einfache IP-Adressen für DNS. Die Unterstützung dafür ist in Vorbereitung. Bis dahin richte deine Geräte einzeln ein: [Android](../android-private-dns/), [Mac und Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) und [Browser](../browser-dns-over-https/). Du kannst auch einen kleinen Forwarder auf einem Raspberry Pi betreiben, wie im [Pi-hole-Leitfaden](../switch-from-pihole/) beschrieben.

</div>

## FRITZ!Box

FRITZ!OS 7.20 oder neuer.

1. Öffne `http://fritz.box` und gehe zu _Internet → Zugangsdaten → DNS-Server_.
2. Unter _Verschlüsselte Namensauflösung im Internet (DNS over TLS)_ aktiviere _Verschlüsselte Namensauflösung verwenden_.
3. Aktiviere _Zertifikatsüberprüfung für verschlüsselte Namensauflösung erzwingen_.
4. Deaktiviere _Fallback auf unverschlüsselte Namensauflösung zulassen_.
5. Gib unter _Resolver-Namen_ nur {% dot %} ein. **Entferne alle anderen Einträge.** Die FRITZ!Box verwendet alle aufgelisteten Resolver. Jeder weitere würde Werbung durchlassen.
6. Klicke auf _Übernehmen_.

## ASUS

Aktuelle ASUS-Firmware (3.0.0.4.388 oder neuer) und Asuswrt-Merlin.

1. Öffne die Router-Admin-Seite und gehe zu _WAN → Internetverbindung_.
2. Unter _WAN DNS-Einstellung_ stelle _DNS Privacy Protocol_ auf _DNS-over-TLS (DoT)_ und _DNS-over-TLS Profile_ auf _Strict_.
3. Entferne alle Einträge aus der _DNS-over-TLS Serverliste_ und füge dann einen hinzu:
   - Adresse: {% ip \"dot\" %}
   - TLS-Hostname: {% dot %}
4. Klicke auf _Übernehmen_.

## OpenWrt

1. Aktualisiere unter _System → Software_ die Listen und installiere `luci-app-https-dns-proxy`.
2. Öffne _Dienste → HTTPS DNS Proxy_. Lösche die Instanzen anderer Anbieter.
3. Füge eine Instanz mit einer benutzerdefinierten Resolver-URL hinzu: {% doh %}
4. _Speichern & Übernehmen_. Das Paket weist dnsmasq automatisch darauf hin.

## Andere Router

Suche nach einer Einstellung namens _DNS over TLS_, _Private DNS_, _Encrypted DNS_ oder _DNS over HTTPS_. Gib deinen Blokada DNS-Namen oder den DoH-Link von oben ein und entferne alle anderen DNS-Server, einschließlich Fallback-Servern.

## Überprüfe, ob alles funktioniert

1. Starte ein Gerät neu oder deaktiviere und aktiviere sein WLAN, damit die Änderung übernommen wird.
2. Surfe eine Minute und öffne dann die Seite _Aktivität_ im Dashboard. Die DNS-Abfragen deines Netzwerks werden dort angezeigt.

Einige Geräte umgehen den Router: Handys mit aktiviertem _Private DNS_, Browser mit eigenem _sicherem DNS_-Anbieter und Geräte, die ihren eigenen DNS fest eintragen. Konfiguriere diese direkt auf dem Gerät oder deaktiviere die eigene DNS-Einstellung.

<div class="note">

Hinter dem Router teilen sich alle Geräte eine Adresse, sodass das Dashboard dein Netzwerk als einzelnes Gerät anzeigt. Richte Handys und Laptops mit eigenem Blokada DNS-Namen ein, wenn du sie einzeln sehen möchtest. Sie bleiben auch dann geschützt, wenn sie das Haus verlassen.

</div>
