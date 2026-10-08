---
title: Hirdetések blokkolása az egész hálózaton routeres hirdetésblokkolással.
description: Állítsa be a Blokada Cloud szolgáltatást a routerén egyszer, és az otthoni összes eszköz védve lesz, beleértve a TV-ket, játékkonzolokat és okoshangszórókat is, amelyek nem tudnak hirdetésblokkolót futtatni.
updated: 2026-10-02
order: 4
---

A hálózatán lévő minden eszköz megkérdezi a routert, melyik DNS szervert használja. Állítsa be a routert a Blokada Cloud-ra, így a hirdetések és követők blokkolva lesznek minden eszközön, ami mögötte van. Ez magában foglalja az okos TV-ket, játékkonzolokat, streaming stickeket és okosotthon eszközöket, amelyekre nem lehet hirdetésblokkoló alkalmazást telepíteni.

## Amire a routerének szüksége van

A routerének támogatnia kell a **titkosított DNS-t hosztnévvel**, például DNS over TLS (DoT) vagy DNS over HTTPS (DoH) protokollokat. Sok újabb router támogatja ezt, beleértve az alábbi modelleket is. Attól függően, hogy a routere melyiket támogatja, szüksége lesz a DNS nevére vagy a DoH linkjére, amelyeket fent talál a _Saját adatok_ alatt.

<div class="note important">

**Csak natív IP-címeket támogat?** Sok internetszolgáltató routere csak natív IP-címeket fogad el DNS szervernek. A támogatás ezekhez úton van. Addig is, állítsa be az eszközeit egyenként: [Android](../android-private-dns/), [Mac és Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) és [böngészők](../browser-dns-over-https/). Kis továbbítót is futtathat egy Raspberry Pi-n, ahogy a [Pi-hole útmutatóban](../switch-from-pihole/) leírtuk.

</div>

## FRITZ!Box

FRITZ!OS 7.20 vagy újabb.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. A _DNS szerver feloldott nevei_ mezőbe csak ezt írja be: {% dot %}. **Távolítson el minden egyéb bejegyzést.** A FRITZ!Box minden felsorolt feloldót használ, és bármelyik másik átengedi a hirdetéseket.
4. Untick _Allow fallback to unencrypted name resolution_.
5. Ha látja, hogy _Átváltás nyilvános DNS szerverekre, ha a DNS megszakad_, kapcsolja ki.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Cím: {% ip "dot" %}
   - TLS gazdanév: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Nyissa meg a _Szolgáltatások → HTTPS DNS Proxy_ menüt. Törölje a más szolgáltatók példányait.
3. Adjon hozzá egy példányt egy egyéni resolver URL-lel: {% doh %}
4. _Mentés és alkalmazás_. A csomag automatikusan beállítja rá a dnsmasq-ot.

## Egyéb routerek

Keressen egy olyan beállítást, mint a _DNS over TLS_, _Privát DNS_, _Titkosított DNS_ vagy _DNS over HTTPS_. Adja meg a fenti Blokada DNS nevét vagy DoH linkjét, majd távolítson el minden más DNS szervert, beleértve a tartalék szervereket is.

## Ellenőrizze, hogy működik-e

1. Indítson újra egy eszközt, vagy kapcsolja ki majd vissza a Wi-Fi-t, hogy az átvegye a változást.
2. Böngésszen egy percig, majd nyissa meg az irányítópulton az _Aktivitás_ oldalt. Itt jelennek meg a hálózat lekérdezései.

## Ha néhány eszközön még mindig megjelennek hirdetések

Egyes eszközök megkerülik a routert: olyan telefonok, amelyeken _Privát DNS_ van beállítva, böngészők, ahol a _biztonságos DNS_ másik szolgáltatóra van állítva, és olyan eszközök is, amelyek saját DNS-t használnak. Ezeken az eszközön állítsa be külön, vagy kapcsolja ki az eszköz egyéni DNS beállítását.

<div class="note tip">

A router mögött minden eszköz egy címet oszt meg, így az irányítópulton a hálózata egyetlen eszközként jelenik meg. Ha külön szeretné látni a telefonokat és laptopokat, állítsa be azokat saját Blokada DNS névvel. Így akkor is megmarad a blokkolás, ha elhagyja az otthonát.

</div>
