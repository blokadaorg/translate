---
title: Blokada Cloud を使って Android でプライベート DNS を設定する
description: Android の標準プライベート DNS 設定と Blokada Cloud を利用して、すべてのアプリで広告やトラッカーを Wi-Fi とモバイルデータ両方でブロックできます。または、Blokada 6 アプリに任せることもできます。
updated: 2026-10-02
order: 5},{
---

## 最も簡単な方法：アプリ

[Blokada 6](https://go.blokada.org/play_cloud) がすべての設定を行い、ワンタップでブロックのオン／オフ切り替えや、何がブロックされたかを端末で確認できます。アカウント ID でサインインすれば完了です。

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Google Play で Blokada 6 を入手</a></p>

## アプリなしで：プライベート DNS

Android 9 以降には _プライベート DNS_ 設定があります。これを Blokada Cloud に設定すると、すべてのアプリ、すべてのネットワークで、バックグラウンドで何も動かさずに広告やトラッカーがブロックされます。

1. _設定 → ネットワークとインターネット_ を開きます。機種によっては _接続_ または _接続と共有_ の場合もあります。
2. _プライベート DNS_ をタップします。Samsung の場合は _接続の詳細設定_ の下にあります。
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

見つからない場合は、設定アプリで「プライベートDNS」と検索してください。

## 動作確認

いくつかのアプリやウェブサイトを開いた後、[ダッシュボード](https://app.blokada.org/stats?src=guides) の _アクティビティ_ ページをチェックしてください。この端末の参照履歴が表示されます。

## うまくいかない場合

- **「接続できません」やインターネットが使えない場合：** Blokada DNS 名にタイプミスがないか確認してください。上記とまったく同じで、`https://` を含めてはいけません。
- **他の VPN アプリが有効：** 一部の VPN アプリは独自の DNS を使い、プライベート DNS をバイパスします。VPN の DNS や広告ブロック設定をオフにするか、代わりに Blokada 6 を使ってください。
- **Chrome でまだ広告が表示される場合：** Chrome が独自のセキュア DNS プロバイダーを使う設定になっている可能性があります。Chrome の _設定 → プライバシーとセキュリティ → セキュア DNS を使用_ で _現在のサービスプロバイダを使用_ を選択してください。こうすると Chrome もプライベート DNS に従います。
