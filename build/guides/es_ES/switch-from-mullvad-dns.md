---
title: El DNS de Mullvad dejará de funcionar. Mantenga su bloqueo de anuncios con La Nube de Blokada
description: Mullvad cerrará su DNS público el 2 de noviembre de 2026. Aquí le mostramos cómo migrar su teléfono, computadora y router a La Nube de Blokada antes de esa fecha, sin perder el bloqueo de anuncios.
updated: 2026-10-02
order: 2
---

Mullvad cerrará su servicio de DNS público gratuito el **2 de noviembre de 2026** y recomienda Quad9 como alternativa. Quad9 bloquea el malware pero **no** bloquea anuncios ni rastreadores. Cuando el DNS de Mullvad deje de funcionar, los dispositivos configurados para usarlo dejarán de cargar sitios web y aplicaciones. Si el dispositivo puede cambiar automáticamente a otro servidor DNS, los anuncios volverán a aparecer. Cambie antes de esa fecha.

Esta página trata sobre los nombres públicos de DNS que terminan en `dns.mullvad.net`. No cubre la aplicación VPN de Mullvad.

## Lo que utilizaba y lo que debe elegir en Blokada

| Nombre de DNS de Mullvad   | Qué bloqueaba                              | En el panel de Blokada                                                                                                                             |
| -------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | nada                                       | Blokada es un servicio de filtrado. Si no desea filtrado, Quad9 o el DNS de su proveedor son opciones más simples. |
| `adblock.dns.mullvad.net`  | anuncios, rastreadores                     | una lista de bloqueo de anuncios y rastreadores                                                                                                    |
| `base.dns.mullvad.net`     | anuncios, rastreadores, malware            | agregue una lista de malware                                                                                                                       |
| `extended.dns.mullvad.net` | base más redes sociales                    | agregue una lista de redes sociales                                                                                                                |
| `family.dns.mullvad.net`   | base más contenido para adultos y apuestas | agregue listas de contenido para adultos y apuestas                                                                                                |
| `all.dns.mullvad.net`      | todas las anteriores                       | active todas ellas                                                                                                                                 |

Usted elige las listas de bloqueo en el panel bajo _Listas de bloqueo_. Puede cambiarlas en cualquier momento y el cambio se aplica a todos sus dispositivos.

## Cambie cada dispositivo

Blokada otorga a cada dispositivo su propio nombre, para que el panel pueda mostrar la actividad por dispositivo. Dependiendo del dispositivo, necesitará su nombre DNS o su enlace DoH, ambos en _Sus detalles_ arriba.

### Android

La guía de Mullvad le indicaba ingresar un nombre de host en _DNS Privado_. Reemplace ese nombre por su nombre DNS de Blokada. La [guía para Android](../android-private-dns/) contiene los pasos.

### iPhone, iPad y Mac

La configuración de Mullvad utilizaba un perfil de configuración. Elimínelo primero:

- **iPhone y iPad:** _Configuración → General → VPN y gestión de dispositivos_, toque el perfil de DNS de Mullvad, luego _Eliminar perfil_.
- **Mac:** abra la lista de perfiles (_Configuración del sistema → General → Gestión de dispositivos_ en macOS 15 y posteriores, _Configuración del sistema → Privacidad y seguridad → Perfiles_ en macOS 13 y 14, _Preferencias del sistema → Perfiles_ en macOS 12 y anteriores), seleccione el perfil de DNS de Mullvad y haga clic en _−_.

Luego instale el perfil de Blokada desde la [guía de Apple](../apple-devices/).

### Navegadores

Si ingresó un enlace DoH de Mullvad como `https://adblock.dns.mullvad.net/dns-query` bajo _DNS seguro_ o _DNS sobre HTTPS_, reemplácelo por su enlace DoH. La [guía del navegador](../browser-dns-over-https/) tiene los pasos para cada navegador.

### Router

Si su router usa Mullvad sobre DNS sobre TLS, reemplace el nombre de host de Mullvad por su nombre DNS de Blokada y elimine las direcciones IP de Mullvad. La [guía para routers](../router-ad-blocking/) cubre los modelos más comunes.

## Compruebe que funcione

Abra algunos sitios web y luego revise la página de _Actividad_ en el panel. Allí verá las consultas de sus dispositivos, con las bloqueadas marcadas. Si un dispositivo no aparece, todavía está usando otro servidor DNS.
