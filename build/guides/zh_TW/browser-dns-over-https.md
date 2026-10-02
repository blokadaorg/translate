---
title: 使用 DNS over HTTPS 在 Chrome、Firefox、Edge 和 Brave 阻擋廣告
description: 在您的瀏覽器中將 Blokada Cloud 設為安全 DNS 提供者，即可在任何電腦上（包括無法安裝應用程式的工作筆記型電腦）阻擋廣告和追蹤器。
updated: 2026-10-02
order: 7
---

現代瀏覽器可以使用自己的加密 DNS 提供者，稱為「安全 DNS」或「DNS over HTTPS」。將其設為 Blokada Cloud，瀏覽器即可於任何網路上阻擋廣告和追蹤器，無需安裝延伸功能。將其設為 Blokada Cloud，瀏覽器即可於任何網路上阻擋廣告和追蹤器，無需安裝延伸功能。

此設定僅適用於此瀏覽器。如需保護整部電腦，請在 Mac 上使用 [Apple 設定檔](../apple-devices/)，或設定您的[路由器](../router-ad-blocking/)。

## Chrome

1. 開啟 `chrome://settings/security`。
2. 啟用「使用安全 DNS」，然後選擇「新增自訂 DNS 服務提供者」。
3. 輸入 {% doh %}

## Edge

1. 開啟 `edge://settings/privacy`。
2. 在「安全性」下方，啟用「使用安全 DNS 來指定如何查詢網站的網路位址」。
3. 選擇「選擇服務提供者」並輸入 {% doh %}

## Firefox

1. 開啟「設定 → 隱私與安全」，捲動到「DNS over HTTPS」。
2. 選擇「最高防護」。
3. 於「選擇提供者」下，選擇「自訂」，並輸入 {% doh %}

## Brave

1. 開啟 `brave://settings/security`。
2. 啟用「使用安全 DNS」，然後選擇「新增自訂 DNS 服務提供者」。
3. 輸入 {% doh %}

## Safari

Safari 沒有專屬的安全 DNS 設定。它會使用系統的 DNS，請安裝 [Apple 設定檔](../apple-devices/)。它會使用系統的 DNS，請安裝 [Apple 設定檔](../apple-devices/)。

## 檢查是否運作

瀏覽一分鐘後，開啟 [儀表板](https://app.blokada.org/stats?src=guides)中的「活動」頁面。此瀏覽器的查詢會顯示在那裡。此瀏覽器的查詢會顯示在那裡。

## 如果有問題無法運作

<div class="note tip">

如果您的瀏覽器由公司或學校管理，則安全 DNS 設定可能會被鎖定。請詢問您的管理員。請詢問您的管理員。

</div>
