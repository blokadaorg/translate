---
title: Blokuj reklamy w całej swojej sieci dzięki blokowaniu reklam na routerze.
description: Skonfiguruj Blokada Cloud na swoim routerze tylko raz, a każde urządzenie w domu będzie chronione, w tym telewizory, konsole do gier i inteligentne głośniki, które nie mogą uruchamiać blokera reklam.
updated: 2026-10-09
order: 4
---

Każde urządzenie w Twojej sieci pyta router, z którego serwera DNS ma korzystać. Skieruj router na Blokada Cloud, a reklamy i trackery zostaną zablokowane dla wszystkiego za nim. Dotyczy to również smart TV, konsol do gier, sticków do streamingu oraz urządzeń smart home, które nie mają możliwości zainstalowania aplikacji blokującej reklamy.

## Czego potrzebuje Twój router

Istnieją dwa sposoby konfiguracji routera:

- **Szyfrowany DNS z nazwą hosta**, czyli DNS przez TLS (DoT) lub DNS przez HTTPS (DoH). Wiele nowszych routerów obsługuje te technologie, w tym poniższe modele. W zależności od tego, który wariant obsługuje Twój router, będziesz potrzebować swojej nazwy DNS lub linku DoH – oba znajdziesz powyżej w _Twoje dane_.
- **Zwykły adres IPv6 DNS.** Wiele routerów dostarczanych przez dostawców internetu akceptuje jako DNS wyłącznie zwykłe adresy IP. Jeśli Twój router działa w ten sposób i Twoje połączenie obsługuje IPv6, Blokada udostępnia adres IPv6 do wpisania. Zobacz: [Routery akceptujące wyłącznie adres IP](#routers-that-only-take-an-ip-address).

Użyj szyfrowanego DNS, jeśli Twój router go obsługuje. Zapytania pozostaną prywatne w drodze do Blokada.

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

Poszukaj ustawienia o nazwie _DNS przez TLS_, _Prywatny DNS_, _Szyfrowany DNS_ lub _DNS przez HTTPS_. Wprowadź swoją nazwę DNS Blokada lub link DoH z powyższej instrukcji i usuń wszystkie pozostałe serwery DNS, łącznie z serwerami zapasowymi. Jeśli nie ma takiego ustawienia, użyj zwykłego adresu IPv6 według poniższych wskazówek.

## Routery, które akceptują tylko adres IP {:#routers-that-only-take-an-ip-address}

Twój router i Twoje połączenie internetowe muszą obsługiwać IPv6, aby to działało. Obsługa zwykłych adresów IPv4 pojawi się później.

1. W [panelu](https://app.blokada.org/setup?src=guides) otwórz _Konfiguracja_ i wybierz _Router, TV, konsola do gier_.
2. Nazwij router, na przykład _Router domowy_, i wybierz _Pobierz adres_. Nazwa będzie widoczna w Twojej aktywności i nie można jej później zmienić.
3. W ustawieniach routera znajdź serwery DNS dla IPv6, zazwyczaj w sekcjach _Internet_, _WAN_ lub _IPv6_, i wprowadź adres jako jedyny serwer DNS.
4. **Usuń wszystkie pozostałe serwery DNS, w tym IPv4.** Urządzenia, które nadal otrzymują od routera serwer DNS IPv4, mogą wysyłać część zapytań z pominięciem Blokady. Jeśli nie możesz zostawić pustego pola IPv4 DNS w routerze, skonfiguruj każde urządzenie osobno: [Android](../android-private-dns/), [Mac i Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) oraz [przeglądarki](../browser-dns-over-https/).

Taka sama konfiguracja działa dla telewizorów lub konsol, które umożliwiają ręczne wprowadzenie serwera DNS. Nadaj każdemu urządzeniu własny adres, aby pokazywało się z nazwą w Twojej aktywności.

<div class="note aside">

Te zapytania przesyłane są nieszyfrowane do Blokady, jak do zwykłego serwera DNS. Jeśli twój router obsługuje DNS przez TLS lub DNS przez HTTPS, użyj tej opcji zamiast zwykłego DNS.

</div>

## Sprawdź, czy działa

1. Uruchom ponownie jedno z urządzeń lub wyłącz i włącz jego Wi-Fi, aby odebrało zmianę.
2. Na tym urządzeniu wyłącz Blokadę, jeśli jest włączona, i otwórz [go.blokada.org/test](https://go.blokada.org/test). Strona pokaże, czy Twój DNS przechodzi przez Blokadę.
3. Przeglądaj przez chwilę, a następnie otwórz stronę _Aktywność_ w [panelu](https://app.blokada.org/stats?src=guides). Zapytania z Twojej sieci będą tam widoczne.

## Jeśli na niektórych urządzeniach wciąż wyświetlają się reklamy

Niektóre urządzenia omijają router: telefony z ustawionym _Prywatnym DNS_, przeglądarki z _bezpiecznym DNS_ ustawionym na innego dostawcę oraz urządzenia na stałe ustawiające własny DNS. Skonfiguruj takie urządzenie osobno lub wyłącz własne ustawianie DNS.

<div class="note tip">

Za routerem wszystkie urządzenia korzystają z jednego adresu, więc panel wyświetla Twoją sieć jako jedno urządzenie. Jeśli chcesz widzieć telefony i laptopy osobno, skonfiguruj dla nich indywidualną nazwę DNS Blokada. Dzięki temu będą one chronione również po opuszczeniu domu.

</div>
