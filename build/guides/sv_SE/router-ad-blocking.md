---
title: Blockera reklam i hela nätverket med reklamblockering i routern
description: Ställ in Blokada Cloud i routern en gång och skydda alla enheter hemma, även tv, spelkonsoler och smarta högtalare som inte kan köra en annonsblockerare.
updated: 2026-09-23
order: 4
---

Alla enheter i nätverket frågar routern vilken DNS-server de ska använda. Peka routern mot Blokada Cloud, så blockeras reklam och spårare för allt som är anslutet till den. Det gäller även smarta tv-apparater, spelkonsoler, streamingstickor och smarta hem-enheter, som inte har plats för en app för reklamblockering.

## Det här behöver din router

Routern måste ha stöd för **krypterad DNS med värdnamn**, alltså DNS över TLS (DoT) eller DNS över HTTPS (DoH). Många nyare routrar har det, bland annat modellerna nedan. Beroende på vad din router har stöd för behöver du:

- För DNS över TLS, ditt Blokada-DNS-namn: {% dot %}
- För DNS över HTTPS, din DoH-länk: {% doh %}

<div class="note">

**Bara vanliga IP-adresser?** Många routrar från internetleverantörer accepterar bara vanliga IP-adresser som DNS. Stöd för det är på väg. Till dess kan du ställa in dina enheter en i taget: [Android](../android-private-dns/), [Mac och Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) och [webbläsare](../browser-dns-over-https/). Du kan också köra en liten vidarebefordrare på en Raspberry Pi, som beskrivs i [Pi-hole-guiden](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 eller senare.

1. Öppna `http://fritz.box` och gå till *Internet → Account Information → DNS Server*.
2. Under *Encrypted Name Resolution on the Internet (DNS over TLS)* kryssar du i *Use encrypted name resolution*.
3. Kryssa i *Enforce certificate verification for encrypted name resolution*.
4. Avmarkera *Allow fallback to unencrypted name resolution*.
5. Ange bara {% dot %} under *Resolver names*. **Ta bort alla andra poster.** FRITZ!Box använder alla resolvers i listan, och varje annan resolver släpper igenom reklam.
6. Klicka på *Apply*.

## ASUS

Nyare ASUS-firmware (3.0.0.4.388 eller senare) och Asuswrt-Merlin.

1. Öppna routerns administrationssida och gå till *WAN → Internet Connection*.
2. Under *WAN DNS Setting* ställer du in *DNS Privacy Protocol* på *DNS-over-TLS (DoT)* och *DNS-over-TLS Profile* på *Strict*.
3. Ta bort alla poster i *DNS-over-TLS Server List* och lägg sedan till en:
   - Address: {% ip "dot" %}
   - TLS Hostname: {% dot %}
4. Klicka på *Apply*.

## OpenWrt

1. Under *System → Software* uppdaterar du listorna och installerar `luci-app-https-dns-proxy`.
2. Öppna *Services → HTTPS DNS Proxy*. Ta bort instanserna för andra leverantörer.
3. Lägg till en instans med en egen resolver-URL: {% doh %}
4. *Save & Apply*. Paketet pekar automatiskt dnsmasq mot den.

## Andra routrar

Leta efter en inställning som heter *DNS over TLS*, *Private DNS*, *Encrypted DNS* eller *DNS over HTTPS*. Ange ditt Blokada-DNS-namn eller din DoH-länk från ovan och ta bort alla andra DNS-servrar, även reservservrar.

## Kontrollera att det fungerar

1. Starta om en enhet, eller stäng av och slå på dess wifi, så att den får den nya inställningen.
2. Surfa en stund och öppna sedan sidan *Aktivitet* i dashboarden. Nätverkets uppslag visas där.

Vissa enheter går förbi routern: telefoner med *privat DNS* inställd, webbläsare med *säker DNS* inställd på en annan leverantör och enheter med egen, hårdkodad DNS. Ställ in dem direkt på enheten, eller stäng av deras egen DNS-inställning.

<div class="note">

Bakom routern delar alla enheter en adress, så dashboarden visar ditt nätverk som en enda enhet. Ställ in telefoner och datorer med ett eget Blokada-DNS-namn om du vill se dem var för sig. Då behåller de också blockeringen när de lämnar hemmet.

</div>
