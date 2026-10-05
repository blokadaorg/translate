---
title: Blocca le pubblicità su Mac e Apple TV con un profilo DNS di Blokada
description: Installa un profilo DNS Blokada Cloud per bloccare pubblicità e tracker su tutto il sistema su Mac o Apple TV, con DNS criptato e senza nulla in esecuzione in background.
updated: 02/10/2026
order: 6
---

I dispositivi Apple possono utilizzare il DNS crittografato per l'intero sistema tramite un profilo di configurazione. Il profilo di Blokada indirizza il dispositivo a Blokada Cloud, che blocca pubblicità e tracker in ogni app e browser.

Funziona su macOS 11 (Big Sur), tvOS 14, iOS e iPadOS 14 e versioni successive.

<div class="if-no-device">

Questa pagina non conosce ancora il tuo dispositivo, quindi non può offrire il tuo profilo. Accedi alla dashboard, apri _Setup_, scegli il tuo dispositivo e apri questa guida con _Apri su un altro dispositivo_.

<p><a class=\"btn btn-outline\" href=\"https://app.blokada.org/setup?src=guides\">Ottieni il link del mio profilo</a></p>

</div>

## iPhone e iPad

Il modo più semplice è tramite l'app. [Blokada 6](https://go.blokada.org/appstore) configura tutto per te, attiva e disattiva il blocco con un solo tocco e mostra ciò che è stato bloccato direttamente sul telefono. Accedi con il tuo ID account e hai finito.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/appstore\">Scarica Blokada 6 su App Store</a></p>

### Senza l’app

In alternativa puoi installare il profilo. iPhone e iPad installano i profili solo da **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Questa pagina è aperta in un altro browser. Copia il tuo link e aprilo in Safari per continuare lì: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tocca il pulsante qui sotto, poi _Consenti_ per scaricare il profilo.
2. Apri _Impostazioni_. Tocca _Profilo scaricato_ vicino alla parte superiore. Puoi trovarlo anche sotto _Generali → VPN e gestione dispositivo_.
3. Tocca _Installa_, inserisci il tuo codice e conferma.

</div>

<p class="if-device if-safari">{% appleProfile %}Scarica il mio profilo{% endappleProfile %}</p>

## Mac

1. Fai clic sul pulsante qui sotto per scaricare il profilo.
2. Apri l’elenco dei profili: _Impostazioni di sistema → Generali → Gestione dispositivi_ su macOS 15 e successivi, _Impostazioni di sistema → Privacy e sicurezza → Profili_ su macOS 13 e 14, oppure _Preferenze di sistema → Profili_ su macOS 12 e precedenti.
3. Fai doppio clic sul profilo Blokada e poi clicca su _Installa_.

<p class="if-device">{% appleProfile %}Scarica il mio profilo{% endappleProfile %}</p>

## Apple TV

L’Apple TV non può aprire pagine web, quindi devi digitare il tuo link del profilo su di essa.

1. Il link del tuo profilo: {% appleUrl %}
2. Su Apple TV, apri _Impostazioni → Generali → Privacy e sicurezza_.
3. Evidenzia _Condividi analisi Apple TV_. Non selezionarla. Premi invece il pulsante Play/Pausa sul telecomando.
4. Scegli _Aggiungi profilo_ e inserisci il link del tuo profilo. Digitare è più semplice con la tastiera dell'iPhone, dove puoi incollarlo. Installa il profilo e conferma.

<div class="note aside">

**Apple TV e altri dispositivi a casa:** Se configuri Blokada Cloud sul [router](../router-ad-blocking/), anche Apple TV e tutti gli altri dispositivi saranno protetti.

</div>

## Verifica che funzioni

Naviga per un minuto, poi apri la pagina _Attività_ nella [dashboard](https://app.blokada.org/stats?src=guides). Le richieste di questo dispositivo verranno visualizzate lì.

Per rimuovere Blokada in seguito, elimina il profilo dove lo hai installato.
