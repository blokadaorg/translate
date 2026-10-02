---
title: 无需硬件的 Pi-hole 替代方案
description: 将你家的广告拦截从 Pi-hole 迁移到 Blokada Cloud，或者保留 Pi-hole 并通过 Blokada 发送其查询请求。
updated: 2026-10-02
order: 1
---

只要 Raspberry Pi 正常运行、已更新且在家，Pi-hole 会为你网络上的每台设备拦截广告。 Blokada Cloud 通过我们的服务器实现同样的功能：

- **无需维护硬件设备。** 无需 SD 卡，无需更新，树莓派宕机时也不会造成服务中断。
- **外出也可用。** 手机和笔记本电脑在移动数据和其它 Wi-Fi 网络下也能持续拦截广告。
- **加密传输。** 设备通过 DNS over TLS 或 DNS over HTTPS 与 Blokada 通信，你的供应商无法读取或修改你的查询请求。
- **统一管理面板。** 阻止列表、允许与阻止的域名，以及各设备的活动都可在 [app.blokada.org](https://app.blokada.org/?src=guides) 查看。

有两种切换方式。完全替换 Pi-hole，或者保留并将 Blokada Cloud 作为上游。

## 选项 1：完全替换 Pi-hole

1. **获取 Blokada Cloud** 并打开管理面板。您的 DNS 名称和 DoH 链接位于 _设置_ 中，以及在上面的 _您的详细信息_ 中。
2. **将你的路由器指向 Blokada，而不是 Pi-hole。** 按照[路由器指南](../router-ad-blocking/)操作。如果你的路由器只接受纯 IP 地址作为 DNS 服务器，请改为逐个配置你的设备：[Android](../android-private-dns/)、[Mac 和 Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/)、以及[浏览器](../browser-dns-over-https/)。
3. **如果你的 Pi-hole 充当 DHCP 服务器，** 请在关闭 Pi 之前，先在路由器里重新启用 DHCP。否则你的设备将无法获取网络地址。
4. **迁移你的列表。** 在管理面板选择 _阻止列表_ 下的 blocklists，然后在 _例外_ 下添加你自己的允许或阻止的域名。
5. **关闭 Pi-hole，** 或留作它用。

<div class="note aside">

你的 Pi-hole 以前通过 IP 地址显示网络中每台设备。使用 Blokada，每台设备只要使用自己的 Blokada DNS 名称，就会以各自的名称显示。用同一个 Blokada DNS 名称设置的路由器会以单一设备显示。

</div>

## 选项 2：保留 Pi-hole，并使用 Blokada Cloud 作为上游

如果你需要保留本地设置，例如本地主机名、DHCP 或自定义列表，可以让 Pi-hole 通过加密连接将查询转发到 Blokada。 Pi-hole 本身无法实现加密转发，因此需要在其旁边运行一个小型转发器。本指南使用 [dnsproxy](https://github.com/AdguardTeam/dnsproxy)，这是一个开源的单文件转发器。

1. 在 Pi-hole 设备上，从其发布页面下载适合你 CPU 的 `dnsproxy` 版本（例如新版树莓派使用 `linux-arm64`），并将 `dnsproxy` 二进制文件复制到 `/usr/local/bin/`。
2. 创建 `/etc/systemd/system/dnsproxy.service`：

<pre><code>[Unit]
Description=加密 DNS 转发器到 Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. 启动：`sudo systemctl enable --now dnsproxy`
4. 在 Pi-hole 管理端，打开 _设置 → DNS_。取消勾选所有上游服务器，并添加 `127.0.0.1#5054` 作为自定义上游服务器。保存。
5. 查看管理面板的 _活动_ 页面。现在你网络中的查询将在此处显示。

你可以关闭 Pi-hole 自带的阻止列表并在管理面板管理拦截，也可以两者同时使用。

## 常见问题

**我需要 Blokada Plus 吗？** 不需要。 Blokada Cloud 覆盖你整个家庭的 DNS 拦截。 [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 还可进一步为你提供 VPN 服务。

**如果 Blokada 无法访问怎么办？** 你的设备将无法解析域名，直到服务恢复，就像 Pi-hole 宕机时一样。请勿添加第二个未过滤的 DNS 服务器作为备用。大多数设备会随机使用所有服务器，因此广告可能会穿透拦截。
