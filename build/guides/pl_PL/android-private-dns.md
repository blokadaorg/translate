---
title: Skonfiguruj Prywatny DNS na Androidzie z Blokada Cloud.
description: Użyj wbudowanego ustawienia Prywatnego DNS w Androidzie z Blokada Cloud, aby blokować reklamy i trackery we wszystkich aplikacjach, zarówno w sieci Wi-Fi, jak i transmisji danych komórkowych. Lub pozwól aplikacji Blokada 6 zrobić to za Ciebie.
updated: 02.10.2026
order: 5
---

## Najprostszy sposób: aplikacja

[Blokada 6](https://go.blokada.org/play_cloud) skonfiguruje wszystko za Ciebie, umożliwia włączanie i wyłączanie blokowania jednym stuknięciem oraz pokazuje, co zostało zablokowane bezpośrednio na telefonie. Zaloguj się swoim identyfikatorem konta i gotowe.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Pobierz Blokada 6 z Google Play</a></p>

## Bez aplikacji: Prywatny DNS

Android 9 i nowszy posiada ustawienie _Prywatny DNS_. Ustaw na Blokada Cloud, a reklamy i trackery będą blokowane we wszystkich aplikacjach, w każdej sieci, bez żadnych procesów działających w tle.

1. Otwórz _Ustawienia → Sieć i internet_. Na niektórych telefonach będzie to _Połączenia_ lub _Połączenie i udostępnianie_.
2. Stuknij w _Prywatny DNS_. W telefonach Samsung znajduje się to w _Więcej ustawień połączenia_.
3. Wybierz _Adres dostawcy prywatnego DNS_.
4. Wpisz swoją nazwę DNS Blokada {% dot %} i stuknij _Zapisz_.

Jeśli nie możesz tego znaleźć, wyszukaj w aplikacji Ustawienia hasło "Prywatny DNS".

## Sprawdź, czy działa

Otwórz kilka aplikacji lub stron internetowych, a następnie sprawdź stronę _Aktywność_ w [panelu](https://app.blokada.org/stats?src=guides). Zapytania z tego telefonu pojawią się tam.

## Jeśli coś nie działa

- **„Nie można połączyć” lub brak internetu:** sprawdź nazwę swojego DNS Blokada pod kątem literówek. Musi być dokładnie taka, jak pokazano powyżej, bez `https://`.
- **Inna aplikacja VPN jest aktywna:** niektóre aplikacje VPN używają własnego DNS i omijają Prywatny DNS. Wyłącz ustawienie DNS lub blokowania reklam w tej aplikacji VPN albo użyj Blokada 6.
- **Chrome nadal wyświetla reklamy:** Chrome może być ustawiony na własnego, bezpiecznego dostawcę DNS, co omija Prywatny DNS. W Chrome przejdź do _Ustawienia → Prywatność i bezpieczeństwo → Używaj bezpiecznego DNS_ i wybierz _Użyj aktualnego dostawcy usług_. Wtedy Chrome korzysta z Prywatnego DNS.
