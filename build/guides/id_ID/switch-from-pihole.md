---
title: Alternatif Pi-hole yang tidak memerlukan perangkat keras
description: Pindahkan pemblokiran iklan di rumah Anda dari Pi-hole ke Blokada Cloud, atau pertahankan Pi-hole Anda dan kirimkan permintaannya melalui Blokada.
updated: 2026-10-02
order: 1
---

Pi-hole memblokir iklan untuk setiap perangkat di jaringan Anda, selama Raspberry Pi berjalan, diperbarui, dan berada di rumah. Blokada Cloud melakukan hal yang sama langsung dari server kami:

- **Tidak ada perangkat yang harus dirawat.** Tidak ada kartu SD, tidak ada pembaruan, tidak ada mati layanan saat perangkat Pi Anda mati.
- **Bisa digunakan di luar rumah.** Ponsel dan laptop tetap terblokir iklan meskipun menggunakan data seluler atau jaringan Wi-Fi lain.
- **Terenkripsi.** Perangkat berbicara dengan Blokada melalui DNS over TLS atau DNS over HTTPS, sehingga penyedia Anda tidak dapat membaca atau mengubah permintaan DNS Anda.
- **Satu dashboard.** Daftar blokir, domain yang diizinkan dan diblokir, serta aktivitas per perangkat dapat dikelola di [app.blokada.org](https://app.blokada.org/?src=guides).

Ada dua cara untuk beralih. Ganti Pi-hole sepenuhnya, atau tetap gunakan Pi-hole dan gunakan Blokada Cloud sebagai upstream-nya.

## Opsi 1: ganti Pi-hole

1. **Dapatkan Blokada Cloud** dan buka dashboard-nya. Nama DNS Anda dan tautan DoH tersedia di bagian _Setup_ di sana, serta di bawah _Your details_ di atas.
2. **Arahkan router Anda ke Blokada, bukan ke Pi-hole.** Ikuti [panduan router](../router-ad-blocking/). Jika router Anda hanya menerima alamat IP sebagai server DNS, atur masing-masing perangkat secara manual: [Android](../android-private-dns/), [Mac dan Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), dan [browser](../browser-dns-over-https/).
3. **Jika Pi-hole Anda berperan sebagai server DHCP,** aktifkan kembali DHCP di router _sebelum_ Anda mematikan Pi. Jika tidak, perangkat tidak akan mendapatkan alamat jaringan.
4. **Pindahkan daftar Anda.** Di dashboard, pilih daftar blokir di bawah _Blocklists_, dan tambahkan domain yang Anda izinkan atau blokir sendiri di bawah _Exceptions_.
5. **Matikan Pi-hole,** atau tetap gunakan untuk keperluan lain.

<div class="note aside">

Pi-hole Anda menampilkan setiap perangkat di jaringan berdasarkan alamat IP mereka. Dengan Blokada, setiap perangkat akan terlihat dengan namanya sendiri, selama menggunakan nama DNS Blokada masing-masing. Router yang diatur dengan satu nama DNS Blokada akan tampil sebagai satu perangkat.

</div>

## Opsi 2: tetap gunakan Pi-hole, gunakan Blokada Cloud sebagai upstream

Jika Anda ingin mempertahankan konfigurasi lokal seperti nama host lokal, DHCP, atau daftar Anda sendiri, biarkan Pi-hole meneruskan permintaannya ke Blokada melalui koneksi terenkripsi. Pi-hole tidak bisa meneruskan secara terenkripsi sendiri, jadi perlu aplikasi kecil yang berjalan di sampingnya. Panduan ini menggunakan [dnsproxy](https://github.com/AdguardTeam/dnsproxy), penerus terbuka yang hanya berupa satu berkas.

1. Di mesin Pi-hole, unduh rilis `dnsproxy` untuk CPU Anda (`linux-arm64` untuk Raspberry Pi terbaru) dari halaman rilisnya, lalu salin berkas biner `dnsproxy` ke `/usr/local/bin/`.
2. Buat `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Penerus DNS terenkripsi ke Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Mulai: `sudo systemctl enable --now dnsproxy`
4. Di admin Pi-hole, buka _Settings → DNS_. Hilangkan centang pada setiap server upstream dan tambahkan `127.0.0.1#5054` sebagai server upstream kustom. Simpan.
5. Cek halaman _Activity_ di dashboard. Permintaan dari jaringan Anda sekarang akan tampil di sana.

Anda bisa mematikan daftar blokir milik Pi-hole dan mengelola blokir di dashboard, atau tetap menggunakan keduanya.

## Pertanyaan yang sering ditanyakan

**Apakah saya perlu Blokada Plus?** Tidak. Blokada Cloud sudah mencakup pemblokiran DNS untuk seluruh rumah Anda. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) menambahkan VPN di atasnya.

**Bagaimana jika Blokada tidak dapat dijangkau?** Perangkat Anda tidak bisa melakukan resolusi nama hingga layanan kembali tersedia, sama seperti Pi-hole yang mati. Jangan tambahkan server DNS kedua yang tidak disaring sebagai cadangan. Sebagian besar perangkat menggunakan semua server yang ada secara acak, sehingga iklan bisa lolos.
