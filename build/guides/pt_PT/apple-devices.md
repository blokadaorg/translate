---
title: Bloqueie anúncios no Mac e na Apple TV com um perfil DNS do Blokada
description: Instale um perfil DNS do Blokada Cloud para bloquear anúncios e rastreadores em todo o sistema em um Mac ou Apple TV, com DNS criptografado e nada em execução em segundo plano.
updated: 2026-10-02
order: 6
---

Os dispositivos Apple podem usar DNS criptografado para todo o sistema por meio de um perfil de configuração. O perfil do Blokada aponta o dispositivo para o Blokada Cloud, que bloqueia anúncios e rastreadores em todos os aplicativos e navegadores.

Funciona no macOS 11 (Big Sur), tvOS 14, iOS e iPadOS 14 ou superior.

<div class="if-no-device">

Esta página ainda não reconhece seu dispositivo, por isso não pode oferecer o seu perfil. Faça login no painel, abra _Configuração_, escolha seu dispositivo e abra este guia com _Abrir em outro dispositivo_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Obter meu link de perfil</a></p>

</div>

## iPhone e iPad

A maneira mais fácil é pelo aplicativo. O [Blokada 6](https://go.blokada.org/appstore) faz toda a configuração para você, permite ativar e desativar o bloqueio com um toque e mostra o que foi bloqueado no próprio telefone. Faça login com seu ID de conta e pronto.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Obtenha o Blokada 6 na App Store</a></p>

### Sem o aplicativo

Você também pode instalar o perfil. iPhone e iPad só instalam perfis a partir do **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Esta página está aberta em outro navegador. Copie seu link e abra-o no Safari para continuar lá: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Abra as _Configurações_. Toque em _Perfil Baixado_ perto do topo. Você também pode encontrá-lo em _Geral → Gerenciamento de VPN e Dispositivos_.
3. Tap _Install_, enter your passcode, and confirm.

</div>

<p class="if-device if-safari">{% appleProfile %}Baixar meu perfil{% endappleProfile %}</p>

## Mac

1. Clique no botão abaixo para baixar o perfil.
2. Open the list of profiles: _System Settings → General → Device Management_ on macOS 15 and later, _System Settings → Privacy & Security → Profiles_ on macOS 13 and 14, or _System Preferences → Profiles_ on macOS 12 and earlier.
3. Double-click the Blokada profile and click _Install_.

<p class="if-device">{% appleProfile %}Baixar meu perfil{% endappleProfile %}</p>

## Apple TV

A Apple TV não pode abrir páginas da web, então você deve digitar o seu link de perfil nela.

1. Seu link de perfil: {% appleUrl %}
2. On the Apple TV, open _Settings → General → Privacy & Security_.
3. Realce _Compartilhar Análise da Apple TV_. Não selecione. Em vez disso, pressione o botão Reproduzir/Pausar no controle remoto.
4. Escolha _Adicionar Perfil_ e insira seu link de perfil. Digitar é mais fácil com o teclado do iPhone, onde você pode colar. Instale o perfil e confirme.

<div class="note aside">

**Apple TV e outros dispositivos em casa:** se você configurar o Blokada Cloud no seu [roteador](../router-ad-blocking/), a Apple TV também estará protegida, junto com todos os outros dispositivos.

</div>

## Verifique se está funcionando

Navegue por um minuto e depois abra a página _Atividade_ no [painel](https://app.blokada.org/stats?src=guides). As consultas deste dispositivo aparecerão lá.

Para remover o Blokada depois, exclua o perfil onde ele foi instalado.
