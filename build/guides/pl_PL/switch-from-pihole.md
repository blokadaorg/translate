---
title: Alternatywa dla Pi-hole, która nie wymaga sprzętu.
description: Przenieś blokowanie reklam w swoim domu z Pi-hole do Blokada Cloud lub zachowaj Pi-hole i przesyłaj zapytania przez Blokada.
updated: 2026-10-02
order: 1
---

Pi-hole blokuje reklamy dla każdego urządzenia w Twojej sieci, pod warunkiem że Raspberry Pi jest włączony, zaktualizowany i znajduje się w domu. Blokada Cloud wykonuje tę samą pracę z naszych serwerów:

- **Brak urządzenia do obsługi.** Brak kart SD, brak aktualizacji, brak przerw w działaniu, gdy Pi się wyłączy.
- **Działa poza domem.** Telefony i laptopy zachowują blokowanie na danych mobilnych i innych sieciach Wi-Fi.
- **Szyfrowane.** Urządzenia komunikują się z Blokada za pomocą DNS over TLS lub DNS over HTTPS, więc Twój dostawca nie może czytać ani zmieniać Twoich zapytań.
- **Jedno miejsce zarządzania.** Listy blokujące, dozwolone i blokowane domeny oraz aktywność według urządzenia na [app.blokada.org](https://app.blokada.org/?src=guides).

Są dwa sposoby przełączenia się. Całkowicie zastąp Pi-hole lub zachowaj go i użyj Blokada Cloud jako jego serwera nadrzędnego.

## Opcja 1: zamień Pi-hole

1. **Uzyskaj Blokada Cloud** i otwórz panel zarządzania. Twoja nazwa DNS oraz link DoH znajdują się w sekcji _Konfiguracja_, a także powyżej w _Twoje szczegóły_.
2. **Skieruj swój router na Blokada zamiast na Pi-hole.** Skorzystaj z [instrukcji routera](../router-ad-blocking/). Jeśli Twój router akceptuje tylko zwykły adres IP jako serwer DNS, skonfiguruj swoje urządzenia pojedynczo: [Android](../android-private-dns/), [Mac i Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) oraz [przeglądarki](../browser-dns-over-https/).
3. **Jeśli Twój Pi-hole pełnił funkcję serwera DHCP,** włącz DHCP ponownie w routerze _przed_ wyłączeniem Pi. W przeciwnym razie Twoje urządzenia przestaną otrzymywać adresy sieciowe.
4. **Przenieś swoje listy.** W panelu zarządzania wybierz listy blokujące w sekcji _Blocklists_ i dodaj własne dozwolone lub blokowane domeny w sekcji _Exceptions_.
5. **Wyłącz Pi-hole,** lub zachowaj go do innych celów.

<div class="note aside">

Twój Pi-hole pokazywał każde urządzenie w sieci po jego adresie IP. W Blokada każde urządzenie pojawia się pod własną nazwą, o ile korzysta ze swojej własnej nazwy DNS w Blokada. Router skonfigurowany z jedną nazwą DNS Blokada pojawi się jako jedno urządzenie.

</div>

## Opcja 2: zachowaj Pi-hole, korzystaj z Blokada Cloud jako serwera nadrzędnego

Jeśli chcesz zachować swoją lokalną konfigurację, taką jak lokalne nazwy hostów, DHCP lub własne listy, pozwól, aby Pi-hole przekazywał zapytania do Blokada przez zaszyfrowane połączenie. Pi-hole nie obsługuje samodzielnie szyfrowanego przekazywania, więc obok niego działa mały forwarder. Ten poradnik używa [dnsproxy](https://github.com/AdguardTeam/dnsproxy), otwartoźródłowego forwardera w postaci pojedynczego pliku.

1. Na urządzeniu z Pi-hole pobierz wydanie `dnsproxy` odpowiednie dla swojego procesora (`linux-arm64` dla nowszego Raspberry Pi) ze strony z wydaniami i skopiuj plik wykonywalny `dnsproxy` do `/usr/local/bin/`.
2. Utwórz plik `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Zaszyfrowany przekierowujący DNS do Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Uruchom: `sudo systemctl enable --now dnsproxy`
4. W panelu administratora Pi-hole otwórz _Ustawienia → DNS_. Odznacz wszystkich serwerów nadrzędnych i dodaj `127.0.0.1#5054` jako własny serwer nadrzędny. Zapisz.
5. Sprawdź stronę _Aktywność_ w panelu zarządzania. Zapytania z Twojej sieci pojawią się teraz tam.

Możesz wyłączyć własne listy blokujące Pi-hole i zarządzać blokowaniem w panelu, lub używać obu jednocześnie.

## Najczęściej zadawane pytania

**Czy potrzebuję Blokada Plus?** Nie. Blokada Cloud zapewnia blokowanie DNS dla całego domu. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) dodaje VPN do tej ochrony.

**Co jeśli Blokada jest niedostępna?** Twoje urządzenia nie będą mogły rozwiązywać nazw dopóki usługa nie wróci, tak samo jak gdy Pi-hole przestanie działać. Nie dodawaj drugiego, niefiltrowanego serwera DNS jako zapasowego. Większość urządzeń wykorzystuje wszystkie swoje serwery losowo, więc reklamy mogłyby się przedostać.
