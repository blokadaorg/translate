---
title: Blocca le pubblicità in Chrome, Firefox, Edge e Brave con DNS over HTTPS
description: Imposta Blokada Cloud come provider DNS sicuro nel tuo browser per bloccare pubblicità e tracker, su qualsiasi computer, inclusi i portatili aziendali dove non puoi installare app.
updated: 02/10/2026
order: 7
---

I browser moderni possono utilizzare un proprio provider DNS crittografato, chiamato _DNS sicuro_ o _DNS over HTTPS_. Impostalo su Blokada Cloud e il browser bloccherà annunci e tracker su qualsiasi rete, senza dover installare estensioni.

Questa impostazione copre solo questo browser. Per coprire l’intero computer, usa il [profilo Apple](../apple-devices/) su un Mac o configura il tuo [router](../router-ad-blocking/).

## Chrome

1. Apri `chrome://settings/security`.
2. Attiva _Usa DNS sicuro_, poi scegli _Aggiungi provider DNS personalizzato_.
3. Inserisci {% doh %}

## Edge

1. Apri `edge://settings/privacy`.
2. Sotto _Sicurezza_, attiva _Usa DNS sicuro per specificare come cercare l’indirizzo di rete dei siti web_.
3. Scegli _Scegli un provider di servizi_ e inserisci {% doh %}

## Firefox

1. Apri _Impostazioni → Privacy e sicurezza_ e scorri fino a _DNS over HTTPS_.
2. Scegli _Massima protezione_.
3. In _Scegli provider_, seleziona _Personalizzato_ e inserisci {% doh %}

## Brave

1. Apri `brave://settings/security`.
2. Attiva _Usa DNS sicuro_, poi scegli _Aggiungi provider DNS personalizzato_.
3. Inserisci {% doh %}

## Safari

Safari non ha un’impostazione DNS sicura propria. Utilizza il DNS di sistema, quindi installa il [profilo Apple](../apple-devices/).

## Verifica che funzioni

Naviga per un minuto, poi apri la pagina _Attività_ nella [dashboard](https://app.blokada.org/stats?src=guides). Le richieste da questo browser appariranno lì.

## Se qualcosa non va

<div class="note tip">

Se il tuo browser è gestito dal lavoro o dalla scuola, l’impostazione DNS sicura potrebbe essere bloccata. Chiedi all’amministratore.

</div>
