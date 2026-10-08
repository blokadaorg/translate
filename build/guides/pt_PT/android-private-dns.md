---
title: Configure o DNS Privado no Android com o Blokada Cloud
description: Use a opção de DNS Privado nativa do Android com o Blokada Cloud para bloquear anúncios e rastreadores em todos os apps, tanto no Wi-Fi quanto nos dados móveis. Ou deixe o app Blokada 6 fazer isso para você.
updated: 02-10-2026
order: 5
---

## O jeito mais fácil: o app

O [Blokada 6](https://go.blokada.org/play_cloud) configura tudo para você, ativa e desativa o bloqueio com um toque e mostra o que foi bloqueado diretamente no celular. Acesse com seu ID de conta e pronto.

<p><a class="btn btn-primary" href="https://go.blokada.org/play_cloud">Obtenha o Blokada 6 no Google Play</a></p>

## Sem o app: DNS Privado

O Android 9 e versões posteriores têm uma configuração de _DNS Privado_. Defina para Blokada Cloud e anúncios e rastreadores serão bloqueados em todos os apps, em todas as redes, sem nada rodando em segundo plano.

1. Abra _Configurações → Rede e internet_. Em alguns aparelhos, é _Conexões_ ou _Conexão e compartilhamento_.
2. Toque em _DNS Privado_. Nos aparelhos Samsung, está em _Mais configurações de conexão_.
3. Choose _Private DNS provider hostname_.
4. Enter your Blokada DNS name {% dot %} and tap _Save_.

Se não conseguir encontrar, pesquise por "DNS Privado" no app de configurações.

## Verifique se está funcionando

Abra alguns apps ou sites e depois acesse a página _Atividade_ no [painel](https://app.blokada.org/stats?src=guides). As consultas deste celular aparecerão lá.

## Se algo não funcionar

- **"Não foi possível conectar" ou sem internet:** verifique se o nome DNS do seu Blokada está correto. Ele deve ser exatamente como mostrado acima, sem `https://`.
- **Outro app de VPN está ativo:** alguns apps de VPN usam seu próprio DNS e ignoram o DNS Privado. Desative a opção de DNS ou bloqueio de anúncios da VPN, ou utilize o Blokada 6.
- **O Chrome ainda mostra anúncios:** O Chrome pode estar configurado para usar seu próprio provedor de DNS seguro, o que ignora o DNS Privado. No Chrome, abra _Configurações → Privacidade e segurança → Usar DNS seguro_ e escolha _Usar seu provedor de serviços atual_. Assim, o Chrome seguirá o DNS Privado.
