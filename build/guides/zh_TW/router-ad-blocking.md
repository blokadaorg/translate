---
title: 使用路由器廣告阻擋，為整個網路阻擋廣告
description: 只需在您的路由器上設置一次 Blokada Cloud，家中的每一台裝置都能受到保護，包括無法執行廣告阻擋程式的電視、遊戲主機與智慧喇叭。
updated: 2026-10-02
order: 4
---

您網路上的每個裝置會向路由器詢問應該使用哪個 DNS 伺服器。您網路上的每個裝置會向路由器詢問應該使用哪個 DNS 伺服器。將路由器設定為使用 Blokada Cloud，所有在背後的裝置都會被阻擋廣告與追蹤器。這包含智慧電視、遊戲主機、串流播放器與智慧家庭裝置，這些無法安裝廣告阻擋應用程式。這包含智慧電視、遊戲主機、串流播放器與智慧家庭裝置，這些無法安裝廣告阻擋應用程式。

## 您的路由器需求

您的路由器必須支援**使用主機名稱的加密 DNS**，也就是 DNS over TLS（DoT）或 DNS over HTTPS（DoH）。許多新型路由器都支援，包括下方這些型號。根據您的路由器支援的功能，您需要：許多新型路由器都支援，包括下方這些型號。根據您的路由器支援的功能，您需要提供您的 DNS 名稱或 DoH 連結，這兩者都可以在上方「您的詳細資訊」中找到。

<div class="note important">

**只能輸入純 IP 位址？** 很多網際網路供應商的路由器只接受 DNS 的純 IP 位址。對這些的支援即將推出。在這之前，請分別為您的裝置設定：[Android](../android-private-dns/)、[Mac 及 Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/)、以及[瀏覽器](../browser-dns-over-https/)。您也可以如在 [Pi-hole 教學](../switch-from-pihole/)中所述，在 Raspberry Pi 上運行小型轉發程式。

</div>

## FRITZ!Box

FRITZ!OS 7.20 或更新版本。

1. 開啟 `http://fritz.box`，進入 _Internet → 帳戶資訊 → DNS 伺服器_。
2. 在\*網際網路上的加密主機名稱解析（DNS over TLS）\*下，勾選 _使用加密主機名稱解析_。
3. 在 _DNS 伺服器的名稱解析_ 欄位中，只輸入 {% dot %}。 &#x5728;_解析程式名&#x7A31;_&#x4E2D;，僅輸入 {% dot %}。**移除所有其他項目。** FRITZ!Box 會使用所有列出的解析程式，任何其他的都可能讓廣告通過。
4. 勾選強制驗證憑證的選項，並取消允許回退到未加密名稱解析的選項。
5. 如果你看到 _Failover to public DNS servers when DNS disrupted_，請將其關閉。
6. 點選 _套用_。

## ASUS

最新版 ASUS 韌體（3.0.0.4.388 或更新版本）與 Asuswrt-Merlin。

1. 開啟路由器管理頁面，進入 _WAN → 網際網路連線_。
2. &#x5728;_&#x57;AN DNS 設&#x5B9A;_&#x4E0B;，&#x5C07;_&#x44;NS 私隱協&#x8B70;_&#x8A2D;&#x70BA;_&#x44;NS-over-TLS (DoT)_，_DNS-over-TLS Profile_ 設為 _Strict_。
3. &#x5F9E;_&#x44;NS-over-TLS 伺服器清&#x55AE;_&#x4E2D;移除所有項目，然後新增一個：
   - 地址：{% ip "dot" %}
   - TLS 主機名稱：{% dot %}
4. 點選 _套用_。

## OpenWrt

1. &#x65BC;_&#x7CFB;統 → 軟&#x9AD4;_&#x4E2D;，更新清單並安裝 `luci-app-https-dns-proxy`。
2. 開啟 _服務 → HTTPS DNS Proxy_。刪除其他供應商的實例。刪除其他供應商的實例。
3. 新增一個自訂解析程式 URL 的實例：{% doh %}
4. _儲存並套用_。該套件會自動指向 dnsmasq。

## 其他路由器

請尋找名為 _DNS over TLS_、_Private DNS_、_Encrypted DNS_ 或 _DNS over HTTPS_ 的設定。輸入您的 Blokada DNS 名稱或上方的 DoH 連結，並移除所有其他 DNS 伺服器，包括備用伺服器。輸入您的 Blokada DNS 名稱或上方的 DoH 連結，並移除所有其他 DNS 伺服器，包括備用伺服器。

## 檢查是否運作正常

1. 重新啟動一台裝置，或關閉再開啟其 Wi-Fi，使其重新獲取設定。
2. 瀏覽一分鐘，然後在儀表板中開啟 _活動_ 頁面。您網路的查詢將會顯示在該處。

## 如果有些裝置仍然顯示廣告

有些裝置會繞開路由器：已設&#x5B9A;_&#x50;rivate DN&#x53;_&#x7684;手機、已設&#x5B9A;_&#x5B89;全 DN&#x53;_&#x70BA;其他供應商的瀏覽器，及自行硬編碼 DNS 的裝置。請直接在裝置上設定，或關閉他們自己的 DNS 設定。

<div class="note tip">

在路由器後方，所有裝置會共用一個位址，因此儀表板會將您的網路顯示為單一裝置。如果希望分開查看，請分別為手機和筆電設置它們自己的 Blokada DNS 名稱。這樣它們即使外出也仍會維持阻擋功能。

</div>
