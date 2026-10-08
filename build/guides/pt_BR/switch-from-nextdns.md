---
title: Uma alternativa ao NextDNS com a mesma configuração em todos os dispositivos
description: Mude do NextDNS para o Blokada Cloud. Troque seu nome DNS, link DoH ou perfil do NextDNS pelo do Blokada no seu celular, computador e roteador, e mantenha o bloqueio de anúncios.
updated: 2026-10-02
order: 3
---

NextDNS e Blokada Cloud funcionam da mesma forma: um serviço de DNS criptografado que bloqueia anúncios e rastreadores por nome, com suas próprias configurações atrás de um nome DNS pessoal. Trocar significa substituir os valores do NextDNS em cada dispositivo pelos seus do Blokada. Nada mais no dispositivo é alterado.

## O que você usava e o que escolher no Blokada

| No NextDNS                                                            | No Blokada Cloud                                                   |
| --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Seu ID de configuração, ex.: `abc123` | Sua tag de dispositivo, parte do nome DNS do Blokada e do link DoH |
| Listas de bloqueio de _Privacidade_                                   | _Listas de bloqueio_ no painel                                     |
| _Segurança_ (malware, phishing)                    | uma lista de malware em _Listas de bloqueio_                       |
| _Controle parental_                                                   | listas de conteúdo adulto e apostas em _Listas de bloqueio_        |
| _Lista de permissões_ e _Lista de negação_                            | _Exceções_ no painel                                               |
| _Registros_ e _Análises_                                              | _Atividade_ e _Estatísticas_ no painel                             |

## Troque cada dispositivo

Dependendo do dispositivo, você precisa do seu nome DNS ou do seu link DoH, ambos estão em _Suas informações_ acima.

### Android

Se você usou _DNS Privado_ com `<your-id>.dns.nextdns.io`, substitua pelo nome DNS do Blokada, conforme explica o [guia para Android](../android-private-dns/). Se você usou o aplicativo NextDNS, desinstale-o e instale o [Blokada 6](https://go.blokada.org/play_cloud) em seu lugar.

### iPhone e iPad

Se você usou o aplicativo NextDNS, desinstale-o e instale o [Blokada 6](https://go.blokada.org/appstore). Se você instalou um perfil do NextDNS, remova em _Ajustes → Geral → VPN e Gerenciamento do Dispositivo_, depois siga o [guia da Apple](../apple-devices/).

### Mac e Apple TV

Remova o perfil ou aplicativo NextDNS, depois instale o perfil Blokada seguindo o [guia da Apple](../apple-devices/).

### Windows e Linux

Desinstale o aplicativo NextDNS se usar. No Windows, substitua o servidor NextDNS e o template DoH pelo do Blokada, conforme o [guia do Windows](../windows-dns-over-https/). No Linux, substitua o servidor NextDNS no systemd-resolved, conforme o [guia do Linux](../linux-dns-over-tls/).

### Navegadores

Se você definiu `https://dns.nextdns.io/…` como _DNS seguro_ do seu navegador, substitua pelo seu link DoH, conforme mostrado no [guia do navegador](../browser-dns-over-https/).

### Roteador

Se seu roteador usa NextDNS por DNS sobre TLS ou DNS sobre HTTPS, substitua o nome ou link do NextDNS pelo do Blokada, conforme o [guia do roteador](../router-ad-blocking/).

Se usar NextDNS por endereços IP comuns com um _IP vinculado_, o Blokada ainda não consegue assumir isso. O suporte a roteadores com endereços DNS simples está a caminho. Até lá, configure seus dispositivos um a um, ou use um roteador que suporte DNS criptografado.

## Verifique se está funcionando

Abra alguns sites, depois olhe a página _Atividade_ no painel. Você verá as consultas dos seus dispositivos lá, com as bloqueadas marcadas. Se um dispositivo não aparecer, ele ainda está usando o NextDNS.
