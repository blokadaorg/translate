---
title: Blockera reklam i hela nätverket med reklamblockering i routern
description: Ställ in Blokada Cloud i routern en gång och skydda alla enheter hemma, även tv, spelkonsoler och smarta högtalare som inte kan köra en annonsblockerare.
updated: 2026-10-09
order: 4
---

Alla enheter i nätverket frågar routern vilken DNS-server de ska använda. Peka routern mot Blokada Cloud, så blockeras reklam och spårare för allt som är anslutet till den. Det gäller även smarta tv-apparater, spelkonsoler, streamingstickor och smarta hem-enheter, som inte har plats för en app för reklamblockering.

## Det här behöver din router

Det finns två sätt att konfigurera en router:

- Din router måste stödja **krypterad DNS med ett värdnamn**, det vill säga DNS över TLS (DoT) eller DNS över HTTPS (DoH). Många nyare routrar gör det, inklusive modellerna nedan. Beroende på vad din router stöder behöver du ditt DNS-namn eller din DoH-länk, båda finns ovan under _Dina uppgifter_.
- **En vanlig IPv6 DNS-adress.** Många routers från internetleverantörer accepterar bara vanliga IP-adresser för DNS. Om din gör det och din anslutning har IPv6, ger Blokada dig en IPv6-adress att ange. Se [Routrar som bara accepterar en IP-adress](#routers-that-only-take-an-ip-address).

Använd krypterad DNS om din router stöder det. Uppslag hålls privata på sin väg till Blokada.

## FRITZ!Box

FRITZ!OS 7.20 eller senare. FRITZ!OS finns inte på svenska, så stegen använder de engelska namnen.

1. Öppna `http://fritz.box`, gå till _Internet → Account Information_ och sedan fliken _DNS Server_.
2. Aktivera _Encrypted name resolution in the internet (DNS over TLS)_.
3. Ange bara {% dot %} under _Resolved Names of the DNS Server_. **Ta bort alla andra poster.** FRITZ!Box använder alla resolvers i listan, och varje annan resolver släpper igenom reklam.
4. Kryssa i alternativet som kräver certifikatkontroll och avmarkera det som tillåter återgång till okrypterad namnupplösning.
5. Om du ser _Failover to public DNS servers when DNS disrupted_ stänger du av det.
6. Klicka på _Apply_.

## ASUS

ASUS-firmware senare än 3.0.0.4.386.4xxxx och Asuswrt-Merlin.

1. Öppna routerns administrationssida och gå till _WAN → Internet Connection_.
2. Under _WAN DNS Setting_ ställer du in _DNS Privacy Protocol_ på _DNS-over-TLS (DoT)_ och _DNS-over-TLS Profile_ på _Strict_.
3. Ta bort alla poster i _DNS-over-TLS Server List_ och lägg sedan till en:
   - Address: {% ip "dot" %}
   - TLS Hostname: {% dot %}
4. Klicka på _Apply_.

## OpenWrt

1. Under _System → Software_ uppdaterar du listorna och installerar `luci-app-https-dns-proxy`.
2. Öppna _Services → HTTPS DNS Proxy_. Ta bort instanserna för andra leverantörer.
3. Lägg till en instans med en egen resolver-URL: {% doh %}
4. _Save & Apply_. Paketet pekar automatiskt dnsmasq mot den.

## Andra routrar

Leta efter en inställning som heter _DNS over TLS_, _Private DNS_, _Encrypted DNS_ eller _DNS over HTTPS_. Ange ditt Blokada DNS-namn eller DoH-länk ovan och ta bort alla andra DNS-servrar, inklusive reservservrar. Om det inte finns någon sådan inställning, använd en vanlig IPv6-adress enligt nedan.

## Routrar som endast accepterar en IP-adress {:#routers-that-only-take-an-ip-address}

Din router och din internetanslutning behöver IPv6 för detta. Stöd för vanliga IPv4-adresser kommer senare.

1. I [dashboarden](https://app.blokada.org/setup?src=guides), öppna _Konfiguration_ och välj _Router, TV, spelkonsol_.
2. Ge routern ett namn, till exempel _Hemrouter_, och välj _Hämta adress_. Namnet visas i din aktivitet och kan inte ändras senare.
3. Gå till routerinställningarna och leta upp DNS-servrarna för IPv6, ofta under _Internet_, _WAN_ eller _IPv6_, och ange adressen som den enda DNS-servern.
4. **Ta bort alla andra DNS-servrar, även IPv4-servrar.** Enheter som fortfarande får en IPv4 DNS-server från routern skickar vissa uppslag utanför Blokada. Om routern inte kan lämna IPv4 DNS tom, ställ in dina enheter en i taget istället: [Android](../android-private-dns/), [Mac och Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) och [webbläsare](../browser-dns-over-https/).

Samma inställning fungerar för en TV eller spelkonsol där du kan ange DNS-server manuellt. Ge varje enhet en egen adress så den visas med namn i din aktivitet.

<div class="note aside">

Dessa uppslag skickas okrypterade till Blokada, precis som med vilken vanlig DNS-server som helst. Om din router stöder DNS over TLS eller DNS over HTTPS rekommenderas att du använder det istället.

</div>

## Kontrollera att det fungerar

1. Starta om en enhet, eller stäng av och slå på dess wifi, så att den får den nya inställningen.
2. Stäng av Blokada på enheten om den körs där, och öppna sedan [go.blokada.org/test](https://go.blokada.org/test). Där visas om din DNS går genom Blokada.
3. Surfa en stund och öppna sedan sidan _Aktivitet_ i [dashboarden](https://app.blokada.org/stats?src=guides). Ditt nätverks uppslag visas där.

## Om vissa enheter fortfarande visar reklam

Vissa enheter går förbi routern: telefoner med _privat DNS_ inställd, webbläsare med _säker DNS_ inställd på en annan leverantör och enheter med egen, hårdkodad DNS. Ställ in dem direkt på enheten, eller stäng av deras egen DNS-inställning.

<div class="note tip">

Bakom routern delar alla enheter en adress, så dashboarden visar ditt nätverk som en enda enhet. Ställ in telefoner och datorer med ett eget Blokada-DNS-namn om du vill se dem var för sig. Då behåller de också blockeringen när de lämnar hemmet.

</div>
