---
title: Block ads on Linux with DNS over TLS
description: Set up systemd-resolved to use Blokada Cloud over encrypted DNS over TLS, and block ads and trackers for every app on your Linux computer.
updated: 2026-09-28
order: 9
---

Most current Linux distributions, including Ubuntu and Fedora, resolve names through *systemd-resolved*, which supports DNS over TLS. On Debian, install it first with `sudo apt install systemd-resolved`. Point it at Blokada Cloud, and ads and trackers are blocked for every app on the computer.

## Set up systemd-resolved

1. Create the folder with `sudo mkdir -p /etc/systemd/resolved.conf.d`, then the file `/etc/systemd/resolved.conf.d/blokada.conf` with these settings:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Restart it: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Check it: <code>resolvectl status</code> shows <code>+DNSOverTLS</code> and the Blokada server.</li>
</ol>

The part after `#` is your Blokada DNS name: {% dot %} systemd-resolved checks the server's certificate against it, and Blokada uses it to know which device is asking.

<div class="note">

**NetworkManager** also passes on the DNS servers of your network. `Domains=~.` sends all lookups to Blokada, but if `resolvectl status` still lists another server on a connection, turn off automatic DNS for that connection (the *Automatic* switch next to *DNS* in its IPv4 and IPv6 settings).

</div>

## Without systemd-resolved

If `resolvectl` isn't found, your distribution resolves names another way. Set up secure DNS in your browser instead, as in the [browser guide](../browser-dns-over-https/), or set up your [router](../router-ad-blocking/) to cover the whole home.

## Check that it works

Open a few websites, then look at the *Activity* page in the [dashboard](https://app.blokada.org/stats?src=guides). This computer's lookups show up there.

<div class="note">

Want a VPN on this computer too? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) includes a WireGuard setup that encrypts all traffic, with the same blocking.

</div>
