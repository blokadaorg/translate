---
title: Алтернатива на Pi-hole, която не изисква хардуер
description: Преместете блокирането на реклами във вашия дом от Pi-hole към Blokada Cloud, или запазете Pi-hole и изпращайте заявките му през Blokada.
updated: 2026-10-09
order: 1
---

Pi-hole блокира рекламите за всяко устройство във вашата мрежа, стига Raspberry Pi да е включен, актуализиран и вкъщи. Blokada Cloud върши същата работа от нашите сървъри:

- **Няма кутия за поддръжка.** Без SD карти, без актуализации, без прекъсване ако Pi спре да работи.
- **Работи и извън дома.** Телефоните и лаптопите запазват блокирането си в мобилните мрежи за данни и други Wi-Fi мрежи.
- **Encrypted.** Devices talk to Blokada over DNS over TLS or DNS over HTTPS, so your provider cannot read or change your lookups. The exception is a router or device set up with a plain IPv6 address, whose lookups are not encrypted.
- **Едно табло за управление.** Блокиращи списъци, разрешени и блокирани домейни и активност по устройство, на [app.blokada.org](https://app.blokada.org/?src=guides).

Има два начина за преход. Заменете Pi-hole напълно, или го запазете и използвайте за достъп на Blokada Cloud.

## Вариант 1: замяна на Pi-hole

1. **Вземете Blokada Cloud** и отворете таблото. Вашето име на DNS и вашият DoH линк са в секция _Настройки_, в началото на _Вашите данни_.
2. **Point your router at Blokada instead of the Pi-hole.** Follow the [router guide](../router-ad-blocking/). It also covers routers that only accept a plain IP address as DNS server, as long as your connection has IPv6. Without IPv6, set up your devices one by one instead: [Android](../android-private-dns/), [Mac and Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), and [browsers](../browser-dns-over-https/).
3. **Ако вашият Pi-hole е бил DHCP сървърът,** включете DHCP отново на вашия рутер _преди_ да изключите Pi. В противен случай устройствата ви няма да получават мрежови адреси.
4. **Преместете вашите списъци.** В таблото за управление изберете блокиращи списъци под _Блокиращи списъци_ и добавете вашите разрешени или блокирани домейни под _Изключения_.
5. **Изключете Pi-hole,** или го запазете за последваща друга употреба.

<div class="note aside">

Your Pi-hole showed every device on the network by its IP address. With Blokada each device shows up by its own name, as long as it uses its own Blokada DNS name. A router set up with one Blokada DNS name or IPv6 address shows up as one device.

</div>

## Вариант 2: запазете Pi-hole, използвайте Blokada Cloud като входящ Dns сървър

Ако желаете да запазите локалната си конфигурация, като локални имена на хостове, DHCP или собствени списъци, трябва Pi-hole да препраща заявките си към Blokada по криптирана връзка. Pi-hole сам не поддържа криптирано препращане, затова трябва малък ретранслатор да работи до него. Това ръководство използва [dnsproxy](https://github.com/AdguardTeam/dnsproxy), софтуер с отворен код, който представлява единичен файл.

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
4. В админ панела на Pi-hole отворете _Настройки → DNS_. Премахнете отметката от всички налични сървъри и добавете `127.0.0.1#5054` като персонализиран препращащ сървър. Запазете.
5. Проверете страницата _Activity_ (Дейност) в таблото за управление. Вече там ще виждате заявките от вашата мрежа.

Можете да изключите собствените блоклисти на Pi-hole и да управлявате блокирането в таблото за управление, или да използвате и двете едновременно.

## Често задавани въпроси

**Трябва ли ми Blokada Plus?** Не. Blokada Cloud осигурява DNS блокиране за целия ви дом. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) добавя VPN отгоре.

Ами ако Blokada стане недостъпна? Устройствата ви няма да могат да намират IP адресите по имена, докато услугата не заработи отново — също както когато Pi-hole спре. Не добавяйте втори, нефилтриращ DNS сървър за резервен вариант. Повечето устройства използват всички зададени сървъри на случаен принцип, така че рекламите ще се показват.
