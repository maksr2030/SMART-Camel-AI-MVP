# SMART Camel AI | منصة الإبل الذكية

## العربية

SMART Camel AI هي بيئة رقمية متكاملة لإدارة دورة حياة الإبل والقطعان والمزارع والصحة والتكاثر والأنساب والمراعي والمسابقات والسباقات والمزادات والأسواق والمنتجات والمخاطر والبيانات التشغيلية ضمن واجهة موحدة قابلة للتدقيق.

هذا المستودع يمثل **Acquisition Demonstrator Release package** مخصصاً للفحص الأولي من مستحوذ أو فريق تقني، مع إبقاء الخوارزميات المملوكة والأوزان ومجموعات التدريب ووثائق الملكية السرية خارج المستودع العام.

### النطاق المعياري الحالي

- **245 قدرة معيارية F001-F245**.
- **29 خوارزمية ومحركاً مسمىً وموثقاً في المصدر**.
- **20 عائلة نظامية معيارية**.
- **2 نموذجَي تدريب مسميين في المصدر**.
- **EVD-001-EVD-020**.
- **12/12 قدرة استراتيجية عند Evidence Grade A — Automated + Runtime**.

هذه الأرقام لا تعني وجود 245 نظاماً Production Ready أو 29 نموذجاً معتمداً إنتاجياً.

### العرض الحي

**https://maksr2030.github.io/SMART-Camel-AI-MVP/**

GitHub Pages موثق حالياً كالتالي:

- Status: `built`
- Source: `main`
- Folder: `/(root)`
- Public: نعم
- HTTPS: مفعل

انظر: [Live Demo Verification](docs/LIVE_DEMO_VERIFICATION.md).

### قدرات العرض العام

- واجهة عربية وإنجليزية.
- سجل إبل اصطناعي مع validation.
- سجل قدرات runtime كامل F001-F245.
- Health-risk simulation.
- Geofence demonstrator.
- Mazayen scoring demonstrator.
- Auction state-transition demonstrator.
- CAMEL-001 certificate verification.
- Bilingual in-session audit trail.
- بحث وفلترة عبر سجل القدرات.

### العناية الواجبة

**Claim → F-ID → Source/Evidence → Maturity → Demo/Test → Limitation → Production Closure Plan**

- [Acquisition Release Manifest](docs/ACQUISITION_RELEASE_MANIFEST.md)
- [Acquisition Technical Overview](docs/ACQUISITION_TECHNICAL_OVERVIEW.md)
- [Phase 4 — 245 Capability Reconciliation](docs/PHASE4_245_RECONCILIATION.md)
- [Evidence Catalog](docs/EVIDENCE_CATALOG.md)
- [Phase 3 Grade A Evidence](docs/PHASE3_GRADE_A_EVIDENCE.md)
- [Strategic Evidence Matrix](docs/STRATEGIC_EVIDENCE_MATRIX.md)
- [Known Limitations](docs/KNOWN_LIMITATIONS.md)
- [Security](docs/SECURITY.md)
- [Dependency & License Review](docs/DEPENDENCY_AND_LICENSE_REVIEW.md)
- [IP Notice](docs/IP_NOTICE.md)
- [Release Readiness](docs/RELEASE_READINESS.md)
- [Live Demo Verification](docs/LIVE_DEMO_VERIFICATION.md)
- [Release Notes v1.0-acquisition-demo](docs/RELEASE_NOTES_v1.0-acquisition-demo.md)

### الاختبارات

```bash
python scripts/validate.py
node tests/test_core.mjs
node tests/test_phase3.mjs
node tests/test_phase4.mjs
python tests/test_evidence_contract.py
python scripts/security_check.py
python scripts/release_check.py
```

PR #6 اجتاز GitHub Actions Run #122 بالكامل قبل الدمج إلى `main`.

### حالة الإصدار

- G01-G08: مغلقة أو Ready ضمن نطاق الـpublic acquisition demonstrator.
- G09: جاهزة للنشر عند إنشاء tag `v1.0-acquisition-demo` على commit النهائي بعد Release Finalization.
- G10-G15: تبقى بوابات منفصلة تخص Chain of Title السرية، Production Security، backend/data، field validation، commercial evidence وindependent validation.

هذا الإصدار **ليس Production Ready** ولا يدعي تكاملات حكومية حية أو أجهزة IoT فعلية أو اعتماداً بيطرياً أو إيرادات مثبتة.

## English

SMART Camel AI is a buyer-facing **Acquisition Demonstrator Release package** for a broader camel-sector operating and intelligence platform.

Current normalized scope:

- **245 canonical capabilities, F001-F245**
- **29 source-documented named algorithms and engines**
- **20 canonical system families**
- **2 named training models**
- **EVD-001-EVD-020**
- **12/12 selected strategic capabilities at Evidence Grade A**

### Live demonstrator

**https://maksr2030.github.io/SMART-Camel-AI-MVP/**

GitHub Pages is verified as built, public and HTTPS-enforced from `main/(root)`.

### Release status

G01-G08 are closed/Ready for the public acquisition demonstrator. G09 closes when the fixed `v1.0-acquisition-demo` tag is published on the final Release Finalization commit. G10-G15 remain separate production, confidential legal, field, commercial and independent-validation diligence gates.

This package is not a Production Release.
