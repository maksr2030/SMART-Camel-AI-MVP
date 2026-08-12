# SMART Camel AI — v1.0-acquisition-demo

## العربية

### الحالة

**Release package finalized — tag publication pending.**

تم إغلاق شروط ما قبل الـtag التالية:

1. نجاح PR CI على الـhead النهائي.
2. دمج Phase 4 إلى `main` عبر PR #6.
3. نجاح النشر الفعلي على GitHub Pages من `main/(root)`.
4. التحقق من أن Pages بحالة `built` وموقعها Public وHTTPS مفعل.
5. إغلاق G08 — Live Stable Demo.

المتبقي فقط لإغلاق G09 هو إنشاء tag:

`v1.0-acquisition-demo`

على commit النهائي بعد دمج Release Finalization.

### نطاق الإصدار

- **245 قدرة معيارية F001-F245**.
- **29 خوارزمية ومحركاً مسمىً وموثقاً في المصدر**.
- **2 نموذجَي تدريب مسميين في المصدر**.
- **20 عائلة نظامية معيارية**.
- **EVD-001-EVD-020**.
- **12/12 قدرة استراتيجية عند Evidence Grade A — Automated + Runtime**.

### العرض الحي

`https://maksr2030.github.io/SMART-Camel-AI-MVP/`

مصدر النشر: `main/(root)`.

### إضافات Phase 4 والإصدار

- F244 — Genetic Breeding with Environmental Impact Analysis — Planned.
- F245 — Positive Environmental Impact Evaluation for Camel Breeding — Planned.
- CI يمنع نقص أو تكرار أي F-ID من F001 إلى F245.
- اختبار Phase 4 مستقل.
- Security release check للأسرار والملفات الحساسة.
- Dependency & License review.
- Acquisition Release Manifest.
- G01-G15 Release Readiness Matrix.
- Live Demo Verification evidence.
- إزالة workflow Pages المخصص بعد اعتماد النشر المباشر من `main/(root)` لتجنب Actions فاشلة زائدة.

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

هذا الإصدار هو **Acquisition Demonstrator Release** عند نشر tag النهائي، وليس Production Release.

لا يثبت:

- نشر 245 قدرة إنتاجياً.
- backend/database/IAM إنتاجي.
- أجهزة IoT/GPS/كاميرات حية.
- اعتماداً بيطرياً أو حكومياً.
- تكاملات حكومية/بيطرية حية.
- إيرادات أو عقوداً أو شراكات.
- اكتمال Chain of Title السرية.
- اعتماداً أمنياً مستقلاً.

## English

The SMART Camel AI `v1.0-acquisition-demo` package is finalized for tag publication.

Pre-tag gates are closed: final PR CI passed, Phase 4 was merged to `main`, GitHub Pages is live from `main/(root)`, the site is built/public/HTTPS-enforced, and G08 is Ready.

Release scope:

- **245 canonical capabilities, F001-F245**
- **29 source-documented named algorithms/engines**
- **2 named training models**
- **20 canonical system families**
- **EVD-001-EVD-020**
- **12/12 selected strategic capabilities at Evidence Grade A**

Live demonstrator: `https://maksr2030.github.io/SMART-Camel-AI-MVP/`

The remaining public release action is to publish the fixed `v1.0-acquisition-demo` tag on the final Release Finalization commit. This release is an Acquisition Demonstrator Release, not a Production Release.
