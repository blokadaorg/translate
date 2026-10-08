---
title: Nastavení soukromého DNS v Androidu s Blokada Cloudem
description: Použijte vestavěné nastavení soukromého DNS v Androidu s Blokada Cloudem pro blokování reklam a sledovačů ve všech aplikacích, na Wi-Fi i mobilních datech. Nebo to nechte udělat aplikaci Blokada 6.
updated: 2026-10-02
order: 5
---

## Nejjednodušší způsob: aplikace

[Blokada 6](https://go.blokada.org/play_cloud) vše nastaví za vás, zapíná a vypíná blokování jedním klepnutím a ukazuje, co bylo blokováno přímo v telefonu. Přihlaste se svým ID účtem a je hotovo.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Získat Blokada 6 na Google Play</a></p>

## Bez aplikace: Soukromý DNS

Android 9 a novější má nastavení _Soukromý DNS_. Nastavte jej na Blokada Cloud a reklamy i sledovače budou blokovány ve všech aplikacích, na všech sítích, bez čehokoli běžícího na pozadí.

1. Otevřete _Nastavení → Síť a internet_. Na některých telefonech je to _Připojení_ nebo _Připojení a sdílení_.
2. Klepněte na _Soukromý DNS_. Na telefonech Samsung to najdete pod _Další nastavení připojení_.
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

Pokud jej nemůžete najít, vyhledejte v aplikaci Nastavení výraz "Soukromý DNS".

## Ověřte, že to funguje

Otevřete několik aplikací nebo webových stránek, poté se podívejte na stránku _Aktivita_ v [dashboardu](https://app.blokada.org/stats?src=guides). Dotazy tohoto telefonu se zde zobrazí.

## Pokud něco nefunguje

- **"Nepodařilo se připojit" nebo žádný internet:** zkontrolujte své jméno Blokada DNS na překlepy. Musí být přesně tak, jak je uvedeno výše, bez `https://`.
- **Je aktivní jiná VPN aplikace:** některé VPN aplikace používají vlastní DNS a obchází soukromý DNS. Vypněte DNS nebo nastavení blokování reklam ve VPN, nebo místo toho použijte Blokada 6.
- **Chrome stále zobrazuje reklamy:** Chrome může být nastaven na svého vlastního poskytovatele zabezpečeného DNS, čímž obchází soukromý DNS. V Chrome otevřete _Nastavení → Ochrana soukromí a zabezpečení → Používat zabezpečený DNS_ a zvolte _Používat aktuálního poskytovatele služeb_. Chrome pak bude následovat soukromý DNS.
