---
title: Блокируйте рекламу на Mac и Apple TV с помощью профиля Blokada DNS
description: Установите профиль Blokada Cloud DNS, чтобы заблокировать рекламу и трекеры на уровне всей системы на Mac или Apple TV с помощью зашифрованного DNS и без фоновых процессов.
updated: 2026-10-02
order: 6
---

Apple-устройства могут использовать зашифрованный DNS для всей системы через конфигурационный профиль. Профиль Blokada направляет устройство на Blokada Cloud, который блокирует рекламу и трекеры во всех приложениях и браузерах.

Работает на macOS 11 (Big Sur), tvOS 14, iOS и iPadOS 14 и новее.

<div class="if-no-device">

На этой странице ваше устройство пока не определено, поэтому профиль недоступен. Войдите в панель управления, откройте _Настройку_, выберите своё устройство и откройте это руководство через _Открыть на другом устройстве_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Получить ссылку на профиль</a></p>

</div>

## iPhone и iPad

Самый простой способ — это приложение. [Blokada 6](https://go.blokada.org/appstore) всё настраивает за вас, позволяет включать и выключать блокировку одним нажатием и показывает, что было заблокировано прямо на телефоне. Войдите под своим ID аккаунта — и готово.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Скачать Blokada 6 в App Store</a></p>

### Без приложения

Вы также можете просто установить профиль. На iPhone и iPad профили устанавливаются только через **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Эта страница открыта в другом браузере. Скопируйте вашу ссылку и откройте её в Safari, чтобы продолжить: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Откройте _Настройки_. Нажмите _Загруженный профиль_ вверху. Также его можно найти в _Основные → VPN и управление устройством_.
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}Скачать мой профиль{% endappleProfile %}</p>

## Mac

1. Нажмите на кнопку ниже, чтобы скачать профиль.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Скачать мой профиль{% endappleProfile %}</p>

## Apple TV

Apple TV не может открывать веб-страницы, поэтому вам нужно ввести ссылку на свой профиль вручную.

1. Ваша ссылка на профиль: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. Выделите _Передавать аналитику Apple TV_. Не выбирайте её. Нажмите кнопку Воспроизвести/Пауза на пульте.
4. Выберите _Добавить профиль_ и введите ссылку на профиль. Проще всего печатать с помощью клавиатуры на iPhone, куда можно просто вставить. Установите профиль и подтвердите.

<div class="note aside">

**Apple TV и другие устройства дома:** если вы настроите Blokada Cloud на своем [роутере](../router-ad-blocking/), то Apple TV и все остальные устройства тоже будут защищены.

</div>

## Проверьте, что всё работает

Пользуйтесь устройством минуту, затем откройте страницу _Активность_ в [панели управления](https://app.blokada.org/stats?src=guides). Запросы этого устройства отобразятся там.

Чтобы удалить Blokada позже, удалите профиль там, где вы его устанавливали.
