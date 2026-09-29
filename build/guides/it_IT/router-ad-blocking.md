---
title: Block ads on your whole network with router ad blocking
description: Set up Blokada Cloud on your router once, and every device at home is covered, including TVs, game consoles and smart speakers that cannot run an ad blocker.
updated: 2026-09-23
order: 4
---

Every device on your network asks the router which DNS server to use. Point the router at Blokada Cloud, and ads and trackers are blocked for everything behind it. That includes smart TVs, game consoles, streaming sticks and smart home devices, which have no room for an ad blocker app.

## What your router needs

Your router must support **encrypted DNS with a host name**, that is DNS over TLS (DoT) or DNS over HTTPS (DoH). Many recent routers do, including the models below. Depending on which your router supports, you need:

- For DNS over TLS, your Blokada DNS name: {% dot %}
- For DNS over HTTPS, your DoH link: {% doh %}

<div class="note">

**Only plain IP addresses?** Many internet provider routers only accept plain IP addresses for DNS. Support for those is on the way. Until then, set up your devices one at a time: [Android](../android-private-dns/), [Mac and Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), and [browsers](../browser-dns-over-https/). You can also run a small forwarder on a Raspberry Pi, as described in the [Pi-hole guide](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 or later.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. Tick _Enforce certificate verification for encrypted name resolution_.
4. Untick _Allow fallback to unencrypted name resolution_.
5. In _Resolver names_, enter only {% dot %}. **Remove every other entry.** The FRITZ!Box uses all listed resolvers, and any other one lets ads through.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Address: {% ip "dot" %}
   - TLS Hostname: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Open _Services → HTTPS DNS Proxy_. Delete the instances for other providers.
3. Add an instance with a custom resolver URL: {% doh %}
4. _Save & Apply_. The package points dnsmasq at it automatically.

## Other routers

Look for a setting called _DNS over TLS_, _Private DNS_, _Encrypted DNS_ or _DNS over HTTPS_. Enter your Blokada DNS name or DoH link from above, and remove every other DNS server, including fallback servers.

## Check that it works

1. Restart one device, or turn its Wi-Fi off and on, so it picks up the change.
2. Browse for a minute, then open the _Activity_ page in the dashboard. Your network's lookups show up there.

Some devices bypass the router: phones with _Private DNS_ set, browsers with _secure DNS_ set to another provider, and devices that hard-code their own DNS. Set those up on the device itself, or turn their own DNS setting off.

<div class="note">

Behind the router, all devices share one address, so the dashboard shows your network as a single device. Set up phones and laptops with their own Blokada DNS name if you want to see them separately. They also keep their blocking when they leave home.

</div>
