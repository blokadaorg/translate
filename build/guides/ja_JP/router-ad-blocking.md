---
title: ルーターの広告ブロックでネットワーク全体の広告をブロックする
description: Blokada Cloud を一度ルーターに設定すれば、広告ブロッカーを実行できないテレビやゲーム機、スマートスピーカーなどを含め、家庭内のすべてのデバイスが保護されます。
updated: 2026-10-02
order: 4
---

ネットワーク上のすべてのデバイスは、どの DNS サーバーを使うかルーターに問い合わせます。ルーターに Blokada Cloud を設定することで、その背後にいるすべてのデバイスで広告やトラッカーをブロックできます。これには、広告ブロッカーアプリを動かせないスマートテレビやゲーム機、ストリーミングスティック、スマートホーム機器も含まれます。

## ルーターに必要な条件

ルーターは、**ホスト名付きの暗号化DNS**、つまりDNS over TLS（DoT）またはDNS over HTTPS（DoH）に対応している必要があります。多くの最新ルーターが対応しており、以下のモデルも含まれます。ご利用のルーターがどちらに対応しているかによって、上記「あなたの詳細」に記載されているDNS名、またはDoHリンクが必要です。

<div class="note important">

**IP アドレスのみ？** 一部のプロバイダーレンタルルーターでは、DNS にプレーンな IP アドレスしか指定できません。今後サポート予定ですが、それまではデバイスごとに個別設定してください: [Android](../android-private-dns/)、[Mac および Apple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/)、および [ブラウザー](../browser-dns-over-https/)。また、[Pi-hole ガイド](../switch-from-pihole/)の手順に従い、Raspberry Pi 上で小さなフォワーダーを動かすこともできます。

</div>

## FRITZ!Box

FRITZ!OS 7.20 以降。

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. 「DNS サーバーの解決済み名」には {% dot %} のみを入力してください。**ほかのエントリーはすべて削除してください。** FRITZ!Box はリスト内の全てのリゾルバーを使用し、他のエントリーがあると広告がブロックされません。
4. Tick _Enforce certificate verification for encrypted name resolution_.
5. 「DNS 障害時にパブリック DNS サーバーへフェイルオーバーする」という設定があれば、オフにしてください。
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - アドレス: {% ip "dot" %}
   - TLS ホスト名: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. 「サービス → HTTPS DNS プロキシ」を開きます。他プロバイダーのインスタンスは削除してください。
3. カスタムリゾルバーURLでインスタンスを追加: {% doh %}
4. 「保存して適用」。このパッケージは自動的に dnsmasq を適切に設定します。

## その他のルーター

「DNS over TLS」「Private DNS」「Encrypted DNS」「DNS over HTTPS」などの設定を探してください。上記のBlokada DNS名またはDoHリンクを入力し、他のDNSサーバー（フォールバックも含む）はすべて削除してください。

## 動作確認

1. デバイスを再起動するか、そのデバイスのWi-Fiを一度オフにしてからオンにし、変更を反映させてください。
2. 少しブラウジングしたのち、ダッシュボードの「アクティビティ」ページを開いてください。ネットワークの問い合わせ履歴がそこに表示されます。

## 一部のデバイスで広告が表示される場合

一部のデバイスではルーターをバイパスします。例：_プライベート DNS_ が設定されたスマートフォン、別のプロバイダーの _セキュア DNS_ を設定したブラウザー、自分自身で DNS をハードコードしているデバイスなどです。これらはデバイス本体で設定するか、独自の DNS 設定を無効にしてください。

<div class="note tip">

ルーターの背後では、すべてのデバイスが1つのアドレスを共有するため、ダッシュボード上ではネットワークが1つのデバイスとして表示されます。個別に確認したい場合は、スマートフォンやノートパソコンにそれぞれBlokada DNS名を設定してください。それらのデバイスは家庭外でもブロックが有効です。

</div>
