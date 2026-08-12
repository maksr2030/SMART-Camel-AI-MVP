# SMART Camel AI — v1.0-acquisition-demo

## العربية

### الحالة

**ملاحظات إصدار جاهزة مسبقاً — لا يوجد tag نهائي بعد.**

لا يجوز نشر هذا المستند كإصدار نهائي أو إنشاء tag `v1.0-acquisition-demo` قبل:

1. نجاح PR CI على الـhead النهائي.
2. دمج التغييرات إلى `main`.
3. نجاح GitHub Pages deployment.
4. التحقق الخارجي من الرابط الحي.
5. إغلاق G08 وG09 في `docs/RELEASE_READINESS.md`.

### نطاق الإصدار

- **245 قدرة معيارية F001-F245**.
- **29 خوارزمية ومحركاً مسمىً وموثقاً في المصدر**.
- **2 نموذجَي تدريب مسميين في المصدر**.
- **20 عائلة نظامية معيارية**.
- **EVD-001-EVD-020**.
- **12/12 قدرة استراتيجية عند Evidence Grade A — Automated + Runtime**.

### إضافات Phase 4

- F244 — Genetic Breeding with Environmental Impact Analysis — Planned.
- F245 — Positive Environmental Impact Evaluation for Camel Breeding — Planned.
- بوابة CI تمنع نقص أو تكرار أي F-ID من F001 إلى F245.
- اختبار Phase 4 مستقل.
- Security release check للأسرار والملفات الحساسة.
- Dependency & License review.
- Acquisition Release Manifest.
- G01-G15 Release Readiness Matrix.
- GitHub Pages deployment workflow للواجهة العامة فقط.

### العرض القابل للفحص

المراجع يستطيع اختبار:

- الواجهة العربية/الإنجليزية.
- سجل الإبل الاصطناعي.
- البحث والفلترة في F001-F245.
- Health-risk simulation.
- Geofence demonstrator.
- Mazayen scoring demonstrator.
- Auction state-transition demonstrator.
- CAMEL-001 certificate verification.
- In-session bilingual audit trail.

### سلسلة التحقق

```bash
python scripts/validate.py
node tests/test_core.mjs
node tests/test_phase3.mjs
node tests/test_phase4.mjs
python tests/test_evidence_contract.py
python scripts/security_check.py
python scripts/release_check.py
```

### الحدود

هذا الإصدار هو **Acquisition Demonstrator Release** عند إغلاق G08/G09، وليس Production Release.

لا يثبت:

- نشر 245 قدرة إنتاجياً.
- backend أو database أو IAM إنتاجي.
- أجهزة IoT أو GPS أو كاميرات حية.
- اعتماداً بيطرياً أو حكومياً.
- تكاملات حكومية/بيطرية حية.
- إيرادات أو عقوداً أو شراكات.
- اكتمال Chain of Title السرية.
- اعتماداً أمنياً مستقلاً.

## English

### Status

**Pre-authored release notes — no final tag exists yet.**

The `v1.0-acquisition-demo` tag must not be created until final PR CI succeeds, the branch is merged to `main`, GitHub Pages deploys successfully, the live URL is externally verified, and G08/G09 are closed.

### Release scope

- **245 canonical capabilities, F001-F245.**
- **29 source-documented named algorithms/engines.**
- **2 named training models.**
- **20 canonical system families.**
- **EVD-001-EVD-020.**
- **12/12 selected strategic capabilities at Evidence Grade A — Automated + Runtime.**

Phase 4 adds source-backed F244/F245, dedicated 245-capability tests, security/release checks, dependency/license diligence, buyer-facing release manifests and a GitHub Pages deployment workflow.

Once G08/G09 are closed, this package may be designated **Acquisition Demonstrator Release**. It remains distinct from Production Readiness and does not claim live institutional integrations, field devices, production backend/security, commercial revenue or completed confidential Chain of Title.
