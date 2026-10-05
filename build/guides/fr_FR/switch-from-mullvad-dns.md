---
title: Mullvad DNS ferme ses portes. Gardez votre blocage des publicités avec Blokada Cloud
description: Mullvad arrête son DNS public le 2 novembre 2026. Voici comment migrer votre téléphone, ordinateur et routeur vers Blokada Cloud d'ici là, sans perdre le blocage des publicités.
updated: 2026-10-02
order: 2
---

Mullvad met fin à son service public DNS gratuit le **2 novembre 2026** et recommande Quad9 à la place. Quad9 bloque les malwares mais ne bloque **pas** les publicités ni les traqueurs. Lorsque le DNS de Mullvad s'arrête, les appareils configurés avec celui-ci cessent de charger les sites web et les applications. Si un appareil peut revenir à un autre serveur DNS, les publicités réapparaissent. Changez avant cette date.

Cette page concerne les noms DNS publics se terminant par `dns.mullvad.net`. Elle ne traite pas de l'application VPN Mullvad.

## Ce que vous utilisiez et quoi choisir dans Blokada

| Nom DNS Mullvad            | Ce qu’il bloquait                                | Dans le tableau de bord Blokada                                                                                                                                            |
| -------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | rien                                             | Blokada est un service de filtrage. Si vous ne souhaitez aucun filtrage, Quad9 ou le DNS de votre fournisseur est le choix le plus simple. |
| `adblock.dns.mullvad.net`  | publicités, pisteurs                             | une liste de blocage des publicités et pisteurs                                                                                                                            |
| `base.dns.mullvad.net`     | publicités, pisteurs, malwares                   | ajouter une liste pour les malwares                                                                                                                                        |
| `extended.dns.mullvad.net` | base plus réseaux sociaux                        | ajouter une liste réseaux sociaux                                                                                                                                          |
| `family.dns.mullvad.net`   | base plus contenus pour adultes et jeux d’argent | ajouter des listes pour contenus pour adultes et jeux d’argent                                                                                                             |
| `all.dns.mullvad.net`      | tout ce qui précède                              | les activer toutes                                                                                                                                                         |

Vous choisissez les listes de blocage dans le tableau de bord sous _Listes de blocage_. Vous pouvez les modifier à tout moment, et ces changements s'appliquent à tous vos appareils.

## Configurez chaque appareil

Blokada attribue à chaque appareil un nom unique, afin que le tableau de bord puisse afficher l'activité par appareil. Selon l'appareil, vous aurez besoin soit de votre nom DNS, soit de votre lien DoH, tous deux disponibles dans _Vos détails_ ci-dessus.

### Android

Le guide de Mullvad vous demandait de saisir un nom d’hôte sous _DNS privé_. Remplacez-le par votre nom DNS Blokada. Le [guide Android](../android-private-dns/) décrit les étapes.

### iPhone, iPad et Mac

La configuration Mullvad utilisait un profil de configuration. Supprimez-le d'abord :

- **iPhone et iPad :** _Réglages → Général → VPN et gestion des appareils_, touchez le profil DNS Mullvad, puis _Supprimer le profil_.
- **Mac :** ouvrez la liste des profils (_Réglages système → Général → Gestion des appareils_ sur macOS 15 et versions ultérieures, _Réglages système → Confidentialité et sécurité → Profils_ sur macOS 13 et 14, _Préférences système → Profils_ sur macOS 12 et antérieur), sélectionnez le profil DNS Mullvad et cliquez sur _−_.

Installez ensuite le profil Blokada depuis le [guide Apple](../apple-devices/).

### Navigateurs

Si vous avez saisi un lien DoH Mullvad tel que `https://adblock.dns.mullvad.net/dns-query` sous _DNS sécurisé_ ou _DNS via HTTPS_, remplacez-le par votre lien DoH. Le [guide navigateur](../browser-dns-over-https/) décrit les étapes pour chaque navigateur.

### Routeur

Si votre routeur utilise Mullvad sur DNS via TLS, remplacez le nom d’hôte Mullvad par votre nom DNS Blokada et supprimez les adresses IP de Mullvad. Le [guide routeur](../router-ad-blocking/) couvre les modèles courants.

## Vérifiez que cela fonctionne

Ouvrez quelques sites web, puis consultez la page _Activité_ dans le tableau de bord. Vous voyez là les recherches de vos appareils, les bloquées étant signalées. Si un appareil n'apparaît pas, il utilise encore un autre serveur DNS.
