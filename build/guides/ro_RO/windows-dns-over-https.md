---
title: Blochează reclamele pe Windows folosind DNS peste HTTPS
description: Folosește DNS-ul criptat integrat în Windows 11 împreună cu Blokada Cloud pentru a bloca reclamele și urmăritorii în orice aplicație și browser, fără să fie nevoie să instalezi software suplimentar.
updated: 2026-10-02
order: 8
---

Windows 11 poate trimite toate interogările DNS criptat, folosind DNS peste HTTPS. Direcționează-le către Blokada Cloud și reclamele, precum și urmăritorii, vor fi blocate pe orice aplicație și browser de pe computer, fără nimic de instalat.

Ai nevoie de adresa IP a serverului DNS și de linkul tău DoH, ambele fiind la _Detaliile tale_ de mai sus.

## Windows 11

1. Deschide _Setări → Rețea și internet_, apoi _Wi-Fi_ sau _Ethernet_, în funcție de cum este conectat computerul.
2. Deschide _Proprietăți hardware_ ale conexiunii tale. Pentru Wi-Fi, selectează _Gestionează rețelele cunoscute_ și apoi rețeaua, sau _Proprietăți hardware_ din partea de sus a paginii Wi-Fi.
3. Lângă _Atribuire server DNS_, selectează _Editează_. Alege _Manual_ și activează _IPv4_.
4. La _DNS preferat_, introdu serverul DNS {% ip "doh" %}
5. Setează _DNS peste HTTPS_ pe _Activ (șablon manual)_ și lipsește linkul tău DoH {% doh %} ca _șablon DoH_.
6. Dezactivează _Trecere la text simplu_, apoi selectează _Salvează_.

Dacă computerul folosește atât Wi-Fi, cât și Ethernet, repetă pașii pentru cealaltă conexiune.

<div class="note important">

Lasă _DNS alternativ_ necompletat. Windows folosește ambii serveri, iar folosirea oricărui alt server permite reclamelor să treacă.

</div>

<div class="note tip">

Nu există opțiunea _Activ (șablon manual)_? Windows 11 este mai vechi. Actualizează Windows sau folosește [ghidul pentru browser](../browser-dns-over-https/) între timp.

</div>

## Windows 10

Windows 10 nu are DNS criptat integrat. Configurează DNS securizat în browser, ca în [ghidul pentru browser](../browser-dns-over-https/), sau configurează [routerul](../router-ad-blocking/) pentru a acoperi toată casa.

## Verifică dacă funcționează

Deschide câteva site-uri, apoi verifică pagina _Activitate_ din [panoul de control](https://app.blokada.org/stats?src=guides). Interogările acestui computer vor apărea acolo.

<div class="note aside">

Vrei și un VPN pe acest computer? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) include configurare WireGuard care criptează tot traficul, cu aceeași blocare a reclamelor.

</div>

## Dacă ceva nu funcționează

Chrome și Edge au setarea lor _DNS securizat_, care ocolește Windows. Lăsată pe automat, poate trece la DNS obișnuit, pe care Blokada îl refuză. Setează-o pe linkul tău DoH:

- **Chrome:** deschide `chrome://settings/security`, activează _Folosește DNS securizat_, iar la _Selectează furnizorul DNS_ alege _Adaugă furnizor de DNS personalizat_.
- **Edge:** deschide `edge://settings/privacy`, activează DNS securizat și alege _Alege un furnizor de servicii_.

Apoi lipește linkul tău DoH {% doh %}

Dacă unele reclame tot apar pe o rețea cu IPv6, Windows poate folosi și serverul DNS IPv6 al routerului. Dezactivează _Internet Protocol Version 6 (TCP/IPv6)_ din proprietățile adaptorului (_Panou de control → Conexiuni de rețea_) sau configurează [routerul](../router-ad-blocking/).
