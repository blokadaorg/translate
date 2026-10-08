---
title: Estä mainokset Windowsissa DNS over HTTPS -yhteydellä
description: Käytä Windows 11:n sisäänrakennettua salattua DNS:ää yhdessä Blokada Cloudin kanssa estääksesi mainokset ja seurantalaitteet kaikissa sovelluksissa ja selaimissa ilman, että sinun tarvitsee asentaa ohjelmistoa.
updated: 2026-10-02
order: 8
---

Windows 11 voi lähettää kaikki DNS-kyselynsä salattuna DNS over HTTPS -yhteyden yli. Suuntaa se Blokada Cloudiin, jolloin mainokset ja seurantalaitteet estetään kaikissa sovelluksissa ja selaimissa ilman asennusta.

Tarvitset DNS-palvelimen IP-osoitteen ja DoH-linkkisi, molemmat löytyvät yllä olevasta kohdasta _Omat tiedot_.

## Windows 11

1. Avaa _Asetukset → Verkkoyhteys ja internet_, sitten _Wi-Fi_ tai _Ethernet_ riippuen siitä, miten tietokone on yhdistetty.
2. Avaa yhteytesi _Laitteiston ominaisuudet_. Wi-Fi:ssä valitse _Hallitse tunnettuja verkkoja_ ja sitten kyseinen verkko, tai _Laitteiston ominaisuudet_ Wi-Fi-sivun yläreunasta.
3. Valitse _DNS-palvelimen määritys_ -kohdasta _Muokkaa_. Valitse _Manuaalinen_ ja ota käyttöön _IPv4_.
4. Kirjoita _Ensisijainen DNS_ -kenttään DNS-palvelin {% ip "doh" %}
5. Aseta _DNS over HTTPS_ päälle valitsemalla _Käytössä (manuaalinen malli)_ ja liitä DoH-linkkisi {% doh %} kohtaan _DoH-malli_.
6. Kytke _Varmuuskäyttö selväkielisenä_ pois päältä ja valitse _Tallenna_.

Jos tietokone käyttää sekä Wi-Fi- että Ethernet-yhteyttä, toista tämä toiselle yhteydelle.

<div class="note important">

Jätä _Vaihtoehtoinen DNS_ tyhjäksi. Windows käyttää molempia palvelimia ja toinen päästää mainokset läpi.

</div>

<div class="note tip">

Ei _Käytössä (manuaalinen malli)_ -vaihtoehtoa? Windows 11 -versiosi on vanhempi. Päivitä Windows tai noudata [selainohjetta](../browser-dns-over-https/) sillä välin.

</div>

## Windows 10

Windows 10:ssä ei ole sisäänrakennettua salattua DNS:ää. Ota turvallinen DNS käyttöön selaimessasi kuten [selainohjeessa](../browser-dns-over-https/) neuvotaan, tai määritä [reititin](../router-ad-blocking/) suojaamaan koko kotiverkkoa.

## Tarkista, että se toimii

Avaa muutama verkkosivusto ja tarkista sitten _Toiminta_-sivu [ohjauspaneelista](https://app.blokada.org/stats?src=guides). Tämän tietokoneen kyselyt näkyvät siellä.

<div class="note aside">

Haluatko myös VPN:n tälle tietokoneelle? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) sisältää WireGuard-asetuksen, joka salaa kaiken liikenteen samalla estosuodatuksella.

</div>

## Jos jokin ei toimi

Chromessa ja Edgessä on oma _turvallinen DNS_ -asetus, joka ohittaa Windowsin. Jos asetus jätetään automaattiseksi, se voi palautua käyttämään tavallista DNS:ää, mitä Blokada ei hyväksy. Anna siihen oma DoH-linkkisi:

- **Chrome:** avaa `chrome://settings/security`, ota käyttöön _Käytä turvallista DNS:ää_ ja kohdassa _Valitse DNS-palveluntarjoaja_ valitse _Lisää mukautettu DNS-palveluntarjoaja_.
- **Edge:** avaa `edge://settings/privacy`, ota käyttöön turvallinen DNS ja valitse _Valitse palveluntarjoaja_.

Liitä seuraavaksi DoH-linkkisi {% doh %}

Jos mainoksia pääsee silti läpi IPv6-verkoissa, Windows saattaa käyttää myös reitittimesi IPv6 DNS -palvelinta. Poista _Internet Protocol Version 6 (TCP/IPv6)_ käytöstä verkkosovittimen ominaisuuksista (_Ohjauspaneeli → Verkkoyhteydet_) tai määritä [reititin](../router-ad-blocking/).
