---
title: 在 Android 上使用 Blokada Cloud 设置专用 DNS。
description: 使用 Android 内置的专用 DNS 设置搭配 Blokada Cloud，在所有应用中、包括 Wi-Fi 和移动数据下屏蔽广告和追踪器。或者让 Blokada 6 应用自动完成。
updated: 2026-09-28
order: 5
---

## 最简单的方法：应用

[Blokada 6](https://go.blokada.org/play_cloud) 会为你自动完成所有设置，一键开启或关闭拦截，并在手机上显示已拦截内容。使用你的帐号 ID 登录即可。

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">在 Google Play 获取 Blokada 6</a></p>

## 不使用应用程序：私有 DNS

Android 9 及更高版本有一&#x4E2A;_&#x79C1;有 DN&#x53;_&#x8BBE;置。将其设置为 Blokada Cloud，广告和跟踪器将在所有应用程序和每个网络中被拦截，且后台无需运行任何程序。

您的 Blokada DNS 名称：{% dot %}

1. 打&#x5F00;_&#x8BBE;置 → 网络和互联网_。在某些手机上，该选项&#x4E3A;_&#x8FDE;&#x63A5;_&#x6216;_连接与共享_。
2. 点&#x51FB;_&#x79C1;有 DNS_。在三星手机上，此选项位&#x4E8E;_&#x66F4;多连接设&#x7F6E;_&#x4E0B;。
3. 选&#x62E9;_&#x79C1;有 DNS 提供商主机名_。
4. 输入您的 Blokada DNS 名称 {% dot %} 并点&#x51FB;_&#x4FDD;存_。

如果找不到该选项，请在设置应用中搜索“私有 DNS”。

## 检查其是否有效

打开几个应用程序或网站，然后查看[仪表盘](https://app.blokada.org/stats?src=guides)中&#x7684;_&#x6D3B;&#x52A8;_&#x9875;面。此手机的查询记录会显示在那里。

## 如遇问题

- \*\*“无法连接”或无网络：\*\*请检查您的 Blokada DNS 名称是否有拼写错误。必须与上方显示内容完全一致，不带 `https://`。
- \*\*另一个 VPN 应用正在运行：\*\*某些 VPN 应用使用自己的 DNS 并绕过私有 DNS。请关闭该 VPN 的 DNS 或广告拦截设置，或者改用 Blokada 6。
- \*\*Chrome 仍然显示广告：\*\*在 Chrome 中，打&#x5F00;_&#x8BBE;置 → 隐私和安全 → 使用安全 DNS_，并选&#x62E9;_&#x4F7F;用当前服务提供商_。
