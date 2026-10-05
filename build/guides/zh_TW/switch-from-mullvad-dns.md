---
title: Mullvad DNS 即將關閉。使用 Blokada Cloud 保持您的廣告阻擋功能
description: Mullvad 將於 2026 年 11 月 2 日關閉其公開 DNS。以下說明如何在此日期前，將您的手機、電腦和路由器切換至 Blokada Cloud，同時維持廣告阻擋功能。
updated: 2026-10-02
order: 2
---

Mullvad 將於 **2026 年 11 月 2 日** 關閉其免費公開 DNS 服務，並建議改用 Quad9。Quad9 能阻擋惡意軟體，但**不**會阻擋廣告或追蹤器。當 Mullvad 的 DNS 停止運作時，設為該服務的裝置將無法載入網站和應用程式。若裝置允許自動切換到其他 DNS 伺服器，廣告則會重新出現。請務必在該日期前完成切換。

本頁內容僅針對結尾為 `dns.mullvad.net` 的公開 DNS 名稱，未涵蓋 Mullvad VPN 應用程式。

## 您過去使用什麼，以及在 Blokada 中要選擇什麼

| Mullvad DNS 名稱             | 已阻擋內容          | 在 Blokada 儀表板中                                        |
| -------------------------- | -------------- | ----------------------------------------------------- |
| `dns.mullvad.net`          | 無              | Blokada 是一項篩選服務。如果您不需要篩選功能，Quad9 或您的提供者 DNS 會是更簡單的選擇。 |
| `adblock.dns.mullvad.net`  | 廣告、追蹤器         | 廣告與追蹤器的阻擋清單                                           |
| `base.dns.mullvad.net`     | 廣告、追蹤器、惡意軟體    | 新增一個惡意軟體清單                                            |
| `extended.dns.mullvad.net` | base 加上社群媒體    | 新增一個社群媒體清單                                            |
| `family.dns.mullvad.net`   | base 加上成人內容與賭博 | 新增成人內容與賭博清單                                           |
| `all.dns.mullvad.net`      | 上述全部           | 全部開啟                                                  |

您可在控制台的 _Blocklists_ 選擇阻擋清單。您可隨時變更，變更後將套用到所有您的裝置。

## 切換每個裝置

Blokada 為每台裝置分配專屬名稱，因此控制台可以按裝置顯示活動記錄。依照裝置不同，您需要使用您的 DNS 名稱或 DoH 連結，兩者皆可在上方 _您的詳細資料_ 中找到。

### Android

Mullvad 指南曾要求您在 _Private DNS_ 下輸入主機名稱。請改為輸入您的 Blokada DNS 名稱。[Android 指南](../android-private-dns/)中有詳細步驟。

### iPhone、iPad 與 Mac

Mullvad 的設定使用了設定描述檔。請先將其移除：

- **iPhone 與 iPad：** _設定 → 一般 → VPN 與裝置管理_，點擊 Mullvad DNS 描述檔，然後選擇 _移除描述檔_。
- **Mac：** 打開描述檔列表（macOS 15 及以上為 _系統設定 → 一般 → 裝置管理_，macOS 13 與 14 為 _系統設定 → 隱私權與安全性 → 描述檔_，macOS 12 及更早版本為 _系統偏好設定 → 描述檔_），選取 Mullvad DNS 描述檔並點選 _−_。

接著依照[Apple 指南](../apple-devices/)安裝 Blokada 描述檔。

### 瀏覽器

如果您在 _secure DNS_ 或 _DNS over HTTPS_ 輸入了如 `https://adblock.dns.mullvad.net/dns-query` 的 Mullvad DoH 連結，請改為輸入您的 DoH 連結。[瀏覽器指南](../browser-dns-over-https/)有各瀏覽器步驟。

### 路由器

如果您的路由器使用 Mullvad 的 DNS over TLS，請將 Mullvad 的主機名稱換成您的 Blokada DNS 名稱，並移除 Mullvad 的 IP 位址。[路由器指南](../router-ad-blocking/)提供常見型號操作方法。

## 確認其運作

開啟幾個網站，然後查看控制台的 _Activity_ 頁面。您可以在此看到各裝置的查詢記錄，已阻擋者會有標記。如果裝置沒有顯示，即代表其仍在使用其他 DNS 伺服器。
