---
title: Atur DNS Pribadi di Android dengan Blokada Cloud
description: Gunakan pengaturan DNS Pribadi bawaan Android dengan Blokada Cloud untuk memblokir iklan dan pelacak di setiap aplikasi, baik di Wi-Fi maupun data seluler. Atau biarkan aplikasi Blokada 6 yang melakukannya.
updated: 2026-10-02
order: 5
---

## Cara termudah: aplikasi

[Blokada 6](https://go.blokada.org/play_cloud) mengatur semuanya untuk Anda, mengaktifkan dan menonaktifkan pemblokiran dengan satu ketukan, dan menampilkan apa saja yang diblokir langsung di ponsel. Masuk dengan ID akun Anda dan selesai.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Dapatkan Blokada 6 di Google Play</a></p>

## Tanpa aplikasi: DNS Pribadi

Android 9 dan setelahnya memiliki pengaturan _DNS Pribadi_. Atur ke Blokada Cloud, maka iklan dan pelacak diblokir di semua aplikasi, di setiap jaringan, tanpa ada aplikasi berjalan di latar belakang.

1. Buka _Pengaturan → Jaringan & internet_. Di beberapa ponsel ini adalah _Koneksi_ atau _Koneksi & berbagi_.
2. Ketuk _DNS Pribadi_. Pada ponsel Samsung, ini berada di bawah _Pengaturan koneksi lainnya_.
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

Jika Anda tidak dapat menemukannya, cari "DNS Pribadi" di aplikasi Pengaturan.

## Periksa apakah sudah berfungsi

Buka beberapa aplikasi atau situs web, kemudian lihat halaman _Aktivitas_ di [dasbor](https://app.blokada.org/stats?src=guides). Permintaan dari ponsel ini akan muncul di sana.

## Jika ada yang tidak berfungsi

- **"Tidak dapat terhubung" atau tidak ada internet:** periksa nama DNS Blokada Anda, pastikan tidak ada kesalahan ketik. Harus persis seperti yang ditunjukkan di atas, tanpa `https://`.
- **Aplikasi VPN lain aktif:** beberapa aplikasi VPN menggunakan DNS mereka sendiri dan melewati DNS Pribadi. Nonaktifkan pengaturan DNS atau pemblokiran iklan pada VPN tersebut, atau gunakan Blokada 6 sebagai gantinya.
- **Chrome masih menampilkan iklan:** Chrome mungkin disetel ke penyedia DNS aman sendiri, yang melewati DNS Pribadi. Di Chrome, buka _Pengaturan → Privasi dan keamanan → Gunakan DNS aman_ dan pilih _Gunakan penyedia layanan Anda saat ini_. Chrome kemudian akan mengikuti DNS Pribadi.
