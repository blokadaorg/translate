---
title: ハードウェア不要のPi-hole代替ソリューション
description: ご家庭の広告ブロックをPi-holeからBlokada Cloudへ移行、またはPi-holeを維持したままその問い合わせをBlokada経由に送信できます。
updated: 2026-10-02
order: 1
---

Pi-holeは、Raspberry Piが稼働・更新され自宅にある限り、ネットワーク上の全デバイスの広告をブロックします。Blokada Cloudは、弊社サーバーから同様の機能を提供します：

- **ボックスの管理が不要。** SDカードも、アップデートも不要で、Piがダウンしても停止しません。
- **外出先でも有効。** スマートフォンやノートパソコンは、モバイルデータや他のWi-Fiネットワークでもブロック機能が維持されます。
- **暗号化済み。** デバイスはDNS over TLSやDNS over HTTPSを使ってBlokadaと通信するため、プロバイダーが問い合わせ内容を読み取ったり改ざんしたりできません。
- **一括管理ダッシュボード。** ブロックリスト、許可/ブロック済みドメイン、デバイスごとのアクティビティが [app.blokada.org](https://app.blokada.org/?src=guides) で管理できます。

切り替え方法は2つあります。Pi-holeを完全にBlokada Cloudに置き換えることも、そのまま残してBlokada Cloudを上流として利用することもできます。

## 方法1：Pi-holeを置き換える

1. **Blokada Cloudを取得**してダッシュボードを開きます。DNS名とDoHリンクは、そこ&#x3067;_&#x53;etu&#x70;_&#x306E;下、または上&#x8A18;_&#x59;our detail&#x73;_&#x306B;あります。
2. **ルーターのDNSをPi-holeからBlokadaに切り替えます。** [ルーターガイド](../router-ad-blocking/)を参照してください。ルーターがDNSサーバーにプレーンなIPアドレスしか指定できない場合は、各デバイスごとに設定してください：[Android](../android-private-dns/)、[MacやApple TV](../apple-devices/)、[Windows](../windows-dns-over-https/)、[Linux](../linux-dns-over-tls/)、[ブラウザー](../browser-dns-over-https/)。
3. **Pi-holeがDHCPサーバーの場合は、** Piをオフにす&#x308B;_&#x524D;_&#x306B;ルーターでDHCPを再度オンにしてください。そうしないとデバイスがネットワークアドレスを取得できなくなります。
4. **リストを移行。** ダッシュボード&#x306E;_&#x42;locklist&#x73;_&#x3067;ブロックリストを選択し、_Exception&#x73;_&#x3067;許可ドメインやブロックドメインを追加してください。
5. **Pi-holeをオフにする**、または他の目的で残しておくこともできます。

<div class="note aside">

Pi-holeはネットワーク上の全デバイスをIPアドレスで表示していました。一方、Blokadaでは各デバイスが自分専用のBlokada DNS名を使っていれば、それぞれ名前で表示されます。ルーターを1つのBlokada DNS名で設定した場合、1つのデバイスとして表示されます。

</div>

## 方法2：Pi-holeを維持し、Blokada Cloudを上流に設定する

ローカル設定（ローカルホスト名、DHCP、自作のリストなど）を維持したい場合は、Pi-holeでのクエリを暗号化された接続でBlokadaに転送できます。Pi-hole自体には暗号化転送の機能がないため、隣に小さなフォワーダーを動作させます。このガイドでは、[dnsproxy](https://github.com/AdguardTeam/dnsproxy)という単一ファイルのオープンソースのフォワーダーを使用します。

1. Pi-holeマシン上で、CPUに合った `dnsproxy` リリース（最新Raspberry Piなら `linux-arm64`）をリリースページからダウンロードし、`dnsproxy` バイナリを `/usr/local/bin/` にコピーします。
2. `/etc/systemd/system/dnsproxy.service` を作成：

<pre><code>[Unit]
Description=Blokada Cloud への暗号化DNSフォワーダー
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. 起動： `sudo systemctl enable --now dnsproxy`
4. Pi-holeの管理画面で _設定 → DNS_ を開きます。全ての上流サーバーのチェックを外し、カスタム上流サーバーとして `127.0.0.1#5054` を追加してください。保存します。
5. ダッシュボード&#x306E;_&#x30A2;クティビテ&#x30A3;_&#x30DA;ージで確認できます。ご家庭のネットワークからの問い合わせが表示されます。

Pi-hole独自のブロックリストは無効にしてダッシュボードでブロックを管理するか、両方併用もできます。

## よくあるご質問

**Blokada Plusは必要ですか？** 必要ありません。Blokada Cloudがご家庭全体のDNSブロックをカバーします。[Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides)は追加でVPN機能を提供します。

**Blokadaに接続できない場合はどうなりますか？** Pi-holeがダウンしたときと同様、Blokadaが復旧するまでデバイスは名前解決できません。セカンダリの（無フィルターの）DNSサーバーをフォールバックとして追加しないでください。多くのデバイスはすべてのDNSサーバーをランダムに利用するため、広告が通過してしまいます。
