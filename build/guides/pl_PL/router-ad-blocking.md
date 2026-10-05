---
title: Blokuj reklamy w całej swojej sieci dzięki blokowaniu reklam na routerze.
description: Skonfiguruj Blokada Cloud na swoim routerze tylko raz, a każde urządzenie w domu będzie chronione, w tym telewizory, konsole do gier i inteligentne głośniki, które nie mogą uruchamiać blokera reklam.
updated: 2026-10-02
order: 4
---

Każde urządzenie w Twojej sieci pyta router, z którego serwera DNS ma korzystać. Skieruj router na Blokada Cloud, a reklamy i trackery zostaną zablokowane dla wszystkiego za nim. Dotyczy to również smart TV, konsol do gier, sticków do streamingu oraz urządzeń smart home, które nie mają możliwości zainstalowania aplikacji blokującej reklamy.

## Czego potrzebuje Twój router

Twój router musi obsługiwać **szyfrowany DNS z nazwą hosta**, czyli DNS-over-TLS (DoT) lub DNS-over-HTTPS (DoH). Wiele nowszych routerów to umożliwia, w tym poniższe modele. W zależności od tego, co obsługuje Twój router, potrzebujesz swojej nazwy DNS lub linku DoH, oba widoczne powyżej w sekcji _Twoje dane_.

<div class="note important">

**Tylko zwykłe adresy IP?** Wiele routerów od dostawców internetu akceptuje tylko zwykłe adresy IP dla DNS. Obsługa ich jest w przygotowaniu. Do tego czasu konfiguruj urządzenia pojedynczo: [Android](../android-private-dns/), [Mac i Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) oraz [przeglądarki](../browser-dns-over-https/). Można także uruchomić mały przekierowujący serwer na Raspberry Pi – opis znajdziesz w [poradniku Pi-hole](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 lub nowszy.

1. Otwórz `http://fritz.box` i przejdź do _Internet → Informacje o koncie → Serwer DNS_.
2. W sekcji _Szyfrowana rozdzielczość nazw w Internecie (DNS-over-TLS)_ zaznacz _Używaj szyfrowanej rozdzielczości nazw_.
3. W _Rozwiązane nazwy serwera DNS_ wpisz tylko {% dot %}. **Usuń wszystkie inne wpisy.** FRITZ!Box korzysta ze wszystkich wpisanych resolverów, a każdy inny przepuszcza reklamy.
4. Zaznacz _Wymuś weryfikację certyfikatu dla szyfrowanej rozdzielczości nazw_.
5. Jeśli widzisz opcję _Przełącz na publiczne serwery DNS, gdy DNS jest zakłócony_, wyłącz ją.
6. Kliknij _Zastosuj_.

## ASUS

Najnowsze oprogramowanie ASUS (3.0.0.4.388 lub nowsze) oraz Asuswrt-Merlin.

1. Otwórz stronę administracyjną routera i przejdź do _WAN → Połączenie z Internetem_.
2. W sekcji _Ustawienia DNS WAN_ ustaw _Protokół prywatności DNS_ na _DNS-over-TLS (DoT)_, a _Profil DNS-over-TLS_ na _Ścisły_.
3. Usuń wszystkie wpisy z _Listy serwerów DNS-over-TLS_, a następnie dodaj jeden:
   - Adres: {% ip "dot" %}
   - TLS Hostname: {% dot %}
4. Kliknij _Zastosuj_.

## OpenWrt

1. W _System → Oprogramowanie_ zaktualizuj listy i zainstaluj `luci-app-https-dns-proxy`.
2. Otwórz _Usługi → HTTPS DNS Proxy_. Usuń instancje dla innych dostawców.
3. Dodaj instancję z niestandardowym adresem URL resolvera: {% doh %}
4. _Zapisz i zastosuj_. Pakiet automatycznie wskazuje na niego dnsmasq.

## Inne routery

Znajdź ustawienie takie jak _DNS-over-TLS_, _Prywatny DNS_, _Szyfrowany DNS_ lub _DNS-over-HTTPS_. Wprowadź swoją nazwę DNS Blokada lub link DoH z powyższych pozycji i usuń wszystkie inne serwery DNS, wraz z serwerami rezerwowym.

## Sprawdź, czy działa

1. Uruchom ponownie jedno z urządzeń lub wyłącz i włącz jego Wi-Fi, aby odebrało zmianę.
2. Przeglądaj przez minutę, a następnie otwórz stronę _Aktywność_ w panelu. Zapytania z Twojej sieci pojawią się tam.

## Jeśli na niektórych urządzeniach wciąż wyświetlają się reklamy

Niektóre urządzenia omijają router: telefony z ustawionym _Prywatnym DNS_, przeglądarki z _bezpiecznym DNS_ ustawionym na innego dostawcę oraz urządzenia na stałe ustawiające własny DNS. Skonfiguruj takie urządzenie osobno lub wyłącz własne ustawianie DNS.

<div class="note tip">

Za routerem wszystkie urządzenia korzystają z jednego adresu, więc panel wyświetla Twoją sieć jako jedno urządzenie. Jeśli chcesz widzieć telefony i laptopy osobno, skonfiguruj dla nich indywidualną nazwę DNS Blokada. Dzięki temu będą one chronione również po opuszczeniu domu.

</div>
