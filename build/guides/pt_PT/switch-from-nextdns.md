---
title: Uma alternativa ao NextDNS com a mesma configuração em todos os dispositivos
description: Mude do NextDNS para o Blokada Cloud. Troque seu nome DNS, link DoH ou perfil do NextDNS para o da Blokada no seu celular, computador e roteador, e mantenha o bloqueio de anúncios.
updated: 2026-10-02
order: 3
---

NextDNS e Blokada Cloud funcionam do mesmo jeito: um serviço DNS criptografado que bloqueia anúncios e rastreadores por nome, com suas próprias configurações protegidas por um nome DNS pessoal. Trocar significa substituir os valores do NextDNS em cada dispositivo pelos da Blokada. Nada mais muda no dispositivo.

## O que você usava e o que escolher no Blokada

| No NextDNS                                         | No Blokada Cloud                                                    |
| -------------------------------------------------- | ------------------------------------------------------------------- |
| Seu ID de configuração, por exemplo, `abc123`      | Sua tag de dispositivo, parte do seu nome DNS da Blokada e link DoH |
| blocklists de _privacidade_                        | _Blocklists_ no painel                                              |
| _Segurança_ (malware, phishing) | uma lista de malware em _Blocklists_                                |
| _Controle parental_                                | listas de conteúdo adulto e jogos de azar em _Blocklists_           |
| _Allowlist_ e _Denylist_                           | _Exceções_ no painel                                                |
| _Logs_ e _Analytics_                               | _Atividade_ e _Estatísticas_ no painel                              |

## Troque cada dispositivo

Dependendo do dispositivo, você precisa do seu nome DNS ou do seu link DoH, ambos em _Seus detalhes_ acima.

### Android

Se você usou _DNS privado_ com `<your-id>.dns.nextdns.io`, substitua pelo seu nome DNS da Blokada, conforme mostrado no [guia para Android](../android-private-dns/). Se você usou o app NextDNS, desinstale-o e instale o [Blokada 6](https://go.blokada.org/play_cloud) em vez disso.

### iPhone e iPad

Se você usou o aplicativo NextDNS, desinstale-o e instale o [Blokada 6](https://go.blokada.org/appstore). Se você instalou um perfil NextDNS, remova-o em _Ajustes → Geral → Gerenciamento de VPN e Dispositivos_, depois siga o [guia Apple](../apple-devices/).

### Mac e Apple TV

Remova o perfil ou o aplicativo NextDNS, depois instale o perfil da Blokada pelo [guia Apple](../apple-devices/).

### Windows e Linux

Desinstale o aplicativo NextDNS caso o utilize. No Windows, substitua o servidor NextDNS e o modelo DoH pelo da Blokada, como indicado no [guia Windows](../windows-dns-over-https/). No Linux, substitua o servidor NextDNS no systemd-resolved, como no [guia Linux](../linux-dns-over-tls/).

### Navegadores

Se você configurou `https://dns.nextdns.io/…` como _DNS seguro_ do seu navegador, substitua pelo seu link DoH, como explicado no [guia para navegadores](../browser-dns-over-https/).

### Roteador

Se seu roteador usa NextDNS sobre DNS over TLS ou DNS over HTTPS, substitua o nome ou link NextDNS pelo da Blokada, conforme o [guia para roteadores](../router-ad-blocking/).

Se ele usar NextDNS via endereços IP simples com _IP vinculado_, a Blokada ainda não pode assumir essa configuração. O suporte para roteadores com endereços DNS simples está a caminho. Até lá, configure seus dispositivos um a um, ou use um roteador que suporte DNS criptografado.

## Verifique se está funcionando

Abra alguns sites e depois acesse a página de _Atividade_ no painel. Você verá as consultas dos seus dispositivos lá, com as bloqueadas marcadas. Se um dispositivo não aparecer, ele ainda está usando o NextDNS.
