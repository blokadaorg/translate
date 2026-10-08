---
title: MacおよびApple TVでBlokada DNSプロファイルを使って広告をブロックする
description: Blokada Cloud DNSプロファイルをインストールすることで、MacやApple TV全体で広告やトラッカーをブロックし、暗号化されたDNSを利用しつつバックグラウンドで何も動作しません。
updated: 2026-10-02
order: 6
---

Appleデバイスは構成プロファイルを使ってシステム全体で暗号化DNSを利用できます。Blokadaプロファイルは端末をBlokada Cloudに向け、全てのアプリやブラウザー内の広告やトラッカーをブロックします。

macOS 11（Big Sur）、tvOS 14、iOSおよびiPadOS 14以降で動作します。

<div class="if-no-device">

このページはまだあなたのデバイスを認識していないため、プロファイルを提供できません。ダッシュボードにサインインし、［セットアップ］を開き、デバイスを選んでこのガイドを［他のデバイスで開く］からアクセスしてください。

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">プロファイルリンクを取得</a></p>

</div>

## iPhoneとiPad

最も簡単なのはアプリを使う方法です。[Blokada 6](https://go.blokada.org/appstore)を使えば、すべての設定が自動化され、ワンタップでブロックのオン/オフやブロックされたものの確認が端末上でできます。アカウントIDでサインインするだけで完了です。

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">App StoreでBlokada 6を入手</a></p>

### アプリを使わない場合

代わりにプロファイルをインストールすることもできます。iPhoneとiPadは、**Safari**からのみプロファイルをインストールできます。

<div class="if-device">
<div class="if-other-browser note important">

このページは別のブラウザーで開かれています。リンクをコピーしてSafariで開いて続行してください: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. 「設定」を開きます。上部近くにある「プロファイルがダウンロード済み」をタップします。また、「一般」→「VPNとデバイス管理」でも見つかります。
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}プロファイルをダウンロード{% endappleProfile %}</p>

## Mac

1. 下のボタンをクリックしてプロファイルをダウンロードしてください。
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}プロファイルをダウンロード{% endappleProfile %}</p>

## Apple TV

Apple TVではウェブページを開けないため、プロファイルリンクを手入力します。

1. あなたのプロファイルリンク: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. 「Apple TV分析を共有」をハイライトしますが、選択しません。かわりにリモコンの再生/一時停止ボタンを押します。
4. 「プロファイル追加」を選び、自分のプロファイルリンクを入力します。入力はiPhoneのキーボードプロンプトを使うと簡単で、貼り付けもできます。プロファイルをインストールし、確認してください。

<div class="note aside">

**Apple TVや他の家庭内デバイス:** [ルーター](../router-ad-blocking/)でBlokada Cloudを設定すると、Apple TVも含めて全てのデバイスが保護されます。

</div>

## 動作確認方法

少しブラウズしてから、[dashboard](https://app.blokada.org/stats?src=guides)&#x306E;_&#x30A2;クティビテ&#x30A3;_&#x30DA;ージを開いてください。この端末の参照履歴が表示されます。

後でBlokadaを削除するには、インストールしたプロファイルを削除してください。
