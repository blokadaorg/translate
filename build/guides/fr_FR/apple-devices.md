---
title: Bloquez les publicités sur Mac et Apple TV avec un profil DNS Blokada
description: Installez un profil DNS Blokada Cloud pour bloquer les publicités et les traqueurs sur tout le système d’un Mac ou d’une Apple TV, avec un DNS chiffré et aucun processus en arrière-plan.
updated: 2026-09-28
order: 6
---

Les appareils Apple peuvent utiliser un DNS chiffré pour tout le système via un profil de configuration. Le profil Blokada dirige l’appareil vers Blokada Cloud, qui bloque les publicités et les traqueurs dans chaque application et navigateur.

Il fonctionne sur macOS 11 (Big Sur), tvOS 14, iOS et iPadOS 14 et versions ultérieures.

<div class="if-no-device">

Cette page ne connaît pas encore votre appareil, donc elle ne peut pas proposer votre profil. Connectez-vous au tableau de bord, ouvrez _Configuration_, choisissez votre appareil, puis ouvrez ce guide avec _Ouvrir sur un autre appareil_.

<p><a class=\"btn btn-outline\" href=\"https://app.blokada.org/setup?src=guides\">Obtenir mon lien de profil</a></p>

</div>

## iPhone et iPad

Le moyen le plus simple est l’application. [Blokada 6](https://go.blokada.org/appstore) configure tout pour vous, active ou désactive le blocage avec une seule pression et affiche ce qui a été bloqué directement sur le téléphone. Connectez-vous avec l’ID de votre compte et c’est terminé.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/appstore\">Téléchargez Blokada 6 sur l'App Store</a></p>

### Sans l’application

Vous pouvez installer le profil à la place. Les iPhone et iPad installent uniquement les profils depuis **Safari**.

<div class="if-device">
<div class="if-other-browser note">

Cette page est ouverte dans un autre navigateur. Copiez votre lien et ouvrez-le dans Safari pour continuer là-bas : {% pageLink %}

</div>
</div>

<div class="if-safari">

1. Dans Safari, touchez le bouton ci-dessous, puis _Autoriser_ pour télécharger le profil.
2. Ouvrez les Paramètres. Touchez _Profil téléchargé_ en haut de l’écran. Vous pouvez aussi le trouver sous _Général → VPN et gestion des appareils_.
3. Touchez _Installer_, saisissez votre code d’accès, puis confirmez.

</div>

<p class="if-device if-safari">{% appleProfile %}Télécharger mon profil{% endappleProfile %}</p>

## Mac

1. Cliquez sur le bouton ci-dessous pour télécharger le profil.
2. Ouvrez la liste des profils : _Paramètres système → Général → Gestion des appareils_ sur macOS 15 et ultérieur, _Paramètres système → Confidentialité et sécurité → Profils_ sur macOS 13 et 14, ou _Préférences Système → Profils_ sur macOS 12 et versions antérieures.
3. Double-cliquez sur le profil Blokada et cliquez sur _Installer_.

<p class="if-device">{% appleProfile %}Télécharger mon profil{% endappleProfile %}</p>

## Apple TV

L’Apple TV ne peut pas ouvrir de pages Web, vous devez donc saisir votre lien de profil dessus.

1. Lien de votre profil : {% appleUrl %}
2. Sur l’Apple TV, ouvrez _Réglages → Général → Confidentialité et sécurité_.
3. Sélectionnez _Envoyer à Apple_ (appelé _Partager les analyses Apple TV_ sur les versions tvOS plus anciennes). Ne le sélectionnez pas. Appuyez sur le bouton Lecture/Pause de la télécommande à la place.
4. Choisissez _Ajouter un profil_ et saisissez votre lien de profil. Il est plus facile de taper à l’aide du clavier affiché sur votre iPhone, où vous pouvez coller le lien. Installez le profil puis confirmez.

<div class="note">

**Apple TV et autres appareils à la maison :** si vous configurez Blokada Cloud sur votre [routeur](../router-ad-blocking/), l’Apple TV sera protégée ainsi que tous vos autres appareils.

</div>

## Vérifiez que cela fonctionne

Naviguez pendant une minute, puis ouvrez la page _Activité_ dans le [tableau de bord](https://app.blokada.org/stats?src=guides). Les requêtes de cet appareil apparaissent là-bas.

Pour supprimer Blokada par la suite, supprimez le profil là où vous l’avez installé.
