---
title: Configurează DNS privat pe Android cu Blokada Cloud
description: Folosește opțiunea de DNS privat integrată în Android împreună cu Blokada Cloud pentru a bloca reclamele și trackerele în orice aplicație, atât pe Wi-Fi cât și pe date mobile. Sau lasă ca aplicația Blokada 6 să facă acest lucru.
updated: 2026-10-02
order: 5
---

## Cea mai simplă metodă: aplicația

[Blokada 6](https://go.blokada.org/play_cloud) configurează totul pentru tine, permite activarea sau dezactivarea blocării printr-o singură apăsare și arată ce a fost blocat chiar pe telefon. Autentifică-te cu ID-ul contului și ești gata.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Obține Blokada 6 din Google Play</a></p>

## Fără aplicație: DNS privat

Android 9 și versiunile ulterioare au o opțiune _DNS privat_. Setează-l pe Blokada Cloud, iar reclamele și trackerele vor fi blocate în toate aplicațiile, pe orice rețea, fără ca vreo aplicație să ruleze în fundal.

1. Deschide _Setări → Rețea și internet_. Pe unele telefoane aceasta apare ca _Conexiuni_ sau _Conexiune și partajare_.
2. Apasă pe _DNS privat_. Pe telefoanele Samsung, se află la _Setări suplimentare de conexiune_.
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

Dacă nu îl găsești, caută în aplicația Setări termenul "DNS privat".

## Verifică dacă funcționează

Deschide câteva aplicații sau site-uri web, apoi verifică pagina _Activitate_ din [panoul de control](https://app.blokada.org/stats?src=guides). Căutările acestui telefon vor apărea acolo.

## Dacă ceva nu funcționează

- **„Nu s-a putut conecta” sau nu există internet:** verifică numele DNS Blokada pentru eventuale greșeli de scriere. Trebuie să fie exact cum este prezentat mai sus, fără `https://`.
- **O altă aplicație VPN este activă:** unele aplicații VPN folosesc propriul DNS și ocolesc DNS-ul privat. Dezactivează DNS-ul sau setarea de blocare reclame din VPN, sau folosește Blokada 6 în loc.
- **Chrome încă afișează reclame:** Chrome poate fi setat să utilizeze propriul furnizor securizat de DNS, ceea ce ocolește DNS-ul privat. În Chrome, deschide _Setări → Confidențialitate și securitate → Utilizează DNS securizat_ și alege _Utilizează furnizorul de servicii actual_. Astfel, Chrome va folosi DNS-ul privat.
