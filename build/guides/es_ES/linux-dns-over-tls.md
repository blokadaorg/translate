---
title: Bloquear anuncios en Linux con DNS sobre TLS
description: Configure systemd-resolved para usar La Nube de Blokada a través de DNS cifrado sobre TLS, y bloquee anuncios y rastreadores para cada aplicación en su ordenador Linux.
updated: 2026-10-02
order: 9
---

La mayoría de las distribuciones Linux actuales, incluidas Ubuntu y Fedora, resuelven los nombres mediante <em>systemd-resolved</em>, que admite DNS sobre TLS. En Debian, instálelo primero con <code>sudo apt install systemd-resolved</code>. Apúntelo a La Nube de Blokada, y los anuncios y rastreadores se bloquean para cada aplicación del ordenador.

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

<b>NetworkManager</b> también pasa los servidores DNS de su red. <code>Domains=~.</code> envía todas las consultas a Blokada, pero si <code>resolvectl status</code> todavía lista otro servidor en una conexión, desactive el DNS automático para esa conexión (el interruptor <em>Automático</em> junto a <em>DNS</em> en su configuración IPv4 e IPv6).

</div>

## Sin systemd-resolved

Si no se encuentra <code>resolvectl</code>, su distribución resuelve los nombres de otra manera. En su lugar, configure el DNS seguro en su navegador, como se explica en la [guía del navegador](../browser-dns-over-https/), o configure su [router](../router-ad-blocking/) para cubrir toda la casa.

## Compruebe que funciona

Abra algunos sitios web y luego mire la página <em>Actividad</em> en el [panel de control](https://app.blokada.org/stats?src=guides). Las búsquedas de este ordenador aparecerán allí.

<div class="note aside">

¿Quiere una VPN en este ordenador también? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) incluye una configuración de WireGuard que cifra todo el tráfico, con el mismo bloqueo.

</div>
