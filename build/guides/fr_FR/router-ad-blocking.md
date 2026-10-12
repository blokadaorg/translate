---
title: Bloquez les publicités sur l'ensemble de votre réseau grâce au blocage des publicités via le routeur.
description: Configurez Blokada Cloud une fois sur votre routeur, et chaque appareil à la maison sera protégé, y compris les téléviseurs, consoles de jeu et enceintes connectées qui ne peuvent pas exécuter d'application de blocage des publicités.
updated: 2026-10-09
order: 4
---

Chaque appareil de votre réseau demande au routeur quel serveur DNS utiliser. Pointez le routeur vers Blokada Cloud, et les publicités ainsi que les traqueurs seront bloqués pour tout ce qui se trouve derrière lui. Cela inclut les téléviseurs intelligents, les consoles de jeux, les clés de streaming et les appareils domotiques, qui ne peuvent pas accueillir d’application de blocage des publicités.

## Ce dont votre routeur a besoin

Il existe deux façons de configurer un routeur :

- **DNS chiffré avec un nom d’hôte**, c’est-à-dire DNS sur TLS (DoT) ou DNS sur HTTPS (DoH). De nombreux routeurs récents le prennent en charge, y compris les modèles ci-dessous. Selon ce que prend en charge votre routeur, vous aurez besoin de votre nom DNS ou de votre lien DoH, tous deux disponibles sous _Vos informations_ ci-dessus.
- **Une adresse DNS IPv6 simple.** De nombreux routeurs de fournisseurs d’accès à Internet n’acceptent que des adresses IP simples pour le DNS. Si c’est le cas du vôtre et que votre connexion utilise IPv6, Blokada vous fournit une adresse IPv6 à saisir. Voir [Routeurs qui n’acceptent qu’une adresse IP](#routers-that-only-take-an-ip-address).

Utilisez le DNS chiffré si votre routeur le prend en charge. Les requêtes restent privées jusqu’à Blokada.

## FRITZ!Box

FRITZ!OS 7.20 ou version ultérieure.

1. Ouvrez `http://fritz.box` et allez dans _Internet → Informations sur le compte → Serveur DNS_.
2. Sous _Résolution de nom chiffrée sur Internet (DNS over TLS)_, cochez _Utiliser la résolution de nom chiffrée_.
3. Dans _Noms résolus du serveur DNS_, saisissez uniquement {% dot %}. **Supprimez toutes les autres entrées.** La FRITZ!Box utilise tous les résolveurs listés, et tout autre résolveur laissera passer des publicités.
4. Cochez l’option qui impose la vérification du certificat et décochez celle qui autorise la résolution de nom non chiffrée en cas d’échec.
5. Si vous voyez _Basculement sur des serveurs DNS publics en cas d'interruption du DNS_, désactivez cette option.
6. Cliquez sur _Appliquer_.

## ASUS

Micrologiciel ASUS récent (3.0.0.4.388 ou version ultérieure) et Asuswrt-Merlin.

1. Ouvrez la page d'administration du routeur et allez dans _WAN → Connexion Internet_.
2. Dans _Paramètres DNS du WAN_, définissez _Protocole de confidentialité DNS_ sur _DNS-over-TLS (DoT)_ et _Profil DNS-over-TLS_ sur _Strict_.
3. Supprimez chaque entrée de la _liste des serveurs DNS-over-TLS_, puis ajoutez-en une :
   - Adresse : {% ip \"dot\" %}
   - Nom d'hôte TLS : {% dot %}
4. Cliquez sur _Appliquer_.

## OpenWrt

1. Dans _Système → Logiciel_, mettez à jour les listes et installez `luci-app-https-dns-proxy`.
2. Ouvrez _Services → HTTPS DNS Proxy_. Supprimez les instances des autres fournisseurs.
3. Ajoutez une instance avec une URL de résolveur personnalisée : {% doh %}
4. _Sauvegarder & Appliquer_. Le paquet dirige automatiquement dnsmasq vers celui-ci.

## Autres routeurs

Recherchez un paramètre appelé _DNS over TLS_, _DNS privé_, _DNS chiffré_ ou _DNS over HTTPS_. Saisissez votre nom DNS Blokada ou le lien DoH indiqué ci-dessus, puis supprimez tous les autres serveurs DNS, y compris les serveurs de secours. S'il n'existe pas un tel paramètre, utilisez une adresse IPv6 simple comme ci-dessous.

## Routeurs qui n'acceptent qu'une adresse IP {:#routers-that-only-take-an-ip-address}

Votre routeur et votre connexion Internet doivent prendre en charge IPv6 pour cette configuration. Le support des adresses IPv4 simples arrivera prochainement.

1. Dans le [tableau de bord](https://app.blokada.org/setup?src=guides), ouvrez _Configuration_ et choisissez _Routeur, TV, console de jeux_.
2. Nommez le routeur, par exemple _Routeur principal_, et sélectionnez _Obtenir l'adresse_. Le nom apparaîtra dans votre activité et ne pourra pas être modifié plus tard.
3. Dans les paramètres du routeur, trouvez les serveurs DNS pour IPv6, souvent sous _Internet_, _WAN_ ou _IPv6_, et saisissez l'adresse comme unique serveur DNS.
4. **Supprimez tous les autres serveurs DNS, y compris les serveurs IPv4.** Les appareils qui continuent de recevoir un serveur DNS IPv4 du routeur envoient certaines requêtes en dehors de Blokada. Si le routeur ne peut pas laisser le champ DNS IPv4 vide, configurez vos appareils individuellement : [Android](../android-private-dns/), [Mac et Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) et [navigateurs](../browser-dns-over-https/).

Cette configuration fonctionne aussi pour une TV ou une console de jeux vous permettant de saisir manuellement un serveur DNS. Attribuez à chacune une adresse distincte pour qu'elle s'affiche par nom dans votre activité.

<div class="note aside">

Ces recherches voyagent sans chiffrement vers Blokada, comme avec n'importe quel serveur DNS classique. Si votre routeur prend en charge DNS over TLS ou DNS over HTTPS, privilégiez ce mode.

</div>

## Vérifiez que cela fonctionne

1. Redémarrez un appareil, ou désactivez puis réactivez son Wi-Fi, afin qu'il prenne en compte la modification.
2. Sur cet appareil, désactivez Blokada s'il l'utilise, puis ouvrez [go.blokada.org/test](https://go.blokada.org/test). Ceci indiquera si votre DNS passe par Blokada.
3. Naviguez pendant une minute, puis ouvrez la page _Activité_ dans le [tableau de bord](https://app.blokada.org/stats?src=guides). Les recherches de votre réseau y apparaîtront.

## Si certains appareils affichent encore des publicités

Certains appareils contournent le routeur : téléphones avec _DNS privé_ activé, navigateurs avec _DNS sécurisé_ configuré sur un autre fournisseur, et appareils qui utilisent leur propre DNS codé en dur. Configurez ces appareils directement ou désactivez leur réglage DNS.

<div class="note tip">

Derrière le routeur, tous les appareils partagent une seule adresse, donc le tableau de bord affichera votre réseau comme un seul appareil. Configurez téléphones et ordinateurs portables avec leur propre nom DNS Blokada si vous souhaitez les voir séparément. Ils conserveront aussi leur blocage lorsqu’ils quitteront la maison.

</div>
