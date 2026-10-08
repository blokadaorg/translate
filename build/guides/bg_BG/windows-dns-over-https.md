---
title: Блокиране на рекламите в Windows чрез DNS през HTTPS
description: Използвайте вградения в Windows 11 криптиран DNS заедно с Blokada Cloud, за да блокирате реклами и тракери във всяко приложение и браузър, без нужда от инсталиране на допълнителен софтуер.
updated: 02-10-2026
order: 8
---

Windows 11 can send all its DNS lookups encrypted, over DNS over HTTPS. Point it at Blokada Cloud, and ads and trackers are blocked in every app and browser on the computer, with nothing to install.

You need the DNS server's IP address and your DoH link, both under _Your details_ above.

## Windows 11

1. Отворете _Настройки → Мрежа и интернет_, след това _Wi-Fi_ или _Ethernet_, в зависимост от това как е свързан компютърът.
2. Open your connection's _Hardware properties_. For Wi-Fi, select _Manage known networks_ and then the network, or _Hardware properties_ at the top of the Wi-Fi page.
3. Next to _DNS server assignment_, select _Edit_. Choose _Manual_ and turn on _IPv4_.
4. Във _Възможен DNS_ въведете DNS сървъра {% ip "doh" %}
5. Задайте _DNS през HTTPS_ на _Включено (ръчен шаблон)_ и поставете вашия DoH линк {% doh %} като _DoH шаблон_.
6. Изключете _Fallback to plaintext_ и изберете _Запази_.

Ако компютърът използва както Wi-Fi, така и Ethernet, повторете това и за другата връзка.

<div class="note important">

Leave _Alternate DNS_ empty. Windows uses both servers, and any other one lets ads through.

</div>

<div class="note tip">

No _On (manual template)_ option? Your Windows 11 is older. Update Windows, or use the [browser guide](../browser-dns-over-https/) meanwhile.

</div>

## Windows 10+

Windows 10 has no built-in encrypted DNS. Set up secure DNS in your browser instead, as in the [browser guide](../browser-dns-over-https/), or set up your [router](../router-ad-blocking/) to cover the whole home.

## Проверка дали работи

Open a few websites, then look at the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). This computer's lookups show up there.

<div class="note aside">

Want a VPN on this computer too? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) includes a WireGuard setup that encrypts all traffic, with the same blocking.

</div>

## If something doesn't work

Chrome and Edge have their own _secure DNS_ setting, which bypasses Windows. Left on automatic, it can fall back to plain DNS, which Blokada refuses. Set it to your DoH link instead:

- **Chrome:** отворете `chrome://settings/security`, включете _Използване на защитен DNS_ и под _Избор на DNS доставчик_ изберете _Добавяне на собствен доставчик на DNS услуги_.
- **Edge:** отворете `edge://settings/privacy`, включете защитен DNS и изберете _Изберете доставчик на услуга_.

След това поставете вашия DoH линк {% doh %}

If some ads still get through on a network with IPv6, Windows may also be asking your router's IPv6 DNS server. Turn off _Internet Protocol Version 6 (TCP/IPv6)_ in the adapter's properties (_Control Panel → Network Connections_), or set up your [router](../router-ad-blocking/).
