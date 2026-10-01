---
title: Блокирайте рекламите в цялата си мрежа чрез блокиране на рекламите от рутера
description: Настройте Blokada Cloud на вашия рутер само веднъж и всички устройства у дома ще бъдат защитени, включително телевизори, игрови конзоли и смарт спийкъри, които не могат да използват рекламен блокер.
updated: 2026-09-23
order: 4
---

Всяко устройство във Вашата мрежа пита рутера кой DNS сървър да използва. Насочете рутера към Blokada Cloud и рекламите и тракерите ще бъдат блокирани за всичко, което зад него. Това включва смарт телевизори, игрови конзоли, стрийминг устройства и умни домашни устройства, които не поддържат приложение за блокиране на реклами.

## Какво е необходимо за вашия рутер

Вашият рутер трябва да поддържа **криптиран DNS с име на хост**, тоест DNS over TLS (DoT) или DNS over HTTPS (DoH). Много от по-новите рутери го поддържат, включително моделите по-долу. В зависимост от това кое поддържа вашият рутер, ви е необходимо:

- За DNS през TLS, вашето име на Blokada DNS: {% dot %}
- За DNS през HTTPS, вашият DoH линк: {% doh %}

<div class="note">

**Само обикновени IP адреси?** Много рутери на интернет доставчици приемат само обикновени IP адреси за DNS. Поддръжката за тях предстои. До тогава настройте устройствата си едно по едно: [Android](../android-private-dns/), [Mac и Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) и [броузъри](../browser-dns-over-https/). Можете също така да стартирате малък препращач на Raspberry Pi, както е описано в [Pi-hole guide](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 или по-нова версия.

1. Отворете `http://fritz.box` и отидете на _Интернет → Информация за акаунта_, след това на таба _DNS сървър_.
2. Включете _Шифрирано разрешаване на имена в интернет (DNS over TLS)_.
3. В _Разрешени имена на DNS сървъра_ въведете само {% dot %}. **Премахнете всеки друг запис.** FRITZ!Box използва всички изброени преобразуватели и всеки друг ще пропуска реклами.
4. Отметнете опцията за проверка на сертификати и премахнете отметката от тази, която позволява връщане към нешифрирано разрешаване на имена.
5. Ако виждате _Превключване към публични DNS сървъри при прекъсване на DNS_, изключете го.
6. Кликнете върху _Приложи_.

## ASUS

Фърмуер на ASUS 3.0.0.4.386.4хххх, или по-нова версия и Asuswrt-Merlin.

1. Отворете администраторската страница на рутера и отидете на _WAN → Интернет връзка_.
2. Под _WAN DNS Setting_ задайте _DNS Privacy Protocol_ на _DNS-over-TLS (DoT)_ и _DNS-over-TLS Profile_ на _Strict_.
3. Премахнете всички записи от _Списък на DNS-over-TLS сървърите_, след това добавете един:
   - Адрес: {% ip "dot" %}
   - TLS Hostname: {% dot %}
4. Кликнете върху _Приложи_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Open _Services → HTTPS DNS Proxy_. Delete the instances for other providers.
3. Add an instance with a custom resolver URL: {% doh %}
4. _Save & Apply_. The package points dnsmasq at it automatically.

## Other routers

Look for a setting called _DNS over TLS_, _Private DNS_, _Encrypted DNS_ or _DNS over HTTPS_. Enter your Blokada DNS name or DoH link from above, and remove every other DNS server, including fallback servers.

## Check that it works

1. Restart one device, or turn its Wi-Fi off and on, so it picks up the change.
2. Browse for a minute, then open the _Activity_ page in the dashboard. Your network's lookups show up there.

Some devices bypass the router: phones with _Private DNS_ set, browsers with _secure DNS_ set to another provider, and devices that hard-code their own DNS. Set those up on the device itself, or turn their own DNS setting off.

<div class="note">

Behind the router, all devices share one address, so the dashboard shows your network as a single device. Set up phones and laptops with their own Blokada DNS name if you want to see them separately. They also keep their blocking when they leave home.

</div>
