---
title: Mullvad DNS dejará de funcionar. Mantenga Su bloqueo de anuncios con La Nube de Blokada
description: Mullvad cerrará su DNS público el 2 de noviembre de 2026. Aquí le mostramos cómo mover Su teléfono, computadora y router a La Nube de Blokada antes de esa fecha, sin perder el bloqueo de anuncios.
updated: 2026-10-02
order: 2
---

Mullvad cerrará su servicio gratuito de DNS público el **2 de noviembre de 2026** y recomienda Quad9 en su lugar. Quad9 bloquea malware pero **no** bloquea anuncios ni rastreadores. Cuando se detenga el DNS de Mullvad, los dispositivos configurados para usarlo dejarán de cargar sitios web y aplicaciones. Donde un dispositivo pueda alternar a otro servidor DNS, los anuncios volverán a aparecer. Cambia antes de esa fecha.

Esta página trata sobre los nombres públicos de DNS que terminan en `dns.mullvad.net`. No cubre la app de VPN de Mullvad.

## Lo que utilizaba y lo que debe elegir en Blokada

| Nombre de DNS de Mullvad   | Qué bloqueaba                              | En el panel de Blokada                                                                                                                              |
| -------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | nada                                       | Blokada es un servicio de filtrado. Si no desea filtrado, Quad9 o el DNS de Su proveedor es la opción más sencilla. |
| `adblock.dns.mullvad.net`  | anuncios, rastreadores                     | una lista de bloqueo de anuncios y rastreadores                                                                                                     |
| `base.dns.mullvad.net`     | anuncios, rastreadores, malware            | agregue una lista de malware                                                                                                                        |
| `extended.dns.mullvad.net` | base más redes sociales                    | agregue una lista de redes sociales                                                                                                                 |
| `family.dns.mullvad.net`   | base más contenido para adultos y apuestas | agregue listas de contenido para adultos y apuestas                                                                                                 |
| `all.dns.mullvad.net`      | todas las anteriores                       | active todas ellas                                                                                                                                  |

Usted elige las listas de bloqueo en el panel bajo _Listas de bloqueo_. Puede cambiarlas en cualquier momento, y el cambio se aplicará a todos Sus dispositivos.

## Cambie cada dispositivo

Blokada asigna un nombre a cada dispositivo, por lo que el panel puede mostrar la actividad por dispositivo. Dependiendo del dispositivo, necesita su nombre de DNS o su enlace DoH, ambos se encuentran en _Sus detalles_ arriba.

### Android

La guía de Mullvad le indicó que ingresara un nombre de host en _DNS privado_. Reemplácelo por Su nombre de DNS de Blokada. La [guía de Android](../android-private-dns/) tiene los pasos.

### iPhone, iPad y Mac

La configuración de Mullvad utilizó un perfil de configuración. Primero elimínelo:

- **iPhone y iPad:** _Configuración → General → VPN y gestión de dispositivos_, toque el perfil de DNS de Mullvad, luego _Eliminar perfil_.
- **Mac:** abra la lista de perfiles (_Configuración del sistema → General → Gestión de dispositivos_ en macOS 15 y posteriores, _Configuración del sistema → Privacidad y seguridad → Perfiles_ en macOS 13 y 14, _Preferencias del sistema → Perfiles_ en macOS 12 y anteriores), seleccione el perfil de DNS de Mullvad y haga clic en _−_.

Luego instale el perfil de Blokada desde la [guía de Apple](../apple-devices/).

### Navegadores

Si ingresó un enlace DoH de Mullvad como `https://adblock.dns.mullvad.net/dns-query` en _DNS seguro_ o _DNS sobre HTTPS_, reemplácelo por Su enlace DoH. La [guía del navegador](../browser-dns-over-https/) tiene los pasos para cada navegador.

### Router

Si Su router utiliza Mullvad sobre DNS sobre TLS, reemplace el nombre de host de Mullvad con Su nombre de DNS de Blokada, y elimine las direcciones IP de Mullvad. La [guía de router](../router-ad-blocking/) cubre los modelos más comunes.

## Compruebe que funcione

Abra algunos sitios web y luego vea la página de _Actividad_ en el panel. Allí verá las consultas de Sus dispositivos, con las bloqueadas marcadas. Si un dispositivo no aparece, todavía está usando otro servidor DNS.
