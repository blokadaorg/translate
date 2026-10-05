---
title: Bloquea anuncios en Mac y Apple TV con un perfil DNS de Blokada
description: Instala un perfil DNS de La Nube de Blokada para bloquear anuncios y rastreadores en todo el sistema de un Mac o Apple TV, con DNS cifrado y sin nada ejecutándose en segundo plano.
updated: 2026-10-02
order: 6
---

Los dispositivos Apple pueden usar DNS cifrado para todo el sistema mediante un perfil de configuración. El perfil de Blokada dirige el dispositivo a la Nube de Blokada, que bloquea anuncios y rastreadores en todas las aplicaciones y navegadores.

Funciona en macOS 11 (Big Sur), tvOS 14, iOS y iPadOS 14 y versiones posteriores.

<div class="if-no-device">

Esta página aún no conoce su dispositivo, por lo que no puede ofrecerle su perfil. Inicie sesión en el panel, abra _Configuración_, elija su dispositivo y abra esta guía con _Abrir en otro dispositivo_.

<p><a class=\"btn btn-outline\" href=\"https://app.blokada.org/setup?src=guides\">Obtener mi enlace de perfil</a></p>

</div>

## iPhone y iPad

La forma más fácil es la aplicación. [Blokada 6](https://go.blokada.org/appstore) configura todo por usted, activa y desactiva el bloqueo con un solo toque, y muestra lo que fue bloqueado en el propio teléfono. Inicie sesión con su ID de cuenta y ha terminado.

<p><a class=\"btn btn-primary\" href=\"https://go.blokada.org/appstore\">Consiga Blokada 6 en la App Store</a></p>

### Sin la aplicación

También puede instalar el perfil. El iPhone y el iPad solo instalan perfiles desde **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Esta página está abierta en otro navegador. Copie su enlace y ábralo en Safari para continuar allí: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. En Safari, toque el botón de abajo y luego _Permitir_ para descargar el perfil.
2. Abra _Configuración_. Toque _Perfil descargado_ cerca de la parte superior. También puede encontrarlo en _General → VPN y administración de dispositivos_.
3. Toque _Instalar_, introduzca su código y confirme.

</div>

<p class="if-device if-safari">{% appleProfile %}Descargar mi perfil{% endappleProfile %}</p>

## Mac

1. Haga clic en el botón de abajo para descargar el perfil.
2. Abra la lista de perfiles: _Ajustes del sistema → General → Gestión de dispositivos_ en macOS 15 y posteriores, _Ajustes del sistema → Privacidad y seguridad → Perfiles_ en macOS 13 y 14, o _Preferencias del sistema → Perfiles_ en macOS 12 y anteriores.
3. Haga doble clic en el perfil de Blokada y haga clic en _Instalar_.

<p class="if-device">{% appleProfile %}Descargar mi perfil{% endappleProfile %}</p>

## Apple TV

El Apple TV no puede abrir páginas web, por lo que debe escribir su enlace de perfil en él.

1. Su enlace de perfil: {% appleUrl %}
2. En el Apple TV, abra _Ajustes → General → Privacidad y seguridad_.
3. Resalte _Compartir análisis del Apple TV_. No lo seleccione. Presione el botón de Reproducir/Pausa en el control remoto en su lugar.
4. Elija _Agregar perfil_ e ingrese su enlace de perfil. Es más fácil escribirlo con el teclado de su iPhone, donde puede pegarlo. Instale el perfil y confirme.

<div class="note aside">

**Apple TV y otros dispositivos en casa:** si configura La Nube de Blokada en su [router](../router-ad-blocking/), el Apple TV estará protegido junto con todo lo demás.

</div>

## Compruebe que funcione

Navegue durante un minuto, luego abra la página de _Actividad_ en el [panel](https://app.blokada.org/stats?src=guides). Las búsquedas de este dispositivo aparecerán allí.

Para quitar Blokada después, elimine el perfil donde lo instaló.
