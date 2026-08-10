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

### Acquisition Technical Due Diligence Foundation — Phase 1

سلسلة العناية الواجبة الأساسية:

**Claim → F-ID → Source/Evidence → Maturity → Demo/Test → Limitation → Production Closure Plan**

- [سجل القدرات للاستحواذ | Acquisition Feature Registry](docs/FEATURE_REGISTRY.md) — خط الأساس التاريخي F001-F243.
- [مطابقة 245 قدرة | Phase 4 — 245 Capability Reconciliation](docs/PHASE4_245_RECONCILIATION.md) — تضيف F244-F245 وتثبت النطاق الحالي F001-F245.
- [سيناريوهات العرض | Reproducible Demo Scenarios](docs/DEMO_SCENARIOS.md) — D01-D10.
- [القيود المعروفة | Known Limitations](docs/KNOWN_LIMITATIONS.md) — 23 قيداً عربياً + 23 إنجليزياً.
- [الأمن ونموذج التهديدات | Security Baseline & Threat Model](docs/SECURITY.md).
- [إشعار الملكية الفكرية | IP Notice](docs/IP_NOTICE.md).
- [النظرة التقنية للاستحواذ | Acquisition Technical Overview](docs/ACQUISITION_TECHNICAL_OVERVIEW.md).

### Evidence & Test Closure — Phase 2

- [سجل أدلة الاستحواذ | Acquisition Evidence Catalog](docs/EVIDENCE_CATALOG.md) — EVD-001 إلى EVD-015.
- `app/core.js` — منطق عام قابل للاختبار تستخدمه الواجهة نفسها.
- `tests/test_core.mjs` — اختبارات **F001-F245**، حالات النضج، المخاطر الصحية، التحقق من الشهادة، البحث والفلترة، والسجلات الاصطناعية، مع تحقق صريح من F244 وF245.
- `tests/test_evidence_contract.py` — اختبار عقد الأدلة، حدود الملكية الفكرية، القيود المعروفة، وربط الـCore بالواجهة.

### Strategic Grade A Closure — Phase 3

- F001/F002 — Registry schema, uniqueness, identity lookup → EVD-016.
- F012 — Geofence state evaluation → EVD-017.
- F026/F027 — Testable Mazayen scoring demonstrator → EVD-018.
- F034 — Auction state-transition contract → EVD-019.
- F060 — Ordered bilingual audit-event contract → EVD-020.

النتيجة: **جميع القدرات الاستراتيجية الاثنتي عشرة المختارة أصبحت Grade A Evidence**.

- [إغلاق أدلة Phase 3 | Phase 3 Grade A Evidence](docs/PHASE3_GRADE_A_EVIDENCE.md).
- [مصفوفة الأدلة الاستراتيجية | Strategic Capability Evidence Matrix](docs/STRATEGIC_EVIDENCE_MATRIX.md).
- `tests/test_phase3.mjs` — اختبار السجل والهوية وgeofence والمزايين والمزاد والتدقيق.

### Phase 4 — 245 Capability Reconciliation & Acquisition Readiness

تمت إضافة قدرتين مصدرّيتين مستقلتين كانتا موجودتين في ملفات SMART Camel التاريخية ولم تكونا ممثلتين كـF-ID مستقلين:

- **F244 — التحسين الوراثي مع تحليل الأثر البيئي / Genetic Breeding with Environmental Impact Analysis — Planned.**
- **F245 — تقييم الأثر البيئي الإيجابي لتربية الإبل / Positive Environmental Impact Evaluation for Camel Breeding — Planned.**

يحمّل runtime ملف `app/source-features-244-245.js` بعد F243، ويُلزم `scripts/validate.py` و`tests/test_core.mjs` بوجود تسلسل فريد ومتصل **F001-F245**. لا يُسمح لإصدار الاستحواذ أن يدّعي تغطية كاملة إذا انخفض العدد عن 245.

### حالات النضج

- Implemented: منفذة مباشرة داخل النموذج العام.
- Demonstrated: مسار وظيفي قابل للاستعراض وليس نظام إنتاج كامل.
- Simulated: نتيجة أو محرك يعتمد على بيانات أو منطق محاكاة.
- Mock Integration: نقطة تكامل توضيحية دون اتصال خارجي حي.
- Planned: ضمن النطاق المعماري ولم تدخل بعد في الإصدار التشغيلي العام.

### تشغيل محلي

```bash
python3 -m http.server 4173
```

ثم افتح `http://localhost:4173/`.

### التحقق والاختبارات

```bash
python scripts/validate.py
node tests/test_core.mjs
node tests/test_phase3.mjs
python tests/test_evidence_contract.py
```

GitHub Actions يشغّل هذه الاختبارات كعقد مستمر لجاهزية العناية الواجبة.

### التوثيق الأساسي

- [المعمارية | Architecture](docs/ARCHITECTURE.md)
- [مصفوفة الأدلة | Evidence Matrix](docs/EVIDENCE.md)
- [النظرة العامة | Public Overview](docs/PUBLIC_OVERVIEW.md)
- [مطابقة ميزات المصادر | Source Reconciliation](docs/SOURCE_RECONCILIATION.md)
- [سجل الخوارزميات والمحركات | Algorithm & Engine Registry](docs/ALGORITHM_ENGINE_REGISTRY.md)
- [عائلات الأنظمة | System Families](docs/SYSTEM_FAMILIES.md)
- [مطابقة 245 قدرة | Phase 4 Reconciliation](docs/PHASE4_245_RECONCILIATION.md)

### حدود الإفصاح

جميع بيانات العرض اصطناعية أو توضيحية ما لم يُذكر خلاف ذلك. بيانات المستشعرات، مخرجات الذكاء الاصطناعي، التقييمات والتكاملات الخارجية لا تمثل تشغيلًا إنتاجيًا أو ربطًا حكوميًا حيًا. لا يحتوي المستودع العام على الخوارزميات المملوكة أو الأوزان أو مجموعات التدريب أو نماذج التقييم السرية أو بيانات الشركاء أو وثائق العناية الواجبة الخاصة.

## English

SMART Camel AI is an integrated digital operating environment for camel lifecycle management, herd and farm operations, health, breeding, lineage, grazing, competitions, racing, auctions, marketplaces, products, risk and operational intelligence within one auditable interface.

This public repository supports executable demonstration and technical review without exposing proprietary algorithms, protected implementation details or confidential intellectual-property records.

### Current normalized result

- **245 canonical capability records**, F001 through F245.
- **29 source-documented named algorithms and engines**.
- **20 canonical system families**.
- **Two independently named training models**.
- **20 acquisition Evidence IDs**, EVD-001 through EVD-020.
- **12/12 selected strategic capabilities at Evidence Grade A — Automated + Runtime**.

These counts do not claim 245 production systems or 29 validated production models. Evidence Grade A does not mean production readiness.

### Acquisition diligence chain

**Claim → F-ID → Source/Evidence → Maturity → Demo/Test → Limitation → Production Closure Plan**

- [Acquisition Feature Registry](docs/FEATURE_REGISTRY.md) — historical Phase 1 baseline F001-F243.
- [Phase 4 — 245 Capability Reconciliation](docs/PHASE4_245_RECONCILIATION.md) — source-backed F244-F245 addendum and current F001-F245 scope.
- [Reproducible Demo Scenarios](docs/DEMO_SCENARIOS.md) — D01-D10.
- [Known Limitations](docs/KNOWN_LIMITATIONS.md) — 23 Arabic + 23 English disclosures.
- [Security Baseline & Threat Model](docs/SECURITY.md).
- [IP Notice](docs/IP_NOTICE.md).
- [Acquisition Technical Overview](docs/ACQUISITION_TECHNICAL_OVERVIEW.md).
- [Acquisition Evidence Catalog](docs/EVIDENCE_CATALOG.md).
- [Phase 3 Grade A Evidence](docs/PHASE3_GRADE_A_EVIDENCE.md).
- [Strategic Capability Evidence Matrix](docs/STRATEGIC_EVIDENCE_MATRIX.md).

### Phase 4 additions

- **F244 — Genetic Breeding with Environmental Impact Analysis — Planned.**
- **F245 — Positive Environmental Impact Evaluation for Camel Breeding — Planned.**

The public runtime loads `app/source-features-244-245.js`. Structural validation and executable core tests require a unique, continuous **F001-F245** sequence and explicitly verify F244/F245.

### Validate and test

```bash
python scripts/validate.py
node tests/test_core.mjs
node tests/test_phase3.mjs
python tests/test_evidence_contract.py
```

### Disclosure boundary

All demonstration records are synthetic or illustrative unless explicitly stated otherwise. Sensor streams, AI outputs, valuations and external integrations do not represent production deployment or live government connectivity. Proprietary algorithms, model weights, training datasets, confidential scoring models, partner data and private due-diligence records are excluded from the public repository.
