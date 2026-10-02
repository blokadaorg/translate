---
title: Block ads in Chrome, Firefox, Edge and Brave with DNS over HTTPS
description: Set Blokada Cloud as the secure DNS provider in your browser to block ads and trackers, on any computer, including work laptops where you can't install apps.
updated: 2026-10-02
order: 7
---

Modern browsers can use their own encrypted DNS provider, called _secure DNS_ or _DNS over HTTPS_. Set it to Blokada Cloud, and the browser blocks ads and trackers on any network, with no extension to install.

This setting covers only this browser. To cover the whole computer, use the [Apple profile](../apple-devices/) on a Mac, or set up your [router](../router-ad-blocking/).

## Chrome

1. Open `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Enter {% doh %}

## Edge

1. Open `edge://settings/privacy`.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. Open `brave://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Enter {% doh %}

## Safari

Safari has no secure DNS setting of its own. It uses the system's DNS, so install the [Apple profile](../apple-devices/).

## Check that it works

Browse for a minute, then open the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). This browser's lookups show up there.

## If something doesn't work

<div class="note tip">

If your browser is managed by work or school, the secure DNS setting may be locked. Ask your administrator.

</div>
