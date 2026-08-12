# SMART Camel AI MVP | منصة الإبل الذكية

## العربية

منصة الإبل الذكية هي بيئة رقمية متكاملة لإدارة دورة حياة الإبل والقطعان والمزارع والصحة والتكاثر والأنساب والمراعي والمسابقات والسباقات والمزادات والأسواق والمنتجات والمخاطر والبيانات التشغيلية ضمن واجهة موحدة قابلة للتدقيق.

هذا المستودع هو الإصدار العام التجريبي للمنصة، والغرض منه تقديم نموذج أولي قابل للتشغيل والمراجعة التقنية دون نشر الخوارزميات الخاصة أو الأسرار التنفيذية أو وثائق الملكية الفكرية الداخلية.

### النتيجة المعيارية الحالية

- **245 سجل قدرة معيارية** من F001 إلى F245.
- **29 خوارزمية ومحركاً مسمىً وموثقاً في المصدر** ضمن سجل مستقل.
- **20 عائلة نظامية معيارية**.
- **نموذجَي تدريب مسميين في المصدر** موثقين بشكل منفصل.
- **20 Evidence IDs** من EVD-001 إلى EVD-020 عبر Phase 2 وPhase 3.
- **12 من 12 قدرة استراتيجية** أصبحت Grade A من ناحية Evidence — Automated + Runtime.

هذه الأرقام لا تعني وجود 245 نظاماً إنتاجياً أو 29 نموذجاً معتمداً. حالة النضج التشغيلية معلنة لكل قدرة، وGrade A لا تعني Production Ready.

### ما الذي يعمل في هذا الإصدار

- واجهة عربية وإنجليزية مع تبديل فوري بين اللغتين.
- لوحة قيادة تشغيلية ببيانات اصطناعية.
- سجل إبل تجريبي يمر عبر schema/uniqueness validation عند التشغيل.
- سجل قدرات runtime كامل **F001-F245** مصنف حسب حالة النضج.
- محرك مخاطر صحي تفاعلي تفسيري.
- محاكاة geofence بحالات Inside/Near/Outside.
- scoring demonstrator للمزايين يستخدم نفس الـCore المختبر.
- محرك مزاد تجريبي بحالة وسعر وعدد مزايدات وقاعدة قبول للمزايدة الأعلى فقط.
- تحقق تجريبي من شهادة CAMEL-001.
- سجل أحداث ثنائي اللغة بتسلسل ومراجع داخل الجلسة.
- سجل عام للخوارزميات والمحركات المسمّاة دون إفشاء التنفيذ المملوك.
- خريطة من 20 عائلة نظامية.
- Core Logic مشترك بين الواجهة والاختبارات.

### Acquisition Technical Due Diligence Foundation

**Claim → F-ID → Source/Evidence → Maturity → Demo/Test → Limitation → Production Closure Plan**

- [سجل القدرات للاستحواذ | Acquisition Feature Registry](docs/FEATURE_REGISTRY.md) — خط الأساس التاريخي F001-F243.
- [مطابقة 245 قدرة | Phase 4 — 245 Capability Reconciliation](docs/PHASE4_245_RECONCILIATION.md) — تضيف F244-F245 وتثبت النطاق الحالي F001-F245.
- [سيناريوهات العرض | Reproducible Demo Scenarios](docs/DEMO_SCENARIOS.md) — D01-D10.
- [القيود المعروفة | Known Limitations](docs/KNOWN_LIMITATIONS.md) — 23 قيداً عربياً + 23 إنجليزياً.
- [الأمن ونموذج التهديدات | Security Baseline & Threat Model](docs/SECURITY.md).
- [إشعار الملكية الفكرية | IP Notice](docs/IP_NOTICE.md).
- [النظرة التقنية للاستحواذ | Acquisition Technical Overview](docs/ACQUISITION_TECHNICAL_OVERVIEW.md).
- [بيان إصدار الاستحواذ | Acquisition Release Manifest](docs/ACQUISITION_RELEASE_MANIFEST.md).

### Evidence & Grade A Closure

- [سجل أدلة الاستحواذ | Acquisition Evidence Catalog](docs/EVIDENCE_CATALOG.md) — EVD-001 إلى EVD-015.
- [إغلاق أدلة Phase 3 | Phase 3 Grade A Evidence](docs/PHASE3_GRADE_A_EVIDENCE.md).
- [مصفوفة الأدلة الاستراتيجية | Strategic Capability Evidence Matrix](docs/STRATEGIC_EVIDENCE_MATRIX.md).
- `app/core.js` — منطق عام قابل للاختبار تستخدمه الواجهة نفسها.
- `tests/test_core.mjs` — اختبارات F001-F245 وحالات النضج والمخاطر والبحث والفلترة.
- `tests/test_phase3.mjs` — اختبارات Grade A للهوية والسجل وgeofence والمزايين والمزاد والتدقيق.
- `tests/test_phase4.mjs` — اختبار مستقل لاكتمال F001-F245 وF244/F245.
- `tests/test_evidence_contract.py` — عقد الأدلة وحدود الملكية والقيود.

### Acquisition Demonstrator Release Readiness

- [جاهزية إصدار الاستحواذ | Acquisition Release Readiness](docs/RELEASE_READINESS.md) — G01-G15.
- [نشر العرض الحي | Live Demo Deployment](docs/LIVE_DEMO_DEPLOYMENT.md).
- [مراجعة الاعتماديات والتراخيص | Dependency & License Review](docs/DEPENDENCY_AND_LICENSE_REVIEW.md).
- `.github/workflows/pages.yml` — workflow لنشر `index.html + app/` فقط على GitHub Pages بعد تفعيل Source: GitHub Actions.
- `scripts/security_check.py` — فحص الأسرار والملفات الحساسة والاعتماديات الخارجية في runtime.
- `scripts/release_check.py` — يحرس نطاق 245 وبوابات الإصدار والنشر الحي.

الرابط المستهدف بعد تفعيل GitHub Pages ونجاح أول deployment على `main` هو:

`https://maksr2030.github.io/SMART-Camel-AI-MVP/`

هذا الرابط **ليس مثبتاً كعامل بعد**؛ G08 يبقى Pending حتى نجاح النشر والتحقق الخارجي.

### التحقق والاختبارات

```bash
python scripts/validate.py
node tests/test_core.mjs
node tests/test_phase3.mjs
node tests/test_phase4.mjs
python tests/test_evidence_contract.py
python scripts/security_check.py
python scripts/release_check.py
```

### حدود الإفصاح

جميع بيانات العرض اصطناعية أو توضيحية ما لم يُذكر خلاف ذلك. لا يمثل هذا المستودع تشغيلًا إنتاجياً، ولا يحتوي على الخوارزميات المملوكة أو الأوزان أو مجموعات التدريب أو نماذج التقييم السرية أو بيانات الشركاء أو وثائق العناية الواجبة الخاصة.

## English

SMART Camel AI is an integrated public demonstrator for a broader camel-sector operating and intelligence platform.

### Current normalized result

- **245 canonical capability records**, F001 through F245.
- **29 source-documented named algorithms and engines**.
- **20 canonical system families**.
- **Two independently named training models**.
- **20 acquisition Evidence IDs**, EVD-001 through EVD-020.
- **12/12 selected strategic capabilities at Evidence Grade A — Automated + Runtime**.

The historical Phase 1 registry remains F001-F243 for traceability; Phase 4 establishes F001-F245 as the current runtime/CI boundary.

### Acquisition Demonstrator Release readiness

- [Acquisition Release Manifest](docs/ACQUISITION_RELEASE_MANIFEST.md)
- [Acquisition Release Readiness](docs/RELEASE_READINESS.md)
- [Live Demo Deployment](docs/LIVE_DEMO_DEPLOYMENT.md)
- [Dependency & License Review](docs/DEPENDENCY_AND_LICENSE_REVIEW.md)

Target GitHub Pages URL after Pages is enabled with GitHub Actions and the first `main` deployment succeeds:

`https://maksr2030.github.io/SMART-Camel-AI-MVP/`

The URL remains unverified until deployment and external validation close G08.

### Validate and test

```bash
python scripts/validate.py
node tests/test_core.mjs
node tests/test_phase3.mjs
node tests/test_phase4.mjs
python tests/test_evidence_contract.py
python scripts/security_check.py
python scripts/release_check.py
```

This package is an **Acquisition Demonstrator Candidate** until final PR CI, merge, live Pages verification and the fixed acquisition release tag are complete. It is not Production Ready.
