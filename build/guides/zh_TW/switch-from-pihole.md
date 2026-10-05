---
title: 無需硬體的 Pi-hole 替代方案
description: 將您家中的廣告阻擋從 Pi-hole 遷移到 Blokada Cloud，或保留 Pi-hole 並將其查詢通過 Blokada 傳送。
updated: 2026-10-02
order: 1
---

只要 Raspberry Pi 正常運行、更新且在家，Pi-hole 就會為您網路上的每台裝置阻擋廣告。Blokada Cloud 透過我們的伺服器提供相同的功能：

- **無需維護盒子。** 沒有 SD 卡，沒有更新，當 Pi 掛掉時也不會中斷服務。
- **外出也能運作。** 手機與筆電連接行動數據與其他 Wi-Fi 網路時仍可阻擋廣告。
- **加密連線。** 裝置透過 DNS over TLS 或 DNS over HTTPS 連接 Blokada，因此您的服務提供商無法讀取或更改查詢內容。
- **統一儀表板。** 可在 [app.blokada.org](https://app.blokada.org/?src=guides) 查看阻擋清單、允許與已阻擋網域、以及各裝置的活動紀錄。

有兩種切換方式。可以完全替換 Pi-hole，或者保留 Pi-hole 並將 Blokada Cloud 設為其上游。

## 選項 1：取代 Pi-hole

1. **取得 Blokada Cloud** 並開啟儀表板。您的 DNS 名稱和 DoH 連結&#x5728;_&#x8A2D;&#x5B9A;_&#x9801;籤下，以及上方&#x7684;_&#x60A8;的詳細資&#x6599;_&#x4E2D;。
2. \*\*將您的路由器指向 Blokada，而不是 Pi-hole。\*\*請依照[路由器指南](../router-ad-blocking/)操作。如果您的路由器只接受純 IP 位址做為 DNS 伺服器，請逐一設定您的裝置：[Android](../android-private-dns/)、[Mac 和 Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/)以及[瀏覽器](../browser-dns-over-https/)。
3. \*\*如果您的 Pi-hole 曾擔任 DHCP 伺服器，\*\*請在關閉 Pi 之前先在路由器中重新啟用 DHCP。否則您的裝置將無法獲得網路位址。
4. **搬移您的清單。** 在儀表板中於 _阻擋清單_ 選擇阻擋清單，並在 _例外_ 中新增您允許或已阻擋的網域。
5. **關閉 Pi-hole，** 或保留作為其他用途。

<div class="note aside">

您的 Pi-hole 會以 IP 位址顯示網路上的每台裝置。使用 Blokada 時，只要每台裝置使用自己的 Blokada DNS 名稱，就能以裝置名稱顯示。如果用同一個 Blokada DNS 名稱設在路由器上，則會顯示為一個裝置。

</div>

## 選項 2：保留 Pi-hole，使用 Blokada Cloud 作為上游

如果您想保留本地設定，例如本地主機名稱、DHCP 或自訂列表，可以讓 Pi-hole 透過加密連線將查詢轉發到 Blokada。Pi-hole 自身無法進行加密轉發，因此需要在旁邊運行一個小型轉發程式。本指南採用 [dnsproxy](https://github.com/AdguardTeam/dnsproxy)，這是一個單一檔案的開源轉發程式。

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
4. 在 Pi-hole 管理後台，打&#x958B;_&#x8A2D;定 → DNS_。取消勾選所有上游伺服器，並新增 `127.0.0.1#5054` 作為自訂上游伺服器，然後儲存。
5. 請檢查儀表板&#x7684;_&#x6D3B;&#x52D5;_&#x9801;面。現在來自您網路的查詢都會出現在那裏。

您可以關閉 Pi-hole 自身的阻擋清單並在儀表板上管理阻擋，亦可同時保留兩者。

## 常見問題

**我需要 Blokada Plus 嗎？** 不需要。Blokada Cloud 可涵蓋您的整個家庭 DNS 阻擋功能。[Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 則額外提供 VPN。

\*\*如果 Blokada 無法連線怎麼辦？\*\*在服務恢復之前，您的裝置將無法解析名稱，就像 Pi-hole 當機一樣。不要新增第二個未過濾的 DNS 伺服器做為備援，大多數裝置會隨機使用他們的所有伺服器，廣告將得以穿透。
