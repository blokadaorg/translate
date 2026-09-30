---
title: 使用路由器广告拦截在整个网络上屏蔽广告
description: 只需在路由器上设置一次 Blokada Cloud，家中所有设备都能获得保护，包括无法运行广告拦截器的电视、游戏主机和智能音箱。
updated: 2026-09-23
order: 4
---

你网络中的每台设备都会请求路由器指定 DNS 服务器。将路由器指向 Blokada Cloud，所有连接其后的设备的广告和跟踪器都会被屏蔽。这包括智能电视、游戏主机、流媒体棒和智能家居设备，这些设备无法安装广告拦截 App。

## 你的路由器所需条件

你的路由器必须支持**使用主机名的加密 DNS**，也就是支持 DNS over TLS（DoT）或 DNS over HTTPS（DoH）。许多新款路由器都支持，包括下列机型。根据你的路由器支持的内容，你需要：

- 对于 DNS over TLS，请使用你的 Blokada DNS 名称：{% dot %}
- 对于 DNS over HTTPS，请使用你的 DoH 链接：{% doh %}

<div class="note">

**仅支持纯 IP 地址？** 许多互联网运营商提供的路由器只接受作为 DNS 的纯 IP 地址。对此的支持正在开发中。在此之前，请逐一为你的设备进行设置：[Android](../android-private-dns/)、[Mac 和 Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/) 和 [浏览器](../browser-dns-over-https/)。你也可以按照 [Pi-hole 指南](../switch-from-pihole/) 在树莓派上运行一个小型转发器。

</div>

## FRITZ!Box

FRITZ!OS 7.20 或更高版本。

1. 打开 `http://fritz.box` 并进入 _Internet → 帐号信息 → DNS 服务器_。
2. &#x5728;_&#x49;nternet 上的加密名称解析（DNS over TLS）_下，勾&#x9009;_&#x4F7F;用加密名称解析_。
3. 勾&#x9009;_&#x5F3A;制为加密名称解析验证证书_。
4. 取消勾&#x9009;_&#x5141;许回退到非加密名称解析_。
5. &#x5728;_&#x89E3;析器名&#x79F0;_&#x4E2D;，只输入 {% dot %}。**移除所有其他条目。** FRITZ!Box 会使用列出的所有解析器，任何其他条目都会让广告通过。
6. 点&#x51FB;_&#x5E94;用_。

## 华硕（ASUS）

近期的 ASUS 固件（3.0.0.4.388 或以上）及 Asuswrt-Merlin。

1. 打开路由器管理页面并进入 _WAN → Internet 连接_。
2. &#x5728;_&#x57;AN DNS 设&#x7F6E;_&#x4E0B;，&#x5C06;_&#x44;NS 隐私协&#x8BAE;_&#x8BBE;置&#x4E3A;_&#x44;NS-over-TLS (DoT)_，_DNS-over-TLS 配&#x7F6E;_&#x8BBE;&#x4E3A;_&#x4E25;格_。
3. &#x4ECE;_&#x44;NS-over-TLS 服务器列&#x8868;_&#x4E2D;移除所有条目，然后添加一个：
   - 地址：{% ip \"dot\" %}
   - TLS 主机名：{% dot %}
4. 点&#x51FB;_&#x5E94;用_。

## OpenWrt

1. &#x5728;_&#x7CFB;统 → 软&#x4EF6;_&#x4E2D;，更新列表并安装 `luci-app-https-dns-proxy`。
2. 打&#x5F00;_&#x670D;务 → HTTPS DNS Proxy_。删除其他供应商的实例。
3. 添加一个自定义解析器 URL 的实例：{% doh %}
4. _保存并应用_。该软件包会自动将 dnsmasq 指向它。

## 其他路由器

请查找名为 _DNS over TLS_、_Private DNS_、_加密 DNS_ 或 _DNS over HTTPS_ 的设置。输入上方你的 Blokada DNS 名称或 DoH 链接，并移除所有其他 DNS 服务器，包括备用服务器。

## 检查其是否正常工作

1. 重启一台设备，或将其 Wi-Fi 关闭再打开，使其获取更改。
2. 浏览片刻，然后在仪表板中打&#x5F00;_&#x6D3B;&#x52A8;_&#x9875;面。你网络的查询会显示在这里。

有些设备会绕过路由器：设置&#x4E86;_&#x50;rivate DNS_ 的手机，设置成其他提供&#x5546;_&#x5B89;全 DNS_ 的浏览器，以及内嵌指定 DNS 的设备。请在设备上单独设置，或关闭设备自身的 DNS 设置。

<div class="note">

在路由器下，所有设备共用一个地址，因此仪表板会将你的网络显示为一台设备。如果你希望分别看到每台设备，请为手机和笔记本配置独立的 Blokada DNS 名称。它们离开家时也会继续拦截广告。

</div>
