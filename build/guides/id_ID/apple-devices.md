---
title: Blokir iklan di Mac dan Apple TV dengan profil DNS Blokada
description: Pasang profil DNS Blokada Cloud untuk memblokir iklan dan pelacak secara menyeluruh di Mac atau Apple TV, dengan DNS terenkripsi dan tanpa ada yang berjalan di latar belakang.
updated: 2026-10-02
order: 6
---

Perangkat Apple dapat menggunakan DNS terenkripsi untuk seluruh sistem melalui profil konfigurasi. Profil Blokada mengarahkan perangkat ke Blokada Cloud, yang memblokir iklan dan pelacak di setiap aplikasi dan browser.

Berfungsi di macOS 11 (Big Sur), tvOS 14, iOS dan iPadOS 14 ke atas.

<div class="if-no-device">

Halaman ini belum mengetahui perangkat Anda, jadi belum dapat menawarkan profil Anda. Masuk ke dasbor, buka _Setup_, pilih perangkat Anda, dan buka panduan ini dengan _Buka di perangkat lain_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Dapatkan tautan profil saya</a></p>

</div>

## iPhone dan iPad

Cara termudah adalah dengan aplikasi. [Blokada 6](https://go.blokada.org/appstore) akan mengatur semuanya untuk Anda, menyalakan dan mematikan pemblokiran dengan sekali ketuk, dan menampilkan apa saja yang diblokir langsung di ponsel. Masuk dengan ID akun Anda dan selesai.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Dapatkan Blokada 6 di App Store</a></p>

### Tanpa aplikasi

Sebagai gantinya, Anda dapat memasang profil. iPhone dan iPad hanya dapat menginstal profil dari **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Halaman ini dibuka di browser lain. Salin tautan Anda dan buka di Safari untuk melanjutkan: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Buka _Pengaturan_. Ketuk _Profil Terunduh_ di dekat bagian atas. Anda juga dapat menemukannya di bawah _Umum → VPN & Manajemen Perangkat_.
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}Unduh profil saya{% endappleProfile %}</p>

## Mac

1. Klik tombol di bawah ini untuk mengunduh profil.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Unduh profil saya{% endappleProfile %}</p>

## Apple TV

Apple TV tidak dapat membuka halaman web, jadi Anda harus mengetikkan tautan profil Anda secara manual.

1. Tautan profil Anda: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. Sorot _Bagikan Analitik Apple TV_. Jangan pilih. Tekan tombol Play/Pause pada remote.
4. Pilih _Tambahkan Profil_ dan masukkan tautan profil Anda. Mengetik lebih mudah dengan prompt keyboard di iPhone Anda, di mana Anda dapat menempelkan tautan tersebut. Instal profil dan konfirmasi.

<div class="note aside">

**Apple TV dan perangkat lain di rumah:** jika Anda mengatur Blokada Cloud di [router](../router-ad-blocking/) Anda, Apple TV juga akan terlindungi bersama semua perangkat lainnya.

</div>

## Cek apakah sudah berfungsi

Jelajahi sebentar, lalu buka halaman _Aktivitas_ di [dasbor](https://app.blokada.org/stats?src=guides). Permintaan pencarian dari perangkat ini akan tampil di sana.

Untuk menghapus Blokada nanti, hapus profil di tempat Anda menginstalnya.
