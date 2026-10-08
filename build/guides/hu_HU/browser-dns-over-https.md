---
title: Hirdetések blokkolása a Chrome, Firefox, Edge és Brave böngészőkben DNS over HTTPS használatával.
description: Állítsd be a Blokada Cloudot biztonságos DNS szolgáltatóként a böngésződben, hogy blokkolhasd a hirdetéseket és követőket bármilyen számítógépen, beleértve a munkahelyi laptopokat is, ahol nem tudsz alkalmazásokat telepíteni.
updated: 2026-10-02
order: 7
---

A modern böngészők képesek saját titkosított DNS szolgáltatót használni, amelyet _biztonságos DNS_-nek vagy _DNS over HTTPS_-nek nevezünk. Állítsd be a Blokada Cloudot, és a böngésző blokkolja a hirdetéseket és követőket bármely hálózaton, bővítmény telepítése nélkül.

Ez a beállítás csak erre a böngészőre vonatkozik. Az egész számítógép védelméhez használd az [Apple-profilt](../apple-devices/) Mac-en, vagy állítsd be az [útválasztót](../router-ad-blocking/).

## Chrome

1. Nyisd meg a következőt: `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Írd be: {% doh %}

## Edge

1. Nyisd meg a következőt: `edge://settings/privacy`.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. Nyisd meg a következőt: `brave://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Írd be: {% doh %}

## Safari

A Safarinak nincs saját biztonságos DNS beállítása. A rendszer DNS-t használja, ezért telepítsd az [Apple-profilt](../apple-devices/).

## Ellenőrizd, hogy működik-e

Böngéssz egy percig, majd nyisd meg az _Aktivitás_ oldalt a [vezérlőpultban](https://app.blokada.org/stats?src=guides). Ennek a böngészőnek a lekérdezései ott jelennek meg.

## Ha valami nem működik

<div class="note tip">

Ha a böngésződet a munkahely vagy az iskola kezeli, a biztonságos DNS beállítás le lehet zárva. Fordulj a rendszergazdádhoz.

</div>
