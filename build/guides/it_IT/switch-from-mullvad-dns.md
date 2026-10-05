---
title: Mullvad DNS sta chiudendo. Mantieni il blocco della pubblicità con Blokada Cloud
description: Mullvad chiude il suo DNS pubblico il 2 novembre 2026. Ecco come migrare il tuo telefono, computer e router a Blokada Cloud entro quella data, senza perdere il blocco della pubblicità.
updated: 02/10/2026
order: 2
---

Mullvad sta chiudendo il suo servizio DNS pubblico gratuito il **2 novembre 2026** e consiglia invece Quad9. Quad9 blocca i malware ma **non** blocca pubblicità o tracker. Quando il DNS di Mullvad smette di funzionare, i dispositivi impostati su di esso smetteranno di caricare siti web e app. Dove un dispositivo può passare a un altro server DNS, la pubblicità tornerà. Passa a un nuovo servizio prima di quella data.

Questa pagina riguarda i nomi DNS pubblici che terminano con `dns.mullvad.net`. Non tratta l'app Mullvad VPN.

## Cosa usavi e cosa scegliere in Blokada

| Nome DNS Mullvad           | Cosa veniva bloccato                            | Nel pannello di controllo di Blokada                                                                                                                            |
| -------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | niente                                          | Blokada è un servizio di filtraggio. Se non vuoi alcun filtraggio, Quad9 o il DNS del tuo provider sono la scelta più semplice. |
| `adblock.dns.mullvad.net`  | pubblicità, tracker                             | una lista di blocco per pubblicità e tracker                                                                                                                    |
| `base.dns.mullvad.net`     | pubblicità, tracker, malware                    | aggiungi una lista malware                                                                                                                                      |
| `extended.dns.mullvad.net` | base più social media                           | aggiungi una lista social media                                                                                                                                 |
| `family.dns.mullvad.net`   | base più contenuti per adulti e gioco d'azzardo | aggiungi le liste per contenuti per adulti e gioco d'azzardo                                                                                                    |
| `all.dns.mullvad.net`      | tutti i precedenti                              | attivali tutti                                                                                                                                                  |

Puoi scegliere le blocklist nel dashboard sotto _Blocklists_. Puoi cambiarle in qualsiasi momento, e la modifica si applica a tutti i tuoi dispositivi.

## Cambia su ogni dispositivo

Blokada assegna a ciascun dispositivo il proprio nome, così il dashboard può mostrare l'attività per dispositivo. A seconda del dispositivo, ti serve il tuo nome DNS o il tuo link DoH, entrambi nella sezione _I tuoi dettagli_ qui sopra.

### Android

La guida di Mullvad ti faceva inserire un hostname sotto _DNS privato_. Sostituiscilo con il tuo nome DNS Blokada. La [guida Android](../android-private-dns/) contiene i passaggi.

### iPhone, iPad e Mac

La configurazione di Mullvad utilizzava un profilo di configurazione. Rimuovilo prima:

- **iPhone e iPad:** _Impostazioni → Generali → VPN e gestione dispositivi_, tocca il profilo DNS di Mullvad, quindi _Rimuovi profilo_.
- **Mac:** apri la lista dei profili (_Impostazioni di sistema → Generali → Gestione dispositivi_ su macOS 15 e successivi, _Impostazioni di sistema → Privacy e sicurezza → Profili_ su macOS 13 e 14, _Preferenze di sistema → Profili_ su macOS 12 e precedenti), seleziona il profilo DNS di Mullvad e fai clic su _−_.

Poi installa il profilo Blokada dalla [guida Apple](../apple-devices/).

### Browser

Se hai inserito un link DoH di Mullvad come `https://adblock.dns.mullvad.net/dns-query` sotto _DNS sicuro_ o _DNS over HTTPS_, sostituiscilo con il tuo link DoH. La [guida browser](../browser-dns-over-https/) contiene i passaggi per ogni browser.

### Router

Se il tuo router utilizza Mullvad su DNS over TLS, sostituisci l’hostname Mullvad con il tuo nome DNS Blokada e rimuovi gli indirizzi IP di Mullvad. La [guida router](../router-ad-blocking/) copre i modelli più comuni.

## Verifica che funzioni

Apri alcuni siti web, poi guarda la pagina _Attività_ nel dashboard. Lì vedi le richieste dei tuoi dispositivi, con quelle bloccate segnalate. Se un dispositivo non appare, sta ancora utilizzando un altro server DNS.
