---
title: Egy Pi-hole alternatíva, amelyhez nem szükséges hardver.
description: Vidd át otthoni reklámblokkolásodat a Pi-hole-ról a Blokada Cloud-ra, vagy használd tovább a Pi-hole-t, és irányítsd a lekérdezéseit a Blokada-n keresztül.
updated: 2026-10-02
order: 1
---

A Pi-hole minden eszközön blokkolja a reklámokat a hálózatodon, amíg a Raspberry Pi működik, naprakész és otthon van. A Blokada Cloud ugyanezt a feladatot végzi el a szervereinken keresztül:

- **Nincs külön doboz karbantartása.** Nincs SD kártya, nincs frissítés, nincs kiesés, ha a Pi leáll.
- **Otthonon kívül is működik.** A telefonok és laptopok továbbra is blokkolnak mobilneten és más Wi-Fi hálózatokon is.
- **Titkosított.** Az eszközök a Blokada-val DNS over TLS vagy DNS over HTTPS protokollon keresztül kommunikálnak, így a szolgáltatód nem tudja elolvasni vagy módosítani a lekérdezéseidet.
- **Egyetlen vezérlőpult.** Feketelisták, engedélyezett és blokkolt domainek, valamint eszközönkénti aktivitás a [app.blokada.org](https://app.blokada.org/?src=guides) oldalon.

Két módon válthatsz. Cseréld le teljesen a Pi-hole-t, vagy tartsd meg, és használd a Blokada Cloud-ot upstreamként.

## 1. lehetőség: a Pi-hole lecserélése

1. **Szerezd be a Blokada Cloud-ot**, és nyisd meg a vezérlőpultot. A DNS neved és DoH linked a _Setup_ résznél, illetve fent a _Your details_ alatt található.
2. **Irányítsd a routeredet a Blokada-ra a Pi-hole helyett.** Kövesd a [router útmutatót](../router-ad-blocking/). Ha a routered csak egyszerű IP címet fogad el DNS szerverként, akkor állítsd be az eszközöket egyenként: [Android](../android-private-dns/), [Mac és Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) és [böngészők](../browser-dns-over-https/).
3. **Ha a Pi-hole volt a DHCP szervered,** kapcsold vissza a DHCP-t a routeredben _mielőtt_ kikapcsolod a Pi-t. Különben az eszközeid nem kapnak hálózati címet.
4. **Vidd át a listáidat.** A vezérlőpulton válaszd a feketelistákat a _Blocklists_ alatt, és add hozzá saját engedélyezett vagy blokkolt domaineidet az _Exceptions_ részben.
5. **Kapcsold ki a Pi-hole-t,** vagy használd más célra.

<div class="note aside">

A Pi-hole az összes eszközt IP cím szerint mutatta a hálózatodban. A Blokada esetén minden eszköz saját nevével jelenik meg, ha saját Blokada DNS nevet használ. Az a router, amely egy Blokada DNS névre van beállítva, egyetlen eszközként jelenik meg.

</div>

## 2. lehetőség: a Pi-hole megtartása, Blokada Cloud használata upstreamként

Ha meg akarod őrizni a helyi beállításaidat, például a helyi hosztneveket, DHCP-t vagy saját listákat, akkor a Pi-hole névfeloldásait titkosított kapcsolaton keresztül továbbítsd a Blokada-hoz. A Pi-hole önmagában nem tud titkosított továbbítást, ezért egy kis továbbító fut mellette. Ez az útmutató a [dnsproxy](https://github.com/AdguardTeam/dnsproxy) nevű nyílt forráskódú továbbítót használja, amely egyetlen fájl.

1. A Pi-hole gépen töltsd le a `dnsproxy` kiadást a processzorodhoz (`linux-arm64` egy újabb Raspberry Pi-hez) a kiadások oldaláról, majd másold a `dnsproxy` binárist a `/usr/local/bin/` mappába.
2. Hozd létre ezt: `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Titkosított DNS továbbító a Blokada Cloud-hoz
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Indítsd el: `sudo systemctl enable --now dnsproxy`
4. A Pi-hole adminban nyisd meg a _Settings → DNS_ menüt. Kapcsold ki az összes upstream szervert, majd add hozzá a `127.0.0.1#5054`-et egyéni upstream szerverként. Mentsd el.
5. Ellenőrizd a vezérlőpult _Aktivitás_ oldalát. Mostantól a hálózatod lekérdezései ott is megjelennek.

A Pi-hole saját feketelistáit kikapcsolhatod, és a blokkolást a vezérlőpultól kezelheted, vagy megtarthatod mindkettőt.

## Gyakran ismételt kérdések

**Szükségem van Blokada Plus-ra?** Nem. A Blokada Cloud lefedi a teljes otthonodra vonatkozó DNS alapú blokkolást. A [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) egy VPN-t ad hozzá.

**Mi van, ha a Blokada nem elérhető?** Az eszközeid nem tudnak neveket feloldani, amíg vissza nem tér, ugyanúgy, mint amikor a Pi-hole leáll. Ne adj hozzá második, szűretlen DNS szervert tartaléknak! A legtöbb eszköz ugyanis véletlenszerűen használja szervereit, így a hirdetések átjuthatnak.
