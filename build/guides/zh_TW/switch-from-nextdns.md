---
title: 一個在每個裝置上都能用相同設定的 NextDNS 替代方案
description: 從 NextDNS 轉移到 Blokada Cloud。將你的 NextDNS DNS 名稱、DoH 鏈接或設定檔替換為你的 Blokada，在手機、電腦和路由器上，並持續阻擋廣告。
updated: 2026-09-28
order: 3
---

NextDNS 與 Blokada Cloud 以相同方式運作：它們是能透過加密 DNS 阻擋廣告與追蹤器的服務，而且你可以通過個人 DNS 名稱設定自己的專屬選項。切換時，就是將每個裝置上的 NextDNS 參數換成你的 Blokada 參數。裝置上的其他內容皆不會變化。

## 你過去使用的項目，以及應在 Blokada 選擇什麼

| 在 NextDNS 中         | 在 Blokada Cloud 中                   |
| ------------------- | ----------------------------------- |
| 你的設定 ID，例如 `abc123` | 你的裝置標籤，是 Blokada DNS 名稱和 DoH 連結的一部分 |
| _隱私_ 阻擋清單           | 儀表板內的 _阻擋清單_                        |
| _安全性_（惡意軟體、網路釣魚）    | _阻擋清單_ 下的惡意軟體清單                     |
| _家長監護_              | _阻擋清單_ 下的成人內容與賭博清單                  |
| _允許清單_ 與 _封鎖清單_     | 儀表板中的 _例外_                          |
| _日誌_ 與 _統計分析_       | 儀表板中 _活動_ 與 _統計_                    |

## 你的 Blokada 資訊

- 你的 Blokada DNS 名稱，適用於 DNS over TLS：{% dot %}
- 你的 DoH 連結，適用於 DNS over HTTPS：{% doh %}

## 逐一切換你的裝置

### Android

若你使用 _私人 DNS_ 並設為 `<your-id>.dns.nextdns.io`，請將其換成你的 Blokada DNS 名稱，如[Android 指引](../android-private-dns/)所示。如果你之前使用 NextDNS 應用程式，請卸載它，改為安裝 [Blokada 6](https://go.blokada.org/play_cloud)。

### iPhone 和 iPad

如果你之前使用 NextDNS 應用程式，請卸載它，改為安裝 [Blokada 6](https://go.blokada.org/appstore)。如果你改為安裝了 NextDNS 設定檔，請於 _設定 → 一般 → VPN 與裝置管理_ 中移除，然後依照 [Apple 指引](../apple-devices/) 操作。

### Mac 和 Apple TV

移除 NextDNS 的設定檔或應用程式，然後從 [Apple 指引](../apple-devices/) 安裝 Blokada 設定檔。

### Windows 和 Linux

若有使用 NextDNS 應用程式，請將其解除安裝。在 Windows 上，請將 NextDNS 伺服器與 DoH 範本換成 Blokada，如[Windows 指引](../windows-dns-over-https/)所示。在 Linux 上，請將 systemd-resolved 的 NextDNS 伺服器替換掉，參照 [Linux 指引](../linux-dns-over-tls/)。

### 瀏覽器

如果你將 `https://dns.nextdns.io/…` 設為瀏覽器的 _安全 DNS_，請換成你的 DoH 連結，如 [瀏覽器指引](../browser-dns-over-https/) 所示。

### 路由器

如果你的路由器使用 NextDNS 作為 DNS over TLS 或 DNS over HTTPS，請將 NextDNS 名稱或連結，按照 [路由器指引](../router-ad-blocking/) 換成你的 Blokada 名稱或連結。

如果它是通過純 IP 並有 _已連結 IP_ 使用 NextDNS，Blokada 目前尚未支援此功能。對於只支援純 DNS 位址的路由器，支援功能即將推出。在那之前，請逐一為你的裝置設定，或換用能支援加密 DNS 的路由器。

## 檢查是否運作正常

打開幾個網站，然後檢視儀表板中的 _活動_ 頁面。你會看到你的裝置查詢紀錄，其中已阻擋的項目會有標記。如果某個裝置沒出現，就代表它仍使用 NextDNS。
