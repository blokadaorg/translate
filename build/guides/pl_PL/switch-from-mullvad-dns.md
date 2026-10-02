---
title: Mullvad DNS zostaje zamknięty. Zachowaj blokowanie reklam dzięki Blokada Cloud
description: Mullvad zamyka swój publiczny DNS 2 listopada 2026. Oto jak przenieść swój telefon, komputer i router do Blokada Cloud przed tą datą, nie tracąc przy tym blokowania reklam.
updated: 2026-10-02
order: 2
---

Mullvad zamyka swoją bezpłatną publiczną usługę DNS **2 listopada 2026** i zaleca zamiast tego korzystanie z Quad9. Quad9 blokuje złośliwe oprogramowanie, ale **nie** blokuje reklam ani trackerów. Gdy DNS Mullvad przestanie działać, urządzenia ustawione na niego przestaną ładować strony internetowe i aplikacje. Jeśli urządzenie może automatycznie przełączyć się na inny serwer DNS, zamiast tego powrócą reklamy. Przełącz się przed tą datą.

Ta strona dotyczy publicznych nazw DNS kończących się na `dns.mullvad.net`. Nie dotyczy aplikacji Mullvad VPN.

## Czego używałeś i co wybrać w Blokada

| Nazwa DNS Mullvad          | Co blokowało                                  | W panelu Blokada                                                                                                                            |
| -------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | nic                                           | Blokada to usługa filtrująca. Jeśli nie chcesz filtracji, Quad9 lub DNS twojego dostawcy to prostszy wybór. |
| `adblock.dns.mullvad.net`  | reklamy, trackery                             | bloklista reklam i trackerów                                                                                                                |
| `base.dns.mullvad.net`     | reklamy, trackery, złośliwe oprogramowanie    | dodaj listę złośliwego oprogramowania                                                                                                       |
| `extended.dns.mullvad.net` | podstawowa plus media społecznościowe         | dodaj listę mediów społecznościowych                                                                                                        |
| `family.dns.mullvad.net`   | podstawowa plus treści dla dorosłych i hazard | dodaj listy treści dla dorosłych i hazardu                                                                                                  |
| `all.dns.mullvad.net`      | wszystko powyższe                             | włącz wszystkie                                                                                                                             |

Wybierasz bloklisty w panelu w sekcji _Blocklists_. Możesz je zmieniać w dowolnym momencie, a zmiana dotyczy wszystkich twoich urządzeń.

## Zmień każde urządzenie

Blokada nadaje każdemu urządzeniu własną nazwę, dzięki czemu na panelu można wyświetlać aktywność dla każdego urządzenia osobno. W zależności od urządzenia potrzebujesz swojej nazwy DNS lub linku DoH, oba znajdziesz powyżej w sekcji _Twoje dane_.

### Android

Instrukcja Mullvad polegała na wpisaniu nazwy hosta w sekcji _Prywatny DNS_. Zamień ją na swoją nazwę DNS Blokada. [Przewodnik Android](../android-private-dns/) zawiera wszystkie kroki.

### iPhone, iPad i Mac

Konfiguracja Mullvad wykorzystywała profil konfiguracyjny. Najpierw go usuń:

- **iPhone i iPad:** _Ustawienia → Ogólne → VPN i Zarządzanie Urządzeniem_, dotknij profilu DNS Mullvad, następnie _Usuń profil_.
- **Mac:** otwórz listę profili (_Ustawienia systemowe → Ogólne → Zarządzanie urządzeniem_ na macOS 15 i nowszych, _Ustawienia systemowe → Prywatność i bezpieczeństwo → Profile_ na macOS 13 i 14, _Preferencje systemowe → Profile_ na macOS 12 i starszych), wybierz profil DNS Mullvad i kliknij _−_.

Następnie zainstaluj profil Blokada z [przewodnika Apple](../apple-devices/).

### Przeglądarki

Jeśli wprowadziłeś link DoH Mullvad, taki jak `https://adblock.dns.mullvad.net/dns-query` w sekcji _bezpieczny DNS_ lub _DNS over HTTPS_, zamień go na swój własny link DoH. [Przewodnik dotyczący przeglądarki](../browser-dns-over-https/) zawiera instrukcje dla każdej przeglądarki.

### Router

Jeśli twój router używa Mullvad przez DNS over TLS, zamień nazwę hosta Mullvad na nazwę DNS Blokada i usuń adresy IP Mullvad. [Przewodnik dotyczący routerów](../router-ad-blocking/) obejmuje popularne modele.

## Sprawdź, czy działa

Otwórz kilka stron internetowych, a następnie przejdź do zakładki _Aktywność_ w panelu. Zobaczysz tam zapytania DNS swoich urządzeń, a zablokowane będą oznaczone. Jeśli urządzenie nie pojawia się na liście, nadal korzysta z innego serwera DNS.
