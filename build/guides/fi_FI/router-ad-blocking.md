---
title: Estä mainokset koko verkossasi reitittimen avulla mainosten estolla.
description: Ota Blokada Cloud käyttöön reitittimessäsi kerran, ja jokainen kodin laite on suojattu, mukaan lukien televisiot, pelikonsolit ja älykaiuttimet, joihin ei voi asentaa mainosten esto -sovellusta.
updated: 2026-10-09'
order: 4
---

Jokainen laite verkossasi kysyy reitittimeltä, mitä DNS-palvelinta sen tulisi käyttää. Suuntaa reititin Blokada Cloudiin, niin mainokset ja seurantalaitteet estetään kaikelle sen takana olevalle. Tämä sisältää älytelevisiot, pelikonsolit, suoratoistotikut ja älykotilaitteet, joihin ei mahdu mainosten esto -sovellusta.

## Mitä reitittimesi tarvitsee

Reitittimen voi asentaa kahdella tavalla:

- **Suojaamaton DNS isäntänimellä**, eli DNS over TLS (DoT) tai DNS over HTTPS (DoH). Monet uudet reitittimet tukevat tätä, mukaan lukien alla olevat mallit. Riippuen siitä, kumpaa reitittimesi tukee, tarvitset DNS-nimesi tai DoH-linkkisi, molemmat löytyvät yllä kohdasta _Omat tiedot_.
- **Pelkkä IPv6 DNS-osoite.** Monet internet-operaattoreiden reitittimet hyväksyvät DNS:lle vain IP-osoitteet. Jos omasi toimii näin ja yhteytesi tukee IPv6:ta, Blokada antaa sinulle syötettävän IPv6-osoitteen. Katso kohta [Reitittimet, jotka hyväksyvät vain IP-osoitteen](#routers-that-only-take-an-ip-address).

Käytä salattua DNS:ää, jos reitittimesi tukee sitä. Kyselyt pysyvät yksityisinä matkalla Blokadaan.

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

Etsi asetusta nimeltä _DNS over TLS_, _Yksityinen DNS_, _Salattu DNS_ tai _DNS over HTTPS_. Syötä Blokada DNS -nimesi tai DoH-linkki yllä olevasta, ja poista kaikki muut DNS-palvelimet, myös varapalvelimet. Jos tällaista asetusta ei ole, käytä tavallista IPv6-osoitetta alla olevalla tavalla.

## Reitittimet, jotka hyväksyvät vain IP-osoitteen

Tätä varten reitittimesi ja internet-yhteytesi tarvitsevat IPv6:n. Tuki pelkille IPv4-osoitteille on tulossa myöhemmin.

1. Avaa [hallintapaneelissa](https://app.blokada.org/setup?src=guides) kohta _Asetukset_ ja valitse _Reititin, TV, pelikonsoli_.
2. Nimeä reititin, esimerkiksi _Kotireititin_, ja valitse _Hae osoite_. Nimi näkyy toiminnassasi, eikä sitä voi muuttaa myöhemmin.
3. Reitittimen asetuksista löydät IPv6 DNS -palvelimet usein kohdasta _Internet_, _WAN_ tai _IPv6_. Syötä osoite ainoaksi DNS-palvelimeksi.
4. **Poista kaikki muut DNS-palvelimet, myös IPv4-palvelimet.** Laitteet, jotka edelleen saavat reitittimeltä IPv4 DNS -palvelimen, ohjaavat joitain kyselyitä Blokadan ohi. Jos reititin ei voi jättää IPv4 DNS -palvelinta tyhjäksi, määritä laitteesi yksitellen: [Android](../android-private-dns/), [Mac ja Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) ja [selaimet](../browser-dns-over-https/).

Sama asennus toimii myös televisiossa tai pelikonsolissa, jossa voit syöttää DNS-palvelimen käsin. Anna jokaiselle oma osoite, jotta se näkyy nimellä toiminnassasi.

<div class="note aside">

Nämä kyselyt kulkevat salaamattomina Blokadaan, kuten minkä tahansa tavallisen DNS-palvelimen tapauksessa. Jos reitittimesi tukee DNS over TLS:ää tai DNS over HTTPS:ää, käytä niitä sen sijaan.

</div>

## Tarkista, että se toimii

1. Käynnistä yksi laite uudelleen tai laita sen Wi-Fi pois päältä ja takaisin päälle, jotta se huomaa muutoksen.
2. Sammuta kyseisessä laitteessa Blokada, jos se on käytössä, ja avaa [go.blokada.org/test](https://go.blokada.org/test). Se näyttää, ohjautuvatko DNS-pyynnöt Blokadan kautta.
3. Selaa hetki ja avaa sitten _Toiminta_-sivu [hallintapaneelissa](https://app.blokada.org/stats?src=guides). Verkkosi kyselyt näkyvät siellä.

## Jos jotkin laitteet näyttävät silti mainoksia

Jotkin laitteet ohittavat reitittimen: puhelimet, joissa on _Yksityinen DNS_ asetettuna, selaimet joissa _turvallinen DNS_ on määritetty toiselle palveluntarjoajalle sekä laitteet, joilla on kovakoodattu oma DNS. Aseta nämä suoraan kyseiselle laitteelle tai poista niiden oma DNS-asetus käytöstä.

<div class="note tip">

Reitittimen takana kaikilla laitteilla on sama osoite, joten ohjauspaneeli näyttää verkon yhtenä laitteena. Jos haluat tarkastella puhelimia ja kannettavia tietokoneita erikseen, määritä niille oma Blokada DNS -nimi. Ne säilyttävät myös estonsa kodin ulkopuolella.

</div>
