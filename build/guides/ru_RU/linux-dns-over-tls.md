---
title: Блокировка рекламы в Linux с помощью DNS over TLS.
description: Настройте systemd-resolved для использования Blokada Cloud через зашифрованный DNS over TLS и блокировки рекламы и трекеров для каждого приложения на вашем компьютере с Linux.
updated: 2026-10-02
order: 9
---

Большинство современных дистрибутивов Linux, включая Ubuntu и Fedora, разрешают имена через _systemd-resolved_, который поддерживает DNS over TLS. В Debian сначала установите его с помощью `sudo apt install systemd-resolved`. Настройте его на Blokada Cloud — реклама и трекеры будут заблокированы для каждого приложения на компьютере.

## Настройка systemd-resolved

1. Создайте папку командой `sudo mkdir -p /etc/systemd/resolved.conf.d`, затем файл `/etc/systemd/resolved.conf.d/blokada.conf` с такими параметрами:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Перезапустите: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Проверьте: <code>resolvectl status</code> показывает <code>+DNSOverTLS</code> и сервер Blokada.</li>
</ol>

Часть после символа `#` — это ваш DNS-имя Blokada: {% dot %} systemd-resolved проверяет сертификат сервера по этому имени, а Blokada использует его, чтобы узнать, какое устройство делает запрос.

<div class="note important">

**NetworkManager** также передаёт DNS-серверы вашей сети. `Domains=~.` отправляет все запросы в Blokada, но если в `resolvectl status` всё ещё отображается другой сервер на соединении, отключите автоматическое получение DNS для этого соединения (переключатель _Автоматически_ рядом с _DNS_ в его настройках IPv4 и IPv6).

</div>

## Без systemd-resolved

Если команда `resolvectl` не найдена, ваша система использует другой способ резолвинга. Вместо этого настройте защищённый DNS в вашем браузере, как описано в [руководстве по браузеру](../browser-dns-over-https/), или настройте [роутер](../router-ad-blocking/), чтобы защитить всю домашнюю сеть.

## Проверьте работоспособность

Откройте несколько сайтов, затем посмотрите страницу _Активность_ в [dashboard](https://app.blokada.org/stats?src=guides). Запросы этого компьютера будут отображаться там.

<div class="note aside">

Хотите VPN и на этом компьютере? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) включает настройку WireGuard для шифрования всего трафика с такой же блокировкой.

</div>
