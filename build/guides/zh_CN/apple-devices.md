---
title: 使用 Blokada DNS 配置文件在 Mac 和 Apple TV 上屏蔽广告
description: 安装 Blokada Cloud DNS 配置文件，在 Mac 或 Apple TV 上实现全系统广告和跟踪器屏蔽，采用加密 DNS，无需后台运行任何程序。
updated: 2026-10-02
order: 6
---

Apple 设备可以通过配置描述文件在整个系统上使用加密的 DNS。Blokada 描述文件会将设备指向 Blokada Cloud，从而在每个应用和浏览器中屏蔽广告和追踪器。

适用于 macOS 11（Big Sur）、tvOS 14、iOS 和 iPadOS 14 及更高版本。

<div class="if-no-device">

此页面尚未识别你的设备，因此无法提供你的描述文件。请登录到仪表盘，打开 _设置_，选择你的设备，然后通过 _在其他设备上打开_ 打开本指南。

<p><a class=\"btn btn-outline\" href=\"https://app.blokada.org/setup?src=guides\">获取我的配置文件链接</a></p>

</div>

## iPhone 和 iPad

最简单的方法是使用应用程序。[Blokada 6](https://go.blokada.org/appstore) 会为你自动完成所有设置，一键即可开启或关闭屏蔽，并直接在手机上显示已屏蔽内容。使用你的帐号 ID 登录即可。

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/appstore\">从 App Store 获取 Blokada 6</a></p>

### 不使用应用程序

你也可以选择安装配置描述文件。iPhone 和 iPad 只能通过 **Safari** 安装描述文件。

<div class="if-device">
<div class="if-other-browser note important">

本页面在其他浏览器中打开。复制你的链接，在 Safari 中打开以继续操作：{% pageLink %}

</div>
</div>

<div class="if-safari">

1. 在 Safari 中，点击下方按钮，然后选择 _允许_ 下载配置文件。
2. 打开 _设置_。点击顶部附近&#x7684;_&#x5DF2;下载描述文件_。你也可以在 _通用 → VPN 与设备管理_ 下找到它。
3. 点击“安装”，输入你的密码并确认。

</div>

<p class="if-device if-safari">{% appleProfile %}下载我的配置文件{% endappleProfile %}</p>

## Mac

1. 点击下方按钮下载配置文件。
2. 打开配置文件列表：在 macOS 15 及更高版本为“系统设置 → 通用 → 设备管理”，macOS 13 和 14 为“系统设置 → 隐私与安全性 → 配置文件”，或 macOS 12 及更早版本为“系统偏好设置 → 配置文件”。
3. 双击 Blokada 配置文件并点击“安装”。

<p class="if-device">{% appleProfile %}下载我的配置文件{% endappleProfile %}</p>

## Apple TV

Apple TV 无法打开网页，因此你需要手动输入你的配置文件链接。

1. 你的配置文件链接：{% appleUrl %}
2. 在 Apple TV 上，打开“设置 → 通用 → 隐私与安全”。
3. 高&#x4EAE;_&#x5171;享 Apple TV 分析_，但不要选择它。请按遥控器上的播放/暂停按钮。
4. 选择 _添加配置描述文件_ 并输入你的配置链接。使用 iPhone 上的键盘提示输入最为方便，你可以直接粘贴。安装配置文件并确认。

<div class="note aside">

**Apple TV 和家中其它设备：** 如果你已在[路由器](../router-ad-blocking/)上设置了 Blokada Cloud，Apple TV 与其他所有设备都能获得保护。

</div>

## 检查是否正常运行

浏览网页片刻后，进入 [仪表盘](https://app.blokada.org/stats?src=guides) 的 _活动_ 页面。此设备的查询会显示在该页面。

如需以后移除 Blokada，只需删除你安装的配置文件即可。
