---
title: Blokujte reklamy ve Windows pomocí DNS přes HTTPS
description: Použijte šifrovaný DNS vestavěný ve Windows 11 s Blokada Cloud pro blokování reklam a sledovačů ve všech aplikacích a prohlížečích – bez nutnosti instalace dalšího softwaru.
updated: 2026-10-02
order: 8
---

Windows 11 může posílat všechny své DNS dotazy šifrovaně přes DNS přes HTTPS. Nastavte ho na Blokada Cloud a reklamy i sledovače budou blokovány ve všech aplikacích a prohlížečích na počítači – bez nutnosti cokoli instalovat.

Potřebujete IP adresu DNS serveru a svůj DoH odkaz, obojí najdete výše pod _Vaše údaje_.

## Windows 11

1. Otevřete _Nastavení → Síť a internet_, poté _Wi-Fi_ nebo _Ethernet_ podle toho, jak je počítač připojen.
2. Otevřete _Vlastnosti hardwaru_ vašeho připojení. U Wi-Fi zvolte _Spravovat známé sítě_ a poté konkrétní síť nebo _Vlastnosti hardwaru_ nahoře na stránce Wi-Fi.
3. Vedle _Přiřazení DNS serveru_ vyberte _Upravit_. Zvolte _Ruční_ a zapněte _IPv4_.
4. Do pole _Preferovaný DNS_ zadejte DNS server {% ip "doh" %}
5. Nastavte _DNS přes HTTPS_ na _Zapnuto (ruční šablona)_ a vložte svůj DoH odkaz {% doh %} jako _šablonu DoH_.
6. Vypněte _Záložní režim na prostý text_ a klikněte na _Uložit_.

Pokud počítač používá jak Wi-Fi, tak Ethernet, opakujte tento postup i pro druhé připojení.

<div class="note important">

Pole _Alternativní DNS_ ponechte prázdné. Windows používá oba servery a jakýkoli jiný by propouštěl reklamy.

</div>

<div class="note tip">

Chybí možnost _Zapnuto (ruční šablona)_? Váš Windows 11 je starší verze. Aktualizujte Windows, nebo použijte mezitím [prohlížečový návod](../browser-dns-over-https/).

</div>

## Windows 10

Windows 10 nemá vestavěné šifrované DNS. Nastavte si zabezpečený DNS ve svém prohlížeči podle [prohlížečového návodu](../browser-dns-over-https/), nebo použijte [router](../router-ad-blocking/) pro ochranu celé domácnosti.

## Zkontrolujte, že vše funguje

Otevřete několik webových stránek a poté zobrazte stránku _Aktivita_ v [panelu](https://app.blokada.org/stats?src=guides). Požadavky tohoto počítače se tam zobrazí.

<div class="note aside">

Chcete i na tomto počítači VPN? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) obsahuje WireGuard nastavení pro šifrování veškerého provozu se stejným blokováním.

</div>

## Pokud něco nefunguje

Chrome a Edge mají své vlastní nastavení _zabezpečený DNS_, které obchází Windows. Pokud necháte nastaveno automaticky, může přejít zpět na prostý DNS, což Blokada odmítá. Nastavte raději svůj DoH odkaz:

- **Chrome:** otevřete `chrome://settings/security`, zapněte _Používat zabezpečený DNS_, a pod _Vybrat poskytovatele DNS_ zvolte _Přidat vlastního poskytovatele DNS_.
- **Edge:** otevřete `edge://settings/privacy`, zapněte zabezpečený DNS a vyberte _Zvolit poskytovatele služeb_.

Poté vložte svůj DoH odkaz {% doh %}

Pokud i přes to některé reklamy na IPv6 sítích procházejí, je možné, že Windows používá také IPv6 DNS server vašeho routeru. Vypněte _Internetový protokol verze 6 (TCP/IPv6)_ ve vlastnostech adaptéru (_Ovládací panely → Síťová připojení_), nebo nastavte svůj [router](../router-ad-blocking/).
