---
title: A Pi-hole alternative that needs no hardware
description: Move your home's ad blocking from a Pi-hole to Blokada Cloud, or keep your Pi-hole and send its lookups through Blokada.
updated: 2026-09-23
order: 1
---

A Pi-hole blocks ads for every device on your network, as long as the Raspberry Pi is running, updated and at home. Blokada Cloud does the same job from our servers:

- **No box to maintain.** No SD cards, no updates, no outage when the Pi goes down.
- **It works away from home.** Phones and laptops keep their blocking on mobile data and other Wi-Fi networks.
- **Encrypted.** Devices talk to Blokada over DNS over TLS or DNS over HTTPS, so your provider cannot read or change your lookups.
- **One dashboard.** Blocklists, allowed and blocked domains, and activity per device, at [app.blokada.org](https://app.blokada.org/?src=guides).

There are two ways to switch. Replace the Pi-hole completely, or keep it and use Blokada Cloud as its upstream.

## Option 1: replace the Pi-hole

1. **Get Blokada Cloud** and open the dashboard. Under *Setup* you find your details:
   - Your Blokada DNS name, for DNS over TLS: {% dot %}
   - Your DoH link, for DNS over HTTPS: {% doh %}
2. **Point your router at Blokada instead of the Pi-hole.** Follow the [router guide](../router-ad-blocking/). If your router only accepts a plain IP address as DNS server, set up your devices one by one instead: [Android](../android-private-dns/), [Mac and Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), and [browsers](../browser-dns-over-https/).
3. **If your Pi-hole was the DHCP server,** turn DHCP back on in your router *before* you switch the Pi off. Otherwise your devices stop getting network addresses.
4. **Move your lists.** In the dashboard, choose blocklists under *Blocklists*, and add your own allowed or blocked domains under *Exceptions*.
5. **Switch the Pi-hole off,** or keep it for something else.

<div class="note">

Your Pi-hole showed every device on the network by its IP address. With Blokada each device shows up by its own name, as long as it uses its own Blokada DNS name. A router set up with one Blokada DNS name shows up as one device.

</div>

## Option 2: keep the Pi-hole, use Blokada Cloud upstream

If you want to keep your local setup, such as local host names, DHCP or your own lists, let the Pi-hole forward its lookups to Blokada over an encrypted connection. Pi-hole cannot do encrypted forwarding itself, so a small forwarder runs next to it. This guide uses [dnsproxy](https://github.com/AdguardTeam/dnsproxy), an open source forwarder that is a single file.

1. On the Pi-hole machine, download the `dnsproxy` release for your CPU (`linux-arm64` for a recent Raspberry Pi) from its releases page, and copy the `dnsproxy` binary to `/usr/local/bin/`.
2. Create `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Encrypted DNS forwarder to Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Start it: `sudo systemctl enable --now dnsproxy`
4. In the Pi-hole admin, open *Settings → DNS*. Untick every upstream server and add `127.0.0.1#5054` as a custom upstream server. Save.
5. Check the dashboard *Activity* page. Lookups from your network now show up there.

You can turn off the Pi-hole's own blocklists and manage blocking in the dashboard, or keep both.

## Frequently asked

**Do I need Blokada Plus?** No. Blokada Cloud covers DNS blocking for your whole home. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) adds a VPN on top.

**What if Blokada is unreachable?** Your devices cannot resolve names until it is back, just as when a Pi-hole goes down. Don't add a second, unfiltered DNS server as fallback. Most devices use all their servers at random, so ads would get through.
