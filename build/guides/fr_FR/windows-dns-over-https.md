---
title: Bloquez les publicités sur Windows avec DNS over HTTPS
description: Utilisez le DNS chiffré intégré à Windows 11 avec Blokada Cloud pour bloquer les publicités et les traqueurs dans chaque application et navigateur, sans installer de logiciel.
updated: 2026-09-28
order: 8
---

Windows 11 peut envoyer toutes ses requêtes DNS de façon chiffrée, via DNS over HTTPS. Configurez Blokada Cloud et les publicités ainsi que les traqueurs seront bloqués dans chaque application et navigateur du PC, sans rien installer.

Vous avez besoin de deux valeurs :

- Serveur DNS (adresse IP) : {% ip "doh" %}
- Votre lien DoH : {% doh %}

## Windows 11

1. Ouvrez _Paramètres → Réseau et Internet_, puis _Wi-Fi_ ou _Ethernet_, selon la façon dont l’ordinateur est connecté.
2. Ouvrez les _Propriétés matérielles_ de votre connexion. Pour le Wi-Fi, sélectionnez _Gérer les réseaux connus_ puis le réseau, ou _Propriétés matérielles_ en haut de la page Wi-Fi.
3. À côté de _Attribution du serveur DNS_, sélectionnez _Modifier_. Choisissez _Manuel_ et activez _IPv4_.
4. Dans _DNS préféré_, entrez le serveur DNS {% ip "doh" %}
5. Activez _DNS over HTTPS_ sur _Activé (modèle manuel)_, puis collez votre lien DoH {% doh %} comme _Modèle DoH_.
6. Désactivez _Revenir en texte clair_, puis sélectionnez _Enregistrer_.

Si l’ordinateur utilise à la fois le Wi-Fi et l’Ethernet, répétez ceci pour l’autre connexion.

<div class="note">

Laissez _DNS alternatif_ vide. Windows utilise les deux serveurs, et un autre serveur laisse passer les publicités.

Pas d’option _Activé (modèle manuel)_ ? Votre Windows 11 est plus ancien. Mettez à jour Windows ou utilisez le [guide navigateur](../browser-dns-over-https/) en attendant.

Si certaines publicités passent encore sur un réseau avec IPv6, il se peut que Windows utilise aussi le serveur DNS IPv6 de votre routeur. Désactivez _Protocole Internet version 6 (TCP/IPv6)_ dans les propriétés de l’adaptateur (_Panneau de configuration → Connexions réseau_), ou configurez votre [routeur](../router-ad-blocking/).

</div>

## Windows 10

Windows 10 n’a pas de DNS chiffré intégré. Configurez un DNS sécurisé dans votre navigateur comme indiqué dans le [guide navigateur](../browser-dns-over-https/), ou configurez votre [routeur](../router-ad-blocking/) pour couvrir toute la maison.

## Vérifiez que cela fonctionne

Ouvrez quelques sites web puis consultez la page _Activité_ dans le [tableau de bord](https://app.blokada.org/stats?src=guides). Les requêtes de cet ordinateur s’y afficheront.

Les navigateurs dotés de leur propre paramètre _DNS sécurisé_ contournent Windows. Dans Chrome et Edge, configurez-le pour utiliser le fournisseur de service actuel ou votre lien DoH.

<div class="note">

Vous souhaitez aussi un VPN sur cet ordinateur ? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) comprend une configuration WireGuard qui chiffre tout le trafic, avec le même blocage.

</div>
