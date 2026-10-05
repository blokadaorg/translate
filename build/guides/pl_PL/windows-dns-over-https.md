---
title: Blokowanie reklam w systemie Windows za pomocą DNS przez HTTPS
description: Użyj wbudowanego w Windows 11 szyfrowanego DNS z Blokada Cloud, aby blokować reklamy i trackery we wszystkich aplikacjach i przeglądarkach, bez instalowania dodatkowego oprogramowania.
updated: 02.10.2026
order: 8
---

Windows 11 może wysyłać wszystkie swoje zapytania DNS w formie zaszyfrowanej, przez DNS over HTTPS. Skieruj je do Blokada Cloud, a reklamy i trackery będą blokowane we wszystkich aplikacjach i przeglądarkach na komputerze, bez konieczności instalowania dodatkowego oprogramowania.

Potrzebujesz adresu IP serwera DNS oraz swojego linku DoH, oba znajdują się powyżej w sekcji _Twoje dane_.

## Windows 11

1. Otwórz _Ustawienia → Sieć i internet_, następnie _Wi-Fi_ lub _Ethernet_, w zależności od sposobu połączenia komputera.
2. Otwórz _Właściwości sprzętowe_ swojego połączenia. Dla Wi-Fi wybierz _Zarządzaj znanymi sieciami_, a następnie sieć lub _Właściwości sprzętowe_ u góry strony Wi-Fi.
3. Obok _Przypisanie serwera DNS_ wybierz _Edytuj_. Wybierz _Ręcznie_ i włącz _IPv4_.
4. W _Preferowany serwer DNS_ wpisz serwer DNS {% ip "doh" %}
5. Ustaw _DNS przez HTTPS_ na _Włączone (szablon ręczny)_ i wklej swój link DoH {% doh %} jako _szablon DoH_.
6. Wyłącz _Powrót do czystego tekstu_ i wybierz _Zapisz_.

Jeśli komputer korzysta zarówno z Wi-Fi, jak i Ethernetu, powtórz to dla drugiego połączenia.

<div class="note important">

Pole _Alternatywny DNS_ pozostaw puste. Windows używa obu serwerów, a każdy inny pozwala reklamom się przedostawać.

</div>

<div class="note tip">

Brak opcji _Włączone (szablon ręczny)_? Twoja wersja Windows 11 jest starsza. Zaktualizuj system Windows lub do czasu aktualizacji skorzystaj z [poradnika do przeglądarki](../browser-dns-over-https/).

</div>

## Windows 10

Windows 10 nie ma wbudowanego szyfrowanego DNS. Skonfiguruj bezpieczny DNS w swojej przeglądarce, według [poradnika do przeglądarki](../browser-dns-over-https/), lub skonfiguruj swój [router](../router-ad-blocking/), aby objąć ochroną cały dom.

## Sprawdź, czy działa

Otwórz kilka stron internetowych, a następnie sprawdź stronę _Aktywność_ w [panelu](https://app.blokada.org/stats?src=guides). Zapytania z tego komputera pojawią się tam.

<div class="note aside">

Chcesz VPN również na tym komputerze? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) zawiera konfigurację WireGuard, która szyfruje cały ruch, z takim samym blokowaniem.

</div>

## Jeśli coś nie działa

Chrome i Edge mają własne ustawienie _bezpiecznego DNS_, które omija Windows. Pozostawione jako automatyczne może przełączyć się na zwykły DNS, który Blokada odrzuca. Ustaw zamiast tego swój link DoH:

- **Chrome:** otwórz `chrome://settings/security`, włącz _Użyj bezpiecznego DNS_, a pod _Wybierz dostawcę DNS_ wybierz _Dodaj niestandardowego dostawcę usług DNS_.
- **Edge:** otwórz `edge://settings/privacy`, włącz bezpieczny DNS i wybierz _Wybierz dostawcę usług_.

Następnie wklej swój link DoH {% doh %}

Jeśli na sieci z IPv6 nadal pojawiają się reklamy, Windows może również korzystać z serwera DNS IPv6 routera. Wyłącz _Protokół internetowy w wersji 6 (TCP/IPv6)_ we właściwościach adaptera (_Panel Sterowania → Połączenia sieciowe_) lub skonfiguruj swój [router](../router-ad-blocking/).
