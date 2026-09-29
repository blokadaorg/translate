---
title: Ställ in privat DNS på Android med Blokada Cloud.
description: Använd Androids inbyggda inställning för privat DNS med Blokada Cloud för att blockera annonser och spårare i alla appar, både på Wi-Fi och mobildata. Eller låt appen Blokada 6 göra det.
updated: 2026-09-28
order: 5
---

## Det enklaste sättet: appen

[Blokada 6](https://go.blokada.org/play_cloud) ställer in allt åt dig, slår på och av blockeringen med ett tryck, och visar vad som blockerades på själva telefonen. Logga in med ditt konto-ID och du är klar.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">Hämta Blokada 6 på Google Play</a></p>

## Utan appen: Privat DNS

Android 9 och senare har en inställning för _Privat DNS_. Ställ in den på Blokada Cloud, och annonser och spårare blockeras i alla appar, på varje nätverk, utan att något körs i bakgrunden.

Ditt Blokada DNS-namn: {% dot %}

1. Öppna _Inställningar → Nätverk & internet_. På vissa telefoner heter detta _Anslutningar_ eller _Anslutning & delning_.
2. Tryck på _Privat DNS_. På Samsung-telefoner finns det under _Fler anslutningsinställningar_.
3. Välj _Privat DNS-leverantörs värdnamn_.
4. Skriv in ditt Blokada DNS-namn {% dot %} och tryck på _Spara_.

Om du inte hittar det, sök efter "Privat DNS" i Inställningar-appen.

## Kontrollera att det fungerar

Öppna några appar eller webbsidor, titta sedan på sidan _Aktivitet_ i [instrumentpanelen](https://app.blokada.org/stats?src=guides). Den här telefonens uppslag visas där.

## Om något inte fungerar

- **"Kunde inte ansluta" eller inget internet:** kontrollera ditt Blokada DNS-namn för stavfel. Det måste vara exakt som visas ovan, utan `https://`.
- **En annan VPN-app är aktiv:** vissa VPN-appar använder sin egen DNS och kringgår Privat DNS. Stäng av VPN:ens DNS- eller annonsblockeringsinställning, eller använd istället Blokada 6.
- **Chrome visar fortfarande annonser:** öppna i Chrome _Inställningar → Integritet och säkerhet → Använd säker DNS_ och välj _Använd nuvarande tjänsteleverantör_.
