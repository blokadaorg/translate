---
title: Blokker annonser på Linux med DNS over TLS
description: Konfigurer systemd-resolved til å bruke Blokada Cloud over kryptert DNS over TLS, og blokker annonser og sporingsmekanismer for alle apper på Linux-maskinen din.
updated: 2026-09-28
order: 9
---

De fleste moderne Linux-distribusjoner, inkludert Ubuntu og Fedora, slår opp navn gjennom <em>systemd-resolved</em>, som støtter DNS over TLS. På Debian, installer det først med <code>sudo apt install systemd-resolved</code>. Pek den mot Blokada Cloud, så blir annonser og sporingsmekanismer blokkert for alle apper på datamaskinen.

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

<div class="note">

<strong>NetworkManager</strong> videreformidler også DNS-serverne til nettverket ditt. <code>Domains=~.</code> sender alle oppslag til Blokada, men hvis <code>resolvectl status</code> fortsatt viser en annen server på en tilkobling, slå av automatisk DNS for den tilkoblingen (bryteren <em>Automatisk</em> ved siden av <em>DNS</em> i dens IPv4- og IPv6-innstillinger).

</div>

## Uten systemd-resolved

Hvis <code>resolvectl</code> ikke finnes, slår distribusjonen din opp navn på en annen måte. Konfigurer sikker DNS i nettleseren din i stedet, som vist i <a href="../browser-dns-over-https/">nettleserguiden</a>, eller konfigurer <a href="../router-ad-blocking/">ruteren</a> for å dekke hele hjemmet.

## Sjekk at det virker

Åpne noen nettsider og se deretter på siden <em>Aktivitet</em> i <a href="https://app.blokada.org/stats?src=guides">dashbordet</a>. Denne datamaskinens oppslag vises der.

<div class="note">

Vil du ha VPN på denne datamaskinen også? <a href="https://app.blokada.org/activate?tier=plus&amp;src=guides">Blokada Plus</a> inkluderer en WireGuard-oppsett som krypterer all trafikk, med samme blokkering.

</div>
