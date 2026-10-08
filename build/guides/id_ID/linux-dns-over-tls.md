---
title: Blokir iklan di Linux dengan DNS over TLS
description: Atur systemd-resolved untuk menggunakan Blokada Cloud melalui DNS over TLS terenkripsi, dan blokir iklan serta pelacak untuk setiap aplikasi di komputer Linux Anda.
updated: 2026-10-02
order: 9
---

Sebagian besar distribusi Linux saat ini, termasuk Ubuntu dan Fedora, melakukan resolusi nama melalui _systemd-resolved_, yang mendukung DNS over TLS. Di Debian, instal terlebih dahulu dengan `sudo apt install systemd-resolved`. Arahkan ke Blokada Cloud, dan iklan serta pelacak akan diblokir untuk setiap aplikasi di komputer.

## Atur systemd-resolved

1. Buat folder dengan `sudo mkdir -p /etc/systemd/resolved.conf.d`, lalu file `/etc/systemd/resolved.conf.d/blokada.conf` dengan pengaturan berikut:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Restart layanan: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Periksa: <code>resolvectl status</code> menampilkan <code>+DNSOverTLS</code> dan server Blokada.</li>
</ol>

Bagian setelah `#` adalah nama DNS Blokada Anda: {% dot %} systemd-resolved akan memeriksa sertifikat server terhadapnya, dan Blokada menggunakannya untuk mengidentifikasi perangkat yang melakukan permintaan.

<div class="note important">

**NetworkManager** juga meneruskan server DNS dari jaringan Anda. `Domains=~.` mengirimkan semua permintaan pencarian ke Blokada, tetapi jika `resolvectl status` masih mencantumkan server lain pada suatu koneksi, matikan DNS otomatis untuk koneksi tersebut (pengaturan _Otomatis_ di samping _DNS_ pada pengaturan IPv4 dan IPv6-nya).

</div>

## Tanpa systemd-resolved

Jika `resolvectl` tidak ditemukan, distribusi Anda melakukan resolusi nama dengan cara lain. Atur DNS aman di peramban Anda sesuai [panduan peramban](../browser-dns-over-https/), atau atur [router](../router-ad-blocking/) Anda untuk melindungi seluruh rumah.

## Cek apakah berhasil

Buka beberapa situs web, lalu periksa halaman _Aktivitas_ di [dasbor](https://app.blokada.org/stats?src=guides). Permintaan pencarian komputer ini akan muncul di sana.

<div class="note aside">

Ingin VPN di komputer ini juga? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) mencakup pengaturan WireGuard yang mengenkripsi semua lalu lintas, dengan pemblokiran yang sama.

</div>
