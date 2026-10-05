---
title: Bloquear anuncios en Linux con DNS sobre TLS
description: Configure systemd-resolved para usar La Nube de Blokada a través de DNS cifrado sobre TLS, y bloquee anuncios y rastreadores para cada aplicación en su ordenador Linux.
updated: 2026-10-02
order: 9
---

La mayoría de las distribuciones actuales de Linux, incluidas Ubuntu y Fedora, resuelven los nombres a través de _systemd-resolved_, que admite DNS sobre TLS. En Debian, instálelo primero con `sudo apt install systemd-resolved`. Apúntelo a la Nube de Blokada y los anuncios y rastreadores serán bloqueados para cada app en el ordenador.

## Configurar systemd-resolved

1. Cree la carpeta con <code>sudo mkdir -p /etc/systemd/resolved.conf.d</code>, luego el archivo <code>/etc/systemd/resolved.conf.d/blokada.conf</code> con estas opciones:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns=\"dot\">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Reinícielo: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Compruébelo: <code>resolvectl status</code> muestra <code>+DNSOverTLS</code> y el servidor de Blokada.</li>
</ol>

La parte después de <code>#</code> es su nombre DNS de Blokada: {% dot %} systemd-resolved comprueba el certificado del servidor con él, y Blokada lo usa para saber qué dispositivo está consultando.

<div class="note important">

**NetworkManager** también transmite los servidores DNS de su red. `Domains=~.` envía todas las consultas a Blokada, pero si `resolvectl status` todavía muestra otro servidor en una conexión, desactive el DNS automático para esa conexión (el interruptor _Automático_ junto a _DNS_ en su configuración IPv4 e IPv6).

</div>

## Sin systemd-resolved

Si no se encuentra `resolvectl`, su distribución resuelve los nombres de otra manera. En su lugar, configure el DNS seguro en su navegador, como se explica en la [guía del navegador](../browser-dns-over-https/), o configure su [router](../router-ad-blocking/) para cubrir toda la casa.

## Compruebe que funciona

Abra algunos sitios web, luego consulte la página _Actividad_ en el [dashboard](https://app.blokada.org/stats?src=guides). Las búsquedas de este ordenador aparecerán allí.

<div class="note aside">

¿Quiere una VPN también en este ordenador? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) incluye una configuración de WireGuard que cifra todo el tráfico, con el mismo bloqueo.

</div>
