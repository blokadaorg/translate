---
title: Hirdetések blokkolása az egész hálózaton routeres hirdetésblokkolással.
description: Állítsa be a Blokada Cloud szolgáltatást a routerén egyszer, és az otthoni összes eszköz védve lesz, beleértve a TV-ket, játékkonzolokat és okoshangszórókat is, amelyek nem tudnak hirdetésblokkolót futtatni.
updated: 2026-10-09
order: 4
---

A hálózatán lévő minden eszköz megkérdezi a routert, melyik DNS szervert használja. Állítsa be a routert a Blokada Cloud-ra, így a hirdetések és követők blokkolva lesznek minden eszközön, ami mögötte van. Ez magában foglalja az okos TV-ket, játékkonzolokat, streaming stickeket és okosotthon eszközöket, amelyekre nem lehet hirdetésblokkoló alkalmazást telepíteni.

## Amire a routerének szüksége van

Kétféleképpen állíthatja be az útválasztót:

- **Titkosított DNS hosztnévvel**, vagyis DNS over TLS (DoT) vagy DNS over HTTPS (DoH). Számos újabb útválasztó támogatja ezeket, beleértve az alábbi modelleket is. Attól függően, melyiket támogatja az útválasztója, szüksége lesz a DNS nevére vagy a DoH hivatkozására, mindkettőt megtalálja fent a _Saját adatok_ részben.
- **Egy sima IPv6 DNS-cím.** Sok internetszolgáltatói útválasztó csak egyszerű IP-címet fogad el DNS-nek. Ha az öné is ilyen, és a kapcsolaton van IPv6 támogatás, a Blokada ad önnek egy IPv6 címet, amelyet megadhat. Lásd: [Olyan útválasztók, amelyek csak IP-címet fogadnak el](#routers-that-only-take-an-ip-address).

Használjon titkosított DNS-t, ha az útválasztója támogatja. A lekérdezések így titkosítva maradnak a Blokada felé vezető úton.

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

Keressen egy beállítást, amelynek neve _DNS over TLS_, _Privát DNS_, _Titkosított DNS_ vagy _DNS over HTTPS_. Adja meg a Blokada DNS nevét vagy a fenti DoH hivatkozást, és távolítson el minden más DNS szervert, beleértve a tartalék szervereket is. Ha nincs ilyen beállítás, használjon egy egyszerű IPv6 címet az alábbiak szerint.

## Olyan routerek, amelyek csak IP címet fogadnak el

Ehhez a routerének és az internetkapcsolatának IPv6 támogatással kell rendelkeznie. Az IPv4 címek támogatása később érkezik.

1. A [vezérlőpulton](https://app.blokada.org/setup?src=guides) nyissa meg a _Beállítás_ menüt, és válassza a _Router, TV, játékkonzol_ lehetőséget.
2. Nevezze el a routert, például _Otthoni router_, majd válassza a _Cím lekérése_ opciót. A név megjelenik tevékenységei között, és később nem módosítható.
3. A router beállításainál keresse meg az IPv6-hoz tartozó DNS szervereket, általában az _Internet_, _WAN_ vagy _IPv6_ menüpont alatt, és adja meg a címet egyetlen DNS szerverként.
4. **Távolítson el minden más DNS szervert, beleértve az IPv4-eseket is.** Azok az eszközök, amelyek a routertől IPv4 DNS szervert kapnak, néhány lekérdezést a Blokada megkerülésével küldenek el. Ha a router nem tudja üresen hagyni az IPv4 DNS-t, akkor egyenként állítsa be az eszközöket: [Android](../android-private-dns/), [Mac és Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) és [böngészők](../browser-dns-over-https/).

Ugyanez a beállítás működik TV-n vagy játékkonzolon is, ha kézzel tudja megadni a DNS szervert. Mindegyiknek adjon külön címet, hogy név szerint jelenjenek meg tevékenységeiben.

<div class="note aside">

Ezek a lekérdezések titkosítatlanul mennek el a Blokadához, mint bármely egyszerű DNS szerver esetén. Ha a router támogatja a DNS over TLS-t vagy a DNS over HTTPS-t, inkább azt használja.

</div>

## Ellenőrizze, hogy működik-e

1. Indítson újra egy eszközt, vagy kapcsolja ki majd vissza a Wi-Fi-t, hogy az átvegye a változást.
2. Az érintett eszközön kapcsolja ki a Blokadát, ha fut, majd nyissa meg a [go.blokada.org/test](https://go.blokada.org/test) oldalt. Megmutatja, hogy a DNS forgalma a Blokadán keresztül megy-e.
3. Böngésszen egy percig, majd nyissa meg a _Tevékenység_ oldalt a [vezérlőpulton](https://app.blokada.org/stats?src=guides). Itt megjelennek a hálózata lekérdezései.

## Ha néhány eszközön még mindig megjelennek hirdetések

Egyes eszközök megkerülik a routert: olyan telefonok, amelyeken _Privát DNS_ van beállítva, böngészők, ahol a _biztonságos DNS_ másik szolgáltatóra van állítva, és olyan eszközök is, amelyek saját DNS-t használnak. Ezeken az eszközön állítsa be külön, vagy kapcsolja ki az eszköz egyéni DNS beállítását.

<div class="note tip">

A router mögött minden eszköz egy címet oszt meg, így az irányítópulton a hálózata egyetlen eszközként jelenik meg. Ha külön szeretné látni a telefonokat és laptopokat, állítsa be azokat saját Blokada DNS névvel. Így akkor is megmarad a blokkolás, ha elhagyja az otthonát.

</div>
