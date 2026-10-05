---
title: Een Pi-hole alternatief dat geen hardware nodig heeft.
description: Verplaats de advertentieblokkering van je huis van een Pi-hole naar Blokada Cloud, of behoud je Pi-hole en stuur de zoekopdrachten daarvan via Blokada.
updated: 2026-10-02
order: 1
---

Een Pi-hole blokkeert advertenties voor elk apparaat op je netwerk, zolang de Raspberry Pi aanstaat, up-to-date is en thuis is. Blokada Cloud doet hetzelfde vanaf onze servers:

- **Geen apparaat om te onderhouden.** Geen SD-kaarten, geen updates, geen uitval als de Pi uitvalt.
- **Het werkt ook buitenshuis.** Telefoons en laptops blijven advertenties blokkeren via mobiel internet en andere Wi-Fi netwerken.
- **Versleuteld.** Apparaten communiceren met Blokada via DNS over TLS of DNS over HTTPS, zodat je provider je zoekopdrachten niet kan lezen of wijzigen.
- **Één dashboard.** Blokkeerlijsten, toegestane en geblokkeerde domeinen, en activiteit per apparaat, op [app.blokada.org](https://app.blokada.org/?src=guides).

Er zijn twee manieren om over te stappen. Vervang de Pi-hole volledig, of houd hem en gebruik Blokada Cloud als zijn upstream.

## Optie 1: vervang de Pi-hole

1. **Neem Blokada Cloud** en open het dashboard. Je DNS-naam en DoH-link staan daar onder _Installatie_, en hierboven onder _Je gegevens_.
2. **Stel je router in op Blokada in plaats van de Pi-hole.** Volg de [routergids](../router-ad-blocking/). Accepteert je router alleen een gewoon IP-adres als DNS-server? Stel dan je apparaten één voor één in: [Android](../android-private-dns/), [Mac en Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) en [browsers](../browser-dns-over-https/).
3. **Als je Pi-hole de DHCP-server was,** schakel DHCP dan weer in op je router _voordat_ je de Pi uitzet. Anders krijgen je apparaten geen netwerkadressen meer.
4. **Verplaats je lijsten.** Kies in het dashboard blokkeerlijsten onder _Blocklists_, en voeg je eigen toegestane of geblokkeerde domeinen toe onder _Exceptions_.
5. **Schakel de Pi-hole uit,** of bewaar hem voor een ander doel.

<div class="note aside">

Je Pi-hole gaf elk apparaat in het netwerk weer via zijn IP-adres. Met Blokada verschijnt elk apparaat onder zijn eigen naam, zolang het zijn eigen Blokada DNS-naam gebruikt. Een router ingesteld met één Blokada DNS-naam wordt als één apparaat weergegeven.

</div>

## Optie 2: behoud de Pi-hole, gebruik Blokada Cloud als upstream

Wil je je lokale configuratie behouden, zoals lokale hostnamen, DHCP of je eigen lijsten, laat dan de Pi-hole verzoeken doorsturen naar Blokada via een versleutelde verbinding. Pi-hole kan zelf geen versleuteld doorsturen, daarom draait er een kleine forwarder naast. Deze handleiding gebruikt [dnsproxy](https://github.com/AdguardTeam/dnsproxy), een open source forwarder die uit één bestand bestaat.

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
4. Open in het Pi-hole-beheer _Instellingen → DNS_. Vink elke upstream-server uit en voeg `127.0.0.1#5054` toe als aangepaste upstream-server. Sla op.
5. Controleer de _Activiteit_-pagina van het dashboard. Verzoeken vanaf je netwerk verschijnen nu daar.

Je kunt de eigen blokkeerlijsten van de Pi-hole uitschakelen en het blokkeren beheren in het dashboard, of beide houden.

## Veelgestelde vragen

**Heb ik Blokada Plus nodig?** Nee. Blokada Cloud dekt DNS-blokkering voor je hele huis. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) voegt daar een VPN bovenop toe.

**Wat als Blokada niet bereikbaar is?** Je apparaten kunnen geen namen oplossen tot het terug is, net als wanneer een Pi-hole uitvalt. Voeg geen tweede, ongefilterde DNS-server toe als back-up. De meeste apparaten gebruiken willekeurig al hun servers, waardoor advertenties toch doorkomen.
