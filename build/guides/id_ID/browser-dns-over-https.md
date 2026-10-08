---
title: Blokir iklan di Chrome, Firefox, Edge, dan Brave dengan DNS over HTTPS
description: Atur Blokada Cloud sebagai penyedia DNS aman di peramban Anda untuk memblokir iklan dan pelacak di komputer apa pun, termasuk laptop kerja di mana Anda tidak dapat memasang aplikasi.
updated: 2026-10-02
order: 7
---

Peramban modern dapat menggunakan penyedia DNS terenkripsi mereka sendiri, disebut _DNS aman_ atau _DNS over HTTPS_. Atur ke Blokada Cloud, dan peramban akan memblokir iklan dan pelacak di jaringan apa pun tanpa perlu menginstal ekstensi.

Pengaturan ini hanya berlaku untuk peramban ini. Untuk mencakup seluruh komputer, gunakan [profil Apple](../apple-devices/) di Mac, atau atur [router](../router-ad-blocking/) Anda.

## Chrome

1. Buka `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Masukkan {% doh %}

## Edge

1. Buka `edge://settings/privacy`.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. Buka `brave://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Masukkan {% doh %}

## Safari

Safari tidak memiliki pengaturan DNS aman sendiri. Safari menggunakan DNS sistem, jadi instal [profil Apple](../apple-devices/).

## Periksa apakah sudah berfungsi

Jelajahi sebentar, lalu buka halaman _Aktivitas_ di [dasbor](https://app.blokada.org/stats?src=guides). Permintaan pencarian dari peramban ini akan muncul di sana.

## Jika ada yang tidak berfungsi

<div class="note tip">

Jika peramban Anda dikendalikan oleh kantor atau sekolah, pengaturan DNS aman mungkin dikunci. Hubungi administrator Anda.

</div>
