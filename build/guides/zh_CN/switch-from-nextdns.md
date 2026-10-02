---
title: 一个在每台设备上使用相同设置的 NextDNS 替代方案
description: 从 NextDNS 迁移到 Blokada Cloud。将你的 NextDNS DNS 名称、DoH 链接或配置文件替换为 Blokada 的设置，适用于你的手机、电脑和路由器，并继续保持广告拦截。
updated: 2026-10-02​​
order: 3
---

NextDNS 和 Blokada Cloud 的工作方式相同：都是加密的 DNS 服务，通过名称拦截广告和追踪器，并在个人 DNS 名称后面使用你的自定义设置。切换意味着在每台设备上将 NextDNS 的设置替换为你的 Blokada 设置。设备上的其他内容不会发生变化。

## 你之前用过的，以及在 Blokada 中该选择什么

| 在 NextDNS 中            | 在 Blokada Cloud 中                                 |
| ---------------------- | ------------------------------------------------- |
| 你的配置 ID，例如 `abc123`    | 你的设备标签，是 Blokada DNS 名称和 DoH 链接的一部分               |
| _隐&#x79C1;_&#x5C4F;蔽列表 | 控制面板中&#x7684;_&#x5C4F;蔽列表_                        |
| _安全_（恶意软件、网络钓鱼）        | 控制面&#x677F;_&#x5C4F;蔽列&#x8868;_&#x4E0B;的恶意软件列表    |
| _家长控制_                 | 控制面&#x677F;_&#x5C4F;蔽列&#x8868;_&#x4E0B;的成人内容和赌博列表 |
| _允许列表_ 和 _拒绝列表_        | 控制面板中&#x7684;_&#x4F8B;外_                          |
| _日志_ 和 _分析_            | 控制面板中&#x7684;_&#x6D3B;&#x52A8;_&#x548C;_统计_       |

## 切换每台设备

根据您的设备，您需要您的 DNS 名称或 DoH 链接，这两项都可以在上方的 _您的详细信息_ 中找到。

### Android

如果你使用了 _私人 DNS_，地址为 `<your-id>.dns.nextdns.io`，请将其替换为你的 Blokada DNS 名称，具体请参见[Android 指南](../android-private-dns/)。如果你使用了 NextDNS 应用，请卸载并改为安装 [Blokada 6](https://go.blokada.org/play_cloud)。

### iPhone 和 iPad

如果你使用了 NextDNS 应用，请卸载并改为安装 [Blokada 6](https://go.blokada.org/appstore)。如果你安装的是 NextDNS 配置文件，请在 _设置 → 通用 → VPN 与设备管理_ 下将其移除，然后按照 [Apple 指南](../apple-devices/) 操作。

### Mac 和 Apple TV

移除 NextDNS 配置文件或应用，然后从 [Apple 指南](../apple-devices/) 安装 Blokada 配置文件。

### Windows 和 Linux

如果你正在使用 NextDNS 应用，请卸载它。在 Windows 上，将 NextDNS 服务器和 DoH 模板替换为 Blokada 的设置，具体请参见 [Windows 指南](../windows-dns-over-https/)。在 Linux 上，请将 systemd-resolved 中的 NextDNS 服务器替换为 Blokada 的，详见 [Linux 指南](../linux-dns-over-tls/)。

### 浏览器

如果你设定了 `https://dns.nextdns.io/…` 作为浏览器&#x7684;_&#x5B89;全 DNS_，请将其替换为你的 DoH 链接，详情参见[浏览器指南](../browser-dns-over-https/)。

### 路由器

如果你的路由器通过 DNS over TLS 或 DNS over HTTPS 使用 NextDNS，请将 NextDNS 名称或链接替换为你的 Blokada 设置，具体参见[路由器指南](../router-ad-blocking/)。

如果它通过普通 IP 地址&#x548C;_&#x7ED1;定 I&#x50;_&#x4F7F;用 NextDNS，目前 Blokada 还无法支持接管。对普通 DNS 地址路由器的支持即将推出。在此之前，请单独为你的设备进行设置，或使用支持加密 DNS 的路由器。

## 检查是否生效

打开几个网站，然后查看控制面板里&#x7684;_&#x6D3B;&#x52A8;_&#x9875;面。你可以在那里看到你的各个设备的解析记录，被拦截的会有标记。如果某台设备没有显示出来，说明它还在使用 NextDNS。
