---
title: Blokuj reklamy w Chrome, Firefox, Edge i Brave za pomocą DNS over HTTPS
description: Ustaw Blokada Cloud jako bezpiecznego dostawcę DNS w swojej przeglądarce, aby blokować reklamy i trackery na dowolnym komputerze, w tym na laptopach służbowych, na których nie możesz instalować aplikacji.
updated: 2026-10-02
order: 7
---

Nowoczesne przeglądarki mogą używać własnego szyfrowanego dostawcy DNS, zwanego _bezpiecznym DNS_ lub _DNS przez HTTPS_. Ustaw Blokada Cloud, a przeglądarka będzie blokować reklamy i trackery w każdej sieci, bez konieczności instalacji rozszerzenia.

To ustawienie obejmuje tylko tę przeglądarkę. Aby objąć ochroną cały komputer, użyj [profilu Apple](../apple-devices/) na Macu lub skonfiguruj [router](../router-ad-blocking/).

## Chrome

1. Otwórz `chrome://settings/security`.
2. Włącz _Używaj bezpiecznego DNS_, a następnie wybierz _Dodaj niestandardowego dostawcę usługi DNS_.
3. Wprowadź {% doh %}

## Edge

1. Otwórz `edge://settings/privacy`.
2. W sekcji _Bezpieczeństwo_ włącz _Używaj bezpiecznego DNS, aby określić jak wyszukiwać adresy sieciowe dla stron internetowych_.
3. Wybierz _Wybierz dostawcę usług_ i wprowadź {% doh %}

## Firefox

1. Otwórz _Ustawienia → Prywatność i bezpieczeństwo_ i przewiń do _DNS over HTTPS_.
2. Wybierz _Maksymalna ochrona_.
3. W sekcji _Wybierz dostawcę_ wybierz _Niestandardowy_ i wprowadź {% doh %}

## Brave

1. Otwórz `brave://settings/security`.
2. Włącz _Używaj bezpiecznego DNS_, a następnie wybierz _Dodaj niestandardowego dostawcę usługi DNS_.
3. Wprowadź {% doh %}

## Safari

Safari nie ma własnego ustawienia bezpiecznego DNS. Używa DNS systemu, dlatego zainstaluj [profil Apple](../apple-devices/).

## Sprawdź, czy działa

Przeglądaj przez chwilę, a następnie otwórz stronę _Aktywność_ w [panelu](https://app.blokada.org/stats?src=guides). Zapytania tej przeglądarki pojawią się tam.

## Jeśli coś nie działa

<div class="note tip">

Jeśli Twoja przeglądarka jest zarządzana przez firmę lub szkołę, ustawienie bezpiecznego DNS może być zablokowane. Skontaktuj się z administratorem.

</div>
