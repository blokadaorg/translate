---
title: Blochează reclamele în Chrome, Firefox, Edge și Brave cu DNS over HTTPS
description: Setează Blokada Cloud ca furnizor securizat de DNS în browserul tău pentru a bloca reclame și trackere, pe orice computer, inclusiv laptopurile de serviciu unde nu poți instala aplicații.
updated: 2026-10-02
order: 7​​
---

Browserele moderne pot folosi propriul furnizor de DNS criptat, numit _DNS securizat_ sau _DNS over HTTPS_. Selectează Blokada Cloud, iar browserul va bloca reclamele și trackerele pe orice rețea, fără să fie nevoie să instalezi extensii.

Această setare se aplică doar acestui browser. Pentru a acoperi întregul computer, folosește [profilul Apple](../apple-devices/) pe un Mac sau configurează [routerul](../router-ad-blocking/).

## Chrome

1. Deschide `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Introdu {% doh %}

## Edge

1. Deschide `edge://settings/privacy`.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. Deschide `brave://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Introdu {% doh %}

## Safari

Safari nu are o setare de DNS securizat proprie. Utilizează DNS-ul sistemului, deci instalează [profilul Apple](../apple-devices/).

## Verifică dacă funcționează

Navighează un minut, apoi deschide pagina _Activitate_ din [panoul de control](https://app.blokada.org/stats?src=guides). Căutările acestui browser vor apărea acolo.

## Dacă ceva nu funcționează

<div class="note tip">

Dacă browserul tău este gestionat de serviciu sau școală, setarea DNS securizat poate fi blocată. Adresează-te administratorului.

</div>
