---
title: Mullvad DNS is shutting down. Keep your ad blocking with Blokada Cloud
description: Mullvad closes its public DNS on 2 November 2026. Here is how to move your phone, computer and router to Blokada Cloud before then, without losing ad blocking.
updated: 2026-09-23
order: 2
---

Mullvad is closing its free public DNS service on **2 November 2026** and recommends Quad9 instead. Quad9 blocks malware but does **not** block ads or trackers. If you used one of Mullvad's filtering DNS names, ads come back on that date unless you switch.

This page is about the public DNS names ending in `dns.mullvad.net`. It does not cover the Mullvad VPN app.

## What you used, and what to pick in Blokada

| Mullvad DNS name | What it blocked | In the Blokada dashboard |
|---|---|---|
| `dns.mullvad.net` | nothing | Blokada is a filtering service. If you want no filtering, Quad9 or your provider's DNS is the simpler choice. |
| `adblock.dns.mullvad.net` | ads, trackers | an ad and tracker blocklist |
| `base.dns.mullvad.net` | ads, trackers, malware | add a malware list |
| `extended.dns.mullvad.net` | base plus social media | add a social media list |
| `family.dns.mullvad.net` | base plus adult content and gambling | add adult content and gambling lists |
| `all.dns.mullvad.net` | all of the above | turn on all of them |

You choose blocklists in the dashboard under *Blocklists*. You can change them at any time, and the change applies to all your devices.

## Your Blokada details

Blokada gives each device its own name, so the dashboard can show activity per device:

- Your Blokada DNS name, for DNS over TLS (Android, routers): {% dot %}
- Your DoH link, for DNS over HTTPS (browsers, some routers): {% doh %}

## Switch each device

### Android

Mullvad's guide had you enter a hostname under *Private DNS*. Replace it with your Blokada DNS name. The [Android guide](../android-private-dns/) has the steps.

### iPhone, iPad and Mac

Mullvad's setup used a configuration profile. Remove it first:

- **iPhone and iPad:** *Settings → General → VPN & Device Management*, tap the Mullvad DNS profile, then *Remove Profile*.
- **Mac:** open the list of profiles (*System Settings → General → Device Management* on macOS 15 and later, *System Settings → Privacy & Security → Profiles* on macOS 13 and 14, *System Preferences → Profiles* on macOS 12 and earlier), select the Mullvad DNS profile and click *−*.

Then install the Blokada profile from the [Apple guide](../apple-devices/).

### Browsers

If you entered a Mullvad DoH link such as `https://adblock.dns.mullvad.net/dns-query` under *secure DNS* or *DNS over HTTPS*, replace it with your DoH link. The [browser guide](../browser-dns-over-https/) has the steps for each browser.

### Router

If your router uses Mullvad over DNS over TLS, replace the Mullvad hostname with your Blokada DNS name, and remove Mullvad's IP addresses. The [router guide](../router-ad-blocking/) covers common models.

## Check that it works

Open a few websites, then look at the *Activity* page in the dashboard. You see your devices' lookups there, with blocked ones marked. If a device doesn't show up, it is still using another DNS server.
