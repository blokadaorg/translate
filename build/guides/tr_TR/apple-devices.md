---
title: Mac ve Apple TV’de Blokada DNS profili ile reklamları engelle
description: Mac veya Apple TV'de reklamları ve izleyicileri sistem genelinde engellemek için şifreli DNS ile hiçbir şey arka planda çalışmadan bir Blokada Cloud DNS profili yükleyin.
updated: 2026-10-02
order: 6
---

Apple cihazları, tüm sistem için şifreli DNS'i bir yapılandırma profiliyle kullanabilir. Blokada profili, cihazı Blokada Cloud'a yönlendirir ve böylece tüm uygulamalarda ve tarayıcılarda reklamlar ve izleyiciler engellenir.

It works on macOS 11 (Big Sur), tvOS 14, iOS ve iPadOS 14 ve sonraki sürümlerde çalışır.

<div class="if-no-device">

Bu sayfa henüz cihazınızı bilmiyor, bu yüzden profiliniz sağlanamaz. Panele giriş yapın, _Kurulum_'u açın, cihazınızı seçin ve bu rehberi _Başka bir cihazda aç_ üzerinden açın.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Profil bağlantımı al</a></p>

</div>

## iPhone ve iPad

En kolay yol uygulamayı kullanmaktır. [Blokada 6](https://go.blokada.org/appstore) tüm ayarları sizin için yapar, engellemeyi tek dokunuşla açıp kapatır ve telefonda nelerin engellendiğini gösterir. Hesap kimliğinizle giriş yapın, işlem tamam.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Blokada 6’yı App Store’dan edinin</a></p>

### Uygulama olmadan

Alternatif olarak profili kurabilirsiniz. iPhone ve iPad, profilleri yalnızca **Safari** üzerinden kurar.

<div class="if-device">
<div class="if-other-browser note important">

Bu sayfa başka bir tarayıcıda açık. Devam etmek için bağlantınızı kopyalayıp Safari'de açın: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. _Ayarlar_'ı açın. Üstteki _Profil İndirildi_'ye dokunun. Ayrıca bunu _Genel → VPN ve Aygıt Yönetimi_ altında da bulabilirsiniz.
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}Profilimi indir{% endappleProfile %}</p>

## Mac

1. Profili indirmek için aşağıdaki butona tıklayın.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Profilimi indir{% endappleProfile %}</p>

## Apple TV

Apple TV web sayfalarını açamaz, bu yüzden profil bağlantınızı elle girmeniz gerekir.

1. Profil bağlantınız: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. _Apple TV Analitiğini Paylaş_'ı vurgulayın. Seçmeyin. Bunun yerine kumandada Oynat/Duraklat tuşuna basın.
4. _Profil Ekle_'yi seçin ve profil bağlantınızı girin. Yazmak, iPhone'unuzda çıkan klavye ile en kolay yöntemdir, buradan yapıştırabilirsiniz. Profili yükleyip onaylayın.

<div class="note aside">

**Apple TV ve evdeki diğer cihazlar:** Eğer Blokada Cloud'u [router](../router-ad-blocking/) üzerinden kurarsanız, Apple TV dahil tüm cihazlar korunmuş olur.

</div>

## Çalıştığını kontrol edin

Biraz gezinin, ardından [paneldeki](https://app.blokada.org/stats?src=guides) _Etkinlik_ sayfasını açın. Bu cihazın sorguları orada gösterilecektir.

Blokada'yı daha sonra kaldırmak için, kurduğunuz yerde profili silin.
