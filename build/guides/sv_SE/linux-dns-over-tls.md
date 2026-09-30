---
title: Blockera reklam i Linux med DNS över TLS
description: Ställ in systemd-resolved på att använda Blokada Cloud via krypterad DNS över TLS och blockera reklam och spårare för alla appar på din Linux-dator.
updated: 2026-09-28
order: 9
---

De flesta aktuella Linux-distributioner, inklusive Ubuntu och Fedora, löser namn via _systemd-resolved_, som stöder DNS över TLS. På Debian, installera det först med `sudo apt install systemd-resolved`. Peka den mot Blokada Cloud, så blockeras annonser och spårare för alla appar på datorn.

## Ställ in systemd-resolved

1. Skapa mappen med `sudo mkdir -p /etc/systemd/resolved.conf.d` och sedan filen `/etc/systemd/resolved.conf.d/blokada.conf` med de här inställningarna:

<pre><code>[Resolve]\nDNS={{ site.dnsIps.dot }}#<span data-dns=\"dot\">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>\nDNSOverTLS=yes\nDomains=~.</code></pre>

<ol start="2">
<li>Starta om den: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Kontrollera den: <code>resolvectl status</code> visar <code>+DNSOverTLS</code> och Blokada-servern.</li>
</ol>

Delen efter `#` är ditt Blokada-DNS-namn: {% dot %} systemd-resolved kontrollerar serverns certifikat mot det, och Blokada använder det för att veta vilken enhet som frågar.

<div class="note">

**NetworkManager** skickar också med nätverkets DNS-servrar. `Domains=~.` skickar alla uppslag till Blokada, men om `resolvectl status` ändå visar en annan server på en anslutning, stäng av automatisk DNS för den anslutningen (brytaren _Automatisk_ bredvid _DNS_ i IPv4- och IPv6-inställningarna).

</div>

## Utan systemd-resolved

Om `resolvectl` inte hittas, löser din distribution namn på ett annat sätt. Ställ istället in säker DNS i din webbläsare enligt [webbläsarguiden](../browser-dns-over-https/), eller konfigurera din [router](../router-ad-blocking/) för att täcka hela hemmet.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan _Aktivitet_ i [dashboarden](https://app.blokada.org/stats?src=guides). Den här datorns uppslag visas där.

<div class="note">

Vill du ha ett VPN på den här datorn också? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) inkluderar en WireGuard-konfiguration som krypterar all trafik, med samma blockering.

</div>
