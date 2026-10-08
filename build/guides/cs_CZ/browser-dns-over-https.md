---
title: Blokujte reklamy v Chrome, Firefoxu, Edge a Brave pomocí DNS over HTTPS
description: Nastavte Blokada Cloud jako bezpečného poskytovatele DNS ve vašem prohlížeči pro blokování reklam a trackerů na jakémkoli počítači, včetně pracovních laptopů, kde nemůžete instalovat aplikace.
updated: 2026-10-02
order: 7
---

Moderní prohlížeče mohou používat vlastního šifrovaného poskytovatele DNS, označovaného jako _bezpečné DNS_ nebo _DNS over HTTPS_. Nastavte Blokada Cloud a prohlížeč bude blokovat reklamy a trackery na jakékoli síti, bez nutnosti instalace rozšíření.

Toto nastavení platí pouze pro tento prohlížeč. Pokud chcete pokrýt celý počítač, použijte [Apple profil](../apple-devices/) na Macu, nebo nastavte svůj [router](../router-ad-blocking/).

## Chrome

1. Otevřete `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Zadejte {% doh %}

## Edge

1. Otevřete `edge://settings/privacy`.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. Otevřete `brave://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Zadejte {% doh %}

## Safari

Safari nemá vlastní nastavení bezpečného DNS. Používá systémové DNS, proto nainstalujte [Apple profil](../apple-devices/).

## Ověřte, že to funguje

Procházejte chvíli web a poté otevřete stránku _Aktivita_ v [dashboardu](https://app.blokada.org/stats?src=guides). Dotazy tohoto prohlížeče se zde zobrazí.

## Pokud něco nefunguje

<div class="note tip">

Pokud je váš prohlížeč spravován prací nebo školou, nastavení bezpečného DNS může být uzamčeno. Obraťte se na svého administrátora.

</div>
