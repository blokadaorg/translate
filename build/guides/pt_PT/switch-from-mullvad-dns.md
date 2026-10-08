---
title: O Mullvad DNS será descontinuado. Mantenha o bloqueio de anúncios com o Blokada Cloud
description: O Mullvad encerrará seu DNS público em 2 de novembro de 2026. Veja como migrar seu telefone, computador e roteador para o Blokada Cloud antes dessa data, sem perder o bloqueio de anúncios.
updated: 2026-10-02
order: 2
---

O Mullvad está encerrando seu serviço gratuito de DNS público em **2 de novembro de 2026** e recomenda o Quad9 como alternativa. O Quad9 bloqueia malware, mas **não** bloqueia anúncios ou rastreadores. Quando o DNS do Mullvad parar, os dispositivos configurados para ele deixarão de carregar sites e apps. Onde o dispositivo puder usar outro servidor DNS como alternativa, os anúncios voltarão a aparecer. Troque antes dessa data.

Esta página se refere aos nomes públicos de DNS terminados em `dns.mullvad.net`. Não cobre o app VPN do Mullvad.

## O que você usava e o que escolher no Blokada

| Nome do DNS do Mullvad     | O que bloqueava                           | No painel do Blokada                                                                                                                                        |
| -------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dns.mullvad.net`          | nada                                      | O Blokada é um serviço de filtragem. Se você não quiser filtragem, o Quad9 ou o DNS do seu provedor é a opção mais simples. |
| `adblock.dns.mullvad.net`  | anúncios, rastreadores                    | uma blocklist de anúncios e rastreadores                                                                                                                    |
| `base.dns.mullvad.net`     | anúncios, rastreadores, malware           | adicione uma lista de malware                                                                                                                               |
| `extended.dns.mullvad.net` | base mais redes sociais                   | adicione uma lista de redes sociais                                                                                                                         |
| `family.dns.mullvad.net`   | base mais conteúdo adulto e jogos de azar | adicione listas de conteúdo adulto e jogos de azar                                                                                                          |
| `all.dns.mullvad.net`      | todos os acima                            | ative todos eles                                                                                                                                            |

Você escolhe as blocklists no painel, em _Blocklists_. Você pode alterá-las a qualquer momento, e a mudança será aplicada a todos os seus dispositivos.

## Troque cada dispositivo

O Blokada dá a cada dispositivo um nome, assim o painel pode mostrar a atividade de cada dispositivo. Dependendo do dispositivo, você precisará do seu nome DNS ou do seu link DoH, ambos em _Seus dados_ acima.

### Android

O guia do Mullvad fazia você colocar um hostname em _DNS Privado_. Substitua pelo seu nome DNS do Blokada. O [guia Android](../android-private-dns/) mostra os passos.

### iPhone, iPad e Mac

A configuração do Mullvad usava um perfil. Remova-o primeiro:

- **iPhone e iPad:** _Ajustes → Geral → VPN e Gerenciamento de Dispositivo_, toque no perfil DNS do Mullvad e depois em _Remover Perfil_.
- **Mac:** abra a lista de perfis (_Ajustes do Sistema → Geral → Gerenciamento de Dispositivo_ no macOS 15 e posteriores, _Ajustes do Sistema → Privacidade e Segurança → Perfis_ no macOS 13 e 14, _Preferências do Sistema → Perfis_ no macOS 12 e anteriores), selecione o perfil DNS do Mullvad e clique em _−_.

Em seguida, instale o perfil do Blokada pelo [guia da Apple](../apple-devices/).

### Navegadores

Se você inseriu um link DoH do Mullvad como `https://adblock.dns.mullvad.net/dns-query` em _DNS seguro_ ou _DNS sobre HTTPS_, substitua pelo seu link DoH. O [guia para navegadores](../browser-dns-over-https/) mostra os passos para cada navegador.

### Roteador

Se o seu roteador usa Mullvad via DNS over TLS, troque o hostname do Mullvad pelo seu nome DNS do Blokada e remova os endereços IP do Mullvad. O [guia de roteadores](../router-ad-blocking/) cobre modelos comuns.

## Verifique se está funcionando

Abra alguns sites e então veja a página _Atividade_ no painel. Lá você verá as consultas dos seus dispositivos, com os bloqueios marcados. Se um dispositivo não aparecer, ainda está usando outro servidor DNS.
