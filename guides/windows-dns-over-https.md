---
title: Block ads on Windows with DNS over HTTPS
description: Use the encrypted DNS built into Windows 11 with Blokada Cloud to block ads and trackers in every app and browser, with no software to install.
updated: 2026-09-28
order: 8
---

Windows 11 can send all its DNS lookups encrypted, over DNS over HTTPS. Point it at Blokada Cloud, and ads and trackers are blocked in every app and browser on the computer, with nothing to install.

You need two values:

- DNS server (IP address): {% ip "doh" %}
- Your DoH link: {% doh %}

## Windows 11

1. Open *Settings → Network & internet*, then *Wi-Fi* or *Ethernet*, depending on how the computer is connected.
2. Open your connection's *Hardware properties*. For Wi-Fi, select *Manage known networks* and then the network, or *Hardware properties* at the top of the Wi-Fi page.
3. Next to *DNS server assignment*, select *Edit*. Choose *Manual* and turn on *IPv4*.
4. In *Preferred DNS*, enter the DNS server {% ip "doh" %}
5. Set *DNS over HTTPS* to *On (manual template)*, and paste your DoH link {% doh %} as the *DoH template*.
6. Turn *Fallback to plaintext* off, and select *Save*.

If the computer uses both Wi-Fi and Ethernet, repeat this for the other connection.

<div class="note">

Leave *Alternate DNS* empty. Windows uses both servers, and any other one lets ads through.

No *On (manual template)* option? Your Windows 11 is older. Update Windows, or use the [browser guide](../browser-dns-over-https/) meanwhile.

If some ads still get through on a network with IPv6, Windows may also be asking your router's IPv6 DNS server. Turn off *Internet Protocol Version 6 (TCP/IPv6)* in the adapter's properties (*Control Panel → Network Connections*), or set up your [router](../router-ad-blocking/).

</div>

## Windows 10

Windows 10 has no built-in encrypted DNS. Set up secure DNS in your browser instead, as in the [browser guide](../browser-dns-over-https/), or set up your [router](../router-ad-blocking/) to cover the whole home.

## Check that it works

Open a few websites, then look at the *Activity* page in the [dashboard](https://app.blokada.org/stats?src=guides). This computer's lookups show up there.

Browsers with their own *secure DNS* setting bypass Windows. In Chrome and Edge, set it to use the current service provider, or to your DoH link.

<div class="note">

Want a VPN on this computer too? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) includes a WireGuard setup that encrypts all traffic, with the same blocking.

</div>
