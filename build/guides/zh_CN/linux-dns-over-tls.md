---
title: 在 Linux 上使用 DNS over TLS 屏蔽广告
description: 配置 systemd-resolved 通过加密的 DNS over TLS 使用 Blokada Cloud，为你的 Linux 电脑上的每个应用程序屏蔽广告和跟踪器。
updated: 2026-10-02
order: 9
---

目前大多数 Linux 发行版，包括 Ubuntu 和 Fedora，都是通过 _systemd-resolved_ 进行名称解析的，它支持 DNS over TLS。在 Debian 上，首先用 `sudo apt install systemd-resolved` 安装它。将其指向 Blokada Cloud 后，电脑上所有应用的广告和跟踪器都会被屏蔽。

## 设置 systemd-resolved

1. 用 `sudo mkdir -p /etc/systemd/resolved.conf.d` 创建文件夹，然后新建文件 `/etc/systemd/resolved.conf.d/blokada.conf`，内容如下：

<pre><code>[Resolve]\nDNS={{ site.dnsIps.dot }}#<span data-dns=\"dot\">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>\nDNSOverTLS=yes\nDomains=~.</code></pre>

<ol start="2">
<li>重启它：<code>sudo systemctl restart systemd-resolved</code></li>
<li>检查状态：<code>resolvectl status</code> 应显示 <code>+DNSOverTLS</code> 以及 Blokada 服务器。</li>
</ol>

`#` 号后的部分是你的 Blokada DNS 名称：{% dot %} systemd-resolved 会根据它检查服务器证书，Blokada 会用它识别是哪台设备在请求。

<div class="note important">

**NetworkManager** 同样会传递你网络的 DNS 服务器。`Domains=~.` 会将所有查询发送至 Blokada，但如果 `resolvectl status` 在某个连接上仍然显示了其他服务器，请为该连接关闭自动 DNS（在其 IPv4 和 IPv6 设置中 _DNS_ 旁的 _自动_ 开关）。

</div>

## 未使用 systemd-resolved

如果找不到 `resolvectl` 命令，说明你的发行版使用了其他方式进行名称解析。请改为在浏览器中设置安全 DNS，具体请参见[浏览器指南](../browser-dns-over-https/)，或者设置你的[路由器](../router-ad-blocking/)以覆盖整个家庭。

## 检查是否生效

打开几个网站，然后在[仪表板](https://app.blokada.org/stats?src=guides)的 _活动_ 页面查看。这台计算机的查询会显示在该处。

<div class="note aside">

想在这台计算机上也使用 VPN？[Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 包含 WireGuard 配置，可以加密所有流量，并保持相同的拦截效果。

</div>
