---
title: Blokowanie reklam na Macu i Apple TV za pomocą profilu DNS Blokada
description: Zainstaluj profil DNS Blokada Cloud, aby blokować reklamy i trackery w całym systemie na komputerze Mac lub Apple TV, z szyfrowanym DNS i bez niczego uruchomionego w tle.
updated: 2026-10-02
order: 6
---

Urządzenia Apple mogą korzystać z szyfrowanego DNS dla całego systemu dzięki profilowi konfiguracyjnemu. Profil Blokada kieruje urządzenie do Blokada Cloud, która blokuje reklamy i trackery w każdej aplikacji i przeglądarce.

Działa na macOS 11 (Big Sur), tvOS 14, iOS oraz iPadOS 14 i nowszych.

<div class="if-no-device">

Ta strona nie rozpoznała jeszcze Twojego urządzenia, więc nie może zaproponować profilu. Zaloguj się do panelu, otwórz _Konfiguracja_, wybierz swoje urządzenie i otwórz ten przewodnik przez _Otwórz na innym urządzeniu_.

<p><a class=\"btn btn-outline\" href=\"https://app.blokada.org/setup?src=guides\">Pobierz mój link do profilu</a></p>

</div>

## iPhone i iPad

Najprostszy sposób to aplikacja. [Blokada 6](https://go.blokada.org/appstore) skonfiguruje wszystko za Ciebie, pozwoli włączać i wyłączać blokowanie jednym stuknięciem oraz pokaże, co zostało zablokowane na telefonie. Zaloguj się swoim identyfikatorem konta i gotowe.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/appstore\">Pobierz Blokada 6 z App Store</a></p>

### Bez aplikacji

Możesz zamiast tego zainstalować profil. iPhone i iPad instalują profile tylko z **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Ta strona jest otwarta w innej przeglądarce. Skopiuj swój link i otwórz go w Safari, aby kontynuować: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. W Safari stuknij przycisk poniżej, a następnie _Zezwól_, aby pobrać profil.
2. Otwórz _Ustawienia_. Stuknij _Pobrano profil_ na górze. Możesz go także znaleźć w _Ogólne → VPN i zarządzanie urządzeniem_.
3. Stuknij _Zainstaluj_, wpisz swój kod i potwierdź.

</div>

<p class="if-device if-safari">{% appleProfile %}Pobierz mój profil{% endappleProfile %}</p>

## Mac

1. Kliknij poniższy przycisk, aby pobrać profil.
2. Otwórz listę profili: _Ustawienia systemowe → Ogólne → Zarządzanie urządzeniem_ w macOS 15 i nowszych, _Ustawienia systemowe → Prywatność i bezpieczeństwo → Profile_ w macOS 13 i 14 lub _Preferencje systemowe → Profile_ w macOS 12 i starszych.
3. Kliknij dwukrotnie profil Blokada, a następnie kliknij _Zainstaluj_.

<p class="if-device">{% appleProfile %}Pobierz mój profil{% endappleProfile %}</p>

## Apple TV

Apple TV nie może otwierać stron internetowych, więc należy ręcznie wpisać link do profilu.

1. Twój link do profilu: {% appleUrl %}
2. Na Apple TV otwórz _Ustawienia → Ogólne → Prywatność i bezpieczeństwo_.
3. Zaznacz _Wyślij do Apple_ (na starszym tvOS nazywane _Udostępnij analizę Apple TV_). Nie wybieraj tej opcji. Zamiast tego naciśnij przycisk Odtwórz/Pauza na pilocie.
4. Wybierz _Dodaj profil_ i wprowadź swój link do profilu. Najwygodniej wpisywać korzystając z podpowiedzi klawiatury na iPhonie, gdzie można link wkleić. Zainstaluj profil i potwierdź.

<div class="note aside">

**Apple TV i inne urządzenia w domu:** jeśli skonfigurujesz Blokada Cloud na swoim [routerze](../router-ad-blocking/), Apple TV zostanie objęte ochroną razem z resztą urządzeń.

</div>

## Sprawdź, czy działa

Przeglądaj przez minutę, a następnie otwórz stronę _Aktywność_ w [panelu](https://app.blokada.org/stats?src=guides). Zapytania tego urządzenia pojawią się tam.

Aby później usunąć Blokada, skasuj profil tam, gdzie go zainstalowałeś.
