---
title: Mullvad DNS se închide. Păstrați blocarea reclamelor cu Blokada Cloud
description: Mullvad își închide DNS-ul public pe 2 noiembrie 2026. Iată cum să mutați telefonul, calculatorul și routerul pe Blokada Cloud înainte de această dată, fără a pierde blocarea reclamelor.
updated: 2026-10-02
order: 2
---

Mullvad va închide serviciul său public DNS gratuit pe **2 noiembrie 2026** și recomandă în schimb Quad9. Quad9 blochează malware, dar **nu** blochează reclame sau trackere. Când serviciul DNS al Mullvad se oprește, dispozitivele setate pe acesta nu vor mai încărca site-uri web și aplicații. Unde un dispozitiv are voie să treacă automat la alt server DNS, reclamele vor reveni. Schimbați înainte de această dată.

Această pagină se referă la numele DNS publice care se termină în `dns.mullvad.net`. Nu acoperă aplicația Mullvad VPN.

## Ce ați folosit și ce să alegeți în Blokada

| Numele DNS Mullvad         | Ce a blocat                                         | În tabloul de bord Blokada                                                                                                                                                  |
| -------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | nimic                                               | Blokada este un serviciu de filtrare. Dacă nu doriți filtrare, Quad9 sau DNS-ul furnizorului dvs. este alegerea mai simplă. |
| `adblock.dns.mullvad.net`  | reclame, trackere                                   | o listă de blocare pentru reclame și trackere                                                                                                                               |
| `base.dns.mullvad.net`     | reclame, trackere, malware                          | adăugați o listă de malware                                                                                                                                                 |
| `extended.dns.mullvad.net` | baza plus rețele sociale                            | adăugați o listă pentru rețele sociale                                                                                                                                      |
| `family.dns.mullvad.net`   | baza plus conținut pentru adulți și jocuri de noroc | adăugați liste pentru conținut pentru adulți și jocuri de noroc                                                                                                             |
| `all.dns.mullvad.net`      | toate cele de mai sus                               | activați-le pe toate                                                                                                                                                        |

Alegeți listele de blocare în tabloul de bord, la secțiunea _Liste de blocare_. Le puteți schimba oricând, iar modificarea se aplică tuturor dispozitivelor dumneavoastră.

## Schimbați fiecare dispozitiv

Blokada atribuie fiecărui dispozitiv un nume propriu, astfel încât tabloul de bord poate afișa activitatea pentru fiecare dispozitiv. În funcție de dispozitiv, aveți nevoie de numele dvs. DNS sau de linkul DoH, ambele disponibile la secțiunea _Detalii personale_ de mai sus.

### Android

Ghidul Mullvad v-a cerut să introduceți un nume gazdă la _DNS privat_. Înlocuiți-l cu numele Blokada DNS. [Ghidul pentru Android](../android-private-dns/) conține pașii.

### iPhone, iPad și Mac

Configurarea Mullvad folosea un profil de configurare. Eliminați-l mai întâi:

- **iPhone and iPad:** _Settings → General → VPN & Device Management_, tap the Mullvad DNS profile, then _Remove Profile_.
- **Mac:** open the list of profiles (_System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, _System Preferences → Profiles_ on macOS 12 and earlier), select the Mullvad DNS profile and click _−_.

Apoi instalați profilul Blokada folosind [ghidul pentru Apple](../apple-devices/).

### Browsere

Dacă ați introdus un link Mullvad DoH, precum `https://adblock.dns.mullvad.net/dns-query`, la _DNS securizat_ sau _DNS prin HTTPS_, înlocuiți-l cu propriul link DoH. [Ghidul pentru browser](../browser-dns-over-https/) conține pașii pentru fiecare browser.

### Router

Dacă routerul dvs. folosește Mullvad cu DNS over TLS, înlocuiți numele de gazdă Mullvad cu numele Blokada DNS și eliminați adresele IP Mullvad. [Ghidul pentru router](../router-ad-blocking/) acoperă modelele comune.

## Verificați dacă funcționează

Deschideți câteva site-uri web, apoi accesați pagina _Activitate_ din tabloul de bord. Acolo vedeți interogările dispozitivelor dvs., cu cele blocate marcate. Dacă un dispozitiv nu apare, încă folosește un alt server DNS.
