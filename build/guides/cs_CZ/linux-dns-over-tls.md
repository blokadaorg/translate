---
title: Blokujte reklamy na Linuxu pomocí DNS přes TLS
description: Nastavte systemd-resolved pro použití Blokada Cloud přes šifrovaný DNS přes TLS a blokujte reklamy a trackery pro každou aplikaci na vašem počítači s Linuxem.
updated: 2026-10-02
order: 9
---

Většina současných distribucí Linuxu, včetně Ubuntu a Fedory, řeší názvy prostřednictvím _systemd-resolved_, který podporuje DNS přes TLS. Na Debianu jej nejdříve nainstalujte příkazem `sudo apt install systemd-resolved`. Nasměrujte jej na Blokada Cloud a reklamy i trackery budou blokovány pro každou aplikaci v počítači.

## Nastavení systemd-resolved

1. Vytvořte složku příkazem `sudo mkdir -p /etc/systemd/resolved.conf.d`, poté soubor `/etc/systemd/resolved.conf.d/blokada.conf` s těmito nastaveními:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Restartujte službu: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Zkontrolujte: <code>resolvectl status</code> zobrazí <code>+DNSOverTLS</code> a Blokada server.</li>
</ol>

Část za znakem `#` je váš Blokada DNS název: {% dot %} systemd-resolved ověřuje certifikát serveru podle něj a Blokada jej používá ke zjištění, které zařízení se ptá.

<div class="note important">

**NetworkManager** také předává DNS servery vaší sítě. `Domains=~.` posílá všechny dotazy na Blokada, ale pokud `resolvectl status` stále zobrazuje jiný server u připojení, vypněte automatické DNS pro toto připojení (přepínač _Automaticky_ vedle _DNS_ v jeho nastavení IPv4 a IPv6).

</div>

## Bez systemd-resolved

Pokud `resolvectl` nebyl nalezen, vaše distribuce řeší názvy jiným způsobem. Nastavte bezpečné DNS ve svém prohlížeči podle [průvodce nastavením prohlížeče](../browser-dns-over-https/) nebo nastavte [router](../router-ad-blocking/), abyste pokryli celou domácnost.

## Ověřte, že to funguje

Otevřete několik webových stránek, poté se podívejte na stránku _Aktivita_ v [dashboardu](https://app.blokada.org/stats?src=guides). Dotazy z tohoto počítače se tam zobrazí.

<div class="note aside">

Chcete na tomto počítači také VPN? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) obsahuje nastavení WireGuard, které šifruje veškerý provoz se stejným blokováním.

</div>
