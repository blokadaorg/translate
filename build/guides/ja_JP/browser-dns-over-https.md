---
title: Chrome、Firefox、Edge、BraveでDNS over HTTPSによる広告ブロック
description: アプリをインストールできない職場のノートパソコンなど、あらゆるパソコンのブラウザーで広告やトラッカーをブロックするために、ブラウザーのセキュアDNSプロバイダーとしてBlokada Cloudを設定しましょう。
updated: 2026-10-02
order: 7
---

最新のブラウザーは、「セキュアDNS」または「DNS over HTTPS」と呼ばれる独自の暗号化DNSプロバイダーを利用できます。これをBlokada Cloudに設定すると、拡張機能をインストールせずに、どのネットワーク上でもブラウザーが広告やトラッカーをブロックします。

この設定はこのブラウザーだけに適用されます。パソコン全体に適用するには、Macでは[Appleプロファイル](../apple-devices/)を使用するか、[ルーター](../router-ad-blocking/)のセットアップを行ってください。

## Chrome

1. 「chrome://settings/security」を開きます。
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. {% doh %} を入力

## Edge

1. 「edge://settings/privacy」を開きます。
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. 「brave://settings/security」を開きます。
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. {% doh %} を入力

## Safari

Safari には独自のセキュアDNS設定はありません。システムのDNSを使用するため、[Appleプロファイル](../apple-devices/)をインストールしてください。

## 動作確認

少しブラウジングをした後、[ダッシュボード](https://app.blokada.org/stats?src=guides)の「アクティビティ」ページを開いてください。このブラウザーの問い合わせがそこに表示されます。

## 正しく動作しない場合

<div class="note tip">

ブラウザーが職場や学校で管理されている場合、セキュアDNS設定はロックされている場合があります。管理者にお問い合わせください。

</div>
