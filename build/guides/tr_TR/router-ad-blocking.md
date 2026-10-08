---
title: Tüm ağınızda reklamları yönlendirici ile engelleyin.
description: Blokada Cloud'u yönlendiricinize bir kez kurun, evdeki tüm cihazlarınız - reklam engelleyici çalıştıramayan TV'ler, oyun konsolları ve akıllı hoparlörler dahil - korunur.
updated: 2026-10-02
order: 4
---

Ağınızdaki her cihaz hangi DNS sunucusunun kullanılacağını yönlendiricinize sorar. Yönlendiricinizi Blokada Cloud'a yönlendirin, ardından arkasındaki tüm cihazlarda reklamlar ve izleyiciler engellenir. Bu, reklam engelleyici uygulamasını çalıştıramayan akıllı TV'ler, oyun konsolları, yayın çubukları ve akıllı ev cihazlarını da içerir.

## Yönlendiricinizin ihtiyacı olanlar

Yönlendiriciniz **ana bilgisayar adı ile şifrelenmiş DNS** desteklemelidir, yani DNS over TLS (DoT) veya DNS over HTTPS (DoH). Birçok yeni yönlendirici bu özelliği desteklemektedir, aşağıdaki modeller dahil. Sizin yönlendiriciniz hangisini destekliyorsa, _Yukarıdaki bilgileriniz_ kısmında bulunan DNS adınızı veya DoH bağlantınızı kullanmalısınız.

<div class="note important">

**Yalnızca sade IP adresleri mi?** Birçok internet sağlayıcı yönlendiricisi DNS için yalnızca IP adreslerini kabul eder. Bu tip cihazlar için destek yakında gelecek. O zamana kadar, cihazlarınızı tek tek ayarlayın: [Android](../android-private-dns/), [Mac ve Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) ve [tarayıcılar](../browser-dns-over-https/). Ayrıca [Pi-hole rehberinde](../switch-from-pihole/) anlatıldığı şekilde bir Raspberry Pi üzerinde küçük bir yönlendirici de çalıştırabilirsiniz.

</div>

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

_DNS over TLS_, _Özel DNS_, _Şifreli DNS_ veya _DNS over HTTPS_ adında bir ayar arayın. Yukarıdan Blokada DNS adınızı veya DoH bağlantınızı girin ve diğer tüm DNS sunucularını, yedek sunucular dahil, kaldırın.

## Çalışıp çalışmadığını kontrol edin

1. Bir cihazı yeniden başlatın veya Wi-Fi'ını kapatıp açın ki değişikliği alsın.
2. Bir dakika gezin, ardından kontrol panelindeki _Etkinlik_ sayfasını açın. Ağınıza ait sorgulamalar burada görünür.

## Bazı cihazlar hâlâ reklam gösteriyorsa

Bazı cihazlar yönlendiriciyi atlar: _Özel DNS_ ayarlı telefonlar, başka bir sağlayıcıya ayarlı güvenli DNS'e sahip tarayıcılar ve kendi DNS ayarını sabitleyen cihazlar. Bu cihazları doğrudan kendilerinde ayarlayın ya da bu DNS ayarını kapatın.

<div class="note tip">

Yönlendiricinin arkasında tüm cihazlar tek bir adresi paylaşır, bu yüzden kontrol paneli ağınızı tek bir cihaz olarak gösterir. Telefon ve dizüstü bilgisayarlarınızı ayrı görmek isterseniz onları kendi Blokada DNS adıyla ayarlayın. Ayrıca evden çıktıklarında da engelleme devam eder.

</div>
