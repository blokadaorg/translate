---
title: Блокирайте рекламите в цялата си мрежа, чрез блокиране на рекламите от рутера
description: Настройте Blokada Cloud на вашия рутер само веднъж и всички устройства у дома ще бъдат защитени, включително телевизори, игрови конзоли и смарт спийкъри, които не могат да използват рекламен блокер.
updated: 09-10-2026
order: 4
---

Всяко устройство във вашата мрежа пита рутера кой DNS сървър да използва. Насочете рутера към Blokada Cloud и рекламите и тракерите ще бъдат блокирани за всичко зад него. Това включва смарт телевизори, игрови конзоли, стрийминг устройства и умни домашни устройства, които нямат възможност за приложение за блокиране на реклами.

## Какво е необходимо за вашия рутер

Има два начина да настроите рутерa:

- **Encrypted DNS with a host name**, that is DNS over TLS (DoT) or DNS over HTTPS (DoH). Many recent routers support it, including the models below. Depending on which your router supports, you need your DNS name or your DoH link, both under _Your details_ above.
- **A plain IPv6 DNS address.** Many internet provider routers only accept plain IP addresses for DNS. If yours does and your connection has IPv6, Blokada gives you an IPv6 address to enter. See [Routers that only take an IP address](#routers-that-only-take-an-ip-address).

Use encrypted DNS if your router supports it. Lookups stay private on their way to Blokada.

## FRITZ!Box

FRITZ!OS 7.20 или по-нова версия.

1. Отворете `http://fritz.box` и отидете на _Интернет → Информация за акаунта_, след това на таба _DNS сървър_.
2. Включете _Шифрирано разрешаване на имена в интернет (DNS over TLS)_.
3. В _Разрешени имена на DNS сървъра_ въведете само {% dot %}. **Премахнете всеки друг запис.** FRITZ!Box използва всички изброени преобразуватели, и всеки друг ще пропуска реклами.
4. Отметнете опцията за проверка на сертификати и премахнете отметката от тази, която позволява връщане към нешифрирано разрешаване на имена.
5. Ако виждате _Превключване към публични DNS сървъри при прекъсване на DNS_, изключете го.
6. Кликнете върху _Приложи_.

## ASUS

Фърмуер на ASUS 3.0.0.4.386.4хххх, или по-нова версия и Asuswrt-Merlin.

1. Отворете администраторската страница на рутера и отидете на _WAN → Интернет връзка_.
2. Под _WAN DNS Setting_ задайте _DNS Privacy Protocol_ на _DNS-over-TLS (DoT)_ и _DNS-over-TLS Profile_ на _Strict_.
3. Премахнете всички записи от _Списък на DNS-over-TLS сървърите_, след това добавете един:
   - Адрес: {% ip "dot" %}
   - TLS хост: {% dot %}
4. Кликнете върху _Приложи_.

## OpenWrt

1. В _System → Software_ актуализирайте списъците и инсталирайте `luci-app-https-dns-proxy`.
2. Отворете _Услуги → HTTPS DNS Proxy_. Изтрийте настройките за другите доставчици.
3. Добавете запис с персонализиран URL на препращане: {% doh %}
4. _Запазете и приложете_. Пакетът автоматично ще насочва dnsmasq към него.

## Други рутери

Look for a setting called _DNS over TLS_, _Private DNS_, _Encrypted DNS_ or _DNS over HTTPS_. Enter your Blokada DNS name or DoH link from above, and remove every other DNS server, including fallback servers. If there is no such setting, use a plain IPv6 address as below.

## Routers that only take an IP address {:#routers-that-only-take-an-ip-address}

Your router and your internet connection need IPv6 for this. Support for plain IPv4 addresses is coming later.

1. In the [dashboard](https://app.blokada.org/setup?src=guides), open _Setup_ and choose _Router, TV, game console_.
2. Name the router, for example _Home router_, and select _Get address_. The name shows up in your activity and can't be changed later.
3. In the router's settings, find the DNS servers for IPv6, often under _Internet_, _WAN_ or _IPv6_, and enter the address as the only DNS server.
4. **Remove every other DNS server, IPv4 ones included.** Devices that still get an IPv4 DNS server from the router send some lookups past Blokada. If the router can't leave IPv4 DNS empty, set up your devices one at a time instead: [Android](../android-private-dns/), [Mac and Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), and [browsers](../browser-dns-over-https/).

The same setup works for a TV or game console that lets you enter a DNS server by hand. Give each one its own address, so it shows up by name in your activity.

<div class="note aside">

These lookups travel unencrypted to Blokada, like with any plain DNS server. If your router supports DNS over TLS or DNS over HTTPS, use that instead.

</div>

## Проверка дали работи

1. Рестартирайте едно устройство или изключете и включете отново неговата Wi-Fi връзка, за да се обнови промяната.
2. On that device, turn off Blokada if it runs it, then open [go.blokada.org/test](https://go.blokada.org/test). It shows whether your DNS goes through Blokada.
3. Browse for a minute, then open the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). Your network's lookups show up there.

## Ако някои устройства все още показват реклами

Някои устройства заобикалят рутера: телефони с активирана _Частна DNS_ услуга, браузъри със _Сигурна DNS_ услуга, настроена към друг доставчик и устройства с вграден собствен DNS. Настройте тези устройства индивидуално, или изключете тяхната DNS настройка.

<div class="note tip">

Зад рутера всички устройства споделят един адрес, затова таблото показва вашата мрежа като едно устройство. Настройте телефоните и лаптопите с тяхно собствено Blokada DNS име, ако искате да ги виждате поотделно. Също така те ще си запазят блокирането, когато напуснат дома.

</div>
