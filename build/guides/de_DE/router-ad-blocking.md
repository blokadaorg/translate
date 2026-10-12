---
title: Werbung im ganzen Netzwerk blockieren mit einem Router-Werbeblocker
description: Richte Blokada Cloud einmal im Router ein und blockiere Werbung auf allen Geräten in deinem Zuhause, auch auf Smart-TV, Spielkonsole und Smart Speaker.
updated: 2026-10-09
order: 4
---

Jedes Gerät in deinem Netzwerk fragt den Router, welchen DNS-Server es nutzen soll. Stellst du den Router auf Blokada Cloud um, werden Werbung und Tracker für alles dahinter blockiert. Dazu gehören Smart-TVs, Spielkonsolen, Streaming-Sticks und Smart-Home-Geräte, auf denen kein Platz für eine Werbeblocker-App ist.

## Was dein Router können muss

Es gibt zwei Möglichkeiten, einen Router einzurichten:

- **Verschlüsseltes DNS mit Hostnamen**, also DNS over TLS (DoT) oder DNS over HTTPS (DoH). Viele neuere Router unterstützen das, darunter die unten aufgeführten Modelle. Je nachdem, was dein Router unterstützt, benötigst du entweder deinen DNS-Namen oder deinen DoH-Link, beide findest du oben unter _Deine Daten_.
- **Eine einfache IPv6-DNS-Adresse.** Viele Router von Internetanbietern akzeptieren nur einfache IP-Adressen für DNS. Wenn das bei deinem Router der Fall ist und deine Verbindung IPv6 hat, stellt dir Blokada eine IPv6-Adresse zur Verfügung, die du eintragen kannst. Siehe [Router, die nur eine IP-Adresse akzeptieren](#routers-that-only-take-an-ip-address).

Verwende verschlüsseltes DNS, wenn dein Router dies unterstützt. So bleiben Anfragen auf dem Weg zu Blokada privat.

## FRITZ!Box

FRITZ!OS 7.20 oder neuer.

1. Öffne `http://fritz.box`, gehe zu _Internet → Zugangsdaten_ und dann auf die Registerkarte _DNS-Server_.
2. Aktiviere die Option _Verschlüsselte Namensauflösung im Internet (DNS over TLS)_.
3. Trage im Eingabefeld _Auflösungsnamen der DNS-Server_ nur {% dot %} ein. **Entferne alle anderen Einträge.** Die FRITZ!Box nutzt alle eingetragenen Resolver, und jeder andere lässt Werbung durch.
4. Setze den Haken bei _Zertifikatsprüfung für verschlüsselte Namensauflösung im Internet erzwingen_ und entferne ihn bei _Fallback auf unverschlüsselte Namensauflösung im Internet zulassen_.
5. Siehst du die Option _Bei DNS-Störungen auf öffentliche DNS-Server zurückgreifen_, deaktiviere sie.
6. Klicke auf _Übernehmen_.

## ASUS

ASUS-Firmware neuer als 3.0.0.4.386.4xxxx und Asuswrt-Merlin.

1. Öffne die Admin-Seite des Routers und gehe zu _WAN → Internet Connection_.
2. Stelle unter _WAN DNS Setting_ das _DNS Privacy Protocol_ auf _DNS-over-TLS (DoT)_ und das _DNS-over-TLS Profile_ auf _Strict_.
3. Entferne alle Einträge aus der _DNS-over-TLS Server List_ und füge dann einen hinzu:
   - Address: {% ip "dot" %}
   - TLS Hostname: {% dot %}
4. Klicke auf _Apply_.

## OpenWrt

1. Aktualisiere unter _System → Software_ die Listen und installiere `luci-app-https-dns-proxy`.
2. Öffne _Services → HTTPS DNS Proxy_. Lösche die Instanzen anderer Anbieter.
3. Füge eine Instanz mit eigener Resolver-URL hinzu: {% doh %}
4. _Save & Apply_. Das Paket leitet dnsmasq automatisch darauf um.

## Andere Router

Suche nach einer Einstellung namens _DNS over TLS_, _Privates DNS_, _Verschlüsseltes DNS_ oder _DNS over HTTPS_. Gib deinen Blokada-DNS-Namen oder den DoH-Link von oben ein und entferne alle anderen DNS-Server, einschließlich Fallback-Server. Falls es keine solche Einstellung gibt, verwende wie unten beschrieben eine einfache IPv6-Adresse.

## Router, die nur eine IP-Adresse akzeptieren {:#routers-that-only-take-an-ip-address}

Dein Router und deine Internetverbindung benötigen hierfür IPv6. Die Unterstützung für einfache IPv4-Adressen folgt später.

1. Öffne im [Dashboard](https://app.blokada.org/setup?src=guides) den Bereich _Einrichtung_ und wähle _Router, TV, Spielkonsole_.
2. Gib dem Router einen Namen, zum Beispiel _Heimrouter_, und wähle _Adresse abrufen_. Der Name erscheint in deiner Aktivität und kann später nicht geändert werden.
3. Finde in den Einstellungen des Routers die DNS-Server für IPv6, meist unter _Internet_, _WAN_ oder _IPv6_, und trage die Adresse als einzigen DNS-Server ein.
4. **Entferne alle anderen DNS-Server, einschließlich IPv4.** Geräte, die vom Router weiterhin einen IPv4-DNS-Server erhalten, schicken einige Anfragen an Blokada vorbei. Falls der Router kein leeres IPv4-DNS zulässt, richte deine Geräte stattdessen einzeln ein: [Android](../android-private-dns/), [Mac und Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) und [Browser](../browser-dns-over-https/).

Die gleiche Einrichtung funktioniert für Fernseher oder Spielkonsolen, bei denen man einen DNS-Server manuell eingeben kann. Vergib für jedes Gerät eine eigene Adresse, damit es namentlich in deiner Aktivität erscheint.

<div class="note aside">

Diese Anfragen werden wie bei jedem normalen DNS-Server unverschlüsselt zu Blokada übertragen. Falls dein Router DNS over TLS oder DNS over HTTPS unterstützt, nutze stattdessen diese Optionen.

</div>

## Prüfen, ob es funktioniert

1. Starte ein Gerät neu oder schalte sein WLAN aus und wieder ein, damit es die Änderung übernimmt.
2. Deaktiviere auf diesem Gerät Blokada, falls die App ausgeführt wird, und öffne dann [go.blokada.org/test](https://go.blokada.org/test). Die Seite zeigt an, ob dein DNS über Blokada läuft.
3. Surfe eine Minute lang und öffne dann die Seite _Aktivität_ im [Dashboard](https://app.blokada.org/stats?src=guides). Dort erscheinen die Anfragen deines Netzwerks.

## Wenn manche Geräte noch Werbung zeigen

Manche Geräte umgehen den Router: Handys mit eingerichtetem _Privatem DNS_, Browser, deren _sicheres DNS_ auf einen anderen Anbieter eingestellt ist, und Geräte mit fest eingebautem eigenem DNS. Richte diese direkt auf dem Gerät ein oder schalte ihre eigene DNS-Einstellung aus.

<div class="note tip">

Hinter dem Router teilen sich alle Geräte eine Adresse, deshalb zeigt das Dashboard dein Netzwerk als ein einziges Gerät. Richte Handys und Laptops mit ihrem eigenen Blokada-DNS-Namen ein, wenn du sie einzeln sehen möchtest. So bleibt ihre Blockierung auch unterwegs aktiv.

</div>
