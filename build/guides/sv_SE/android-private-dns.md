---
title: Ställ in privat DNS på Android med Blokada Cloud
description: Använd Androids inbyggda inställning för privat DNS med Blokada Cloud för att blockera annonser och spårare i alla appar, både på Wi-Fi och mobildata. Eller låt appen Blokada 6 göra det.
updated: 2026-10-02
order: 5
---

## Det enklaste sättet: appen

[Blokada 6](https://go.blokada.org/play_cloud) ställer in allt åt dig, slår på och av blockeringen med ett tryck, och visar vad som blockerades på själva telefonen. Logga in med ditt konto-ID och du är klar.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Hämta Blokada 6 på Google Play</a></p>

## Utan appen: privat DNS

Android 9 och senare har en inställning för _Privat DNS_. Ställ in den på Blokada Cloud, och annonser och spårare blockeras i alla appar, på varje nätverk, utan att något körs i bakgrunden.

1. Öppna _Inställningar → Nätverk & internet_. På vissa telefoner heter detta _Anslutningar_ eller _Anslutning & delning_.
2. Tryck på _Privat DNS_. På Samsung-telefoner finns det under _Fler anslutningsinställningar_.
3. Välj _Värdnamn för privat DNS-leverantör_.
4. Ange ditt Blokada-DNS-namn {% dot %} och tryck på _Spara_.

Hittar du det inte kan du söka efter ”Privat DNS” i appen Inställningar.

## Kontrollera att det fungerar

Öppna några appar eller webbsidor, titta sedan på sidan _Aktivitet_ i [instrumentpanelen](https://app.blokada.org/stats?src=guides). Den här telefonens uppslag visas där.

## Om något inte fungerar

- **"Kunde inte ansluta" eller inget internet:** kontrollera ditt Blokada DNS-namn för stavfel. Det måste vara exakt som visas ovan, utan `https://`.
- **En annan VPN-app är aktiv:** vissa VPN-appar använder sin egen DNS och kringgår Privat DNS. Stäng av VPN:ens DNS- eller annonsblockeringsinställning, eller använd istället Blokada 6.
- **Chrome visar fortfarande annonser:** Chrome kan vara inställt på sin egen säkra DNS-leverantör, vilket kringgår Privat DNS. I Chrome, öppna _Inställningar → Integritet och säkerhet → Använd säker DNS_ och välj _Använd din nuvarande tjänsteleverantör_. Chrome följer då Privat DNS.
