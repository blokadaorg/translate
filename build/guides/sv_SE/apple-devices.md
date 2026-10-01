---
title: Blockera reklam på Mac och Apple TV med en DNS-profil från Blokada
description: Installera en DNS-profil för Blokada Cloud och blockera reklam och spårare i hela systemet på Mac eller Apple TV, med krypterad DNS och inget i bakgrunden.
updated: 2026-10-01
order: 6
---

Apple-enheter kan använda krypterad DNS för hela systemet via en konfigurationsprofil. Blokada-profilen pekar enheten mot Blokada Cloud, som blockerar annonser och spårare i alla appar och webbläsare.

Det fungerar på macOS 11 (Big Sur), tvOS 14, iOS och iPadOS 14 och senare.

<div class="if-no-device">

Den här sidan känner ännu inte till din enhet, så den kan inte erbjuda din profil. Logga in på instrumentpanelen, öppna _Setup_, välj din enhet och öppna denna guide med _Öppna på en annan enhet_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Hämta min profillänk</a></p>

</div>

## iPhone och iPad

Det enklaste sättet är appen. [Blokada 6](https://go.blokada.org/appstore) ställer in allting åt dig, aktiverar och avaktiverar blockering med ett tryck, och visar vad som blockerades direkt på telefonen. Logga in med ditt konto-ID och du är klar.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Hämta Blokada 6 i App Store</a></p>

### Utan appen

Du kan istället installera profilen. iPhone och iPad installerar profiler endast från **Safari**.

<div class="if-device">
<div class="if-other-browser note">

Den här sidan är öppen i en annan webbläsare. Kopiera din länk och öppna den i Safari för att fortsätta där: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. Tryck på knappen nedan i Safari och sedan på _Tillåt_ för att hämta profilen.
2. Öppna _Inställningar_. Tryck på _Profil hämtad_ högst upp. Du hittar den också under _Allmänt → VPN & enhetshantering_.
3. Tryck på _Installera_, ange din lösenkod och bekräfta.

</div>

<p class="if-device if-safari">{% appleProfile %}Hämta min profil{% endappleProfile %}</p>

## Mac

1. Klicka på knappen nedan för att hämta profilen.
2. Öppna listan med profiler: _Systeminställningar → Allmänt → Enhetshantering_ på macOS 15 och senare, _Systeminställningar → Integritet och säkerhet → Profiler_ på macOS 13 och 14, eller _Systeminställningar → Profiler_ på macOS 12 och tidigare.
3. Dubbelklicka på Blokada-profilen och klicka på _Installera_.

<p class="if-device">{% appleProfile %}Hämta min profil{% endappleProfile %}</p>

## Apple TV

Apple TV kan inte öppna webbsidor, så du skriver in din profillänk på den.

1. Din profillänk: {% appleUrl %}
2. Öppna _Inställningar → Allmänt → Integritet och säkerhet_ på Apple TV.
3. Markera _Dela Apple TV-analys_. Välj den inte. Tryck på Play/Paus-knappen på fjärrkontrollen istället.
4. Välj _Lägg till profil_ och ange din profillänk. Det är enklast att skriva in med tangentbordet på din iPhone, där du kan klistra in den. Installera profilen och bekräfta.

<div class="note">

**Apple TV och andra enheter i hemmet:** om du ställer in Blokada Cloud på din [router](../router-ad-blocking/) skyddas Apple TV tillsammans med allt annat.

</div>

## Kontrollera att det fungerar

Surfa i en minut, öppna sedan sidan _Aktivitet_ i [instrumentpanelen](https://app.blokada.org/stats?src=guides). Denna enhets förfrågningar visas där.

Vill du ta bort Blokada senare raderar du profilen där du installerade den.
