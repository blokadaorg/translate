---
title: Alternativa NextDNS se stejným nastavením na každém zařízení
description: Přejděte z NextDNS na Blokada Cloud. Vyměňte svůj NextDNS název DNS, DoH odkaz nebo profil za ekvivalent od Blokady na telefonu, počítači i routeru a ponechte si blokování reklam.
updated: 2026-10-02
order: 3
---

NextDNS a Blokada Cloud fungují stejným způsobem: šifrovaná DNS služba, která blokuje reklamy a trackery podle názvu, s vaším vlastním nastavením za osobním názvem DNS. Přechod znamená pouze výměnu hodnot NextDNS na každém zařízení za vaše Blokada hodnoty. Ostatní nastavení zařízení zůstávají nezměněná.

## Co jste používali a co zvolit v Blokadě

| V NextDNS                                            | V Blokada Cloud                                                      |
| ---------------------------------------------------- | -------------------------------------------------------------------- |
| Vaše ID konfigurace, např. `abc123`  | Váš tag zařízení, součást vašeho názvu Blokada DNS a DoH odkazu      |
| _Ochrana soukromí_ blokovací seznamy                 | _Blokovací seznamy_ v ovládacím panelu                               |
| _Zabezpečení_ (malware, phishing) | seznam malware v rámci _Blokovacích seznamů_                         |
| _Rodičovská kontrola_                                | seznamy pro obsah pro dospělé a hazard v rámci _Blokovacích seznamů_ |
| _Povolené_ a _Zakázané seznamy_                      | _Výjimky_ v ovládacím panelu                                         |
| _Logy_ a _Analytika_                                 | _Aktivita_ a _Statistiky_ v ovládacím panelu                         |

## Vyměňte na každém zařízení

Podle zařízení potřebujete svůj DNS název nebo DoH odkaz, obojí naleznete výše v sekci _Vaše údaje_.

### Android

Pokud jste použili _Private DNS_ s "<your-id>.dns.nextdns.io", nahraďte jej svým názvem Blokada DNS podle [návodu pro Android](../android-private-dns/). Pokud jste používali aplikaci NextDNS, odinstalujte ji a místo ní si nainstalujte [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone a iPad

Pokud jste používali aplikaci NextDNS, odinstalujte ji a nainstalujte [Blokada 6](https://go.blokada.org/appstore). Pokud jste místo toho instalovali profil NextDNS, odeberte jej v _Nastavení → Obecné → Správa VPN a zařízení_ a poté pokračujte podle [návodu pro Apple](../apple-devices/).

### Mac a Apple TV

Odeberte profil nebo aplikaci NextDNS a poté nainstalujte profil Blokada podle [Apple návodu](../apple-devices/).

### Windows a Linux

Pokud používáte aplikaci NextDNS, odinstalujte ji. Ve Windows nahraďte NextDNS server a DoH šablonu hodnotami od Blokady podle [návodu pro Windows](../windows-dns-over-https/). V Linuxu změňte NextDNS server v systemd-resolved dle [návodu pro Linux](../linux-dns-over-tls/).

### Prohlížeče

Pokud jste měli nastaveno `https://dns.nextdns.io/…` jako _zabezpečený DNS_ vašeho prohlížeče, nahraďte ho svým DoH odkazem podle [návodu pro prohlížeče](../browser-dns-over-https/).

### Router

Pokud váš router používá NextDNS přes DNS over TLS nebo DNS over HTTPS, nahraďte NextDNS název nebo odkaz tím od Blokady, jak je popsáno v [návodu pro router](../router-ad-blocking/).

Pokud využívá NextDNS přes běžné IP adresy s _přiřazenou IP_, Blokada toto zatím převzít neumí. Podpora pro routery s obyčejnými DNS adresami se připravuje. Do té doby nastavujte svá zařízení jednotlivě, nebo použijte router podporující šifrovaný DNS.

## Ověřte, že vše funguje

Otevřete několik webových stránek a poté se podívejte na stránku _Aktivita_ v ovládacím panelu. Uvidíte tam požadavky svých zařízení, přičemž zablokované budou označeny. Pokud se některé zařízení nezobrazí, stále používá NextDNS.
