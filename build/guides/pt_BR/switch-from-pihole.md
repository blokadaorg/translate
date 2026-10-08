---
title: Uma alternativa ao Pi-hole que não precisa de hardware
description: Mova o bloqueio de anúncios da sua casa de um Pi-hole para o Blokada Cloud, ou mantenha seu Pi-hole e envie as consultas dele pelo Blokada.
updated: 2026-10-02
order: 1
---

Um Pi-hole bloqueia anúncios para todos os dispositivos da sua rede, desde que o Raspberry Pi esteja ligado, atualizado e em casa. O Blokada Cloud faz o mesmo por nossos servidores:

- **Sem aparelho para manter.** Sem cartões SD, sem atualizações, sem interrupção quando o Pi desliga.
- **Funciona fora de casa.** Celulares e notebooks continuam bloqueando anúncios em dados móveis e outras redes Wi-Fi.
- **Criptografado.** Os dispositivos se comunicam com o Blokada via DNS sobre TLS ou DNS sobre HTTPS, então sua operadora não pode ler ou alterar suas consultas.
- **Um painel só.** Listas de bloqueio, domínios permitidos e bloqueados e atividade por dispositivo, em [app.blokada.org](https://app.blokada.org/?src=guides).

Há duas formas de trocar. Substitua o Pi-hole completamente ou mantenha-o e use o Blokada Cloud como upstream.

## Opção 1: substituir o Pi-hole

1. **Obtenha o Blokada Cloud** e abra o painel. Seu nome DNS e link DoH estão em _Setup_ lá, e em _Seus detalhes_ acima.
2. **Aponte seu roteador para o Blokada em vez do Pi-hole.** Siga o [guia do roteador](../router-ad-blocking/). Se o seu roteador só aceitar um endereço IP puro como servidor DNS, configure cada dispositivo manualmente: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [navegadores](../browser-dns-over-https/).
3. **Se seu Pi-hole era o servidor DHCP,** ative o DHCP no seu roteador _antes_ de desligar o Pi. Caso contrário, seus dispositivos deixarão de receber endereços de rede.
4. **Transfira suas listas.** No painel, escolha listas de bloqueio em _Blocklists_ e adicione seus próprios domínios permitidos ou bloqueados em _Exceptions_.
5. **Desligue o Pi-hole,** ou mantenha-o para outra finalidade.

<div class="note aside">

Seu Pi-hole mostrava cada dispositivo na rede pelo endereço IP. Com o Blokada, cada dispositivo aparece com seu próprio nome, desde que use o próprio nome DNS do Blokada. Um roteador configurado com um nome DNS Blokada mostra-se como um dispositivo só.

</div>

## Opção 2: manter o Pi-hole, usar o Blokada Cloud como upstream

Se quiser manter sua configuração local, como nomes de hosts locais, DHCP ou listas próprias, faça o Pi-hole encaminhar suas consultas para o Blokada por uma conexão criptografada. O Pi-hole não pode encaminhar criptografado por si só, então um pequeno encaminhador é executado ao lado dele. Este guia usa o [dnsproxy](https://github.com/AdguardTeam/dnsproxy), um encaminhador de código aberto em arquivo único.

1. Na máquina do Pi-hole, baixe o release do `dnsproxy` para sua CPU (`linux-arm64` para um Raspberry Pi recente) na página de releases, e copie o binário `dnsproxy` para `/usr/local/bin/`.
2. Crie `/etc/systemd/system/dnsproxy.service`:

<pre><code>[Unit]
Description=Encaminhador DNS criptografado para o Blokada Cloud
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/dnsproxy -l 127.0.0.1 -p 5054 -u tls://<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span> -b 9.9.9.9
Restart=always
DynamicUser=yes

[Install]
WantedBy=multi-user.target</code></pre>

3. Inicie: `sudo systemctl enable --now dnsproxy`
4. No admin do Pi-hole, abra _Settings → DNS_. Desmarque todos os servidores upstream e adicione `127.0.0.1#5054` como servidor upstream personalizado. Salve.
5. Confira a página _Atividade_ do painel. Consultas de sua rede agora aparecem lá.

Você pode desativar as próprias listas de bloqueio do Pi-hole e gerenciar o bloqueio no painel, ou manter ambos.

## Perguntas frequentes

**Preciso do Blokada Plus?** Não. O Blokada Cloud cobre o bloqueio de DNS para toda a sua casa. O [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) adiciona uma VPN por cima.

**E se o Blokada ficar inacessível?** Seus dispositivos não poderão resolver nomes até ele voltar, igual quando o Pi-hole cai. Não adicione um segundo servidor DNS sem filtro como reserva. A maioria dos dispositivos usa todos os servidores de forma aleatória, então anúncios podem passar.
