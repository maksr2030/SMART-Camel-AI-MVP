# SMART Camel AI MVP | منصة الإبل الذكية

## العربية

منصة الإبل الذكية هي بيئة رقمية متكاملة لإدارة دورة حياة الإبل والقطعان والمزارع والصحة والتكاثر والأنساب والمراعي والمسابقات والسباقات والمزادات والأسواق والمنتجات والمخاطر والبيانات التشغيلية ضمن واجهة موحدة قابلة للتدقيق.

هذا المستودع هو الإصدار العام التجريبي للمنصة، والغرض منه تقديم نموذج أولي قابل للتشغيل والمراجعة التقنية دون نشر الخوارزميات الخاصة أو الأسرار التنفيذية أو وثائق الملكية الفكرية الداخلية.

### النتيجة المعيارية الحالية

- **243 سجل قدرة معيارية** من F001 إلى F243.
- **29 خوارزمية ومحركاً مسمىً وموثقاً في المصدر** ضمن سجل مستقل.
- **20 عائلة نظامية معيارية**.
- **نموذجَي تدريب مسميين في المصدر** موثقين بشكل منفصل.
- **20 Evidence IDs** من EVD-001 إلى EVD-020 عبر Phase 2 وPhase 3.
- **12 من 12 قدرة استراتيجية** أصبحت Grade A من ناحية Evidence — Automated + Runtime.

هذه الأرقام لا تعني وجود 243 نظاماً إنتاجياً أو 29 نموذجاً معتمداً. حالة النضج التشغيلية معلنة لكل قدرة، وGrade A لا تعني Production Ready.

### ما الذي يعمل في هذا الإصدار

- واجهة عربية وإنجليزية مع تبديل فوري بين اللغتين.
- لوحة قيادة تشغيلية ببيانات اصطناعية.
- سجل إبل تجريبي يمر عبر schema/uniqueness validation عند التشغيل.
- سجل قدرات كامل F001-F243 مصنف حسب حالة النضج.
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

- [سجل القدرات للاستحواذ | Acquisition Feature Registry](docs/FEATURE_REGISTRY.md) — F001-F243.
- [سيناريوهات العرض | Reproducible Demo Scenarios](docs/DEMO_SCENARIOS.md) — D01-D10.
- [القيود المعروفة | Known Limitations](docs/KNOWN_LIMITATIONS.md) — 23 قيداً عربياً + 23 إنجليزياً.
- [الأمن ونموذج التهديدات | Security Baseline & Threat Model](docs/SECURITY.md).
- [إشعار الملكية الفكرية | IP Notice](docs/IP_NOTICE.md).
- [النظرة التقنية للاستحواذ | Acquisition Technical Overview](docs/ACQUISITION_TECHNICAL_OVERVIEW.md).

### Evidence & Test Closure — Phase 2

- [سجل أدلة الاستحواذ | Acquisition Evidence Catalog](docs/EVIDENCE_CATALOG.md) — EVD-001 إلى EVD-015.
- `app/core.js` — منطق عام قابل للاختبار تستخدمه الواجهة نفسها.
- `tests/test_core.mjs` — اختبارات F001-F243، حالات النضج، المخاطر الصحية، التحقق من الشهادة، البحث والفلترة، والسجلات الاصطناعية.
- `tests/test_evidence_contract.py` — اختبار عقد الأدلة، حدود الملكية الفكرية، القيود المعروفة، وربط الـCore بالواجهة.

### Strategic Grade A Closure — Phase 3

ترفع Phase 3 القدرات الاستراتيجية السبعة المتبقية من Evidence Grade B إلى Grade A دون تغيير حالة النضج العامة:

- F001/F002 — Registry schema, uniqueness, identity lookup → EVD-016.
- F012 — Geofence state evaluation → EVD-017.
- F026/F027 — Testable Mazayen scoring demonstrator → EVD-018.
- F034 — Auction state-transition contract → EVD-019.
- F060 — Ordered bilingual audit-event contract → EVD-020.

النتيجة: **جميع القدرات الاستراتيجية الاثنتي عشرة المختارة أصبحت Grade A Evidence**.

- [إغلاق أدلة Phase 3 | Phase 3 Grade A Evidence](docs/PHASE3_GRADE_A_EVIDENCE.md).
- [مصفوفة الأدلة الاستراتيجية | Strategic Capability Evidence Matrix](docs/STRATEGIC_EVIDENCE_MATRIX.md).
- `tests/test_phase3.mjs` — اختبار السجل والهوية وgeofence والمزايين والمزاد والتدقيق.

### الطبقة النهائية F236-F243

- F236: التعرف الذكي على سلالات الإبل.
- F237: التحكم التكيفي المغلق في تغذية الإبل.
- F238: التعرف البيومتري على الإبل ببصمة الوجه.
- F239: المراقبة الصحية الحرارية بالكاميرات.
- F240: تتبع نوم الإبل وتحليل جودته.
- F241: الإنذار المبكر بالإجهاد الحراري للإبل.
- F242: تحليل مخاطر الأمراض الوراثية.
- F243: مراقبة الحمل والولادة في الإبل.

بقيت هذه القدرات **Planned** في الإصدار العام لأن ملفات المصدر تثبت التصميم والهوية الوظيفية، لا نشرها الإنتاجي الحالي.

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

### حدود الإفصاح

جميع بيانات العرض اصطناعية أو توضيحية ما لم يُذكر خلاف ذلك. بيانات المستشعرات، مخرجات الذكاء الاصطناعي، التقييمات والتكاملات الخارجية لا تمثل تشغيلًا إنتاجيًا أو ربطًا حكوميًا حيًا. لا يحتوي المستودع العام على الخوارزميات المملوكة أو الأوزان أو مجموعات التدريب أو نماذج التقييم السرية أو بيانات الشركاء أو وثائق العناية الواجبة الخاصة.

## English

SMART Camel AI is an integrated digital operating environment for camel lifecycle management, herd and farm operations, health, breeding, lineage, grazing, competitions, racing, auctions, marketplaces, products, risk and operational intelligence within one auditable interface.

This repository contains the public demonstrator of the platform. It supports executable demonstration and technical review without exposing proprietary algorithms, protected implementation details or confidential intellectual-property records.

### Current normalized result

- **243 canonical capability records**, F001 through F243.
- **29 source-documented named algorithms and engines**.
- **20 canonical system families**.
- **Two independently named training models**.
- **20 acquisition Evidence IDs**, EVD-001 through EVD-020.
- **12/12 selected strategic capabilities at Evidence Grade A — Automated + Runtime**.

These counts do not claim 243 production systems or 29 validated production models. Evidence Grade A does not mean production readiness.

### Acquisition Technical Due Diligence Foundation — Phase 1

**Claim → F-ID → Source/Evidence → Maturity → Demo/Test → Limitation → Production Closure Plan**

- [Acquisition Feature Registry](docs/FEATURE_REGISTRY.md) — F001-F243.
- [Reproducible Demo Scenarios](docs/DEMO_SCENARIOS.md) — D01-D10.
- [Known Limitations](docs/KNOWN_LIMITATIONS.md) — 23 Arabic + 23 English disclosures.
- [Security Baseline & Threat Model](docs/SECURITY.md).
- [IP Notice](docs/IP_NOTICE.md).
- [Acquisition Technical Overview](docs/ACQUISITION_TECHNICAL_OVERVIEW.md).

### Evidence & Test Closure — Phase 2

- [Acquisition Evidence Catalog](docs/EVIDENCE_CATALOG.md) — EVD-001-EVD-015.
- `app/core.js` — shared testable logic used by the runtime.
- `tests/test_core.mjs` — executable tests for registry continuity, maturity states, risk logic, certificate verification, search/filter and synthetic evidence records.
- `tests/test_evidence_contract.py` — evidence-contract, IP-boundary and disclosure checks.

### Strategic Grade A Closure — Phase 3

Phase 3 upgrades the remaining seven strategic capabilities from Evidence Grade B to Grade A without altering public maturity states:

- F001/F002 → EVD-016.
- F012 → EVD-017.
- F026/F027 → EVD-018.
- F034 → EVD-019.
- F060 → EVD-020.

Result: **all 12 selected strategic capabilities now have automated + runtime evidence paths**.

- [Phase 3 Grade A Evidence](docs/PHASE3_GRADE_A_EVIDENCE.md).
- [Strategic Capability Evidence Matrix](docs/STRATEGIC_EVIDENCE_MATRIX.md).
- `tests/test_phase3.mjs` — executable Grade A tests for registry/identity, geofence, Mazayen scoring, auction transitions and audit events.

### Run locally

```bash
python3 -m http.server 4173
```

Then open `http://localhost:4173/`.

### Validate and test

```bash
python scripts/validate.py
node tests/test_core.mjs
node tests/test_phase3.mjs
python tests/test_evidence_contract.py
```

### Core documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Evidence Matrix](docs/EVIDENCE.md)
- [Public Overview](docs/PUBLIC_OVERVIEW.md)
- [Source Reconciliation](docs/SOURCE_RECONCILIATION.md)
- [Algorithm & Engine Registry](docs/ALGORITHM_ENGINE_REGISTRY.md)
- [System Families](docs/SYSTEM_FAMILIES.md)

### Disclosure boundary

All demonstration records are synthetic or illustrative unless explicitly stated otherwise. Sensor streams, AI outputs, valuations and external integrations do not represent production deployment or live government connectivity. Proprietary algorithms, model weights, training datasets, confidential scoring models, partner data and private due-diligence records are excluded from the public repository.
