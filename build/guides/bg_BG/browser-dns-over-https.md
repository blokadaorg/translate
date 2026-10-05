---
title: Блокиране на реклами в Chrome, Firefox, Edge и Brave с DNS през HTTPS
description: Задайте Blokada Cloud като защитен DNS доставчик във вашия браузър, за да блокирате реклами и тракери на всеки компютър, включително служебни лаптопи, на които не можете да инсталирате приложения.
updated: 2026-10-02
order: 7
---

Modern browsers can use their own encrypted DNS provider, called _secure DNS_ or _DNS over HTTPS_. Set it to Blokada Cloud, and the browser blocks ads and trackers on any network, with no extension to install.

This setting covers only this browser. To cover the whole computer, use the [Apple profile](../apple-devices/) on a Mac, or set up your [router](../router-ad-blocking/).

## Chrome

1. Отворете `chrome://settings/security`.
2. Включете _Използвай защитен DNS_, след което изберете _Добави собствен доставчик на DNS услуги_.
3. Въведете {% doh %}

## Edge

1. Отворете `edge://settings/privacy`.
2. В раздел _Сигурност_ включете _Използвай защитен DNS, за да зададете как да се търси мрежовия адрес на уебсайтовете_.
3. Изберете _Изберете доставчик на услуги_ и въведете {% doh %}

## Firefox

1. Отворете _Настройки → Поверителност и сигурност_ и превъртете до _DNS през HTTPS_.
2. Изберете _Максимална защита_.
3. Под _Избор на доставчик_ изберете _Потребителски_ и въведете {% doh %}

## Brave

1. Отворете `brave://settings/security`.
2. Включете _Използвай защитен DNS_, след това изберете _Добави персонализиран DNS доставчик_.
3. Въведете {% doh %}

## Safari

Safari has no secure DNS setting of its own. It uses the system's DNS, so install the [Apple profile](../apple-devices/).

## Проверка дали работи

Browse for a minute, then open the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). This browser's lookups show up there.

## If something doesn't work

<div class="note tip">

If your browser is managed by work or school, the secure DNS setting may be locked. Ask your administrator.

</div>
