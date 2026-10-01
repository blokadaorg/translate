---
title: Una alternativa a NextDNS con la misma configuración en todos los dispositivos
description: Pase de NextDNS a La Nube de Blokada. Intercambie su nombre DNS, enlace DoH o perfil de NextDNS por el de Blokada en su teléfono, ordenador y router, y mantenga el bloqueo de anuncios.
updated: 2026-10-01
order: 3
---

NextDNS y La Nube de Blokada funcionan de la misma manera: un servicio DNS cifrado que bloquea anuncios y rastreadores por nombre, con su propia configuración detrás de un nombre DNS personal. Cambiar significa reemplazar los valores de NextDNS en cada dispositivo por los suyos de Blokada. Nada más en el dispositivo cambia.

## Lo que usaba, y qué elegir en Blokada

| En NextDNS                                                             | En La Nube de Blokada                                                           |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Su ID de configuración, p.ej. `abc123` | Su identificador de dispositivo, parte de su nombre DNS de Blokada y enlace DoH |
| Listas de bloqueo de _privacidad_                                      | Listas de bloqueo en el tablero                                                 |
| _Seguridad_ (malware, phishing)                     | Una lista de malware en _Listas de bloqueo_                                     |
| _Control parental_                                                     | Listas de contenido adulto y apuestas en _Listas de bloqueo_                    |
| _Lista de permitidos_ y _Lista de denegados_                           | _Excepciones_ en el tablero                                                     |
| _Registros_ y _Analíticas_                                             | _Actividad_ y _Estadísticas_ en el tablero                                      |

## Sus detalles de Blokada

- Su nombre DNS de Blokada, para DNS sobre TLS: {% dot %}
- Su enlace DoH, para DNS sobre HTTPS: {% doh %}

## Cambie cada dispositivo

### Android

Si usó _DNS Privado_ con `<su-id>.dns.nextdns.io`, reemplácelo por su nombre DNS de Blokada, como en la [guía de Android](../android-private-dns/). Si usó la aplicación de NextDNS, desinstálela e instale [Blokada 6](https://go.blokada.org/play_cloud) en su lugar.

### iPhone y iPad

Si usó la aplicación de NextDNS, desinstálela e instale [Blokada 6](https://go.blokada.org/appstore). Si instaló un perfil de NextDNS en su lugar, elimínelo en _Configuración → General → VPN y gestión de dispositivos_, luego siga la [guía de Apple](../apple-devices/).

### Mac y Apple TV

Elimine el perfil o la aplicación de NextDNS, luego instale el perfil de Blokada desde la [guía de Apple](../apple-devices/).

### Windows y Linux

Desinstale la aplicación de NextDNS si la utiliza. En Windows, reemplace el servidor y plantilla DoH de NextDNS por los de Blokada, como en la [guía de Windows](../windows-dns-over-https/). En Linux, reemplace el servidor NextDNS en systemd-resolved, como en la [guía de Linux](../linux-dns-over-tls/).

### Navegadores

Si configuró `https://dns.nextdns.io/…` como _DNS seguro_ de su navegador, reemplácelo por su enlace DoH, como en la [guía de navegadores](../browser-dns-over-https/).

### Router

Si su router usa NextDNS sobre DNS sobre TLS o DNS sobre HTTPS, reemplace el nombre o enlace de NextDNS por el de Blokada, como en la [guía de routers](../router-ad-blocking/).

Si utiliza NextDNS a través de direcciones IP simples con una _IP vinculada_, Blokada aún no puede hacerse cargo de eso. El soporte para routers con direcciones DNS simples está en camino. Hasta entonces, configure sus dispositivos uno por uno, o use un router que soporte DNS cifrado.

## Comprobar que funciona

Abra algunos sitios web, luego mire la página de _Actividad_ en el tablero. Verá las consultas de sus dispositivos allí, con las bloqueadas marcadas. Si un dispositivo no aparece, todavía está usando NextDNS.
