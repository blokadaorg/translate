---
title: 使用 DNS over HTTPS 在 Windows 上屏蔽广告
description: 利用 Windows 11 内置的加密 DNS 搭配 Blokada Cloud，在每个应用和浏览器中屏蔽广告与跟踪器，无需安装任何软件。
updated: 2026-10-01
order: 8
---

Windows 11 可以通过 DNS over HTTPS 加密发送所有的 DNS 查询。将其指向 Blokada Cloud，广告和跟踪器将在电脑上的所有应用和浏览器中被屏蔽，无需安装任何内容。

你需要两个数值：

- DNS 服务器（IP 地址）：{% ip "doh" %}
- 你的 DoH 链接：{% doh %}

## Windows 11

1. 打开 _设置 → 网络和 Internet_，然后根据电脑的连接方式选择 _Wi-Fi_ 或 _以太网_。
2. 打开你连接&#x7684;_&#x786C;件属性_。对于 Wi-Fi，选&#x62E9;_&#x7BA1;理已知网&#x7EDC;_&#x5E76;选中相应网络，或在 Wi-Fi 页面顶部选&#x62E9;_&#x786C;件属性_。
3. &#x5728;_&#x44;NS 服务器分&#x914D;_&#x65C1;，选&#x62E9;_&#x7F16;辑_。选&#x62E9;_&#x624B;动_，并开&#x542F;_&#x49;Pv4_。
4. &#x5728;_&#x9996;选 DN&#x53;_&#x4E2D;，输入 DNS 服务器 {% ip "doh" %}
5. &#x5C06;_&#x44;NS over HTTP&#x53;_&#x8BBE;置&#x4E3A;_&#x5F00;启（手动模板）_，并将你的 DoH 链接 {% doh %} 粘贴&#x4E3A;_&#x44;oH 模板_。
6. 关&#x95ED;_&#x56DE;退到明文_，然后选&#x62E9;_&#x4FDD;存_。

如果电脑同时使用 Wi-Fi 和以太网，请为另一个连接重复以上步骤。

<div class="note">

&#x5C06;_&#x5907;用 DN&#x53;_&#x7559;空。 Windows 会使用两个服务器，任何其他服务器都会导致广告通过。

没有 _开启（手动模板）_ 选项？你的 Windows 11 版本较旧。请更新 Windows，或者暂时使用[浏览器指南](../browser-dns-over-https/)。

如果在使用 IPv6 的网络中仍然有广告没有被屏蔽，Windows 也可能在请求你路由器的 IPv6 DNS 服务器。在适配器属性中关&#x95ED;_&#x49;nternet 协议版本 6 (TCP/IPv6)_（_控制面板 → 网络连接_），或设置你的[路由器](../router-ad-blocking/)。

</div>

## Windows 10

Windows 10 没有内置加密 DNS。请在浏览器内设置安全 DNS，参见[浏览器指南](../browser-dns-over-https/)，或设置你的[路由器](../router-ad-blocking/)来覆盖全屋。

## 检查是否有效

打开几个网站，然后在[控制台](https://app.blokada.org/stats?src=guides)&#x7684;_&#x6D3B;&#x52A8;_&#x9875;面查看。此电脑的查询将在那里显示。

Chrome 和 Edge 有各自&#x7684;_&#x5B89;全 DN&#x53;_&#x8BBE;置，会绕过 Windows。如保持自动模式，可能会回落到普通 DNS，这会被 Blokada 拒绝。请将其设置为你的 DoH 链接：

- **Chrome：** 打开 `chrome://settings/security`，开启 _使用安全 DNS_，&#x5728;_&#x9009;择 DNS 提供&#x5546;_&#x4E0B;选&#x62E9;_&#x6DFB;加自定义 DNS 服务提供商_。
- **Edge：** 打开 `edge://settings/privacy`，开启安全 DNS，然后选&#x62E9;_&#x9009;择服务提供商_。

然后粘贴你的 DoH 链接 {% doh %}

<div class="note">

想在这台电脑上也使用 VPN 吗？ [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 包含 WireGuard 配置，可以加密全部流量，并同样进行屏蔽。

</div>
