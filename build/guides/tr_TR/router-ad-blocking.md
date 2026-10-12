---
title: Tüm ağınızda reklamları yönlendirici ile engelleyin.
description: Blokada Cloud'u yönlendiricinize bir kez kurun, evdeki tüm cihazlarınız - reklam engelleyici çalıştıramayan TV'ler, oyun konsolları ve akıllı hoparlörler dahil - korunur.
updated: 2026-10-09
order: 4
---

Ağınızdaki her cihaz hangi DNS sunucusunun kullanılacağını yönlendiricinize sorar. Yönlendiricinizi Blokada Cloud'a yönlendirin, ardından arkasındaki tüm cihazlarda reklamlar ve izleyiciler engellenir. Bu, reklam engelleyici uygulamasını çalıştıramayan akıllı TV'ler, oyun konsolları, yayın çubukları ve akıllı ev cihazlarını da içerir.

## Yönlendiricinizin ihtiyacı olanlar

Bir yönlendirici kurmanın iki yolu vardır:

- **Bir ana bilgisayar adı ile şifreli DNS**, yani TLS üzerinden DNS (DoT) veya HTTPS üzerinden DNS (DoH). Birçok yeni yönlendirici bunu destekler ve aşağıdaki modeller buna dahildir. Yönlendiricinizin hangisini desteklediğine bağlı olarak, yukarıdaki _Bilgileriniz_ kısmında hem DNS adınıza hem de DoH bağlantınıza ihtiyacınız olacak.
- **Düz bir IPv6 DNS adresi.** Birçok internet sağlayıcı yönlendiricisi, DNS için yalnızca düz IP adreslerini kabul eder. Sizin yönlendiriciniz de böyleyse ve bağlantınız IPv6 ise, Blokada size girmeniz için bir IPv6 adresi sağlar. [Yalnızca IP adresi kabul eden yönlendiriciler](#routers-that-only-take-an-ip-address) bölümüne bakın.

Yönlendiriciniz destekliyorsa şifreli DNS kullanın. Sorgularınız Blokada'ya giderken gizli kalır.

## FRITZ!Box

FRITZ!OS 7.20 veya üzeri.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. _DNS Sunucusunun Çözülen Adları_ bölümüne yalnızca {% dot %} girin. **Diğer tüm girişleri kaldırın.** FRITZ!Box listelenen tüm resolver'ları kullanır ve herhangi başka biri reklamların geçmesine izin verir.
4. Tick _Enforce certificate verification for encrypted name resolution_.
5. _DNS bozulduğunda genel DNS sunucularına geçiş_ seçeneğini görürseniz, bunu kapatın.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Adres: {% ip "dot" %}
   - TLS Ana Bilgisayar Adı: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. _Hizmetler → HTTPS DNS Proxy_'yi açın. Diğer sağlayıcılar için olan örnekleri silin.
3. Özel bir resolver URL'si ile bir örnek ekleyin: {% doh %}
4. _Kaydet & Uygula_. Paket, dnsmasq'u otomatik olarak ona yönlendirir.

## Diğer yönlendiriciler

_DNS over TLS_, _Özel DNS_, _Şifreli DNS_ veya _DNS over HTTPS_ adında bir ayar arayın. Yukarıdan Blokada DNS adınızı veya DoH bağlantınızı girin ve tüm diğer DNS sunucularını, yedek sunucular dahil, kaldırın. Böyle bir ayar yoksa, aşağıdaki gibi düz bir IPv6 adresi kullanın.

## Yalnızca bir IP adresi kabul eden yönlendiriciler

Yönlendiricinizin ve internet bağlantınızın bunun için IPv6 desteklemesi gerekir. Düz IPv4 adresleri desteği daha sonra eklenecektir.

1. [Pano](https://app.blokada.org/setup?src=guides) üzerinden _Kurulum_ bölümünü açın ve _Yönlendirici, TV, oyun konsolu_ seçeneğini seçin.
2. Yönlendiriciye bir isim verin, örneğin _Ev yönlendiricisi_, ve _Adres al_ seçeneğini seçin. Bu isim etkinliğinizde görünecek ve daha sonra değiştirilemez.
3. Yönlendiricinin ayarlarında, genellikle _İnternet_, _WAN_ veya _IPv6_ altında, IPv6 için DNS sunucularını bulun ve adresi tek DNS sunucusu olarak girin.
4. **Diğer tüm DNS sunucularını, IPv4 olanlar dahil kaldırın.** Yönlendiriciden halen bir IPv4 DNS sunucusu alan cihazlar bazı sorguları Blokada'nın dışından gönderir. Eğer yönlendirici IPv4 DNS'yi boş bırakmaya izin vermiyorsa, cihazlarınızı tek tek yapılandırın: [Android](../android-private-dns/), [Mac ve Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) ve [tarayıcılar](../browser-dns-over-https/).

TV veya elle DNS sunucusu girebileceğiniz bir oyun konsolu için de aynı kurulum geçerlidir. Her biri için ayrı bir adres girin, böylece etkinliğinizde ismiyle görünsün.

<div class="note aside">

Bu sorgular şifrelemesiz olarak Blokada'ya iletilir, tıpkı herhangi bir düz DNS sunucusunda olduğu gibi. Eğer yönlendiriciniz DNS over TLS veya DNS over HTTPS destekliyorsa, bunun yerine onu kullanın.

</div>

## Çalışıp çalışmadığını kontrol edin

1. Bir cihazı yeniden başlatın veya Wi-Fi'ını kapatıp açın ki değişikliği alsın.
2. Cihazda Blokada çalışıyorsa kapatın, sonra [go.blokada.org/test](https://go.blokada.org/test) adresini açın. DNS'inizin Blokada üzerinden gidip gitmediğini gösterir.
3. Bir dakika dolaşın, ardından [pano](https://app.blokada.org/stats?src=guides) üzerinden _Etkinlik_ sayfasını açın. Ağınızın sorguları burada görüntülenir.

## Bazı cihazlar hâlâ reklam gösteriyorsa

Bazı cihazlar yönlendiriciyi atlar: _Özel DNS_ ayarlı telefonlar, başka bir sağlayıcıya ayarlı güvenli DNS'e sahip tarayıcılar ve kendi DNS ayarını sabitleyen cihazlar. Bu cihazları doğrudan kendilerinde ayarlayın ya da bu DNS ayarını kapatın.

<div class="note tip">

Yönlendiricinin arkasında tüm cihazlar tek bir adresi paylaşır, bu yüzden kontrol paneli ağınızı tek bir cihaz olarak gösterir. Telefon ve dizüstü bilgisayarlarınızı ayrı görmek isterseniz onları kendi Blokada DNS adıyla ayarlayın. Ayrıca evden çıktıklarında da engelleme devam eder.

</div>
