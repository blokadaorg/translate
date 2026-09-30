---
title: Configura il DNS privato su Android con Blokada Cloud
description: Usa l'impostazione DNS privato integrata di Android con Blokada Cloud per bloccare annunci e tracker in ogni app, su Wi-Fi e dati mobili. Oppure lascia che sia l'app Blokada 6 a farlo.
updated: 2026-09-28
order: 5
---

## Il modo più semplice: l'app

[Blokada 6](https://go.blokada.org/play_cloud) configura tutto per te, attiva o disattiva il blocco con un tocco e mostra cosa è stato bloccato direttamente sul telefono. Accedi con l'ID del tuo account e hai finito.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">Scarica Blokada 6 su Google Play</a></p>

## Senza l'app: DNS privato

Android 9 e versioni successive hanno un'impostazione _DNS privato_. Impostalo su Blokada Cloud, e pubblicità e tracker vengono bloccati in tutte le app, su ogni rete, senza nulla in esecuzione in background.

Il tuo nome DNS Blokada: {% dot %}

1. Apri _Impostazioni → Rete e Internet_. Su alcuni telefoni si trova sotto _Connessioni_ oppure _Connessione e condivisione_.
2. Tocca _DNS privato_. Sui telefoni Samsung si trova sotto _Altre impostazioni di connessione_.
3. Scegli _Nome host DNS privato_.
4. Inserisci il tuo nome DNS Blokada {% dot %} e tocca _Salva_.

Se non riesci a trovarlo, cerca "DNS privato" nell'app Impostazioni.

## Verifica che funzioni

Apri alcune app o siti web, poi vai alla pagina _Attività_ nella [dashboard](https://app.blokada.org/stats?src=guides). Le ricerche di questo telefono saranno mostrate lì.

## Se qualcosa non funziona

- **“Impossibile connettersi” o nessuna connessione a internet:** controlla che il tuo nome DNS Blokada non abbia errori di digitazione. Deve essere esattamente come mostrato sopra, senza `https://`.
- **Un'altra app VPN è attiva:** alcune app VPN usano il proprio DNS e bypassano il DNS privato. Disattiva l'impostazione DNS o di blocco pubblicità della VPN, oppure usa Blokada 6.
- **Chrome mostra ancora pubblicità:** in Chrome, apri _Impostazioni → Privacy e sicurezza → Usa DNS sicuro_ e scegli _Usa il provider di servizi attuale_.
