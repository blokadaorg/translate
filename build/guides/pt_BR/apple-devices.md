---
title: Bloqueie anúncios no Mac e na Apple TV com um perfil de DNS do Blokada
description: Instale um perfil de DNS do Blokada Cloud para bloquear anúncios e rastreadores em todo o sistema no Mac ou Apple TV, com DNS criptografado e nada em execução em segundo plano.
updated: 2026-10-02
order: 6
---

Dispositivos Apple podem usar DNS criptografado em todo o sistema através de um perfil de configuração. O perfil do Blokada direciona o dispositivo para o Blokada Cloud, que bloqueia anúncios e rastreadores em todos os aplicativos e navegadores.

Funciona no macOS 11 (Big Sur), tvOS 14, iOS e iPadOS 14 e posteriores.

<div class="if-no-device">

Esta página ainda não reconhece seu dispositivo, por isso não pode oferecer seu perfil. Faça login no painel, abra _Configurar_, escolha seu dispositivo e abra este guia com _Abrir em outro dispositivo_.

<p><a class="btn btn-outline" href="https://app.blokada.org/setup?src=guides">Obter meu link de perfil</a></p>

</div>

## iPhone e iPad

A maneira mais fácil é pelo aplicativo. [Blokada 6](https://go.blokada.org/appstore) faz toda a configuração para você, ativa e desativa o bloqueio com um toque e mostra o que foi bloqueado no próprio telefone. Entre com a sua ID de conta e pronto.

<p><a class="btn btn-primary" href="https://go.blokada.org/appstore">Baixe o Blokada 6 na App Store</a></p>

### Sem o aplicativo

Você também pode instalar o perfil. iPhone e iPad instalam perfis somente pelo **Safari**.

<div class="if-device">
<div class="if-other-browser note important">

Esta página está aberta em outro navegador. Copie seu link e abra-o no Safari para continuar lá: {% pageLink %}

</div>
</div>

<div class="if-safari">

1. In Safari, tap the button below, then _Allow_ to download the profile.
2. Abra as _Ajustes_. Toque em _Perfil Baixado_ no topo. Você também pode encontrá-lo em _Geral → Gerenciamento de VPN e Dispositivo_.
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
3. Selecione _Compartilhar análises da Apple TV_. Não selecione a opção. Em vez disso, pressione o botão Reproduzir/Pausar no controle remoto.
4. Escolha _Adicionar Perfil_ e digite seu link de perfil. É mais fácil digitar usando o teclado do iPhone, onde você pode colar. Instale o perfil e confirme.

<div class="note aside">

**Apple TV e outros dispositivos em casa:** se você configurar o Blokada Cloud no seu [roteador](../router-ad-blocking/), a Apple TV estará coberta junto com todos os outros dispositivos.

</div>

## Verifique se está funcionando

Navegue por um minuto, depois abra a página de _Atividade_ no [painel](https://app.blokada.org/stats?src=guides). As pesquisas deste dispositivo aparecerão lá.

Para remover o Blokada depois, exclua o perfil onde você o instalou.
