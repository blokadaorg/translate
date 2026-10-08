---
title: Windows'ta DNS over HTTPS ile reklamları engelleyin
description: Blokada Cloud ile Windows 11'e dahili gelen şifreli DNS'i kullanarak, hiçbir ek yazılım kurmadan her uygulama ve tarayıcıda reklamları ve izleyicileri engelleyin.
updated: 2026-10-02
order: 8},{
---

Windows 11 tüm DNS sorgularını şifreli olarak, DNS over HTTPS üzerinden gönderebilir. Blokada Cloud'u seçerek, bilgisayardaki her uygulama ve tarayıcıda reklamlar ve izleyiciler engellenir, hiçbir şey kurmanıza gerek yoktur.

DNS sunucusunun IP adresine ve DoH bağlantınıza ihtiyacınız olacak, ikisi de yukarıda _Bilgileriniz_ altında bulunur.

## Windows 11

1. _Ayarlar → Ağ ve internet_'i açın, ardından bilgisayarın bağlantı şekline bağlı olarak _Wi-Fi_ veya _Ethernet_'i seçin.
2. Bağlantınızın _Donanım özellikleri_'ni açın. Wi-Fi kullanıyorsanız, _Bilinen ağları yönet_'i ve ardından ağı, ya da Wi-Fi sayfasının üstünde _Donanım özellikleri_'ni seçin.
3. _DNS sunucusu ataması_ yanında, _Düzenle_'yi seçin. _Manuel_'i seçin ve _IPv4_'ü etkinleştirin.
4. _Tercih edilen DNS_ bölümüne DNS sunucusunu girin {% ip "doh" %}
5. _DNS over HTTPS_'i _Açık (manuel şablon)_ olarak ayarlayın ve DoH bağlantınızı {% doh %} _DoH şablonu_ olarak yapıştırın.
6. _Düz metine geri dönüş_ seçeneğini kapatın ve _Kaydet_'i seçin.

Bilgisayar hem Wi-Fi hem de Ethernet kullanıyorsa, diğer bağlantı için de aynı işlemi tekrarlayın.

<div class="note important">

_Alternatif DNS_'i boş bırakın. Windows her iki sunucuyu da kullanır ve diğer herhangi biri reklamların geçmesine izin verir.

</div>

<div class="note tip">

_Açık (manuel şablon)_ seçeneği yok mu? Windows 11'iniz eski. Windows'u güncelleyin veya bu arada [tarayıcı rehberini](../browser-dns-over-https/) kullanın.

</div>

## Windows 10

Windows 10'da dahili şifreli DNS yoktur. Bunun yerine, [tarayıcı rehberi](../browser-dns-over-https/)'ndeki gibi tarayıcınızda güvenli DNS ayarlayın ya da tüm evi kapsaması için [yönlendiricinizi](../router-ad-blocking/) yapılandırın.

## Çalıştığını kontrol edin

Birkaç web sitesi açın, ardından [gösterge panelindeki](https://app.blokada.org/stats?src=guides) _Etkinlik_ sayfasına bakın. Bu bilgisayarın sorgulamaları orada görünür.

<div class="note aside">

Bu bilgisayarda da VPN ister misiniz? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) ile tüm trafiği şifreleyen ve aynı engellemeyi yapan bir WireGuard kurulumu dahildir.

</div>

## Bir şey çalışmıyor mu

Chrome ve Edge'in kendi _güvenli DNS_ ayarı vardır, bu da Windows'u atlatır. Otomatikte bırakılırsa, düz DNS'e geri dönebilir, bu da Blokada tarafından reddedilir. Onun yerine DoH bağlantınızı girin:

- **Chrome:** `chrome://settings/security` adresini açın, _Güvenli DNS kullanımını_ etkinleştirin ve _DNS sağlayıcısı seç_ altında _Özel DNS hizmeti sağlayıcısı ekle_'yi seçin.
- **Edge:** `edge://settings/privacy` adresini açın, güvenli DNS'i etkinleştirin ve _Hizmet sağlayıcısı seç_'i seçin.

Ardından DoH bağlantınızı yapıştırın {% doh %}

Bazı reklamlar hâlâ IPv6 olan bir ağda gösteriliyorsa, Windows yönlendiricinizin IPv6 DNS sunucusuna da sorgu gönderebilir. Adaptör ayarlarından _Internet Protocol Version 6 (TCP/IPv6)_'yı kapatın (_Denetim Masası → Ağ Bağlantıları_) veya [yönlendiricinizi](../router-ad-blocking/) ayarlayın.
