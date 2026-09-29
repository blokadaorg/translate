---
title: Ställ in privat DNS på Android med Blokada Cloud
description: Använd Androids inbyggda privata DNS med Blokada Cloud och blockera reklam och spårare i alla appar, på wifi och mobildata. Eller låt appen Blokada 6 göra det.
updated: 2026-09-28
order: 5
---

## Det enklaste sättet: appen

[Blokada 6](https://go.blokada.org/play_cloud) ställer in allt åt dig, slår på och av blockeringen med ett tryck och visar vad som blockerats direkt i telefonen. Logga in med ditt konto-ID, så är du klar.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Hämta Blokada 6 på Google Play</a></p>

## Utan appen: privat DNS

Android 9 och senare har inställningen *Privat DNS*. Ställ in den på Blokada Cloud, så blockeras reklam och spårare i alla appar, på alla nätverk, utan att något körs i bakgrunden.

Ditt Blokada-DNS-namn: {% dot %}

1. Öppna *Inställningar → Nätverk och internet*. På vissa telefoner heter det *Anslutningar* eller *Anslutning och delning*.
2. Tryck på *Privat DNS*. På Samsung-telefoner finns det under *Fler anslutningsinställningar*.
3. Välj *Värdnamn för privat DNS-leverantör*.
4. Ange ditt Blokada-DNS-namn {% dot %} och tryck på *Spara*.

Hittar du det inte kan du söka efter ”Privat DNS” i appen Inställningar.

## Kontrollera att det fungerar

Öppna några appar eller webbplatser och titta sedan på sidan *Aktivitet* i [dashboarden](https://app.blokada.org/stats?src=guides). Telefonens uppslag visas där.

## Om något inte fungerar

- **”Det gick inte att ansluta” eller inget internet:** kontrollera att ditt Blokada-DNS-namn inte har några stavfel. Det måste vara exakt som ovan, utan `https://`.
- **En annan VPN-app är aktiv:** vissa VPN-appar använder egen DNS och kringgår privat DNS. Stäng av VPN-appens DNS- eller reklamblockeringsinställning, eller använd Blokada 6 i stället.
- **Chrome visar fortfarande reklam:** öppna *Inställningar → Integritet och säkerhet → Använd säker DNS* i Chrome och välj *Use current service provider*.
