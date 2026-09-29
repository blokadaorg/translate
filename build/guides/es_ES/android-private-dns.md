---
title: Configura DNS privado en Android con La Nube de Blokada
description: Utilice la configuración de DNS privado integrada de Android con La Nube de Blokada para bloquear anuncios y rastreadores en cada app, tanto en Wi-Fi como en datos móviles. O deja que la app Blokada 6 lo haga.
updated: 2026-09-28
order: 5
---

## La forma más sencilla: la app

[Blokada 6](https://go.blokada.org/play_cloud) configura todo por usted, permite activar y desactivar el bloqueo con un solo toque y muestra lo que fue bloqueado en el propio teléfono. Inicie sesión con su ID de cuenta y habrá terminado.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/play_cloud\">Obtener Blokada 6 en Google Play</a></p>

## Sin la app: DNS privado

Android 9 y versiones posteriores tienen una configuración de _DNS privado_. Configúrelo en La Nube de Blokada y los anuncios y rastreadores serán bloqueados en todas las apps, en todas las redes, sin que nada se ejecute en segundo plano.

Su nombre de DNS de Blokada: {% dot %}

1. Abra _Configuración → Red e Internet_. En algunos teléfonos esto es _Conexiones_ o _Conexión y compartición_.
2. Toque _DNS privado_. En los teléfonos Samsung está en _Configuraciones de conexión adicionales_.
3. Elija _Nombre del host del proveedor de DNS privado_.
4. Ingrese su nombre de DNS de Blokada {% dot %} y toque _Guardar_.

Si no lo encuentra, busque "DNS privado" en la app de Configuración.

## Comprobar que funciona

Abra algunas apps o sitios web y luego mire la página de _Actividad_ en el [panel de control](https://app.blokada.org/stats?src=guides). Las búsquedas de este teléfono aparecerán allí.

## Si algo no funciona

- **"No se pudo conectar" o sin internet:** verifique que su nombre de DNS de Blokada no tenga errores tipográficos. Debe ser exactamente como se muestra arriba, sin `https://`.
- **Otra app VPN está activa:** algunas apps VPN usan su propio DNS y omiten el DNS privado. Desactive la configuración de DNS o bloqueo de anuncios de la VPN, o use Blokada 6 en su lugar.
- **Chrome aún muestra anuncios:** en Chrome, abra _Configuración → Privacidad y seguridad → Usar DNS seguro_ y elija _Usar proveedor de servicios actual_.
