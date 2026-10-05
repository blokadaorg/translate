---
title: Блокиране на рекламите в Linux чрез DNS през TLS
description: Настройтка на systemd-resolved да използва Blokada Cloud чрез криптиран DNS over TLS и блокирайте реклами и тракери за всяко приложение на вашия Linux компютър.
updated: 2026-10-02
order: 9
---

Most current Linux distributions, including Ubuntu and Fedora, resolve names through _systemd-resolved_, which supports DNS over TLS. On Debian, install it first with `sudo apt install systemd-resolved`. Point it at Blokada Cloud, and ads and trackers are blocked for every app on the computer.

## Настройване на systemd-resolved

1. Създайте папката с команда `sudo mkdir -p /etc/systemd/resolved.conf.d`, след това файла `/etc/systemd/resolved.conf.d/blokada.conf` със следните настройки:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Рестартирайте го: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Проверка: <code>resolvectl status</code> показва <code>+DNSOverTLS</code> и сървъра на Blokada.</li>
</ol>

Частта след `#` е вашето име на Blokada DNS: {% dot %} systemd-resolved проверява сертификата на сървъра спрямо него, а Blokada го използва, за да разбере кое устройство прави заявката.

<div class="note important">

**NetworkManager** also passes on the DNS servers of your network. `Domains=~.` sends all lookups to Blokada, but if `resolvectl status` still lists another server on a connection, turn off automatic DNS for that connection (the _Automatic_ switch next to _DNS_ in its IPv4 and IPv6 settings).

</div>

## Без systemd-resolved

If `resolvectl` isn't found, your distribution resolves names another way. Set up secure DNS in your browser instead, as in the [browser guide](../browser-dns-over-https/), or set up your [router](../router-ad-blocking/) to cover the whole home.

## Проверка дали работи

Open a few websites, then look at the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). This computer's lookups show up there.

<div class="note aside">

Want a VPN on this computer too? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) includes a WireGuard setup that encrypts all traffic, with the same blocking.

</div>
