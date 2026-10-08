---
title: Donanım gerektirmeyen bir Pi-hole alternatifi.
description: Evinizdeki reklam engellemeyi Pi-hole'dan Blokada Cloud'a taşıyın veya Pi-hole'u kullanmaya devam edip sorgularını Blokada üzerinden yönlendirin.
updated: 2026-10-02
order: 1
---

Bir Pi-hole, ağınızdaki tüm cihazlar için reklamları engeller; Raspberry Pi çalıştıkça, güncel ve evde olduğu sürece. Blokada Cloud aynı işi kendi sunucularımızdan yapar:

- **Kutu yok, bakım yok.** SD kart yok, güncelleme yok, Pi kapanınca erişim kesilmez.
- **Evden uzakta da çalışır.** Telefonlar ve dizüstü bilgisayarlar, mobil veri ve farklı Wi-Fi ağlarında da engellemeye devam eder.
- **Şifreli.** Cihazlar Blokada ile DNS over TLS veya DNS over HTTPS üzerinden iletişim kurar, böylece sağlayıcınız sorgularınızı okuyamaz veya değiştiremez.
- **Tek pano.** Engel listeleri, izin verilen ve engellenen alan adları ile cihaz başına etkinlik [app.blokada.org](https://app.blokada.org/?src=guides) adresinden yönetilir.

Geçiş yapmanın iki yolu var. Pi-hole'u tamamen değiştirebilir veya onu tutup Blokada Cloud'u üst DNS olarak kullanabilirsiniz.

## Seçenek 1: Pi-hole'u değiştirin

1. **Blokada Cloud'u edinin** ve panoyu açın. DNS adınız ve DoH bağlantınız _Kurulum_ bölümünde ve üstte _Bilgileriniz_ altında yer alır.
2. **Yönlendiricinizi Pi-hole yerine Blokada'ya yönlendirin.** [Yönlendirici kılavuzunu](../router-ad-blocking/) izleyin. Yönlendiriciniz DNS sunucusu olarak yalnızca düz bir IP adresi kabul ediyorsa, cihazlarınızı tek tek ayarlayın: [Android](../android-private-dns/), [Mac ve Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) ve [tarayıcılar](../browser-dns-over-https/).
3. **Eğer Pi-hole'unuz DHCP sunucusuyduysa,** Pi'yi kapatmadan _önce_ yönlendiricinizde DHCP'yi tekrar etkinleştirin. Aksi takdirde cihazlarınız ağ adresi alamaz.
4. **Listelerinizi taşıyın.** Panoda _Engel listeleri_ bölümünde engel listesi seçip kendi izin verilen veya engellenen alan adlarınızı _İstisnalar_ altında ekleyin.
5. **Pi-hole'u kapatın,** veya başka bir amaç için kullanmaya devam edin.

<div class="note aside">

Pi-hole ağdaki her cihazı IP adresiyle gösteriyordu. Blokada ile her cihaz, kendi Blokada DNS adını kullandığı sürece, ismiyle görünür. Bir yönlendirici tek bir Blokada DNS adıyla yapılandırılırsa tek bir cihaz olarak görünür.

</div>

## Seçenek 2: Pi-hole'u tutun, Blokada Cloud'u üst DNS olarak kullanın

Yerel kurulumunuzu (örneğin yerel ana bilgisayar adları, DHCP veya kendi listeleriniz) korumak istiyorsanız, Pi-hole'un sorgularını şifreli bir bağlantı üzerinden Blokada'ya yönlendirin. Pi-hole şifreli yönlendirmeyi kendisi yapamaz, bu yüzden yanında küçük bir yönlendirici çalışır. Bu rehber, tek dosyadan oluşan açık kaynaklı bir yönlendirici olan [dnsproxy](https://github.com/AdguardTeam/dnsproxy)'yi kullanır.

1. Pi-hole cihazında, işlemcinize uygun (`linux-arm64` yeni Raspberry Pi için) `dnsproxy` sürümünü indirin ve `dnsproxy` dosyasını `/usr/local/bin/` dizinine kopyalayın.
2. `/etc/systemd/system/dnsproxy.service` dosyasını oluşturun:

<pre><code>[Unit]
Description=Şifreli DNS yönlendiricisi Blokada Cloud'a
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Başlatın: `sudo systemctl enable --now dnsproxy`
4. Pi-hole yönetiminde _Ayarlar → DNS_ bölümünü açın. Tüm üst sunucuların işaretini kaldırın ve özel üst sunucu olarak `127.0.0.1#5054` ekleyin. Kaydedin.
5. Pano _Etkinlik_ sayfasını kontrol edin. Artık ağınızdan gelen sorgular burada görüntülenecek.

Pi-hole'un kendi engel listelerini devre dışı bırakıp engellemeyi panodan yönetebilirsiniz veya her ikisini birden kullanabilirsiniz.

## Sıkça sorulanlar

**Blokada Plus'a ihtiyacım var mı?** Hayır. Blokada Cloud, tüm eviniz için DNS engellemesini sağlar. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) ise buna ek olarak bir VPN sunar.

**Blokada'ya ulaşılamazsa ne olur?** Cihazlarınız, Blokada geri gelene kadar isim çözümlenemez; tıpkı Pi-hole kapanınca olduğu gibi. Yedek olarak ikinci, filtresiz bir DNS sunucusu eklemeyin. Çünkü çoğu cihaz tüm sunucuları rastgele kullanır ve reklamlar engellenemez.
