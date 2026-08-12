# Reproducible Demo Scenarios | سيناريوهات العرض القابلة لإعادة التنفيذ

## العربية

### الغرض

هذه السيناريوهات مصممة لمراجع تقني أو مستحوذ يريد اختبار الـMVP بنفسه دون اعتماد على شرح شفهي. كل سيناريو يوضح الإجراء والنتيجة المتوقعة ونوع الدليل الذي يقدمه وحدود ما لا يثبته.

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

**المتوقع:** تظهر مؤشرات تشغيلية وسجلات CAMEL تجريبية متسقة مع بيانات العرض، ويظهر KPI تغطية القدرات بقيمة 245 بعد تحميل جميع ملفات السجل.

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

### D05 — التحقق من سجل F001-F245

**الإجراء:** انتقل إلى سجل القدرات ونفّذ عمليات البحث التالية:

1. ابحث عن `F001` للتأكد من بداية السجل.
2. ابحث عن `F243` وتأكد من ظهور Pregnancy and Labor Monitoring بحالة Planned.
3. ابحث عن `F244` وتأكد من ظهور Genetic Breeding with Environmental Impact Analysis بحالة Planned.
4. ابحث عن `F245` وتأكد من ظهور Positive Environmental Impact Evaluation for Camel Breeding بحالة Planned.
5. استخدم البحث عن `environmental impact` وتأكد من أن F244 وF245 قابلتان للاكتشاف.

**المتوقع:** يظهر السجل الحالي متصلاً من F001 إلى F245 مع حالات النضج المعلنة، وتظهر F244 وF245 كقدرتين مصدرّيتين Planned.

**الدليل:** Canonical registry continuity + Phase 4 reconciliation + public maturity transparency.

**لا يثبت:** أن جميع 245 قدرة منفذة إنتاجياً.

### D06 — فلترة حالات النضج

**الإجراء:** استخدم مرشح الحالة لاختيار Implemented ثم Demonstrated ثم Simulated ثم Mock Integration ثم Planned.

**المتوقع:** تتغير البطاقات والإحصاءات وفق الحالة المختارة، ويظل مجموع الحالات عبر السجل الكامل = 245.

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

**المتوقع:** تظهر أحداث التفاعل التي تمت أثناء جلسة العرض مع تسلسل ومراجع ورسائل ثنائية اللغة.

**الدليل:** Demonstrated in-session audit trail.

**لا يثبت:** immutable ledger أو WORM storage أو نظام تدقيق مؤسسي دائم.

### D10 — فحص المطابقة التقنية وإصدار الاستحواذ

**الإجراء:** من نسخة محلية للمستودع شغّل:

```bash
python scripts/validate.py
node tests/test_core.mjs
node tests/test_phase3.mjs
node tests/test_phase4.mjs
python tests/test_evidence_contract.py
python scripts/security_check.py
python scripts/release_check.py
```

**المتوقع:** نجاح جميع الفحوص، بما فيها تسلسل F001-F245، F244/F245، Evidence Grade A، حدود الملكية، فحص الأسرار، وبوابات Release Readiness.

**الدليل:** Repeatable structural, functional-evidence, security and acquisition-release validation.

**لا يثبت:** Production end-to-end readiness أو live hosting أو independent field/security validation.

## مصفوفة السيناريوهات

| السيناريو | نوع الدليل | مستوى النضج الذي يدعمه |
|---|---|---|
| D01 | Executable UI | Implemented presentation |
| D02 | Executable UI | Demonstrated |
| D03 | Executable UI | Demonstrated/Simulated |
| D04 | Executable logic | Simulated |
| D05 | Registry evidence | Source reconciliation F001-F245 |
| D06 | Registry evidence | Maturity transparency |
| D07 | Workflow | Demonstrated |
| D08 | Workflow | Demonstrated |
| D09 | Audit workflow | Demonstrated |
| D10 | Automated validation | Structural + Evidence + Security + Release Readiness |

### قاعدة العناية الواجبة

أي سيناريو مستقبلي يجب أن يحدد صراحة **ما يثبته وما لا يثبته**. لا تعتبر لقطة شاشة أو فيديو وحدهما دليلاً كافياً إذا كان يمكن توفير مسار قابل لإعادة التنفيذ.

## English

These ten scenarios provide a reproducible first-pass acquisition demo covering bilingual presentation, dashboard/registry review, risk alerts, health-risk simulation, **F001-F245 registry lookup including explicit F244/F245 verification**, maturity filtering, auction interaction, certificate verification, in-session audit events, and the complete automated validation/security/release-readiness chain.

Each scenario states both the evidence it provides and the claim boundary it does not cross. The goal is reproducible diligence, not a marketing-only walkthrough.
