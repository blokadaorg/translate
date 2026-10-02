---
title: Bloquee los anuncios en toda su red con el bloqueo de anuncios en el router.
description: Configure La Nube de Blokada en su router una sola vez y todos los dispositivos de su hogar estarán protegidos, incluyendo televisores, consolas de juegos y altavoces inteligentes que no pueden ejecutar un bloqueador de anuncios.
updated: 2026-10-02
order: 4
---

Cada dispositivo en su red le pide al router qué servidor DNS debe usar. Apunte el router a La Nube de Blokada y los anuncios y rastreadores se bloquearán para todo lo que esté detrás de él. Eso incluye televisores inteligentes, consolas de juegos, sticks de streaming y dispositivos inteligentes para el hogar, que no tienen espacio para una app de bloqueador de anuncios.

## Lo que necesita su router

Su router debe soportar **DNS cifrado con un nombre de host**, es decir, DNS sobre TLS (DoT) o DNS sobre HTTPS (DoH). Muchos routers recientes lo permiten, incluyendo los modelos que se indican a continuación. Dependiendo de lo que sea compatible con su router, necesita su nombre DNS o su enlace DoH, ambos debajo de _Sus detalles_ arriba.

<div class="note important">

Muchos routers de proveedores de internet solo aceptan direcciones IP simples para DNS. El soporte para estos casos está en camino. Mientras tanto, configure sus dispositivos uno por uno: [Android](../android-private-dns/), [Mac y Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) y [navegadores](../browser-dns-over-https/). También puede ejecutar un pequeño reenviador en una Raspberry Pi, como se describe en la [guía de Pi-hole](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 o posterior.

1. Abra `http://fritz.box` y vaya a _Internet → Información de la cuenta → Servidor DNS_.
2. En _Resolución de nombres cifrada en Internet (DNS sobre TLS)_, marque _Usar resolución de nombres cifrada_.
3. En _Nombres de los resolutores_, introduzca solo {% dot %}. **Elimine todas las demás entradas.** El FRITZ!Box utiliza todos los resolutores que aparecen en la lista, y cualquier otro permitirá el paso de anuncios.
4. Selecciona la opción que obliga la verificación de certificados y desmarca la que permite volver a la resolución de nombres sin cifrar.
5. Si ves _Conmutar a servidores DNS públicos cuando el DNS se interrumpe_, apágalo.
6. Haga clic en _Aplicar_.

## ASUS

Firmware reciente de ASUS (3.0.0.4.388 o posterior) y Asuswrt-Merlin.

1. Abra la página de administración del router y vaya a _WAN → Conexión a Internet_.
2. En _Configuración de DNS WAN_, establezca _Protocolo de privacidad DNS_ en _DNS-over-TLS (DoT)_ y _Perfil de DNS-over-TLS_ en _Estricto_.
3. Elimine todas las entradas de la _Lista de servidores DNS-over-TLS_, luego añada una:
   - Dirección: {% ip "dot" %}
   - Nombre de host TLS: {% dot %}
4. Haga clic en _Aplicar_.

## OpenWrt

1. En _Sistema → Software_, actualice las listas e instale `luci-app-https-dns-proxy`.
2. Abra _Servicios → Proxy HTTPS DNS_. Elimine las instancias de otros proveedores.
3. Agregue una instancia con una URL de resolutor personalizada: {% doh %}
4. _Guardar y Aplicar_. El paquete apunta automáticamente dnsmasq a él.

## Otros routers

Busque una opción llamada _DNS sobre TLS_, _DNS privado_, _DNS cifrado_ o _DNS sobre HTTPS_. Introduzca su nombre DNS de Blokada o el enlace DoH de arriba y elimine cualquier otro servidor DNS, incluidos los de respaldo.

## Compruebe que funciona

1. Reinicie un dispositivo, o apague y encienda su Wi-Fi, para que recoja el cambio.
2. Navegue por un minuto y luego abra la página de _Actividad_ en el panel de control. Las consultas de su red aparecerán allí.

## Si algunos dispositivos siguen mostrando anuncios

Algunos dispositivos evitan el router: teléfonos con _DNS privado_ activado, navegadores con _DNS seguro_ configurado con otro proveedor y dispositivos que usan su propio DNS. Configure esos en el propio dispositivo, o desactive la configuración de DNS propia.

<div class="note tip">

Detrás del router, todos los dispositivos comparten una dirección, por lo que el panel muestra su red como un solo dispositivo. Configure teléfonos y portátiles con su propio nombre DNS de Blokada si quiere verlos por separado. También mantienen su bloqueo cuando salen de casa.

</div>
