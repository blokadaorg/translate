---
title: Configurer le DNS privé sur Android avec Blokada Cloud.
description: Utilisez le paramètre DNS privé intégré d’Android avec Blokada Cloud pour bloquer les publicités et les traqueurs dans chaque application, sur le Wi-Fi et les données mobiles. Ou laissez l’app Blokada 6 s’en charger.
updated: 02/10/2026
order: 5
---

## Le moyen le plus simple : l’application

[Blokada 6](https://go.blokada.org/play_cloud) configure tout pour vous, active et désactive le blocage en un seul geste, et affiche ce qui a été bloqué directement sur le téléphone. Connectez-vous avec votre identifiant de compte et c'est terminé.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">Obtenir Blokada 6 sur Google Play</a></p>

## Sans l'application : DNS privé

Android 9 et versions ultérieures possèdent un paramètre _DNS privé_. Réglez-le sur Blokada Cloud, et les publicités ainsi que les traqueurs seront bloqués dans toutes les applications, sur tous les réseaux, sans rien d’autre en arrière-plan.

1. Ouvrez _Paramètres → Réseau et Internet_. Sur certains téléphones, cela correspond à _Connexions_ ou _Connexion et partage_.
2. Touchez _DNS privé_. Sur les téléphones Samsung, cela se trouve dans _Plus de paramètres de connexion_.
3. Choisissez _Nom d'hôte du fournisseur DNS privé_.
4. Entrez votre nom DNS Blokada {% dot %} puis touchez _Enregistrer_.

Si vous ne le trouvez pas, recherchez "DNS privé" dans l'application Paramètres.

## Vérifiez que cela fonctionne

Ouvrez quelques applications ou sites web, puis consultez la page _Activité_ dans le [tableau de bord](https://app.blokada.org/stats?src=guides). Les requêtes de ce téléphone y seront affichées.

## Si quelque chose ne fonctionne pas

- **« Impossible de se connecter » ou pas d’Internet :** vérifiez que le nom DNS Blokada ne contient pas de faute de frappe. Il doit être exactement comme indiqué ci-dessus, sans `https://`.
- **Une autre app VPN est active :** certaines applications VPN utilisent leur propre DNS et contournent le DNS privé. Désactivez le DNS ou le blocage de publicités de l’application VPN, ou utilisez plutôt Blokada 6.
- **Chrome affiche toujours des publicités :** Chrome peut être configuré avec son propre fournisseur de DNS sécurisé, ce qui contourne le DNS privé. Dans Chrome, ouvrez _Paramètres → Confidentialité et sécurité → Utiliser un DNS sécurisé_ et choisissez _Utiliser votre fournisseur de service actuel_. Chrome suivra alors le DNS privé.
