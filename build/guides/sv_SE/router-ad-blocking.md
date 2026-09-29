---
title: Blockera annonser i hela ditt nätverk med router-baserad annonsblockering
description: Ställ in Blokada Cloud på din router en gång, så är varje enhet i hemmet skyddad, inklusive TV-apparater, spelkonsoler och smarta högtalare som inte kan köra en annonsblockerare.
updated: 2026-09-23
order: 4
---

Varje enhet i ditt nätverk frågar routern vilken DNS-server som ska användas. Peka routern mot Blokada Cloud, så blockeras annonser och spårare för allt bakom den. Det inkluderar smarta TV-apparater, spelkonsoler, streaming-stickor och smarta hem-enheter som inte har plats för en annonsblockerare.

## Det din router behöver

Din router måste stödja **krypterad DNS med ett värdnamn**, det vill säga DNS över TLS (DoT) eller DNS över HTTPS (DoH). Många nyare routrar gör det, inklusive modellerna nedan. Beroende på vad din router stödjer behöver du:

- För DNS över TLS, ditt Blokada DNS-namn: {% dot %}
- För DNS över HTTPS, din DoH-länk: {% doh %}

<div class="note">

**Endast vanliga IP-adresser?** Många routrar från internetleverantörer accepterar bara vanliga IP-adresser för DNS. Stöd för dessa är på väg. Tills dess, ställ in dina enheter en i taget: [Android](../android-private-dns/), [Mac och Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) och [webbläsare](../browser-dns-over-https/). Du kan också köra en liten vidarebefordrare på en Raspberry Pi, enligt [Pi-hole-guiden](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 eller senare.

1. Öppna `http://fritz.box` och gå till _Internet → Kontoinformation → DNS-server_.
2. Under _Krypterad namnupplösning på internet (DNS över TLS)_, kryssa i _Använd krypterad namnupplösning_.
3. Kryssa i _Tvinga certifikatverifiering för krypterad namnupplösning_.
4. Avmarkera _Tillåt återgång till okrypterad namnupplösning_.
5. I _Resolver-namn_, ange endast {% dot %}. **Ta bort alla andra poster.** FRITZ!Box använder alla listade resolvers, och någon annan släpper igenom annonser.
6. Klicka på _Verkställ_.

## ASUS

Nyare ASUS-firmware (3.0.0.4.388 eller senare) och Asuswrt-Merlin.

1. Öppna routerns admin-sida och gå till _WAN → Internetanslutning_.
2. Under _WAN DNS-inställning_, sätt _DNS Privacy Protocol_ till _DNS-over-TLS (DoT)_ och _DNS-over-TLS Profile_ till _Strict_.
3. Ta bort alla poster från _DNS-over-TLS Server List_ och lägg sedan till en:
   - Adress: {% ip "dot" %}
   - TLS-värdnamn: {% dot %}
4. Klicka på _Verkställ_.

## OpenWrt

1. I _System → Programvara_, uppdatera listorna och installera `luci-app-https-dns-proxy`.
2. Öppna _Tjänster → HTTPS DNS Proxy_. Ta bort instanserna för andra leverantörer.
3. Lägg till en instans med en anpassad resolver-URL: {% doh %}
4. _Spara & Verkställ_. Paketet pekar dnsmasq mot den automatiskt.

## Andra routrar

Leta efter en inställning som heter _DNS över TLS_, _Privat DNS_, _Krypterad DNS_ eller _DNS över HTTPS_. Ange ditt Blokada DNS-namn eller DoH-länk från ovan, och ta bort alla andra DNS-servrar, inklusive reservservrar.

## Kontrollera att det fungerar

1. Starta om en enhet, eller slå av och på dess Wi-Fi, så att den tar upp ändringen.
2. Surfa i en minut, öppna sedan sidan _Aktivitet_ i instrumentpanelen. Ditt nätverks uppslag visas där.

Vissa enheter går förbi routern: telefoner med _Privat DNS_ inställt, webbläsare med _säker DNS_ satt till en annan leverantör, och enheter som hårdkodar sin egen DNS. Ställ in dessa på själva enheten, eller stäng av deras egna DNS-inställning.

<div class="note">

Bakom routern delar alla enheter samma adress, så instrumentpanelen visar ditt nätverk som en enda enhet. Ställ in telefoner och bärbara datorer med egna Blokada DNS-namn om du vill se dem separat. De behåller också blockeringen när de lämnar hemmet.

</div>
