---
title: Алтернатива на Pi-hole, която не изисква хардуер
description: Преместете блокирането на реклами във вашия дом от Pi-hole към Blokada Cloud, или запазете Pi-hole и изпращайте заявките му през Blokada.
updated: 2026-10-02
order: 1
---

A Pi-hole blocks ads for every device on your network, as long as the Raspberry Pi is running, updated and at home. Blokada Cloud does the same job from our servers:

- **Няма кутия за поддръжка.** Без SD карти, без актуализации, без прекъсване, ако Pi спре да работи.
- **Работи и извън дома.** Телефоните и лаптопите запазват блокирането си в мобилните мрежи за данни и други Wi-Fi мрежи.
- **Криптирано.** Устройствата комуникират с Blokada чрез DNS през TLS или DNS през HTTPS, така че вашият доставчик не може да чете или променя вашите заявки.
- **Едно табло за управление.** Блокиращи списъци, разрешени и блокирани домейни и активност по устройство, на [app.blokada.org](https://app.blokada.org/?src=guides).

There are two ways to switch. Replace the Pi-hole completely, or keep it and use Blokada Cloud as its upstream.

## Вариант 1: замяна на Pi-hole

1. **Get Blokada Cloud** and open the dashboard. Your DNS name and DoH link are under _Setup_ there, and under _Your details_ above.
2. **Point your router at Blokada instead of the Pi-hole.** Follow the [router guide](../router-ad-blocking/). If your router only accepts a plain IP address as DNS server, set up your devices one by one instead: [Android](../android-private-dns/), [Mac and Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), and [browsers](../browser-dns-over-https/).
3. **If your Pi-hole was the DHCP server,** turn DHCP back on in your router _before_ you switch the Pi off. Otherwise your devices stop getting network addresses.
4. **Преместете вашите списъци.** В таблото за управление изберете блокиращи списъци под _Блокиращи списъци_ и добавете вашите разрешени или блокирани домейни под _Изключения_.
5. **Изключете Pi-hole,** или го запазете за последваща друга употреба.

<div class="note aside">

Your Pi-hole showed every device on the network by its IP address. With Blokada each device shows up by its own name, as long as it uses its own Blokada DNS name. A router set up with one Blokada DNS name shows up as one device.

</div>

## Вариант 2: запазете Pi-hole, използвайте Blokada Cloud като входящ Dns сървър

If you want to keep your local setup, such as local host names, DHCP or your own lists, let the Pi-hole forward its lookups to Blokada over an encrypted connection. Pi-hole cannot do encrypted forwarding itself, so a small forwarder runs next to it. This guide uses [dnsproxy](https://github.com/AdguardTeam/dnsproxy), an open source forwarder that is a single file.

1. На машината с Pi-hole изтеглете изданието на `dnsproxy` за вашия процесор (`linux-arm64` за по-нов Raspberry Pi) от страницата с издания и копирайте бинарния файл `dnsproxy` в `/usr/local/bin/`.
2. Създайте файл `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Encrypted DNS forwarder to Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Стартирайте го: `sudo systemctl enable --now dnsproxy`
4. In the Pi-hole admin, open _Settings → DNS_. Untick every upstream server and add `127.0.0.1#5054` as a custom upstream server. Save.
5. Check the dashboard _Activity_ page. Lookups from your network now show up there.

Можете да изключите собствените блоклисти на Pi-hole и да управлявате блокирането в таблото за управление, или да използвате и двете едновременно.

## Често задавани въпроси

**Do I need Blokada Plus?** No. Blokada Cloud covers DNS blocking for your whole home. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) adds a VPN on top.

**What if Blokada is unreachable?** Your devices cannot resolve names until it is back, just as when a Pi-hole goes down. Don't add a second, unfiltered DNS server as fallback. Most devices use all their servers at random, so ads would get through.
