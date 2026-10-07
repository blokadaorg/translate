---
title: Блокиране на рекламите в Linux чрез DNS през TLS
description: Настройтка на systemd-resolved да използва Blokada Cloud чрез криптиран DNS over TLS и блокирайте реклами и тракери за всяко приложение на вашия Linux компютър.
updated: 02-10-2026
order: 9
---

Повечето съвременни Linux дистрибуции, включително Ubuntu и Fedora, разрешават имена чрез _systemd-resolved_, който поддържа DNS през TLS. В Debian първо го инсталирайте с `sudo apt install systemd-resolved`. Насочете го към Blokada Cloud и рекламите и тракерите ще бъдат блокирани за всяко приложение на компютъра.

## Настройване на systemd-resolved

1. Създайте папката с команда `sudo mkdir -p /etc/systemd/resolved.conf.d`, след това файла `/etc/systemd/resolved.conf.d/blokada.conf` със следните настройки:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Рестартирайте го: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Проверка: <code>resolvectl status</code> показва <code>+DNSOverTLS</code> и сървъра на Blokada.</li>
</ol>

Частта след `#` е вашето име на Blokada DNS: {% dot %} systemd-resolved проверява сертификата на сървъра спрямо него, а Blokada го използва, за да разбере кое устройство прави заявката.

<div class="note important">

**NetworkManager** също предава DNS сървърите на вашата мрежа. `Domains=~.` изпраща всички заявки към Blokada, но ако `resolvectl status` все още показва друг сървър за дадена връзка, то изключете автоматичното задаване на DNS за тази връзка (превключвателя _Автоматично_ до _DNS_ в неговите IPv4 и IPv6 настройки).

</div>

## Без systemd-resolved

Ако не е намерена команда `resolvectl`, Вашата дистрибуция решава за имената по друг начин. Вместо това настройте защитен DNS във Вашия браузър, както е описано в [ръководството за браузър](../browser-dns-over-https/), или настройте Вашия [рутер](../router-ad-blocking/), за да покриете целия дом.

## Проверка дали работи

Отворете няколко уебсайта, а след това проверете страницата _Дейност_ в [таблото за управление](https://app.blokada.org/stats?src=guides). Търсенията от този компютър ще се покажат там.

<div class="note aside">

Искате ли VPN и на този компютър? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) включва настройка от WireGuard, която криптира целия трафик и осигурява същото блокиране.

</div>
