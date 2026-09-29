---
title: Blockera annonser på Windows med DNS över HTTPS
description: Använd den inbyggda krypterade DNS i Windows 11 med Blokada Cloud för att blockera annonser och spårare i alla appar och webbläsare, utan att behöva installera någon programvara.
updated: 2026-09-28
order: 8
---

Windows 11 kan skicka alla sina DNS-förfrågningar krypterade, över DNS över HTTPS. Peka den mot Blokada Cloud, så blockeras annonser och spårare i alla appar och webbläsare på datorn, utan något att installera.

Du behöver två värden:

- DNS-server (IP-adress): {% ip "doh" %}
- Din DoH-länk: {% doh %}

## Windows 11

1. Öppna _Inställningar → Nätverk & internet_, sedan _Wi-Fi_ eller _Ethernet_, beroende på hur datorn är ansluten.
2. Öppna anslutningens _Maskinvaruegenskaper_. För Wi-Fi, välj _Hantera kända nätverk_ och sedan nätverket, eller _Maskinvaruegenskaper_ högst upp på Wi-Fi-sidan.
3. Bredvid _DNS-serverinställning_, välj _Redigera_. Välj _Manuell_ och aktivera _IPv4_.
4. I _Föredragen DNS_, ange DNS-servern {% ip "doh" %}
5. Ställ in _DNS över HTTPS_ på _På (manuell mall)_ och klistra in din DoH-länk {% doh %} som _DoH-mall_.
6. Stäng av _Fallback till okrypterad_ och välj _Spara_.

Om datorn använder både Wi-Fi och Ethernet, upprepa detta för den andra anslutningen.

<div class="note">

Lämna _Alternativ DNS_ tomt. Windows använder båda servrarna, och någon annan tillåter annonser att släppas igenom.

Ingen _På (manuell mall)_-option? Din Windows 11 är äldre. Uppdatera Windows, eller använd [webbläsarguiden](../browser-dns-over-https/) så länge.

Om vissa annonser ändå släpps igenom på ett nätverk med IPv6, kan Windows också fråga din routers IPv6 DNS-server. Stäng av _Internet Protocol Version 6 (TCP/IPv6)_ i adapterns egenskaper (_Kontrollpanelen → Nätverksanslutningar_), eller konfigurera din [router](../router-ad-blocking/).

</div>

## Windows 10

Windows 10 har ingen inbyggd krypterad DNS. Ställ in säker DNS i din webbläsare istället, enligt [webbläsarguiden](../browser-dns-over-https/), eller konfigurera din [router](../router-ad-blocking/) för att täcka hela hemmet.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan _Aktivitet_ i [instrumentpanelen](https://app.blokada.org/stats?src=guides). Den här datorns förfrågningar visas där.

Webbläsare med egna _säkra DNS_-inställningar kringgår Windows. I Chrome och Edge, ställ in den på att använda nuvarande tjänsteleverantör eller din DoH-länk.

<div class="note">

Vill du också ha ett VPN på den här datorn? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) inkluderar en WireGuard-konfiguration som krypterar all trafik, med samma blockering.

</div>
