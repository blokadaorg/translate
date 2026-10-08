---
title: NextDNS-vaihtoehto, jossa sama asennus jokaisella laitteella.
description: Siirry NextDNS:stä Blokada Cloudiin. Vaihda NextDNS:n DNS-nimi, DoH-linkki tai profiili Blokadan vastaaviin puhelimella, tietokoneella ja reitittimellä, ja säilytä mainosten esto.
updated: 2026-10-02
order: 3
---

NextDNS ja Blokada Cloud toimivat samalla tavalla: salattu DNS-palvelu, joka estää mainokset ja seurannan nimien perusteella, omilla asetuksillasi henkilökohtaisen DNS-nimen takana. Vaihto tarkoittaa, että korvaat NextDNS-tiedot Blokadan tiedoilla jokaisella laitteella. Mikään muu laitteella ei muutu.

## Mitä käytit ja mitä valita Blokadassa

| NextDNS:ssä                                           | Blokada Cloudissa                                           |
| --------------------------------------------------------------------- | ----------------------------------------------------------- |
| Konfiguraatio-ID:si, esim. `abc123`   | Laitetunnisteesi, osa Blokada DNS -nimeäsi ja DoH-linkkiäsi |
| _Yksityisyys_ -estolistat                                             | _Estolistat_ hallintapaneelissa                             |
| _Turvallisuus_ (haittaohjelmat, tietojenkalastelu) | haittaohjelmalista _Estolistoissa_                          |
| _Lapsilukko_                                                          | aikuissisältö- ja rahapelisivustolistat _Estolistoissa_     |
| _Sallittulista_ ja _Estolista_                                        | _Poikkeukset_ hallintapaneelissa                            |
| _Lokit_ ja _Analytiikka_                                              | _Toiminta_ ja _Tilastot_ hallintapaneelissa                 |

## Vaihda jokainen laite

Laitteesta riippuen tarvitset joko DNS-nimen tai DoH-linkin, molemmat löytyvät yllä kohdasta _Omat tiedot_.

### Android

Jos käytit _yksityistä DNS:ää_, jonka osoite on `<your-id>.dns.nextdns.io`, vaihda siihen oma Blokada DNS -nimi kuten [Android-ohjeessa](../android-private-dns/). Jos käytit NextDNS-sovellusta, poista se ja asenna tilalle [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone ja iPad

Jos käytit NextDNS-sovellusta, poista se ja asenna tilalle [Blokada 6](https://go.blokada.org/appstore). Jos asensit NextDNS-profiilin, poista se kohdasta _Asetukset → Yleiset → VPN ja laitehallinta_ ja seuraa sitten [Applen ohjetta](../apple-devices/).

### Mac ja Apple TV

Poista NextDNS-profiili tai -sovellus ja asenna Blokada-profiili [Applen ohjeesta](../apple-devices/).

### Windows ja Linux

Poista NextDNS-sovellus, jos käytät sitä. Windowsissa vaihda NextDNS-palvelin ja DoH-malli Blokadan vastaaviin kuten [Windows-ohjeessa](../windows-dns-over-https/). Linuxissa vaihda NextDNS-palvelin systemd-resolvedin asetuksissa kuten [Linux-ohjeessa](../linux-dns-over-tls/).

### Selaimet

Jos olet asettanut selaimesi _suojatuksi DNS_:ksi `https://dns.nextdns.io/…`, vaihda se omaan DoH-linkkiisi kuten [selaimen ohjeessa](../browser-dns-over-https/).

### Reititin

Jos reitittimesi käyttää NextDNS:ää DNS over TLS:llä tai DNS over HTTPS:llä, vaihda NextDNS-nimi tai -linkki Blokada-nimeen tai -linkkiin, kuten [reititinoppaassa](../router-ad-blocking/).

Jos reititin käyttää NextDNS:ää pelkillä IP-osoitteilla ja _liitetyllä IP:llä_, Blokada ei voi vielä ottaa sitä käyttöön. Tuki pelkkien DNS-osoitteiden reitittimille on tulossa. Siihen asti asenna laitteet yksi kerrallaan tai käytä reititintä, joka tukee salattua DNS:ää.

## Varmista että se toimii

Avaa muutama verkkosivusto ja katso sitten _Toiminta_-sivua hallintapaneelissa. Näet siellä laitteidesi kyselyt, ja estetyt on merkitty. Jos laitetta ei näy, se käyttää edelleen NextDNS:ää.
