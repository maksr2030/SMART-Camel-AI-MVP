# Live Demo Deployment | نشر العرض الحي

## العربية

### الهدف

هذه الوثيقة تغلق المسار التقني المطلوب لتحويل SMART Camel AI من Acquisition Demonstrator Candidate إلى **Acquisition Demonstrator Release** من ناحية العرض الحي.

### رابط GitHub Pages المستهدف

بعد تفعيل GitHub Pages للمستودع واختيار GitHub Actions كمصدر للنشر، يكون رابط المشروع المتوقع:

`https://maksr2030.github.io/SMART-Camel-AI-MVP/`

هذا الرابط **مستهدف وليس مثبتاً كعامل حالياً** حتى ينجح أول deployment على `main` ويتم التحقق منه خارج GitHub.

### Workflow النشر

الملف:

`.github/workflows/pages.yml`

ينشر فقط:

- `index.html`
- مجلد `app/`
- ملف `.nojekyll` داخل artifact

ولا ينشر `docs/` أو `scripts/` أو ملفات العناية الواجبة كجزء من الموقع الحي.

### الإعداد المطلوب مرة واحدة في GitHub

1. افتح المستودع.
2. Settings.
3. Pages.
4. تحت Build and deployment اختر **Source: GitHub Actions**.

بعد ذلك، عند دمج الفرع إلى `main`، يعمل workflow النشر تلقائياً.

### شروط إغلاق G08

لا تتحول بوابة Live Stable Demo إلى Ready إلا بعد:

1. نجاح Pages deployment على `main`.
2. ظهور `page_url` من خطوة `actions/deploy-pages`.
3. فتح الرابط من خارج GitHub بنجاح.
4. تحميل `index.html` وملفات `app/` دون أخطاء 404.
5. ظهور سجل القدرات حتى F245 داخل الواجهة.
6. نجاح التبديل العربي/الإنجليزي والمحاكاة والبحث والفلترة.
7. بقاء البيانات موسومة كبيانات عرض/محاكاة.

### حدود الادعاء

نجاح GitHub Pages يثبت وجود **عرض حي ثابت قابل للمراجعة** فقط. لا يثبت backend إنتاجياً أو قاعدة بيانات أو تكاملات حية أو أجهزة IoT أو جاهزية أمنية إنتاجية.

## English

This document defines the live-deployment gate for the SMART Camel AI Acquisition Demonstrator Release.

Target project URL after GitHub Pages is enabled with **GitHub Actions** as the publishing source:

`https://maksr2030.github.io/SMART-Camel-AI-MVP/`

The URL remains a target, not a verified live claim, until the first `main` deployment succeeds and the site is externally checked.

The deployment workflow publishes only `index.html` and `app/`, keeping due-diligence documents and scripts outside the website artifact.

G08 closes only after a successful Pages deployment, an externally reachable site, working static assets, visible F001-F245 scope, and successful bilingual/demo interactions.
