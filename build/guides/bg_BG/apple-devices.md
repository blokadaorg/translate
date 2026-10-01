---
title: Block ads on Mac and Apple TV with a Blokada DNS profile
description: Install a Blokada Cloud DNS profile to block ads and trackers system-wide on a Mac or Apple TV, with encrypted DNS and nothing running in the background.
updated: 2026-09-28
order: 6
---

Устройствата на Apple могат да използват криптиран DNS за цялата система чрез конфигурационен профил. Blokada профила насочва устройството към Blokada Cloud, който блокира реклами и тракери във всяко приложение и браузър.

It works on macOS 11 (Big Sur), tvOS 14, iOS and iPadOS 14 and later.

<div class="if-no-device">

Страницата все още не разпознава вашето устройство, затова не може да ви предложи профил. Влезте в таблото, отворете _Настройка_, изберете вашето устройство и отворете това ръководство с _Отвори на друго устройство_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Get my profile link</a></p>

</div>

## iPhone and iPad

Най-лесният начин е приложението. [Blokada 6](https://go.blokada.org/appstore) настройва всичко вместо вас, включва и изключва блокирането с едно докосване и показва какво е блокирано директно на телефона. Влезте с вашия Акаунт ID и сте готови.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Get Blokada 6 on the App Store</a></p>

### Without the app

Можете да инсталирате профила. На iPhone и iPad инсталирането на профил е възможно само чрез **Safari**.

<div class="if-device">
<div class="if-other-browser note">

Страницата е отворена в друг браузър. Копирайте вашия линк и го отворете в Safari, за да продължите там: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Отворете _Настройки_. Докоснете _Изтеглен профил_ близо до горната част. Може да го намерите и под _Общи → VPN и управление на устройства_.
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
3. Highlight _Share Apple TV Analytics_. Не го избирайте. Вместо това натиснете бутона Play/Pause на дистанционното.
4. Изберете _Добавяне на профил_ и въведете вашия линк към профила. Най-лесно е да го въведете от клавиатурния прозорец на вашия iPhone, където можете да го поставите. Инсталирайте профила и потвърдете.

<div class="note">

**Apple TV and other devices at home:** if you set up Blokada Cloud on your [router](../router-ad-blocking/), the Apple TV is covered along with everything else.

</div>

## Check that it works

Сърфирайте за минута, след това отворете страницата _Дейност_ в [таблото за управление](https://app.blokada.org/stats?src=guides). Запитванията от това устройство ще се показват там.

To remove Blokada later, delete the profile where you installed it.
