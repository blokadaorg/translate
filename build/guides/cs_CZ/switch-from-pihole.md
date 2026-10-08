---
title: Alternativa k Pi-hole, která nevyžaduje žádný hardware
description: Přesuňte blokování reklam ve vašem domově z Pi-hole do Blokada Cloud, nebo ponechte Pi-hole a přesměrujte jeho dotazy přes Blokada.
updated: 2026-10-02
order: 1
---

Pi-hole blokuje reklamy pro všechna zařízení ve vaší síti, pokud je Raspberry Pi zapnutý, aktualizovaný a doma. Blokada Cloud dělá totéž z našich serverů:

- **Žádná krabička na údržbu.** Žádné SD karty, žádné aktualizace, žádné výpadky, když Pi přestane fungovat.
- **Funguje i mimo domov.** Telefony a notebooky zůstávají blokovány i na mobilních datech a jiných Wi-Fi sítích.
- **Šifrováno.** Zařízení komunikují s Blokada přes DNS over TLS nebo DNS over HTTPS, takže váš poskytovatel nemůže číst ani měnit vaše dotazy.
- **Jedna hlavní stránka.** Blokovací seznamy, povolené a blokované domény a aktivita podle zařízení – vše na [app.blokada.org](https://app.blokada.org/?src=guides).

Existují dva způsoby, jak přejít. Buď úplně nahradíte Pi-hole, nebo jej ponecháte a použijete Blokada Cloud jako jeho upstream.

## Možnost 1: nahraďte Pi-hole

1. **Pořiďte si Blokada Cloud** a otevřete hlavní stránku. Vaše DNS jméno a DoH odkaz najdete v části _Nastavení_ a výše pod _Vaše údaje_.
2. **Nasměrujte váš router na Blokada namísto Pi-hole.** Postupujte podle [průvodce routerem](../router-ad-blocking/). Pokud váš router akceptuje jako DNS server pouze čistou IP adresu, nastavte si zařízení po jednom: [Android](../android-private-dns/), [Mac a Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) a [prohlížeče](../browser-dns-over-https/).
3. **Pokud byl Pi-hole také DHCP serverem,** zapněte DHCP zpět v routeru _předtím_, než Pi-hole vypnete. Jinak vaše zařízení přestanou získávat síťové adresy.
4. **Přesuňte své seznamy.** V hlavní stránce zvolte blokovací seznamy pod _Blocklists_ a přidejte vlastní povolené nebo blokované domény pod _Výjimky_.
5. **Vypněte Pi-hole,** nebo jej použijte na něco jiného.

<div class="note aside">

Pi-hole zobrazoval každé zařízení v síti podle jeho IP adresy. V Blokada se každé zařízení zobrazuje svým vlastním jménem, pokud používá svůj vlastní Blokada DNS název. Router nastavený s jedním Blokada DNS jménem se zobrazí jako jedno zařízení.

</div>

## Možnost 2: ponechte Pi-hole, používejte Blokada Cloud jako upstream

Pokud chcete ponechat místní nastavení, jako jsou lokální názvy počítačů, DHCP nebo vlastní seznamy, nechte Pi-hole přeposílat dotazy do Blokada přes šifrované spojení. Pi-hole neumí šifrovaný forwarding přímo, proto u něj běží malý přeposílač. Tento návod používá [dnsproxy](https://github.com/AdguardTeam/dnsproxy), open source forwarder v jednom souboru.

1. Na zařízení s Pi-hole stáhněte vydání `dnsproxy` pro váš CPU (`linux-arm64` pro novější Raspberry Pi) ze stránky vydání a zkopírujte binárku `dnsproxy` do /usr/local/bin/.
2. Vytvořte `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Šifrovaný DNS forwarder do Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Spusťte: `sudo systemctl enable --now dnsproxy`
4. V administraci Pi-hole otevřete _Nastavení → DNS_. Odškrtněte všechny upstream servery a přidejte `127.0.0.1#5054` jako vlastní upstream server. Uložte.
5. Zkontrolujte stránku _Aktivita_ v hlavní stránce. Dotazy z vaší sítě se tam nyní zobrazují.

Můžete vypnout vlastní blokovací seznamy Pi-hole a spravovat blokování v hlavní stránce, nebo ponechat obojí.

## Často kladené dotazy

**Potřebuji Blokada Plus?** Ne. Blokada Cloud pokrývá DNS blokování pro celý váš domov. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) přidává VPN navíc.

**Co když Blokada není dostupná?** Vaše zařízení nebudou moci překládat jména, dokud nebude Blokada opět dostupná, stejně jako když Pi-hole vypadne. Nepřidávejte druhý, nefiltrovaný DNS server jako zálohu. Většina zařízení používá všechny své servery náhodně, takže by reklamy prošly.
