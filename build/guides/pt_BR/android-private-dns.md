---
title: Configurar DNS Privado no Android com o Blokada Cloud
description: Use a configuração de DNS Privado embutida do Android com o Blokada Cloud para bloquear anúncios e rastreadores em todos os apps, no Wi-Fi e dados móveis. Ou deixe que o app Blokada 6 faça isso.
updated: 02/10/2026
order: 5
---

## A maneira mais fácil: o app

O [Blokada 6](https://go.blokada.org/play_cloud) configura tudo para você, permite ativar e desativar o bloqueio com um toque e mostra o que foi bloqueado no próprio telefone. Faça login com seu ID de conta e pronto.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Baixe o Blokada 6 no Google Play</a></p>

## Sem o app: DNS Privado

O Android 9 e versões posteriores possuem uma configuração de _DNS Privado_. Defina para Blokada Cloud, e anúncios e rastreadores serão bloqueados em todos os apps, em todas as redes, sem nada rodando em segundo plano.

1. Abra _Configurações → Rede e internet_. Em alguns celulares isso é _Conexões_ ou _Conexão e compartilhamento_.
2. Toque em _DNS Privado_. Em celulares Samsung está em _Mais configurações de conexão_.
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

Se não conseguir encontrar, procure por "DNS Privado" no app de Configurações.

## Verifique se está funcionando

Abra alguns apps ou sites e então veja a página de _Atividade_ no [painel](https://app.blokada.org/stats?src=guides). As consultas deste telefone aparecerão lá.

## Se algo não funcionar

- **"Não foi possível conectar" ou sem internet:** verifique se o nome DNS do seu Blokada está correto. Ele deve ser exatamente como mostrado acima, sem `https://`.
- **Outro app de VPN está ativo:** alguns apps de VPN usam seu próprio DNS e ignoram o DNS Privado. Desative o DNS ou o bloqueio de anúncios da VPN, ou use o Blokada 6.
- **O Chrome ainda mostra anúncios:** o Chrome pode estar configurado para usar seu próprio provedor de DNS seguro, o que ignora o DNS Privado. No Chrome, abra _Configurações → Privacidade e segurança → Usar DNS seguro_ e escolha _Usar o provedor de serviço atual_. Assim, o Chrome seguirá o DNS Privado.
