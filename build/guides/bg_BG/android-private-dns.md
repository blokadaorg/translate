---
title: Настройка на частен DNS на Android с Blokada Cloud
description: Use Android's built-in Private DNS setting with Blokada Cloud to block ads and trackers in every app, on Wi-Fi and mobile data. Or let the Blokada 6 app do it.
updated: 2026-10-02
order: 5
---

## Най-лесният начин: приложението

[Blokada 6](https://go.blokada.org/play_cloud) sets everything up for you, turns blocking on and off in one tap, and shows what was blocked on the phone itself. Sign in with your account ID and you're done.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Вземете Blokada 6 от Google Play</a></p>

## Без приложението: Частен DNS

Android 9 and later has a _Private DNS_ setting. Set it to Blokada Cloud, and ads and trackers are blocked in all apps, on every network, with nothing running in the background.

1. Open _Settings → Network & internet_. On some phones this is _Connections_ or _Connection & sharing_.
2. Tap _Private DNS_. On Samsung phones it is under _More connection settings_.
3. Изберете _Име на хост на доставчик на частен DNS_.
4. Въведете вашето име на Blokada DNS {% dot %} и докоснете _Запазване_.

Ако не можете да го намерите, потърсете в приложението Настройки за "Частен DNS".

## Проверка дали работи

Open a few apps or websites, then look at the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). This phone's lookups show up there.

## Ако нещо не работи

- **"Couldn't connect" or no internet:** check your Blokada DNS name for typos. It must be exactly as shown above, without `https://`.
- **Another VPN app is active:** some VPN apps use their own DNS and bypass Private DNS. Turn the VPN's DNS or ad blocking setting off, or use Blokada 6 instead.
- **Chrome still shows ads:** Chrome may be set to its own secure DNS provider, which bypasses Private DNS. In Chrome, open _Settings → Privacy and security → Use secure DNS_ and choose _Use your current service provider_. Chrome then follows Private DNS.
