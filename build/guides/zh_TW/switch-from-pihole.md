---
title: 無需硬體的 Pi-hole 替代方案
description: 將您家中的廣告阻擋從 Pi-hole 遷移到 Blokada Cloud，或保留 Pi-hole 並將其查詢通過 Blokada 傳送。
updated: 2026-10-01
order: 1
---

只要 Raspberry Pi 處於開機、更新且在家中，Pi-hole 會為您網路上的每個裝置阻擋廣告。 Blokada Cloud 會從我們的伺服器執行相同的工作：

- **無需維護盒子。** 沒有 SD 卡，沒有更新，當 Pi 掛掉時也不會中斷服務。
- **外出也能運作。** 手機與筆電連接行動數據與其他 Wi-Fi 網路時仍可阻擋廣告。
- **加密連線。** 裝置透過 DNS over TLS 或 DNS over HTTPS 連接 Blokada，因此您的服務提供商無法讀取或更改查詢內容。
- **統一儀表板。** 可在 [app.blokada.org](https://app.blokada.org/?src=guides) 查看阻擋清單、允許與已阻擋網域、以及各裝置的活動紀錄。

有兩種切換方式。可以完全取代 Pi-hole，或保留並將 Blokada Cloud 設為其上游。

## 選項 1：取代 Pi-hole

1. **取得 Blokada Cloud** 並開啟儀表板。在 _設定_ 頁籤下您可以找到詳細資訊：
   - 您的 Blokada DNS 名稱，供 DNS over TLS 使用：{% dot %}
   - 您的 DoH 連結，供 DNS over HTTPS 使用：{% doh %}
2. **將您的路由器指向 Blokada 而不是 Pi-hole。** 請參考[路由器指南](../router-ad-blocking/)。如果您的路由器僅能接受純 IP 位址當成 DNS 伺服器，請改為分別設定各裝置：[Android](../android-private-dns/)、[Mac 與 Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/)，以及[瀏覽器](../browser-dns-over-https/)。
3. **如果您的 Pi-hole 是 DHCP 伺服器，** 在關掉 Pi 之前請先於路由器重新啟用 DHCP。否則您的裝置將無法取得網路位址。
4. **搬移您的清單。** 在儀表板中於 _阻擋清單_ 選擇阻擋清單，並在 _例外_ 中新增您允許或已阻擋的網域。
5. **關閉 Pi-hole，** 或保留作為其他用途。

<div class="note">

您的 Pi-hole 以 IP 位址顯示網路中每個裝置。在 Blokada 中，只要裝置使用其自己的 Blokada DNS 名稱，就會以各自名稱顯示。以單一 Blokada DNS 名稱設定的路由器會顯示為一個裝置。

</div>

## 選項 2：保留 Pi-hole，使用 Blokada Cloud 作為上游

如果您想保留在地設定，例如本地主機名稱、DHCP 或自訂清單，請讓 Pi-hole 透過加密連線將查詢轉送到 Blokada。 Pi-hole 本身無法執行加密轉送，因此會有一個小型轉送程式與其並行運作。本指南使用 [dnsproxy](https://github.com/AdguardTeam/dnsproxy)，這是一款單檔的開源轉送工具。

1. 在 Pi-hole 機器上，從其發布頁面下載適合您 CPU 的 `dnsproxy` 版本（針對新版 Raspberry Pi 為 `linux-arm64`），並將 `dnsproxy` 可執行檔複製到 `/usr/local/bin/`。
2. 建立 `/etc/systemd/system/dnsproxy.service`：

<pre><code>[Unit]
Description=Encrypted DNS forwarder to Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. 啟動指令：`sudo systemctl enable --now dnsproxy`
4. 在 Pi-hole 管理介面中，開啟 _設定 → DNS_。取消勾選所有上游伺服器，並新增 `127.0.0.1#5054` 作為自訂上游伺服器。儲存。
5. 查看儀表板的 _活動_ 頁面。來自您網路的查詢現在會顯示在那裡。

您可以關閉 Pi-hole 自身的阻擋清單並在儀表板上管理阻擋，亦可同時保留兩者。

## 常見問題

**我需要 Blokada Plus 嗎？** 不需要。 Blokada Cloud 為您全家提供 DNS 阻擋保護。 [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 會額外提供 VPN 功能。

**如果 Blokada 無法連線怎麼辦？** 您的裝置將無法解析名稱，直到服務恢復，就像 Pi-hole 掛掉時一樣。請勿新增未過濾的第二個 DNS 伺服器作為備援。大多數裝置會隨機使用所有伺服器，這樣廣告就會漏過。
