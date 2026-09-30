---
title: Skonfiguruj Prywatny DNS na Androidzie z Blokada Cloud.
description: Użyj wbudowanego ustawienia Prywatnego DNS w Androidzie z Blokada Cloud, aby blokować reklamy i trackery we wszystkich aplikacjach, zarówno w sieci Wi-Fi, jak i transmisji danych komórkowych. Lub pozwól, aby zrobiła to aplikacja Blokada 6.
updated: 2026-09-28
order: 5
---

## Najprostszy sposób: aplikacja

[Blokada 6](https://go.blokada.org/play_cloud) skonfiguruje wszystko za Ciebie, umożliwia włączanie i wyłączanie blokowania jednym stuknięciem oraz pokazuje, co zostało zablokowane na samym telefonie. Zaloguj się za pomocą swojego ID konta i gotowe.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Pobierz Blokada 6 z Google Play</a></p>

## Bez aplikacji: Prywatny DNS

Android 9 i nowszy posiada ustawienie _Prywatny DNS_. Ustaw na Blokada Cloud, a reklamy i trackery będą blokowane we wszystkich aplikacjach, w każdej sieci, bez konieczności uruchamiania niczego w tle.

Twoja nazwa DNS Blokada: {% dot %}

1. Otwórz _Ustawienia → Sieć i internet_. Na niektórych telefonach to _Połączenia_ lub _Połączenie i udostępnianie_.
2. Stuknij _Prywatny DNS_. W telefonach Samsung znajduje się to w _Więcej ustawień połączenia_.
3. Wybierz _Adres dostawcy prywatnego DNS_.
4. Wpisz swoją nazwę DNS Blokada {% dot %} i stuknij _Zapisz_.

Jeśli nie możesz tego znaleźć, wyszukaj w aplikacji Ustawienia hasło "Prywatny DNS".

## Sprawdź, czy działa

Otwórz kilka aplikacji lub stron internetowych, a następnie sprawdź stronę _Aktywność_ w [panelu](https://app.blokada.org/stats?src=guides). Wyszukiwania z tego telefonu będą się tam pojawiać.

## Jeśli coś nie działa

- **"Nie można połączyć" lub brak internetu:** sprawdź swoją nazwę DNS Blokada pod kątem literówek. Musi być dokładnie taka, jak pokazano powyżej, bez `https://`.
- **Aktywna jest inna aplikacja VPN:** niektóre aplikacje VPN używają własnego DNS i omijają Prywatny DNS. Wyłącz ustawienie DNS lub blokowania reklam w VPN, albo użyj zamiast tego Blokada 6.
- **Chrome nadal wyświetla reklamy:** w Chrome otwórz _Ustawienia → Prywatność i bezpieczeństwo → Użyj bezpiecznego DNS_ i wybierz _Użyj bieżącego dostawcy usług_.
