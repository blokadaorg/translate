---
title: Uma alternativa ao Pi-hole que não requer hardware
description: Transfira o bloqueio de anúncios da sua casa de um Pi-hole para o Blokada Cloud, ou mantenha o seu Pi-hole e envie as consultas dele pelo Blokada.
updated: 02-10-2026
order: 1​ (um)
---

Um Pi-hole bloqueia anúncios para todos os dispositivos na sua rede, desde que o Raspberry Pi esteja ligado, atualizado e em casa. O Blokada Cloud faz o mesmo trabalho a partir dos nossos servidores:

- **Sem caixa para manter.** Sem cartões SD, sem atualizações, sem interrupções quando o Pi cai.
- **Funciona fora de casa.** Celulares e laptops mantêm o bloqueio usando dados móveis e outras redes Wi-Fi.
- **Criptografado.** Os dispositivos se comunicam com o Blokada usando DNS sobre TLS ou DNS sobre HTTPS, assim seu provedor não pode ler ou alterar suas consultas.
- **Um único painel.** Listas de bloqueio, domínios permitidos e bloqueados, e atividade por dispositivo, em [app.blokada.org](https://app.blokada.org/?src=guides).

Há duas maneiras de trocar. Substitua o Pi-hole completamente ou mantenha-o usando o Blokada Cloud como upstream.

## Opção 1: substituir o Pi-hole

1. **Adquira o Blokada Cloud** e abra o painel. Seu nome DNS e o link DoH estão na seção _Configuração_ ali, e em _Seus detalhes_ acima.
2. **Aponte seu roteador para o Blokada em vez do Pi-hole.** Siga o [guia do roteador](../router-ad-blocking/). Se seu roteador só aceitar um endereço IP simples como servidor DNS, configure seus dispositivos individualmente: [Android](../android-private-dns/), [Mac e Apple TV](../apple-devices/), [Windows](../windows-dns-over-https/), [Linux](../linux-dns-over-tls/) e [navegadores](../browser-dns-over-https/).
3. **Se o seu Pi-hole era o servidor DHCP,** ative o DHCP no seu roteador _antes_ de desligar o Pi. Caso contrário, seus dispositivos deixarão de receber endereços de rede.
4. **Transfira suas listas.** No painel, escolha listas de bloqueio em _Blocklists_ e adicione seus próprios domínios permitidos ou bloqueados em _Exceções_.
5. **Desligue o Pi-hole,** ou mantenha-o para outra finalidade.

<div class="note aside">

Seu Pi-hole mostrava cada dispositivo na rede pelo endereço IP. Com o Blokada, cada dispositivo aparece com seu próprio nome, contanto que utilize seu próprio nome DNS do Blokada. Um roteador configurado com um único nome DNS do Blokada aparece como um único dispositivo.

</div>

## Opção 2: mantenha o Pi-hole, use o Blokada Cloud como upstream

Se quiser manter sua configuração local, como nomes de hosts locais, DHCP ou suas próprias listas, faça com que o Pi-hole encaminhe suas consultas ao Blokada por uma conexão criptografada. O Pi-hole não faz encaminhamento criptografado sozinho, então um pequeno encaminhador roda ao lado dele. Este guia usa o [dnsproxy](https://github.com/AdguardTeam/dnsproxy), um encaminhador open source que é um único arquivo.

1. Na máquina do Pi-hole, baixe a versão do `dnsproxy` para sua CPU (`linux-arm64` para um Raspberry Pi recente) na página de releases, e copie o binário `dnsproxy` para `/usr/local/bin/`.
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

3. Inicie com: `sudo systemctl enable --now dnsproxy`
4. No admin do Pi-hole, abra _Configurações → DNS_. Desmarque todos os servidores upstream e adicione `127.0.0.1#5054` como um servidor upstream personalizado. Salve.
5. Verifique a página _Atividade_ do painel. As consultas da sua rede agora aparecem ali.

Você pode desativar as próprias listas de bloqueio do Pi-hole e gerenciar o bloqueio pelo painel, ou manter ambos.

## Perguntas frequentes

**Preciso do Blokada Plus?** Não. O Blokada Cloud cobre o bloqueio DNS de toda sua casa. O [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) adiciona um VPN extra.

**E se o Blokada estiver inacessível?** Seus dispositivos não poderão resolver nomes até que ele volte, assim como quando o Pi-hole para. Não adicione um segundo servidor DNS sem filtro como reserva. A maioria dos dispositivos utiliza todos os servidores aleatoriamente, então os anúncios passariam.
