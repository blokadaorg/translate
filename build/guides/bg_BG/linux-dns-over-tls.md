---
title: Блокиране на рекламите в Linux чрез DNS през TLS
description: Настройтка на systemd-resolved да използва Blokada Cloud чрез криптиран DNS over TLS и блокирайте реклами и тракери за всяко приложение на вашия Linux компютър.
updated: 2026-10-02
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

**NetworkManager** също препраща DNS сървърите на вашата мрежа. `Domains=~.` изпраща всички заявки към Blokada, но ако `resolvectl status` все още показва друг сървър за връзката, изключете автоматичното задаване на DNS за тази връзка (превключвателя _Автоматично_ до _DNS_ в нейните IPv4 и IPv6 настройки).

</div>

## Без systemd-resolved

Ако `resolvectl` не е наличен, вашата дистрибуция разрешава имената по друг начин. Настройте защитен DNS направо в браузъра си, според [ръководството за браузър](../browser-dns-over-https/), или настройте [рутера си](../router-ad-blocking/), за да покриете цялото домакинство.

## Проверка дали работи

Отворете няколко уебсайта, след това прегледайте страницата _Дейност_ в [таблото за управление](https://app.blokada.org/stats?src=guides). Запитванията от този компютър ще се показват там.

<div class="note aside">

Искате ли VPN и на този компютър? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) включва настройка на WireGuard, която криптира целия трафик с едно и също блокиране.

</div>
