---
title: Mullvad DNS is shutting down. Keep your ad blocking with Blokada Cloud
description: Mullvad closes its public DNS on 2 November 2026. Here is how to move your phone, computer and router to Blokada Cloud before then, without losing ad blocking.
updated: 2026-10-02
order: 2
---

Mullvad is closing its free public DNS service on **2 November 2026** and recommends Quad9 instead. Quad9 blocks malware but does **not** block ads or trackers. When Mullvad's DNS stops, devices set to it stop loading websites and apps. Where a device is allowed to fall back to another DNS server, ads come back instead. Switch before that date.

This page is about the public DNS names ending in `dns.mullvad.net`. It does not cover the Mullvad VPN app.

## Какво сте използвали и какво да изберете в Blokada

| Име на Mullvad DNS         | Какво блокира                                 | В таблото на Blokada                                                                                                                          |
| -------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | нищо                                          | Blokada is a filtering service. If you want no filtering, Quad9 or your provider's DNS is the simpler choice. |
| `adblock.dns.mullvad.net`  | реклами, тракери                              | списък за блокиране на реклами и тракери                                                                                                      |
| `base.dns.mullvad.net`     | реклами, тракери, зловреден софтуер           | добавяне на списък с вредоносен софтуер                                                                                                       |
| `extended.dns.mullvad.net` | основен плюс социални мрежи                   | добавяне на списък със социални медии                                                                                                         |
| `family.dns.mullvad.net`   | основен плюс съдържание за възрастни и хазарт | добавяне на списъци за съдържание за възрастни и хазарт                                                                                       |
| `all.dns.mullvad.net`      | всички изброени по-горе                       | включване на всички тях                                                                                                                       |

You choose blocklists in the dashboard under _Blocklists_. You can change them at any time, and the change applies to all your devices.

## Превключване на всяко устройство

Blokada gives each device its own name, so the dashboard can show activity per device. Depending on the device, you need your DNS name or your DoH link, both under _Your details_ above.

### Android

Mullvad's guide had you enter a hostname under _Private DNS_. Replace it with your Blokada DNS name. The [Android guide](../android-private-dns/) has the steps.

### iPhone, iPad и Mac

Mullvad's setup used a configuration profile. Remove it first:

- **iPhone и iPad:** _Настройки → Основни → VPN и управление на устройства_, докоснете DNS профила на Mullvad, след това _Премахване на профила_.
- **Mac:** отворете списъка с профили (_Системни настройки → Общи → Управление на устройства_ на macOS 15 и по-нови, _Системни настройки → Поверителност и сигурност → Профили_ на macOS 13 и 14, _Системни предпочитания → Профили_ на macOS 12 и по-стари), изберете профила Mullvad DNS и кликнете на _−_.

След това инсталирайте профила на Blokada от [ръководството за Apple](../apple-devices/).

### Браузъри

If you entered a Mullvad DoH link such as `https://adblock.dns.mullvad.net/dns-query` under _secure DNS_ or _DNS over HTTPS_, replace it with your DoH link. The [browser guide](../browser-dns-over-https/) has the steps for each browser.

### Рутер

If your router uses Mullvad over DNS over TLS, replace the Mullvad hostname with your Blokada DNS name, and remove Mullvad's IP addresses. The [router guide](../router-ad-blocking/) covers common models.

## Проверка дали работи

Open a few websites, then look at the _Activity_ page in the dashboard. You see your devices' lookups there, with blocked ones marked. If a device doesn't show up, it is still using another DNS server.
