---
title: Block ads on Linux with DNS over TLS
description: Set up systemd-resolved to use Blokada Cloud over encrypted DNS over TLS, and block ads and trackers for every app on your Linux computer.
updated: 2026-09-28
order: 9
---

Повечето съвременни Linux дистрибуции, включително Ubuntu и Fedora, разрешават имена чрез _systemd-resolved_, който поддържа DNS през TLS. В Debian първо го инсталирайте с `sudo apt install systemd-resolved`. Насочете го към Blokada Cloud и рекламите и тракерите ще бъдат блокирани за всяко приложение на компютъра.

## Set up systemd-resolved

1. Create the folder with `sudo mkdir -p /etc/systemd/resolved.conf.d`, then the file `/etc/systemd/resolved.conf.d/blokada.conf` with these settings:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Restart it: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Check it: <code>resolvectl status</code> shows <code>+DNSOverTLS</code> and the Blokada server.</li>
</ol>

The part after `#` is your Blokada DNS name: {% dot %} systemd-resolved checks the server's certificate against it, and Blokada uses it to know which device is asking.

<div class="note">

**NetworkManager** също препраща DNS сървърите на вашата мрежа. `Domains=~.` изпраща всички заявки към Blokada, но ако `resolvectl status` все още показва друг сървър за връзката, изключете автоматичното задаване на DNS за тази връзка (превключвателя _Автоматично_ до _DNS_ в нейните IPv4 и IPv6 настройки).

</div>

## Without systemd-resolved

Ако `resolvectl` не е наличен, вашата дистрибуция разрешава имената по друг начин. Настройте защитен DNS направо в браузъра си, според [ръководството за браузър](../browser-dns-over-https/), или настройте [рутера си](../router-ad-blocking/), за да покриете цялото домакинство.

## Проверка дали работи

Отворете няколко уебсайта, след това прегледайте страницата _Дейност_ в [таблото за управление](https://app.blokada.org/stats?src=guides). Запитванията от този компютър ще се показват там.

<div class="note">

Искате ли VPN и на този компютър? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) включва настройка на WireGuard, която криптира целия трафик с едно и също блокиране.

</div>
