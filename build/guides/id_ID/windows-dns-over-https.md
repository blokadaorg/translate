---
title: Blokir iklan di Windows dengan DNS over HTTPS
description: Gunakan DNS terenkripsi bawaan Windows 11 dengan Blokada Cloud untuk memblokir iklan dan pelacak di setiap aplikasi dan peramban, tanpa perlu menginstal perangkat lunak tambahan.
updated: 2026-10-02
order: 8
---

Windows 11 dapat mengenkripsi seluruh permintaan DNS-nya menggunakan DNS over HTTPS. Mengarahkan ke Blokada Cloud, iklan dan pelacak akan diblokir di setiap aplikasi dan peramban pada komputer, tanpa perlu menginstal apa pun.

Anda memerlukan alamat IP server DNS dan tautan DoH Anda, keduanya ada di bawah _Detail Anda_ di atas.

## Windows 11

1. Buka _Pengaturan → Jaringan & internet_, lalu _Wi-Fi_ atau _Ethernet_, tergantung bagaimana komputer terhubung.
2. Buka _Properti perangkat keras_ koneksi Anda. Untuk Wi-Fi, pilih _Kelola jaringan yang dikenal_ lalu jaringan tersebut, atau _Properti perangkat keras_ di bagian atas halaman Wi-Fi.
3. Di samping _Penetapan server DNS_, pilih _Edit_. Pilih _Manual_ dan aktifkan _IPv4_.
4. Pada _DNS utama_, masukkan server DNS {% ip "doh" %}
5. Atur _DNS over HTTPS_ ke _Aktif (template manual)_, lalu tempel tautan DoH Anda {% doh %} sebagai _template DoH_.
6. Nonaktifkan _Fallback ke plaintext_, lalu pilih _Simpan_.

Jika komputer menggunakan baik Wi-Fi maupun Ethernet, ulangi langkah ini untuk sambungan lainnya.

<div class="note important">

Biarkan _DNS alternatif_ kosong. Windows menggunakan kedua server, dan server lain akan membiarkan iklan lewat.

</div>

<div class="note tip">

Tidak ada opsi _Aktif (template manual)_? Windows 11 Anda masih versi lama. Perbarui Windows, atau gunakan [panduan peramban](../browser-dns-over-https/) sementara.

</div>

## Windows 10

Windows 10 tidak memiliki DNS terenkripsi bawaan. Atur DNS aman di peramban Anda sebagai gantinya, seperti pada [panduan peramban](../browser-dns-over-https/), atau atur [router](../router-ad-blocking/) Anda untuk melindungi seluruh rumah.

## Periksa apakah sudah berfungsi

Buka beberapa situs web, lalu lihat halaman _Aktivitas_ di [dasbor](https://app.blokada.org/stats?src=guides). Permintaan dari komputer ini akan muncul di sana.

<div class="note aside">

Ingin VPN di komputer ini juga? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) mencakup pengaturan WireGuard yang mengenkripsi seluruh lalu lintas, dengan pemblokiran yang sama.

</div>

## Jika ada yang tidak berfungsi

Chrome dan Edge memiliki pengaturan _DNS aman_ sendiri, yang melewati Windows. Jika dibiarkan otomatis, ini dapat kembali ke DNS biasa, yang ditolak oleh Blokada. Atur ke tautan DoH Anda sebagai gantinya:

- **Chrome:** buka `chrome://settings/security`, aktifkan _Gunakan DNS aman_, dan di bawah _Pilih penyedia DNS_ pilih _Tambahkan penyedia layanan DNS kustom_.
- **Edge:** buka `edge://settings/privacy`, aktifkan DNS aman, dan pilih _Pilih penyedia layanan_.

Kemudian tempel tautan DoH Anda {% doh %}

Jika beberapa iklan masih lolos di jaringan yang menggunakan IPv6, Windows mungkin juga meminta server DNS IPv6 dari router Anda. Nonaktifkan _Internet Protocol Version 6 (TCP/IPv6)_ di properti adapter (_Panel Kontrol → Jaringan dan Koneksi_), atau atur [router](../router-ad-blocking/) Anda.
