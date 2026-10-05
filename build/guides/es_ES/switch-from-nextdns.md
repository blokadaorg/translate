---
title: Una alternativa a NextDNS con la misma configuración en todos los dispositivos
description: Pásese de NextDNS a La Nube de Blokada. Cambie su nombre DNS, enlace DoH o perfil de NextDNS por el de La Nube de Blokada en su teléfono, ordenador y router, y mantenga el bloqueo de anuncios.
updated: 2026-10-02
order: 3
---

NextDNS y La Nube de Blokada funcionan de la misma manera: un servicio DNS cifrado que bloquea anuncios y rastreadores por nombre, con sus propios ajustes detrás de un nombre DNS personal. Cambiar significa reemplazar los valores de NextDNS en cada dispositivo por los de La Nube de Blokada. Nada más en el dispositivo cambia.

## Lo que usaba, y qué elegir en Blokada

| En NextDNS                                                             | En La Nube de Blokada                                                           |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Su ID de configuración, p.ej. `abc123` | Su identificador de dispositivo, parte de su nombre DNS de Blokada y enlace DoH |
| Listas de bloqueo de _privacidad_                                      | Listas de bloqueo en el tablero                                                 |
| _Seguridad_ (malware, phishing)                     | Una lista de malware en _Listas de bloqueo_                                     |
| _Control parental_                                                     | Listas de contenido adulto y apuestas en _Listas de bloqueo_                    |
| _Lista de permitidos_ y _Lista de denegados_                           | _Excepciones_ en el tablero                                                     |
| _Registros_ y _Analíticas_                                             | _Actividad_ y _Estadísticas_ en el tablero                                      |

## Cambie cada dispositivo

Dependiendo del dispositivo, necesita su nombre de DNS o su enlace DoH, ambos se encuentran en _Sus detalles_ arriba.

### Android

Si utilizó _DNS Privado_ con `<your-id>.dns.nextdns.io`, reemplácelo por su nombre de DNS de Blokada, como se indica en la [guía de Android](../android-private-dns/). Si utilizó la app de NextDNS, desinstálela e instale [Blokada 6](https://go.blokada.org/play_cloud) en su lugar.

### iPhone y iPad

Si utilizó la aplicación NextDNS, desinstálela e instale [Blokada 6](https://go.blokada.org/appstore). Si en su lugar instaló un perfil de NextDNS, elimínelo desde _Ajustes → General → VPN y Administración de Dispositivo_, luego siga la [guía para Apple](../apple-devices/).

### Mac y Apple TV

Elimine el perfil o la aplicación de NextDNS, luego instale el perfil de Blokada desde la [guía de Apple](../apple-devices/).

### Windows y Linux

Desinstale la aplicación NextDNS si la usa. En Windows, reemplace el servidor NextDNS y la plantilla DoH por los de Blokada, como indica la [guía de Windows](../windows-dns-over-https/). En Linux, reemplace el servidor NextDNS en systemd-resolved, como se explica en la [guía de Linux](../linux-dns-over-tls/).

### Navegadores

Si configuró `https://dns.nextdns.io/…` como _DNS seguro_ de su navegador, reemplácelo por su enlace DoH, como en la [guía de navegadores](../browser-dns-over-https/).

### Router

Si su router usa NextDNS sobre DNS sobre TLS o DNS sobre HTTPS, reemplace el nombre o enlace de NextDNS por el de Blokada, como en la [guía de routers](../router-ad-blocking/).

Si utiliza NextDNS mediante direcciones IP simples con una _IP vinculada_, Blokada aún no puede hacerse cargo de eso. El soporte para routers con direcciones DNS simples está en camino. Hasta entonces, configure sus dispositivos uno por uno, o utilice un router que admita DNS cifrado.

## Comprobar que funciona

Abra algunos sitios web y luego consulte la página de _Actividad_ en el panel. Allí verá las consultas de sus dispositivos, con las bloqueadas marcadas. Si un dispositivo no aparece, todavía está usando NextDNS.
