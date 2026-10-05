---
title: حظر الإعلانات على لينكس باستخدام DNS عبر TLS
description: قم بإعداد systemd-resolved لاستخدام Blokada Cloud عبر DNS عبر TLS المشفر، وحظر الإعلانات وأجهزة التتبع لجميع التطبيقات على جهاز الكمبيوتر الخاص بك بنظام لينكس.
updated: ٢٠٢٦-١٠-٠٢
order: 9
---

تقوم معظم توزيعات لينكس الحديثة، بما في ذلك Ubuntu وFedora، بحل الأسماء عبر _systemd-resolved_، الذي يدعم DNS عبر TLS. في Debian، قم بتثبيته أولاً باستخدام الأمر `sudo apt install systemd-resolved`. قم بتوجيهه إلى Blokada Cloud، وسيتم حظر الإعلانات وأدوات التعقب لكل تطبيق على الكمبيوتر.

## إعداد systemd-resolved

1. أنشئ المجلد باستخدام <code>sudo mkdir -p /etc/systemd/resolved.conf.d</code>، ثم أنشئ الملف <code>/etc/systemd/resolved.conf.d/blokada.conf</code> مع هذه الإعدادات:

<pre><code>[Resolve]
DNS={{ site.dnsIps.dot }}#<span data-dns="dot">{{ t[lang].placeholder | safe }}.cloud.blokada.org</span>
DNSOverTLS=yes
Domains=~.</code></pre>

<ol start="2">
<li>أعد تشغيله: <code>sudo systemctl restart systemd-resolved</code></li>
<li>تحقق منه: <code>resolvectl status</code> سيُظهر <code>+DNSOverTLS</code> وخادم Blokada.</li>
</ol>

الجزء الذي يأتي بعد "#" هو اسم DNS الخاص بك في Blokada: يقوم systemd-resolved بالتحقق من شهادة الخادم باستخدام هذا الاسم، وتستخدمه Blokada لمعرفة الجهاز الذي يطلب.

<div class="note important">

يمرر **NetworkManager** أيضاً خوادم DNS لشبكتك. يقوم `Domains=~.` بإرسال جميع الاستعلامات إلى Blokada، ولكن إذا استمر `resolvectl status` في عرض خادم آخر على اتصال ما، قم بإيقاف تعيين DNS التلقائي لهذا الاتصال (المفتاح _تلقائي_ بجانب _DNS_ في إعدادات IPv4 وIPv6 الخاصة به).

</div>

## بدون systemd-resolved

إذا لم يتم العثور على `resolvectl`، فإن التوزيعة تستخدم طريقة أخرى لحل الأسماء. قم بإعداد DNS آمن في متصفحك بدلاً من ذلك، كما هو موضح في [دليل المتصفح](../browser-dns-over-https/)، أو قم بإعداد [الراوتر](../router-ad-blocking/) ليغطي المنزل بأكمله.

## تحقق من أن الإعداد يعمل

افتح بعض المواقع، ثم انتقل إلى صفحة _النشاط_ في [لوحة المعلومات](https://app.blokada.org/stats?src=guides). ستظهر عمليات البحث لهذا الكمبيوتر هناك.

<div class="note aside">

هل ترغب في وجود VPN على هذا الجهاز أيضاً؟ [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) تتضمن إعداد WireGuard الذي يقوم بتشفير جميع حركة المرور، مع نفس الحجب.

</div>
