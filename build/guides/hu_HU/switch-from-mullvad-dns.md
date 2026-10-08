---
title: A Mullvad DNS megszűnik. Tartsd meg hirdetésblokkolásodat a Blokada Cloud-dal
description: A Mullvad 2026. november 2-án bezárja nyilvános DNS szolgáltatását. Így állíthatod át a telefonodat, számítógépedet és routeredet a Blokada Cloud-ra, anélkül, hogy elveszítenéd a hirdetésblokkolást.
updated: 2026-10-02
order: 2
---

A Mullvad megszünteti ingyenes nyilvános DNS szolgáltatását **2026. november 2-án**, és helyette a Quad9-et ajánlja. A Quad9 blokkolja a kártevőket, de **nem** blokkolja a hirdetéseket vagy a nyomkövetőket. Amikor a Mullvad DNS leáll, a rá állított eszközök nem töltik be a weboldalakat és alkalmazásokat. Ahol egy eszköznek megengedett másik DNS szerverre visszaállni, a hirdetések visszatérnek ehelyett. Válts még azelőtt az időpont előtt.

Ez az oldal a dns.mullvad.net-re végződő nyilvános DNS nevekről szól. Nem tartalmazza a Mullvad VPN alkalmazást.

## Mit használtál, és mit válassz a Blokadában

| Mullvad DNS név            | Mit blokkolt                                      | A Blokada vezérlőpultjában                                                                                                                               |
| -------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | semmit                                            | A Blokada egy szűrőszolgáltatás. Ha nem szeretnél szűrést, akkor a Quad9 vagy a szolgáltatód DNS-e egyszerűbb választás. |
| `adblock.dns.mullvad.net`  | hirdetések, nyomkövetők                           | hirdetés- és nyomkövető blokkolási lista                                                                                                                 |
| `base.dns.mullvad.net`     | hirdetések, nyomkövetők, kártevők                 | adj hozzá egy kártevőlistát                                                                                                                              |
| `extended.dns.mullvad.net` | alap, valamint közösségi média                    | adj hozzá egy közösségi média listát                                                                                                                     |
| `family.dns.mullvad.net`   | alap, valamint felnőtt tartalom és szerencsejáték | adj hozzá felnőtt tartalom és szerencsejáték listákat                                                                                                    |
| `all.dns.mullvad.net`      | az összes fentit                                  | kapcsold be mindet                                                                                                                                       |

A vezérlőpultban a _Blokkolási listák_ alatt választhatsz blokkolási listákat. Ezeket bármikor módosíthatod, és a változás minden eszközödre érvényes lesz.

## Minden eszköz átváltása

A Blokada minden eszköznek saját nevet ad, így a vezérlőpultban eszközönként láthatod a tevékenységet. Az eszköztől függően szükséged lesz a DNS nevedre vagy a DoH hivatkozásodra, mindkettő megtalálható fent a _Saját adatok_ részben.

### Android

A Mullvad útmutatója szerint a _Privát DNS_ alá kellett beírnod egy gépnevet. Cseréld le a saját Blokada DNS nevedre. Az [Android útmutató](../android-private-dns/) tartalmazza a lépéseket.

### iPhone, iPad és Mac

A Mullvad beállítása egy konfigurációs profilt használt. Először távolítsd el:

- **iPhone és iPad:** _Beállítások → Általános → VPN és eszközkezelés_, érintsd meg a Mullvad DNS profilt, majd _Profil eltávolítása_.
- **Mac:** Nyisd meg a profilok listáját (_Rendszerbeállítások → Általános → Eszközkezelés_ macOS 15-ön és újabb verziókon, _Rendszerbeállítások → Adatvédelem és biztonság → Profilok_ macOS 13-on és 14-en, _Rendszerbeállítások → Profilok_ macOS 12-őn és korábbiakon), válaszd ki a Mullvad DNS profilt és kattints a _−_ gombra.

Ezután telepítsd a Blokada profilt az [Apple útmutató](../apple-devices/) szerint.

### Böngészők

Ha egy Mullvad DoH hivatkozást adtál meg, például `https://adblock.dns.mullvad.net/dns-query` a _biztonságos DNS_ vagy _DNS over HTTPS_ alatt, cseréld le a saját DoH hivatkozásodra. A [böngésző útmutató](../browser-dns-over-https/) minden böngészőhöz leírja a lépéseket.

### Útválasztó

Ha a routered a Mullvad DNS over TLS-t használja, cseréld ki a Mullvad gépnevét a saját Blokada DNS nevedre, és töröld a Mullvad IP-címeit. A [router útmutató](../router-ad-blocking/) a leggyakoribb modellekhez ad segítséget.

## Ellenőrizd, hogy működik-e

Nyiss meg néhány weboldalt, majd nézd meg a _Tevékenység_ oldalt a vezérlőpultban. Itt láthatod az eszközeid lekérdezéseit, a blokkoltakat pedig jelölve. Ha egy eszköz nem jelenik meg, az még mindig másik DNS szervert használ.
