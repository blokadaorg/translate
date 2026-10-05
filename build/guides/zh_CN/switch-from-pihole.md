---
title: 无需硬件的 Pi-hole 替代方案
description: 将你家的广告拦截从 Pi-hole 迁移到 Blokada Cloud，或者保留 Pi-hole 并通过 Blokada 发送其查询请求。
updated: 2026-10-02
order: 1
---

只要树莓派在运行、已更新且位于家中，Pi-hole 就能为你网络上的每台设备屏蔽广告。Blokada Cloud 则通过我们的服务器完成同样的任务：

- **无需维护硬件设备。** 无需 SD 卡，无需更新，树莓派宕机时也不会造成服务中断。
- **外出也可用。** 手机和笔记本电脑在移动数据和其它 Wi-Fi 网络下也能持续拦截广告。
- **加密传输。** 设备通过 DNS over TLS 或 DNS over HTTPS 与 Blokada 通信，你的供应商无法读取或修改你的查询请求。
- **统一管理面板。** 阻止列表、允许与阻止的域名，以及各设备的活动都可在 [app.blokada.org](https://app.blokada.org/?src=guides) 查看。

切换有两种方式。完全替换 Pi-hole，或保留 Pi-hole 并将 Blokada Cloud 作为其上游。

## 选项 1：完全替换 Pi-hole

1. **获取 Blokada Cloud** 并打开管理面板。你的 DNS 名称和 DoH 链接可在 _设置_ 以及上方的 _你的详细信息_ 中找到。
2. **将路由器指向 Blokada，而不是 Pi-hole。** 请按照[路由器指南](../router-ad-blocking/)进行操作。如果你的路由器只接受普通 IP 地址作为 DNS 服务器，请为每个设备单独设置：[Android](../android-private-dns/)、[Mac 与 Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/)，以及[浏览器](../browser-dns-over-https/)。
3. **如果你的 Pi-hole 是 DHCP 服务器，** 请在关闭 Pi 之前，提前在路由器中重新启用 DHCP。否则你的设备将无法获取网络地址。
4. **迁移你的列表。** 在管理面板选择 _阻止列表_ 下的 blocklists，然后在 _例外_ 下添加你自己的允许或阻止的域名。
5. **关闭 Pi-hole，** 或留作它用。

<div class="note aside">

你的 Pi-hole 通过 IP 地址显示网络上的每个设备。使用 Blokada 时，只要设备使用各自的 Blokada DNS 名称，每台设备都将以名称显示。若路由器配置为一个 Blokada DNS 名称，则该路由器会作为一个设备显示。

</div>

## 选项 2：保留 Pi-hole，并使用 Blokada Cloud 作为上游

如果你想保留本地设置，比如本地主机名、DHCP 或自定义列表，可以让 Pi-hole 通过加密连接将查询转发到 Blokada。Pi-hole 本身无法进行加密转发，因此需要有一个小型转发器在其旁运行。本指南使用 [dnsproxy](https://github.com/AdguardTeam/dnsproxy)，这是一个开源且仅有单一文件的转发器。

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
4. 在 Pi-hole 管理界面中，打开 _设置 → DNS_。取消勾选所有上游服务器，并添加 `127.0.0.1#5054` 作为自定义上游服务器。保存。
5. 在管理面板的 _活动_ 页面检查。你网络的查询现在会显示在这里。

你可以关闭 Pi-hole 自带的阻止列表并在管理面板管理拦截，也可以两者同时使用。

## 常见问题

**我需要 Blokada Plus 吗？** 不需要。Blokada Cloud 已覆盖你整个家庭的 DNS 屏蔽。[Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 则额外提供 VPN 功能。

**如果 Blokada 无法连接怎么办？** 你的设备将在 Blokada 恢复前无法解析域名，就像 Pi-hole 离线时一样。不要添加第二个未过滤的 DNS 服务器作为备选。大多数设备会随机使用所有 DNS 服务器，这会导致广告漏过屏蔽。
