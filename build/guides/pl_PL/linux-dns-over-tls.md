---
title: Blokuj reklamy na Linuksie za pomocą DNS przez TLS
description: Skonfiguruj systemd-resolved, aby korzystał z Blokada Cloud przez szyfrowany DNS przez TLS i blokuj reklamy oraz trackery dla każdej aplikacji na Twoim komputerze z Linuksem.
updated: 2026-10-02
order: 9
---

Większość obecnych dystrybucji Linuksa, w tym Ubuntu i Fedora, rozwiązuje nazwy za pomocą _systemd-resolved_, który obsługuje DNS przez TLS. Na Debianie zainstaluj go najpierw poleceniem `sudo apt install systemd-resolved`. Ustaw jako serwer DNS Blokada Cloud, a reklamy i trackery zostaną zablokowane dla każdej aplikacji na komputerze.

## Skonfiguruj systemd-resolved

1. Utwórz folder poleceniem `sudo mkdir -p /etc/systemd/resolved.conf.d`, a następnie plik `/etc/systemd/resolved.conf.d/blokada.conf` z następującymi ustawieniami:

<pre><code>[Resolve]\nDNS={{ site.dnsIps.dot }}#<span data-dns=\"dot\">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>\nDNSOverTLS=yes\nDomains=~.</code></pre>

<ol start="2">
<li>Uruchom ponownie: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Sprawdź: <code>resolvectl status</code> wyświetla <code>+DNSOverTLS</code> oraz serwer Blokada.</li>
</ol>

Część po `#` to Twoja nazwa DNS Blokada: {% dot %} systemd-resolved sprawdza z nią certyfikat serwera, a Blokada używa jej do rozpoznania, które urządzenie pyta.

<div class="note important">

**NetworkManager** również przekazuje serwery DNS Twojej sieci. `Domains=~.` przekierowuje wszystkie zapytania do Blokada, ale jeśli `resolvectl status` nadal pokazuje inny serwer na połączeniu, wyłącz automatyczny DNS dla tego połączenia (przełącznik _Automatyczny_ obok _DNS_ w ustawieniach IPv4 i IPv6).

</div>

## Bez systemd-resolved

Jeśli `resolvectl` nie został znaleziony, dystrybucja rozwiązuje nazwy w inny sposób. Skonfiguruj bezpieczny DNS w swojej przeglądarce, według [poradnika do przeglądarki](../browser-dns-over-https/), lub skonfiguruj swój [router](../router-ad-blocking/), aby zabezpieczyć całe gospodarstwo domowe.

## Sprawdź, czy działa

Otwórz kilka stron internetowych, a następnie przejdź do strony _Aktywność_ w [panelu](https://app.blokada.org/stats?src=guides). Zapytania tego komputera pojawią się tam.

<div class="note aside">

Chcesz używać VPN także na tym komputerze? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) zawiera konfigurację WireGuard, która szyfruje cały ruch, z tym samym blokowaniem.

</div>
