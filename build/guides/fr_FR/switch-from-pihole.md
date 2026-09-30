---
title: Une alternative à Pi-hole qui ne nécessite aucun matériel.
description: Déplacez le blocage des publicités de votre domicile d'un Pi-hole vers Blokada Cloud, ou gardez votre Pi-hole et faites transiter ses requêtes par Blokada.
updated: 2026-09-23
order: 1
---

Un Pi-hole bloque les publicités pour chaque appareil sur votre réseau, tant que le Raspberry Pi fonctionne, est à jour et se trouve à la maison. Blokada Cloud fait le même travail depuis nos serveurs :

- **Aucun boîtier à gérer.** Pas de cartes SD, pas de mises à jour, pas de panne quand le Pi s'arrête.
- **Ça fonctionne même hors de la maison.** Les téléphones et ordinateurs portables continuent à bloquer sur les données mobiles et d'autres réseaux Wi-Fi.
- **Chiffré.** Les appareils communiquent avec Blokada via DNS sur TLS ou DNS sur HTTPS, donc votre fournisseur ne peut pas lire ni modifier vos requêtes.
- **Un seul tableau de bord.** Listes de blocage, domaines autorisés et bloqués, et activité par appareil, sur [app.blokada.org](https://app.blokada.org/?src=guides).

Il y a deux façons de faire la transition. Remplacez complètement le Pi-hole, ou gardez-le et utilisez Blokada Cloud comme serveur en amont.

## Option 1 : remplacer le Pi-hole

1. **Obtenez Blokada Cloud** et ouvrez le tableau de bord. Dans _Configuration_, vous trouverez vos informations :
   - Le nom DNS de votre Blokada, pour DNS sur TLS : {% dot %}
   - Votre lien DoH, pour DNS sur HTTPS : {% doh %}
2. **Pointez votre routeur vers Blokada au lieu du Pi-hole.** Suivez le [guide routeur](../router-ad-blocking/). Si votre routeur n'accepte qu'une adresse IP comme serveur DNS, configurez vos appareils un par un : [Android](../android-private-dns/), [Mac et Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) et [navigateurs](../browser-dns-over-https/).
3. **Si votre Pi-hole faisait office de serveur DHCP,** réactivez le DHCP sur votre routeur _avant_ d'éteindre le Pi. Sinon, vos appareils ne recevront plus d'adresses réseau.
4. **Transférez vos listes.** Dans le tableau de bord, choisissez les listes de blocage sous _Listes de blocage_, et ajoutez vos domaines autorisés ou bloqués sous _Exceptions_.
5. **Éteignez le Pi-hole,** ou gardez-le pour un autre usage.

<div class="note">

Votre Pi-hole affichait chaque appareil du réseau selon son adresse IP. Avec Blokada, chaque appareil apparaît sous son propre nom, tant qu'il utilise son propre nom DNS Blokada. Un routeur configuré avec un seul nom DNS Blokada apparaît comme un seul appareil.

</div>

## Option 2 : garder le Pi-hole, utiliser Blokada Cloud en amont

Si vous souhaitez garder votre configuration locale, tels que noms d'hôtes locaux, DHCP ou vos propres listes, laissez le Pi-hole transmettre ses requêtes à Blokada via une connexion chiffrée. Pi-hole ne peut pas transmettre de façon chiffrée lui-même, donc un petit agent de transmission s'exécute à côté. Ce guide utilise [dnsproxy](https://github.com/AdguardTeam/dnsproxy), un agent open source qui tient dans un seul fichier.

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
4. Dans l'admin Pi-hole, ouvrez _Paramètres → DNS_. Décochez tous les serveurs en amont et ajoutez `127.0.0.1#5054` comme serveur en amont personnalisé. Sauver.
5. Consultez la page _Activité_ du tableau de bord. Les requêtes venant de votre réseau s'afficheront désormais ici.

Vous pouvez désactiver les listes de blocage propres à Pi-hole et gérer le blocage dans le tableau de bord, ou garder les deux.

## Questions fréquentes

**Ai-je besoin de Blokada Plus ?** Non. Blokada Cloud couvre le blocage DNS pour toute votre maison. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) ajoute un VPN en plus.

**Que se passe-t-il si Blokada est inaccessible ?** Vos appareils ne pourront plus résoudre les noms jusqu'à ce que le service soit rétabli, tout comme si un Pi-hole s'arrêtait. N'ajoutez pas de deuxième serveur DNS non filtré comme secours. La plupart des appareils utilisent leurs serveurs de manière aléatoire, donc les publicités passeraient.
