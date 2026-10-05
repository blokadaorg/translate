---
title: Bloquez les publicités dans Chrome, Firefox, Edge et Brave avec DNS sur HTTPS.
description: Définissez Blokada Cloud en tant que fournisseur DNS sécurisé dans votre navigateur pour bloquer les publicités et les traqueurs, sur n'importe quel ordinateur, y compris les ordinateurs professionnels où vous ne pouvez pas installer d'applications.
updated: 2026-10-02
order: 7
---

Les navigateurs modernes peuvent utiliser leur propre fournisseur de DNS chiffré, appelé _DNS sécurisé_ ou _DNS over HTTPS_. Configurez-le sur Blokada Cloud, et le navigateur bloque les publicités et les traqueurs sur n'importe quel réseau, sans extension à installer.

Ce paramètre couvre uniquement ce navigateur. Pour couvrir tout l'ordinateur, utilisez le [profil Apple](../apple-devices/) sur un Mac, ou configurez votre [routeur](../router-ad-blocking/).

## Chrome

1. Ouvrez `chrome://settings/security`.
2. Activez _Utiliser DNS sécurisé_, puis choisissez _Ajouter un fournisseur de service DNS personnalisé_.
3. Entrez {% doh %}

## Edge

1. Ouvrez `edge://settings/privacy`.
2. Sous _Sécurité_, activez _Utiliser DNS sécurisé pour spécifier comment rechercher l'adresse réseau des sites web_.
3. Choisissez _Choisir un fournisseur de service_ et entrez {% doh %}

## Firefox

1. Ouvrez _Paramètres → Vie privée et sécurité_ puis faites défiler jusqu'à _DNS sur HTTPS_.
2. Choisissez _Protection maximale_.
3. Sous _Choisir un fournisseur_, sélectionnez _Personnalisé_ et entrez {% doh %}

## Brave

1. Ouvrez `brave://settings/security`.
2. Activez _Utiliser DNS sécurisé_, puis choisissez _Ajouter un fournisseur de service DNS personnalisé_.
3. Entrez {% doh %}

## Safari

Safari ne possède pas de paramètre DNS sécurisé propre. Il utilise le DNS du système, donc installez le [profil Apple](../apple-devices/).

## Vérifiez que cela fonctionne

Naviguez pendant une minute, puis ouvrez la page _Activité_ dans le [tableau de bord](https://app.blokada.org/stats?src=guides). Les requêtes de ce navigateur s'y afficheront.

## Si quelque chose ne fonctionne pas

<div class="note tip">

Si votre navigateur est géré par votre entreprise ou école, le paramètre DNS sécurisé peut être verrouillé. Demandez à votre administrateur.

</div>
