---
title: Bloqueie anúncios no Windows com DNS sobre HTTPS
description: Use o DNS criptografado integrado ao Windows 11 com o Blokada Cloud para bloquear anúncios e rastreadores em todos os aplicativos e navegadores, sem precisar instalar nenhum software.
updated: 2026-10-02
order: 8
---

O Windows 11 pode enviar todas as suas consultas DNS de forma criptografada, usando DNS sobre HTTPS. Basta apontá-lo para o Blokada Cloud, e anúncios e rastreadores serão bloqueados em todos os aplicativos e navegadores do computador, sem necessidade de instalação.

Você precisa do endereço IP do servidor DNS e do seu link DoH, ambos em _Seus dados_ acima.

## Windows 11

1. Abra _Configurações → Rede e Internet_, então _Wi-Fi_ ou _Ethernet_, dependendo de como o computador está conectado.
2. Abra as _Propriedades de hardware_ da sua conexão. Para Wi-Fi, selecione _Gerenciar redes conhecidas_ e depois a rede, ou _Propriedades de hardware_ no topo da página de Wi-Fi.
3. Ao lado de _Atribuição do servidor DNS_, selecione _Editar_. Escolha _Manual_ e ative _IPv4_.
4. Em _DNS preferencial_, insira o servidor DNS {% ip "doh" %}
5. Defina _DNS sobre HTTPS_ como _Ativado (modelo manual)_ e cole seu link DoH {% doh %} como o _modelo DoH_.
6. Desative _Alternar para texto simples_ e selecione _Salvar_.

Se o computador usar tanto Wi-Fi quanto Ethernet, repita isso para a outra conexão.

<div class="note important">

Deixe _DNS alternativo_ em branco. O Windows usa ambos os servidores, e qualquer outro permite a passagem de anúncios.

</div>

<div class="note tip">

Sem opção _Ativado (modelo manual)_? Seu Windows 11 é antigo. Atualize o Windows ou use o [guia do navegador](../browser-dns-over-https/) enquanto isso.

</div>

## Windows 10

O Windows 10 não possui DNS criptografado integrado. Configure o DNS seguro em seu navegador, conforme o [guia do navegador](../browser-dns-over-https/), ou configure seu [roteador](../router-ad-blocking/) para proteger toda a casa.

## Verifique se está funcionando

Abra alguns sites e depois veja a página _Atividade_ no [painel](https://app.blokada.org/stats?src=guides). As consultas deste computador aparecerão lá.

<div class="note aside">

Também quer uma VPN neste computador? O [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) inclui uma configuração do WireGuard que criptografa todo o tráfego, com o mesmo bloqueio.

</div>

## Se algo não funcionar

Chrome e Edge possuem suas próprias configurações de _DNS seguro_, que ignoram o Windows. Se estiver em automático, pode voltar ao DNS comum, que o Blokada recusa. Defina para o seu link DoH:

- **Chrome:** abra `chrome://settings/security`, ative _Usar DNS seguro_ e, em _Selecionar provedor de DNS_, escolha _Adicionar provedor de serviço DNS personalizado_.
- **Edge:** abra `edge://settings/privacy`, ative o DNS seguro e escolha _Escolher um provedor de serviço_.

Em seguida, cole seu link DoH {% doh %}

Se ainda aparecerem alguns anúncios em uma rede com IPv6, o Windows pode estar consultando também o servidor DNS IPv6 do seu roteador. Desative _Protocolo de Internet Versão 6 (TCP/IPv6)_ nas propriedades do adaptador (_Painel de Controle → Conexões de Rede_) ou configure o seu [roteador](../router-ad-blocking/).
