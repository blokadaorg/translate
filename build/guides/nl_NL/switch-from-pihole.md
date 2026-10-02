---
title: Een Pi-hole alternatief dat geen hardware nodig heeft.
description: Verplaats de advertentieblokkering van je huis van een Pi-hole naar Blokada Cloud, of behoud je Pi-hole en stuur de zoekopdrachten daarvan via Blokada.
updated: 2026-10-02
order: 1
---

Een Pi-hole blokkeert advertenties voor elk apparaat op je netwerk, zolang de Raspberry Pi actief, bijgewerkt en thuis is. Blokada Cloud doet hetzelfde vanaf onze servers:

- **Geen apparaat om te onderhouden.** Geen SD-kaarten, geen updates, geen uitval als de Pi uitvalt.
- **Het werkt ook buitenshuis.** Telefoons en laptops blijven advertenties blokkeren via mobiel internet en andere Wi-Fi netwerken.
- **Versleuteld.** Apparaten communiceren met Blokada via DNS over TLS of DNS over HTTPS, zodat je provider je zoekopdrachten niet kan lezen of wijzigen.
- **Één dashboard.** Blokkeerlijsten, toegestane en geblokkeerde domeinen, en activiteit per apparaat, op [app.blokada.org](https://app.blokada.org/?src=guides).

Er zijn twee manieren om over te stappen. Vervang de Pi-hole volledig, of houd hem en gebruik Blokada Cloud als zijn upstream.

## Optie 1: vervang de Pi-hole

1. **Haal Blokada Cloud** en open het dashboard. Je DNS-naam en DoH-link vind je onder _Setup_ daar, en onder _Jouw gegevens_ hierboven.
2. **Stel je router in op Blokada in plaats van de Pi-hole.** Volg de [routerhandleiding](../router-ad-blocking/). Als je router alleen een gewoon IP-adres als DNS-server accepteert, stel dan je apparaten één voor één in: [Android](../android-private-dns/), [Mac en Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) en [browsers](../browser-dns-over-https/).
3. **Als je Pi-hole de DHCP-server was,** zet DHCP weer aan op je router _voordat_ je de Pi uitschakelt. Anders krijgen je apparaten geen netwerkadressen meer.
4. **Verplaats je lijsten.** Kies in het dashboard blokkeerlijsten onder _Blocklists_, en voeg je eigen toegestane of geblokkeerde domeinen toe onder _Exceptions_.
5. **Schakel de Pi-hole uit,** of bewaar hem voor een ander doel.

<div class="note aside">

Je Pi-hole liet elk apparaat in het netwerk zien met zijn IP-adres. Met Blokada verschijnt elk apparaat onder zijn eigen naam, zolang het zijn eigen Blokada DNS-naam gebruikt. Een router die is ingesteld met één Blokada DNS-naam verschijnt als één apparaat.

</div>

## Optie 2: behoud de Pi-hole, gebruik Blokada Cloud als upstream

Als je je lokale instelling wilt behouden, zoals lokale hostnamen, DHCP of eigen lijsten, laat de Pi-hole de zoekopdrachten doorsturen naar Blokada via een versleutelde verbinding. Pi-hole kan geen versleutelde forwarding uitvoeren, dus er draait een kleine forwarder naast. Deze handleiding gebruikt [dnsproxy](https://github.com/AdguardTeam/dnsproxy), een open source forwarder die uit één bestand bestaat.

1. Download op de Pi-hole-machine de `dnsproxy` release voor je CPU (`linux-arm64` voor een recente Raspberry Pi) van de releasespagina, en kopieer het bestand `dnsproxy` naar `/usr/local/bin/`.
2. Maak `/etc/systemd/system/dnsproxy.service`:

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

3. Start deze: `sudo systemctl enable --now dnsproxy`
4. Open in de Pi-hole admin _Instellingen → DNS_. Vink alle upstream-servers uit en voeg `127.0.0.1#5054` toe als aangepaste upstream-server. Opslaan.
5. Controleer de _Activiteit_-pagina in het dashboard. Zoekopdrachten vanaf je netwerk verschijnen nu daar.

Je kunt de eigen blokkeerlijsten van de Pi-hole uitschakelen en het blokkeren beheren in het dashboard, of beide houden.

## Veelgestelde vragen

**Heb ik Blokada Plus nodig?** Nee. Blokada Cloud verzorgt DNS-blokkering voor je hele huis. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) voegt een VPN toe.

**Wat als Blokada niet bereikbaar is?** Je apparaten kunnen geen namen oplossen totdat deze weer beschikbaar is, net zoals wanneer een Pi-hole uitvalt. Voeg geen tweede, ongefilterde DNS-server toe als fallback. De meeste apparaten gebruiken al hun servers willekeurig, zodat advertenties toch door kunnen komen.
