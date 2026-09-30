---
title: Block ads on Mac and Apple TV with a Blokada DNS profile
description: Install a Blokada Cloud DNS profile to block ads and trackers system-wide on a Mac or Apple TV, with encrypted DNS and nothing running in the background.
updated: 2026-09-28
order: 6
---

Apple devices can use encrypted DNS for the whole system through a configuration profile. The Blokada profile points the device at Blokada Cloud, which blocks ads and trackers in every app and browser.

It works on macOS 11 (Big Sur), tvOS 14, iOS and iPadOS 14 and later.

<div class="if-no-device">

This page doesn't know your device yet, so it can't offer your profile. Sign in to the dashboard, open _Setup_, choose your device, and open this guide with _Open on another device_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Get my profile link</a></p>

</div>

## iPhone and iPad

The easiest way is the app. [Blokada 6](https://go.blokada.org/appstore) sets everything up for you, turns blocking on and off in one tap, and shows what was blocked on the phone itself. Sign in with your account ID and you're done.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Get Blokada 6 on the App Store</a></p>

### Without the app

You can install the profile instead. iPhone and iPad install profiles from **Safari** only.

<div class="if-device">
<div class="if-other-browser note">

This page is open in another browser. Copy your link and open it in Safari to continue there: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Open _Settings_. Tap _Profile Downloaded_ near the top. You can also find it under _General → VPN & Device Management_.
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}Download my profile{% endappleProfile %}</p>

## Mac

1. Click the button below to download the profile.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Download my profile{% endappleProfile %}</p>

## Apple TV

The Apple TV cannot open web pages, so you type your profile link into it.

1. Your profile link: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. Highlight _Send to Apple_ (called _Share Apple TV Analytics_ on older tvOS). Don't select it. Press the Play/Pause button on the remote instead.
4. Choose _Add Profile_ and enter your profile link. Typing is easiest with the keyboard prompt on your iPhone, where you can paste it. Install the profile and confirm.

<div class="note">

**Apple TV and other devices at home:** if you set up Blokada Cloud on your [router](../router-ad-blocking/), the Apple TV is covered along with everything else.

</div>

## Check that it works

Browse for a minute, then open the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). This device's lookups show up there.

To remove Blokada later, delete the profile where you installed it.
