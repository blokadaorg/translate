---
title: Blockera reklam i Windows med DNS över HTTPS
description: Använd den inbyggda krypterade DNS:en i Windows 11 med Blokada Cloud och blockera reklam och spårare i alla appar och webbläsare, utan att installera något.
updated: 2026-10-02
order: 8
---

Windows 11 kan skicka alla sina DNS-uppslag krypterat, via DNS över HTTPS. Peka Windows mot Blokada Cloud, så blockeras reklam och spårare i alla appar och webbläsare på datorn, utan något att installera.

Du behöver DNS-serverns IP-adress och din DoH-länk. Båda finns under _Dina uppgifter_ ovan.

## Windows 11

1. Öppna _Inställningar → Nätverk & Internet_ och sedan _Wi-Fi_ eller _Ethernet_, beroende på hur datorn är ansluten.
2. Öppna anslutningens _Maskinvaruegenskaper_ (_Hardware properties_). För Wi-Fi väljer du _Hantera kända nätverk_ och sedan nätverket, eller _Maskinvaruegenskaper_ högst upp på Wi-Fi-sidan.
3. Välj _Redigera_ bredvid _DNS-servertilldelning_ (_DNS server assignment_). Välj _Manuellt_ och aktivera _IPv4_.
4. Ange DNS-servern {% ip "doh" %} under _Önskad DNS-server_.
5. Ställ in _DNS över HTTPS_ på _På (manuell mall)_ och klistra in din DoH-länk {% doh %} i mallrutan _DNS över HTTPS_.
6. Stäng av _Återställning till oformaterad text_ och välj _Spara_.

Om datorn använder både Wi-Fi och Ethernet upprepar du detta för den andra anslutningen.

<div class="note important">

Lämna _Alternativ DNS-server_ tom. Windows använder båda servrarna, och varje annan server släpper igenom reklam.

</div>

<div class="note tip">

Finns inte alternativet _På (manuell mall)_? Då är ditt Windows 11 äldre. Uppdatera Windows, eller använd [webbläsarguiden](../browser-dns-over-https/) så länge.

</div>

## Windows 10

Windows 10 har ingen inbyggd krypterad DNS. Ställ in säker DNS i webbläsaren i stället, enligt [webbläsarguiden](../browser-dns-over-https/), eller ställ in din [router](../router-ad-blocking/) för att skydda hela hemmet.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan _Aktivitet_ i [dashboarden](https://app.blokada.org/stats?src=guides). Datorns uppslag visas där.

<div class="note aside">

Vill du också ha en VPN på den här datorn? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) innehåller en WireGuard-konfiguration som krypterar all trafik, med samma blockering.

</div>

## Om något inte fungerar

Chrome och Edge har en egen inställning för _säker DNS_, som går förbi Windows. I automatiskt läge kan den falla tillbaka på okrypterad DNS, som Blokada nekar. Ställ in den på din DoH-länk i stället:

- **Chrome:** öppna `chrome://settings/security`, aktivera _Använd säker DNS_ och välj _Lägg till en anpassad DNS-tjänsteleverantör_ under _Välj DNS-leverantör_.
- **Edge:** öppna `edge://settings/privacy`, aktivera säker DNS och välj _Välj en tjänsteleverantör_ (_Choose a service provider_).

Klistra sedan in din DoH-länk {% doh %}

Om reklam fortfarande slinker igenom i ett nätverk med IPv6 kan Windows även fråga routerns IPv6-DNS-server. Stäng av _Internet Protocol Version 6 (TCP/IPv6)_ i nätverkskortets egenskaper (_Kontrollpanelen → Nätverksanslutningar_), eller ställ in din [router](../router-ad-blocking/).
