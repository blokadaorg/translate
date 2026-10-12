---
title: Blokování reklam na celé vaší síti pomocí routeru pro blokování reklam.
description: Nastavte Blokada Cloud na svém routeru jednou a každé zařízení v domácnosti bude chráněno – včetně televizí, herních konzolí a chytrých reproduktorů, které nemohou spustit blokátor reklam.
updated: 2026-10-09
order: 4
---

Každé zařízení ve vaší síti se ptá routeru, který DNS server má použít. Nastavte router na Blokada Cloud a reklamy a trackery budou blokovány pro vše, co je za ním. To zahrnuje chytré televize, herní konzole, streamovací zařízení a chytrá domácí zařízení, která nemají prostor pro aplikaci blokátoru reklam.

## Co váš router potřebuje

Existují dva způsoby nastavení routeru:

- **Šifrovaný DNS s názvem hostitele**, tedy DNS přes TLS (DoT) nebo DNS přes HTTPS (DoH). Mnoho moderních routerů tuto funkci podporuje, včetně níže uvedených modelů. Podle toho, co váš router podporuje, potřebujete svůj DNS název nebo svůj DoH odkaz, oba naleznete výše v části _Vaše údaje_.
- **Prostá IPv6 adresa DNS.** Mnoho routerů od poskytovatelů internetu přijímá pouze prosté IP adresy jako DNS. Pokud to platí u vašeho a vaše připojení má IPv6, Blokada vám poskytne IPv6 adresu pro zadání. Viz [Routery, které přijímají pouze IP adresu](#routers-that-only-take-an-ip-address).

Použijte šifrovaný DNS, pokud to váš router podporuje. Vyhledávání zůstávají na cestě do Blokady soukromá.

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

Najděte nastavení nazvané _DNS over TLS_, _Private DNS_, _Encrypted DNS_ nebo _DNS over HTTPS_. Zadejte svůj název Blokada DNS nebo DoH odkaz z výše uvedeného a odstraňte všechny ostatní DNS servery, včetně záložních serverů. Pokud takové nastavení není k dispozici, použijte obyčejnou IPv6 adresu dle níže uvedeného postupu.

## Routery, které přijímají pouze IP adresu

Váš router i vaše internetové připojení potřebují IPv6 pro toto nastavení. Podpora pro obyčejné IPv4 adresy bude k dispozici později.

1. V [ovládacím panelu](https://app.blokada.org/setup?src=guides) otevřete _Nastavení_ a vyberte možnost _Router, TV, herní konzole_.
2. Pojmenujte router, například _Domácí router_, a zvolte _Získat adresu_. Jméno se zobrazí ve vaší aktivitě a později jej již nepůjde změnit.
3. V nastavení routeru najděte DNS servery pro IPv6, často pod _Internet_, _WAN_ nebo _IPv6_, a zadejte adresu jako jediný DNS server.
4. **Odstraňte všechny ostatní DNS servery, včetně těch pro IPv4.** Zařízení, která stále získají IPv4 DNS server od routeru, posílají některé požadavky mimo Blokada. Pokud router nedovoluje nechat pole pro IPv4 DNS prázdné, nastavujte DNS na každém zařízení jednotlivě: [Android](../android-private-dns/), [Mac a Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) a [prohlížeče](../browser-dns-over-https/).

Stejné nastavení funguje také pro TV nebo herní konzoli, které umožňují ručně zadat DNS server. Každému zařízení zadejte vlastní adresu, aby se zobrazovalo pod jménem ve vaší aktivitě.

<div class="note aside">

Tyto dotazy putují nešifrovaně do Blokada, stejně jako k běžnému DNS serveru. Pokud váš router podporuje DNS over TLS nebo DNS over HTTPS, použijte raději tato nastavení.

</div>

## Ověřte, že to funguje

1. Restartujte jedno zařízení nebo vypněte a zapněte jeho Wi-Fi, aby se změna projevila.
2. Na tomto zařízení vypněte Blokada, pokud je spuštěná, a poté otevřete [go.blokada.org/test](https://go.blokada.org/test). Zjistíte tak, zda vaše DNS prochází přes Blokada.
3. Procházejte internet minutu a poté otevřete stránku _Aktivita_ v [ovládacím panelu](https://app.blokada.org/stats?src=guides). Vaše síťové dotazy se tam zobrazí.

## Pokud některá zařízení stále zobrazují reklamy

Některá zařízení obejdou router: telefony s nastaveným _soukromým DNS_, prohlížeče s _bezpečným DNS_ u jiného poskytovatele a zařízení, která mají vlastní tvrdě nastavený DNS. Nastavte je přímo na zařízení, nebo vypněte jejich vlastní nastavení DNS.

<div class="note tip">

Za routerem sdílí všechna zařízení jednu adresu, takže dashboard zobrazí vaši síť jako jediné zařízení. Pokud chcete vidět telefony a notebooky zvlášť, nastavte pro ně vlastní Blokada DNS název. Blokování také zůstane funkční, když zařízení opustí domov.

</div>
