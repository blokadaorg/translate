---
title: Блокируйте рекламу во всей сети с помощью блокировки рекламы на роутере
description: Настройте Blokada Cloud на вашем роутере один раз, и все устройства дома будут защищены, включая телевизоры, игровые приставки и умные колонки, которые не могут использовать блокировщик рекламы.
updated: 2026-10-09
order: 4
---

Каждое устройство в вашей сети запрашивает у роутера, какой DNS-сервер использовать. Укажите роутеру Blokada Cloud, чтобы реклама и трекеры блокировались для всего, что находится за ним. Это включает в себя умные телевизоры, игровые консоли, стриминговые приставки и устройства умного дома, для которых невозможно использовать приложение-блокировщик рекламы.

## Что необходимо вашему роутеру

There are two ways to set up a router:

- **Encrypted DNS with a host name**, that is DNS over TLS (DoT) or DNS over HTTPS (DoH). Many recent routers support it, including the models below. Depending on which your router supports, you need your DNS name or your DoH link, both under _Your details_ above.
- **A plain IPv6 DNS address.** Many internet provider routers only accept plain IP addresses for DNS. If yours does and your connection has IPv6, Blokada gives you an IPv6 address to enter. See [Routers that only take an IP address](#routers-that-only-take-an-ip-address).

Use encrypted DNS if your router supports it. Lookups stay private on their way to Blokada.

## FRITZ!Box

FRITZ!OS 7.20 или новее.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. В разделе _Разрешённые имена DNS-сервера_ укажите только {% dot %}. **Удалите все остальные записи.** FRITZ!Box использует все записанные резольверы — и любая лишняя запись позволит рекламе проходить.
4. Tick _Enforce certificate verification for encrypted name resolution_.
5. Если вы видите _Автоматическое переключение на общедоступные DNS-серверы при нарушении работы DNS_, отключите эту опцию.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Адрес: {% ip "dot" %}
   - Имя хоста TLS: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Откройте _Службы → HTTPS DNS Proxy_. Удалите экземпляры для других провайдеров.
3. Добавьте экземпляр с пользовательским URL-адресом резольвера: {% doh %}
4. _Сохранить и применить_. Пакет автоматически укажет на него dnsmasq.

## Другие роутеры

Look for a setting called _DNS over TLS_, _Private DNS_, _Encrypted DNS_ or _DNS over HTTPS_. Enter your Blokada DNS name or DoH link from above, and remove every other DNS server, including fallback servers. If there is no such setting, use a plain IPv6 address as below.

## Роутеры, которые принимают только IP-адрес {:#routers-that-only-take-an-ip-address}

Your router and your internet connection need IPv6 for this. Support for plain IPv4 addresses is coming later.

1. In the [dashboard](https://app.blokada.org/setup?src=guides), open _Setup_ and choose _Router, TV, game console_.
2. Name the router, for example _Home router_, and select _Get address_. The name shows up in your activity and can't be changed later.
3. In the router's settings, find the DNS servers for IPv6, often under _Internet_, _WAN_ or _IPv6_, and enter the address as the only DNS server.
4. **Remove every other DNS server, IPv4 ones included.** Devices that still get an IPv4 DNS server from the router send some lookups past Blokada. If the router can't leave IPv4 DNS empty, set up your devices one at a time instead: [Android](../android-private-dns/), [Mac and Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), and [browsers](../browser-dns-over-https/).

The same setup works for a TV or game console that lets you enter a DNS server by hand. Give each one its own address, so it shows up by name in your activity.

<div class="note aside">

These lookups travel unencrypted to Blokada, like with any plain DNS server. If your router supports DNS over TLS or DNS over HTTPS, use that instead.

</div>

## Проверьте, что всё работает

1. Перезапустите одно устройство или выключите и включите его Wi‑Fi, чтобы оно приняло изменения.
2. On that device, turn off Blokada if it runs it, then open [go.blokada.org/test](https://go.blokada.org/test). It shows whether your DNS goes through Blokada.
3. Browse for a minute, then open the _Activity_ page in the [dashboard](https://app.blokada.org/stats?src=guides). Your network's lookups show up there.

## Если на некоторых устройствах все еще отображается реклама

Некоторые устройства обходят роутер: смартфоны с включённым _Private DNS_, браузеры с _Secure DNS_ от другого провайдера и устройства с жёстко прописанным собственным DNS. Настройте их непосредственно на устройстве или отключите их собственные настройки DNS.

<div class="note tip">

За роутером все устройства используют один адрес, поэтому панель управления показывает вашу сеть как одно устройство. Чтобы видеть телефоны и ноутбуки отдельно, настройте их с собственным DNS-именем Blokada. Также эти устройства сохраняют блокировку, когда покидают дом.

</div>
