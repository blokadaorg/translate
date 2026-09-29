---
title: Ett alternativ till Pi-hole som inte kräver någon hårdvara
description: Flytta hemmets reklamblockering från Pi-hole till Blokada Cloud, eller behåll din Pi-hole och skicka dess uppslag via Blokada.
updated: 2026-09-23
order: 1
---

En Pi-hole blockerar reklam för alla enheter i nätverket, så länge Raspberry Pi:n är igång, uppdaterad och hemma. Blokada Cloud gör samma jobb från våra servrar:

- **Ingen låda att sköta.** Inga SD-kort, inga uppdateringar och inget avbrott när Pi:n går ner.
- **Fungerar utanför hemmet.** Telefoner och datorer behåller blockeringen på mobildata och andra wifi-nätverk.
- **Krypterat.** Enheterna pratar med Blokada via DNS över TLS eller DNS över HTTPS, så din leverantör kan inte läsa eller ändra dina uppslag.
- **En dashboard.** Blocklistor, tillåtna och blockerade domäner och aktivitet per enhet, på [app.blokada.org](https://app.blokada.org/?src=guides).

Det finns två sätt att byta. Ersätt Pi-hole helt, eller behåll den och använd Blokada Cloud som uppströmsserver.

## Alternativ 1: ersätt Pi-hole

1. **Skaffa Blokada Cloud** och öppna dashboarden. Under *Inställningar* hittar du dina uppgifter:
   - Ditt Blokada-DNS-namn, för DNS över TLS: {% dot %}
   - Din DoH-länk, för DNS över HTTPS: {% doh %}
2. **Peka routern mot Blokada i stället för Pi-hole.** Följ [routerguiden](../router-ad-blocking/). Om routern bara accepterar en vanlig IP-adress som DNS-server ställer du in enheterna en i taget i stället: [Android](../android-private-dns/), [Mac och Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) och [webbläsare](../browser-dns-over-https/).
3. **Om din Pi-hole var DHCP-server** aktiverar du DHCP i routern igen *innan* du stänger av Pi:n. Annars slutar dina enheter att få nätverksadresser.
4. **Flytta dina listor.** I dashboarden väljer du blocklistor under *Blocklists* och lägger till egna tillåtna eller blockerade domäner under *Undantag*.
5. **Stäng av Pi-hole,** eller använd den till något annat.

<div class="note">

Din Pi-hole visade varje enhet i nätverket med dess IP-adress. Med Blokada visas varje enhet med sitt eget namn, så länge den använder sitt eget Blokada-DNS-namn. En router som är inställd med ett Blokada-DNS-namn visas som en enhet.

</div>

## Alternativ 2: behåll Pi-hole och använd Blokada Cloud uppströms

Vill du behålla din lokala installation, till exempel lokala värdnamn, DHCP eller egna listor, kan du låta Pi-hole vidarebefordra sina uppslag till Blokada över en krypterad anslutning. Pi-hole kan inte själv vidarebefordra krypterat, så en liten vidarebefordrare körs bredvid. Den här guiden använder [dnsproxy](https://github.com/AdguardTeam/dnsproxy), en vidarebefordrare med öppen källkod som består av en enda fil.

1. Ladda ner den `dnsproxy`-version som passar din processor (`linux-arm64` för en nyare Raspberry Pi) från projektets releasesida till Pi-hole-datorn och kopiera binärfilen `dnsproxy` till `/usr/local/bin/`.
2. Skapa `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Encrypted DNS forwarder to Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Starta den: `sudo systemctl enable --now dnsproxy`
4. Öppna *Settings → DNS* i Pi-holes administrationsgränssnitt. Avmarkera alla uppströmsservrar och lägg till `127.0.0.1#5054` som anpassad uppströmsserver. Spara.
5. Kontrollera sidan *Aktivitet* i dashboarden. Uppslag från ditt nätverk visas nu där.

Du kan stänga av Pi-holes egna blocklistor och sköta blockeringen i dashboarden, eller behålla båda.

## Vanliga frågor

**Behöver jag Blokada Plus?** Nej. Blokada Cloud sköter DNS-blockeringen för hela hemmet. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) lägger till en VPN ovanpå.

**Vad händer om Blokada inte går att nå?** Dina enheter kan inte slå upp namn förrän tjänsten är tillbaka, precis som när en Pi-hole går ner. Lägg inte till en andra, ofiltrerad DNS-server som reserv. De flesta enheter använder alla sina servrar slumpmässigt, så reklam skulle slinka igenom.
