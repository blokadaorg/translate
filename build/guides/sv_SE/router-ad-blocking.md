---
title: Blockera reklam i hela nätverket med reklamblockering i routern
description: Ställ in Blokada Cloud i routern en gång och skydda alla enheter hemma, även tv, spelkonsoler och smarta högtalare som inte kan köra en annonsblockerare.
updated: 2026-09-23
order: 4
---

Varje enhet i ditt nätverk frågar routern vilken DNS-server som ska användas. Peka routern mot Blokada Cloud, så blockeras annonser och spårare för allt bakom den. Det inkluderar smarta TV-apparater, spelkonsoler, streaming-stickor och smarta hem-enheter som inte har plats för en annonsblockerare.

## Det här behöver din router

Din router måste stödja **krypterad DNS med ett värdnamn**, det vill säga DNS över TLS (DoT) eller DNS över HTTPS (DoH). Många nyare routrar gör det, inklusive modellerna nedan. Beroende på vad din router stödjer behöver du:

- För DNS över TLS, ditt Blokada-DNS-namn: {% dot %}
- För DNS över HTTPS, din DoH-länk: {% doh %}

<div class="note">

**Endast vanliga IP-adresser?** Många routrar från internetleverantörer accepterar bara vanliga IP-adresser för DNS. Stöd för dessa är på väg. Tills dess, ställ in dina enheter en i taget: [Android](../android-private-dns/), [Mac och Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) och [webbläsare](../browser-dns-over-https/). Du kan också köra en liten vidarebefordrare på en Raspberry Pi, enligt [Pi-hole-guiden](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 eller senare.

1. Öppna `http://fritz.box` och gå till _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_ kryssar du i _Use encrypted name resolution_.
3. Kryssa i _Enforce certificate verification for encrypted name resolution_.
4. Avmarkera _Allow fallback to unencrypted name resolution_.
5. I _Resolver-namn_, ange endast {% dot %}. **Ta bort alla andra poster.** FRITZ!Box använder alla listade resolvers, och någon annan släpper igenom annonser.
6. Klicka på _Apply_.

## ASUS

Nyare ASUS-firmware (3.0.0.4.388 eller senare) och Asuswrt-Merlin.

1. Öppna routerns administrationssida och gå till _WAN → Internet Connection_.
2. Under _WAN DNS Setting_ ställer du in _DNS Privacy Protocol_ på _DNS-over-TLS (DoT)_ och _DNS-over-TLS Profile_ på _Strict_.
3. Ta bort alla poster i _DNS-over-TLS Server List_ och lägg sedan till en:
   - Adress: {% ip "dot" %}
   - TLS-värdnamn: {% dot %}
4. Klicka på _Apply_.

## OpenWrt

1. Under _System → Software_ uppdaterar du listorna och installerar `luci-app-https-dns-proxy`.
2. Öppna _Tjänster → HTTPS DNS Proxy_. Ta bort instanserna för andra leverantörer.
3. Lägg till en instans med en egen resolver-URL: {% doh %}
4. _Spara & Verkställ_. Paketet pekar dnsmasq mot den automatiskt.

## Andra routrar

Leta efter en inställning som heter _DNS över TLS_, _Privat DNS_, _Krypterad DNS_ eller _DNS över HTTPS_. Ange ditt Blokada DNS-namn eller DoH-länk från ovan, och ta bort alla andra DNS-servrar, inklusive reservservrar.

## Kontrollera att det fungerar

1. Starta om en enhet, eller stäng av och slå på dess wifi, så att den får den nya inställningen.
2. Surfa i en minut, öppna sedan sidan _Aktivitet_ i instrumentpanelen. Ditt nätverks uppslag visas där.

Vissa enheter går förbi routern: telefoner med _Privat DNS_ inställt, webbläsare med _säker DNS_ satt till en annan leverantör, och enheter som hårdkodar sin egen DNS. Ställ in dessa på själva enheten, eller stäng av deras egna DNS-inställning.

<div class="note">

Bakom routern delar alla enheter samma adress, så instrumentpanelen visar ditt nätverk som en enda enhet. Ställ in telefoner och bärbara datorer med egna Blokada DNS-namn om du vill se dem separat. De behåller också blockeringen när de lämnar hemmet.

</div>
