---
title: O alternativă NextDNS cu aceeași configurare pe fiecare dispozitiv
description: Treci de la NextDNS la Blokada Cloud. Înlocuiește numele DNS NextDNS, linkul DoH sau profilul cu cele ale Blokada pe telefon, computer și router, și păstrează blocarea reclamelor.
updated: 2026-10-02
order: 3
---

NextDNS și Blokada Cloud funcționează în același mod: un serviciu DNS criptat care blochează reclamele și trackerii după nume, folosind propriile tale setări dintr-un nume DNS personalizat. Schimbarea înseamnă să înlocuiești detaliile NextDNS pe fiecare dispozitiv cu cele de la Blokada. Nimic altceva nu se schimbă pe dispozitiv.

## Ce ai folosit și ce să alegi în Blokada

| În NextDNS                                          | În Blokada Cloud                                                           |
| --------------------------------------------------- | -------------------------------------------------------------------------- |
| ID-ul configurației tale, de exemplu `abc123`       | Eticheta dispozitivului tău, parte din numele DNS Blokada și linkul DoH    |
| Listă de blocare de _Confidențialitate_             | _Liste de blocare_ în panoul de control                                    |
| _Securitate_ (malware, phishing) | o listă malware în _Listele de blocare_                                    |
| _Control parental_                                  | liste de conținut pentru adulți și jocuri de noroc în _Listele de blocare_ |
| _Listă de permise_ și _Listă de respinse_           | _Excepții_ în panoul de control                                            |
| _Jurnale_ și _Analize_                              | _Activitate_ și _Statistici_ în panoul de control                          |

## Schimbă fiecare dispozitiv

În funcție de dispozitiv, vei avea nevoie de numele tău DNS sau de linkul DoH, ambele fiind prezentate mai sus în _Detaliile tale_.

### Android

Dacă ai folosit _DNS privat_ cu `<your-id>.dns.nextdns.io`, înlocuiește-l cu numele tău DNS Blokada, ca în [ghidul pentru Android](../android-private-dns/). Dacă ai folosit aplicația NextDNS, dezinstaleaz-o și instalează în schimb [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone și iPad

Dacă ai folosit aplicația NextDNS, dezinstaleaz-o și instalează [Blokada 6](https://go.blokada.org/appstore). Dacă ai instalat în schimb un profil NextDNS, elimină-l din _Setări → General → VPN și administrare dispozitiv_, apoi urmează [ghidul Apple](../apple-devices/).

### Mac și Apple TV

Elimină profilul sau aplicația NextDNS, apoi instalează profilul Blokada din [ghidul Apple](../apple-devices/).

### Windows și Linux

Dezinstalează aplicația NextDNS dacă o folosești. Pe Windows, înlocuiește serverul NextDNS și șablonul DoH cu cele de la Blokada, ca în [ghidul pentru Windows](../windows-dns-over-https/). Pe Linux, înlocuiește serverul NextDNS în systemd-resolved, ca în [ghidul pentru Linux](../linux-dns-over-tls/).

### Browsere

Dacă ai setat `https://dns.nextdns.io/…` ca _DNS securizat_ al browserului, înlocuiește-l cu linkul tău DoH, ca în [ghidul pentru browser](../browser-dns-over-https/).

### Router

Dacă routerul tău folosește NextDNS prin DNS over TLS sau DNS over HTTPS, înlocuiește numele sau linkul NextDNS cu cel de la Blokada, ca în [ghidul pentru router](../router-ad-blocking/).

Dacă routerul folosește NextDNS prin adrese IP simple cu un _IP asociat_, Blokada nu poate prelua încă această funcție. Suportul pentru routere cu adrese DNS simple este în curs de implementare. Până atunci, setează fiecare dispozitiv separat sau folosește un router care suportă DNS criptat.

## Verifică dacă funcționează

Deschide câteva site-uri, apoi uită-te la pagina _Activitate_ din panoul de control. Vei vedea interogările dispozitivelor acolo, cu cele blocate marcate distinct. Dacă un dispozitiv nu apare, înseamnă că folosește în continuare NextDNS.
