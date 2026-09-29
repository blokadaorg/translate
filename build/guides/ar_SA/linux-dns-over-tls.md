---
title: حظر الإعلانات على لينكس باستخدام DNS عبر TLS
description: قم بإعداد systemd-resolved لاستخدام Blokada Cloud عبر DNS عبر TLS المشفر، وحظر الإعلانات وأجهزة التتبع لجميع التطبيقات على جهاز الكمبيوتر الخاص بك بنظام لينكس.
updated: 2026-09-28
order: 9
---

معظم توزيعات لينكس الحديثة، بما في ذلك أوبونتو وفيدورا، تقوم بحل الأسماء عبر systemd-resolved، والذي يدعم DNS عبر TLS. على ديبيان، قم بتثبيته أولاً باستخدام الأمر: <code>sudo apt install systemd-resolved</code>. وجهه إلى Blokada Cloud، وسيتم حظر الإعلانات وأجهزة التتبع عن جميع التطبيقات على الكمبيوتر.

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

<div class="note">

**NetworkManager** يمرر أيضاً خوادم DNS لشبكتك. `Domains=~.` يرسل جميع عمليات البحث إلى Blokada، ولكن إذا استمر <code>resolvectl status</code> في عرض خادم آخر على اتصال ما، قم بإيقاف تشغيل تعيين DNS التلقائي لهذا الاتصال (مفتاح _تلقائي_ بجانب _DNS_ في إعدادات IPv4 و IPv6 الخاصة به).

</div>

## بدون systemd-resolved

إذا لم يتم العثور على <code>resolvectl</code>، فإن توزيعتك تقوم بحل الأسماء بطريقة أخرى. قم بإعداد DNS آمن في متصفحك بدلاً من ذلك، كما هو موضح في [دليل المتصفح](../browser-dns-over-https/)، أو قم بإعداد [الراوتر](../router-ad-blocking/) ليغطي المنزل بأكمله.

## تحقق من أن الإعداد يعمل

افتح بعض المواقع، ثم انتقل إلى صفحة _النشاط_ في [لوحة المعلومات](https://app.blokada.org/stats?src=guides). عمليات البحث من هذا الكمبيوتر ستظهر هناك.

<div class="note">

هل ترغب في شبكة VPN على هذا الكمبيوتر أيضاً؟ [Blokada Plus](https://app.blokada.org/activate?tier=plus&src=guides) تتضمن إعداد WireGuard الذي يقوم بتشفير جميع حركة المرور، مع نفس الحظر.

</div>
