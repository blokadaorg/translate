---
title: Estä mainokset koko verkossasi reitittimen avulla mainosten estolla.
description: Ota Blokada Cloud käyttöön reitittimessäsi kerran, ja jokainen kodin laite on suojattu, mukaan lukien televisiot, pelikonsolit ja älykaiuttimet, joihin ei voi asentaa mainosten esto -sovellusta.
updated: 2026-10-02
order: 4
---

Jokainen laite verkossasi kysyy reitittimeltä, mitä DNS-palvelinta sen tulisi käyttää. Suuntaa reititin Blokada Cloudiin, niin mainokset ja seurantalaitteet estetään kaikelle sen takana olevalle. Tämä sisältää älytelevisiot, pelikonsolit, suoratoistotikut ja älykotilaitteet, joihin ei mahdu mainosten esto -sovellusta.

## Mitä reitittimesi tarvitsee

Reitittimesi on tuettava **salausta DNS-isäntänimellä**, eli DNS over TLS (DoT) tai DNS over HTTPS (DoH). Monet uudet reitittimet tukevat tätä, mukaan lukien alla mainitut mallit. Riippuen siitä, mitä reitittimesi tukee, tarvitset joko DNS-nimesi tai DoH-linkin, molemmat löytyvät yltä kohdasta _Omat tiedot_.

<div class="note important">

**Vain tavalliset IP-osoitteet?** Monet internet-palveluntarjoajan reitittimet hyväksyvät DNS:ksi vain IP-osoitteita. Tuki niille on tulossa. Sillä välin asenna laitteet yksitellen: [Android](../android-private-dns/), [Mac ja Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) ja [selaimet](../browser-dns-over-https/). Voit myös käyttää pientä välityspalvelinta Raspberry Pi:llä Pi-hole-ohjeen ([Pi-hole guide](../switch-from-pihole/)) mukaisesti.

</div>

## FRITZ!Box

FRITZ!OS 7.20 tai uudempi.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. Kirjoita _DNS-palvelimen ratkaistut nimet_ -kohtaan vain {% dot %}. **Poista kaikki muut merkinnät.** FRITZ!Box käyttää kaikkia listattuja ratkaisuja, ja muutkin antavat mainosten päästä läpi.
4. Untick _Allow fallback to unencrypted name resolution_.
5. Jos näet _Vaihto julkisiin DNS-palvelimiin, kun DNS ei toimi_, poista se käytöstä.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Osoite: {% ip "dot" %}
   - TLS-isäntänimi: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Avaa _Services → HTTPS DNS Proxy_. Poista muiden palveluntarjoajien instanssit.
3. Lisää instanssi mukautetulla resolver-osoitteella: {% doh %}
4. _Tallenna & Käytä_. Paketti ohjaa dnsmasqin automaattisesti siihen.

## Muut reitittimet

Etsi asetus nimeltä _DNS over TLS_, _Yksityinen DNS_, _Salattu DNS_ tai _DNS over HTTPS_. Anna Blokada DNS -nimesi tai DoH-linkkisi yllä, ja poista kaikki muut DNS-palvelimet, myös varapalvelimet.

## Tarkista, että se toimii

1. Käynnistä yksi laite uudelleen tai laita sen Wi-Fi pois päältä ja takaisin päälle, jotta se huomaa muutoksen.
2. Selaa minuutin ajan, avaa sitten ohjauspaneelin _Toiminta_-sivu. Verkkosi haut näkyvät siellä.

## Jos jotkin laitteet näyttävät silti mainoksia

Jotkin laitteet ohittavat reitittimen: puhelimet, joissa on _Yksityinen DNS_ asetettuna, selaimet joissa _turvallinen DNS_ on määritetty toiselle palveluntarjoajalle sekä laitteet, joilla on kovakoodattu oma DNS. Aseta nämä suoraan kyseiselle laitteelle tai poista niiden oma DNS-asetus käytöstä.

<div class="note tip">

Reitittimen takana kaikilla laitteilla on sama osoite, joten ohjauspaneeli näyttää verkon yhtenä laitteena. Jos haluat tarkastella puhelimia ja kannettavia tietokoneita erikseen, määritä niille oma Blokada DNS -nimi. Ne säilyttävät myös estonsa kodin ulkopuolella.

</div>
