# SMART Camel AI MVP | منصة الإبل الذكية

## العربية

منصة الإبل الذكية هي بيئة رقمية متكاملة لإدارة دورة حياة الإبل والقطعان والمزارع والصحة والتكاثر والأنساب والمراعي والمسابقات والسباقات والمزادات والأسواق والمنتجات والمخاطر والبيانات التشغيلية ضمن واجهة موحدة قابلة للتدقيق.

هذا المستودع هو الإصدار العام التجريبي للمنصة، والغرض منه تقديم نموذج أولي قابل للتشغيل والمراجعة التقنية دون نشر الخوارزميات الخاصة أو الأسرار التنفيذية أو وثائق الملكية الفكرية الداخلية.

### ما الذي يعمل في هذا الإصدار

- واجهة عربية وإنجليزية مع تبديل فوري بين اللغتين.
- لوحة قيادة تشغيلية ببيانات اصطناعية.
- سجل إبل تجريبي.
- 60 قدرة مسجلة ومصنفة حسب حالة النضج.
- محرك مخاطر صحي تفاعلي تفسيري.
- مركز تنبيهات للمخاطر الصحية والجغرافية.
- محاكاة مزايدة وتسجيل حدثها.
- تحقق تجريبي من شهادة CAMEL-001.
- سجل أحداث لجلسة العرض.
- توثيق معماري ومصفوفة أدلة عامة.

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

### حدود الإفصاح

جميع بيانات العرض اصطناعية أو توضيحية ما لم يُذكر خلاف ذلك. بيانات المستشعرات، مخرجات الذكاء الاصطناعي، التقييمات والتكاملات الخارجية في هذا الإصدار لا تمثل تشغيلًا إنتاجيًا أو ربطًا حكوميًا حيًا. لا يحتوي المستودع العام على الخوارزميات المملوكة أو نماذج التقييم السرية أو بيانات الشركاء أو وثائق العناية الواجبة الخاصة.

## English

SMART Camel AI is an integrated digital operating environment for camel lifecycle management, herd and farm operations, health, breeding, lineage, grazing, competitions, racing, auctions, marketplaces, products, risk and operational intelligence within one auditable interface.

This repository contains the public demonstrator of the platform. It is designed for executable demonstration and technical review without exposing proprietary algorithms, protected implementation details or confidential intellectual-property records.

### What works in this release

- Arabic and English interface with instant language switching.
- Operational dashboard using synthetic data.
- Demonstration camel registry.
- 60 registered capabilities classified by maturity status.
- Interactive explainable health-risk engine.
- Health and geospatial risk alert center.
- Demonstration auction bid with event logging.
- Demonstration certificate verification for CAMEL-001.
- In-session audit event trail.
- Architecture documentation and public evidence matrix.

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

### Disclosure boundary

All demonstration records are synthetic or illustrative unless explicitly stated otherwise. Sensor streams, artificial-intelligence outputs, valuations and external integrations in this release do not represent production deployment or live government connectivity. Proprietary algorithms, confidential scoring models, partner data and private due-diligence records are excluded from the public repository.
