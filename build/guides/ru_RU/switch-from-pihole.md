---
title: Альтернатива Pi-hole, не требующая аппаратного обеспечения.
description: Перенесите блокировку рекламы в вашем доме с Pi-hole на Blokada Cloud или оставьте Pi-hole и направьте его запросы через Blokada.
updated: 2026-10-09
order: 1
---

Pi-hole блокирует рекламу для каждого устройства в вашей сети, пока Raspberry Pi работает, обновлён и находится дома. Blokada Cloud делает то же самое с помощью наших серверов:

- **Не нужно обслуживать отдельное устройство.** Нет SD-карт, нет обновлений, нет сбоев при отключении Pi.
- **Работает вне дома.** Блокировка работает на телефонах и ноутбуках в мобильных сетях и других Wi-Fi сетях.
- **Encrypted.** Devices talk to Blokada over DNS over TLS or DNS over HTTPS, so your provider cannot read or change your lookups. The exception is a router or device set up with a plain IPv6 address, whose lookups are not encrypted.
- **Единая панель управления.** Списки блокировок, разрешённые и заблокированные домены, а также активность по устройствам доступны на [app.blokada.org](https://app.blokada.org/?src=guides).

Есть два способа переключения. Полностью заменить Pi-hole или сохранить его и использовать Blokada Cloud как вышестоящий сервер.

## Вариант 1: заменить Pi-hole

1. **Оформите Blokada Cloud** и откройте панель управления. Ваше имя DNS и ссылка DoH находятся в разделе _Настройка_, а также в разделе _Ваши данные_ выше.
2. **Point your router at Blokada instead of the Pi-hole.** Follow the [router guide](../router-ad-blocking/). It also covers routers that only accept a plain IP address as DNS server, as long as your connection has IPv6. Without IPv6, set up your devices one by one instead: [Android](../android-private-dns/), [Mac and Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), and [browsers](../browser-dns-over-https/).
3. **Если ваш Pi-hole был DHCP-сервером,** включите DHCP на роутере _до того_, как выключите Pi. В противном случае устройства перестанут получать сетевые адреса.
4. **Перенесите ваши списки.** В панели управления выберите списки блокировки в разделе _Списки блокировок_, а свои разрешённые или заблокированные домены добавьте в разделе _Исключения_.
5. **Отключите Pi-hole** или используйте его для других задач.

<div class="note aside">

Ваш Pi-hole отображал каждое устройство в сети по его IP-адресу. В Blokada каждое устройство отображается под собственным именем, при условии, что оно использует собственное DNS-имя Blokada. Роутер, настроенный с использованием одного DNS-имени Blokada или IPv6-адреса, отображается как одно устройство.

</div>

## Вариант 2: Оставьте Pi-hole, используйте Blokada Cloud как вышестоящий DNS

Если вы хотите сохранить локальную настройку, например локальные имена хостов, DHCP или собственные списки, настройте Pi-hole на пересылку запросов в Blokada по зашифрованному каналу. Сам Pi-hole не может пересылать DNS-запросы в шифрованном виде, поэтому рядом с ним работает небольшой форвардер. В этом руководстве используется [dnsproxy](https://github.com/AdguardTeam/dnsproxy) — открытый форвардер в виде одного файла.

1. На устройстве с Pi-hole скачайте релиз `dnsproxy` для нужного процессора (`linux-arm64` для современных Raspberry Pi) со страницы релизов и скопируйте бинарный файл `dnsproxy` в `/usr/local/bin/`.
2. Создайте файл `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Зашифрованный DNS-переадресатор на Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Запустите сервис: `sudo systemctl enable --now dnsproxy`
4. В админке Pi-hole откройте _Настройки → DNS_. Снимите все галочки с вышестоящих серверов и добавьте `127.0.0.1#5054` как собственный вышестоящий сервер. Сохраните.
5. Проверьте страницу _Активность_ в панели управления. Запросы с вашей сети теперь отображаются там.

Вы можете отключить собственные списки блокировок Pi-hole и управлять блокировкой через панель управления, либо использовать оба варианта одновременно.

## Часто задаваемые вопросы

**Нужен ли Blokada Plus?** Нет. Blokada Cloud обеспечивает DNS-блокировку для всего вашего дома. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) просто добавляет VPN.

**Что если Blokada будет недоступна?** Ваши устройства не смогут выполнять резолвинг до восстановления работы, так же как при отключении Pi-hole. Не добавляйте второй неотфильтрованный DNS-сервер в качестве резервного. Большинство устройств случайным образом используют любой из указанных серверов, поэтому реклама может просачиваться.
