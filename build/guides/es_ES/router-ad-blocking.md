---
title: Bloquee los anuncios en toda su red con el bloqueo de anuncios en el router.
description: Configure La Nube de Blokada en su router una sola vez y todos los dispositivos de su hogar estarán protegidos, incluyendo televisores, consolas de juegos y altavoces inteligentes que no pueden ejecutar un bloqueador de anuncios.
updated: 2026-10-09
order: 4
---

Cada dispositivo en su red solicita al router qué servidor DNS usar. Apunte el router a la Nube de Blokada y los anuncios y rastreadores serán bloqueados para todo lo que esté conectado a él. Esto incluye televisores inteligentes, consolas de videojuegos, dispositivos de streaming y dispositivos del hogar inteligente, que no permiten instalar una app de bloqueador de anuncios.

## Lo que necesita su router

Hay dos maneras de configurar un router:

- **DNS cifrado con un nombre de host**, es decir, DNS sobre TLS (DoT) o DNS sobre HTTPS (DoH). Muchos routers recientes lo admiten, incluidos los modelos mencionados abajo. Dependiendo de lo que admita su router, necesitará su nombre DNS o su enlace DoH, ambos indicados en _Sus detalles_ arriba.
- **Una dirección DNS IPv6 simple.** Muchos routers de proveedores de internet sólo aceptan direcciones IP simples para DNS. Si el suyo lo hace y su conexión tiene IPv6, Blokada le proporciona una dirección IPv6 para ingresar. Vea [Routers que solo aceptan una dirección IP](#routers-that-only-take-an-ip-address).

Utilice DNS cifrado si su router lo soporta. Las consultas permanecen privadas en su camino hacia Blokada.

## FRITZ!Box

FRITZ!OS 7.20 o posterior.

1. Abra `http://fritz.box` y vaya a _Internet → Información de la cuenta → Servidor DNS_.
2. En _Resolución de nombres cifrada en Internet (DNS sobre TLS)_, marque _Usar resolución de nombres cifrada_.
3. En _Nombres resueltos del servidor DNS_, introduzca solo {% dot %}. **Elimine todas las demás entradas.** El FRITZ!Box utiliza todos los resolutores que aparecen en la lista, y cualquier otro permitirá el paso de anuncios.
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
4. _Guardar y aplicar_. El paquete apunta automáticamente dnsmasq a él.

## Otros routers

Busque una opción llamada _DNS sobre TLS_, _DNS privado_, _DNS cifrado_ o _DNS sobre HTTPS_. Introduzca su nombre DNS de Blokada o enlace DoH de arriba, y elimine todos los demás servidores DNS, incluidos los de respaldo. Si no existe tal opción, utilice una dirección IPv6 simple como se muestra a continuación.

## Enrutadores que solo aceptan una dirección IP

Su enrutador y su conexión a internet necesitan IPv6 para esto. El soporte para direcciones IPv4 simples estará disponible más adelante.

1. En el [panel](https://app.blokada.org/setup?src=guides), abra _Configuración_ y elija _Enrutador, TV, consola de juegos_.
2. Asigne un nombre al enrutador, por ejemplo _Enrutador de casa_, y seleccione _Obtener dirección_. El nombre aparecerá en su actividad y no se podrá cambiar después.
3. En la configuración del enrutador, busque los servidores DNS para IPv6, normalmente en _Internet_, _WAN_ o _IPv6_, e introduzca la dirección como único servidor DNS.
4. **Elimine todos los demás servidores DNS, incluidos los de IPv4.** Los dispositivos que aún reciben un servidor DNS IPv4 del enrutador envían algunas búsquedas fuera de Blokada. Si el enrutador no puede dejar el DNS IPv4 vacío, configure sus dispositivos uno por uno en su lugar: [Android](../android-private-dns/), [Mac y Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) y [navegadores](../browser-dns-over-https/).

La misma configuración funciona para una TV o consola de juegos que le permita introducir manualmente un servidor DNS. Dele a cada uno su propia dirección, para que aparezca por nombre en su actividad.

<div class="note aside">

Estas búsquedas viajan sin cifrar a Blokada, como con cualquier servidor DNS simple. Si su enrutador admite DNS sobre TLS o DNS sobre HTTPS, utilícelo en su lugar.

</div>

## Compruebe que funciona

1. Reinicie un dispositivo, o apague y encienda su Wi-Fi, para que recoja el cambio.
2. En ese dispositivo, apague Blokada si la está ejecutando, luego abra [go.blokada.org/test](https://go.blokada.org/test). Muestra si su DNS pasa por Blokada.
3. Navegue durante un minuto y luego abra la página de _Actividad_ en el [panel](https://app.blokada.org/stats?src=guides). Las búsquedas de su red aparecerán allí.

## Si algunos dispositivos siguen mostrando anuncios

Algunos dispositivos evitan el router: teléfonos con _DNS privado_ activado, navegadores con _DNS seguro_ configurado con otro proveedor y dispositivos que usan su propio DNS. Configure esos dispositivos individualmente, o desactive su propia configuración de DNS.

<div class="note tip">

Detrás del router, todos los dispositivos comparten una dirección, por lo que el panel de control muestra su red como un solo dispositivo. Configure teléfonos y ordenadores portátiles con su propio nombre DNS de Blokada si quiere verlos por separado. También seguirán bloqueando anuncios cuando salgan de casa.

</div>
