---
title: Blochează reclamele pe toată rețeaua ta cu blocarea reclamelor la nivel de router.
description: Configurează Blokada Cloud pe routerul tău o singură dată și fiecare dispozitiv de acasă va fi protejat, inclusiv televizoarele, consolele de jocuri și difuzoarele inteligente care nu pot folosi un blocator de reclame.
updated: 2026-10-02
order: 4
---

Fiecare dispozitiv din rețeaua ta întreabă routerul ce server DNS să folosească. Directionează routerul către Blokada Cloud și reclamele și urmăritorii vor fi blocați pentru tot ceea ce se află în spatele său. Asta include televizoare inteligente, console de jocuri, stick-uri de streaming și dispozitive smart home, care nu permit instalarea unei aplicații blocator de reclame.

## De ce are nevoie routerul tău

Routerul tău trebuie să suporte **DNS criptat cu nume de gazdă**, adică DNS over TLS (DoT) sau DNS over HTTPS (DoH). Multe routere recente oferă această funcție, inclusiv modelele de mai jos. În funcție de ceea ce suportă routerul tău, ai nevoie de numele DNS sau de link-ul DoH, ambele fiind disponibile la secțiunea _Detaliile tale_ de mai sus.

<div class="note important">

**Doar adrese IP simple?** Multe routere ale furnizorilor de internet acceptă doar adrese IP simple pentru DNS. Suportul pentru acestea este în curs de dezvoltare. Până atunci, configurează dispozitivele individual: [Android](../android-private-dns/), [Mac și Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) și [browsere](../browser-dns-over-https/). Poți de asemenea rula un mic forwarder pe un Raspberry Pi, așa cum este descris în [ghidul Pi-hole](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 sau versiuni ulterioare.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. În _Numele rezolvate ale serverului DNS_, introdu doar {% dot %}. **Elimină orice altă intrare.** FRITZ!Box folosește toți rezolvatorii listați, iar orice altul permite trecerea reclamelor.
4. Untick _Allow fallback to unencrypted name resolution_.
5. Dacă vezi _Failover to public DNS servers when DNS disrupted_, dezactiveaz-o.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Adresă: {% ip "dot" %}
   - Nume gazdă TLS: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Deschide _Servicii → DNS HTTPS Proxy_. Șterge instanțele pentru alți furnizori.
3. Adaugă o instanță cu un URL de rezolvator personalizat: {% doh %}
4. _Salvează & aplică_. Pachetul direcționează automat dnsmasq către acesta.

## Alte routere

Caută o opțiune numită _DNS over TLS_, _DNS privat_, _DNS criptat_ sau _DNS over HTTPS_. Introdu numele DNS Blokada sau link-ul DoH de mai sus, și elimină orice alt server DNS, inclusiv cele de rezervă.

## Verifică dacă funcționează

1. Repornește un dispozitiv, sau închide și pornește Wi-Fi-ul acestuia, pentru ca modificarea să fie preluată.
2. Navighează timp de un minut, apoi deschide pagina _Activitate_ din tabloul de bord. Interogările rețelei tale vor apărea acolo.

## Dacă unele dispozitive încă afișează reclame

Unele dispozitive ocolesc routerul: telefoanele cu _DNS privat_ activat, browserele cu _DNS securizat_ setat la un alt furnizor și dispozitive care au propriul DNS impus. Configurează-le direct pe dispozitiv sau dezactivează setarea proprie DNS.

<div class="note tip">

După router, toate dispozitivele împart o singură adresă, astfel încât tabloul de bord arată rețeaua ta ca un singur dispozitiv. Configurează telefoanele și laptopurile cu propriul nume DNS Blokada dacă vrei să le vezi separat. Vor păstra de asemenea blocarea chiar și când nu sunt acasă.

</div>
