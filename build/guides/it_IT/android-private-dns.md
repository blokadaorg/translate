---
title: Configura il DNS privato su Android con Blokada Cloud
description: Usa l'impostazione DNS privato integrata di Android con Blokada Cloud per bloccare annunci e tracker in ogni app, su Wi-Fi e dati mobili. Oppure lascia che l'app Blokada 6 lo faccia per te.
updated: 02/10/2026
order: 5
---

## Il modo più semplice: l'app

[Blokada 6](https://go.blokada.org/play_cloud) configura tutto per te, attiva o disattiva il blocco con un tocco e mostra cosa è stato bloccato direttamente sul telefono. Accedi con il tuo ID account e hai finito.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">Scarica Blokada 6 su Google Play</a></p>

## Senza l'app: DNS privato

Android 9 e versioni successive hanno un'impostazione _DNS privato_. Impostalo su Blokada Cloud, e pubblicità e tracker vengono bloccati in tutte le app, su ogni rete, senza nulla in esecuzione in background.

1. Apri _Impostazioni → Rete e Internet_. Su alcuni telefoni si trova sotto _Connessioni_ oppure _Connessione e condivisione_.
2. Tocca _DNS privato_. Sui telefoni Samsung si trova sotto _Altre impostazioni di connessione_.
3. Scegli _Nome host DNS privato_.
4. Inserisci il tuo nome DNS Blokada {% dot %} e tocca _Salva_.

Se non riesci a trovarlo, cerca "DNS privato" nell'app Impostazioni.

## Verifica che funzioni

Apri alcune app o siti web, poi vai alla pagina _Attività_ nella [dashboard](https://app.blokada.org/stats?src=guides). Le richieste di questo telefono appariranno lì.

## Se qualcosa non funziona

- **"Impossibile connettersi" o nessuna connessione internet:** controlla che il nome DNS di Blokada sia corretto e senza errori di battitura. Deve essere esattamente come mostrato sopra, senza `https://`.
- **Un'altra app VPN è attiva:** alcune app VPN utilizzano il proprio DNS e aggirano il DNS privato. Disattiva il DNS o il blocco annunci dell'app VPN, oppure utilizza Blokada 6.
- **Chrome mostra ancora annunci:** Chrome potrebbe essere impostato su un proprio provider di DNS sicuro, che aggira il DNS privato. In Chrome, vai su _Impostazioni → Privacy e sicurezza → Utilizza DNS sicuro_ e scegli _Utilizza il tuo attuale fornitore di servizi_. Chrome a quel punto seguirà il DNS privato.
