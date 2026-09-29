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

1. Open `http://fritz.box` and go to *Internet → Account Information → DNS Server*.
2. Under *Encrypted Name Resolution on the Internet (DNS over TLS)*, tick *Use encrypted name resolution*.
3. Tick *Enforce certificate verification for encrypted name resolution*.
4. Untick *Allow fallback to unencrypted name resolution*.
5. In *Resolver names*, enter only {% dot %}. **Remove every other entry.** The FRITZ!Box uses all listed resolvers, and any other one lets ads through.
6. Click *Apply*.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to *WAN → Internet Connection*.
2. Under *WAN DNS Setting*, set *DNS Privacy Protocol* to *DNS-over-TLS (DoT)* and *DNS-over-TLS Profile* to *Strict*.
3. Remove every entry from the *DNS-over-TLS Server List*, then add one:
   - Address: {% ip "dot" %}
   - TLS Hostname: {% dot %}
4. Click *Apply*.

## OpenWrt

1. In *System → Software*, update the lists and install `luci-app-https-dns-proxy`.
2. Open *Services → HTTPS DNS Proxy*. Delete the instances for other providers.
3. Add an instance with a custom resolver URL: {% doh %}
4. *Save & Apply*. The package points dnsmasq at it automatically.

## Other routers

Look for a setting called *DNS over TLS*, *Private DNS*, *Encrypted DNS* or *DNS over HTTPS*. Enter your Blokada DNS name or DoH link from above, and remove every other DNS server, including fallback servers.

## Check that it works

1. Restart one device, or turn its Wi-Fi off and on, so it picks up the change.
2. Browse for a minute, then open the *Activity* page in the dashboard. Your network's lookups show up there.

Some devices bypass the router: phones with *Private DNS* set, browsers with *secure DNS* set to another provider, and devices that hard-code their own DNS. Set those up on the device itself, or turn their own DNS setting off.

<div class="note">

Behind the router, all devices share one address, so the dashboard shows your network as a single device. Set up phones and laptops with their own Blokada DNS name if you want to see them separately. They also keep their blocking when they leave home.

</div>
