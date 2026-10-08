---
title: Estä mainokset Chromessa, Firefoxissa, Edgessä ja Bravessa DNS over HTTPS:n avulla.
description: Aseta Blokada Cloud selaimesi suojatuksi DNS-palveluntarjoajaksi, jotta voit estää mainokset ja seurannan millä tahansa tietokoneella, myös työläppäreissä, joihin et voi asentaa sovelluksia.
updated: 2026-10-02
order: 7
---

Nykyaikaiset selaimet voivat käyttää omaa salattua DNS-palvelua, jota kutsutaan nimellä _suojattu DNS_ tai _DNS over HTTPS_. Aseta Blokada Cloud, ja selain estää mainokset ja seurannan millä tahansa verkolla ilman asennettavaa laajennusta.

Tämä asetus koskee vain tätä selainta. Jos haluat suojata koko tietokoneen, käytä [Apple-profiilia](../apple-devices/) Macilla tai määritä [reititin](../router-ad-blocking/).

## Chrome

1. Avaa `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Syötä {% doh %}

## Edge

1. Avaa `edge://settings/privacy`.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. Avaa `brave://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Syötä {% doh %}

## Safari

Safarilla ei ole omaa suojatun DNS:n asetusta. Se käyttää järjestelmän DNS:ää, joten asenna [Apple-profiili](../apple-devices/).

## Tarkista, että se toimii

Surffaa hetki ja avaa sitten _Aktiivisuus_-sivu [kojelaudassa](https://app.blokada.org/stats?src=guides). Tämän selaimen haut näkyvät siellä.

## Jos jokin ei toimi

<div class="note tip">

Jos selaintasi hallinnoi työpaikka tai koulu, suojatun DNS:n asetus voi olla lukittu. Kysy järjestelmänvalvojalta.

</div>
