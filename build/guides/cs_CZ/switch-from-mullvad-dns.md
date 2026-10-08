---
title: Mullvad DNS končí. Zachovejte blokování reklam s Blokada Cloud
description: Mullvad uzavírá svůj veřejný DNS 2. listopadu 2026. Postupujte podle tohoto návodu a přesuňte svůj telefon, počítač a router do Blokada Cloud před tímto datem, abyste nepřišli o blokování reklam.
updated: 2026-10-02
order: 2
---

Mullvad ukončuje svou bezplatnou veřejnou službu DNS dne **2. listopadu 2026** a doporučuje místo ní Quad9. Quad9 blokuje malware, ale **ne** blokuje reklamy ani trackery. Po zastavení DNS Mullvadu zařízení nastavená na něj přestanou načítat webové stránky a aplikace. Pokud zařízení může přejít na jiného DNS poskytovatele, reklamy se opět zobrazí. Přepněte se před tímto datem.

Tato stránka se týká veřejných DNS jmen končících na `dns.mullvad.net`. Netýká se aplikace Mullvad VPN.

## Co jste používali a co vybrat v Blokadě

| Název Mullvad DNS          | Co blokoval                            | V nástěnce Blokada                                                                                                                                      |
| -------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | nic                                    | Blokada je služba filtrování. Pokud nechcete žádné filtrování, Quad9 nebo DNS vašeho poskytovatele je jednodušší volba. |
| `adblock.dns.mullvad.net`  | reklamy, trackery                      | blocklist reklam a trackerů                                                                                                                             |
| `base.dns.mullvad.net`     | reklamy, trackery, malware             | přidejte seznam malwaru                                                                                                                                 |
| `extended.dns.mullvad.net` | základ plus sociální sítě              | přidejte seznam sociálních sítí                                                                                                                         |
| `family.dns.mullvad.net`   | základ plus obsah pro dospělé a hazard | přidejte seznamy pro dospělé a hazardní stránky                                                                                                         |
| `all.dns.mullvad.net`      | vše výše uvedené                       | zapněte všechny z nich                                                                                                                                  |

V nástěnce vybíráte blocklisty v sekci _Blocklisty_. Můžete je kdykoliv změnit a změna se projeví na všech vašich zařízeních.

## Přepněte každé zařízení

Blokada dává každému zařízení vlastní název, takže nástěnka zobrazí aktivitu za zařízení. Podle typu zařízení budete potřebovat DNS název nebo DoH odkaz, obojí je v sekci _Vaše detaily_ výše.

### Android

Pokyn Mullvadu vás nechal zadat hostname do _Soukromý DNS_. Nahraďte jej svým názvem DNS z Blokady. [Průvodce pro Android](../android-private-dns/) obsahuje postup.

### iPhone, iPad a Mac

Nastavení Mullvadu používalo konfigurační profil. Nejprve jej odstraňte:

- **iPhone a iPad:** _Nastavení → Obecné → VPN a správa zařízení_, klepněte na profil Mullvad DNS a poté _Odstranit profil_.
- **Mac:** otevřete seznam profilů (_Nastavení systému → Obecné → Správa zařízení_ na macOS 15 a novějším, _Nastavení systému → Soukromí a zabezpečení → Profily_ na macOS 13 a 14, _Předvolby systému → Profily_ na macOS 12 a starších), vyberte profil Mullvad DNS a klikněte na _−_.

Pak nainstalujte profil Blokada podle [Apple návodu](../apple-devices/).

### Prohlížeče

Pokud jste zadali odkaz DoH Mullvad, například `https://adblock.dns.mullvad.net/dns-query` do _zabezpečeného DNS_ nebo _DNS přes HTTPS_, nahraďte ho svým DoH odkazem. [Průvodce prohlížeče](../browser-dns-over-https/) obsahuje postupy pro každý prohlížeč.

### Router

Pokud váš router používá Mullvad přes DNS-over-TLS, nahraďte hostname Mullvadu názvem DNS z Blokady a odstraňte IP adresy Mullvadu. [Průvodce routerem](../router-ad-blocking/) pokrývá běžné modely.

## Zkontrolujte, že vše funguje

Otevřete několik webových stránek a poté se podívejte na stránku _Aktivita_ v nástěnce. Zde uvidíte vyhledávání svých zařízení a označené blokované položky. Pokud se zařízení nezobrazuje, stále používá jiný DNS server.
