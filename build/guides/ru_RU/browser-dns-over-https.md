---
title: Блокируйте рекламу в Chrome, Firefox, Edge и Brave с помощью DNS через HTTPS
description: Установите Blokada Cloud в качестве защищённого DNS-провайдера в вашем браузере, чтобы блокировать рекламу и трекеры на любом компьютере, включая рабочие ноутбуки, где нельзя установить приложения.
updated: 2026-10-02
order: 7
---

Современные браузеры могут использовать собственный зашифрованный DNS-провайдер, называемый _защищённый DNS_ или _DNS через HTTPS_. Установите Blokada Cloud, и браузер будет блокировать рекламу и трекеры в любой сети без необходимости устанавливать расширение.

Эта настройка применима только к данному браузеру. Чтобы защитить весь компьютер, используйте [профиль Apple](../apple-devices/) на Mac или настройте [роутер](../router-ad-blocking/).

## Chrome

1. Откройте `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Введите {% doh %}

## Edge

1. Откройте `edge://settings/privacy`.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. Откройте `brave://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Введите {% doh %}

## Safari

В Safari нет собственного параметра защищённого DNS. Используется системный DNS, поэтому установите [профиль Apple](../apple-devices/).

## Проверьте, что всё работает

Просмотрите сайты в течение минуты, затем откройте страницу _Активность_ в [панели управления](https://app.blokada.org/stats?src=guides). Запросы этого браузера появятся там.

## Если что-то не работает

<div class="note tip">

Если ваш браузер управляется организацией или учебным заведением, настройка защищённого DNS может быть заблокирована. Обратитесь к вашему администратору.

</div>
