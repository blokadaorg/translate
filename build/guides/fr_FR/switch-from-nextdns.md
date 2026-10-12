---
title: Une alternative à NextDNS avec la même configuration sur chaque appareil.
description: Passez de NextDNS à Blokada Cloud. Remplacez le nom DNS, le lien DoH ou le profil NextDNS par ceux de Blokada sur votre téléphone, ordinateur et routeur, et conservez votre blocage des publicités.
updated: 2026-10-09
order: 3
---

NextDNS et Blokada Cloud fonctionnent de la même manière : un service DNS chiffré qui bloque les publicités et les traqueurs par nom, avec vos propres réglages associés à un nom DNS personnel. Passer de l'un à l'autre consiste simplement à remplacer les valeurs NextDNS sur chaque appareil par celles de Blokada. Rien d'autre ne change sur l'appareil.

## Ce que vous utilisiez et ce qu'il faut choisir dans Blokada

| Dans NextDNS                                         | Dans Blokada Cloud                                                                 |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Votre ID de configuration, par exemple \`abc123\`  | Votre étiquette d'appareil, faisant partie de votre nom DNS Blokada et du lien DoH |
| Listes de blocage _Confidentialité_                  | _Listes de blocage_ dans le tableau de bord                                        |
| _Sécurité_ (malware, hameçonnage) | une liste malwares dans _Listes de blocage_                                        |
| _Contrôle parental_                                  | listes de contenus adultes et de jeux d’argent dans _Listes de blocage_            |
| _Liste d’autorisation_ et _Liste de blocage_         | _Exceptions_ dans le tableau de bord                                               |
| _Journaux_ et _Analyses_                             | _Activité_ et _Statistiques_ dans le tableau de bord                               |

## Changer chaque appareil

Selon l'appareil, vous aurez besoin de votre nom DNS ou de votre lien DoH, tous deux accessibles dans _Vos informations_ ci-dessus.

### Android

Si vous utilisiez _DNS privé_ avec `<your-id>.dns.nextdns.io`, remplacez-le par votre nom DNS Blokada, comme indiqué dans le [guide Android](../android-private-dns/). Si vous utilisiez l’application NextDNS, désinstallez-la et installez [Blokada 6](https://go.blokada.org/play_cloud) à la place.

### iPhone et iPad

Si vous utilisiez l’application NextDNS, désinstallez-la et installez [Blokada 6](https://go.blokada.org/appstore). Si vous aviez installé un profil NextDNS à la place, supprimez-le dans _Réglages → Général → VPN et gestion des appareils_, puis suivez le [guide Apple](../apple-devices/).

### Mac et Apple TV

Supprimez le profil ou l’application NextDNS, puis installez le profil Blokada depuis le [guide Apple](../apple-devices/).

### Windows et Linux

Désinstallez l’application NextDNS si vous l’utilisez. Sous Windows, remplacez le serveur NextDNS et le modèle DoH par ceux de Blokada, comme indiqué dans le [guide Windows](../windows-dns-over-https/). Sous Linux, remplacez le serveur NextDNS dans systemd-resolved, comme expliqué dans le [guide Linux](../linux-dns-over-tls/).

### Navigateurs

Si vous avez défini `https://dns.nextdns.io/…` comme _DNS sécurisé_ de votre navigateur, remplacez-le par votre lien DoH, comme indiqué dans le [guide navigateur](../browser-dns-over-https/).

### Routeur

Si votre routeur utilise NextDNS via DNS over TLS ou DNS over HTTPS, remplacez le nom ou le lien NextDNS par celui de Blokada, comme indiqué dans le [guide routeur](../router-ad-blocking/).

Si NextDNS utilise des adresses IP simples, remplacez-les par une adresse IPv6 de Blokada, comme indiqué dans le [guide du routeur](../router-ad-blocking/). Cela nécessite IPv6 sur votre connexion, et les requêtes ne seront pas chiffrées. Blokada ne propose pas encore d'adresses IPv4 simples, donc une configuration avec une _IP liée_ de NextDNS ne peut pas être reprise telle quelle. Sans IPv6, configurez vos appareils un par un, ou utilisez un routeur qui prend en charge le DNS chiffré.

## Vérifiez que cela fonctionne

Ouvrez quelques sites web, puis consultez la page _Activité_ dans le tableau de bord. Vous y verrez les requêtes de vos appareils, avec celles bloquées indiquées. Si un appareil n’apparaît pas, il utilise encore NextDNS.
