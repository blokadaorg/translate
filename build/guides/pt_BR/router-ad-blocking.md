---
title: Bloqueie anúncios em toda sua rede com o bloqueio de anúncios no roteador.
description: Configure o Blokada Cloud no seu roteador uma vez, e todos os dispositivos em casa estarão protegidos, incluindo TVs, consoles de jogos e alto-falantes inteligentes que não podem executar um bloqueador de anúncios.
updated: 2026-10-02
order: 4
---

Todo dispositivo na sua rede pede ao roteador qual servidor DNS usar. Configure o roteador para o Blokada Cloud, e anúncios e rastreadores serão bloqueados para tudo atrás dele. Isso inclui smart TVs, consoles de jogos, dispositivos de streaming e dispositivos de casa inteligente, que não possuem espaço para um aplicativo bloqueador de anúncios.

## O que seu roteador precisa

Seu roteador deve suportar **DNS criptografado com um nome de host**, ou seja, DNS over TLS (DoT) ou DNS over HTTPS (DoH). Muitos roteadores recentes oferecem esse suporte, incluindo os modelos abaixo. Dependendo do que seu roteador permite, será necessário inserir o nome DNS ou o link do DoH, ambos em _Seus detalhes_ acima.

<div class="note important">

**Apenas endereços IP simples?** Muitos roteadores de provedores de internet só aceitam endereços IP simples para DNS. Esse suporte está a caminho. Até lá, configure seus dispositivos individualmente: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [navegadores](../browser-dns-over-https/). Você também pode executar um pequeno encaminhador em um Raspberry Pi, conforme descrito no [guia do Pi-hole](../switch-from-pihole/).

</div>

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

Procure uma configuração chamada _DNS over TLS_, _DNS Privado_, _DNS Criptografado_ ou _DNS over HTTPS_. Insira o nome DNS do Blokada ou o link DoH indicado acima e remova todos os outros servidores DNS, inclusive servidores de contingência.

## Verifique se está funcionando

1. Reinicie um dispositivo ou desligue e ligue o Wi-Fi dele para que reconheça a mudança.
2. Navegue por um minuto e depois abra a página _Atividade_ no painel. As consultas da sua rede aparecerão lá.

## Se alguns dispositivos ainda exibirem anúncios

Alguns dispositivos ignoram o roteador: celulares com _DNS Privado_ ativado, navegadores com _DNS seguro_ configurado para outro provedor e dispositivos que usam DNS próprio. Configure esses no próprio dispositivo ou desative as opções de DNS deles.

<div class="note tip">

Atrás do roteador, todos os dispositivos compartilham um endereço, por isso o painel mostra sua rede como um único dispositivo. Configure celulares e notebooks com seus próprios nomes DNS do Blokada se quiser vê-los separadamente. Eles também permanecem protegidos quando saírem de casa.

</div>
