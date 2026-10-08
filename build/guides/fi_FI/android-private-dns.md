---
title: Ota käyttöön Yksityinen DNS Androidissa Blokada Cloudin avulla
description: Käytä Androidin sisäänrakennettua Yksityinen DNS -asetusta yhdessä Blokada Cloudin kanssa, jotta mainokset ja seuraimet estetään jokaisessa sovelluksessa, sekä Wi-Fi- että mobiilidatan kautta. Tai anna Blokada 6 -sovelluksen hoitaa se.
updated: 2026-10-02
order: 5
---

## Helpoin tapa: sovellus

[Blokada 6](https://go.blokada.org/play_cloud) hoitaa kaiken puolestasi, kytkee eston päälle tai pois yhdellä napautuksella ja näyttää mitä puhelimella on estetty. Kirjaudu sisään tilisi tunnisteella ja olet valmis.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Lataa Blokada 6 Google Playsta</a></p>

## Ilman sovellusta: Yksityinen DNS

Android 9 ja uudemmissa on _Yksityinen DNS_ -asetus. Aseta se Blokada Cloudiin, jolloin mainokset ja seuraimet estetään kaikissa sovelluksissa ja jokaisessa verkossa ilman taustalla käynnissä olevia sovelluksia.

1. Avaa _Asetukset → Verkko & internet_. Joillakin puhelimilla tämä on _Yhteydet_ tai _Yhteys & jakaminen_.
2. Napauta _Yksityinen DNS_. Samsung-puhelimissa se löytyy _Lisäyhteysasetukset_-kohdasta.
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

Jos et löydä sitä, etsi Asetukset-sovelluksesta "Yksityinen DNS".

## Tarkista että se toimii

Avaa muutama sovellus tai verkkosivusto ja katso sitten _Toiminta_-sivua [hallintapaneelissa](https://app.blokada.org/stats?src=guides). Tämän puhelimen kyselyt näkyvät siellä.

## Jos jokin ei toimi

- **"Yhteyttä ei saatu" tai ei internetiä:** tarkista Blokada DNS -nimesi kirjoitusvirheiden varalta. Sen tulee olla täsmälleen yllä olevan mukainen, ilman `https://`-etuliitettä.
- **Toinen VPN-sovellus on aktiivinen:** jotkin VPN-sovellukset käyttävät omaa DNS-palvelinta ja ohittavat Yksityisen DNS:n. Poista VPN:n DNS- tai mainosten estoasetus käytöstä, tai käytä sen sijaan Blokada 6:tta.
- **Chromessa näkyy yhä mainoksia:** Chrome saattaa olla asetettu käyttämään omaa suojattua DNS-palveluaan, jolloin Yksityinen DNS ohitetaan. Chromessa avaa _Asetukset → Tietosuoja ja turvallisuus → Käytä suojattua DNS:ää_ ja valitse _Käytä nykyistä palveluntarjoajaa_. Tämän jälkeen Chrome käyttää Yksityistä DNS:ää.
