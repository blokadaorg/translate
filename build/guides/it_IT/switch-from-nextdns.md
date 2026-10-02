---
title: Un'alternativa a NextDNS con la stessa configurazione su ogni dispositivo.
description: Passa da NextDNS a Blokada Cloud. Sostituisci il tuo nome DNS, link DoH o profilo NextDNS con quello di Blokada sul tuo telefono, computer e router, e mantieni il blocco degli annunci.
updated: 02/10/2026
order: 3
---

NextDNS e Blokada Cloud funzionano allo stesso modo: un servizio DNS criptato che blocca annunci e tracker per nome, con le tue impostazioni dietro un nome DNS personale. Il passaggio consiste nel sostituire i valori di NextDNS su ogni dispositivo con i tuoi di Blokada. Nient'altro cambia sul dispositivo.

## Cosa usavi, e cosa scegliere su Blokada

| In NextDNS                                                   | In Blokada Cloud                                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Il tuo ID di configurazione, ad es. `abc123` | Il tag del tuo dispositivo, parte del tuo nome DNS Blokada e del link DoH |
| Liste di blocco _Privacy_                                    | _Liste di blocco_ nel pannello di controllo                               |
| _Sicurezza_ (malware, phishing)           | una lista malware sotto _Liste di blocco_                                 |
| _Controllo genitori_                                         | liste per contenuti per adulti e gioco d'azzardo sotto _Liste di blocco_  |
| _Allowlist_ e _Denylist_                                     | _Eccezioni_ nel pannello di controllo                                     |
| _Log_ e _Analitiche_                                         | _Attività_ e _Statistiche_ nel pannello di controllo                      |

## Passa ogni dispositivo

A seconda del dispositivo, ti servirà il tuo nome DNS o il tuo link DoH, entrambi disponibili sotto _I tuoi dettagli_ sopra.

### Android

Se hai usato _DNS privato_ con `<your-id>.dns.nextdns.io`, sostituiscilo con il tuo nome DNS Blokada, come indicato nella [guida Android](../android-private-dns/). Se hai usato l'app NextDNS, disinstallala e installa invece [Blokada 6](https://go.blokada.org/play_cloud).

### iPhone e iPad

Se hai usato l'app NextDNS, disinstallala e installa invece [Blokada 6](https://go.blokada.org/appstore). Se invece hai installato un profilo NextDNS, rimuovilo in _Impostazioni → Generali → VPN e gestione dispositivi_, poi segui la [guida Apple](../apple-devices/).

### Mac e Apple TV

Rimuovi il profilo o l'app NextDNS, poi installa il profilo Blokada dalla [guida Apple](../apple-devices/).

### Windows e Linux

Disinstalla l'app NextDNS se la usi. Su Windows, sostituisci il server NextDNS e il template DoH con quelli di Blokada, come spiegato nella [guida Windows](../windows-dns-over-https/). Su Linux, sostituisci il server NextDNS in systemd-resolved, come nella [guida Linux](../linux-dns-over-tls/).

### Browser

Se hai impostato `https://dns.nextdns.io/…` come _DNS sicuro_ del browser, sostituiscilo con il tuo link DoH, come nella [guida browser](../browser-dns-over-https/).

### Router

Se il tuo router utilizza NextDNS tramite DNS over TLS oppure DNS over HTTPS, sostituisci il nome o il link NextDNS con il tuo di Blokada, come spiegato nella [guida router](../router-ad-blocking/).

Se utilizza NextDNS tramite indirizzi IP semplici con un _IP collegato_, Blokada non può ancora gestire questa funzione. Il supporto per router con indirizzi DNS semplici è in arrivo. Fino ad allora, configura i tuoi dispositivi uno per uno, oppure usa un router che supporti il DNS criptato.

## Verifica che funzioni

Apri alcuni siti web, poi vai sulla pagina _Attività_ del pannello di controllo. Lì vedrai le richieste dei tuoi dispositivi, e quelle bloccate saranno segnate. Se un dispositivo non appare, sta ancora usando NextDNS.
