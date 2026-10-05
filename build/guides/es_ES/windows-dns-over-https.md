---
title: Bloquee anuncios en Windows con DNS sobre HTTPS.
description: Utilice el DNS cifrado integrado en Windows 11 con La Nube de Blokada para bloquear anuncios y rastreadores en cada aplicación y navegador, sin necesidad de instalar software.
updated: '"2026-10-02"'
order: 8
---

Windows 11 puede enviar todas sus consultas de DNS cifradas, a través de DNS sobre HTTPS. Apúntelo a la Nube de Blokada, y los anuncios y rastreadores serán bloqueados en cada aplicación y navegador en el equipo, sin necesidad de instalar nada.

Necesita la dirección IP del servidor DNS y su enlace DoH, ambos se encuentran en _Sus detalles_ arriba.

## Windows 11

1. Abra _Configuración → Red e internet_, luego _Wi-Fi_ o _Ethernet_, dependiendo de cómo esté conectado el ordenador.
2. Abra las _propiedades de hardware_ de su conexión. Para Wi-Fi, seleccione _Gestionar redes conocidas_ y luego la red, o _Propiedades de hardware_ en la parte superior de la página de Wi-Fi.
3. Junto a _Asignación de servidor DNS_, seleccione _Editar_. Elija _Manual_ y active _IPv4_.
4. En _DNS preferido_, introduzca el servidor DNS {% ip "doh" %}
5. Establezca _DNS sobre HTTPS_ en _Activado (plantilla manual)_ e introduzca su enlace DoH {% doh %} como la _plantilla DoH_.
6. Desactive _Permitir volver a texto sin formato_ y seleccione _Guardar_.

Si el ordenador utiliza tanto Wi-Fi como Ethernet, repita esto para la otra conexión.

<div class="note important">

Deje _DNS alternativo_ vacío. Windows usa ambos servidores, y cualquier otro permite que los anuncios pasen.

</div>

<div class="note tip">

¿No ve la opción _Activado (plantilla manual)_? Su Windows 11 es más antiguo. Actualice Windows o utilice la [guía del navegador](../browser-dns-over-https/) mientras tanto.

</div>

## Windows 10

Windows 10 no cuenta con DNS cifrado integrado. En su lugar, configure el DNS seguro en su navegador, como se explica en la [guía del navegador](../browser-dns-over-https/), o configure su [router](../router-ad-blocking/) para cubrir toda la casa.

## Compruebe que funciona

Abre algunos sitios web y luego revisa la página _Actividad_ en el [panel de control](https://app.blokada.org/stats?src=guides). Las consultas de este ordenador aparecerán ahí.

<div class="note aside">

¿Quiere una VPN también en este equipo? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) incluye una configuración de WireGuard que cifra todo el tráfico, con el mismo bloqueo.

</div>

## Si algo no funciona

Chrome y Edge tienen su propia configuración de _DNS seguro_, que omite Windows. Si se deja en automático, puede regresar al DNS sin cifrar, lo que Blokada rechaza. En su lugar, asígnele su enlace DoH:

- **Chrome:** abra `chrome://settings/security`, active _Usar DNS seguro_, y en _Seleccionar proveedor de DNS_ elija _Agregar proveedor de DNS personalizado_.
- **Edge:** abra `edge://settings/privacy`, active DNS seguro, y elija _Seleccionar un proveedor de servicio_.

Luego pegue su enlace DoH {% doh %}

Si todavía se muestran algunos anuncios en una red con IPv6, Windows podría estar usando también el servidor DNS IPv6 de su router. Desactive _Protocolo de Internet versión 6 (TCP/IPv6)_ en las propiedades del adaptador (_Panel de control → Conexiones de red_), o configure su [router](../router-ad-blocking/).
