---
title: Bloquez les publicités sur l'ensemble de votre réseau grâce au blocage des publicités via le routeur.
description: Configurez Blokada Cloud une fois sur votre routeur, et chaque appareil à la maison sera protégé, y compris les téléviseurs, consoles de jeu et enceintes connectées qui ne peuvent pas exécuter d'application de blocage des publicités.
updated: 2026-10-02
order: 4
---

Chaque appareil de votre réseau demande au routeur quel serveur DNS utiliser. Configurez le routeur avec Blokada Cloud, et toutes les publicités et trackers sont bloqués pour tout ce qui y est connecté. Cela inclut les téléviseurs connectés, consoles de jeu, clés de streaming et appareils domotiques, qui ne peuvent pas installer d'application de blocage des publicités.

## Ce dont votre routeur a besoin

Votre routeur doit prendre en charge **le DNS chiffré avec un nom d'hôte**, c'est-à-dire DNS over TLS (DoT) ou DNS over HTTPS (DoH). Beaucoup de routeurs récents le font, y compris les modèles ci-dessous. Selon la compatibilité de votre routeur, vous aurez besoin de votre nom DNS ou de votre lien DoH, tous deux disponibles sous _Vos détails_ ci-dessus.

<div class="note important">

**Adresses IP simples uniquement&nbsp;?** De nombreux routeurs de fournisseurs d'accès à Internet n'acceptent que les adresses IP pour le DNS. La prise en charge de ces appareils arrive prochainement. D'ici là, configurez vos appareils un par un : [Android](../android-private-dns/), [Mac et Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) et [navigateurs](../browser-dns-over-https/). Vous pouvez également utiliser un petit retransmetteur sur un Raspberry Pi, comme indiqué dans le [guide Pi-hole](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 ou version ultérieure.

1. Ouvrez `http://fritz.box` et allez dans _Internet → Informations sur le compte → Serveur DNS_.
2. Sous _Résolution de nom chiffrée sur Internet (DNS over TLS)_, cochez _Utiliser la résolution de nom chiffrée_.
3. Dans _Noms des résolveurs_, saisissez uniquement {% dot %}. **Supprimez toutes les autres entrées.** La FRITZ!Box utilise tous les résolveurs listés, et tout autre résolveur laissera passer des publicités.
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
2. Ouvrez _Services → HTTPS DNS Proxy_. Supprimez les instances pour les autres fournisseurs.
3. Ajoutez une instance avec une URL de résolveur personnalisée : {% doh %}
4. _Sauvegarder et appliquer_. Le paquet dirige automatiquement dnsmasq vers celui-ci.

## Autres routeurs

Cherchez un paramètre nommé _DNS over TLS_, _DNS privé_, _DNS chiffré_ ou _DNS over HTTPS_. Saisissez votre nom DNS Blokada ou le lien DoH ci-dessus, et supprimez tous les autres serveurs DNS, y compris les serveurs de secours.

## Vérifiez que cela fonctionne

1. Redémarrez un appareil, ou désactivez puis réactivez son Wi-Fi, afin qu'il prenne en compte la modification.
2. Naviguez pendant une minute, puis ouvrez la page _Activité_ dans le tableau de bord. Les requêtes de votre réseau apparaissent ici.

## Si certains appareils affichent encore des publicités

Certains appareils contournent le routeur&nbsp;: téléphones avec _DNS privé_ activé, navigateurs avec un _DNS sécurisé_ d'un autre fournisseur, et appareils qui utilisent leur propre DNS codé en dur. Configurez-les directement sur l'appareil, ou désactivez leur propre paramètre DNS.

<div class="note tip">

Derrière le routeur, tous les appareils partagent une seule adresse, ainsi le tableau de bord affiche votre réseau comme un seul appareil. Configurez les téléphones et ordinateurs portables avec leur propre nom DNS Blokada si vous souhaitez les voir séparément. Ils conservent aussi leur blocage lorsqu'ils quittent la maison.

</div>
