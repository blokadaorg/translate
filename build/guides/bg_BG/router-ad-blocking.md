---
title: Блокирайте рекламите в цялата си мрежа чрез блокиране на рекламите от рутера
description: Настройте Blokada Cloud на вашия рутер само веднъж и всички устройства у дома ще бъдат защитени, включително телевизори, игрови конзоли и смарт спийкъри, които не могат да използват рекламен блокер.
updated: 2026-10-02
order: 4
---

Every device on your network asks the router which DNS server to use. Point the router at Blokada Cloud, and ads and trackers are blocked for everything behind it. That includes smart TVs, game consoles, streaming sticks and smart home devices, which have no room for an ad blocker app.

## Какво е необходимо за вашия рутер

Your router must support **encrypted DNS with a host name**, that is DNS over TLS (DoT) or DNS over HTTPS (DoH). Many recent routers do, including the models below. Depending on which your router supports, you need your DNS name or your DoH link, both under _Your details_ above.

<div class="note important">

**Only plain IP addresses?** Many internet provider routers only accept plain IP addresses for DNS. Support for those is on the way. Until then, set up your devices one at a time: [Android](../android-private-dns/), [Mac and Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), and [browsers](../browser-dns-over-https/). You can also run a small forwarder on a Raspberry Pi, as described in the [Pi-hole guide](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 или по-нова версия.

1. Отворете `http://fritz.box` и отидете на _Интернет → Информация за акаунта_, след това на таба _DNS сървър_.
2. Включете _Шифрирано разрешаване на имена в интернет (DNS over TLS)_.
3. In _Resolved Names of the DNS Server_, enter only {% dot %}. **Remove every other entry.** The FRITZ!Box uses all listed resolvers, and any other one lets ads through.
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
2. Open _Services → HTTPS DNS Proxy_. Delete the instances for other providers.
3. Добавете запис с персонализиран URL на препращане: {% doh %}
4. _Save & Apply_. The package points dnsmasq at it automatically.

## Други рутери

Look for a setting called _DNS over TLS_, _Private DNS_, _Encrypted DNS_ or _DNS over HTTPS_. Enter your Blokada DNS name or DoH link from above, and remove every other DNS server, including fallback servers.

## Проверка дали работи

1. Рестартирайте едно устройство или изключете и включете отново неговата Wi-Fi връзка, за да се обнови промяната.
2. Browse for a minute, then open the _Activity_ page in the dashboard. Your network's lookups show up there.

## If some devices still show ads

Some devices bypass the router: phones with _Private DNS_ set, browsers with _secure DNS_ set to another provider, and devices that hard-code their own DNS. Set those up on the device itself, or turn their own DNS setting off.

<div class="note tip">

Behind the router, all devices share one address, so the dashboard shows your network as a single device. Set up phones and laptops with their own Blokada DNS name if you want to see them separately. They also keep their blocking when they leave home.

</div>
