---
title: Bloqueie anúncios em toda sua rede com o bloqueio de anúncios no roteador.
description: Configure o Blokada Cloud no seu roteador uma vez, e todos os dispositivos em casa estarão protegidos, incluindo TVs, consoles de jogos e alto-falantes inteligentes que não podem executar um bloqueador de anúncios.
updated: 2026-10-09​
order: 4
---

Todo dispositivo na sua rede pede ao roteador qual servidor DNS usar. Configure o roteador para o Blokada Cloud, e anúncios e rastreadores serão bloqueados para tudo atrás dele. Isso inclui smart TVs, consoles de jogos, dispositivos de streaming e dispositivos de casa inteligente, que não possuem espaço para um aplicativo bloqueador de anúncios.

## O que seu roteador precisa

Existem duas maneiras de configurar um roteador:

- **DNS criptografado com um nome de host**, ou seja, DNS sobre TLS (DoT) ou DNS sobre HTTPS (DoH). Muitos roteadores recentes são compatíveis, incluindo os modelos abaixo. Dependendo da compatibilidade do seu roteador, você precisará do seu nome DNS ou do seu link DoH, ambos disponíveis em _Seus detalhes_ acima.
- **Um endereço DNS IPv6 simples.** Muitos roteadores fornecidos por provedores de internet aceitam apenas endereços IP simples para DNS. Se este for o caso do seu roteador e a sua conexão possui IPv6, a Blokada fornece um endereço IPv6 para você inserir. Veja [Roteadores que aceitam apenas um endereço IP](#routers-that-only-take-an-ip-address).

Use DNS criptografado se o seu roteador for compatível. As consultas permanecem privadas até a Blokada.

## FRITZ!Box

FRITZ!OS 7.20 ou mais recente.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. Em _Nomes Resolvidos do Servidor DNS_, insira apenas {% dot %}. **Remova todas as outras entradas.** O FRITZ!Box utiliza todos os resolvedores listados, e qualquer outro permite a passagem de anúncios.
4. Tick _Enforce certificate verification for encrypted name resolution_.
5. Se você vir _Failover para servidores DNS públicos quando o DNS estiver interrompido_, desligue essa opção.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Endereço: {% ip "dot" %}
   - Hostname TLS: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Abra _Serviços → HTTPS DNS Proxy_. Exclua as instâncias de outros provedores.
3. Adicione uma instância com uma URL de resolvedor personalizada: {% doh %}
4. _Salvar e Aplicar_. O pacote aponta automaticamente o dnsmasq para ele.

## Outros roteadores

Procure uma configuração chamada _DNS sobre TLS_, _DNS Privado_, _DNS Criptografado_ ou _DNS sobre HTTPS_. Insira o nome DNS da Blokada ou o link DoH informado acima e remova todos os outros servidores DNS, incluindo servidores de fallback. Se não houver tal configuração, use um endereço IPv6 simples conforme abaixo.

## Roteadores que aceitam apenas um endereço IP {:#routers-that-only-take-an-ip-address}

Seu roteador e sua conexão de internet precisam de IPv6 para isso. O suporte para endereços IPv4 simples estará disponível futuramente.

1. No [painel de controle](https://app.blokada.org/setup?src=guides), abra _Configuração_ e escolha _Roteador, TV, console de jogos_.
2. Dê um nome ao roteador, por exemplo _Roteador residencial_, e selecione _Obter endereço_. O nome aparecerá na sua atividade e não poderá ser alterado depois.
3. Nas configurações do roteador, encontre os servidores DNS para IPv6, geralmente em _Internet_, _WAN_ ou _IPv6_, e insira o endereço como o único servidor DNS.
4. **Remova todos os outros servidores DNS, inclusive os IPv4.** Dispositivos que ainda recebem um servidor DNS IPv4 do roteador enviam algumas consultas sem passar pela Blokada. Se o roteador não permitir deixar o campo DNS IPv4 vazio, configure cada dispositivo individualmente: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [navegadores](../browser-dns-over-https/).

A mesma configuração funciona para uma TV ou console de jogos que permita inserir um servidor DNS manualmente. Dê um endereço exclusivo para cada um, assim eles aparecerão pelo nome na sua atividade.

<div class="note aside">

Essas consultas viajam sem criptografia até a Blokada, assim como em qualquer servidor DNS simples. Se seu roteador oferecer suporte a DNS sobre TLS ou DNS sobre HTTPS, prefira essa opção.

</div>

## Verifique se está funcionando

1. Reinicie um dispositivo ou desligue e ligue o Wi-Fi dele para que reconheça a mudança.
2. Nesse dispositivo, desligue o Blokada se ele estiver em execução e depois abra [go.blokada.org/test](https://go.blokada.org/test). Ele mostra se seu DNS está passando pela Blokada.
3. Navegue por um minuto e depois abra a página _Atividade_ no [painel de controle](https://app.blokada.org/stats?src=guides). As consultas da sua rede aparecerão lá.

## Se alguns dispositivos ainda exibirem anúncios

Alguns dispositivos ignoram o roteador: celulares com _DNS Privado_ ativado, navegadores com _DNS seguro_ configurado para outro provedor e dispositivos que usam DNS próprio. Configure esses no próprio dispositivo ou desative as opções de DNS deles.

<div class="note tip">

Atrás do roteador, todos os dispositivos compartilham um endereço, por isso o painel mostra sua rede como um único dispositivo. Configure celulares e notebooks com seus próprios nomes DNS do Blokada se quiser vê-los separadamente. Eles também permanecem protegidos quando saírem de casa.

</div>
