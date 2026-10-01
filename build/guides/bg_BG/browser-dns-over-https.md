---
title: Блокиране на реклами в Chrome, Firefox, Edge и Brave с DNS през HTTPS
description: Задайте Blokada Cloud като защитен DNS доставчик във вашия браузър, за да блокирате реклами и тракери на всеки компютър, включително служебни лаптопи, на които не можете да инсталирате приложения.
updated: 23-09-2026
order: 7
---

Съвременните браузъри могат да използват собствен криптиран DNS доставчик, наречен _сигурен DNS_ или _DNS през HTTPS_. Задайте го на Blokada Cloud и браузърът ще блокира реклами и тракери във всяка мрежа, без да инсталирате разширението.

Тази настройка обхваща само самият браузър. За да защитите целия компютър, използвайте [Apple профил](../apple-devices/) на Mac или настройте вашия [рутер](../router-ad-blocking/).

Вашият DoH линк: {% doh %}

## Chrome

1. Отворете `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Въведете {% doh %}

## Edge

1. Отворете `edge://settings/privacy`.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. Отворете `brave://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Въведете {% doh %}

## Safari

Safari няма собствена настройка за защитен DNS. Използва системния DNS, затова инсталирайте [Apple профила](../apple-devices/).

## Проверка дали работи

Сърфирайте за минута, след това отворете страницата _Дейност_ в [таблото за управление](https://app.blokada.org/stats?src=guides). Запитванията от браузъра ще се показват там.

<div class="note">

Ако вашият браузър се управлява от работа или училище, настройката за защитен DNS може да е заключена. Попитайте вашия администратор.

</div>
