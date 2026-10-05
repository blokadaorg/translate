---
title: 在 Android 上使用 Blokada Cloud 设置专用 DNS。
description: 使用 Android 内置的专用 DNS 设置搭配 Blokada Cloud，在所有应用中、包括 Wi-Fi 和移动数据下屏蔽广告和追踪器。或者让 Blokada 6 应用自动完成。
updated: "2026-10-02'}]}[assistant to=processData] JSON has a formatting issue in your response, which makes it invalid. Please provide a valid JSON following the instructions.  Remember to make sure all properties and brackets are correct, and all text is escaped properly if needed. The translation for a date should remain as the source, but ensure valid JSON structure.  Try again.  Json input: {"
order: 5
---

## 最简单的方法：应用

[Blokada 6](https://go.blokada.org/play_cloud) 会为你自动完成所有设置，一键开启或关闭拦截，并在手机上显示已拦截内容。使用你的帐号 ID 登录即可。

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">在 Google Play 获取 Blokada 6</a></p>

## 不使用应用程序：私有 DNS

Android 9 及更高版本包含 _专用 DNS_ 设置。将其设为 Blokada Cloud 后，广告和追踪器会在所有应用和所有网络中被拦截，且无需后台运行任何应用。

1. 打开 _设置 → 网络与互联网_。在某些手机上，该选项为 _连接_ 或 _连接与共享_。
2. 点击 _专用 DNS_。在三星手机上，该选项位于 _更多连接设置_ 下。
3. 选&#x62E9;_&#x79C1;有 DNS 提供商主机名_。
4. 输入您的 Blokada DNS 名称 {% dot %} 并点&#x51FB;_&#x4FDD;存_。

如果找不到该选项，请在设置应用中搜索“私有 DNS”。

## 检查其是否有效

打开几个应用或网站，然后在 [仪表板](https://app.blokada.org/stats?src=guides) 的 _活动_ 页面查看。这部手机的查询会显示在那里。

## 如遇问题

- **“无法连接”或无网络：** 请检查你的 Blokada DNS 名称是否有拼写错误。必须与上方显示的完全一致，不要包含 `https://`。
- **另一个 VPN 应用正在运行：** 部分 VPN 应用会使用其自有 DNS 并绕过专用 DNS。关闭 VPN 的 DNS 或广告拦截设置，或改用 Blokada 6。
- **Chrome 仍显示广告：** Chrome 可能设置了自有安全 DNS 供应商，导致绕过专用 DNS。在 Chrome 中，打开 _设置 → 隐私和安全 → 启用安全 DNS_ 并选择 _使用你当前的服务提供商_，这样 Chrome 将遵循专用 DNS。
