---
title: Chrome, Firefox, Edge ve Brave'de DNS over HTTPS kullanarak reklamları engelleyin
description: Blokada Cloud'u tarayıcınızda güvenli DNS sağlayıcısı olarak ayarlayın ve reklamları ile takipçileri engelleyin; uygulama yüklemenin mümkün olmadığı iş bilgisayarları dahil herhangi bir bilgisayarda kullanılabilir.
updated: 2026-10-02
order: 7
---

Modern tarayıcılar, kendi şifreli DNS sağlayıcılarını kullanabilir; buna _güvenli DNS_ veya _DNS over HTTPS_ denir. Blokada Cloud'u ayarlayın, ardından tarayıcı herhangi bir ağda uygulama yüklemeye gerek kalmadan reklam ve takipçileri engeller.

Bu ayar yalnızca bu tarayıcıyı kapsar. Tüm bilgisayarı kapsaması için, Mac'te [Apple profilini](../apple-devices/) kullanın veya [yönlendirici](../router-ad-blocking/) ayarlayın.

## Chrome

1. `chrome://settings/security` adresini açın.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. {% doh %} girin

## Edge

1. `edge://settings/privacy` adresini açın.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. `brave://settings/security` adresini açın.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. {% doh %} girin

## Safari

Safari'nin kendi güvenli DNS ayarı yoktur. Sistem DNS'ini kullanır, bu yüzden [Apple profilini](../apple-devices/) yükleyin.

## Çalışıp çalışmadığını kontrol et

Bir dakika gezinin, ardından [kontrol panelindeki](https://app.blokada.org/stats?src=guides) _Etkinlik_ sayfasını açın. Bu tarayıcının sorgulamaları orada görüntülenecektir.

## Bir şey çalışmazsa

<div class="note tip">

Tarayıcınız iş veya okul tarafından yönetiliyorsa, güvenli DNS ayarı kilitli olabilir. Yöneticinize danışın.

</div>
