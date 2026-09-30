---
title: 使用 Blokada DNS 設定檔在 Mac 與 Apple TV 阻擋廣告
description: 安裝 Blokada Cloud DNS 設定檔，在 Mac 或 Apple TV 上系統層級阻擋廣告與追蹤器，並採用加密 DNS，且無需有程式在背景執行。
updated: 2026-09-28
order: 6
---

Apple 裝置可以透過設定檔，為整個系統啟用加密 DNS。 Blokada 設定檔會將裝置指向 Blokada Cloud，讓廣告與追蹤器在所有應用程式及瀏覽器中均被阻擋。

支援 macOS 11（Big Sur）、tvOS 14、iOS 和 iPadOS 14 及更新版本。

<div class="if-no-device">

本頁尚未辨識你的裝置，因此無法提供你的設定檔。請登入控制台，開啟 _設定_，選擇你的裝置，並&#x7528;_&#x5728;其他裝置開&#x555F;_&#x6253;開本指南。

<p><a class=\"btn btn-outline\" href=\"https://app.blokada.org/setup?src=guides\">取得我的設定檔連結</a></p>

</div>

## iPhone 與 iPad

最簡單的方法就是使用應用程式。 [Blokada 6](https://go.blokada.org/appstore) 可為你自動完成所有設定，並能一鍵開啟或關閉阻擋功能，同時在手機上查看已阻擋的項目。使用你的帳戶 ID 登入，即可完成。

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/appstore\">在 App Store 取得 Blokada 6</a></p>

### 不使用應用程式

你也可以改為安裝設定檔。 iPhone 與 iPad 僅能透過 **Safari** 安裝設定檔。

<div class="if-device">
<div class="if-other-browser note">

您正在其他瀏覽器開啟此頁面。請複製你的連結，並用 Safari 開啟以繼續操作：{% pageLink %}

</div>
</div>

<div class="if-safari">

1. 在 Safari 中，點擊下方按鈕，然後選擇 _允許_ 來下載設定檔。
2. 開&#x555F;_&#x8A2D;定_。在上方點&#x64CA;_&#x5DF2;下載描述檔_。你也可以&#x5728;_&#x4E00;般 → VPN 與裝置管&#x7406;_&#x4E2D;找到此項。
3. 點&#x64CA;_&#x5B89;裝_，輸入你的密碼並確認。

</div>

<p class="if-device if-safari">{% appleProfile %}下載我的設定檔{% endappleProfile %}</p>

## Mac

1. 點擊下方按鈕下載設定檔。
2. 開啟設定檔列表：在 macOS 15 及更新版本&#x70BA;_&#x7CFB;統設定 → 一般 → 裝置管理_，在 macOS 13 與 14 &#x70BA;_&#x7CFB;統設定 → 隱私權與安全性 → 描述檔_，macOS 12 及更舊版本則&#x70BA;_&#x7CFB;統偏好設定 → 描述檔_。
3. 連按兩下 Blokada 設定檔，然後點&#x64CA;_&#x5B89;裝_。

<p class="if-device">{% appleProfile %}下載我的設定檔{% endappleProfile %}</p>

## Apple TV

Apple TV 無法開啟網頁，因此你需要手動輸入設定檔連結。

1. 你的設定檔連結：{% appleUrl %}
2. 在 Apple TV 上，開&#x555F;_&#x8A2D;定 → 一般 → 隱私與安全_。
3. 選&#x4E2D;_&#x50B3;送給 Apple_（在舊版 tvOS 中稱&#x70BA;_&#x5206;享 Apple TV 分析資料_）。請勿選取它。請按下遙控器上的播放/暫停按鈕。
4. 選&#x64C7;_&#x65B0;增描述&#x6A94;_&#x4E26;輸入你的設定檔連結。在你的 iPhone 上跳出鍵盤提示時，貼上連結會更方便。安裝設定檔並確認。

<div class="note">

**Apple TV 及家中其他裝置：** 如果你在[路由器](../router-ad-blocking/)上設置 Blokada Cloud，就能讓 Apple TV 及所有裝置同時受保護。

</div>

## 確認功能正常

瀏覽一分鐘後，於[控制台](https://app.blokada.org/stats?src=guides)開&#x555F;_&#x6D3B;&#x52D5;_&#x9801;。此裝置的查詢會顯示於該處。

日後如要移除 Blokada，請刪除你所安裝的設定檔。
