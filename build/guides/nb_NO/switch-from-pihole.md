---
title: Et Pi-hole-alternativ som ikke krever maskinvare
description: Flytt hjemmets annonseblokkering fra en Pi-hole til Blokada Cloud, eller behold din Pi-hole og send oppslagene via Blokada.
updated: 02.10.2026
order: 1
---

En Pi-hole blokkerer annonser for alle enheter på nettverket ditt, så lenge Raspberry Pi kjører, er oppdatert og hjemme. Blokada Cloud gjør den samme jobben fra våre servere:

- **Ingen boks å vedlikeholde.** Ingen SD-kort, ingen oppdateringer, ingen nedetid når Pi-en slår seg av.
- **Det virker også utenfor hjemmet.** Telefoner og bærbare beholder blokkeringen på mobildata og andre Wi-Fi-nettverk.
- **Kryptert.** Enhetene snakker med Blokada over DNS over TLS eller DNS over HTTPS, så leverandøren din ikke kan lese eller endre oppslagene dine.
- **Ett dashbord.** Blokklister, tillatte og blokkerte domener, og aktivitet per enhet, finnes på [app.blokada.org](https://app.blokada.org/?src=guides).

Det finnes to måter å bytte på. Bytt ut Pi-hole fullstendig, eller behold den og bruk Blokada Cloud som dens oppstrøms.

## Alternativ 1: Bytt ut Pi-hole

1. **Få Blokada Cloud** og åpne dashbordet. Ditt DNS-navn og DoH-lenke finner du under _Oppsett_ der, og under _Dine detaljer_ ovenfor.
2. **Pek ruteren din mot Blokada i stedet for Pi-hole.** Følg [ruter-guiden](../router-ad-blocking/). Hvis ruteren din kun godtar en vanlig IP-adresse som DNS-server, sett opp enhetene dine én etter én i stedet: [Android](../android-private-dns/), [Mac og Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) og [nettlesere](../browser-dns-over-https/).
3. **Hvis din Pi-hole var DHCP-serveren,** slå på DHCP i ruteren _før_ du slår av Pi-en. Ellers får ikke enhetene dine nettverksadresser.
4. **Flytt listene dine.** I dashbordet velger du blokklister under _Blocklists_, og legger til dine egne tillatte eller blokkerte domener under _Exceptions_.
5. **Slå av Pi-hole,** eller behold den til noe annet.

<div class="note aside">

Pi-hole viste hver enhet på nettverket med sin IP-adresse. Med Blokada vises hver enhet med sitt eget navn, så lenge den bruker sitt eget Blokada DNS-navn. En ruter satt opp med ett Blokada DNS-navn vises som én enhet.

</div>

## Alternativ 2: Behold Pi-hole, bruk Blokada Cloud som oppstrøms

Hvis du vil beholde ditt lokale oppsett, som lokale vertsnavn, DHCP eller egne lister, lar du Pi-hole videresende oppslagene sine til Blokada over en kryptert tilkobling. Pi-hole kan ikke gjøre kryptert videresending selv, så en liten videresender kjører ved siden av. Denne veiledningen bruker [dnsproxy](https://github.com/AdguardTeam/dnsproxy), en åpen kildekode-videresender som er én enkelt fil.

1. På Pi-hole-maskinen, last ned `dnsproxy`-utgivelsen for din CPU (`linux-arm64` for en nyere Raspberry Pi) fra releases-siden, og kopier `dnsproxy`-programmet til `/usr/local/bin/`.
2. Opprett `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Kryptert DNS-videresender til Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Start den: `sudo systemctl enable --now dnsproxy`
4. I Pi-hole administrasjon, åpne _Innstillinger → DNS_. Fjern avhukingen for alle oppstrøms servere og legg til `127.0.0.1#5054` som en egendefinert oppstrøms server. Lagre.
5. Sjekk dashbordet på siden _Aktivitet_. Oppslag fra nettverket ditt vises nå der.

Du kan slå av Pi-holes egne blokklister og administrere blokkeringen i dashbordet, eller bruke begge.

## Ofte stilte spørsmål

**Trenger jeg Blokada Plus?** Nei. Blokada Cloud dekker DNS-blokkering for hele hjemmet ditt. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) legger til et VPN på toppen.

**Hva om Blokada er utilgjengelig?** Enhetene dine kan ikke løse navn før den er tilbake, akkurat som når en Pi-hole er nede. Ikke legg til en andre, ufiltrert DNS-server som reserve. De fleste enheter bruker alle servere tilfeldig, så annonser vil slippe igjennom.
