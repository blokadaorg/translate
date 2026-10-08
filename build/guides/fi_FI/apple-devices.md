---
title: Estä mainokset Macilla ja Apple TV:llä Blokada DNS -profiililla.
description: Asenna Blokada Cloud DNS -profiili estääksesi mainokset ja seurannan koko Macilla tai Apple TV:llä, salatun DNS:n avulla ilman taustalla pyöriviä sovelluksia.
updated: 2026-10-02
order: 6
---

Apple-laitteet voivat käyttää salattua DNS:ää koko järjestelmään profiilin avulla. Blokada-profiili ohjaa laitteen Blokada Cloudiin, joka estää mainokset ja seurantaevästeet kaikissa sovelluksissa ja selaimissa.

Toimii macOS 11 (Big Sur), tvOS 14, iOS ja iPadOS 14 ja uudemmissa.

<div class="if-no-device">

Tällä sivulla ei vielä tunnisteta laitettasi, joten profiiliasi ei voi tarjota. Kirjaudu ohjauspaneeliin, avaa _Asetukset_, valitse laitteesi ja avaa tämä ohje _Avaa toisella laitteella_ -toiminnolla.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Hae profiililinkkini</a></p>

</div>

## iPhone ja iPad

Helpoin tapa on sovellus. [Blokada 6](https://go.blokada.org/appstore) hoitaa kaiken puolestasi, kytkee eston päälle ja pois yhdellä painalluksella ja näyttää puhelimella, mitä on estetty. Kirjaudu tilisi tunnuksella ja olet valmis.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Lataa Blokada 6 App Storesta</a></p>

### Ilman sovellusta

Voit vaihtoehtoisesti asentaa profiilin. iPhone ja iPad asentavat profiilit vain **Safarilla**.

<div class="if-device">
<div class="if-other-browser note important">

Tämä sivu on auki toisessa selaimessa. Kopioi linkkisi ja avaa se Safarissa jatkaaksesi siellä: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Avaa _Asetukset_. Napauta _Ladattu profiili_ ylhäältä. Löydät sen myös kohdasta _Yleiset → VPN ja laitehallinta_.
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}Lataa profiilini{% endappleProfile %}</p>

## Mac

1. Klikkaa alla olevaa painiketta ladataksesi profiilin.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Lataa profiilini{% endappleProfile %}</p>

## Apple TV

Apple TV ei voi avata verkkosivuja, joten sinun tulee kirjoittaa profiililinkkisi siihen.

1. Profiililinkkisi: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. Korosta _Jaa Apple TV -analytiikkaa_. Älä valitse sitä. Paina kaukosäätimen Toista/Tauko -painiketta sen sijaan.
4. Valitse _Lisää profiili_ ja syötä profiililinkkisi. Kirjoittaminen on helpointa iPhonen näppäimistökehotteella, jossa voit liittää sen. Asenna profiili ja vahvista.

<div class="note aside">

**Apple TV ja muut kodin laitteet:** jos otat Blokada Cloudin käyttöön [reitittimessäsi](../router-ad-blocking/), Apple TV ja kaikki muut laitteet ovat suojattuja.

</div>

## Tarkista että se toimii

Selaa hetki ja avaa sen jälkeen _Aktiviteetti_-sivu [ohjauspaneelissa](https://app.blokada.org/stats?src=guides). Tämän laitteen kyselyt näkyvät siellä.

Jos haluat myöhemmin poistaa Blokadan, poista profiili sieltä mihin sen asensit.
