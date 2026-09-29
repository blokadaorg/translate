---
title: Block ads in Chrome, Firefox, Edge and Brave with DNS over HTTPS
description: Set Blokada Cloud as the secure DNS provider in your browser to block ads and trackers, on any computer, including work laptops where you can't install apps.
updated: 2026-09-23
order: 7
---

Modern browsers can use their own encrypted DNS provider, called *secure DNS* or *DNS over HTTPS*. Set it to Blokada Cloud, and the browser blocks ads and trackers on any network, with no extension to install.

This setting covers only this browser. To cover the whole computer, use the [Apple profile](../apple-devices/) on a Mac, or set up your [router](../router-ad-blocking/).

Your DoH link: {% doh %}

## Chrome

1. Open `chrome://settings/security`.
2. Turn on *Use secure DNS*, then choose *Add custom DNS service provider*.
3. Enter {% doh %}

## Edge

1. Open `edge://settings/privacy`.
2. Under *Security*, turn on *Use secure DNS to specify how to look up the network address for websites*.
3. Choose *Choose a service provider* and enter {% doh %}

## Firefox

1. Open *Settings → Privacy & Security* and scroll to *DNS over HTTPS*.
2. Choose *Max Protection*.
3. Under *Choose provider*, select *Custom* and enter {% doh %}

## Brave

1. Open `brave://settings/security`.
2. Turn on *Use secure DNS*, then choose *Add custom DNS service provider*.
3. Enter {% doh %}

## Safari

Safari has no secure DNS setting of its own. It uses the system's DNS, so install the [Apple profile](../apple-devices/).

## Check that it works

Browse for a minute, then open the *Activity* page in the [dashboard](https://app.blokada.org/stats?src=guides). This browser's lookups show up there.

<div class="note">

If your browser is managed by work or school, the secure DNS setting may be locked. Ask your administrator.

</div>
