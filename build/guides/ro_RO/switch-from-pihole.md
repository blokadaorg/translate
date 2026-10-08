---
title: O alternativă la Pi-hole care nu necesită hardware
description: Mută blocarea reclamelor pentru rețeaua ta de acasă de la un Pi-hole la Blokada Cloud sau păstrează Pi-hole și trimite interogările sale către Blokada.
updated: 2026-10-02
order: 1
---

Un Pi-hole blochează reclamele pentru fiecare dispozitiv de pe rețeaua ta, atât timp cât Raspberry Pi-ul funcționează, este actualizat și este acasă. Blokada Cloud face același lucru de pe serverele noastre:

- **Fără cutie de întreținut.** Fără carduri SD, fără actualizări, fără întreruperi atunci când Pi-ul se oprește.
- **Funcționează și în afara casei.** Telefoanele și laptopurile păstrează blocarea reclamelor prin date mobile și alte rețele Wi-Fi.
- **Criptat.** Dispozitivele comunică cu Blokada prin DNS peste TLS sau DNS peste HTTPS, astfel încât furnizorul tău nu poate citi sau modifica interogările.
- **Un singur panou de control.** Liste de blocare, domenii permise și blocate și activitate pe dispozitiv, la [app.blokada.org](https://app.blokada.org/?src=guides).

Există două moduri de a schimba. Înlocuiește complet Pi-hole sau păstrează-l și folosește Blokada Cloud ca upstream.

## Opțiunea 1: înlocuiește Pi-hole

1. **Obține Blokada Cloud** și deschide panoul de control. Numele tău DNS și linkul DoH sunt sub _Setup_ acolo și sub _Detaliile tale_ mai sus.
2. **Configurează routerul tău pentru Blokada în loc de Pi-hole.** Urmează [ghidul pentru router](../router-ad-blocking/). Dacă routerul tău acceptă doar o adresă IP simplă ca server DNS, configurează dispozitivele pe rând: [Android](../android-private-dns/), [Mac și Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) și [browsere](../browser-dns-over-https/).
3. **Dacă Pi-hole-ul tău era serverul DHCP,** activează din nou DHCP în router _înainte_ să oprești Pi-hole. Altfel, dispozitivele tale nu mai primesc adrese de rețea.
4. **Mută listele tale.** În panoul de control, alege listele de blocare din _Blocklists_ și adaugă domeniile permise sau blocate proprii la _Excepții_.
5. **Oprește Pi-hole,** sau păstrează-l pentru altceva.

<div class="note aside">

Pi-hole-ul tău afișa fiecare dispozitiv din rețea după adresa IP. Cu Blokada, fiecare dispozitiv apare cu numele său, atâta timp cât folosește propriul nume DNS de Blokada. Un router configurat cu un singur nume DNS Blokada va apărea ca un singur dispozitiv.

</div>

## Opțiunea 2: păstrează Pi-hole, folosește Blokada Cloud ca upstream

Dacă vrei să păstrezi configurația locală, precum numele gazdelor locale, DHCP sau listele proprii, lasă Pi-hole să trimită interogările către Blokada printr-o conexiune criptată. Pi-hole nu poate face singur forward criptat, deci un forwarder mic rulează lângă el. Acest ghid folosește [dnsproxy](https://github.com/AdguardTeam/dnsproxy), un forwarder open source care este un singur fișier.

1. Pe calculatorul cu Pi-hole, descarcă varianta `dnsproxy` potrivită procesorului tău (`linux-arm64` pentru un Raspberry Pi recent) de pe pagina de lansări și copiază binarul `dnsproxy` în `/usr/local/bin/`.
2. Creează `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Transmițător DNS criptat către Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Pornește serviciul: `sudo systemctl enable --now dnsproxy`
4. În panoul de administrare Pi-hole, deschide _Settings → DNS_. Debifează fiecare server upstream și adaugă `127.0.0.1#5054` ca server upstream personalizat. Salvează.
5. Verifică pagina _Activitate_ din panoul de control. Interogările din rețeaua ta vor apărea acolo.

Poți dezactiva listele de blocare ale Pi-hole și să gestionezi blocarea din panoul de control sau să le folosești pe ambele.

## Întrebări frecvente

**Am nevoie de Blokada Plus?** Nu. Blokada Cloud acoperă blocarea DNS pentru toată casa ta. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) adaugă un VPN peste.

**Ce se întâmplă dacă Blokada nu e disponibilă?** Dispozitivele tale nu vor putea rezolva nume până când serviciul revine, la fel ca atunci când Pi-hole-ul pică. Nu adăuga un al doilea server DNS nefiltrat ca rezervă. Majoritatea dispozitivelor folosesc toate serverele la întâmplare, astfel că reclamele ar ajunge să treacă.
