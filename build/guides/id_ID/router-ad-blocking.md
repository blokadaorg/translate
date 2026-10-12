---
title: Blokir iklan di seluruh jaringan Anda dengan pemblokiran iklan di router
description: Atur Blokada Cloud di router Anda sekali, dan setiap perangkat di rumah akan terlindungi, termasuk TV, konsol game, dan speaker pintar yang tidak dapat menjalankan pemblokir iklan.
updated: 09-10-2026
order: 4},{
---

Setiap perangkat di jaringan Anda akan meminta router untuk menentukan server DNS yang digunakan. Arahkan router ke Blokada Cloud, dan iklan serta pelacak akan diblokir untuk semua perangkat di dalamnya. Ini mencakup smart TV, konsol game, streaming stick, dan perangkat smart home, yang tidak dapat menjalankan aplikasi pemblokir iklan.

## Kebutuhan router Anda

Ada dua cara untuk mengatur router:

- **DNS terenkripsi dengan nama host**, yaitu DNS over TLS (DoT) atau DNS over HTTPS (DoH). Banyak router terbaru yang mendukungnya, termasuk model di bawah ini. Tergantung mana yang didukung router Anda, Anda memerlukan nama DNS Anda atau tautan DoH Anda, keduanya tersedia di _Detail Anda_ di atas.
- **Alamat DNS IPv6 biasa.** Banyak router dari penyedia internet hanya menerima alamat IP standar untuk DNS. Jika router Anda seperti ini dan koneksi Anda memiliki IPv6, Blokada memberikan alamat IPv6 yang dapat Anda masukkan. Lihat [Router yang hanya menerima alamat IP](#routers-that-only-take-an-ip-address).

Gunakan DNS terenkripsi jika router Anda mendukungnya. Pencarian tetap pribadi saat menuju ke Blokada.

## FRITZ!Box

FRITZ!OS 7.20 atau versi yang lebih baru.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. Pada _Nama yang Diselesaikan dari Server DNS_, masukkan hanya {% dot %}. **Hapus semua entri lainnya.** FRITZ!Box menggunakan semua resolver yang terdaftar, dan resolver lain dapat membiarkan iklan lewat.
4. Untick _Allow fallback to unencrypted name resolution_.
5. Jika Anda melihat _Failover to public DNS servers when DNS disrupted_, matikan fitur tersebut.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Alamat: {% ip "dot" %}
   - Nama Host TLS: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Buka _Services → HTTPS DNS Proxy_. Hapus instance milik penyedia lain.
3. Tambahkan sebuah instance dengan URL resolver khusus: {% doh %}
4. _Simpan & Terapkan_. Paket secara otomatis mengarahkan dnsmasq ke alamat tersebut.

## Router lainnya

Cari pengaturan bernama _DNS over TLS_, _DNS Pribadi_, _DNS Terenkripsi_, atau _DNS over HTTPS_. Masukkan nama DNS Blokada atau tautan DoH Anda dari atas, dan hapus semua server DNS lainnya, termasuk server cadangan. Jika tidak ada pengaturan seperti itu, gunakan alamat IPv6 biasa seperti di bawah ini.

## Router yang hanya menerima alamat IP

Router Anda dan koneksi internet Anda memerlukan IPv6 untuk ini. Dukungan untuk alamat IPv4 biasa akan tersedia nanti.

1. Di [dasbor](https://app.blokada.org/setup?src=guides), buka _Setup_ dan pilih _Router, TV, konsol game_.
2. Beri nama router, misalnya _Router Rumah_, lalu pilih _Dapatkan alamat_. Nama ini akan muncul di aktivitas Anda dan tidak dapat diubah nanti.
3. Di pengaturan router, cari server DNS untuk IPv6, biasanya di bawah _Internet_, _WAN_ atau _IPv6_, dan masukkan alamat tersebut sebagai satu-satunya server DNS.
4. **Hapus semua server DNS lainnya, termasuk yang IPv4.** Perangkat yang masih menerima server DNS IPv4 dari router akan mengirim beberapa permintaan lewat Blokada. Jika router tidak bisa membiarkan DNS IPv4 kosong, atur perangkat Anda satu per satu: [Android](../android-private-dns/), [Mac dan Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), dan [peramban](../browser-dns-over-https/).

Pengaturan yang sama berlaku untuk TV atau konsol game yang memungkinkan Anda memasukkan server DNS secara manual. Berikan setiap perangkat alamatnya sendiri, sehingga akan muncul dengan nama pada aktivitas Anda.

<div class="note aside">

Permintaan ini dikirim tanpa enkripsi ke Blokada, seperti server DNS biasa. Jika router Anda mendukung DNS over TLS atau DNS over HTTPS, gunakan itu sebagai gantinya.

</div>

## Periksa apakah berhasil

1. Mulai ulang satu perangkat, atau matikan lalu nyalakan kembali Wi-Fi perangkat tersebut, agar perubahan diterapkan.
2. Pada perangkat tersebut, matikan Blokada jika sedang berjalan, lalu buka [go.blokada.org/test](https://go.blokada.org/test). Halaman tersebut akan menunjukkan apakah DNS Anda melewati Blokada.
3. Jelajahi internet selama satu menit, lalu buka halaman _Aktivitas_ di [dasbor](https://app.blokada.org/stats?src=guides). Permintaan jaringan Anda akan muncul di sana.

## Jika beberapa perangkat masih menampilkan iklan

Beberapa perangkat melewati router: ponsel dengan _Private DNS_ aktif, browser dengan _secure DNS_ yang diatur ke penyedia lain, dan perangkat yang menggunakan DNS sendiri. Atur perangkat tersebut secara langsung, atau matikan pengaturan DNS mereka.

<div class="note tip">

Di balik router, semua perangkat berbagi satu alamat, sehingga dasbor akan menampilkan jaringan Anda sebagai satu perangkat. Atur ponsel dan laptop dengan nama DNS Blokada masing-masing jika Anda ingin melihatnya secara terpisah. Mereka juga akan tetap terlindungi saat berada di luar rumah.

</div>
