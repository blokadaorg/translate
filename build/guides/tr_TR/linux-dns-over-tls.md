---
title: DNS over TLS ile Linux üzerinde reklamları engelleyin
description: Blokada Cloud'u şifreli DNS over TLS ile kullanacak şekilde systemd-resolved'u yapılandırın ve Linux bilgisayarınızdaki her uygulama için reklamları ve izleyicileri engelleyin.
updated: 2026-10-02
order: 9},{
---

Güncel Linux dağıtımlarının çoğu, Ubuntu ve Fedora dahil, isim çözmeyi _systemd-resolved_ aracılığıyla gerçekleştirir ve bu, DNS over TLS'i destekler. Debian'da önce `sudo apt install systemd-resolved` ile yükleyin. Blokada Cloud'u gösterin ve bilgisayardaki her uygulama için reklamlar ve takipçiler engellenmiş olur.

## Systemd-resolved'u yapılandırın

1. `sudo mkdir -p /etc/systemd/resolved.conf.d` komutu ile klasörü oluşturun, ardından aşağıdaki ayarlarla `/etc/systemd/resolved.conf.d/blokada.conf` dosyasını oluşturun:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Yeniden başlatın: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Kontrol edin: <code>resolvectl status</code> komutunda <code>+DNSOverTLS</code> ve Blokada sunucusu görüntülenir.</li>
</ol>

`#` işaretinden sonraki kısım sizin Blokada DNS adınızdır: {% dot %} systemd-resolved sunucunun sertifikasını buna karşı kontrol eder ve Blokada, hangi cihazın sorgulama yaptığını bilmek için bunu kullanır.

<div class="note important">

**NetworkManager** ayrıca ağınızın DNS sunucularını iletir. `Domains=~.` tüm sorguları Blokada'ya gönderir, fakat `resolvectl status` bir bağlantıda başka bir sunucu listeliyorsa, o bağlantı için otomatik DNS'i kapatın (IPv4 ve IPv6 ayarlarında _DNS_ yanındaki _Otomatik_ anahtarını kapatın).

</div>

## Systemd-resolved olmadan

`resolvectl` bulunamazsa, dağıtımınız isim çözmeyi başka bir şekilde gerçekleştiriyor demektir. Bunun yerine tarayıcınızda güvenli DNS yapılandırın, [tarayıcı rehberine](../browser-dns-over-https/) bakın veya tüm evi kapsamak için [router](../router-ad-blocking/) üzerinde yapılandırma yapın.

## Çalışıp çalışmadığını kontrol edin

Birkaç web sitesini açın, ardından [gösterge panelindeki](https://app.blokada.org/stats?src=guides) _Etkinlik_ sayfasına bakın. Bu bilgisayardan yapılan sorgulamalar orada görünecektir.

<div class="note aside">

Bu bilgisayarda ayrıca VPN ister misiniz? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) ile tüm trafiği şifreleyen WireGuard kurulumu ve aynı engelleme dahildir.

</div>
