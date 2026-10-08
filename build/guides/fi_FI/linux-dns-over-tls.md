---
title: Estä mainokset Linuxissa käyttämällä DNS over TLS:ää.
description: Ota systemd-resolved käyttöön ja yhdistä Blokada Cloudiin salatun DNS over TLS -yhteyden kautta, jolloin mainokset ja seurantalaitteet estetään kaikissa sovelluksissa Linux-tietokoneellasi.
updated: 2026-10-02
order: 9
---

Useimmat nykyiset Linux-jakelut, mukaan lukien Ubuntu ja Fedora, ratkaisevat nimet _systemd-resolved_-palvelun kautta, joka tukee DNS over TLS:ää. Debianissa asenna se ensin komennolla `sudo apt install systemd-resolved`. Osoita se Blokada Cloudiin, niin mainokset ja seurantalaitteet estetään kaikissa sovelluksissa tietokoneellasi.

## Ota systemd-resolved käyttöön

1. Luo kansio komennolla `sudo mkdir -p /etc/systemd/resolved.conf.d`, ja sitten tiedosto `/etc/systemd/resolved.conf.d/blokada.conf` näillä asetuksilla:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Käynnistä se uudelleen: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Tarkista se: <code>resolvectl status</code> näyttää <code>+DNSOverTLS</code> sekä Blokada-palvelimen.</li>
</ol>

Osa `#`-merkin jälkeen on Blokada DNS -nimesi: {% dot %} systemd-resolved tarkistaa palvelimen varmenteen tätä vastaan, ja Blokada käyttää sitä tunnistaakseen, miltä laitteelta pyyntö on peräisin.

<div class="note important">

**NetworkManager** välittää myös verkon DNS-palvelimet eteenpäin. `Domains=~.` ohjaa kaikki nimihakupyynnöt Blokadalle, mutta jos `resolvectl status` näyttää edelleen jonkin toisen palvelimen yhteydessä, kytke automaattinen DNS pois päältä kyseisestä yhteydestä (kohdan _DNS_ vieressä oleva _Automatic_-kytkin IPv4- ja IPv6-asetuksissa).

</div>

## Ilman systemd-resolvedia

Jos `resolvectl`-komentoa ei löydy, jakelusi ratkaisee nimet toisella tavalla. Ota siinä tapauksessa käyttöön suojattu DNS selaimessasi (katso [selainopas](../browser-dns-over-https/)) tai määritä [reitittimesi](../router-ad-blocking/) suojaamaan koko kotiasi.

## Tarkista että se toimii

Avaa muutama verkkosivu ja katso sitten _Toiminta_-sivua [hallintapaneelissa](https://app.blokada.org/stats?src=guides). Tämän tietokoneen nimihakupyynnöt näkyvät siellä.

<div class="note aside">

Haluatko myös VPN:n tälle tietokoneelle? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) sisältää WireGuard-asetuksen, joka salaa kaiken liikenteen ja estää mainokset samalla tavalla.

</div>
