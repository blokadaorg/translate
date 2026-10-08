---
title: Blokir iklan di seluruh jaringan Anda dengan pemblokiran iklan di router
description: Atur Blokada Cloud di router Anda sekali, dan setiap perangkat di rumah akan terlindungi, termasuk TV, konsol game, dan speaker pintar yang tidak dapat menjalankan pemblokir iklan.
updated: 2026-10-02
order: 4},{
---

Setiap perangkat di jaringan Anda akan meminta router untuk menentukan server DNS yang digunakan. Arahkan router ke Blokada Cloud, dan iklan serta pelacak akan diblokir untuk semua perangkat di dalamnya. Ini mencakup smart TV, konsol game, streaming stick, dan perangkat smart home, yang tidak dapat menjalankan aplikasi pemblokir iklan.

## Kebutuhan router Anda

Router Anda harus mendukung **DNS terenkripsi dengan nama host**, yaitu DNS over TLS (DoT) atau DNS over HTTPS (DoH). Banyak router terbaru yang sudah mendukungnya, termasuk model-model di bawah ini. Bergantung pada dukungan router Anda, Anda memerlukan nama DNS atau tautan DoH, keduanya berada di _Detail Anda_ di atas.

<div class="note important">

**Hanya alamat IP polos?** Banyak router dari penyedia internet hanya menerima alamat IP polos untuk DNS. Dukungan untuk hal ini masih dalam pengembangan. Sampai saat itu, atur perangkat Anda satu per satu: [Android](../android-private-dns/), [Mac dan Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/), dan [browser](../browser-dns-over-https/). Anda juga dapat menjalankan penerus kecil di Raspberry Pi, seperti dijelaskan di [panduan Pi-hole](../switch-from-pihole/).

</div>

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

Cari pengaturan bernama _DNS over TLS_, _Private DNS_, _Encrypted DNS_, atau _DNS over HTTPS_. Masukkan nama DNS Blokada atau tautan DoH Anda dari atas, dan hapus semua server DNS lain, termasuk server cadangan.

## Periksa apakah berhasil

1. Mulai ulang satu perangkat, atau matikan lalu nyalakan kembali Wi-Fi perangkat tersebut, agar perubahan diterapkan.
2. Jelajahi selama satu menit, lalu buka halaman _Aktivitas_ di dasbor. Permintaan jaringan Anda akan muncul di sana.

## Jika beberapa perangkat masih menampilkan iklan

Beberapa perangkat melewati router: ponsel dengan _Private DNS_ aktif, browser dengan _secure DNS_ yang diatur ke penyedia lain, dan perangkat yang menggunakan DNS sendiri. Atur perangkat tersebut secara langsung, atau matikan pengaturan DNS mereka.

<div class="note tip">

Di balik router, semua perangkat berbagi satu alamat, sehingga dasbor akan menampilkan jaringan Anda sebagai satu perangkat. Atur ponsel dan laptop dengan nama DNS Blokada masing-masing jika Anda ingin melihatnya secara terpisah. Mereka juga akan tetap terlindungi saat berada di luar rumah.

</div>
