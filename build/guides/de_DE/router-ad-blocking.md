---
title: Werbung im ganzen Netzwerk blockieren mit einem Router-Werbeblocker
description: Richte Blokada Cloud einmal im Router ein und blockiere Werbung auf allen Geräten in deinem Zuhause, auch auf Smart-TV, Spielkonsole und Smart Speaker.
updated: 2026-09-23
order: 4
---

Jedes Gerät in deinem Netzwerk fragt den Router, welchen DNS-Server es nutzen soll. Stellst du den Router auf Blokada Cloud um, werden Werbung und Tracker für alles dahinter blockiert. Dazu gehören Smart-TVs, Spielkonsolen, Streaming-Sticks und Smart-Home-Geräte, auf denen kein Platz für eine Werbeblocker-App ist.

## Was dein Router können muss

Dein Router muss **verschlüsseltes DNS mit Hostnamen** unterstützen, also DNS over TLS (DoT) oder DNS over HTTPS (DoH). Viele neuere Router können das, darunter die Modelle unten. Je nachdem, was dein Router unterstützt, brauchst du:

- Für DNS over TLS deinen Blokada-DNS-Namen: {% dot %}
- Für DNS over HTTPS dein DoH-Link: {% doh %}

<div class="note">

**Nur einfache IP-Adressen?** Viele Router von Internetanbietern akzeptieren für DNS nur einfache IP-Adressen. Unterstützung dafür ist in Arbeit. Bis dahin richtest du deine Geräte einzeln ein: [Android](../android-private-dns/), [Mac und Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) und [Browser](../browser-dns-over-https/). Du kannst auch eine kleine Weiterleitung auf einem Raspberry Pi betreiben, wie in der [Pi-hole-Anleitung](../switch-from-pihole/) beschrieben.

</div>

## FRITZ!Box

FRITZ!OS 7.20 oder neuer.

1. Öffne `http://fritz.box` und gehe zu _Internet → Zugangsdaten → DNS-Server_.
2. Setze unter _Verschlüsselte Namensauflösung im Internet (DNS over TLS)_ den Haken bei _Verschlüsselte Namensauflösung verwenden_.
3. Setze den Haken bei _Zertifikatsprüfung für verschlüsselte Namensauflösung im Internet erzwingen_.
4. Entferne den Haken bei _Fallback auf unverschlüsselte Namensauflösung im Internet erlauben_.
5. Trage unter _Auflösungsnamen_ nur {% dot %} ein. **Entferne alle anderen Einträge.** Die FRITZ!Box nutzt alle eingetragenen Resolver, und jeder andere lässt Werbung durch.
6. Klicke auf _Übernehmen_.

## ASUS

Aktuelle ASUS-Firmware (3.0.0.4.388 oder neuer) und Asuswrt-Merlin.

1. Öffne die Admin-Seite des Routers und gehe zu _WAN → Internet Connection_.
2. Stelle unter _WAN DNS Setting_ das _DNS Privacy Protocol_ auf _DNS-over-TLS (DoT)_ und das _DNS-over-TLS Profile_ auf _Strict_.
3. Entferne alle Einträge aus der _DNS-over-TLS Server List_ und füge dann einen hinzu:
   - Adresse: {% ip \"dot\" %}
   - TLS-Hostname: {% dot %}
4. Klicke auf _Apply_.

## OpenWrt

1. Aktualisiere unter _System → Software_ die Listen und installiere `luci-app-https-dns-proxy`.
2. Öffne _Services → HTTPS DNS Proxy_. Lösche die Instanzen anderer Anbieter.
3. Füge eine Instanz mit eigener Resolver-URL hinzu: {% doh %}
4. _Speichern & Übernehmen_. Das Paket leitet dnsmasq automatisch darauf um.

## Andere Router

Suche nach einer Einstellung namens _DNS over TLS_, _Privates DNS_, _Verschlüsseltes DNS_ oder _DNS over HTTPS_. Trage deinen Blokada-DNS-Namen oder DoH-Link von oben ein und entferne alle anderen DNS-Server, auch Fallback-Server.

## Prüfen, ob es funktioniert

1. Starte ein Gerät neu oder schalte sein WLAN aus und wieder ein, damit es die Änderung übernimmt.
2. Surfe eine Minute lang und öffne dann die Seite _Aktivität_ im Dashboard. Dort erscheinen die Anfragen aus deinem Netzwerk.

Manche Geräte umgehen den Router: Handys mit eingerichtetem _Privatem DNS_, Browser, deren _sicheres DNS_ auf einen anderen Anbieter eingestellt ist, und Geräte mit fest eingebautem eigenem DNS. Richte diese direkt auf dem Gerät ein oder schalte ihre eigene DNS-Einstellung aus.

<div class="note">

Hinter dem Router teilen sich alle Geräte eine Adresse, deshalb zeigt das Dashboard dein Netzwerk als ein einziges Gerät. Richte Handys und Laptops mit ihrem eigenen Blokada-DNS-Namen ein, wenn du sie einzeln sehen möchtest. So bleibt ihre Blockierung auch unterwegs aktiv.

</div>
