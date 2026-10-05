---
title: Mullvad DNS 即将关闭。使用 Blokada Cloud 继续保持广告拦截
description: Mullvad 将于 2026 年 11 月 2 日关闭其公共 DNS。以下是如何在此日期前，将您的手机、电脑和路由器迁移至 Blokada Cloud，同时保持广告拦截功能。
updated: 2026-10-02
order: 2
---

Mullvad 将于 **2026 年 11 月 2 日** 关闭其免费公共 DNS 服务，并推荐使用 Quad9。Quad9 可以拦截恶意软件，但**不**拦截广告或跟踪器。当 Mullvad 的 DNS 停止工作时，设定为该 DNS 的设备将无法加载网站和应用。如果设备允许自动切换到其他 DNS 服务器，则广告会重新出现。请务必在该日期前切换。

本页面介绍以 `dns.mullvad.net` 结尾的公共 DNS 名称。不涉及 Mullvad VPN 应用程序。

## 您之前使用的，以及在 Blokada 里应选择的

| Mullvad DNS 名称             | 其拦截内容        | 在 Blokada 控制台                                         |
| -------------------------- | ------------ | ----------------------------------------------------- |
| `dns.mullvad.net`          | 无            | Blokada 是一个过滤服务。如果您不需要过滤，Quad9 或您的服务提供商的 DNS 是更简单的选择。 |
| `adblock.dns.mullvad.net`  | 广告、追踪器       | 广告和追踪器名单                                              |
| `base.dns.mullvad.net`     | 广告、追踪器、恶意软件  | 添加恶意软件名单                                              |
| `extended.dns.mullvad.net` | 基础内容加社交媒体    | 添加社交媒体名单                                              |
| `family.dns.mullvad.net`   | 基础内容加成人内容和赌博 | 添加成人内容和赌博名单                                           |
| `all.dns.mullvad.net`      | 涵盖以上所有       | 全部开启                                                  |

您可以在控制面板的 _Blocklists_ 下选择拦截列表。您可以随时更改，且更改将适用于您的所有设备。

## 切换每台设备

Blokada 会为每个设备分配独立的名称，因此控制面板可以显示每台设备的活动情况。根据设备类型，您需要使用您的 DNS 名称或 DoH 链接，二者均可在上方的 _Your details_ 下找到。

### Android

Mullvad 的指南要求您在 _Private DNS_ 下输入主机名。将其替换为您的 Blokada DNS 名称。[Android 指南](../android-private-dns/)介绍了具体步骤。

### iPhone、iPad 和 Mac

Mullvad 的设置使用了配置描述文件。请先将其移除：

- **iPhone 和 iPad：** _设置 → 通用 → VPN 与设备管理_，点击 Mullvad DNS 配置文件，然后选择 _移除配置文件_。
- **Mac：** 打开配置文件列表（macOS 15 及以上：_系统设置 → 通用 → 设备管理_；macOS 13 和 14：_系统设置 → 隐私与安全性 → 配置文件_；macOS 12 及以下：_系统偏好设置 → 配置文件_），选择 Mullvad DNS 配置文件并点击 _−_。

然后根据 [Apple 指南](../apple-devices/) 安装 Blokada 配置文件。

### 浏览器

如果您在 _secure DNS_ 或 _DNS over HTTPS_ 下输入了如 `https://adblock.dns.mullvad.net/dns-query` 的 Mullvad DoH 链接，请将其替换为您的 DoH 链接。[浏览器指南](../browser-dns-over-https/)中有对应浏览器的具体步骤。

### 路由器

如果您的路由器使用 Mullvad 的 DNS over TLS，请将 Mullvad 的主机名替换为您的 Blokada DNS 名称，并移除 Mullvad 的 IP 地址。[路由器指南](../router-ad-blocking/)涵盖常见型号。

## 请检查是否生效

打开几个网站后，在控制面板的 _Activity_ 页面查看。您可以在那里看到各设备的解析记录，被拦截的会有标记。如果某个设备未显示，说明它仍在使用其他 DNS 服务器。
