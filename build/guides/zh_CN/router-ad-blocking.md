---
title: 使用路由器广告拦截在整个网络上屏蔽广告
description: 只需在路由器上设置一次 Blokada Cloud，家中所有设备都能获得保护，包括无法运行广告拦截器的电视、游戏主机和智能音箱。
updated: 2026-10-02
order: 4
---

你网络中的每个设备都会向路由器请求使用哪个 DNS 服务器。将路由器指向 Blokada Cloud，路由器后面的所有设备（包括智能电视、游戏主机、流媒体棒和智能家居设备，这些设备无法单独安装广告拦截应用）都能实现广告和跟踪器的屏蔽。

## 你的路由器所需条件

你的路由器必须支持**带主机名的加密 DNS**，即 DNS-over-TLS (DoT) 或 DNS-over-HTTPS (DoH)。许多新款路由器都支持，包括下方列出的型号。根据你的路由器支持的类型，你需要你的 DNS 名称或 DoH 链接，这些都在上&#x65B9;_&#x4F60;的详&#x60C5;_&#x4E2D;。

<div class="note important">

**只支持普通 IP 地址？** 许多网络运营商的路由器只允许为 DNS 填写纯 IP 地址。对这些情况的支持正在开发中。在此之前，请逐个为你的设备进行配置：[Android](../android-private-dns/)、[Mac 和 Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/) 和 [浏览器](../browser-dns-over-https/)。你也可以按照 [Pi-hole 指南](../switch-from-pihole/) 中的说明，在树莓派上运行一个小型转发程序。

</div>

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

查找名&#x4E3A;_&#x44;NS over TLS_、_私有 DNS_、_加密 DN&#x53;_&#x6216;_DNS over HTTP&#x53;_&#x7684;设置。输入你上方获取的 Blokada DNS 名称或 DoH 链接，并移除所有其他 DNS 服务器，包括备用服务器。

## 检查其是否正常工作

1. 重启一台设备，或将其 Wi-Fi 关闭再打开，使其获取更改。
2. 浏览一分钟，然后在仪表盘中打&#x5F00;_&#x6D3B;&#x52A8;_&#x9875;面。你的网络查询会显示在那里。

## 如果部分设备仍然显示广告

有些设备会绕过路由器：如设置&#x4E86;_&#x79C1;有 DN&#x53;_&#x7684;手机、&#x5C06;_&#x5B89;全 DN&#x53;_&#x8BBE;置为其他供应商的浏览器，以及硬编码其自身 DNS 的设备。请在设备上单独设置，或关闭它们自身的 DNS 设置。

<div class="note tip">

在路由器后面，所有设备共用一个地址，所以仪表盘会将你的网络显示为单一设备。如果你希望分别查看手机与电脑的数据，可以为设备单独设置各自的 Blokada DNS 名称。这样，它们离开家时也会继续屏蔽广告。

</div>
