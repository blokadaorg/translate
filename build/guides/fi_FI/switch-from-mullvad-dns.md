---
title: Mullvad DNS lopettaa. Jatka mainosten estoa Blokada Cloudilla
description: Mullvad sulkee julkisen DNS-palvelunsa 2. marraskuuta 2026. Näin siirrät puhelimesi, tietokoneesi ja reitittimen Blokada Cloudiin ennen sitä ilman että mainosten esto katoaa.
updated: 2026-10-02
order: 2
---

Mullvad lopettaa ilmaisen julkisen DNS-palvelunsa **2. marraskuuta 2026** ja suosittelee Quad9-palvelua sen tilalle. Quad9 estää haittaohjelmat, mutta **ei** mainoksia tai jäljittäjiä. Kun Mullvadin DNS lakkaa toimimasta, siihen asetetut laitteet lakkaavat lataamasta sivustoja ja sovelluksia. Jos laite sallii vaihtaa toiseen DNS-palvelimeen, mainokset palaavat sen sijaan. Vaihda ennen tätä päivämäärää.

Tämä sivu käsittelee julkisia DNS-nimiä, jotka päättyvät `dns.mullvad.net`:iin. Se ei kata Mullvad VPN -sovellusta.

## Mitä käytit ja mitä valita Blokadassa

| Mullvad DNS -nimi          | Mitä se esti                             | Blokada-hallintapaneelissa                                                                                                                         |
| -------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | ei mitään                                | Blokada on suodatuspalvelu. Jos et halua suodatusta, Quad9 tai palveluntarjoajasi DNS on yksinkertaisempi valinta. |
| `adblock.dns.mullvad.net`  | mainokset, jäljittäjät                   | mainosten ja jäljittäjien estolista                                                                                                                |
| `base.dns.mullvad.net`     | mainokset, jäljittäjät, haittaohjelmat   | lisää haittaohjelmalista                                                                                                                           |
| `extended.dns.mullvad.net` | base sekä sosiaalinen media              | lisää sosiaalisen median lista                                                                                                                     |
| `family.dns.mullvad.net`   | base sekä aikuisviihde ja uhkapelaaminen | lisää aikuisviihteen ja uhkapelaamisen listat                                                                                                      |
| `all.dns.mullvad.net`      | kaikki yllä mainitut                     | ota kaikki käyttöön                                                                                                                                |

Valitset estolistat hallintapaneelissa kohdasta _Estolistat_. Voit vaihtaa niitä milloin tahansa, ja muutos koskee kaikkia laitteitasi.

## Vaihda jokainen laite

Blokada antaa jokaiselle laitteelle oman nimen, joten hallintapaneeli voi näyttää laitekohtaisen aktiivisuuden. Laitteesta riippuen tarvitset joko DNS-nimesi tai DoH-linkkisi, molemmat löytyvät _Tietosi_-kohdasta yllä.

### Android

Mullvadin ohjeessa syötit isäntänimen _Yksityinen DNS_ -kohtaan. Korvaa se Blokada DNS -nimelläsi. [Android-ohjeessa](../android-private-dns/) on vaiheet.

### iPhone, iPad ja Mac

Mullvadin asennuksessa käytettiin määritysprofiilia. Poista se ensin:

- **iPhone ja iPad:** _Asetukset → Yleiset → VPN ja laitehallinta_, valitse Mullvad DNS -profiili ja napauta _Poista profiili_.
- **Mac:** avaa profiililuettelo (_Järjestelmäasetukset → Yleiset → Laitteiden hallinta_ macOS 15 ja uudemmissa, _Järjestelmäasetukset → Tietosuoja ja turvallisuus → Profiilit_ macOS 13 ja 14:ssä, _Järjestelmäasetukset → Profiilit_ macOS 12:ssa ja aiemmissa), valitse Mullvad DNS -profiili ja napsauta _−_.

Asenna sen jälkeen Blokada-profiili [Applen ohjeesta](../apple-devices/).

### Selaimet

Jos syötit Mullvad DoH -linkin, kuten `https://adblock.dns.mullvad.net/dns-query`, _suojattu DNS_ tai _DNS over HTTPS_ -kohtaan, korvaa se omalla DoH-linkilläsi. [Selaimen ohjeessa](../browser-dns-over-https/) on vaiheet joka selaimelle.

### Reititin

Jos reitittimesi käyttää Mullvadin DNS over TLS:ää, korvaa Mullvadin isäntänimi omalla Blokada DNS -nimelläsi ja poista Mullvadin IP-osoitteet. [Reitittimen ohjeessa](../router-ad-blocking/) on ohjeet yleisimmille malleille.

## Varmista että se toimii

Avaa muutama verkkosivusto ja tarkista sitten _Aktiivisuus_-sivu hallintapaneelissa. Näet laitteesi kyselyt siellä, estetyt ovat merkittyinä. Jos laitetta ei näy, se käyttää vielä toista DNS-palvelinta.
