---
title: Ett alternativ till Pi-hole som inte kräver någon hårdvara
description: Flytta hemmets reklamblockering från Pi-hole till Blokada Cloud, eller behåll din Pi-hole och skicka dess uppslag via Blokada.
updated: 2026-10-01'}]} 2026-10-01
order: 1
---

En Pi-hole blockerar annonser för alla enheter i ditt nätverk, så länge Raspberry Pi körs, är uppdaterad och finns hemma. Blokada Cloud gör samma jobb från våra servrar:

- **Ingen låda att sköta.** Inga SD-kort, inga uppdateringar och inget avbrott när Pi:n går ner.
- **Fungerar utanför hemmet.** Telefoner och datorer behåller blockeringen på mobildata och andra wifi-nätverk.
- **Krypterat.** Enheterna pratar med Blokada via DNS över TLS eller DNS över HTTPS, så din leverantör kan inte läsa eller ändra dina uppslag.
- **En dashboard.** Blocklistor, tillåtna och blockerade domäner och aktivitet per enhet, på [app.blokada.org](https://app.blokada.org/?src=guides).

Det finns två sätt att byta. Byt ut Pi-hole helt, eller behåll den och låt den använda Blokada Cloud som upstream.

## Alternativ 1: ersätt Pi-hole

1. **Skaffa Blokada Cloud** och öppna instrumentpanelen. Under _Setup_ hittar du dina uppgifter:
   - Ditt Blokada-DNS-namn, för DNS över TLS: {% dot %}
   - Din DoH-länk, för DNS över HTTPS: {% doh %}
2. **Peka din router mot Blokada istället för Pi-hole.** Följ [routerguiden](../router-ad-blocking/). Om din router bara accepterar en vanlig IP-adress som DNS-server, konfigurera enheterna en och en istället: [Android](../android-private-dns/), [Mac och Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) och [webbläsare](../browser-dns-over-https/).
3. **Om din Pi-hole var DHCP-server,** slå på DHCP i routern _innan_ du stänger av Pi. Annars kommer dina enheter inte att få några nätverksadresser.
4. **Flytta dina listor.** I dashboarden väljer du blocklistor under _Blocklistor_ och lägger till egna tillåtna eller blockerade domäner under _Undantag_.
5. **Stäng av Pi-hole,** eller använd den till något annat.

<div class="note">

Din Pi-hole visade varje enhet i nätverket med dess IP-adress. Med Blokada visas varje enhet med sitt eget namn, så länge den använder sitt eget Blokada DNS-namn. En router som är konfigurerad med ett Blokada DNS-namn visas som en enhet.

</div>

## Alternativ 2: behåll Pi-hole och använd Blokada Cloud uppströms

Om du vill behålla din lokala installation, såsom lokala värdnamn, DHCP eller egna listor, låt Pi-hole vidarebefordra sina uppslagningar till Blokada över en krypterad anslutning. Pi-hole kan inte vidarebefordra krypterat själv, så en liten forwarder körs bredvid den. Denna guide använder [dnsproxy](https://github.com/AdguardTeam/dnsproxy), en öppen källkods-forwarder som är en enda fil.

1. Ladda ner den `dnsproxy`-version som passar din processor (`linux-arm64` för en nyare Raspberry Pi) från projektets releasesida till Pi-hole-datorn och kopiera binärfilen `dnsproxy` till `/usr/local/bin/`.
2. Skapa `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Krypterad DNS-forwarder till Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Starta den: `sudo systemctl enable --now dnsproxy`
4. Öppna _Inställningar → DNS_ i Pi-hole-admin. Avmarkera alla upstream-servrar och lägg till `127.0.0.1#5054` som en anpassad upstream-server. Spara.
5. Kontrollera sidan _Aktivitet_ i instrumentpanelen. Uppslagningar från ditt nätverk visas nu där.

Du kan stänga av Pi-holes egna blocklistor och sköta blockeringen i dashboarden, eller behålla båda.

## Vanliga frågor

**Behöver jag Blokada Plus?** Nej. Blokada Cloud täcker DNS-blockering för hela ditt hem. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) lägger till ett VPN ovanpå.

**Vad händer om Blokada inte går att nå?** Dina enheter kan inte slå upp namn förrän Blokada är tillbaka, precis som när en Pi-hole går ner. Lägg inte till en andra, ofiltrerad DNS-server som reserv. De flesta enheter använder alla sina servrar slumpmässigt, så annonser kan släppas igenom.
