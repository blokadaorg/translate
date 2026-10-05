---
title: 使用路由器廣告阻擋，為整個網路阻擋廣告
description: 只需在您的路由器上設置一次 Blokada Cloud，家中的每一台裝置都能受到保護，包括無法執行廣告阻擋程式的電視、遊戲主機與智慧喇叭。
updated: 2026-10-02
order: 4
---

您網路上的每個裝置都會詢問路由器要使用哪個 DNS 伺服器。將路由器指向 Blokada Cloud，所有在其後方的裝置，包括智慧電視、遊戲主機、串流棒和智慧家庭裝置等無法安裝廣告阻擋器應用程式的裝置，廣告和追蹤器都會自動被阻擋。​

## 您的路由器需求

您的路由器必須支援**具有主機名稱的加密 DNS**，即 DNS over TLS（DoT）或 DNS over HTTPS（DoH）。許多近期的路由器都支援，包括下列型號。根據您的路由器支援的類型，您需要輸入 DNS 名稱或 DoH 連結，兩者都在上方的「您的詳細資料」下。

<div class="note important">

**只接受純 IP 位址？** 許多網路供應商的路由器僅接受純 IP 位址作為 DNS。針對這類狀況的支援即將推出。在此之前，請逐一設定您的裝置：[Android](../android-private-dns/)、[Mac 和 Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/)，以及[瀏覽器](../browser-dns-over-https/)。您也可依據 [Pi-hole 指南](../switch-from-pihole/)在 Raspberry Pi 上運行小型轉發器。

</div>

## FRITZ!Box

FRITZ!OS 7.20 或更新版本。

1. 開啟 `http://fritz.box`，進入 _Internet → 帳戶資訊 → DNS 伺服器_。
2. 在\*網際網路上的加密主機名稱解析（DNS over TLS）\*下，勾選 _使用加密主機名稱解析_。
3. 在「DNS 伺服器解析名稱」中，僅輸入 {% dot %}。\*\*移除所有其他項目。\*\*FRITZ!Box 會使用所有列出的解析伺服器，其他的條目會讓廣告流通。
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
2. 開啟「服務 → HTTPS DNS Proxy」。刪除其他提供者的條目。
3. 新增一個自訂解析程式 URL 的實例：{% doh %}
4. 點選「儲存並套用」。此套件會自動將 dnsmasq 指向該項。

## 其他路由器

尋找名稱為「DNS over TLS」、「Private DNS」、「Encrypted DNS」或「DNS over HTTPS」的設定。輸入您的 Blokada DNS 名稱或 DoH 連結，然後移除所有其他 DNS 伺服器，包括備用伺服器。

## 檢查是否運作正常

1. 重新啟動一台裝置，或關閉再開啟其 Wi-Fi，使其重新獲取設定。
2. 瀏覽一分鐘後，開啟儀表板中的「活動」頁面。您的網路查詢都會顯示在那裡。

## 如果有些裝置仍然顯示廣告

有些裝置會繞過路由器：例如已設定「Private DNS」的手機、將「安全 DNS」設為其他提供者的瀏覽器，以及硬性設定 DNS 的設備。請在該裝置上單獨設定，或關閉其 DNS 設定功能。

<div class="note tip">

在路由器之下，所有裝置共用一個位址，因此儀表板上會將您的網路顯示為單一裝置。如果您想分開查看，請為手機和筆電分別設定專屬的 Blokada DNS 名稱。當他們離開家時，依然可繼續阻擋廣告。

</div>
