---
title: Blocca le pubblicità su Linux con DNS over TLS
description: Configura systemd-resolved per utilizzare Blokada Cloud tramite DNS su TLS crittografato, e blocca pubblicità e tracker per ogni app sul tuo computer Linux.
updated: 02/10/2026
order: 9
---

La maggior parte delle distribuzioni Linux attuali, inclusi Ubuntu e Fedora, risolvono i nomi tramite _systemd-resolved_, che supporta DNS over TLS. Su Debian, installalo prima con `sudo apt install systemd-resolved`. Configuralo per utilizzare Blokada Cloud, e annunci e tracker saranno bloccati per ogni app sul computer.

## Configura systemd-resolved

1. Crea la cartella con `sudo mkdir -p /etc/systemd/resolved.conf.d`, quindi il file `/etc/systemd/resolved.conf.d/blokada.conf` con queste impostazioni:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Riavvialo: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Verifica: <code>resolvectl status</code> mostra <code>+DNSOverTLS</code> e il server Blokada.</li>
</ol>

La parte dopo `#` è il tuo nome DNS Blokada: {% dot %} systemd-resolved controlla il certificato del server rispetto a questo, e Blokada lo usa per sapere quale dispositivo sta effettuando la richiesta.

<div class="note important">

**NetworkManager** inoltra anche i server DNS della tua rete. `Domains=~.` invia tutte le richieste a Blokada, ma se `resolvectl status` mostra ancora un altro server su una connessione, disattiva il DNS automatico per quella connessione (l'interruttore _Automatico_ accanto a _DNS_ nelle sue impostazioni IPv4 e IPv6).

</div>

## Senza systemd-resolved

Se `resolvectl` non viene trovato, la tua distribuzione risolve i nomi in un altro modo. Configura DNS sicuro nel tuo browser, come indicato nella [guida per browser](../browser-dns-over-https/), oppure configura il tuo [router](../router-ad-blocking/) per proteggere tutta la casa.

## Verifica che funzioni

Apri alcuni siti web e poi guarda la pagina _Attività_ nella [dashboard](https://app.blokada.org/stats?src=guides). Le risoluzioni di nomi di questo computer saranno visibili lì.

<div class="note aside">

Vuoi anche una VPN su questo computer? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) include una configurazione WireGuard che cripta tutto il traffico, offrendo lo stesso blocco.

</div>
