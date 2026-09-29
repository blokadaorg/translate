---
title: Configurer le DNS privé sur Android avec Blokada Cloud.
description: Utilisez le paramètre de DNS privé intégré d’Android avec Blokada Cloud pour bloquer les publicités et les traqueurs dans chaque application, sur le Wi-Fi et les données mobiles. Ou laissez l’application Blokada 6 s’en charger.
updated: 2026-09-28
order: 5
---

## Le moyen le plus simple : l’application

[Blokada 6](https://go.blokada.org/play_cloud) configure tout pour vous, active et désactive le blocage en un seul geste, et affiche ce qui a été bloqué directement sur le téléphone. Connectez-vous avec l’ID de votre compte et c’est terminé.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">Obtenir Blokada 6 sur Google Play</a></p>

## Sans l'application : DNS privé

Android 9 et versions ultérieures disposent d'un paramètre _DNS privé_. Réglez-le sur Blokada Cloud, et les publicités ainsi que les traqueurs seront bloqués dans toutes les applications, sur tous les réseaux, sans rien d'autre en arrière-plan.

Votre nom DNS Blokada : {% dot %}

1. Ouvrez _Paramètres → Réseau et Internet_. Sur certains téléphones, il s'agit de _Connexions_ ou _Connexion et partage_.
2. Appuyez sur _DNS privé_. Sur les téléphones Samsung, cela se trouve dans _Plus de paramètres de connexion_.
3. Choisissez _Nom d'hôte du fournisseur DNS privé_.
4. Entrez votre nom DNS Blokada {% dot %} puis touchez _Enregistrer_.

Si vous ne le trouvez pas, recherchez "DNS privé" dans l'application Paramètres.

## Vérifiez que cela fonctionne

Ouvrez quelques applications ou sites web, puis consultez la page _Activité_ dans le [tableau de bord](https://app.blokada.org/stats?src=guides). Les recherches DNS de ce téléphone apparaissent ici.

## Si quelque chose ne fonctionne pas

- **« Impossible de se connecter » ou pas d'internet :** vérifiez l'orthographe de votre nom DNS Blokada. Il doit être exactement comme indiqué ci-dessus, sans `https://`.
- **Une autre appli VPN est active :** certaines applis VPN utilisent leur propre DNS et contournent le DNS privé. Désactivez le paramètre DNS ou le blocage des pubs du VPN, ou utilisez plutôt Blokada 6.
- **Chrome affiche toujours des pubs :** dans Chrome, ouvrez _Paramètres → Confidentialité et sécurité → Utiliser le DNS sécurisé_ et choisissez _Utiliser le fournisseur de services actuel_.
