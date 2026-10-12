---
title: ルーターの広告ブロックでネットワーク全体の広告をブロックする
description: Blokada Cloud を一度ルーターに設定すれば、広告ブロッカーを実行できないテレビやゲーム機、スマートスピーカーなどを含め、家庭内のすべてのデバイスが保護されます。
updated: 2026-10-09
order: 4
---

ネットワーク上のすべてのデバイスは、どの DNS サーバーを使うかルーターに問い合わせます。ルーターに Blokada Cloud を設定することで、その背後にいるすべてのデバイスで広告やトラッカーをブロックできます。これには、広告ブロッカーアプリを動かせないスマートテレビやゲーム機、ストリーミングスティック、スマートホーム機器も含まれます。

## ルーターに必要な条件

ルーターの設定方法は次の2通りあります:

- **ホスト名を使った暗号化DNS**（DNS over TLS（DoT）またはDNS over HTTPS（DoH））。多くの最近のルーターがこれに対応しており、以下の機種も含まれます。お使いのルーターがどちらに対応しているかによって、上記「_Your details_」にあるDNS名またはDoHリンクが必要になります。
- **通常の IPv6 DNS アドレス。** 多くのインターネットプロバイダのルーターは、DNS に通常の IP アドレスのみを受け付けます。もし対応しており、接続に IPv6 がある場合は、Blokada から指定された IPv6 アドレスを入力してください。詳しくは [IP アドレスのみ入力できるルーター](#routers-that-only-take-an-ip-address) をご覧ください。

ルーターが対応している場合は暗号化 DNS を使用してください。検索クエリは Blokada までの間プライバシーが保護されます。

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

_DNS over TLS_、_Private DNS_、_Encrypted DNS_、また&#x306F;_&#x44;NS over HTTP&#x53;_&#x3068;いう設定を探してください。上記からBlokada DNS名またはDoHリンクを入力し、他のすべてのDNSサーバー（フォールバックサーバーを含む）を削除してください。これらの設定がない場合は、下記のプレーンなIPv6アドレスを使用してください。

## IPアドレスのみを設定できるルーター

この設定には、お使いのルーターとインターネット接続がIPv6に対応している必要があります。プレーンなIPv4アドレスへの対応は今後追加予定です。

1. [ダッシュボード](https://app.blokada.org/setup?src=guides)&#x3067;_&#x30BB;ットアッ&#x30D7;_&#x3092;開き、_ルーター、TV、ゲーム&#x6A5F;_&#x3092;選択します。
2. ルーターに、例え&#x3070;_&#x30DB;ームルータ&#x30FC;_&#x306E;ような名前を付けて、_アドレスを取&#x5F97;_&#x3092;選択します。この名前はアクティビティに表示され、後から変更できません。
3. ルーターの設定で、_インターネット_、_WAN_、また&#x306F;_&#x49;Pv&#x36;_&#x306E;下にあることが多いIPv6用のDNSサーバーを探し、そのアドレスを唯一のDNSサーバーとして入力してください。
4. **他のすべてのDNSサーバー（IPv4も含む）を削除してください。** ルーターからIPv4のDNSサーバーを受け取るデバイスは、一部のルックアップをBlokadaを通さずに行うことがあります。ルーターでIPv4 DNSを空欄のままにできない場合は、デバイスごとに次の手順で設定してください：[Android](../android-private-dns/)、[MacおよびApple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/)、および[ブラウザー](../browser-dns-over-https/)。

TVや、手動でDNSサーバーを設定できるゲーム機にも同じ設定が利用できます。それぞれに固有のアドレスを割り当てることで、アクティビティに名前が表示されます。

<div class="note aside">

これらのルックアップは、通常のDNSサーバーと同様に暗号化されずにBlokadaへ送信されます。ルーターがDNS over TLS または DNS over HTTPS をサポートしている場合は、それらを使用してください。

</div>

## 動作確認

1. デバイスを再起動するか、そのデバイスのWi-Fiを一度オフにしてからオンにし、変更を反映させてください。
2. そのデバイスでBlokadaを実行している場合はオフにし、[go.blokada.org/test](https://go.blokada.org/test)を開いてください。DNS通信がBlokadaを経由しているかどうかが表示されます。
3. しばらくブラウジングした後、[ダッシュボード](https://app.blokada.org/stats?src=guides)&#x306E;_&#x30A2;クティビテ&#x30A3;_&#x30DA;ージを開いてください。ネットワークによるルックアップがそこに表示されます。

## 一部のデバイスで広告が表示される場合

一部のデバイスではルーターをバイパスします。例：_プライベート DNS_ が設定されたスマートフォン、別のプロバイダーの _セキュア DNS_ を設定したブラウザー、自分自身で DNS をハードコードしているデバイスなどです。これらはデバイス本体で設定するか、独自の DNS 設定を無効にしてください。

<div class="note tip">

ルーターの背後では、すべてのデバイスが1つのアドレスを共有するため、ダッシュボード上ではネットワークが1つのデバイスとして表示されます。個別に確認したい場合は、スマートフォンやノートパソコンにそれぞれBlokada DNS名を設定してください。それらのデバイスは家庭外でもブロックが有効です。

</div>
