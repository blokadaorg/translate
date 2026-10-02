---
title: 在 Windows 上使用 DNS over HTTPS 阻擋廣告
description: 使用 Windows 11 內建的加密 DNS 搭配 Blokada Cloud，可在所有應用程式與瀏覽器中阻擋廣告及追蹤器，無需安裝額外軟體。
updated: 2026-10-02
order: 8
---

Windows 11 可以透過 DNS over HTTPS 加密傳送所有 DNS 查詢。將其指向 Blokada Cloud，即可在這台電腦的所有應用程式與瀏覽器中阻擋廣告及追蹤器，無需安裝任何程式。

你需要 DNS 伺服器的 IP 位址以及你的 DoH 連結，這兩者都在上方的「你的詳細資料」中。

## Windows 11

1. 開啟 _設定 → 網路與網際網路_，然後依據電腦連線方式選擇 _Wi-Fi_ 或 _乙太網路_。
2. 開啟您連線的 _硬體內容_。如果是 Wi-Fi，請選擇 _管理已知網路_ 並選擇網路，或在 Wi-Fi 頁面頂端選擇 _硬體內容_。
3. 在 _DNS 伺服器指派_ 旁選擇 _編輯_。選擇 _手動_ 並啟用 _IPv4_。
4. 在 _首選 DNS_ 中輸入 DNS 伺服器 {% ip "doh" %}
5. 將 _DNS over HTTPS_ 設為 _開啟（手動範本）_，並將您的 DoH 連結 {% doh %} 貼到 _DoH 範本_ 欄位。
6. 將 _回落為純文字_ 關閉，然後選擇 _儲存_。

如果這台電腦同時使用 Wi-Fi 和乙太網路，請對另一個連線也執行相同步驟。

<div class="note important">

將 _替代 DNS_ 保持空白。 Windows 會同時使用兩個伺服器，其它任何一個伺服器都可能讓廣告穿透。

</div>

<div class="note tip">

沒有 _開啟（手動範本）_ 選項？您的 Windows 11 版本較舊。請更新 Windows，或暫時依照 [瀏覽器說明](../browser-dns-over-https/) 設定。

</div>

## Windows 10

Windows 10 沒有內建加密 DNS。請改為於瀏覽器中設定安全 DNS，如 [瀏覽器說明](../browser-dns-over-https/) 中所述，或設定您的 [路由器](../router-ad-blocking/) 保護整個家庭網路。

## 檢查設定是否生效

開啟幾個網站，然後在 [儀表板](https://app.blokada.org/stats?src=guides) 的 _活動_ 頁面查看。這台電腦的查詢會顯示在那裡。

<div class="note aside">

想在這台電腦上也使用 VPN 嗎？ [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) 包含 WireGuard 設定，可加密全部流量，並享有同樣的阻擋效果。

</div>

## 如果有問題無法運作

Chrome 和 Edge 有自己的「安全 DNS」設定，這會繞過 Windows。若設為自動，可能會回退至傳統 DNS，這是 Blokada 不允許的。請改設為您的 DoH 連結：

- **Chrome：** 開啟 `chrome://settings/security`，開啟「使用安全 DNS」，在「選擇 DNS 提供者」下點擊「新增自訂 DNS 服務提供者」。
- **Edge：** 開啟 `edge://settings/privacy`，啟用安全 DNS，然後選擇「選擇一個服務提供者」。

然後貼上您的 DoH 連結 {% doh %}

如果在啟用 IPv6 的網路上廣告仍未被完全阻擋，Windows 也可能正在詢問您的路由器的 IPv6 DNS 伺服器。在介面卡內容（_控制台 → 網路連線_）中關閉 _網際網路通訊協定第 6 版 (TCP/IPv6)_，或設定您的 [路由器](../router-ad-blocking/)。
