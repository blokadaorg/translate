---
title: Una alternativa a Pi-hole que no necesita hardware.
description: Traslade el bloqueo de anuncios de su hogar de un Pi-hole a La Nube de Blokada, o mantenga su Pi-hole y envíe sus consultas a través de Blokada.
updated: 2026-10-02
order: 1
---

Un Pi-hole bloquea los anuncios para cada dispositivo en su red, siempre y cuando la Raspberry Pi esté funcionando, actualizada y en casa. La Nube de Blokada hace el mismo trabajo desde nuestros servidores:

- **Sin caja que mantener.** Sin tarjetas SD, sin actualizaciones, sin interrupciones cuando el Pi se apaga.
- **Funciona fuera de casa.** Los teléfonos y portátiles mantienen el bloqueo tanto en datos móviles como en otras redes Wi-Fi.
- **Encriptado.** Los dispositivos se comunican con Blokada usando DNS sobre TLS o DNS sobre HTTPS, de modo que su proveedor no puede leer ni modificar sus consultas.
- **Un solo panel de control.** Listas de bloqueo, dominios permitidos y bloqueados, y actividad por dispositivo, en [app.blokada.org](https://app.blokada.org/?src=guides).

Hay dos formas de hacer el cambio: reemplazar completamente el Pi-hole o mantenerlo y usar La Nube de Blokada como su DNS ascendente.

## Opción 1: reemplace el Pi-hole

1. **Consiga La Nube de Blokada** y abra el panel de control. Su nombre DNS y el enlace DoH están en _Configuración_ allí, y en _Sus datos_ arriba.
2. **Apunte su router a Blokada en vez del Pi-hole.** Siga la [guía para routers](../router-ad-blocking/). Si su router solo acepta una dirección IP como servidor DNS, configure sus dispositivos uno por uno en su lugar: [Android](../android-private-dns/), [Mac y Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) y [navegadores](../browser-dns-over-https/).
3. **Si su Pi-hole era el servidor DHCP,** active el DHCP de nuevo en su router _antes_ de apagar el Pi. De lo contrario, sus dispositivos dejarán de recibir direcciones de red.
4. **Mueva sus listas.** En el panel de control, elija las listas de bloqueo en _Listas de bloqueo_, y añada sus propios dominios permitidos o bloqueados en _Excepciones_.
5. **Apague el Pi-hole,** o consérvelo para otro uso.

<div class="note aside">

Su Pi-hole mostraba cada dispositivo en la red por su dirección IP. Con Blokada, cada dispositivo aparece con su propio nombre, siempre que use su propio nombre DNS de Blokada. Un router configurado con un nombre DNS de Blokada aparecerá como un solo dispositivo.

</div>

## Opción 2: mantenga el Pi-hole, use La Nube de Blokada como ascendente

Si desea mantener su configuración local, como nombres de host locales, DHCP o sus propias listas, deje que el Pi-hole envíe sus búsquedas a Blokada a través de una conexión cifrada. Pi-hole no puede hacer reenvío cifrado por sí mismo, así que un pequeño reenviador corre junto a él. Esta guía utiliza [dnsproxy](https://github.com/AdguardTeam/dnsproxy), un reenviador de código abierto que es un solo archivo.

1. En la máquina de Pi-hole, descargue la versión de `dnsproxy` para su CPU (`linux-arm64` para un Raspberry Pi reciente) desde su página de lanzamientos, y copie el binario `dnsproxy` a `/usr/local/bin/`.
2. Cree `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]\nDescription=Encrypted DNS forwarder to La Nube de Blokada\nWants=network-online.target\nAfter=network-online.target\n\n[Service]\nExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns=\"dot\">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9\nRestart=always\nDynamicUser=yes\n\n[Install]\nWantedBy=multi-user.target</code></pre>

3. Inícielo: `sudo systemctl enable --now dnsproxy`
4. En el panel de administración de Pi-hole, abra _Ajustes → DNS_. Desmarque todos los servidores ascendentes y añada `127.0.0.1#5054` como servidor ascendente personalizado. Guarde.
5. Revise la página de _Actividad_ del panel de control. Ahora las búsquedas desde su red aparecerán allí.

Puede desactivar las listas de bloqueo propias del Pi-hole y gestionar el bloqueo desde el panel de control, o mantener ambas.

## Preguntas frecuentes

**¿Necesito Blokada Plus?** No. La Nube de Blokada cubre el bloqueo de DNS para toda su casa. [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) añade una VPN adicional.

**¿Qué pasa si Blokada no está disponible?** Sus dispositivos no podrán resolver nombres hasta que vuelva, igual que cuando Pi-hole deja de funcionar. No agregue un segundo servidor DNS sin filtro como respaldo. La mayoría de los dispositivos usan todos sus servidores de manera aleatoria, por lo que los anuncios se colarían.
