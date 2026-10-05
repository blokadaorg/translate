---
title: Алтернатива на NextDNS със същата конфигурация на всяко устройство
description: Move from NextDNS to Blokada Cloud. Swap your NextDNS DNS name, DoH link or profile for Blokada's on your phone, computer and router, and keep your ad blocking.
updated: 2026-10-02
order: 3
---

NextDNS and Blokada Cloud work the same way: an encrypted DNS service that blocks ads and trackers by name, with your own settings behind a personal DNS name. Switching means replacing the NextDNS values on each device with your Blokada ones. Nothing else on the device changes.

## Какво сте използвали и какво да изберете в Blokada

| В NextDNS                                                            | В Blokada Cloud                                                                   |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Вашият идентификатор за конфигурация, напр. `abc123` | Идентификаторът на вашето устройство, част от вашето Blokada DNS име и DoH връзка |
| _Поверителни_ списъци за блокиране                                   | _Блокиращи списъци_ в таблото                                                     |
| _Сигурност_ (зловреден софтуер, фишинг)           | списък с вреден софтуер в _Списъци за блокиране_                                  |
| _Родителски контрол_                                                 | списъци за съдържание за възрастни и хазарт в _Блокиращи списъци_                 |
| _Списък с позволени_ и _Списък с блокирани_                          | _Изключения_ в таблото за управление                                              |
| _Логове_ и _Анализ_                                                  | _Активност_ и _Статистика_ в таблото                                              |

## Превключване всяко устройство

Depending on the device, you need your DNS name or your DoH link, both under _Your details_ above.

### Android

If you used _Private DNS_ with `<your-id>.dns.nextdns.io`, replace it with your Blokada DNS name, as in the [Android guide](../android-private-dns/). If you used the NextDNS app, uninstall it and install [Blokada 6](https://go.blokada.org/play_cloud) instead.

### iPhone и iPad

If you used the NextDNS app, uninstall it and install [Blokada 6](https://go.blokada.org/appstore). If you installed a NextDNS profile instead, remove it under _Settings → General → VPN & Device Management_, then follow the [Apple guide](../apple-devices/).

### Mac и Apple TV

Премахнете профила или приложението на NextDNS, след това инсталирайте профила на Blokada от [ръководството за Apple](../apple-devices/).

### Windows и Linux

Uninstall the NextDNS app if you use it. On Windows, replace the NextDNS server and DoH template with Blokada's, as in the [Windows guide](../windows-dns-over-https/). On Linux, replace the NextDNS server in systemd-resolved, as in the [Linux guide](../linux-dns-over-tls/).

### Браузъри

Ако сте задали `https://dns.nextdns.io/…` като _сигурен DNS_ на вашия браузър, заменете го с вашия DoH линк, както е описано в [ръководството за браузъри](../browser-dns-over-https/).

### Рутер

Ако вашият рутер използва NextDNS чрез DNS през TLS или DNS през HTTPS, заменете името или връзката на NextDNS с вашата на Blokada, както е описано в [ръководството за рутер](../router-ad-blocking/).

If it uses NextDNS through plain IP addresses with a _linked IP_, Blokada can't take that over yet. Support for routers with plain DNS addresses is on the way. Until then, set up your devices one by one, or use a router that supports encrypted DNS.

## Проверка дали работи

Open a few websites, then look at the _Activity_ page in the dashboard. You see your devices' lookups there, with blocked ones marked. If a device doesn't show up, it is still using NextDNS.
