---
title: Block ads on Windows with DNS over HTTPS
description: Use the encrypted DNS built into Windows 11 with Blokada Cloud to block ads and trackers in every app and browser, with no software to install.
updated: 2026-10-02
order: 8
---

Windows 11 can send all its DNS lookups encrypted, over DNS over HTTPS. Point it at Blokada Cloud, and ads and trackers are blocked in every app and browser on the computer, with nothing to install.

Вам понадобятся IP-адрес DNS-сервера и ваша DoH-ссылка, оба параметра находятся выше в разделе _Ваши данные_.

## Windows 11

1. Open _Settings → Network & internet_, then _Wi-Fi_ or _Ethernet_, depending on how the computer is connected.
2. Open your connection's _Hardware properties_. For Wi-Fi, select _Manage known networks_ and then the network, or _Hardware properties_ at the top of the Wi-Fi page.
3. Next to _DNS server assignment_, select _Edit_. Choose _Manual_ and turn on _IPv4_.
4. In _Preferred DNS_, enter the DNS server {% ip "doh" %}
5. Set _DNS over HTTPS_ to _On (manual template)_, and paste your DoH link {% doh %} as the _DoH template_.
6. Turn _Fallback to plaintext_ off, and select _Save_.

If the computer uses both Wi-Fi and Ethernet, repeat this for the other connection.

<div class="note important">

Leave _Alternate DNS_ empty. Windows uses both servers, and any other one lets ads through.

</div>

<div class="note tip">

No _On (manual template)_ option? Your Windows 11 is older. Update Windows, or use the [browser guide](../browser-dns-over-https/) meanwhile.

</div>

## Windows 10

Windows 10 has no built-in encrypted DNS. Set up secure DNS in your browser instead, as in the [browser guide](../browser-dns-over-https/), or set up your [router](../router-ad-blocking/) to cover the whole home.

## Check that it works

Open a few websites, then look at the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). This computer's lookups show up there.

<div class="note aside">

Want a VPN on this computer too? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) includes a WireGuard setup that encrypts all traffic, with the same blocking.

</div>

## Если что-то не работает

Chrome and Edge have their own _secure DNS_ setting, which bypasses Windows. Left on automatic, it can fall back to plain DNS, which Blokada refuses. Set it to your DoH link instead:

- **Chrome:** open `chrome://settings/security`, turn on _Use secure DNS_, and under _Select DNS provider_ choose _Add custom DNS service provider_.
- **Edge:** open `edge://settings/privacy`, turn on secure DNS, and choose _Choose a service provider_.

Then paste your DoH link {% doh %}

If some ads still get through on a network with IPv6, Windows may also be asking your router's IPv6 DNS server. Turn off _Internet Protocol Version 6 (TCP/IPv6)_ in the adapter's properties (_Control Panel → Network Connections_), or set up your [router](../router-ad-blocking/).
