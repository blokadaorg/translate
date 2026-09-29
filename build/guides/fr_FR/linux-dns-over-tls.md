---
title: Bloquez les publicités sur Linux avec DNS over TLS
description: Configurez systemd-resolved pour utiliser Blokada Cloud via DNS chiffré over TLS, et bloquez les publicités et traqueurs pour chaque application sur votre ordinateur Linux.
updated: 2026-09-28
order: 9
---

La plupart des distributions Linux récentes, y compris Ubuntu et Fedora, résolvent les noms via _systemd-resolved_, qui prend en charge DNS over TLS. Sur Debian, installez-le d'abord avec `sudo apt install systemd-resolved`. Pointez-le vers Blokada Cloud, et les publicités ainsi que les traqueurs sont bloqués pour chaque application sur l'ordinateur.

## Configurer systemd-resolved

1. Créez le dossier avec `sudo mkdir -p /etc/systemd/resolved.conf.d`, puis le fichier `/etc/systemd/resolved.conf.d/blokada.conf` avec ces paramètres :

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Redémarrez-le : <code>sudo systemctl restart systemd-resolved</code></li>
<li>Vérifiez-le : <code>resolvectl status</code> affiche <code>+DNSOverTLS</code> et le serveur Blokada.</li>
</ol>

La partie après `#` est votre nom DNS Blokada : {% dot %} systemd-resolved vérifie le certificat du serveur avec celui-ci, et Blokada l'utilise pour savoir quel appareil effectue la requête.

<div class="note">

**NetworkManager** transmet aussi les serveurs DNS de votre réseau. `Domains=~.` envoie toutes les recherches à Blokada, mais si `resolvectl status` affiche toujours un autre serveur sur une connexion, désactivez l'attribution automatique du DNS pour cette connexion (l'interrupteur _Automatique_ à côté de _DNS_ dans ses paramètres IPv4 et IPv6).

</div>

## Sans systemd-resolved

Si `resolvectl` n'est pas trouvé, votre distribution résout les noms d'une autre manière. Configurez plutôt un DNS sécurisé dans votre navigateur, comme indiqué dans le [guide du navigateur](../browser-dns-over-https/), ou configurez votre [routeur](../router-ad-blocking/) pour protéger toute la maison.

## Vérifiez que cela fonctionne

Ouvrez quelques sites web, puis consultez la page _Activité_ dans le [tableau de bord](https://app.blokada.org/stats?src=guides). Les recherches de cet ordinateur apparaissent ici.

<div class="note">

Vous voulez aussi un VPN sur cet ordinateur ? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) inclut une configuration WireGuard qui chiffre tout le trafic, avec le même blocage.

</div>
