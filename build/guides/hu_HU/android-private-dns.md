---
title: Privát DNS beállítása Androidon a Blokada Cloud segítségével.
description: Használd az Android beépített Privát DNS beállítását a Blokada Clouddal, hogy blokkolhasd a hirdetéseket és követőket minden alkalmazásban, Wi-Fi-n és mobilhálózaton egyaránt. Vagy engedd, hogy a Blokada 6 alkalmazás tegye ezt meg helyetted.
updated: 2026-10-02
order: 5
---

## A legegyszerűbb mód: az alkalmazás

A [Blokada 6](https://go.blokada.org/play_cloud) mindent elintéz neked: egy érintéssel ki- vagy bekapcsolhatod a blokkolást, és megmutatja, mi lett blokkolva magán a telefonon. Jelentkezz be az azonosítóddal, és kész is vagy.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Szerezd meg a Blokada 6-ot a Google Playen</a></p>

## Alkalmazás nélkül: Privát DNS

Az Android 9-től kezdve elérhető a _Privát DNS_ beállítás. Állítsd be a Blokada Cloudsra, így minden alkalmazásban, minden hálózaton blokkolva lesznek a hirdetések és követők, anélkül hogy bármi futna a háttérben.

1. Nyisd meg a _Beállítások → Hálózat és internet_ menüt. Egyes telefonokon ez _Kapcsolatok_ vagy _Kapcsolat és megosztás_ lehet.
2. Érints rá a _Privát DNS_-re. Samsung telefonokon ez a _További kapcsolatbeállítások_ alatt található.
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

Ha nem találod, keresd meg a Beállítások alkalmazásban a "Privát DNS" kifejezést.

## Ellenőrizd, hogy működik-e

Nyiss meg néhány alkalmazást vagy weboldalt, majd nézd meg az _Aktivitás_ oldalt a [vezérlőpulton](https://app.blokada.org/stats?src=guides). Ennek a telefonnak a lekérdezései ott fognak megjelenni.

## Ha valami nem működik

- **„Nem sikerült csatlakozni” vagy nincs internet:** Ellenőrizd, hogy a Blokada DNS nevében nincs-e elgépelés. Pontosan olyannak kell lennie, ahogy fent látható, `https://` nélkül.
- **Másik VPN alkalmazás aktív:** Egyes VPN alkalmazások saját DNS-t használnak, és megkerülik a Privát DNS-t. Kapcsold ki a VPN DNS vagy hirdetésblokkoló beállítását, vagy használd inkább a Blokada 6-ot.
- **A Chrome még mindig hirdetéseket mutat:** Elképzelhető, hogy a Chrome saját biztonságos DNS szolgáltatót használ, így megkerüli a Privát DNS-t. A Chrome-ban nyisd meg a _Beállítások → Adatvédelem és biztonság → Biztonságos DNS használata_ menüt, és válaszd a _Jelenlegi szolgáltató használata_ opciót. A Chrome így követni fogja a Privát DNS-t.
