---
title: Hirdetések blokkolása Windows rendszeren DNS over HTTPS használatával.
description: Használja a Windows 11-be épített titkosított DNS-t Blokada Cloud-dal, hogy blokkolja a hirdetéseket és követőket minden alkalmazásban és böngészőben, szoftver telepítése nélkül.
updated: 2026-10-02
order: 8
---

A Windows 11 képes az összes DNS-lekérdezést titkosítva, DNS over HTTPS-en keresztül továbbítani. Állítsa be a Blokada Cloud-ot, így minden alkalmazásban és böngészőben blokkolva lesznek a hirdetések és követők a számítógépen, külön szoftver telepítése nélkül.

Szüksége lesz a DNS szerver IP-címére és DoH hivatkozására, mindkettő megtalálható fent a _Saját adataim_ alatt.

## Windows 11

1. Nyissa meg a _Beállítások → Hálózat és internet_ menüt, majd válassza a _Wi-Fi_ vagy _Ethernet_ lehetőséget – attól függően, hogy a számítógép hogyan csatlakozik.
2. Nyissa meg a kapcsolat _Hardver tulajdonságait_. Wi-Fi esetén válassza a _Mentett hálózatok kezelése_ lehetőséget, majd a hálózatot, vagy a _Hardver tulajdonságok_ opciót a Wi-Fi oldal tetején.
3. A _DNS szerver hozzárendelés_ mellett válassza a _Szerkesztés_ lehetőséget. Válassza a _Kézi_ lehetőséget, és kapcsolja be az _IPv4_-et.
4. A _Elsődleges DNS_-hez írja be a DNS szervert: {% ip "doh" %}
5. Állítsa a _DNS over HTTPS_-t _Be (manuális sablon)_ értékre, majd illessze be DoH hivatkozását {% doh %} a _DoH sablon_ mezőbe.
6. Kapcsolja ki a _Visszatérés egyszerű szövegre_ lehetőséget, és válassza a _Mentés_ lehetőséget.

Ha a számítógép mind Wi-Fi-t, mind Ethernetet használ, ismételje meg ugyanezt a másik kapcsolatra is.

<div class="note important">

Hagyja üresen az _Alternatív DNS_ mezőt. A Windows mindkét szervert használja, és bármely másik szerveren átjuthatnak a hirdetések.

</div>

<div class="note tip">

Nincs _Be (manuális sablon)_ lehetőség? Az Ön Windows 11-e régebbi. Frissítse a Windowst, vagy használja addig a [böngésző útmutatót](../browser-dns-over-https/).

</div>

## Windows 10

A Windows 10-ben nincs beépített titkosított DNS. Állítson be biztonságos DNS-t a böngészőjében, ahogy a [böngésző útmutatóban](../browser-dns-over-https/) szerepel, vagy állítsa be [útválasztóját](../router-ad-blocking/), hogy az egész otthon védve legyen.

## Ellenőrizze, hogy működik-e

Nyisson meg néhány weboldalt, majd tekintse meg az _Aktivitás_ oldalt a [vezérlőpulton](https://app.blokada.org/stats?src=guides). Ennek a számítógépnek a lekérdezései ott jelennek meg.

<div class="note aside">

Ezen a számítógépen is szeretne VPN-t? A [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) WireGuard beállítást is tartalmaz, amely minden forgalmat titkosít, azonos blokkolással.

</div>

## Ha valami nem működik

A Chrome és az Edge saját _biztonságos DNS_ beállítással rendelkezik, amely megkerüli a Windows-t. Ha automatikusra van állítva, visszatérhet a sima DNS-re, amit a Blokada elutasít. Állítsa be a saját DoH hivatkozására:

- **Chrome:** Nyissa meg a `chrome://settings/security` oldalt, kapcsolja be a _Biztonságos DNS használata_ lehetőséget, majd a _DNS szolgáltató kiválasztása_ rész alatt válassza az _Egyéni DNS szolgáltató hozzáadása_ opciót.
- **Edge:** Nyissa meg az `edge://settings/privacy` oldalt, kapcsolja be a biztonságos DNS-t, majd válassza a _Szolgáltató választása_ lehetőséget.

Ezután illessze be DoH hivatkozását: {% doh %}

Ha egyes hirdetések még mindig átjutnak IPv6-os hálózaton, előfordulhat, hogy a Windows az útválasztó IPv6 DNS szerverét is lekérdezi. Kapcsolja ki az _Internet Protocol Version 6 (TCP/IPv6)_ opciót az adapter tulajdonságaiban (_Vezérlőpult → Hálózati kapcsolatok_), vagy állítsa be [útválasztóját](../router-ad-blocking/).
