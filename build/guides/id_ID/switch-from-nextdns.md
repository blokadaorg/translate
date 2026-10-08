---
title: Alternatif NextDNS dengan pengaturan yang sama di setiap perangkat
description: Pindah dari NextDNS ke Blokada Cloud. Tukar nama DNS, tautan DoH, atau profil NextDNS Anda dengan milik Blokada di ponsel, komputer, dan router Anda, lalu pertahankan pemblokiran iklan Anda.
updated: 2026-10-02
order: 3
---

NextDNS dan Blokada Cloud bekerja dengan cara yang sama: layanan DNS terenkripsi yang memblokir iklan dan pelacak berdasarkan nama, dengan pengaturan Anda sendiri di balik nama DNS pribadi. Berpindah berarti mengganti nilai NextDNS di setiap perangkat dengan milik Blokada Anda. Tidak ada pengaturan lain di perangkat yang berubah.

## Apa yang Anda gunakan, dan apa yang dipilih di Blokada

| Di NextDNS                                         | Di Blokada Cloud                                                     |
| -------------------------------------------------- | -------------------------------------------------------------------- |
| ID konfigurasi Anda, mis. `abc123` | Tag perangkat Anda, bagian dari nama DNS Blokada dan tautan DoH Anda |
| _Daftar cekal_ privasi                             | _Daftar cekal_ di dashboard                                          |
| _Keamanan_ (malware, phishing)  | daftar malware di bawah _Daftar cekal_                               |
| _Pengawasan orang tua_                             | daftar konten dewasa dan perjudian di bawah _Daftar cekal_           |
| _Allowlist_ dan _Denylist_                         | _Pengecualian_ di dashboard                                          |
| _Log_ dan _Analitik_                               | _Aktivitas_ dan _Statistik_ di dashboard                             |

## Pindahkan setiap perangkat

Tergantung perangkatnya, Anda memerlukan nama DNS atau tautan DoH Anda, keduanya ada di bawah _Rincian Anda_ di atas.

### Android

Jika Anda menggunakan _DNS Pribadi_ dengan `<your-id>.dns.nextdns.io`, ganti dengan nama DNS Blokada Anda, seperti di [panduan Android](../android-private-dns/). Jika Anda menggunakan aplikasi NextDNS, copot dan instal [Blokada 6](https://go.blokada.org/play_cloud) sebagai gantinya.

### iPhone dan iPad

Jika Anda menggunakan aplikasi NextDNS, copot dan instal [Blokada 6](https://go.blokada.org/appstore). Jika Anda memasang profil NextDNS, hapus di _Pengaturan → Umum → VPN & Manajemen Perangkat_, lalu ikuti [panduan Apple](../apple-devices/).

### Mac dan Apple TV

Hapus profil atau aplikasi NextDNS, lalu instal profil Blokada dari [panduan Apple](../apple-devices/).

### Windows dan Linux

Copot aplikasi NextDNS jika Anda menggunakannya. Di Windows, ganti server NextDNS dan template DoH dengan milik Blokada, seperti di [panduan Windows](../windows-dns-over-https/). Di Linux, ganti server NextDNS di systemd-resolved, seperti di [panduan Linux](../linux-dns-over-tls/).

### Peramban

Jika Anda mengatur `https://dns.nextdns.io/…` sebagai _DNS aman_ peramban Anda, ganti dengan tautan DoH Anda, seperti di [panduan peramban](../browser-dns-over-https/).

### Router

Jika router Anda menggunakan NextDNS lewat DNS over TLS atau DNS over HTTPS, ganti nama atau tautan NextDNS dengan milik Blokada Anda, seperti di [panduan router](../router-ad-blocking/).

Jika menggunakan NextDNS melalui alamat IP biasa dengan _IP tertaut_, Blokada belum dapat menggantikan itu. Dukungan untuk router dengan alamat DNS biasa sedang dalam pengembangan. Hingga saat itu, atur perangkat Anda satu per satu, atau gunakan router yang mendukung DNS terenkripsi.

## Periksa apakah sudah berfungsi

Buka beberapa situs web, lalu lihat halaman _Aktivitas_ di dashboard. Anda akan melihat pencarian perangkat Anda di sana, dengan yang diblokir ditandai. Jika suatu perangkat tidak muncul, berarti masih menggunakan NextDNS.
