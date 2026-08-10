# SMART Camel AI MVP | منصة الإبل الذكية

## العربية

منصة الإبل الذكية هي بيئة رقمية متكاملة لإدارة دورة حياة الإبل والقطعان والمزارع والصحة والتكاثر والأنساب والمراعي والمسابقات والسباقات والمزادات والأسواق والمنتجات والمخاطر والبيانات التشغيلية ضمن واجهة موحدة قابلة للتدقيق.

هذا المستودع هو الإصدار العام التجريبي للمنصة، والغرض منه تقديم نموذج أولي قابل للتشغيل والمراجعة التقنية دون نشر الخوارزميات الخاصة أو الأسرار التنفيذية أو وثائق الملكية الفكرية الداخلية.

### ما الذي يعمل في هذا الإصدار

- واجهة عربية وإنجليزية مع تبديل فوري بين اللغتين.
- لوحة قيادة تشغيلية ببيانات اصطناعية.
- سجل إبل تجريبي.
- 235 سجل قدرة موحداً في السجل العام الحالي ومصنفاً حسب حالة النضج بعد مطابقة موسعة مع ملفات المنصة الأصلية ومواد براءة الاختراع والملفات البيطرية والتشغيلية الأخيرة.
- محرك مخاطر صحي تفاعلي تفسيري.
- مركز تنبيهات للمخاطر الصحية والجغرافية.
- محاكاة مزايدة وتسجيل حدثها.
- تحقق تجريبي من شهادة CAMEL-001.
- سجل أحداث لجلسة العرض.
- توثيق معماري ومصفوفة أدلة عامة.
- وثيقة مستقلة تشرح منهج مطابقة ملفات المصدر القديمة وتحويلها إلى سجل موحد.

ملاحظة منهجية: الرقم 235 هو عدد سجلات القدرات المعيارية التي جرى توحيدها حتى هذه المرحلة من مطابقة محفظة المصدر. لا يعني أن الوثائق التاريخية استخدمت تسلسلاً واحداً من 1 إلى 235، ولا يعني أن جميع القدرات منشورة كأنظمة إنتاجية. بعض السجلات تمثل محركات أو تدفقات أو قدرات فرعية مستقلة داخل عائلات أكبر.

أضيفت F224-F231 بعد مراجعة مصادر إضافية تضمنت وثيقة براءة مختصرة ووثائق تشغيل تفصيلية. تشمل هذه الطبقة تشفير ما بعد الكم، التهجين المحسن حسب حالة الاستخدام، التقييمات الصحية والجينية قبل التجارة، التقييم الآلي للمسابقات، توليد النتائج في الزمن الحقيقي، مطابقة المهرجانات، وتكامل الجهات البيطرية.

أضيفت F232-F235 بعد مراجعة المجموعة الأخيرة من الملفات، وبالأخص ملف منصة الطب البيطري وإدارة الكفاءة الجينية وملفات إدارة المزارع. وتشمل توثيق صحة الإبل المشاركة في المهرجانات، تتبع الموقع والسرعة أثناء السباقات، تتبع الإنتاجية عبر دورة حياة الجمل، وتوصيات الطاقة المتجددة للمزارع. لم تُكرر الاستشارات البيطرية أو التحليل الغذائي أو الكفاءة الجينية لأنها كانت موجودة بالفعل في السجل المعياري.

جميع هذه القدرات موسومة بحالة النضج الفعلية في الإصدار العام، ولا يتم تقديم القدرات المصدرية أو الموثقة ببراءة على أنها نشر إنتاجي حي.

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

### التوثيق

- [المعمارية | Architecture](docs/ARCHITECTURE.md)
- [مصفوفة الأدلة | Evidence Matrix](docs/EVIDENCE.md)
- [النظرة العامة | Public Overview](docs/PUBLIC_OVERVIEW.md)
- [مطابقة ميزات المصادر | Source Reconciliation](docs/SOURCE_RECONCILIATION.md)

### حدود الإفصاح

جميع بيانات العرض اصطناعية أو توضيحية ما لم يُذكر خلاف ذلك. بيانات المستشعرات، مخرجات الذكاء الاصطناعي، التقييمات والتكاملات الخارجية في هذا الإصدار لا تمثل تشغيلًا إنتاجيًا أو ربطًا حكوميًا حيًا. لا يحتوي المستودع العام على الخوارزميات المملوكة أو نماذج التقييم السرية أو بيانات الشركاء أو وثائق العناية الواجبة الخاصة.

## English

SMART Camel AI is an integrated digital operating environment for camel lifecycle management, herd and farm operations, health, breeding, lineage, grazing, competitions, racing, auctions, marketplaces, products, risk and operational intelligence within one auditable interface.

This repository contains the public demonstrator of the platform. It is designed for executable demonstration and technical review without exposing proprietary algorithms, protected implementation details or confidential intellectual-property records.

### What works in this release

- Arabic and English interface with instant language switching.
- Operational dashboard using synthetic data.
- Demonstration camel registry.
- 235 normalized capability records in the current public registry, classified by maturity status after expanded reconciliation against original platform source material, patent-related documentation, and the final veterinary and operating files reviewed.
- Interactive explainable health-risk engine.
- Health and geospatial risk alert center.
- Demonstration auction bid with event logging.
- Demonstration certificate verification for CAMEL-001.
- In-session audit event trail.
- Architecture documentation and public evidence matrix.
- A dedicated source-reconciliation document explaining how legacy source files were converted into the normalized registry.

Method note: 235 is the number of canonical capability records normalized at this stage of source-portfolio reconciliation. It does not imply that historical source material used one continuous 1-to-235 numbering scheme, and it does not mean all capabilities are production-deployed. Some records represent independent engines, workflows or sub-capabilities within larger capability families.

F224-F231 were added after reviewing additional sources including a concise patent document and detailed operating documentation. This layer covers post-quantum encryption, use-case optimized hybrid breeding, automated pre-trade health and genetic evaluation, automated competition scoring, real-time result generation, festival suitability matching and a veterinary-authority integration adapter.

F232-F235 were added after reviewing the final uploaded source group, particularly the veterinary/genetic-efficiency platform and farm-management material. They cover festival-participant health documentation, real-time race GPS and speed tracking, lifecycle productivity tracking, and renewable-energy recommendations for camel farms. Remote veterinary consultation, nutritional analysis and genetic-efficiency management were not counted again because they were already represented in the canonical registry.

All capabilities retain explicit public maturity classifications and source documentation is not represented as live production deployment.

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

### Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Evidence Matrix](docs/EVIDENCE.md)
- [Public Overview](docs/PUBLIC_OVERVIEW.md)
- [Source Reconciliation](docs/SOURCE_RECONCILIATION.md)

### Disclosure boundary

All demonstration records are synthetic or illustrative unless explicitly stated otherwise. Sensor streams, artificial-intelligence outputs, valuations and external integrations in this release do not represent production deployment or live government connectivity. Proprietary algorithms, confidential scoring models, partner data and private due-diligence records are excluded from the public repository.
