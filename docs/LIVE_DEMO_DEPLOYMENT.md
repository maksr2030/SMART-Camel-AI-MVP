# Live Demo Deployment | نشر العرض الحي

## العربية

### الحالة الحالية

تم تفعيل GitHub Pages بنجاح للمنصة، والنشر المعتمد حالياً هو من الفرع الرئيسي مباشرة:

- **Branch:** `main`
- **Folder:** `/(root)`
- **URL:** `https://maksr2030.github.io/SMART-Camel-AI-MVP/`
- **GitHub Pages status:** `built`
- **Visibility:** Public
- **HTTPS:** Enforced

تم توثيق نتيجة التحقق في `LIVE_DEMO_VERIFICATION.md`، وبذلك أصبحت **G08 — Live Stable Demo = Ready**.

### آلية النشر المعتمدة

الموقع ثابت HTML/JavaScript ولا يحتاج build system منفصلاً. لذلك يستخدم GitHub Pages النشر من `main/(root)` مباشرة.

تم وضع `.nojekyll` في جذر المستودع لمنع معالجة Jekyll والحفاظ على الأصول الثابتة كما هي.

### ما يتم عرضه

- `index.html`
- ملفات `app/`
- سجل القدرات F001-F245 داخل runtime العام.

وجود ملفات `docs/` و`scripts/` في المستودع العام لا يعني أنها جزء من واجهة العرض، وهي موجودة كمواد عناية واجبة ومراجعة تقنية.

### شروط استمرار G08 كـReady

1. بقاء Pages منشوراً من `main/(root)`.
2. استمرار الرابط العام دون 404.
3. بقاء HTTPS مفروضاً.
4. عدم حذف `index.html` أو أصول `app/`.
5. استمرار CI في حماية نطاق F001-F245.

### حدود الادعاء

العرض الحي يثبت وجود Demonstrator عام قابل للمراجعة فقط. لا يثبت backend إنتاجياً أو قاعدة بيانات أو IAM أو تكاملات حكومية حية أو أجهزة IoT فعلية.

## English

The live demonstrator is published through GitHub Pages directly from `main` and `/(root)` at:

`https://maksr2030.github.io/SMART-Camel-AI-MVP/`

GitHub reports the site as built, public and HTTPS-enforced. `.nojekyll` is kept at repository root so the static HTML/JavaScript surface is served without Jekyll processing. This closes **G08 — Live Stable Demo** while remaining distinct from Production Readiness.
