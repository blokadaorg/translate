---
title: Blockera reklam i Windows med DNS över HTTPS
description: Använd den inbyggda krypterade DNS:en i Windows 11 med Blokada Cloud och blockera reklam och spårare i alla appar och webbläsare, utan att installera något.
updated: 2026-09-28
order: 8
---

Windows 11 kan skicka alla sina DNS-uppslag krypterat, via DNS över HTTPS. Peka Windows mot Blokada Cloud, så blockeras reklam och spårare i alla appar och webbläsare på datorn, utan något att installera.

Du behöver två värden:

- DNS-server (IP-adress): {% ip "doh" %}
- Din DoH-länk: {% doh %}

## Windows 11

1. Öppna *Inställningar → Nätverk och Internet* och sedan *Wi-Fi* eller *Ethernet*, beroende på hur datorn är ansluten.
2. Öppna anslutningens *Maskinvaruegenskaper*. För Wi-Fi väljer du *Hantera kända nätverk* och sedan nätverket, eller *Maskinvaruegenskaper* högst upp på Wi-Fi-sidan.
3. Välj *Redigera* bredvid *DNS-servertilldelning*. Välj *Manuell* och aktivera *IPv4*.
4. Ange DNS-servern {% ip "doh" %} under *Önskad DNS*.
5. Ställ in *DNS över HTTPS* på *På (manuell mall)* och klistra in din DoH-länk {% doh %} som *DoH-mall*.
6. Stäng av *Återgång till oformaterad text* och välj *Spara*.

Om datorn använder både Wi-Fi och Ethernet upprepar du detta för den andra anslutningen.

<div class="note">

Lämna *Alternativ DNS* tom. Windows använder båda servrarna, och varje annan server släpper igenom reklam.

Finns inte alternativet *På (manuell mall)*? Då är ditt Windows 11 äldre. Uppdatera Windows, eller använd [webbläsarguiden](../browser-dns-over-https/) så länge.

Om reklam fortfarande slinker igenom i ett nätverk med IPv6 kan Windows även fråga routerns IPv6-DNS-server. Stäng av *Internet Protocol Version 6 (TCP/IPv6)* i nätverkskortets egenskaper (*Kontrollpanelen → Nätverksanslutningar*), eller ställ in din [router](../router-ad-blocking/).

</div>

## Windows 10

Windows 10 har ingen inbyggd krypterad DNS. Ställ in säker DNS i webbläsaren i stället, enligt [webbläsarguiden](../browser-dns-over-https/), eller ställ in din [router](../router-ad-blocking/) för att skydda hela hemmet.

## Kontrollera att det fungerar

Öppna några webbplatser och titta sedan på sidan *Aktivitet* i [dashboarden](https://app.blokada.org/stats?src=guides). Datorns uppslag visas där.

Webbläsare med en egen inställning för *säker DNS* går förbi Windows. I Chrome och Edge ställer du in den på att använda den aktuella tjänsteleverantören, eller på din DoH-länk.

<div class="note">

Vill du också ha en VPN på den här datorn? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) innehåller en WireGuard-konfiguration som krypterar all trafik, med samma blockering.

</div>
