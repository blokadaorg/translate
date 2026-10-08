---
title: Bloqueie anúncios no Linux com DNS sobre TLS
description: Configure o systemd-resolved para usar o Blokada Cloud com DNS sobre TLS criptografado e bloqueie anúncios e rastreadores para todos os apps no seu computador Linux.
updated: 2026-10-02
order: 9
---

A maioria das distribuições Linux atuais, incluindo Ubuntu e Fedora, resolve nomes através do _systemd-resolved_, que suporta DNS sobre TLS. No Debian, instale primeiro com `sudo apt install systemd-resolved`. Aponte para o Blokada Cloud e anúncios e rastreadores serão bloqueados para todos os apps do computador.

## Configurar o systemd-resolved

1. Crie a pasta com `sudo mkdir -p /etc/systemd/resolved.conf.d`, depois o arquivo `/etc/systemd/resolved.conf.d/blokada.conf` com estas configurações:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>Reinicie o serviço: <code>sudo systemctl restart systemd-resolved</code></li>
<li>Verifique: <code>resolvectl status</code> exibe <code>+DNSOverTLS</code> e o servidor da Blokada.</li>
</ol>

A parte após o `#` é o seu nome DNS Blokada: {% dot %} o systemd-resolved verifica o certificado do servidor com base nele, e a Blokada o utiliza para saber qual dispositivo está solicitando.

<div class="note important">

O **NetworkManager** também repassa os servidores DNS da sua rede. `Domains=~.` envia todas as consultas para a Blokada, mas se o `resolvectl status` ainda exibir outro servidor em uma conexão, desative o DNS automático para essa conexão (o interruptor _Automático_ ao lado de _DNS_ nas configurações IPv4 e IPv6).

</div>

## Sem systemd-resolved

Se o `resolvectl` não for encontrado, sua distribuição resolve nomes de outra forma. Configure DNS seguro no seu navegador, como no [guia do navegador](../browser-dns-over-https/), ou configure seu [roteador](../router-ad-blocking/) para proteger toda a casa.

## Verifique se está funcionando

Abra alguns sites e depois acesse a página _Atividade_ no [painel de controle](https://app.blokada.org/stats?src=guides). As consultas deste computador aparecerão lá.

<div class="note aside">

Quer um VPN neste computador também? [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) inclui uma configuração WireGuard que criptografa todo o tráfego, com o mesmo bloqueio.

</div>
