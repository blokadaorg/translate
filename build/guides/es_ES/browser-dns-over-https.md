---
title: Bloquee anuncios en Chrome, Firefox, Edge y Brave con DNS sobre HTTPS.
description: Configure La Nube de Blokada como el proveedor de DNS seguro en su navegador para bloquear anuncios y rastreadores, en cualquier computadora, incluyendo portátiles de trabajo donde no puede instalar aplicaciones.
updated: 2026-09-23
order: 7
---

Los navegadores modernos pueden usar su propio proveedor de DNS cifrado, llamado _DNS seguro_ o _DNS sobre HTTPS_. Establézcalo en La Nube de Blokada, y el navegador bloquea anuncios y rastreadores en cualquier red, sin necesidad de instalar extensiones.

Esta configuración cubre solo este navegador. Para cubrir toda la computadora, use el [perfil de Apple](../apple-devices/) en una Mac, o configure su [router](../router-ad-blocking/).

Su enlace DoH: {% doh %}

## Chrome

1. Abra `chrome://settings/security`.
2. Active _Usar DNS seguro_, luego elija _Agregar proveedor de servicios DNS personalizado_.
3. Introduzca {% doh %}

## Edge

1. Abra `edge://settings/privacy`.
2. En _Seguridad_, active _Usar DNS seguro para especificar cómo buscar la dirección de red de los sitios web_.
3. Elija _Elegir un proveedor de servicios_ e introduzca {% doh %}

## Firefox

1. Abra _Configuración → Privacidad y seguridad_ y desplácese hasta _DNS sobre HTTPS_.
2. Elija _Protección máxima_.
3. En _Elegir proveedor_, seleccione _Personalizado_ e introduzca {% doh %}

## Brave

1. Abra `brave://settings/security`.
2. Active _Usar DNS seguro_, luego elija _Agregar proveedor de servicios DNS personalizado_.
3. Introduzca {% doh %}

## Safari

Safari no tiene una configuración propia de DNS seguro. Utiliza el DNS del sistema, así que instale el [perfil de Apple](../apple-devices/).

## Compruebe que funciona

Navegue durante un minuto y luego abra la página de _Actividad_ en el [panel](https://app.blokada.org/stats?src=guides). Las consultas de este navegador se mostrarán allí.

<div class="note">

Si su navegador es administrado por el trabajo o la escuela, la configuración de DNS seguro podría estar bloqueada. Consulte con su administrador.

</div>
