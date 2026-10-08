---
title: Mullvad DNS akan ditutup. Pertahankan pemblokiran iklan Anda dengan Blokada Cloud
description: Mullvad menutup DNS publik mereka pada 2 November 2026. Berikut cara memindahkan ponsel, komputer, dan router Anda ke Blokada Cloud sebelum tanggal tersebut, tanpa kehilangan fungsi pemblokiran iklan.
updated: 2026-10-02
order: 2},{
---

Mullvad akan menutup layanan DNS publik gratis mereka pada **2 November 2026** dan merekomendasikan Quad9 sebagai pengganti. Quad9 memblokir malware tetapi **tidak** memblokir iklan atau pelacak. Ketika DNS Mullvad berhenti, perangkat yang sudah disetel ke sana akan berhenti memuat situs web dan aplikasi. Jika perangkat diizinkan untuk menggunakan DNS lain sebagai cadangan, iklan akan muncul kembali. Beralihlah sebelum tanggal tersebut.

Halaman ini membahas nama DNS publik yang berakhiran `dns.mullvad.net`. Halaman ini tidak membahas aplikasi VPN Mullvad.

## Apa yang Anda gunakan, dan apa yang perlu dipilih di Blokada

| Nama DNS Mullvad           | Apa yang diblokirnya                  | Di dashboard Blokada                                                                                                                                                                      |
| -------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | tidak ada                             | Blokada adalah layanan penyaringan. Jika Anda tidak ingin menggunakan penyaringan, Quad9 atau DNS dari penyedia Anda adalah pilihan yang lebih sederhana. |
| `adblock.dns.mullvad.net`  | iklan, pelacak                        | daftar blokir iklan dan pelacak                                                                                                                                                           |
| `base.dns.mullvad.net`     | iklan, pelacak, malware               | tambahkan daftar malware                                                                                                                                                                  |
| `extended.dns.mullvad.net` | dasar ditambah media sosial           | tambahkan daftar media sosial                                                                                                                                                             |
| `family.dns.mullvad.net`   | dasar ditambah konten dewasa dan judi | tambahkan daftar konten dewasa dan judi                                                                                                                                                   |
| `all.dns.mullvad.net`      | semua yang di atas                    | aktifkan semuanya                                                                                                                                                                         |

Anda memilih daftar blokir di dashboard pada menu _Blocklists_. Anda dapat menggantinya kapan saja, dan perubahan akan berlaku untuk semua perangkat Anda.

## Ganti tiap perangkat

Blokada memberikan nama unik untuk setiap perangkat, sehingga dashboard dapat menampilkan aktivitas berdasarkan perangkat. Tergantung perangkatnya, Anda perlu nama DNS atau tautan DoH Anda, keduanya ada di bagian _Detail Anda_ di atas.

### Android

Panduan Mullvad menginstruksikan Anda untuk memasukkan hostname di _Private DNS_. Ganti dengan nama DNS Blokada Anda. Ikuti langkah-langkah di [panduan Android](../android-private-dns/).

### iPhone, iPad, dan Mac

Konfigurasi Mullvad memakai profil konfigurasi. Hapus terlebih dahulu:

- **iPhone dan iPad:** _Pengaturan → Umum → VPN & Manajemen Perangkat_, ketuk profil DNS Mullvad, kemudian _Hapus Profil_.
- **Mac:** buka daftar profil (_System Settings → General → Device Management_ di macOS 15 dan sesudahnya, _System Settings → Privacy & Security → Profiles_ di macOS 13 dan 14, _System Preferences → Profiles_ di macOS 12 dan sebelumnya), pilih profil DNS Mullvad dan klik _−_.

Kemudian pasang profil Blokada dari [panduan Apple](../apple-devices/).

### Browser

Jika Anda memasukkan tautan DoH Mullvad seperti `https://adblock.dns.mullvad.net/dns-query` di bagian _secure DNS_ atau _DNS over HTTPS_, ganti dengan tautan DoH Anda. [Panduan browser](../browser-dns-over-https/) menyediakan langkah-langkah untuk setiap browser.

### Router

Jika router Anda menggunakan Mullvad secara DNS over TLS, ganti hostname Mullvad dengan nama DNS Blokada Anda, dan hapus alamat IP Mullvad. [Panduan router](../router-ad-blocking/) membahas berbagai model router umum.

## Periksa apakah sudah berfungsi

Buka beberapa situs web, lalu lihat halaman _Aktivitas_ di dashboard. Anda dapat melihat permintaan dari perangkat Anda di sana, dengan permintaan yang diblokir diberi tanda. Jika perangkat tidak muncul, berarti perangkat tersebut masih menggunakan server DNS lain.
