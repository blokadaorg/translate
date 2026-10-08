---
title: Blokujte reklamy na Macu a Apple TV pomocí DNS profilu Blokada
description: Nainstalujte si DNS profil Blokada Cloud a blokujte reklamy a sledovače na celém systému Mac nebo Apple TV s šifrovaným DNS, bez nutnosti spuštění čehokoliv na pozadí.
updated: 2026-10-02
order: 6
---

Zařízení Apple mohou využívat šifrovaný DNS pro celý systém díky konfiguračnímu profilu. Profil Blokada nasměruje zařízení na Blokada Cloud, který blokuje reklamy a sledovače ve všech aplikacích a prohlížečích.

Funguje na macOS 11 (Big Sur), tvOS 14, iOS a iPadOS 14 a novějších.

<div class="if-no-device">

Tato stránka zatím nezná vaše zařízení, proto vám nemůže nabídnout váš profil. Přihlaste se do dashboardu, otevřete _Nastavení_, zvolte své zařízení a otevřete tuto příručku pomocí _Otevřít na jiném zařízení_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Získat odkaz na svůj profil</a></p>

</div>

## iPhone a iPad

Nejjednodušší způsob je pomocí aplikace. [Blokada 6](https://go.blokada.org/appstore) vše nastaví za vás, povolí a zakáže blokování jedním klepnutím a ukáže, co bylo na telefonu zablokováno. Přihlaste se svým ID účtu a máte hotovo.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Získat Blokada 6 v App Store</a></p>

### Bez aplikace

Můžete také nainstalovat profil. iPhone a iPad instalují profily pouze z **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Tato stránka je otevřená v jiném prohlížeči. Zkopírujte si odkaz a otevřete jej v Safari, abyste mohli pokračovat: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Otevřete _Nastavení_. Klepněte na _Stažený profil_ nahoře. Najdete to také v _Obecné → VPN a správa zařízení_.
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}Stáhnout můj profil{% endappleProfile %}</p>

## Mac

1. Klikněte na tlačítko níže pro stažení profilu.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Stáhnout můj profil{% endappleProfile %}</p>

## Apple TV

Apple TV nemůže otevírat webové stránky, proto do ní zadáváte svůj odkaz na profil ručně.

1. Váš odkaz na profil: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. Označte _Sdílet analýzy Apple TV_. Nevybírejte ji. Místo toho stiskněte tlačítko Přehrát/Pauza na ovladači.
4. Vyberte _Přidat profil_ a zadejte svůj odkaz na profil. Nejsnadnější je zadávání pomocí klávesnice na iPhonu, kde jej můžete vložit. Profil nainstalujte a potvrďte.

<div class="note aside">

**Apple TV a další zařízení doma:** Pokud nastavíte Blokada Cloud na svém [routeru](../router-ad-blocking/), Apple TV i všechna ostatní zařízení budou chráněna.

</div>

## Ověřit, že to funguje

Procházejte minutu web a poté otevřete stránku _Aktivita_ v [dashboardu](https://app.blokada.org/stats?src=guides). Dotazy z tohoto zařízení se zde zobrazí.

Pokud chcete Blokadu později odebrat, smažte profil tam, kde jste ho nainstalovali.
