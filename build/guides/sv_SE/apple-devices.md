---
title: Blockera reklam på Mac och Apple TV med en DNS-profil från Blokada
description: Installera en DNS-profil för Blokada Cloud och blockera reklam och spårare i hela systemet på Mac eller Apple TV, med krypterad DNS och inget i bakgrunden.
updated: 2026-09-28
order: 6
---

Apple-enheter kan använda krypterad DNS för hela systemet via en konfigurationsprofil. Blokada-profilen pekar enheten mot Blokada Cloud, som blockerar reklam och spårare i alla appar och webbläsare.

Det fungerar på macOS 11 (Big Sur), tvOS 14, iOS och iPadOS 14 och senare.

<div class="if-no-device">

Den här sidan känner inte till din enhet än, så den kan inte erbjuda din profil. Logga in i dashboarden, öppna *Inställningar*, välj din enhet och öppna den här guiden via länken för att öppna på en annan enhet.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Hämta min profillänk</a></p>

</div>

## iPhone och iPad

Det enklaste sättet är appen. [Blokada 6](https://go.blokada.org/appstore) ställer in allt åt dig, slår på och av blockeringen med ett tryck och visar vad som blockerats direkt i telefonen. Logga in med ditt konto-ID, så är du klar.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Hämta Blokada 6 i App Store</a></p>

### Utan appen

Du kan installera profilen i stället. iPhone och iPad installerar profiler bara från **Safari**.

<div class="if-device">
<div class="if-other-browser note">

Den här sidan är öppen i en annan webbläsare. Kopiera din länk och öppna den i Safari för att fortsätta där: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. Tryck på knappen nedan i Safari och sedan på *Tillåt* för att hämta profilen.
2. Öppna *Inställningar*. Tryck på *Profil hämtad* högst upp. Du hittar den också under *Allmänt → VPN och enhetshantering*.
3. Tryck på *Installera*, ange din lösenkod och bekräfta.

</div>

<p class="if-device if-safari">{% appleProfile %}Hämta min profil{% endappleProfile %}</p>

## Mac

1. Klicka på knappen nedan för att hämta profilen.
2. Öppna listan med profiler: *Systeminställningar → Allmänt → Enhetshantering* på macOS 15 och senare, *Systeminställningar → Integritet och säkerhet → Profiler* på macOS 13 och 14, eller *Systeminställningar → Profiler* på macOS 12 och tidigare.
3. Dubbelklicka på Blokada-profilen och klicka på *Installera*.

<p class="if-device">{% appleProfile %}Hämta min profil{% endappleProfile %}</p>

## Apple TV

Apple TV kan inte öppna webbsidor, så du skriver in din profillänk på den.

1. Din profillänk: {% appleUrl %}
2. Öppna *Inställningar → Allmänt → Integritet och säkerhet* på Apple TV.
3. Markera *Send to Apple* (*Share Apple TV Analytics* i äldre tvOS). Välj den inte, utan tryck på Spela/Paus-knappen på fjärrkontrollen i stället.
4. Välj *Add Profile* och ange din profillänk. Enklast är att skriva med tangentbordsaviseringen på din iPhone, där du kan klistra in den. Installera profilen och bekräfta.

<div class="note">

**Apple TV och andra enheter i hemmet:** om du ställer in Blokada Cloud på din [router](../router-ad-blocking/) skyddas Apple TV tillsammans med allt annat.

</div>

## Kontrollera att det fungerar

Surfa en stund och öppna sedan sidan *Aktivitet* i [dashboarden](https://app.blokada.org/stats?src=guides). Enhetens uppslag visas där.

Vill du ta bort Blokada senare raderar du profilen där du installerade den.
