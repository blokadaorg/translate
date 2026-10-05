---
title: Blokker annonser på Linux med DNS over TLS
description: Konfigurer systemd-resolved til å bruke Blokada Cloud over kryptert DNS over TLS, og blokker annonser og sporingsmekanismer for alle apper på Linux-maskinen din.
updated: 2026-10-02
order: 9
---

De fleste moderne Linux-distribusjoner, inkludert Ubuntu og Fedora, løser navn via _systemd-resolved_, som støtter DNS over TLS. På Debian, installer det først med `sudo apt install systemd-resolved`. Pek den mot Blokada Cloud, så blir annonser og sporing blokkert for alle apper på datamaskinen.

## Konfigurer systemd-resolved

1. Opprett mappen med <code>sudo mkdir -p /etc/systemd/resolved.conf.d</code>, og deretter filen <code>/etc/systemd/resolved.conf.d/blokada.conf</code> med disse innstillingene:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Start den på nytt: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Sjekk: <code>resolvectl status</code> viser <code>+DNSOverTLS</code> og Blokada-serveren.</li>
</ol>

Delen etter <code>#</code> er ditt Blokada DNS-navn: {% dot %} systemd-resolved sjekker serverens sertifikat mot dette, og Blokada bruker det til å vite hvilken enhet som spør.

<div class="note important">

**NetworkManager** videresender også DNS-serverne til ditt nettverk. `Domains=~.` sender alle oppslag til Blokada, men hvis `resolvectl status` fortsatt viser en annen server på en tilkobling, slå av automatisk DNS for den tilkoblingen (bryteren _Automatisk_ ved siden av _DNS_ i IPv4- og IPv6-innstillingene).

</div>

## Uten systemd-resolved

Hvis `resolvectl` ikke finnes, løser din distribusjon navn på en annen måte. Sett opp sikker DNS i nettleseren din i stedet, som beskrevet i [nettleserguiden](../browser-dns-over-https/), eller konfigurer din [ruter](../router-ad-blocking/) for å dekke hele hjemmet.

## Sjekk at det virker

Åpne noen nettsider, og se deretter på siden _Aktivitet_ i [dashboardet](https://app.blokada.org/stats?src=guides). Denne datamaskinens oppslag vises der.

<div class="note aside">

Vil du ha et VPN på denne datamaskinen også? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) inkluderer en WireGuard-oppsett som krypterer all trafikk, med samme blokkering.

</div>
