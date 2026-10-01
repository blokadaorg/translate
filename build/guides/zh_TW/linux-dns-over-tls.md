---
title: 在 Linux 使用 DNS-over-TLS 阻擋廣告
description: 設置 systemd-resolved 以透過加密的 DNS-over-TLS 連接到 Blokada Cloud，並為您 Linux 電腦上的每個應用程式阻擋廣告和追蹤器。
updated: 2026-09-28
order: 9
---

目前大多數現代 Linux 發行版（包括 Ubuntu 和 Fedora）都通過 _systemd-resolved_ 解析名稱，並支援 DNS-over-TLS。在 Debian 上，先使用 `sudo apt install systemd-resolved` 安裝它。將其指向 Blokada Cloud，然後所有應用程式的廣告和追蹤器都會被阻擋。

## 設定 systemd-resolved

1. 使用 `sudo mkdir -p /etc/systemd/resolved.conf.d` 建立資料夾，然後建立設定檔 `/etc/systemd/resolved.conf.d/blokada.conf`，內容如下：

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns=\"dot\">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>重新啟動：<code>sudo systemctl restart systemd-resolved</code></li>
<li>檢查：<code>resolvectl status</code> 會顯示 <code>+DNSOverTLS</code> 和 Blokada 伺服器。</li>
</ol>

`#` 後面部分是您的 Blokada DNS 名稱：{% dot %} systemd-resolved 會檢查伺服器證書並對比名稱，Blokada 也會使用它來識別是哪個裝置正在查詢。

<div class="note">

**NetworkManager** 也會傳遞您網路上的 DNS 伺服器。 **NetworkManager** 也會傳遞您網路上的 DNS 伺服器。 `Domains=~.` 會將所有查詢傳送到 Blokada，但如果 `resolvectl status` 仍然在某個連線上列出其他伺服器，請關閉該連線的自動 DNS 分配（在 IPv4 和 IPv6 設定中的 _DNS_ 旁的 _自動_ 開關）。

</div>

## 未使用 systemd-resolved

如果找不到 `resolvectl`，您的發行版是用其他方式解析名稱。請改為在瀏覽器中設置安全的 DNS，參考[瀏覽器教學](../browser-dns-over-https/)，或設定[路由器](../router-ad-blocking/) 以全家共享。

## 檢查設定是否正常

開啟幾個網站，然後到 [儀表板](https://app.blokada.org/stats?src=guides) 的 _活動_ 頁面查看。這台電腦的 DNS 查詢會顯示在那裡。

<div class="note">

想讓這台電腦也有 VPN 嗎？ [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 包含 WireGuard 設定，可加密所有流量，並同時繼續阻擋廣告與追蹤器。 [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 包含 WireGuard 設定，可加密所有流量，並同時繼續阻擋廣告與追蹤器。

</div>
