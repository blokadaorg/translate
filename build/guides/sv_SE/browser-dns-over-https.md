---
title: Blockera reklam i Chrome, Firefox, Edge och Brave med DNS över HTTPS
description: Ange Blokada Cloud som säker DNS i webbläsaren och blockera reklam och spårare på alla datorer, även jobbdatorer där du inte kan installera appar.
updated: 2026-10-02
order: 7
---

Moderna webbläsare kan använda en egen krypterad DNS-leverantör, så kallad _säker DNS_ eller _DNS över HTTPS_. Ställ in den på Blokada Cloud, så blockerar webbläsaren reklam och spårare på alla nätverk, utan något tillägg att installera.

Inställningen gäller bara den här webbläsaren. Vill du skydda hela datorn använder du [Apple-profilen](../apple-devices/) på en Mac eller ställer in din [router](../router-ad-blocking/).

## Chrome

1. Öppna `chrome://settings/security`.
2. Aktivera _Använd säker DNS_ och välj sedan _Add custom DNS service provider_.
3. Ange {% doh %}

## Edge

1. Öppna `edge://settings/privacy`.
2. Under _Säkerhet_ aktiverar du _Use secure DNS to specify how to look up the network address for websites_.
3. Välj _Choose a service provider_ och ange {% doh %}

## Firefox

1. Öppna _Inställningar → Sekretess & säkerhet_ och scrolla till _DNS över HTTPS_.
2. Välj _Maximalt skydd_.
3. Under _Välj leverantör_ väljer du _Anpassad_ och anger {% doh %}

## Brave

1. Öppna `brave://settings/security`.
2. Aktivera _Använd säker DNS_ och välj sedan _Add custom DNS service provider_.
3. Ange {% doh %}

## Safari

Safari har ingen egen inställning för säker DNS. Den använder systemets DNS, så installera [Apple-profilen](../apple-devices/).

## Kontrollera att det fungerar

Surfa en stund och öppna sedan sidan _Aktivitet_ i [dashboarden](https://app.blokada.org/stats?src=guides). Webbläsarens uppslag visas där.

## Om något inte fungerar

<div class="note tip">

Om webbläsaren hanteras av din arbetsplats eller skola kan inställningen för säker DNS vara låst. Fråga din administratör.

</div>
