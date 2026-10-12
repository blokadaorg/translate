---
title: 使用路由器广告拦截在整个网络上屏蔽广告
description: 只需在路由器上设置一次 Blokada Cloud，家中所有设备都能获得保护，包括无法运行广告拦截器的电视、游戏主机和智能音箱。
updated: 2026-10-09
order: 4
---

你网络中的每个设备都会向路由器请求使用哪个 DNS 服务器。将路由器指向 Blokada Cloud，路由器后面的所有设备（包括智能电视、游戏主机、流媒体棒和智能家居设备，这些设备无法单独安装广告拦截应用）都能实现广告和跟踪器的屏蔽。

## 你的路由器所需条件

有两种方式可以设置路由器：

- **使用带主机名的加密DNS**，即通过TLS的DNS（DoT）或通过HTTPS的DNS（DoH）。许多新款路由器都支持这一功能，包括下方列出的型号。根据您的路由器支持的类型，您需要输入DNS名称或DoH链接，这些信息可在上&#x65B9;_&#x60A8;的详细信&#x606F;_&#x4E2D;找到。
- **纯IPv6 DNS地址。** 许多互联网供应商的路由器只接受作为DNS的纯IP地址。如果您的路由器只接受IP，并且您的连接支持IPv6，Blokada会提供一个IPv6地址供您输入。请参见[仅接受IP地址的路由器](#routers-that-only-take-an-ip-address)。

如果您的路由器支持，请使用加密DNS。这样的查询在传输到Blokada的过程中将保持隐私。

## FRITZ!Box

FRITZ!OS 7.20 或更高版本。

1. 打开 `http://fritz.box` 并进入 _Internet → 帐号信息 → DNS 服务器_。
2. &#x5728;_&#x49;nternet 上的加密名称解析（DNS over TLS）_下，勾&#x9009;_&#x4F7F;用加密名称解析_。
3. &#x5728;_&#x44;NS 服务器的已解析名&#x79F0;_&#x4E2D;，只输入 {% dot %}。**移除所有其他条目。** FRITZ!Box 会使用所有列出的解析器，任何其他条目都会让广告通过。
4. 勾选强制证书验证的选项，取消勾选允许回退到未加密名称解析的选项。
5. 如果您看到 _DNS中断时切换到公共DNS服务器_，请将其关闭。
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

1. &#x5728;_系统 → 软&#x4EF6;_&#x4E2D;，更新列表并安装 `luci-app-https-dns-proxy`。
2. 打&#x5F00;_&#x670D;务 → HTTPS DNS 代理_。删除其他供应商的实例。
3. 添加一个自定义解析器 URL 的实例：{% doh %}
4. _保存并应用_。该软件包会自动将 dnsmasq 指向此地址。

## 其他路由器

查找名为 _DNS over TLS_、_Private DNS_、_Encrypted DNS_ 或 _DNS over HTTPS_ 的设置。输入上面的 Blokada DNS 名称或 DoH 链接，并移除所有其他 DNS 服务器，包括备用服务器。如果没有这些设置，请使用下方提供的普通 IPv6 地址。

## 仅支持输入 IP 地址的路由器

为此，您的路由器和网络连接需要支持 IPv6。对仅支持 IPv4 地址的支持将在后续推出。

1. 在 [仪表盘](https://app.blokada.org/setup?src=guides) 中，打开 _设置_ 并选择 _路由器、电视、游戏主机_。
2. 为路由器命名，例如 _家庭路由器_，然后选择 _获取地址_。该名称会显示在您的活动中，且之后无法更改。
3. 在路由器的设置中，找到 IPv6 的 DNS 服务器，通常位于 _Internet_、_WAN_ 或 _IPv6_ 下，将该地址作为唯一的 DNS 服务器填写。
4. **移除所有其他 DNS 服务器，包括 IPv4 的。** 如果设备仍然从路由器获取到 IPv4 DNS 服务器，一些查询将绕过 Blokada。如果路由器无法将 IPv4 DNS 留空，请分别在每台设备上单独设置：[Android](../android-private-dns/)、[Mac 和 Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/) 以及 [浏览器](../browser-dns-over-https/)。

对于允许手动输入 DNS 服务器的电视或游戏主机，也可以采用相同设置。为每台设备分配独立的地址，这样它们将在您的活动中以名称显示。

<div class="note aside">

这些查询会以未加密形式发送到 Blokada，就像普通 DNS 服务器一样。如果路由器支持 DNS over TLS 或 DNS over HTTPS，请优先使用这些加密方式。

</div>

## 检查其是否正常工作

1. 重启一台设备，或将其 Wi-Fi 关闭再打开，使其获取更改。
2. 在该设备上关闭 Blokada（如果正在运行），然后打开 [go.blokada.org/test](https://go.blokada.org/test)。它会显示您的 DNS 是否通过 Blokada。
3. 浏览片刻后，打开 [仪表盘](https://app.blokada.org/stats?src=guides) 的 _活动_ 页面。您的网络查询会显示在这里。

## 如果部分设备仍然显示广告

有些设备会绕过路由器：如设置&#x4E86;_&#x79C1;有 DN&#x53;_&#x7684;手机、&#x5C06;_&#x5B89;全 DN&#x53;_&#x8BBE;置为其他供应商的浏览器，以及硬编码其自身 DNS 的设备。请在设备上单独设置，或关闭它们自身的 DNS 设置。

<div class="note tip">

在路由器后面，所有设备共用一个地址，所以仪表盘会将你的网络显示为单一设备。如果你希望分别查看手机与电脑的数据，可以为设备单独设置各自的 Blokada DNS 名称。这样，它们离开家时也会继续屏蔽广告。

</div>
