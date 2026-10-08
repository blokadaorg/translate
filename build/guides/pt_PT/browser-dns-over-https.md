---
title: Bloqueie anúncios no Chrome, Firefox, Edge e Brave com DNS sobre HTTPS
description: Defina o Blokada Cloud como o provedor de DNS seguro no seu navegador para bloquear anúncios e rastreadores em qualquer computador, inclusive laptops de trabalho nos quais não é possível instalar aplicativos.
updated: 2026-10-02
order: 7},{
---

Navegadores modernos podem usar seu próprio provedor de DNS criptografado, chamado _DNS seguro_ ou _DNS sobre HTTPS_. Defina para Blokada Cloud e o navegador irá bloquear anúncios e rastreadores em qualquer rede, sem extensão para instalar.

Esta configuração cobre apenas este navegador. Para cobrir todo o computador, use o [perfil Apple](../apple-devices/) em um Mac, ou configure seu [roteador](../router-ad-blocking/).

## Chrome

1. Abra `chrome://settings/security`.
2. Turn on _Use secure DNS_, then choose _Add custom DNS service provider_.
3. Insira {% doh %}

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
3. Insira {% doh %}

## Safari

O Safari não possui configuração própria de DNS seguro. Ele usa o DNS do sistema, então instale o [perfil Apple](../apple-devices/).

## Verifique se está funcionando

Navegue por um minuto e abra a página _Atividade_ no [painel](https://app.blokada.org/stats?src=guides). As consultas deste navegador aparecerão lá.

## Se algo não funcionar

<div class="note tip">

Se seu navegador for gerenciado pelo trabalho ou escola, a configuração de DNS seguro pode estar bloqueada. Peça ao seu administrador.

</div>
