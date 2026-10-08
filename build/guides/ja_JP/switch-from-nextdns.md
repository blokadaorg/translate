---
title: すべてのデバイスで同じ設定を使える NextDNS の代替サービス
description: NextDNS から Blokada Cloud に移行しましょう。電話、コンピューター、ルーターで NextDNS の DNS 名、DoH リンク、またはプロファイルを Blokada のものに入れ替えて、広告ブロック機能を維持できます。
updated: 2026-10-02
order: 3
---

NextDNS と Blokada Cloud は同じ仕組みで動作します。名前ベースで広告やトラッカーをブロックする暗号化 DNS サービスで、各自の設定は個人用 DNS 名で管理されます。切り替え作業は、各デバイスの NextDNS 情報を Blokada の情報に置き換えるだけです。他の端末設定に変更はありません。

## 使用していたものと、Blokada で選択するもの

| NextDNS の場合                       | Blokada Cloud の場合                |
| --------------------------------- | -------------------------------- |
| 設定 ID 例: `abc123` | Blokada DNS 名や DoH リンクの一部である端末タグ |
| _プライバシー_ ブロックリスト                  | ダッシュボード内の _ブロックリスト_              |
| _セキュリティ_（マルウェア、フィッシング）            | _ブロックリスト_ 内のマルウェアリスト             |
| _ペアレンタルコントロール_                    | _ブロックリスト_ 内のアダルト・ギャンブル用リスト       |
| _許可リスト_ と _拒否リスト_                 | ダッシュボード内の _例外_                   |
| _ログ_ および _分析_                     | ダッシュボード内の _アクティビティ_ および _統計_     |

## 各デバイスを切り替える

端末によって、DNS 名または DoH リンクが必要です。どちらも上記 _あなたの詳細_ に記載されています。

### Android

_プライベート DNS_ を `<your-id>.dns.nextdns.io` で利用していた場合は、[Android ガイド](../android-private-dns/) に従い Blokada DNS 名へ切り替えてください。NextDNS アプリを使っていた場合はアンインストールし、代わりに [Blokada 6](https://go.blokada.org/play_cloud) をインストールしてください。

### iPhone と iPad

NextDNS アプリを使っていた場合はアンインストールし、[Blokada 6](https://go.blokada.org/appstore) をインストールしてください。NextDNS のプロファイルをインストールしていた場合は、「設定 → 一般 → VPNとデバイス管理」から削除し、[Apple ガイド](../apple-devices/) の手順に従ってください。

### Mac と Apple TV

NextDNS のプロファイルまたはアプリを削除し、[Apple ガイド](../apple-devices/) に従って Blokada プロファイルをインストールしてください。

### Windows および Linux

NextDNS アプリを使用している場合はアンインストールしてください。Windows では、[Windows ガイド](../windows-dns-over-https/) に従い NextDNS サーバーと DoH テンプレートを Blokada のものへ置き換えてください。Linux では、[Linux ガイド](../linux-dns-over-tls/) に従い、systemd-resolved 内の NextDNS サーバーを Blokada のものに置き換えてください。

### ブラウザー

ブラウザーの _セキュア DNS_ に `https://dns.nextdns.io/…` を設定している場合は、[ブラウザー ガイド](../browser-dns-over-https/) に従い自分の DoH リンクへ置き換えてください。

### ルーター

ルーターが DNS over TLS または DNS over HTTPS 経由で NextDNS を利用している場合は、[ルーターガイド](../router-ad-blocking/) に従い NextDNS の名前またはリンクを Blokada のものに置き換えてください。

_リンク済み IP_ 付きのプレーン IP アドレス経由で NextDNS を使っている場合、Blokada ではまだ対応できません。プレーン DNS アドレス対応ルーターのサポートは今後追加予定です。それまでは各端末ごとに設定するか、暗号化 DNS に対応したルーターをご利用ください。

## 動作確認

いくつかのウェブサイトを開いてから、ダッシュボードの _アクティビティ_ ページを確認してください。そこで各端末のルックアップ履歴が表示され、ブロックされたものはマークで判別できます。端末が表示されなければ、まだ NextDNS を利用している状態です。
