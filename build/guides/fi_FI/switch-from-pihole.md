---
title: Pi-hole-vaihtoehto, joka ei vaadi laitteistoa.
description: Siirrä kotisi mainosten esto Pi-holelta Blokada Cloudiin tai säilytä Pi-hole ja ohjaa sen kyselyt Blokadan kautta.
updated: 2026-10-02
order: 1
---

Pi-hole estää mainokset kaikilta laitteiltasi verkossa, kunhan Raspberry Pi on käynnissä, päivitetty ja kotona. Blokada Cloud tekee saman palvelimiltamme:

- **Ei ylläpidettävää laatikkoa.** Ei SD-kortteja, ei päivityksiä, eikä katkoksia, kun Pi sammuu.
- **Toimii myös kodin ulkopuolella.** Puhelimet ja kannettavat säilyttävät eston mobiilidatalla ja muissa Wi-Fi-verkoissa.
- **Salattu.** Laitteet keskustelevat Blokadan kanssa DNS over TLS:n tai DNS over HTTPS:n kautta, joten palveluntarjoajasi ei voi lukea tai muokata kyselyitäsi.
- **Yksi hallintapaneeli.** Estolistat, sallitut ja estettyvät verkkotunnukset sekä laitekohtainen aktiivisuus osoitteessa [app.blokada.org](https://app.blokada.org/?src=guides).

On kaksi tapaa vaihtaa. Vaihda Pi-hole kokonaan Blokada Cloudiin, tai säilytä se ja käytä Blokada Cloudia sen ylävirran DNS-palvelimena.

## Vaihtoehto 1: korvaa Pi-hole

1. **Hanki Blokada Cloud** ja avaa hallintapaneeli. DNS-nimesi ja DoH-linkkisi löytyvät siellä kohdasta _Asetus_ sekä yllä kohdasta _Tiedot_.
2. **Ohjaa reitittimesi Blokadaan Pi-holen sijaan.** Noudata [reititinohjetta](../router-ad-blocking/). Jos reitittimesi tukee vain tavallista IP-osoitetta DNS-palvelimena, määritä laitteesi yksitellen: [Android](../android-private-dns/), [Mac ja Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) ja [selaimet](../browser-dns-over-https/).
3. **Jos Pi-hole oli DHCP-palvelin,** kytke DHCP takaisin päälle reitittimessä _ennen_ kuin sammutat Pin. Muuten laitteesi eivät saa verkko-osoitteita.
4. **Siirrä listasi.** Hallintapaneelissa valitse estolistat kohdasta _Estolistat_ ja lisää omat sallitut tai estetyt verkkotunnukset kohtaan _Poikkeukset_.
5. **Sammuta Pi-hole** tai pidä se muuhun käyttöön.

<div class="note aside">

Pi-hole näytti jokaisen verkon laitteen IP-osoitteensa perusteella. Blokadassa kukin laite näkyy omalla nimellään, kunhan se käyttää omaa Blokada DNS -nimeään. Yhdellä Blokada DNS -nimellä varustettu reititin näkyy yhtenä laitteena.

</div>

## Vaihtoehto 2: säilytä Pi-hole, käytä Blokada Cloudia ylävirrassa

Jos haluat säilyttää paikalliset asetuksesi, kuten paikalliset laitennimet, DHCP:n tai omat listasi, anna Pi-holen välittää kyselynsä Blokadaan salattuna. Pi-hole ei tue salattua välitystä itsessään, joten sen vierelle asennetaan pieni välittäjä. Tämä ohje käyttää [dnsproxy](https://github.com/AdguardTeam/dnsproxy)-ohjelmaa, joka on avoimen lähdekoodin ja yhdessä tiedostossa.

1. Lataa Pi-hole-koneelle `dnsproxy`-julkaisu suorittimellesi (`linux-arm64` uudemmalle Raspberry Pille) sen julkaisusivulta ja kopioi `dnsproxy`-binääri kansioon `/usr/local/bin/`.
2. Luo tiedosto `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Salattu DNS-välittäjä Blokada Cloudiin
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Käynnistä: `sudo systemctl enable --now dnsproxy`
4. Avaa Pi-holen hallinnassa _Asetukset → DNS_. Poista valinta kaikista ylävirran palvelimista ja lisää `127.0.0.1#5054` mukautetuksi ylävirran palvelimeksi. Tallenna.
5. Tarkista hallintapaneelin _Aktiivisuus_-sivu. Verkkosi kyselyt näkyvät nyt siellä.

Voit kytkeä pois päältä Pi-holen omat estolistat ja hallinnoida estoja hallintapaneelissa tai käyttää molempia.

## Usein kysytyt

**Tarvitsenko Blokada Plusin?** En. Blokada Cloud kattaa DNS-eston koko kotitaloudelle. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) lisää joukkoon VPN:n.

**Mitä jos Blokada ei ole saavutettavissa?** Laitteesi eivät saa ratkaistua nimiä ennen kuin Blokada taas toimii, aivan kuten Pi-holen kaatuessa. Älä lisää toista, suodattamatonta DNS-palvelinta varmuuskäyttöön. Useimmat laitteet käyttävät kaikkia määritettyjä palvelimia satunnaisesti, jolloin mainokset pääsisivät läpi.
