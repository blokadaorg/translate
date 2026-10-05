---
title: Блокиране на реклами на Mac и Apple TV с профил Blokada DNS
description: Инсталиране на профил на Blokada Cloud DNS, за да блокирате реклами и тракери на системно ниво на Mac или Apple TV с криптиран DNS, без нищо да работи във фонов режим.
updated: 2026-10-02
order: 6
---

Apple devices can use encrypted DNS for the whole system through a configuration profile. The Blokada profile points the device at Blokada Cloud, which blocks ads and trackers in every app and browser.

Работи на macOS 11 (Big Sur), tvOS 14, iOS и iPadOS 14 и по-нови версии.

<div class="if-no-device">

This page doesn't know your device yet, so it can't offer your profile. Sign in to the dashboard, open _Setup_, choose your device, and open this guide with _Open on another device_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Вземи линка за моя профил</a></p>

</div>

## iPhone и iPad

The easiest way is the app. [Blokada 6](https://go.blokada.org/appstore) sets everything up for you, turns blocking on and off in one tap, and shows what was blocked on the phone itself. Sign in with your account ID and you're done.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Вземете Blokada 6 от App Store</a></p>

### Без приложението

You can install the profile instead. iPhone and iPad install profiles from **Safari** only.

<div class="if-device">
<div class="if-other-browser note important">

This page is open in another browser. Copy your link and open it in Safari to continue there: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. В Safari натиснете върху бутона по-долу, после изберете _Разреши_, за да изтеглите профила.
2. Open _Settings_. Tap _Profile Downloaded_ near the top. You can also find it under _General → VPN & Device Management_.
3. Докоснете _Инсталиране_, въведете вашия код за достъп и потвърдете.

</div>

<p class="if-device if-safari">{% appleProfile %}Изтегли моят профил{% endappleProfile %}</p>

## Mac

1. Кликнете върху бутона по-долу, за да изтеглите профила.
2. Отворете списъка с профили: _Системни настройки → Общи → Управление на устройства_ в macOS 15 и по-нови, _Системни настройки → Поверителност и сигурност → Профили_ в macOS 13 и 14, или _Системни предпочитания → Профили_ в macOS 12 и по-стари.
3. Щракнете двукратно върху профила на Blokada и изберете _Инсталиране_.

<p class="if-device">{% appleProfile %}Изтегляне на моя профил{% endappleProfile %}</p>

## Apple TV

Apple TV не може да отваря уеб страници, затова въвеждате вашия линк към профила в него.

1. Вашият линк към профила: {% appleUrl %}
2. На Apple TV отворете _Настройки → Общи → Поверителност и сигурност_.
3. Highlight _Share Apple TV Analytics_. Don't select it. Press the Play/Pause button on the remote instead.
4. Choose _Add Profile_ and enter your profile link. Typing is easiest with the keyboard prompt on your iPhone, where you can paste it. Install the profile and confirm.

<div class="note aside">

**Apple TV и други устройства у дома:** ако настроите Blokada Cloud на вашия [рутер](../router-ad-blocking/), Apple TV ще бъде защитен заедно с всички останали устройства.

</div>

## Проверка дали работи

Browse for a minute, then open the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). This device's lookups show up there.

За да премахнете Blokada по-късно, изтрийте профила, от там където сте го инсталирали.
