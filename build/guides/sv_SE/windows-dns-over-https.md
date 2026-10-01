---
title: Blockera reklam i Windows med DNS över HTTPS
description: Använd den inbyggda krypterade DNS:en i Windows 11 med Blokada Cloud och blockera reklam och spårare i alla appar och webbläsare, utan att installera något.
updated: 2026-10-01
order: 8
---

Windows 11 kan skicka alla sina DNS-förfrågningar krypterade, över DNS över HTTPS. Peka den mot Blokada Cloud, så blockeras annonser och spårare i alla appar och webbläsare på datorn, utan något att installera.

Du behöver två värden:

- DNS-server (IP-adress): {% ip "doh" %}
- Din DoH-länk: {% doh %}

## Windows 11

1. Öppna _Inställningar → Nätverk och Internet_ och sedan _Wi-Fi_ eller _Ethernet_, beroende på hur datorn är ansluten.
2. Öppna anslutningens _Maskinvaruegenskaper_. För Wi-Fi, välj _Hantera kända nätverk_ och sedan nätverket, eller _Maskinvaruegenskaper_ högst upp på Wi-Fi-sidan.
3. Bredvid _DNS-serverinställning_, välj _Redigera_. Välj _Manuell_ och aktivera _IPv4_.
4. Ange DNS-servern {% ip "doh" %} under _Önskad DNS_.
5. Ställ in _DNS över HTTPS_ på _På (manuell mall)_ och klistra in din DoH-länk {% doh %} som _DoH-mall_.
6. Stäng av _Återgång till oformaterad text_ och välj _Spara_.

Om datorn använder både Wi-Fi och Ethernet upprepar du detta för den andra anslutningen.

<div class="note">

Lämna _Alternativ DNS_ tomt. Windows använder båda servrarna, och någon annan tillåter annonser att släppas igenom.

Ingen _På (manuell mall)_-option? Din Windows 11 är äldre. Uppdatera Windows, eller använd [webbläsarguiden](../browser-dns-over-https/) så länge.

Om vissa annonser ändå släpps igenom på ett nätverk med IPv6, kan Windows också fråga din routers IPv6 DNS-server. Stäng av _Internet Protocol Version 6 (TCP/IPv6)_ i adapterns egenskaper (_Kontrollpanelen → Nätverksanslutningar_), eller konfigurera din [router](../router-ad-blocking/).

</div>

## Windows 10

Windows 10 har ingen inbyggd krypterad DNS. Ställ in säker DNS i din webbläsare istället, enligt [webbläsarguiden](../browser-dns-over-https/), eller konfigurera din [router](../router-ad-blocking/) för att täcka hela hemmet.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan _Aktivitet_ i [instrumentpanelen](https://app.blokada.org/stats?src=guides). Den här datorns förfrågningar visas där.

Chrome och Edge har ett eget _säker DNS_-alternativ, som kringgår Windows. Om det är inställt på automatiskt kan det falla tillbaka till vanlig DNS, vilket Blokada inte tillåter. Ange istället din DoH-länk:

- **Chrome:** öppna `chrome://settings/security`, slå på _Använd säker DNS_, och under _Välj DNS-leverantör_ välj _Lägg till egen DNS-leverantör_.
- **Edge:** öppna `edge://settings/privacy`, slå på säker DNS och välj _Välj en tjänsteleverantör_.

Klistra sedan in din DoH-länk {% doh %}

<div class="note">

Vill du också ha ett VPN på den här datorn? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) inkluderar en WireGuard-konfiguration som krypterar all trafik, med samma blockering.

</div>
