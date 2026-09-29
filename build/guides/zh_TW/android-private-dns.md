---
title: 使用 Blokada Cloud 在 Android 上設定私人 DNS
description: 使用 Android 內建的私人 DNS 設定搭配 Blokada Cloud，可在所有應用程式、Wi-Fi 及行動數據上阻擋廣告與追蹤器。或者讓 Blokada 6 應用自動完成。
updated: 2026-09-28
order: 5
---

## 最簡單的方法：應用程式

[Blokada 6](https://go.blokada.org/play_cloud) 為您完成所有設定，可以一鍵開啟或關閉阻擋，並直接在手機上顯示哪些內容已被阻擋。使用您的帳號 ID 登入即可完成。

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">在 Google Play 取得 Blokada 6</a></p>

## 不使用應用程式：私人 DNS

Android 9 及更新版本具有 _私人 DNS_ 設定。將其設為 Blokada Cloud，所有應用程式及所有網路中的廣告與追蹤器都會被阻擋，且無須在背景運行任何程式。

您的 Blokada DNS 名稱：{% dot %}

1. 開啟 _設定 → 網路與網際網路_。在某些手機上這稱為 _連線_ 或 _連線與分享_。
2. 點選 _私人 DNS_。在 Samsung 手機上，此選項位於 _更多連線設定_ 下。
3. 選擇 _私人 DNS 提供者主機名稱_。
4. 輸入您的 Blokada DNS 名稱 {% dot %} 並點選 _儲存_。

如果找不到，請在設定應用程式中搜尋「私人 DNS」。

## 檢查其是否運作

開啟幾個應用程式或網站，然後在 [儀表板](https://app.blokada.org/stats?src=guides)的 _活動_ 頁面查看。此手機的查詢會在這裡顯示。

## 如果有問題無法運作

- **「無法連接」或沒有網路：** 請檢查您的 Blokada DNS 名稱是否有打錯字。必須與上面所顯示完全一致，不要包含 `https://`。
- **其他 VPN 應用程式正在啟動：** 部分 VPN 應用程式會使用其自有 DNS 並繞過私人 DNS。請關閉該 VPN 的 DNS 或廣告阻擋功能，或改用 Blokada 6。
- **Chrome 仍顯示廣告：** 在 Chrome，請開啟 _設定 → 隱私權與安全性 → 使用安全 DNS_ 並選擇 _使用目前的服務提供者_。
