---
title: 一个在每台设备上使用相同设置的 NextDNS 替代方案
description: 从 NextDNS 迁移到 Blokada Cloud。在您的手机、电脑和路由器上将 NextDNS 的 DNS 名称、DoH 链接或配置文件替换为 Blokada 的对应内容，保持广告拦截功能不变。
updated: 2026-10-02​​
order: 3
---

NextDNS 和 Blokada Cloud 的工作方式相同：均为加密 DNS 服务，按名称拦截广告和跟踪器，并通过专属 DNS 名称进行您的个性化设置。切换只需在每个设备上将 NextDNS 的相关配置替换为 Blokada 的即可，设备上的其他内容无需更改。

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

如果您使用了 _私有 DNS_ 并设置了 `<your-id>.dns.nextdns.io`，请用您的 Blokada DNS 名称进行替换，具体可参考[Android 指南](../android-private-dns/)。如果您使用了 NextDNS 应用，请卸载它，并改为安装 [Blokada 6](https://go.blokada.org/play_cloud)。

### iPhone 和 iPad

如果您使用了 NextDNS 应用，请卸载它并安装 [Blokada 6](https://go.blokada.org/appstore)。如果您是安装的 NextDNS 配置文件，请在 _设置 → 通用 → VPN 与设备管理_ 中将其移除，然后按[Apple 设备指南](../apple-devices/)操作。

### Mac 和 Apple TV

移除 NextDNS 配置文件或应用，然后从 [Apple 指南](../apple-devices/) 安装 Blokada 配置文件。

### Windows 和 Linux

如有使用 NextDNS 应用，请卸载。在 Windows 上，将 NextDNS 服务器和 DoH 模板替换为 Blokada 的，具体操作请参考[Windows 指南](../windows-dns-over-https/)。在 Linux 上，将 systemd-resolved 中的 NextDNS 服务器替换为 Blokada 的，请参考[Linux 指南](../linux-dns-over-tls/)。

### 浏览器

如果你设定了 `https://dns.nextdns.io/…` 作为浏览器&#x7684;_&#x5B89;全 DNS_，请将其替换为你的 DoH 链接，详情参见[浏览器指南](../browser-dns-over-https/)。

### 路由器

如果你的路由器通过 DNS over TLS 或 DNS over HTTPS 使用 NextDNS，请将 NextDNS 名称或链接替换为你的 Blokada 设置，具体参见[路由器指南](../router-ad-blocking/)。

如果您的路由器通过带有 _关联 IP_ 的纯 IP 地址使用 NextDNS，目前 Blokada 暂不支持该方式。Blokada 对仅支持纯 DNS 地址的路由器的支持即将推出。在此之前，请逐一为您的设备设置，或使用支持加密 DNS 的路由器。

## 检查是否生效

打开几个网站，然后在仪表板的 _活动_ 页面查看。您可以看到各设备的查询记录，被拦截的会有明显标记。如果某个设备没有显示，说明它依然在使用 NextDNS。
