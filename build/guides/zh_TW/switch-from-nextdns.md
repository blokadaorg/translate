---
title: 一個在每個裝置上都能用相同設定的 NextDNS 替代方案
description: 從 NextDNS 轉換到 Blokada Cloud。只需在您的手機、電腦和路由器上將 NextDNS 的 DNS 名稱、DoH 連結或設定檔換成 Blokada 的對應資訊，即可繼續維持廣告阻擋功能。
updated: 2026-10-02
order: 3
---

NextDNS 和 Blokada Cloud 的運作方式相同：它們是加密的 DNS 服務，透過名稱來阻擋廣告和追蹤器，且能以個人 DNS 名稱進行專屬設定。切換服務時，只需在每台裝置上將 NextDNS 的相關資訊替換為 Blokada 的設定，裝置本身其他部分不需做任何更動。

## 你過去使用的項目，以及應在 Blokada 選擇什麼

| 在 NextDNS 中         | 在 Blokada Cloud 中                   |
| ------------------- | ----------------------------------- |
| 你的設定 ID，例如 `abc123` | 你的裝置標籤，是 Blokada DNS 名稱和 DoH 連結的一部分 |
| _隱私_ 阻擋清單           | 儀表板內的 _阻擋清單_                        |
| _安全性_（惡意軟體、網路釣魚）    | _阻擋清單_ 下的惡意軟體清單                     |
| _家長監護_              | _阻擋清單_ 下的成人內容與賭博清單                  |
| _允許清單_ 與 _封鎖清單_     | 儀表板中的 _例外_                          |
| _日誌_ 與 _統計分析_       | 儀表板中 _活動_ 與 _統計_                    |

## 逐一切換你的裝置

根據您的裝置，您需要您的 DNS 名稱或 DoH 連結，這兩者都在上方的 _您的詳細資料_ 下可找到。

### Android

如果您在 Android 上使用 _Private DNS_ 並設定了 `<your-id>.dns.nextdns.io`，請依照[Android 指南](../android-private-dns/)將其換成您的 Blokada DNS 名稱。如果您使用的是 NextDNS 應用程式，請將其解除安裝，然後改為安裝 [Blokada 6](https://go.blokada.org/play_cloud)。

### iPhone 和 iPad

如果您正在使用 NextDNS 應用程式，請將其解除安裝，然後安裝 [Blokada 6](https://go.blokada.org/appstore)。如果您是安裝 NextDNS 設定檔，請前往 _設定 → 一般 → VPN 與裝置管理_ 中移除，接著依照 [Apple 設備指南](../apple-devices/) 設定。

### Mac 和 Apple TV

移除 NextDNS 的設定檔或應用程式，然後從 [Apple 指引](../apple-devices/) 安裝 Blokada 設定檔。

### Windows 和 Linux

如果您正在使用 NextDNS 應用程式，請先解除安裝。在 Windows 上，請參照 [Windows 指南](../windows-dns-over-https/) 將 NextDNS 伺服器和 DoH 範本替換為 Blokada 的設定。在 Linux 上，請依照 [Linux 指南](../linux-dns-over-tls/)，將 systemd-resolved 中的 NextDNS 伺服器替換為 Blokada。

### 瀏覽器

如果你將 `https://dns.nextdns.io/…` 設為瀏覽器的 _安全 DNS_，請換成你的 DoH 連結，如 [瀏覽器指引](../browser-dns-over-https/) 所示。

### 路由器

如果你的路由器使用 NextDNS 作為 DNS over TLS 或 DNS over HTTPS，請將 NextDNS 名稱或連結，按照 [路由器指引](../router-ad-blocking/) 換成你的 Blokada 名稱或連結。

如果您的路由器是透過明碼 IP 地址&#x53CA;_&#x5DF2;連結 I&#x50;_&#x4F7F;用 NextDNS，Blokada 尚未支援該方式。針對僅使用明碼 DNS 地址的路由器，支援功能尚在開發中。在此之前，請逐一在每個裝置上設定，或使用可支援加密 DNS 的路由器。

## 檢查是否運作正常

開啟幾個網站，然後在儀表板的 _活動_ 頁面檢視。您會看到各裝置的查詢紀錄，已阻擋的查詢會有標記。如果某台裝置未出現於列表，表示它仍在使用 NextDNS。
