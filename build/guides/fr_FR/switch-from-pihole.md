---
title: Une alternative à Pi-hole qui ne nécessite aucun matériel.
description: Déplacez le blocage des publicités de votre domicile d'un Pi-hole vers Blokada Cloud, ou gardez votre Pi-hole et faites transiter ses requêtes par Blokada.
updated: 02/10/2026
order: 1
---

Un Pi-hole bloque les publicités pour chaque appareil de votre réseau, tant que le Raspberry Pi fonctionne, est à jour et présent à la maison. Blokada Cloud accomplit la même tâche depuis nos serveurs :

- **Aucun boîtier à gérer.** Pas de cartes SD, pas de mises à jour, pas de panne quand le Pi s'arrête.
- **Ça fonctionne même hors de la maison.** Les téléphones et ordinateurs portables continuent à bloquer sur les données mobiles et d'autres réseaux Wi-Fi.
- **Chiffré.** Les appareils communiquent avec Blokada via DNS sur TLS ou DNS sur HTTPS, donc votre fournisseur ne peut pas lire ni modifier vos requêtes.
- **Un seul tableau de bord.** Listes de blocage, domaines autorisés et bloqués, et activité par appareil, sur [app.blokada.org](https://app.blokada.org/?src=guides).

Il y a deux façons de procéder. Remplacer entièrement le Pi-hole, ou le conserver et utiliser Blokada Cloud comme serveur amont.

## Option 1 : remplacer le Pi-hole

1. **Procurez-vous Blokada Cloud** et ouvrez le tableau de bord. Votre nom DNS et le lien DoH se trouvent sous _Configuration_ à cet endroit, et sous _Vos informations_ ci-dessus.
2. **Pointez votre routeur vers Blokada au lieu du Pi-hole.** Suivez le [guide routeur](../router-ad-blocking/). Si votre routeur n'accepte qu'une adresse IP simple comme serveur DNS, configurez vos appareils un par un : [Android](../android-private-dns/), [Mac et Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), et [navigateurs](../browser-dns-over-https/).
3. **Si votre Pi-hole était le serveur DHCP,** réactivez DHCP dans votre routeur _avant_ d'éteindre le Pi. Sinon, vos appareils ne recevront plus d'adresses réseau.
4. **Transférez vos listes.** Dans le tableau de bord, choisissez les listes de blocage sous _Listes de blocage_, et ajoutez vos domaines autorisés ou bloqués sous _Exceptions_.
5. **Éteignez le Pi-hole,** ou gardez-le pour un autre usage.

<div class="note aside">

Votre Pi-hole affichait chaque appareil sur le réseau par son adresse IP. Avec Blokada, chaque appareil s'affiche par son propre nom, tant qu'il utilise son propre nom DNS Blokada. Un routeur configuré avec un nom DNS Blokada s'affiche comme un seul appareil.

</div>

## Option 2 : garder le Pi-hole, utiliser Blokada Cloud en amont

Si vous souhaitez conserver votre configuration locale, comme les noms d'hôtes locaux, le DHCP ou vos propres listes, laissez le Pi-hole transmettre ses requêtes à Blokada via une connexion chiffrée. Pi-hole ne peut pas transmettre de manière chiffrée lui-même, c'est pourquoi un petit transmetteur s'exécute à côté. Ce guide utilise [dnsproxy](https://github.com/AdguardTeam/dnsproxy), un transmetteur open source contenu dans un seul fichier.

1. Sur la machine Pi-hole, téléchargez la version `dnsproxy` adaptée à votre processeur (`linux-arm64` pour un Raspberry Pi récent) depuis sa page des versions, puis copiez le binaire `dnsproxy` dans `/usr/local/bin/`.
2. Créez `/etc/systemd/system/dnsproxy.service` :

<pre><code>[Unit]
Description=Transmetteur DNS chiffré vers Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns=\"dot\">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Démarrez-le : `sudo systemctl enable --now dnsproxy`
4. Dans l'administration Pi-hole, ouvrez _Paramètres → DNS_. Décochez tous les serveurs en amont puis ajoutez `127.0.0.1#5054` comme serveur en amont personnalisé. Enregistrez.
5. Consultez la page _Activité_ du tableau de bord. Les requêtes provenant de votre réseau y apparaissent désormais.

Vous pouvez désactiver les listes de blocage propres à Pi-hole et gérer le blocage dans le tableau de bord, ou garder les deux.

## Questions fréquentes

**Ai-je besoin de Blokada Plus ?** Non. Blokada Cloud assure le blocage DNS pour toute votre maison. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) ajoute un VPN en plus.

**Que se passe-t-il si Blokada est inaccessible ?** Vos appareils ne peuvent pas résoudre les noms tant qu'il n'est pas rétabli, comme lorsque le Pi-hole tombe en panne. N'ajoutez pas de second serveur DNS non filtré en secours. La plupart des appareils utilisent tous leurs serveurs de façon aléatoire, donc les publicités pourraient passer.
