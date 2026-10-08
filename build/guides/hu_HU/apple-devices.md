---
title: Hirdetések blokkolása Macen és Apple TV-n Blokada DNS-profllal.
description: Telepíts egy Blokada Cloud DNS-profilt a hirdetések és követők rendszer-szintű blokkolásához Mac-en vagy Apple TV-n, titkosított DNS-el, háttérben futó folyamat nélkül.
updated: 2026-10-02
order: 6
---

Az Apple készülékek képesek titkosított DNS-t használni az egész rendszer számára konfigurációs profilon keresztül. A Blokada profil a készüléket a Blokada Cloudhoz irányítja, amely minden alkalmazásban és böngészőben blokkolja a hirdetéseket és követőket.

Működik a macOS 11 (Big Sur), tvOS 14, iOS és iPadOS 14 vagy újabb verziókon.

<div class="if-no-device">

Ez az oldal még nem ismeri fel az eszközödet, ezért nem tudja felkínálni a profilodat. Jelentkezz be a vezérlőpultra, nyisd meg a _Beállítások_-at, válaszd ki az eszközöd, majd nyisd meg ezt az útmutatót az _Open on another device_ lehetőséggel.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Profil linkem lekérése</a></p>

</div>

## iPhone és iPad

A legegyszerűbb az alkalmazás használata. A [Blokada 6](https://go.blokada.org/appstore) mindent beállít helyetted, egy érintéssel be- vagy kikapcsolhatod a blokkolást, és megmutatja, mi lett blokkolva magán a telefonon. Jelentkezz be a fiókazonnosítóddal és kész is vagy.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Szerezd be a Blokada 6-ot az App Store-ban</a></p>

### Az alkalmazás nélkül

Alternatívaként profil is telepíthető. iPhone és iPad csak **Safari**-ból telepíthet profilt.

<div class="if-device">
<div class="if-other-browser note important">

Ez az oldal épp egy másik böngészőben van megnyitva. Másold ki a profil linked, és nyisd meg Safariban folytatáshoz: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Nyisd meg a _Beállítások_-at. Koppints a _Letöltött profil_-ra a tetején. Megtalálod a _Beállítások → Általános → VPN és eszközkezelés_ menüpont alatt is.
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}Profilom letöltése{% endappleProfile %}</p>

## Mac

1. Kattints az alábbi gombra a profil letöltéséhez.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Profilom letöltése{% endappleProfile %}</p>

## Apple TV

Az Apple TV-n nem lehet weboldalakat megnyitni, ezért oda kézzel kell beírni a profilod linkjét.

1. A profilod linkje: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. Jelöld ki a _Share Apple TV Analytics_-t. Ne válaszd ki, hanem a Play/Pause gombot nyomd meg a távirányítón.
4. Válaszd az _Add Profile_ lehetőséget és add meg a profil linkedet. Gépelni legegyszerűbb az iPhone billentyűzetes felugró ablakában, ott be is tudod illeszteni. Telepítsd a profilt és erősítsd meg.

<div class="note aside">

**Apple TV és más otthoni eszközök:** ha a Blokada Cloud-ot a [routeren](../router-ad-blocking/) állítod be, akkor az Apple TV is védelemben részesül, csakúgy mint minden más eszköz.

</div>

## Ellenőrizd a működést

Böngéssz egy percig, majd nyisd meg az _Aktivitás_ oldalt a [vezérlőpulton](https://app.blokada.org/stats?src=guides). Ennek az eszköznek a lekérdezései ott fognak megjelenni.

Ha később el szeretnéd távolítani a Blokadát, töröld a profilt abban az eszközben, ahová telepítetted.
