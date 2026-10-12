---
title: Blochează reclamele pe toată rețeaua ta cu blocarea reclamelor la nivel de router.
description: Configurează Blokada Cloud pe routerul tău o singură dată și fiecare dispozitiv de acasă va fi protejat, inclusiv televizoarele, consolele de jocuri și difuzoarele inteligente care nu pot folosi un blocator de reclame.
updated: 09.10.2026
order: 4
---

Fiecare dispozitiv din rețeaua ta întreabă routerul ce server DNS să folosească. Directionează routerul către Blokada Cloud și reclamele și urmăritorii vor fi blocați pentru tot ceea ce se află în spatele său. Asta include televizoare inteligente, console de jocuri, stick-uri de streaming și dispozitive smart home, care nu permit instalarea unei aplicații blocator de reclame.

## De ce are nevoie routerul tău

Există două moduri de a configura un router:

- **DNS criptat cu un nume de gazdă**, adică DNS over TLS (DoT) sau DNS over HTTPS (DoH). Multe routere recente acceptă aceste protocoale, inclusiv modelele de mai jos. În funcţie de ce protocol suportă routerul tău, vei avea nevoie de numele tău DNS sau link-ul tău DoH, ambele aflate în secţiunea _Datele tale_ de mai sus.
- **O adresă DNS IPv6 simplă.** Multe routere oferite de furnizorii de internet acceptă doar adrese IP simple pentru DNS. Dacă al tău funcţionează aşa şi conexiunea ta suportă IPv6, Blokada îţi furnizează o adresă IPv6 de introdus. Vezi secţiunea [Routere care acceptă doar o adresă IP](#routers-that-only-take-an-ip-address).

Foloseşte DNS criptat dacă routerul tău îl suportă. Interogările rămân private pe drumul lor către Blokada.

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

Caută o setare numită _DNS peste TLS_, _DNS privat_, _DNS criptat_ sau _DNS peste HTTPS_. Introdu numele DNS Blokada sau linkul DoH de mai sus și elimină orice alt server DNS, inclusiv serverele de rezervă. Dacă nu există o astfel de setare, folosește o adresă IPv6 simplă, așa cum este mai jos.

## Routere care acceptă doar o adresă IP {:#routers-that-only-take-an-ip-address}

Routerul tău și conexiunea la internet au nevoie de IPv6 pentru aceasta. Suportul pentru adrese doar IPv4 va fi disponibil ulterior.

1. În [dashboard](https://app.blokada.org/setup?src=guides), deschide _Setare_ și alege _Router, TV, consolă de jocuri_.
2. Dă un nume routerului, de exemplu _Router acasă_, și selectează _Obține adresă_. Numele va apărea în activitatea ta și nu mai poate fi schimbat ulterior.
3. În setările routerului, caută serverele DNS pentru IPv6, de obicei la _Internet_, _WAN_ sau _IPv6_, și introdu adresa ca singurul server DNS.
4. **Elimină orice alt server DNS, inclusiv cele pe IPv4.** Dispozitivele care primesc totuși un server DNS pe IPv4 de la router pot trimite unele interogări ocolind Blokada. Dacă routerul nu permite golirea câmpului DNS pe IPv4, configurează dispozitivele separat: [Android](../android-private-dns/), [Mac și Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) și [browsere](../browser-dns-over-https/).

Aceeași configurare funcționează pentru un TV sau o consolă de jocuri care permite introducerea manuală a unui server DNS. Asigură fiecăruia o adresă proprie, ca să apară cu nume în activitatea ta.

<div class="note aside">

Aceste interogări ajung necriptat la Blokada, ca și în cazul oricărui server DNS simplu. Dacă routerul tău suportă DNS peste TLS sau DNS peste HTTPS, folosește acea opțiune în schimb.

</div>

## Verifică dacă funcționează

1. Repornește un dispozitiv, sau închide și pornește Wi-Fi-ul acestuia, pentru ca modificarea să fie preluată.
2. Pe acel dispozitiv, dezactivează Blokada dacă rulează, apoi deschide [go.blokada.org/test](https://go.blokada.org/test). Acesta arată dacă DNS-ul tău trece prin Blokada.
3. Navighează puțin, apoi deschide pagina _Activitate_ din [dashboard](https://app.blokada.org/stats?src=guides). Interogările rețelei tale vor apărea acolo.

## Dacă unele dispozitive încă afișează reclame

Unele dispozitive ocolesc routerul: telefoanele cu _DNS privat_ activat, browserele cu _DNS securizat_ setat la un alt furnizor și dispozitive care au propriul DNS impus. Configurează-le direct pe dispozitiv sau dezactivează setarea proprie DNS.

<div class="note tip">

După router, toate dispozitivele împart o singură adresă, astfel încât tabloul de bord arată rețeaua ta ca un singur dispozitiv. Configurează telefoanele și laptopurile cu propriul nume DNS Blokada dacă vrei să le vezi separat. Vor păstra de asemenea blocarea chiar și când nu sunt acasă.

</div>
