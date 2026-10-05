---
title: 使用 DNS over HTTPS 在 Windows 上屏蔽广告
description: 利用 Windows 11 内置的加密 DNS 搭配 Blokada Cloud，在每个应用和浏览器中屏蔽广告与跟踪器，无需安装任何软件。
updated: 2026-10-02
order: 8
---

Windows 11 可以将所有的 DNS 查询通过 DNS over HTTPS 加密发送。将其指向 Blokada Cloud，即可在计算机上的所有应用和浏览器中屏蔽广告和追踪器，无需安装任何软件。

您需要DNS服务器的IP地址和您的DoH链接，这两项都在上方&#x7684;_&#x60A8;的详细信&#x606F;_&#x4E0B;可找到。

## Windows 11

1. 打开 _设置 → 网络和 Internet_，然后根据电脑的连接方式选择 _Wi-Fi_ 或 _以太网_。
2. 打开您的连接&#x7684;_&#x786C;件属性_。对于 Wi-Fi，请选&#x62E9;_&#x7BA1;理已知网络_，然后选择对应网络，或在 Wi-Fi 页面顶部选&#x62E9;_&#x786C;件属性_。
3. &#x5728;_&#x44;NS 服务器分&#x914D;_&#x65C1;边，选&#x62E9;_&#x7F16;辑_。选&#x62E9;_&#x624B;&#x52A8;_&#x5E76;开&#x542F;_&#x49;Pv4_。
4. &#x5728;_&#x9996;选 DN&#x53;_&#x4E2D;，输入 DNS 服务器 {% ip "doh" %}
5. &#x5C06;_&#x44;NS over HTTP&#x53;_&#x8BBE;置&#x4E3A;_&#x5F00;启（手动模板）_，并将你的 DoH 链接 {% doh %} 粘贴&#x4E3A;_&#x44;oH 模板_。
6. 关&#x95ED;_&#x56DE;退到明文_，然后选&#x62E9;_&#x4FDD;存_。

如果电脑同时使用 Wi-Fi 和以太网，请为另一个连接重复以上步骤。

<div class="note important">

请&#x5C06;_&#x5907;用 DN&#x53;_&#x7559;空。Windows 会同时使用两个服务器，任何其他服务器都可能让广告通过。

</div>

<div class="note tip">

没有\*开启（手动模板）\*选项？您的 Windows 11 版本较旧。请更新 Windows，或暂时使用[浏览器指南](../browser-dns-over-https/)。

</div>

## Windows 10

Windows 10 没有内置的加密 DNS。请按照[浏览器指南](../browser-dns-over-https/)在您的浏览器内设置安全 DNS，或设置[路由器](../router-ad-blocking/)以保护整个家庭网络。

## 检查是否有效

打开几个网站，然后在 [仪表板](https://app.blokada.org/stats?src=guides) &#x7684;_&#x6D3B;&#x52A8;_&#x9875;面查看。这台电脑的查询会显示在那里。

<div class="note aside">

也想让这台电脑使用 VPN 吗？[Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 包含 WireGuard 配置，可以对所有流量进行加密，并具有相同的屏蔽效果。

</div>

## 如果有内容无法正常工作

Chrome 和 Edge 有各自&#x7684;_&#x5B89;全 DN&#x53;_&#x8BBE;置，可以绕过 Windows。若保持自动设置，可能会回退到普通 DNS，而 Blokada 会拒绝此操作。请将其设置为您的 DoH 链接：

- **Chrome：** 打开 `chrome://settings/security`，开启 _使用安全 DNS_，&#x5728;_&#x9009;择 DNS 提供&#x5546;_&#x4E0B;选&#x62E9;_&#x6DFB;加自定义 DNS 服务提供商_。
- **Edge：** 打开 `edge://settings/privacy`，开启安全 DNS，然后选&#x62E9;_&#x9009;择服务提供商_。

然后粘贴你的 DoH 链接 {% doh %}

如果在启用 IPv6 的网络上仍有部分广告漏过，Windows 可能也在请求路由器的 IPv6 DNS 服务器。请在适配器属性中关&#x95ED;_&#x49;nternet 协议版本 6 (TCP/IPv6)_（_控制面板 → 网络连接_），或设置[路由器](../router-ad-blocking/)。
