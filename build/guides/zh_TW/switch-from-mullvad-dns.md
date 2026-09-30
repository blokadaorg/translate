---
title: Mullvad DNS 即將關閉。使用 Blokada Cloud 繼續阻擋廣告
description: Mullvad 將於 2026 年 11 月 2 日關閉其公共 DNS。以下是在此之前將您的手機、電腦和路由器遷移到 Blokada Cloud 的方法，廣告阻擋功能不會中斷。
updated: 2026-09-23
order: 2
---

Mullvad 將於 **2026 年 11 月 2 日** 關閉其免費公共 DNS 服務，並建議改用 Quad9。 Quad9 可以阻擋惡意軟體，但**不會**阻擋廣告或追蹤器。如果您使用了 Mullvad 的過濾 DNS 名稱，在那一天之後廣告將會重新顯示，除非您切換。

此頁面是關於以 `dns.mullvad.net` 結尾的公共 DNS 名稱。此內容不包含 Mullvad VPN 應用程式。

## 您過去使用什麼，以及在 Blokada 中要選擇什麼

| Mullvad DNS 名稱             | 已阻擋內容          | 在 Blokada 儀表板中                                          |
| -------------------------- | -------------- | ------------------------------------------------------- |
| `dns.mullvad.net`          | 無              | Blokada 是一個篩選服務。如果您不想要任何篩選，Quad9 或您的網路提供者的 DNS 是更簡單的選擇。 |
| `adblock.dns.mullvad.net`  | 廣告、追蹤器         | 廣告與追蹤器的阻擋清單                                             |
| `base.dns.mullvad.net`     | 廣告、追蹤器、惡意軟體    | 新增一個惡意軟體清單                                              |
| `extended.dns.mullvad.net` | base 加上社群媒體    | 新增一個社群媒體清單                                              |
| `family.dns.mullvad.net`   | base 加上成人內容與賭博 | 新增成人內容與賭博清單                                             |
| `all.dns.mullvad.net`      | 上述全部           | 全部開啟                                                    |

您可以在儀表板中的 _Blocklists_ 下選擇阻擋清單。您可以隨時變更它們，且變更將適用於您所有裝置。

## 您的 Blokada 詳細資訊

Blokada 會給每個裝置一個獨立名稱，因此儀表板能針對每台裝置顯示活動情況：

- 您的 Blokada DNS 名稱，適用於 DNS over TLS（Android、路由器）：{% dot %}
- 您的 DoH 連結，適用於 DNS over HTTPS（瀏覽器、部分路由器）：{% doh %}

## 切換每個裝置

### Android

Mullvad 的指南要求您在 _Private DNS_ 中輸入主機名稱。請將其替換為您的 Blokada DNS 名稱。 [Android 指南](../android-private-dns/)包含詳細步驟。

### iPhone、iPad 與 Mac

Mullvad 的設定使用了一個組態描述檔。請先移除它：

- **iPhone 與 iPad：** _設定 → 一般 → VPN 與裝置管理_，點擊 Mullvad DNS 描述檔，然後選擇 _移除描述檔_。
- **Mac：** 打開描述檔列表（macOS 15 及以上為 _系統設定 → 一般 → 裝置管理_，macOS 13 與 14 為 _系統設定 → 隱私權與安全性 → 描述檔_，macOS 12 及更早版本為 _系統偏好設定 → 描述檔_），選取 Mullvad DNS 描述檔並點選 _−_。

接著依照[Apple 指南](../apple-devices/)安裝 Blokada 描述檔。

### 瀏覽器

如果您在 _安全 DNS_ 或 _DNS over HTTPS_ 下輸入了 Mullvad DoH 連結，如 `https://adblock.dns.mullvad.net/dns-query`，請將其更換為您的 DoH 連結。[瀏覽器指南](../browser-dns-over-https/)包含每款瀏覽器的步驟。

### 路由器

如果您的路由器使用 Mullvad 的 DNS over TLS，請將 Mullvad 的主機名稱替換為您的 Blokada DNS 名稱，並移除 Mullvad 的 IP 位址。[路由器指南](../router-ad-blocking/)涵蓋常見型號。

## 確認其運作

打開幾個網站，然後在儀表板查看 _活動_ 頁面。您會在那裡看到各裝置的查詢，已阻擋的會有標記。如果某個裝置未出現在列表，表示它仍在使用其他 DNS 伺服器。
