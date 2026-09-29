---
title: Blockera reklam i Chrome, Firefox, Edge och Brave med DNS över HTTPS
description: Ange Blokada Cloud som säker DNS i webbläsaren och blockera reklam och spårare på alla datorer, även jobbdatorer där du inte kan installera appar.
updated: 2026-09-23
order: 7
---

Moderna webbläsare kan använda en egen krypterad DNS-leverantör, så kallad *säker DNS* eller *DNS över HTTPS*. Ställ in den på Blokada Cloud, så blockerar webbläsaren reklam och spårare på alla nätverk, utan något tillägg att installera.

Inställningen gäller bara den här webbläsaren. Vill du skydda hela datorn använder du [Apple-profilen](../apple-devices/) på en Mac eller ställer in din [router](../router-ad-blocking/).

Din DoH-länk: {% doh %}

## Chrome

1. Öppna `chrome://settings/security`.
2. Aktivera *Använd säker DNS* och välj sedan *Add custom DNS service provider*.
3. Ange {% doh %}

## Edge

1. Öppna `edge://settings/privacy`.
2. Under *Säkerhet* aktiverar du *Use secure DNS to specify how to look up the network address for websites*.
3. Välj *Choose a service provider* och ange {% doh %}

## Firefox

1. Öppna *Inställningar → Sekretess & säkerhet* och scrolla till *DNS över HTTPS*.
2. Välj *Maximalt skydd*.
3. Under *Välj leverantör* väljer du *Anpassad* och anger {% doh %}

## Brave

1. Öppna `brave://settings/security`.
2. Aktivera *Använd säker DNS* och välj sedan *Add custom DNS service provider*.
3. Ange {% doh %}

## Safari

Safari har ingen egen inställning för säker DNS. Den använder systemets DNS, så installera [Apple-profilen](../apple-devices/).

## Kontrollera att det fungerar

Surfa en stund och öppna sedan sidan *Aktivitet* i [dashboarden](https://app.blokada.org/stats?src=guides). Webbläsarens uppslag visas där.

<div class="note">

Om webbläsaren hanteras av din arbetsplats eller skola kan inställningen för säker DNS vara låst. Fråga din administratör.

</div>
