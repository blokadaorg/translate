---
title: Her cihazda aynı kuruluma sahip bir NextDNS alternatifi
description: NextDNS'den Blokada Bulut'a geçin. Telefonunuzda, bilgisayarınızda ve yönlendiricinizde NextDNS DNS adınızı, DoH bağlantınızı veya profilinizi Blokada'nınkiyle değiştirin ve reklam engellemeyi sürdürün.
updated: 2026-10-02
order: 3
---

NextDNS ve Blokada Bulut aynı şekilde çalışır: ad ile reklamları ve takipçileri engelleyen, kendi ayarlarınızın kişisel bir DNS adı arkasında saklandığı şifreli bir DNS hizmeti. Geçiş yapmak, her cihazdaki NextDNS değerlerini Blokada'nızla değiştirmek demektir. Cihazda başka hiçbir şey değişmez.

## Kullandığınız şey ve Blokada'da seçmeniz gereken

| NextDNS'te                                                | Blokada Bulut'ta                                                            |
| --------------------------------------------------------- | --------------------------------------------------------------------------- |
| Yapılandırma kimliğiniz, örn. `abc123`    | Blokada DNS adınızın ve DoH bağlantınızın bir parçası olan cihaz etiketiniz |
| _Gizlilik_ engel listeleri                                | Paneldeki _Engel listeleri_                                                 |
| _Güvenlik_ (zararlı yazılım, oltalama) | _Engel listeleri_ altında bir zararlı yazılım listesi                       |
| _Ebeveyn kontrolü_                                        | _Engel listeleri_ altında yetişkin içerik ve bahis listeleri                |
| _İzin listesi_ ve _Engel listesi_                         | Paneldeki _İstisnalar_                                                      |
| _Günlükler_ ve _Analitikler_                              | Paneldeki _Etkinlik_ ve _İstatistikler_                                     |

## Her cihazı değiştirin

Cihaza bağlı olarak, hem _Yukarıdaki bilgileriniz_ kısmında bulunan DNS adınıza hem de DoH bağlantınıza ihtiyacınız olacak.

### Android

_Özel DNS_ ile `<your-id>.dns.nextdns.io` kullandıysanız, bunu Blokada DNS adınız ile değiştirin; ayrıntılar için [Android rehberi](../android-private-dns/)ne bakın. NextDNS uygulamasını kullandıysanız, kaldırıp yerine [Blokada 6](https://go.blokada.org/play_cloud) yükleyin.

### iPhone ve iPad

NextDNS uygulamasını kullandıysanız, kaldırıp yerine [Blokada 6](https://go.blokada.org/appstore) yükleyin. Bunun yerine NextDNS profili yüklediyseniz, _Ayarlar → Genel → VPN ve Aygıt Yönetimi_ kısmından kaldırın, ardından [Apple rehberi](../apple-devices/)ni izleyin.

### Mac ve Apple TV

NextDNS profilini veya uygulamasını kaldırın, ardından [Apple rehberi](../apple-devices/) üzerinden Blokada profilini yükleyin.

### Windows ve Linux

NextDNS uygulamasını kullanıyorsanız kaldırın. Windows'ta, NextDNS sunucusunu ve DoH şablonunu Blokada'nınkiler ile değiştirin; ayrıntılar için [Windows rehberi](../windows-dns-over-https/) üzerinden ilerleyin. Linux'ta, systemd-resolved'da NextDNS sunucusunu Blokada'nınkisi ile değiştirin; ayrıntılar için [Linux rehberi](../linux-dns-over-tls/) üzerinden ilerleyin.

### Tarayıcılar

Tarayıcınızda _güvenli DNS_ olarak `https://dns.nextdns.io/…` ayarlıysa, bunu DoH bağlantınızla değiştirin; ayrıntılar için [tarayıcı rehberi](../browser-dns-over-https/)ne bakın.

### Yönlendirici

Yönlendiriciniz NextDNS'i DNS over TLS veya DNS over HTTPS üzerinden kullanıyorsa, NextDNS adını veya bağlantısını Blokada’nız ile değiştirin, ayrıntılar için [yönlendirici rehberi](../router-ad-blocking/) üzerinden ilerleyin.

Eğer yönlendiriciniz düz IP adresleri üzerinden _bağlı bir IP_ ile NextDNS kullanıyorsa, Blokada henüz bunu devralamıyor. Düz DNS adreslerine sahip yönlendiriciler için destek yakında gelecek. O zamana kadar cihazlarınızı tek tek ayarlayın veya şifreli DNS destekleyen bir yönlendirici kullanın.

## Çalıştığını kontrol edin

Birkaç web sitesini açın, ardından paneldeki _Etkinlik_ sayfasına bakın. Burada cihazlarınızın sorgularını, engellenenler işaretli olarak görebilirsiniz. Bir cihaz görünmüyorsa, hâlâ NextDNS kullanıyor demektir.
