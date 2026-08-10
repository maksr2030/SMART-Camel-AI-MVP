# Reproducible Demo Scenarios | سيناريوهات العرض القابلة لإعادة التنفيذ

## العربية

### الغرض

هذه السيناريوهات مصممة لمراجع تقني أو مستحوذ يريد اختبار الـMVP بنفسه دون اعتماد على شرح شفهي. كل سيناريو يوضح: الإجراء، النتيجة المتوقعة، ونوع الدليل الذي يقدمه.

### شرط التشغيل

من جذر المستودع:

```bash
python3 -m http.server 4173
```

ثم افتح:

```text
http://localhost:4173/
```

جميع بيانات السيناريوهات اصطناعية أو توضيحية.

### D01 — التبديل بين العربية والإنجليزية

**الإجراء:** افتح الصفحة واضغط زر اللغة في أعلى الواجهة ثم أعد التبديل.

**المتوقع:** تتغير النصوص الأساسية واتجاه العرض بين العربية والإنجليزية دون إعادة تحميل التطبيق.

**الدليل:** Bilingual UI / public demonstrator.

**لا يثبت:** اكتمال الترجمة المؤسسية لكل مستند داخلي أو لغة إضافية.

### D02 — فحص لوحة القيادة والسجل

**الإجراء:** راجع بطاقات KPI وسجل الإبل الظاهر في الصفحة.

**المتوقع:** تظهر مؤشرات تشغيلية وسجلات CAMEL تجريبية متسقة مع بيانات العرض.

**الدليل:** Demonstrated registry and dashboard presentation.

**لا يثبت:** اتصالاً بقاعدة بيانات أو سجل حكومي حي.

### D03 — مراجعة إشارات المخاطر

**الإجراء:** افتح قسم التنبيهات واقرأ مستويات التنبيه والسبب المعروض.

**المتوقع:** تظهر تنبيهات صحية/نشاط/سياج جغرافي توضيحية بمستويات مختلفة.

**الدليل:** Demonstrated risk presentation.

**لا يثبت:** رصد أجهزة حية أو إنذاراً طبياً/ميدانياً معتمداً.

### D04 — تشغيل محرك مخاطر الصحة

**الإجراء:** غيّر الحرارة والنشاط والترطيب في منزلقات المحاكاة.

**المتوقع:** تتغير درجة المخاطر والتفسير وفق المنطق التجريبي في الواجهة.

**الدليل:** Executable simulated health-risk behavior.

**لا يثبت:** نموذج تشخيص بيطري أو دقة سريرية.

### D05 — التحقق من سجل F001-F243

**الإجراء:** انتقل إلى سجل القدرات، ابحث عن `F243` ثم ابحث عن `Pregnancy and Labor Monitoring` أو النص العربي المقابل.

**المتوقع:** يظهر F243 بحالة Planned، ويمكن البحث عن القدرات الأخرى وفلترتها حسب حالة النضج.

**الدليل:** Canonical registry continuity and public maturity transparency.

**لا يثبت:** أن جميع 243 قدرة منفذة إنتاجياً.

### D06 — فلترة حالات النضج

**الإجراء:** استخدم مرشح الحالة لاختيار Implemented ثم Demonstrated ثم Simulated ثم Mock Integration ثم Planned.

**المتوقع:** تتغير البطاقات والإحصاءات وفق الحالة المختارة.

**الدليل:** Public maturity classification is queryable rather than hidden in narrative text.

### D07 — تنفيذ مزايدة تجريبية

**الإجراء:** اضغط زر المزايدة التجريبية في قسم السوق.

**المتوقع:** تتغير نتيجة العرض ويضاف حدث إلى سجل التدقيق داخل الجلسة.

**الدليل:** Demonstrated auction interaction + event trace.

**لا يثبت:** دفعاً أو تسوية أو عقد بيع حقيقي.

### D08 — التحقق من شهادة تجريبية

**الإجراء:** اترك الرمز `CAMEL-001` واضغط تحقق. ثم غيّر الرمز إلى قيمة أخرى وأعد المحاولة.

**المتوقع:** ينجح التحقق للرمز التجريبي المعروف ويفشل للرمز غير المعروف، مع تسجيل الحدث.

**الدليل:** Demonstrated certificate-verification path.

**لا يثبت:** شهادة حكومية أو توقيعاً رقمياً قانونياً إنتاجياً.

### D09 — مراجعة سجل التدقيق داخل الجلسة

**الإجراء:** نفّذ D07 وD08 ثم انتقل إلى سجل الأحداث.

**المتوقع:** تظهر أحداث التفاعل التي تمت أثناء جلسة العرض.

**الدليل:** Demonstrated in-session audit trail.

**لا يثبت:** immutable ledger أو WORM storage أو نظام تدقيق مؤسسي دائم.

### D10 — فحص المطابقة التقنية الآلية

**الإجراء:** من نسخة محلية للمستودع شغّل:

```bash
python scripts/validate.py
```

**المتوقع:** نجاح التحقق من الملفات المطلوبة وتسلسل F001-F243 وعدم وجود تكرار وربط الأصول المطلوبة.

**الدليل:** Repeatable structural CI validation.

**لا يثبت:** functional end-to-end production test coverage.

## مصفوفة السيناريوهات

| السيناريو | نوع الدليل | مستوى النضج الذي يدعمه |
|---|---|---|
| D01 | Executable UI | Implemented presentation |
| D02 | Executable UI | Demonstrated |
| D03 | Executable UI | Demonstrated/Simulated |
| D04 | Executable logic | Simulated |
| D05 | Registry evidence | Source reconciliation |
| D06 | Registry evidence | Maturity transparency |
| D07 | Workflow | Demonstrated |
| D08 | Workflow | Demonstrated |
| D09 | Audit workflow | Demonstrated |
| D10 | Automated validation | Structural evidence |

### قاعدة العناية الواجبة

أي سيناريو مستقبلي يجب أن يحدد صراحة **ما يثبته وما لا يثبته**. لا تعتبر لقطة شاشة أو فيديو وحدهما دليلاً كافياً إذا كان يمكن توفير مسار قابل لإعادة التنفيذ.

## English

These ten scenarios provide a reproducible first-pass acquisition demo: bilingual presentation, dashboard/registry review, risk alerts, health-risk simulation, F001-F243 registry lookup, maturity filtering, auction interaction, certificate verification, in-session audit events and automated structural validation.

Each scenario intentionally states both the evidence it provides and the claim boundary it does not cross. The goal is reproducible diligence, not a marketing-only walkthrough.
