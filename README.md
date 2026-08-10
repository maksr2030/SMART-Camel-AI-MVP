# SMART Camel AI MVP | منصة الإبل الذكية

## العربية

منصة الإبل الذكية هي بيئة رقمية متكاملة لإدارة دورة حياة الإبل والقطعان والمزارع والصحة والتكاثر والأنساب والمراعي والمسابقات والسباقات والمزادات والأسواق والمنتجات والمخاطر والبيانات التشغيلية ضمن واجهة موحدة قابلة للتدقيق.

هذا المستودع هو الإصدار العام التجريبي للمنصة، والغرض منه تقديم نموذج أولي قابل للتشغيل والمراجعة التقنية دون نشر الخوارزميات الخاصة أو الأسرار التنفيذية أو وثائق الملكية الفكرية الداخلية.

### النتيجة المعيارية الحالية

- **243 سجل قدرة معيارية** من F001 إلى F243.
- **29 خوارزمية ومحركاً مسمىً وموثقاً في المصدر** ضمن سجل مستقل.
- **20 عائلة نظامية معيارية**.
- **نموذجَي تدريب مسميين في المصدر** موثقين بشكل منفصل.
- **15 Evidence IDs** من EVD-001 إلى EVD-015 في طبقة Evidence & Test Closure الحالية.

هذه الأرقام لا تعني وجود 243 نظاماً إنتاجياً أو 29 نموذجاً معتمداً. حالة النضج التشغيلية معلنة لكل قدرة، والأدلة العامة تفرق صراحة بين الاختبار الآلي، السلوك القابل للتشغيل، الدليل البنيوي، والتوثيق.

### ما الذي يعمل في هذا الإصدار

- واجهة عربية وإنجليزية مع تبديل فوري بين اللغتين.
- لوحة قيادة تشغيلية ببيانات اصطناعية.
- سجل إبل تجريبي.
- سجل قدرات كامل F001-F243 مصنف حسب حالة النضج.
- محرك مخاطر صحي تفاعلي تفسيري.
- مركز تنبيهات للمخاطر الصحية والجغرافية.
- محاكاة مزايدة وتسجيل حدثها.
- تحقق تجريبي من شهادة CAMEL-001.
- سجل أحداث لجلسة العرض.
- سجل عام للخوارزميات والمحركات المسمّاة دون إفشاء التنفيذ المملوك.
- خريطة من 20 عائلة نظامية.
- Core Logic مشترك بين الواجهة والاختبارات للبحث والفلترة وحساب المخاطر والتحقق من الشهادة.

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

بدأت المرحلة الثانية بتحويل الادعاءات العامة إلى أدلة قابلة للاختبار والتتبع:

- [سجل أدلة الاستحواذ | Acquisition Evidence Catalog](docs/EVIDENCE_CATALOG.md) — EVD-001 إلى EVD-015.
- `app/core.js` — منطق عام قابل للاختبار تستخدمه الواجهة نفسها.
- `tests/test_core.mjs` — اختبارات السجل F001-F243، حالات النضج، المخاطر الصحية، التحقق من الشهادة، البحث والفلترة، والسجلات الاصطناعية.
- `tests/test_evidence_contract.py` — اختبار سلامة Evidence IDs، حدود الملكية الفكرية، القيود المعروفة، وربط الـCore بالواجهة.

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
- **15 acquisition Evidence IDs**, EVD-001 through EVD-015, in the current Evidence & Test Closure layer.

These counts do not claim 243 production systems or 29 validated production models. Maturity and evidence class remain explicit.

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

### Run locally

```bash
python3 -m http.server 4173
```

Then open `http://localhost:4173/`.

### Validate and test

```bash
python scripts/validate.py
node tests/test_core.mjs
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
