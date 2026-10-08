---
title: Bloqueie anúncios em toda a rede com o bloqueio de anúncios no roteador.
description: Configure o Blokada Cloud em seu roteador uma vez e todos os dispositivos em casa estarão protegidos, incluindo TVs, consoles de jogos e alto-falantes inteligentes que não podem executar um bloqueador de anúncios.
updated: 2026-10-02
order: 4
---

Cada dispositivo na sua rede consulta o roteador para saber qual servidor DNS usar. Aponte o roteador para o Blokada Cloud e anúncios e rastreadores serão bloqueados para tudo atrás dele. Isso inclui smart TVs, consoles de jogos, sticks de streaming e dispositivos de casa inteligente, que não têm espaço para um aplicativo de bloqueador de anúncios.

## O que seu roteador precisa

Seu roteador deve suportar **DNS criptografado com nome de host**, ou seja, DNS sobre TLS (DoT) ou DNS sobre HTTPS (DoH). Muitos roteadores recentes oferecem esse suporte, incluindo os modelos abaixo. Dependendo do que seu roteador suporta, você precisará do seu nome DNS ou do seu link DoH, ambos na seção _Seus dados_ acima.

<div class="note important">

**Apenas endereços IP simples?** Muitos roteadores fornecidos por operadoras aceitam apenas endereços IP simples para DNS. O suporte para esses casos está a caminho. Até lá, configure seus dispositivos individualmente: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [navegadores](../browser-dns-over-https/). Você também pode executar um pequeno encaminhador em um Raspberry Pi, conforme descrito no [guia do Pi-hole](../switch-from-pihole/).

</div>

## FRITZ!Box

FRITZ!OS 7.20 ou superior.

1. Open `http://fritz.box` and go to _Internet → Account Information → DNS Server_.
2. Under _Encrypted Name Resolution on the Internet (DNS over TLS)_, tick _Use encrypted name resolution_.
3. Em _Nomes Resolvidos do Servidor DNS_, insira apenas {% dot %}. **Remova todas as outras entradas.** O FRITZ!Box usa todos os resolvedores listados e qualquer outro permite a exibição de anúncios.
4. Tick _Enforce certificate verification for encrypted name resolution_.
5. Se você vir _Failover para servidores DNS públicos quando houver interrupção no DNS_, desative essa opção.
6. Click _Apply_.

## ASUS

Recent ASUS firmware (3.0.0.4.388 or later) and Asuswrt-Merlin.

1. Open the router admin page and go to _WAN → Internet Connection_.
2. Under _WAN DNS Setting_, set _DNS Privacy Protocol_ to _DNS-over-TLS (DoT)_ and _DNS-over-TLS Profile_ to _Strict_.
3. Remove every entry from the _DNS-over-TLS Server List_, then add one:
   - Endereço: {% ip "dot" %}
   - Nome do host TLS: {% dot %}
4. Click _Apply_.

## OpenWrt

1. In _System → Software_, update the lists and install `luci-app-https-dns-proxy`.
2. Abra _Serviços → HTTPS DNS Proxy_. Exclua as instâncias de outros provedores.
3. Adicione uma instância com uma URL de resolvedor personalizada: {% doh %}
4. _Salvar & Aplicar_. O pacote aponta o dnsmasq para isso automaticamente.

## Outros roteadores

Procure uma configuração chamada _DNS sobre TLS_, _DNS Privado_, _DNS Criptografado_ ou _DNS sobre HTTPS_. Insira o nome DNS do seu Blokada ou o link DoH acima, e remova todos os outros servidores DNS, incluindo servidores de fallback.

## Verifique se está funcionando

1. Reinicie um dispositivo ou desligue e ligue o Wi-Fi para que ele reconheça a alteração.
2. Navegue por um minuto, depois abra a página _Atividade_ no painel. As buscas da sua rede aparecerão lá.

## Se alguns dispositivos ainda exibirem anúncios

Alguns dispositivos ignoram o roteador: celulares com _DNS Privado_ ativado, navegadores com _DNS seguro_ definido para outro provedor e dispositivos que definem seu próprio DNS de forma fixa. Configure-os diretamente no dispositivo ou desative a configuração própria de DNS.

<div class="note tip">

Atrás do roteador, todos os dispositivos compartilham um endereço, portanto o painel mostra sua rede como um único dispositivo. Configure celulares e notebooks com seu próprio nome DNS do Blokada se quiser vê-los separadamente. Eles também mantêm o bloqueio ao sair de casa.

</div>
