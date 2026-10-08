---
title: O DNS Mullvad será descontinuado. Mantenha o bloqueio de anúncios com o Blokada Cloud
description: A Mullvad encerrará seu DNS público em 2 de novembro de 2026. Veja como migrar seu telefone, computador e roteador para Blokada Cloud antes disso, sem perder o bloqueio de anúncios.
updated: 2026-10-02
order: 2
---

A Mullvad encerrará seu serviço DNS público e gratuito em **2 de novembro de 2026** e recomenda o Quad9 em seu lugar. O Quad9 bloqueia malware, mas **não** bloqueia anúncios nem rastreadores. Quando o DNS da Mullvad parar, dispositivos configurados para usá-lo deixarão de carregar sites e aplicativos. Se o dispositivo puder alternar para outro servidor DNS, os anúncios voltarão a aparecer. Altere antes dessa data.

Esta página trata dos nomes públicos de DNS terminados em `dns.mullvad.net`. Não abrange o app VPN da Mullvad.

## O que você usava e o que escolher na Blokada

| Nome do DNS Mullvad        | O que era bloqueado                       | No painel da Blokada                                                                                                                                          |
| -------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | nada                                      | A Blokada é um serviço de filtragem. Se você não quiser filtragem, o Quad9 ou o DNS do seu provedor é a escolha mais simples. |
| `adblock.dns.mullvad.net`  | anúncios, rastreadores                    | uma lista de bloqueio de anúncios e rastreadores                                                                                                              |
| `base.dns.mullvad.net`     | anúncios, rastreadores, malware           | adicionar uma lista de malware                                                                                                                                |
| `extended.dns.mullvad.net` | base mais redes sociais                   | adicionar uma lista de redes sociais                                                                                                                          |
| `family.dns.mullvad.net`   | base mais conteúdo adulto e jogos de azar | adicionar listas de conteúdo adulto e jogos de azar                                                                                                           |
| `all.dns.mullvad.net`      | todos os anteriores                       | ative todos eles                                                                                                                                              |

Você escolhe listas de bloqueio no painel, em _Listas de bloqueio_. Você pode alterá-las a qualquer momento e a mudança valerá para todos os seus dispositivos.

## Altere cada dispositivo

A Blokada atribui um nome único para cada dispositivo, assim o painel pode mostrar a atividade por dispositivo. Dependendo do aparelho, você precisará do seu nome DNS ou do link DoH, ambos em _Seus dados_ acima.

### Android

O guia da Mullvad pedia para inserir um hostname em _DNS Privado_. Substitua pelo seu nome DNS da Blokada. O [guia Android](../android-private-dns/) mostra o passo a passo.

### iPhone, iPad e Mac

A configuração da Mullvad usava um perfil de configuração. Remova-o primeiro:

- **iPhone e iPad:** _Ajustes → Geral → VPN e Gerenciamento de Dispositivo_, toque no perfil DNS Mullvad e, em seguida, _Remover Perfil_.
- **Mac:** abra a lista de perfis (_Ajustes do Sistema → Geral → Gerenciamento de Dispositivo_ no macOS 15 e posterior, _Ajustes do Sistema → Privacidade e Segurança → Perfis_ no macOS 13 e 14, _Preferências do Sistema → Perfis_ no macOS 12 e anterior), selecione o perfil DNS Mullvad e clique em _−_.

Em seguida, instale o perfil da Blokada pelo [guia Apple](../apple-devices/).

### Navegadores

Se você inseriu um link DoH da Mullvad como `https://adblock.dns.mullvad.net/dns-query` em _DNS seguro_ ou _DNS sobre HTTPS_, substitua pelo seu link DoH. O [guia de navegadores](../browser-dns-over-https/) traz o passo a passo para cada navegador.

### Roteador

Se seu roteador usa Mullvad por DNS sobre TLS, substitua o hostname da Mullvad pelo seu nome DNS da Blokada e remova os endereços IP da Mullvad. O [guia de roteadores](../router-ad-blocking/) cobre os modelos mais comuns.

## Verifique se está funcionando

Abra alguns sites e depois acesse a página _Atividade_ no painel. Lá você verá as pesquisas feitas pelos seus dispositivos, com as bloqueadas marcadas. Se algum dispositivo não aparecer, ele ainda está usando outro servidor DNS.
