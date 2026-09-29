---
title: A NextDNS alternative with the same setup on every device
description: Move from NextDNS to Blokada Cloud. Swap your NextDNS DNS name, DoH link or profile for Blokada's on your phone, computer and router, and keep your ad blocking.
updated: 2026-09-28
order: 3
---

NextDNS and Blokada Cloud work the same way: an encrypted DNS service that blocks ads and trackers by name, with your own settings behind a personal DNS name. Switching means replacing the NextDNS values on each device with your Blokada ones. Nothing else on the device changes.

## What you used, and what to pick in Blokada

| In NextDNS | In Blokada Cloud |
|---|---|
| Your configuration ID, e.g. `abc123` | Your device tag, part of your Blokada DNS name and DoH link |
| *Privacy* blocklists | *Blocklists* in the dashboard |
| *Security* (malware, phishing) | a malware list under *Blocklists* |
| *Parental control* | adult content and gambling lists under *Blocklists* |
| *Allowlist* and *Denylist* | *Exceptions* in the dashboard |
| *Logs* and *Analytics* | *Activity* and *Stats* in the dashboard |

## Your Blokada details

- Your Blokada DNS name, for DNS over TLS: {% dot %}
- Your DoH link, for DNS over HTTPS: {% doh %}

## Switch each device

### Android

If you used *Private DNS* with `<your-id>.dns.nextdns.io`, replace it with your Blokada DNS name, as in the [Android guide](../android-private-dns/). If you used the NextDNS app, uninstall it and install [Blokada 6](https://go.blokada.org/play_cloud) instead.

### iPhone and iPad

If you used the NextDNS app, uninstall it and install [Blokada 6](https://go.blokada.org/appstore). If you installed a NextDNS profile instead, remove it under *Settings → General → VPN & Device Management*, then follow the [Apple guide](../apple-devices/).

### Mac and Apple TV

Remove the NextDNS profile or app, then install the Blokada profile from the [Apple guide](../apple-devices/).

### Windows and Linux

Uninstall the NextDNS app if you use it. On Windows, replace the NextDNS server and DoH template with Blokada's, as in the [Windows guide](../windows-dns-over-https/). On Linux, replace the NextDNS server in systemd-resolved, as in the [Linux guide](../linux-dns-over-tls/).

### Browsers

If you set `https://dns.nextdns.io/…` as your browser's *secure DNS*, replace it with your DoH link, as in the [browser guide](../browser-dns-over-https/).

### Router

If your router uses NextDNS over DNS over TLS or DNS over HTTPS, replace the NextDNS name or link with your Blokada one, as in the [router guide](../router-ad-blocking/).

If it uses NextDNS through plain IP addresses with a *linked IP*, Blokada can't take that over yet. Support for routers with plain DNS addresses is on the way. Until then, set up your devices one by one, or use a router that supports encrypted DNS.

## Check that it works

Open a few websites, then look at the *Activity* page in the dashboard. You see your devices' lookups there, with blocked ones marked. If a device doesn't show up, it is still using NextDNS.
