---
title: Set up Private DNS on Android with Blokada Cloud
description: Use Android's built-in Private DNS setting with Blokada Cloud to block ads and trackers in every app, on Wi-Fi and mobile data. Or let the Blokada 6 app do it.
updated: 2026-09-28
order: 5
---

## The easiest way: the app

[Blokada 6](https://go.blokada.org/play_cloud) sets everything up for you, turns blocking on and off in one tap, and shows what was blocked on the phone itself. Sign in with your account ID and you're done.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Get Blokada 6 on Google Play</a></p>

## Without the app: Private DNS

Android 9 and later has a *Private DNS* setting. Set it to Blokada Cloud, and ads and trackers are blocked in all apps, on every network, with nothing running in the background.

Your Blokada DNS name: {% dot %}

1. Open *Settings → Network & internet*. On some phones this is *Connections* or *Connection & sharing*.
2. Tap *Private DNS*. On Samsung phones it is under *More connection settings*.
3. Choose *Private DNS provider hostname*.
4. Enter your Blokada DNS name {% dot %} and tap *Save*.

If you can't find it, search the Settings app for "Private DNS".

## Check that it works

Open a few apps or websites, then look at the *Activity* page in the [dashboard](https://app.blokada.org/stats?src=guides). This phone's lookups show up there.

## If something doesn't work

- **"Couldn't connect" or no internet:** check your Blokada DNS name for typos. It must be exactly as shown above, without `https://`.
- **Another VPN app is active:** some VPN apps use their own DNS and bypass Private DNS. Turn the VPN's DNS or ad blocking setting off, or use Blokada 6 instead.
- **Chrome still shows ads:** in Chrome, open *Settings → Privacy and security → Use secure DNS* and choose *Use current service provider*.
