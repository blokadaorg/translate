---
title: Une alternative à NextDNS avec la même configuration sur chaque appareil.
description: Passez de NextDNS à Blokada Cloud. Remplacez votre nom DNS, lien DoH ou profil NextDNS par celui de Blokada sur votre téléphone, ordinateur et routeur, et conservez votre blocage des publicités.
updated: 2026-10-01
order: 3
---

NextDNS et Blokada Cloud fonctionnent de la même manière : un service DNS chiffré qui bloque les publicités et les traqueurs par nom, avec vos propres paramètres disponibles via un nom DNS personnel. Changer signifie remplacer les valeurs NextDNS sur chaque appareil par vos propres valeurs Blokada. Rien d’autre ne change sur l’appareil.

## Ce que vous utilisiez et ce qu'il faut choisir dans Blokada

| Dans NextDNS                                         | Dans Blokada Cloud                                                                 |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Votre ID de configuration, par exemple \`abc123\`  | Votre étiquette d'appareil, faisant partie de votre nom DNS Blokada et du lien DoH |
| Listes de blocage _Confidentialité_                  | _Listes de blocage_ dans le tableau de bord                                        |
| _Sécurité_ (malware, hameçonnage) | une liste malwares dans _Listes de blocage_                                        |
| _Contrôle parental_                                  | listes de contenus adultes et de jeux d’argent dans _Listes de blocage_            |
| _Liste d’autorisation_ et _Liste de blocage_         | _Exceptions_ dans le tableau de bord                                               |
| _Journaux_ et _Analyses_                             | _Activité_ et _Statistiques_ dans le tableau de bord                               |

## Vos informations Blokada

- Votre nom DNS Blokada, pour DNS over TLS : {% dot %}
- Votre lien DoH, pour DNS over HTTPS : {% doh %}

## Changer chaque appareil

### Android

Si vous utilisiez le _DNS privé_ avec `<your-id>.dns.nextdns.io`, remplacez-le par votre nom DNS Blokada, comme indiqué dans le [guide Android](../android-private-dns/). Si vous utilisiez l’application NextDNS, désinstallez-la et installez [Blokada 6](https://go.blokada.org/play_cloud) à la place.

### iPhone et iPad

Si vous utilisiez l’application NextDNS, désinstallez-la et installez [Blokada 6](https://go.blokada.org/appstore). Si vous avez installé plutôt un profil NextDNS, supprimez-le dans _Réglages → Général → VPN et gestion des appareils_, puis suivez le [guide Apple](../apple-devices/).

### Mac et Apple TV

Supprimez le profil ou l’application NextDNS, puis installez le profil Blokada depuis le [guide Apple](../apple-devices/).

### Windows et Linux

Désinstallez l’application NextDNS si vous l’utilisez. Sous Windows, remplacez le serveur NextDNS et le modèle DoH par ceux de Blokada, comme indiqué dans le [guide Windows](../windows-dns-over-https/). Sous Linux, remplacez le serveur NextDNS dans systemd-resolved, comme indiqué dans le [guide Linux](../linux-dns-over-tls/).

### Navigateurs

Si vous avez défini `https://dns.nextdns.io/…` comme _DNS sécurisé_ de votre navigateur, remplacez-le par votre lien DoH, comme indiqué dans le [guide navigateur](../browser-dns-over-https/).

### Routeur

Si votre routeur utilise NextDNS via DNS over TLS ou DNS over HTTPS, remplacez le nom ou le lien NextDNS par celui de Blokada, comme indiqué dans le [guide routeur](../router-ad-blocking/).

S’il utilise NextDNS via des adresses IP simples avec une _IP liée_, Blokada ne peut pas encore remplacer cette fonction. La prise en charge des routeurs avec des adresses DNS standards arrive bientôt. En attendant, configurez vos appareils individuellement ou utilisez un routeur compatible avec DNS chiffré.

## Vérifiez que cela fonctionne

Ouvrez quelques sites web, puis consultez la page _Activité_ dans le tableau de bord. Vous voyez les requêtes de vos appareils, les bloquées étant signalées. Si un appareil n'apparaît pas, il utilise toujours NextDNS.
