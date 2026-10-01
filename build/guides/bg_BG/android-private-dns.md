---
title: Настройка на частен DNS на Android с Blokada Cloud
description: Използване на вградената настройка за частен DNS в Android с Blokada Cloud, за да блокирате реклами и тракери във всяко приложение, както през Wi-Fi, така и през мобилни данни. Или оставете приложението Blokada 6 да го направи.
updated: 2026-09-28
order: 5
---

## Най-лесният начин: приложението

[Blokada 6](https://go.blokada.org/play_cloud) настройва всичко вместо вас, включва и изключва блокирането с едно докосване и показва какво е блокирано директно на телефона. Влезте с вашия Акаунт ID и сте готови.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Вземете Blokada 6 от Google Play</a></p>

## Без приложението: Частен DNS

Android 9 и по-новите версии имат настройка за _Частен DNS_. Настройте го на Blokada Cloud и рекламите и тракерите ще бъдат блокирани във всички приложения, на всяка мрежа, без да има нищо работещо на заден план.

Вашето Blokada DNS име: {% dot %}

1. Отворете _Настройки → Мрежа и интернет_. На някои телефони това е _Връзки_ или _Връзка и споделяне_.
2. Докоснете _Частен DNS_. На телефоните Samsung се намира под _Още настройки за връзка_.
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

Ако не можете да го намерите, потърсете в приложението Настройки за "Частен DNS".

## Проверка дали работи

Отворете няколко уебсайта или приложения, а след това проверете страницата _Дейност_ в [таблото за управление](https://app.blokada.org/stats?src=guides). Запитванията от този телефон ще се показват там.

## Ако нещо не работи

- **"Не може да се свърже" или няма интернет:** проверете името на вашия Blokada DNS за правописни грешки. Трябва да е точно както е показано по-горе, без `https://`.
- **Активно е друго VPN приложение:** някои VPN приложения използват собствен DNS и заобикалят Частния DNS. Изключете настройката за DNS или блокиране на реклами във VPN-а или използвайте Blokada 6.
- **Chrome still shows ads:** Chrome may be set to its own secure DNS provider, which bypasses Private DNS. In Chrome, open _Settings → Privacy and security → Use secure DNS_ and choose _Use your current service provider_. Chrome then follows Private DNS.
