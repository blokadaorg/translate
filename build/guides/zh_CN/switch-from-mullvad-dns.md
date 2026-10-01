---
title: Mullvad DNS 即将停止服务。使用 Blokada Cloud 继续拦截广告
description: Mullvad 将于 2026 年 11 月 2 日关闭其公共 DNS 服务。以下是如何在此日期前将您的手机、电脑和路由器切换至 Blokada Cloud，确保广告拦截不中断。
updated: 2026-10-01‍
order: 2
---

Mullvad 将于 **2026 年 11 月 2 日** 关闭其免费公共 DNS 服务，并建议改用 Quad9。 Quad9 会拦截恶意软件，但**不会**拦截广告或追踪器。当 Mullvad 的 DNS 停止服务时，设置为该 DNS 的设备将无法加载网站和应用程序。如果设备允许自动切换到其他 DNS 服务器，则广告会重新出现。请在此日期之前切换。

本页面内容适用于以 `dns.mullvad.net` 结尾的公共 DNS 名称。不涵盖 Mullvad VPN 应用。

## 您之前使用的，以及在 Blokada 里应选择的

| Mullvad DNS 名称             | 其拦截内容        | 在 Blokada 控制台                                   |
| -------------------------- | ------------ | ----------------------------------------------- |
| `dns.mullvad.net`          | 无            | Blokada 是一项过滤服务。如果您不需要过滤，Quad9 或者您的服务商 DNS 更简单。 |
| `adblock.dns.mullvad.net`  | 广告、追踪器       | 广告和追踪器名单                                        |
| `base.dns.mullvad.net`     | 广告、追踪器、恶意软件  | 添加恶意软件名单                                        |
| `extended.dns.mullvad.net` | 基础内容加社交媒体    | 添加社交媒体名单                                        |
| `family.dns.mullvad.net`   | 基础内容加成人内容和赌博 | 添加成人内容和赌博名单                                     |
| `all.dns.mullvad.net`      | 涵盖以上所有       | 全部开启                                            |

您可在控制台的 _Blocklists_ 下选择拦截名单。您可随时更改，且更改会应用到所有设备。

## 您的 Blokada 信息

Blokada 会为每个设备分配唯一名称，控制台可显示每台设备的活动：

- 您的 Blokada DNS 名称，用于 DNS over TLS（Android、路由器）：{% dot %}
- 您的 DoH 链接，用于 DNS over HTTPS（浏览器、部分路由器）：{% doh %}

## 切换每台设备

### Android

Mullvad 指南中需在 _专用 DNS_ 下输入主机名。将其替换为您的 Blokada DNS 名称。请参阅 [Android 指南](../android-private-dns/)。

### iPhone、iPad 和 Mac

Mullvad 的设置内容使用了配置描述文件。请先移除：

- **iPhone 和 iPad：** _设置 → 通用 → VPN 与设备管理_，点击 Mullvad DNS 配置文件，然后选择 _移除配置文件_。
- **Mac：** 打开配置文件列表（macOS 15 及以上：_系统设置 → 通用 → 设备管理_；macOS 13 和 14：_系统设置 → 隐私与安全性 → 配置文件_；macOS 12 及以下：_系统偏好设置 → 配置文件_），选择 Mullvad DNS 配置文件并点击 _−_。

然后根据 [Apple 指南](../apple-devices/) 安装 Blokada 配置文件。

### 浏览器

如果您在 _安全 DNS_ 或 _DNS over HTTPS_ 输入了例如 `https://adblock.dns.mullvad.net/dns-query` 的 Mullvad DoH 链接，请替换为您的 DoH 链接。[浏览器指南](../browser-dns-over-https/) 提供了各浏览器的操作步骤。

### 路由器

如您的路由器使用 Mullvad 的 DNS over TLS，请将 Mullvad 主机名替换为您的 Blokada DNS 名称，并移除 Mullvad 的 IP 地址。[路由器指南](../router-ad-blocking/) 涵盖了常见型号。

## 请检查是否生效

打开几个网站，然后在控制台 _Activity_ 页面查看。您可以在此处看到设备的 DNS 查询，已拦截项会做标记。如果某台设备未显示，说明它仍在使用其他 DNS 服务器。
