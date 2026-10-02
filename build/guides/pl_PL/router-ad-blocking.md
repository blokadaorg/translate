---
title: Blokuj reklamy w całej swojej sieci dzięki blokowaniu reklam na routerze.
description: Skonfiguruj Blokada Cloud na swoim routerze tylko raz, a każde urządzenie w domu będzie chronione, w tym telewizory, konsole do gier i inteligentne głośniki, które nie mogą uruchamiać blokera reklam.
updated: 2026-10-02
order: 4
---

Każde urządzenie w Twojej sieci pyta router, którego serwera DNS użyć. Skieruj router na Blokada Cloud, a reklamy i trackery zostaną zablokowane dla wszystkiego podłączonego za nim. To obejmuje inteligentne telewizory, konsole do gier, sticki do streamingu i urządzenia smart home, które nie mają możliwości uruchomienia aplikacji blokera reklam.

## Czego potrzebuje Twój router

Twój router musi obsługiwać **szyfrowany DNS z nazwą hosta**, czyli DNS-over-TLS (DoT) lub DNS-over-HTTPS (DoH). Wiele nowszych routerów to potrafi, w tym wymienione poniżej modele. W zależności od tego, które z nich obsługuje Twój router, potrzebujesz swojej nazwy DNS lub linku DoH. Obie te informacje znajdziesz powyżej w sekcji _Twoje dane_.

<div class="note important">

**Tylko zwykłe adresy IP?** Wiele routerów od dostawców internetu akceptuje tylko zwykłe adresy IP do DNS. Wsparcie dla nich jest w drodze. Do tego czasu skonfiguruj swoje urządzenia pojedynczo: [Android](../android-private-dns/), [Mac i Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) oraz [przeglądarki](../browser-dns-over-https/). Możesz także uruchomić mały forwarder na Raspberry Pi, zgodnie z opisem w [przewodniku Pi-hole](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 lub nowszy.

1. Otwórz `http://fritz.box` i przejdź do _Internet → Informacje o koncie → Serwer DNS_.
2. W sekcji _Szyfrowana rozdzielczość nazw w Internecie (DNS-over-TLS)_ zaznacz _Używaj szyfrowanej rozdzielczości nazw_.
3. W polu _Nazwy resolverów_ wpisz tylko {% dot %}. **Usuń wszystkie inne wpisy.** FRITZ!Box korzysta ze wszystkich wpisanych resolverów, a każdy inny przepuszcza reklamy.
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
2. Otwórz _Usługi → HTTPS DNS Proxy_. Usuń instancje innych dostawców.
3. Dodaj instancję z niestandardowym adresem URL resolvera: {% doh %}
4. _Zapisz i zastosuj_. Pakiet automatycznie wskazuje na niego dnsmasq.

## Inne routery

Poszukaj ustawienia o nazwie _DNS over TLS_, _Prywatny DNS_, _Szyfrowany DNS_ lub _DNS-over-HTTPS_. Wprowadź swoją nazwę DNS Blokada lub link DoH z powyższej instrukcji i usuń wszystkie inne serwery DNS, w tym zapasowe.

## Sprawdź, czy działa

1. Uruchom ponownie jedno z urządzeń lub wyłącz i włącz jego Wi-Fi, aby odebrało zmianę.
2. Przeglądaj przez minutę, a następnie otwórz stronę _Aktywność_ w panelu. Zapytania Twojej sieci pojawią się tam.

## Jeśli na niektórych urządzeniach wciąż wyświetlają się reklamy

Niektóre urządzenia omijają router: telefony z ustawionym _Prywatnym DNS_, przeglądarki z _bezpiecznym DNS_ ustawionym na innego dostawcę oraz urządzenia na stałe ustawiające własny DNS. Ustaw to bezpośrednio na urządzeniu lub wyłącz ich własne ustawienia DNS.

<div class="note tip">

Za routerem wszystkie urządzenia korzystają z jednego adresu, więc panel wyświetla Twoją sieć jako jedno urządzenie. Skonfiguruj telefony i laptopy z własną nazwą DNS Blokada, jeśli chcesz widzieć je osobno. One również zachowują blokowanie, kiedy są poza domem.

</div>
