---
title: Blokování reklam na celé vaší síti pomocí routeru pro blokování reklam.
description: Nastavte Blokada Cloud na svém routeru jednou a každé zařízení v domácnosti bude chráněno – včetně televizí, herních konzolí a chytrých reproduktorů, které nemohou spustit blokátor reklam.
updated: 2026-10-02
order: 4
---

Každé zařízení ve vaší síti se ptá routeru, který DNS server má použít. Nastavte router na Blokada Cloud a reklamy a trackery budou blokovány pro vše, co je za ním. To zahrnuje chytré televize, herní konzole, streamovací zařízení a chytrá domácí zařízení, která nemají prostor pro aplikaci blokátoru reklam.

## Co váš router potřebuje

Váš router musí podporovat **šifrovaný DNS s názvem hostitele**, tedy DNS over TLS (DoT) nebo DNS over HTTPS (DoH). Mnoho novějších routerů tuto možnost má, včetně níže uvedených modelů. Podle toho, co váš router podporuje, potřebujete svůj DNS název nebo DoH odkaz – oba jsou výše pod _Vaše údaje_.

<div class="note important">

**Pouze prosté IP adresy?** Mnoho routerů od poskytovatelů internetu umožňuje zadat pouze prosté IP adresy pro DNS. Podpora pro ně je v přípravě. Do té doby nastavte svá zařízení zvlášť: [Android](../android-private-dns/), [Mac a Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) a [prohlížeče](../browser-dns-over-https/). Také můžete provozovat malý forwarder na Raspberry Pi, jak je popsáno v [návodu pro Pi-hole](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 nebo novější.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. Do _Vyřešené názvy DNS serveru_ zadejte pouze {% dot %}. **Odstraňte všechna ostatní pole.** FRITZ!Box používá všechny uvedené resolvery a každý další nechá reklamy projít.
4. Untick _Allow fallback to unencrypted name resolution_.
5. Pokud vidíte _Přepnout na veřejné DNS servery při výpadku DNS_, vypněte tuto možnost.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Adresa: {% ip "dot" %}
   - TLS hostname: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Otevřete _Služby → HTTPS DNS Proxy_. Odstraňte instance pro jiné poskytovatele.
3. Přidejte instanci s vlastní URL resolveru: {% doh %}
4. _Uložit a použít_. Balíček automaticky nastaví dnsmasq na tuto možnost.

## Jiné routery

Hledejte nastavení nazvané _DNS over TLS_, _soukromý DNS_, _šifrovaný DNS_ nebo _DNS over HTTPS_. Zadejte svůj Blokada DNS název nebo DoH odkaz z výše uvedeného a odstraňte všechny ostatní DNS servery včetně záložních.

## Ověřte, že to funguje

1. Restartujte jedno zařízení nebo vypněte a zapněte jeho Wi-Fi, aby se změna projevila.
2. Chvíli surfujte a poté otevřete stránku _Aktivita_ v dashboardu. Dotazy vaší sítě se zde zobrazí.

## Pokud některá zařízení stále zobrazují reklamy

Některá zařízení obejdou router: telefony s nastaveným _soukromým DNS_, prohlížeče s _bezpečným DNS_ u jiného poskytovatele a zařízení, která mají vlastní tvrdě nastavený DNS. Nastavte je přímo na zařízení, nebo vypněte jejich vlastní nastavení DNS.

<div class="note tip">

Za routerem sdílí všechna zařízení jednu adresu, takže dashboard zobrazí vaši síť jako jediné zařízení. Pokud chcete vidět telefony a notebooky zvlášť, nastavte pro ně vlastní Blokada DNS název. Blokování také zůstane funkční, když zařízení opustí domov.

</div>
