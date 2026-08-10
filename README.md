# SMART Camel AI MVP | منصة الإبل الذكية

## العربية

منصة الإبل الذكية هي بيئة رقمية متكاملة لإدارة دورة حياة الإبل والقطعان والمزارع والصحة والتكاثر والأنساب والمراعي والمسابقات والسباقات والمزادات والأسواق والمنتجات والمخاطر والبيانات التشغيلية ضمن واجهة موحدة قابلة للتدقيق.

هذا المستودع هو الإصدار العام التجريبي للمنصة، والغرض منه تقديم نموذج أولي قابل للتشغيل والمراجعة التقنية دون نشر الخوارزميات الخاصة أو الأسرار التنفيذية أو وثائق الملكية الفكرية الداخلية.

### النتيجة المعيارية الحالية

بعد إتمام المطابقة النهائية لمحفظة المصدر التاريخية ومواد البراءة والملفات البيطرية والتشغيلية وملفات الخوارزميات الأخيرة، أصبح السجل العام يتكون من:

- **243 سجل قدرة معيارية** من F001 إلى F243.
- **29 خوارزمية ومحركاً مسمىً وموثقاً في المصدر** ضمن سجل مستقل، دون نشر الأكواد أو الأوزان الخاصة.
- **20 عائلة نظامية معيارية** تنظّم القدرات في طبقة معمارية أعلى.
- **نموذجَي تدريب مسميين في المصدر** موثقين بشكل منفصل عن الخوارزميات.

هذه الأرقام لا تعني وجود 243 نظاماً إنتاجياً أو 29 نموذجاً معتمداً. هي أرقام توثيقية معيارية مبنية على مطابقة المصدر، بينما حالة النضج التشغيلية معلنة لكل قدرة.

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
- توثيق معماري ومصفوفة أدلة عامة.
- منهج مستقل لمطابقة ملفات المصدر القديمة.
- سجل عام للخوارزميات والمحركات المسمّاة دون إفشاء التنفيذ المملوك.
- خريطة من 20 عائلة نظامية لعرض البنية بصورة قابلة للعناية الواجبة.

### الطبقة النهائية F236-F243

أضيفت ثماني قدرات مستقلة بعد المقارنة النهائية مع F001-F235:

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

من جذر المستودع:

```bash
python3 -m http.server 4173
```

ثم افتح:

```text
http://localhost:4173/
```

لا يحتاج النموذج العام إلى حزم خارجية.

### التحقق

```bash
python scripts/validate.py
```

يفحص المدقق وجود الملفات الأساسية، وتسلسل F001-F243 دون فجوات أو تكرار، وربط أصول الواجهة، ووجود سجلي الخوارزميات والعائلات النظامية.

### التوثيق

- [المعمارية | Architecture](docs/ARCHITECTURE.md)
- [مصفوفة الأدلة | Evidence Matrix](docs/EVIDENCE.md)
- [النظرة العامة | Public Overview](docs/PUBLIC_OVERVIEW.md)
- [مطابقة ميزات المصادر | Source Reconciliation](docs/SOURCE_RECONCILIATION.md)
- [سجل الخوارزميات والمحركات | Algorithm & Engine Registry](docs/ALGORITHM_ENGINE_REGISTRY.md)
- [عائلات الأنظمة | System Families](docs/SYSTEM_FAMILIES.md)

### حدود الإفصاح

جميع بيانات العرض اصطناعية أو توضيحية ما لم يُذكر خلاف ذلك. بيانات المستشعرات، مخرجات الذكاء الاصطناعي، التقييمات والتكاملات الخارجية في هذا الإصدار لا تمثل تشغيلًا إنتاجيًا أو ربطًا حكوميًا حيًا. لا يحتوي المستودع العام على الخوارزميات المملوكة أو الأوزان أو مجموعات التدريب أو نماذج التقييم السرية أو بيانات الشركاء أو وثائق العناية الواجبة الخاصة.

## English

SMART Camel AI is an integrated digital operating environment for camel lifecycle management, herd and farm operations, health, breeding, lineage, grazing, competitions, racing, auctions, marketplaces, products, risk and operational intelligence within one auditable interface.

This repository contains the public demonstrator of the platform. It is designed for executable demonstration and technical review without exposing proprietary algorithms, protected implementation details or confidential intellectual-property records.

### Current normalized result

After final reconciliation of the historical source portfolio, patent-related material, veterinary and operating documentation, and the final algorithm-focused files, the public record now contains:

- **243 canonical capability records**, F001 through F243.
- **29 source-documented named algorithms and engines** in a separate registry without publishing proprietary code or weights.
- **20 canonical system families** organizing the capabilities at a higher architectural level.
- **Two independently named training models** documented separately from the algorithm registry.

These numbers do not claim 243 production systems or 29 validated production models. They are normalized documentation counts derived from source reconciliation, while operational maturity remains explicit for each capability.

### What works in this release

- Arabic and English interface with instant language switching.
- Operational dashboard using synthetic data.
- Demonstration camel registry.
- Complete F001-F243 capability registry with maturity classification.
- Interactive explainable health-risk engine.
- Health and geospatial risk alert center.
- Demonstration auction bid with event logging.
- Demonstration certificate verification for CAMEL-001.
- In-session audit event trail.
- Architecture documentation and public evidence matrix.
- Dedicated source-reconciliation methodology.
- Public named-algorithm/engine registry without proprietary implementation disclosure.
- Twenty-family system map for due-diligence-friendly architecture review.

### Final layer F236-F243

Eight independent capabilities were accepted after final comparison against F001-F235:

- F236: AI Camel Breed Recognition.
- F237: Closed-Loop Adaptive Feeding Control.
- F238: Facial Biometric Camel Identification.
- F239: Thermal-Camera Health Monitoring.
- F240: Camel Sleep Monitoring and Quality Analysis.
- F241: Camel Heat-Stress Early Warning.
- F242: Genetic Disease Risk Analysis.
- F243: Pregnancy and Labor Monitoring.

These records remain **Planned** in the public release because the source files establish functional design identity, not current production deployment.

### Maturity statuses

- Implemented: directly implemented in the public demonstrator.
- Demonstrated: visible functional workflow but not a complete production subsystem.
- Simulated: output or engine uses synthetic data or simplified logic.
- Mock Integration: represented integration point without a live external connection.
- Planned: part of the platform architecture but not yet activated in the public runtime.

### Run locally

From the repository root:

```bash
python3 -m http.server 4173
```

Then open:

```text
http://localhost:4173/
```

No external packages are required for the public demonstrator.

### Validate

```bash
python scripts/validate.py
```

The validator checks required files, continuous F001-F243 identifiers without duplicates or gaps, front-end asset references, and the algorithm/engine and system-family registries.

### Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Evidence Matrix](docs/EVIDENCE.md)
- [Public Overview](docs/PUBLIC_OVERVIEW.md)
- [Source Reconciliation](docs/SOURCE_RECONCILIATION.md)
- [Algorithm & Engine Registry](docs/ALGORITHM_ENGINE_REGISTRY.md)
- [System Families](docs/SYSTEM_FAMILIES.md)

### Disclosure boundary

All demonstration records are synthetic or illustrative unless explicitly stated otherwise. Sensor streams, artificial-intelligence outputs, valuations and external integrations in this release do not represent production deployment or live government connectivity. Proprietary algorithms, model weights, training datasets, confidential scoring models, partner data and private due-diligence records are excluded from the public repository.
