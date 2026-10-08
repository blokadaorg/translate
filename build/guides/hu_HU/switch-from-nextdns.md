---
title: Egy NextDNS alternatíva, ugyanolyan beállítással minden eszközön.
description: Válts NextDNS-ről Blokada Cloud-ra. Cseréld le a NextDNS DNS nevedet, DoH hivatkozásodat vagy profilodat a Blokada megfelelőjére telefonodon, számítógépeden és routeredben, és tartsd meg a reklámblokkolást.
updated: 2026-10-02
order: 3
---

A NextDNS és a Blokada Cloud ugyanúgy működnek: titkosított DNS szolgáltatásként blokkolják a hirdetéseket és követőket név alapján, saját beállításokkal, egyedi DNS név mögött. A váltás azt jelenti, hogy az egyes eszközökön lecseréled a NextDNS értékeket a saját Blokada adataidra. Minden más változatlan marad az eszközön.

## Mit használtál, és mit válassz a Blokada-ban

| A NextDNS-ben                                                       | A Blokada Cloud-ban                                                         |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| A konfigurációs azonosítód, pl. `abc123`            | Az eszköz címkéd, ami része a Blokada DNS nevednek és a DoH hivatkozásodnak |
| _Adatvédelem_ tiltólisták                                           | _Tiltólisták_ a vezérlőpulton                                               |
| _Biztonság_ (kártékony szoftverek, adathalászat) | egy kártékony szoftver lista a _Tiltólisták_ között                         |
| _Szülői felügyelet_                                                 | felnőtt tartalom és szerencsejáték listák a _Tiltólisták_ között            |
| _Engedélyezési lista_ és _Tiltólista_                               | _Kivétel_ a vezérlőpulton                                                   |
| _Naplók_ és _Analitika_                                             | _Tevékenység_ és _Statisztika_ a vezérlőpulton                              |

## Minden eszköz cseréje

Az eszköztől függően szükséged lesz a DNS nevedre vagy a DoH hivatkozásodra, mindkettő a _Saját adataid_ résznél található fentebb.

### Android

Ha _Privát DNS_-t használtál a következővel: `<your-id>.dns.nextdns.io`, cseréld le a saját Blokada DNS nevedre az [Android útmutató](../android-private-dns/) szerint. Ha a NextDNS alkalmazást használtad, távolítsd el, és telepítsd helyette a [Blokada 6](https://go.blokada.org/play_cloud) alkalmazást.

### iPhone és iPad

Ha a NextDNS alkalmazást használtad, távolítsd el, és telepítsd a [Blokada 6](https://go.blokada.org/appstore) alkalmazást. Ha helyette NextDNS profilt telepítettél, töröld azt a _Beállítások → Általános → VPN & Eszközkezelés_ alatt, majd kövesd az [Apple útmutató](../apple-devices/) lépéseit.

### Mac és Apple TV

Távolítsd el a NextDNS profilt vagy alkalmazást, majd telepítsd a Blokada profilt az [Apple útmutató](../apple-devices/) segítségével.

### Windows és Linux

Ha használod a NextDNS alkalmazást, távolítsd el. Windows esetén cseréld ki a NextDNS szervert és a DoH sablont a Blokada megfelelőjére a [Windows útmutató](../windows-dns-over-https/) alapján. Linuxon cseréld le a NextDNS szervert a systemd-resolved-ban, a [Linux útmutató](../linux-dns-over-tls/) szerint.

### Böngészők

Ha a `https://dns.nextdns.io/…` címet állítottad be böngésződ _biztonságos DNS_-eként, cseréld le saját DoH hivatkozásodra a [böngésző útmutató](../browser-dns-over-https/) szerint.

### Router

Ha a routered a NextDNS-t DNS over TLS vagy DNS over HTTPS protokollon keresztül használja, cseréld le a NextDNS nevet vagy hivatkozást a saját Blokada adatodra a [router útmutató](../router-ad-blocking/) szerint.

Ha a router sima IP címeken keresztül használja a NextDNS-t _kapcsolt IP_-vel, ezt a Blokada még nem tudja átvenni. A sima DNS címmel működő routerek támogatása hamarosan érkezik. Addig állítsd be az eszközeidet egyenként, vagy használj olyan routert, amely támogatja a titkosított DNS-t.

## Ellenőrizd, hogy működik-e

Nyiss meg néhány weboldalt, majd nézd meg a _Tevékenység_ oldalt a vezérlőpulton. Itt láthatod az eszközeid lekérdezéseit, a blokkoltakat megjelölve. Ha egy eszköz nem jelenik meg, akkor az még mindig a NextDNS-t használja.
