---
title: Android üzerinde Blokada Cloud ile Özel DNS'i Kurun
description: Android'in yerleşik Özel DNS ayarını Blokada Cloud ile kullanarak tüm uygulamalarda, Wi-Fi ve mobil veride reklamları ve izleyicileri engelleyin. Ya da bunu Blokada 6 uygulamasına bırakın.
updated: 2026-10-02
order: 5
---

## En kolay yol: uygulama

[Blokada 6](https://go.blokada.org/play_cloud) sizin için her şeyi ayarlar, engellemeyi tek dokunuşla açıp kapatır ve telefonda nelerin engellendiğini gösterir. Hesap kimliğinizle oturum açın ve işlem tamam.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Blokada 6'yı Google Play'den edinin</a></p>

## Uygulama olmadan: Özel DNS

Android 9 ve sonrası sürümlerde bir _Özel DNS_ ayarı var. Bunu Blokada Cloud olarak ayarlayın ve tüm uygulamalarda, her ağda, arka planda hiçbir şey çalışmadan reklamlar ve izleyiciler engellensin.

1. _Ayarlar → Ağ ve internet_ bölümünü açın. Bazı telefonlarda bu _Bağlantılar_ veya _Bağlantı & paylaşım_ olarak geçer.
2. _Özel DNS_'e dokunun. Samsung telefonlarda bu, _Diğer bağlantı ayarları_ altında bulunur.
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

Eğer bulamazsanız, Ayarlar uygulamasında "Özel DNS" arayın.

## Çalışıp çalışmadığını kontrol edin

Birkaç uygulama veya web sitesi açın, ardından [kontrol panelindeki](https://app.blokada.org/stats?src=guides) _Etkinlik_ sayfasına bakın. Bu telefonun sorguları orada gösterilecek.

## Bir şey çalışmıyorsa

- **"Bağlanılamadı" veya internet yok:** Blokada DNS adınızda yazım hatası olup olmadığını kontrol edin. Yukarıda gösterildiği gibi, `https://` olmadan tam olarak girilmelidir.
- **Başka bir VPN uygulaması aktif:** Bazı VPN uygulamaları kendi DNS'ini kullanır ve Özel DNS'i atlar. VPN'in DNS veya reklam engelleme ayarını kapatın ya da bunun yerine Blokada 6'yı kullanın.
- **Chrome hâlâ reklam gösteriyor:** Chrome, kendi güvenli DNS sağlayıcısına ayarlanmış olabilir ve bu da Özel DNS'i atlatır. Chrome'da, _Ayarlar → Gizlilik ve güvenlik → Güvenli DNS kullan_ seçeneğine girin ve _Mevcut hizmet sağlayıcınızı kullanın_ seçeneğini seçin. Böylece Chrome, Özel DNS'i takip eder.
