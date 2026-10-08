---
title: DNS over TLS で Linux の広告をブロックする
description: systemd-resolved を設定して、暗号化された DNS over TLS 経由で Blokada Cloud を使用し、Linux コンピューターのすべてのアプリで広告やトラッカーをブロックします。
updated: 2026-10-02
order: 9
---

最新の Linux ディストリビューション（Ubuntu や Fedora を含む）の多くは、_systemd-resolved_ で名前解決を行い、DNS over TLS に対応しています。Debian では、まず `sudo apt install systemd-resolved` でインストールしてください。Blokada Cloud を指定すると、このコンピューターのすべてのアプリで広告やトラッカーがブロックされます。

## systemd-resolved を設定する

1. `sudo mkdir -p /etc/systemd/resolved.conf.d` でフォルダーを作成し、次の設定で `/etc/systemd/resolved.conf.d/blokada.conf` ファイルを作成します:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns=\"dot\">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>再起動: <code>sudo systemctl restart systemd-resolved</code></li>
<li>確認: <code>resolvectl status</code> で <code>+DNSOverTLS</code> と Blokada サーバーが表示されます。</li>
</ol>

`#` の後の部分があなたの Blokada DNS 名です。{% dot %} systemd-resolved はサーバーの証明書をそれと照合し、Blokada はどのデバイスからの問い合わせかを特定します。

<div class="note important">

**NetworkManager** もネットワークの DNS サーバーを設定します。`Domains=~.` で全ての名前解決が Blokada に送信されますが、`resolvectl status` でまだ他のサーバーが接続に表示される場合は、その接続の自動 DNS をオフにしてください（IPv4 および IPv6 設定&#x306E;_&#x44;NS_ の隣にあ&#x308B;_&#x81EA;&#x52D5;_&#x30B9;イッチをオフ）。

</div>

## systemd-resolved を使わない場合

`resolvectl` が見つからない場合は、お使いのディストリビューションは別の方法で名前解決を行っています。その場合は、[ブラウザーガイド](../browser-dns-over-https/)のようにブラウザーでセキュア DNS を設定するか、[ルーター](../router-ad-blocking/)で自宅全体をカバーできるよう設定してください。

## 動作確認

いくつかのウェブサイトを開いたあと、[ダッシュボード](https://app.blokada.org/stats?src=guides)&#x306E;_&#x30A2;クティビテ&#x30A3;_&#x30DA;ージを確認してください。このコンピューターの名前解決履歴が表示されます。

<div class="note aside">

このコンピューターでも VPN を利用したい場合は、[Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides)で WireGuard を使った通信全体の暗号化と同じ広告ブロック機能が利用できます。

</div>
