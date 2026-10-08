---
title: Mullvad DNS kapanıyor. Reklam engellemenizi Blokada Cloud ile sürdürebilirsiniz
description: Mullvad herkese açık DNS hizmetini 2 Kasım 2026'da kapatıyor. Telefonunuzu, bilgisayarınızı ve yönlendiricinizi o zamandan önce Blokada Cloud'a nasıl taşıyacağınızı, reklam engellemesini kaybetmeden burada bulabilirsiniz.
updated: 2026-10-02
order: 2
---

Mullvad, ücretsiz herkese açık DNS servisini **2 Kasım 2026**'da kapatıyor ve bunun yerine Quad9 öneriliyor. Quad9 zararlı yazılımları engeller fakat reklam veya takipçileri **engellemez**. Mullvad DNS hizmeti durduğunda, ona ayarlı cihazlar internet siteleri ve uygulamaları yüklemeyi durdurur. Cihaz başka bir DNS sunucusuna geçerse, reklamlar geri döner. Bu tarihten önce geçiş yapın.

Bu sayfa, `dns.mullvad.net` ile biten herkese açık DNS adları içindir. Mullvad VPN uygulamasını kapsamaz.

## Kullandığınız ve Blokada'da seçmeniz gerekenler

| Mullvad DNS adı            | Neleri engelledi                       | Blokada pano ekranında                                                                                                                                                     |
| -------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | hiçbir şey                             | Blokada bir filtreleme servisidir. Hiç filtreleme istemiyorsanız, Quad9 ya da servis sağlayıcınızın DNS hizmeti daha basit bir seçenektir. |
| `adblock.dns.mullvad.net`  | reklamlar, takipçiler                  | reklam ve takipçi engel listesi                                                                                                                                            |
| `base.dns.mullvad.net`     | reklamlar, takipçiler, zararlı yazılım | zararlı yazılım listesi ekleyin                                                                                                                                            |
| `extended.dns.mullvad.net` | baz artı sosyal medya                  | sosyal medya listesi ekleyin                                                                                                                                               |
| `family.dns.mullvad.net`   | baz artı yetişkin içeriği ve kumar     | yetişkin içeriği ve kumar listeleri ekleyin                                                                                                                                |
| `all.dns.mullvad.net`      | yukarıdakilerin hepsi                  | hepsini etkinleştirin                                                                                                                                                      |

Pano ekranında _Engel Listeleri_ altında engel listelerini seçebilirsiniz. İstediğiniz zaman değiştirebilirsiniz ve yapılan değişiklikler tüm cihazlarınıza uygulanır.

## Her cihazı değiştirin

Blokada her cihaza kendi adını verir, böylece pano ekranında cihaz başına faaliyet görebilirsiniz. Cihaza göre, DNS adınıza veya DoH bağlantınıza ihtiyacınız olur, ikisi de _Ayrıntılarınız_ kısmında yer alır.

### Android

Mullvad'ın rehberinde _Özel DNS_ altında bir ana makine adı girmeniz isteniyordu. Onun yerine Blokada DNS adınızı girin. [Android rehberi](../android-private-dns/) adımları içerir.

### iPhone, iPad ve Mac

Mullvad'ın kurulumunda bir yapılandırma profili kullanılmıştı. Önce onu kaldırın:

- **iPhone ve iPad:** _Ayarlar → Genel → VPN ve Aygıt Yönetimi_, Mullvad DNS profilini seçin, ardından _Profili Kaldır_'a dokunun.
- **Mac:** profil listesini açın (_Sistem Ayarları → Genel → Aygıt Yönetimi_ macOS 15 ve sonrası için, _Sistem Ayarları → Gizlilik ve Güvenlik → Profiller_ macOS 13 ve 14 için, _Sistem Tercihleri → Profiller_ macOS 12 ve öncesi için), Mullvad DNS profilini seçin ve _−_'ya tıklayın.

Daha sonra [Apple rehberi](../apple-devices/) üzerinden Blokada profilini yükleyin.

### Tarayıcılar

Eğer _güvenli DNS_ veya _HTTPS üzerinden DNS_ altında `https://adblock.dns.mullvad.net/dns-query` gibi bir Mullvad DoH bağlantısı girdiyseniz, onu kendi DoH bağlantınızla değiştirin. Her tarayıcı için adımlar [tarayıcı rehberinde](../browser-dns-over-https/) yer almaktadır.

### Yönlendirici

Eğer yönlendiriciniz Mullvad üzerinden DNS over TLS kullanıyorsa, Mullvad ana makine adını Blokada DNS adınızla değiştirin ve Mullvad'ın IP adreslerini kaldırın. [Yönlendirici rehberi](../router-ad-blocking/) yaygın modelleri kapsar.

## Çalıştığını kontrol edin

Birkaç internet sitesi açın, ardından pano ekranında _Faaliyet_ sayfasına bakın. Burada cihazlarınızın sorgularını ve engellenenleri görebilirsiniz. Bir cihaz görünmüyorsa, hâlâ başka bir DNS sunucusu kullanıyor demektir.
