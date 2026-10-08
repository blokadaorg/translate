---
title: Bloqueie anúncios no Chrome, Firefox, Edge e Brave com DNS sobre HTTPS
description: Defina a Blokada Cloud como o provedor DNS seguro em seu navegador para bloquear anúncios e rastreadores, em qualquer computador, incluindo notebooks de trabalho onde não é possível instalar aplicativos.
updated: 2026-10-02
order: 7
---

Navegadores modernos podem usar seu próprio provedor DNS criptografado, chamado _DNS seguro_ ou _DNS sobre HTTPS_. Configure para a Blokada Cloud e o navegador bloqueará anúncios e rastreadores em qualquer rede, sem precisar instalar extensão.

Esta configuração cobre apenas este navegador. Para configurar em todo o computador, use o [perfil Apple](../apple-devices/) em um Mac, ou configure seu [roteador](../router-ad-blocking/).

## Chrome

1. Abra `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Digite {% doh %}

## Edge

1. Abra `edge://settings/privacy`.
2. Under _Security_, turn on _Use secure DNS to specify how to look up the network address for websites_.
3. Choose _Choose a service provider_ and enter {% doh %}

## Firefox

1. Open _Settings → Privacy & Security_ and scroll to _DNS over HTTPS_.
2. Choose _Max Protection_.
3. Under _Choose provider_, select _Custom_ and enter {% doh %}

## Brave

1. Abra `brave://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Digite {% doh %}

## Safari

O Safari não possui configuração de DNS seguro própria. Ele utiliza o DNS do sistema, então instale o [perfil Apple](../apple-devices/).

## Verifique se está funcionando

Navegue por um minuto, depois abra a página de _Atividade_ no [painel](https://app.blokada.org/stats?src=guides). As consultas deste navegador aparecem lá.

## Se algo não funcionar

<div class="note tip">

Se seu navegador for gerenciado pelo trabalho ou escola, a configuração de DNS seguro pode estar bloqueada. Peça ajuda ao administrador.

</div>
