---
title: Blochează reclamele pe Mac și Apple TV cu un profil DNS Blokada
description: Instalează un profil DNS Blokada Cloud pentru a bloca reclamele și tracker-ele la nivel de sistem pe un Mac sau Apple TV, cu DNS criptat și fără nimic care să ruleze în fundal.
updated: 2026-10-02
order: 6
---

Dispozitivele Apple pot folosi DNS criptat la nivel de sistem printr-un profil de configurare. Profilul Blokada orientează dispozitivul către Blokada Cloud, care blochează reclamele și tracker-ele în orice aplicație și browser.

Funcționează pe macOS 11 (Big Sur), tvOS 14, iOS și iPadOS 14 și versiunile ulterioare.

<div class="if-no-device">

Această pagină nu recunoaște încă dispozitivul tău, deci nu îți poate oferi profilul. Autentifică-te în dashboard, deschide _Setup_, alege dispozitivul tău și deschide acest ghid cu _Deschide pe alt dispozitiv_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Obține linkul profilului meu</a></p>

</div>

## iPhone și iPad

Cea mai simplă metodă este aplicația. [Blokada 6](https://go.blokada.org/appstore) configurează tot pentru tine, pornește și oprește blocarea dintr-o singură atingere și îți arată ce a fost blocat chiar pe telefon. Autentifică-te cu ID-ul contului tău și gata.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Obține Blokada 6 din App Store</a></p>

### Fără aplicație

Poți instala profilul în schimb. iPhone și iPad instalează profiluri doar din **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Această pagină este deschisă într-un alt browser. Copiază-ți linkul și deschide-l în Safari pentru a continua acolo: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Deschide _Setări_. Atinge _Profil descărcat_ aproape de partea de sus. Îl poți găsi și la _General → VPN și administrare dispozitiv_.
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}Descarcă profilul meu{% endappleProfile %}</p>

## Mac

1. Apasă butonul de mai jos pentru a descărca profilul.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Descarcă profilul meu{% endappleProfile %}</p>

## Apple TV

Apple TV nu poate deschide pagini web, așa că trebuie să introduci manual linkul profilului tău.

1. Linkul profilului tău: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. Evidențiază _Share Apple TV Analytics_. Nu o selecta. Apasă butonul Redare/Pauză de pe telecomandă în schimb.
4. Alege _Adăugare profil_ și introdu linkul profilului tău. Tastarea este cea mai ușoară folosind notificarea de tastatură de pe iPhone, unde îl poți lipi. Instalează profilul și confirmă.

<div class="note aside">

**Apple TV și alte dispozitive de acasă:** dacă configurezi Blokada Cloud pe [routerul](../router-ad-blocking/) tău, Apple TV va fi protejat împreună cu toate celelalte dispozitive.

</div>

## Verifică dacă funcționează

Navighează pentru un minut, apoi deschide pagina _Activitate_ în [dashboard](https://app.blokada.org/stats?src=guides). Interogările acestui dispozitiv vor apărea acolo.

Pentru a elimina Blokada ulterior, șterge profilul de unde l-ai instalat.
