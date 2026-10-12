---
title: Bloqueie anúncios em toda a rede com o bloqueio de anúncios no roteador.
description: Configure o Blokada Cloud em seu roteador uma vez e todos os dispositivos em casa estarão protegidos, incluindo TVs, consoles de jogos e alto-falantes inteligentes que não podem executar um bloqueador de anúncios.
updated: 09-10-2026
order: 4
---

Cada dispositivo na sua rede consulta o roteador para saber qual servidor DNS usar. Aponte o roteador para o Blokada Cloud e anúncios e rastreadores serão bloqueados para tudo atrás dele. Isso inclui smart TVs, consoles de jogos, sticks de streaming e dispositivos de casa inteligente, que não têm espaço para um aplicativo de bloqueador de anúncios.

## O que seu roteador precisa

Há duas maneiras de configurar um roteador:

- **DNS criptografado com um nome de host**, ou seja, DNS sobre TLS (DoT) ou DNS sobre HTTPS (DoH). Muitos roteadores recentes oferecem suporte a isso, incluindo os modelos abaixo. Dependendo do que seu roteador suporta, você precisará do seu nome de DNS ou do seu link DoH, ambos disponíveis em _Seus detalhes_ acima.
- **Um endereço DNS IPv6 simples.** Muitos roteadores de provedores de internet só aceitam endereços IP simples para DNS. Se o seu for assim e sua conexão tiver IPv6, a Blokada fornecerá um endereço IPv6 para inserir. Veja [Roteadores que só aceitam um endereço IP](#routers-that-only-take-an-ip-address).

Use DNS criptografado se o seu roteador oferecer suporte. As consultas permanecerão privadas no caminho até a Blokada.

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

Procure por uma configuração chamada _DNS sobre TLS_, _DNS Privado_, _DNS Criptografado_ ou _DNS sobre HTTPS_. Digite o nome do seu Blokada DNS ou o link DoH fornecido acima e remova todos os outros servidores DNS, incluindo servidores de fallback. Se não houver tal configuração, utilize um endereço IPv6 simples conforme mostrado abaixo.

## Roteadores que aceitam apenas um endereço IP

Seu roteador e sua conexão com a internet precisam de IPv6 para isso. O suporte para endereços IPv4 simples será adicionado futuramente.

1. No [dashboard](https://app.blokada.org/setup?src=guides), abra _Configuração_ e escolha _Roteador, TV, console de jogos_.
2. Dê um nome para o roteador, por exemplo _Roteador de casa_, e selecione _Obter endereço_. O nome será exibido na sua atividade e não poderá ser alterado depois.
3. Nas configurações do roteador, localize os servidores DNS para IPv6, geralmente em _Internet_, _WAN_ ou _IPv6_, e informe o endereço como único servidor DNS.
4. **Remova todos os outros servidores DNS, inclusive os de IPv4.** Dispositivos que ainda recebam um servidor DNS IPv4 do roteador enviarão algumas consultas sem passar pelo Blokada. Se o roteador não permitir deixar DNS IPv4 em branco, configure seus dispositivos um por um: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [navegadores](../browser-dns-over-https/).

A mesma configuração funciona para uma TV ou console de jogos que permita inserir manualmente um servidor DNS. Atribua um endereço diferente para cada um, assim eles aparecerão identificados por nome na sua atividade.

<div class="note aside">

Essas consultas são enviadas sem criptografia para o Blokada, como em qualquer servidor DNS comum. Se o seu roteador oferecer suporte a DNS sobre TLS ou DNS sobre HTTPS, prefira essa opção.

</div>

## Verifique se está funcionando

1. Reinicie um dispositivo ou desligue e ligue o Wi-Fi para que ele reconheça a alteração.
2. Nesse dispositivo, desligue o Blokada se ele estiver ativo e acesse [go.blokada.org/test](https://go.blokada.org/test). O site informará se seu DNS está passando pelo Blokada.
3. Navegue por um minuto e, em seguida, acesse a página _Atividade_ no [dashboard](https://app.blokada.org/stats?src=guides). As consultas da sua rede aparecerão lá.

## Se alguns dispositivos ainda exibirem anúncios

Alguns dispositivos ignoram o roteador: celulares com _DNS Privado_ ativado, navegadores com _DNS seguro_ definido para outro provedor e dispositivos que definem seu próprio DNS de forma fixa. Configure-os diretamente no dispositivo ou desative a configuração própria de DNS.

<div class="note tip">

Atrás do roteador, todos os dispositivos compartilham um endereço, portanto o painel mostra sua rede como um único dispositivo. Configure celulares e notebooks com seu próprio nome DNS do Blokada se quiser vê-los separadamente. Eles também mantêm o bloqueio ao sair de casa.

</div>
