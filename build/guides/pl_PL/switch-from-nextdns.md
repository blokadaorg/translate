---
title: Alternatywa dla NextDNS z identyczną konfiguracją na każdym urządzeniu
description: Przenieś się z NextDNS do Blokada Cloud. Zamień nazwę DNS, link DoH lub profil NextDNS na odpowiednik Blokady na swoim telefonie, komputerze i routerze, aby zachować blokowanie reklam.
updated: 2026-10-01
order: 3
---

NextDNS i Blokada Cloud działają w ten sam sposób: jest to szyfrowana usługa DNS, która blokuje reklamy i trackery po nazwach, z Twoimi ustawieniami dostępnymi przez osobistą nazwę DNS. Przełączenie polega na zastąpieniu wartości NextDNS na każdym urządzeniu tymi od Blokady. Nic innego na urządzeniu się nie zmienia.

## Czego używałeś i co wybrać w Blokadzie

| W NextDNS                                                               | W Blokada Cloud                                                           |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Twój identyfikator konfiguracji, np. `abc123`           | Twój tag urządzenia, będący częścią nazwy DNS Blokady oraz linku DoH      |
| _Prywatnościowe_ listy blokowania                                       | _Listy blokowania_ w panelu sterowania                                    |
| _Bezpieczeństwo_ (złośliwe oprogramowanie, phishing) | lista złośliwego oprogramowania w sekcji _Listy blokowania_               |
| _Kontrola rodzicielska_                                                 | listy treści dla dorosłych i gier hazardowych w sekcji _Listy blokowania_ |
| _Lista dozwolonych_ i _Lista zablokowanych_                             | _Wyjątki_ w panelu sterowania                                             |
| _Logi_ i _Analityka_                                                    | _Aktywność_ i _Statystyki_ w panelu sterowania                            |

## Twoje dane Blokady

- Twoja nazwa DNS Blokady, dla DNS przez TLS: {% dot %}
- Twój link DoH, dla DNS przez HTTPS: {% doh %}

## Zmień każde urządzenie

### Android

Jeśli korzystałeś z _Prywatnego DNS_ i wpisywałeś `<your-id>.dns.nextdns.io`, zamień go na swoją nazwę DNS Blokady, zgodnie z [przewodnikiem dla Androida](../android-private-dns/). Jeśli korzystałeś z aplikacji NextDNS, odinstaluj ją i zainstaluj [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone i iPad

Jeśli korzystałeś z aplikacji NextDNS, odinstaluj ją i zainstaluj [Blokada 6](https://go.blokada.org/appstore). Jeśli zamiast tego zainstalowałeś profil NextDNS, usuń go w _Ustawienia → Ogólne → VPN i Zarządzanie urządzeniem_, a następnie postępuj zgodnie z [przewodnikiem Apple](../apple-devices/).

### Mac i Apple TV

Usuń profil lub aplikację NextDNS, a następnie zainstaluj profil Blokady według [przewodnika Apple](../apple-devices/).

### Windows i Linux

Odinstaluj aplikację NextDNS, jeśli ją używasz. Na Windows zamień serwer NextDNS i szablon DoH na Blokady, zgodnie z [przewodnikiem dla Windows](../windows-dns-over-https/). Na Linuksie zamień serwer NextDNS w systemd-resolved, zgodnie z [przewodnikiem dla Linuksa](../linux-dns-over-tls/).

### Przeglądarki

Jeśli ustawiłeś `https://dns.nextdns.io/…` jako _bezpieczny DNS_ przeglądarki, zamień go na swój link DoH, zgodnie z [przewodnikiem dla przeglądarki](../browser-dns-over-https/).

### Router

Jeśli Twój router używa NextDNS przez DNS przez TLS lub DNS przez HTTPS, zamień nazwę lub link NextDNS na swój odpowiednik z Blokady, zgodnie z [przewodnikiem routera](../router-ad-blocking/).

Jeśli używa NextDNS przez zwykłe adresy IP z _powiązanym IP_, Blokada jeszcze tego nie obsługuje. Wsparcie dla routerów ze zwykłymi adresami DNS jest w drodze. Do tego czasu skonfiguruj każde urządzenie osobno albo użyj routera obsługującego szyfrowany DNS.

## Sprawdź, czy działa

Otwórz kilka stron internetowych, a następnie sprawdź stronę _Aktywność_ w panelu. Zobaczysz tam zapytania urządzeń, z oznaczeniem tych zablokowanych. Jeśli dane urządzenie się nie pojawia, nadal używa NextDNS.
