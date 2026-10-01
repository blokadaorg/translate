---
title: Блокиране на реклами на Mac и Apple TV с профил Blokada DNS
description: Инсталиране на профил на Blokada Cloud DNS, за да блокирате реклами и тракери на системно ниво на Mac или Apple TV с криптиран DNS, без нищо да работи във фонов режим.
updated: 2026-09-28
order: 6
---

Устройствата на Apple могат да използват криптиран DNS за цялата система чрез конфигурационен профил. Blokada профила насочва устройството към Blokada Cloud, който блокира реклами и тракери във всяко приложение и браузър.

Работи на macOS 11 (Big Sur), tvOS 14, iOS и iPadOS 14 и по-нови версии.

<div class="if-no-device">

Страницата все още не разпознава вашето устройство, затова не може да ви предложи профил. Влезте в таблото, отворете _Настройка_, изберете вашето устройство и отворете това ръководство с _Отвори на друго устройство_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Вземи линка за моя профил</a></p>

</div>

## iPhone и iPad

Най-лесният начин е приложението. [Blokada 6](https://go.blokada.org/appstore) настройва всичко вместо вас, включва и изключва блокирането с едно докосване и показва какво е блокирано директно на телефона. Влезте с вашия Акаунт ID и сте готови.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Вземете Blokada 6 от App Store</a></p>

### Без приложението

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

<p class="if-device if-safari">{% appleProfile %}Изтегли моя профил{% endappleProfile %}</p>

## Mac

1. Кликнете върху бутона по-долу, за да изтеглите профила.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Изтегляне на моя профил{% endappleProfile %}</p>

## Apple TV

Apple TV не може да отваря уеб страници, затова въвеждате вашия линк към профила в него.

1. Вашият линк към профила: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. Highlight _Share Apple TV Analytics_. Не го избирайте. Вместо това натиснете бутона Play/Pause на дистанционното.
4. Изберете _Добавяне на профил_ и въведете вашия линк към профила. Най-лесно е да го въведете от клавиатурния прозорец на вашия iPhone, където можете да го поставите. Инсталирайте профила и потвърдете.

<div class="note">

**Apple TV и други устройства у дома:** ако настроите Blokada Cloud на вашия [рутер](../router-ad-blocking/), Apple TV ще бъде защитен заедно с всички останали устройства.

</div>

## Проверка дали работи

Сърфирайте за минута, след това отворете страницата _Дейност_ в [таблото за управление](https://app.blokada.org/stats?src=guides). Запитванията от това устройство ще се показват там.

За да премахнете Blokada по-късно, изтрийте профила, от там където сте го инсталирали.
