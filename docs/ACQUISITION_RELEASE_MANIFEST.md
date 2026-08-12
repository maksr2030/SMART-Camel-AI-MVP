# Acquisition Release Manifest | بيان إصدار الاستحواذ

## العربية

### هوية الحزمة

- **المنتج:** SMART Camel AI.
- **حالة الحزمة:** Acquisition Demonstrator Release package — جاهزة لتثبيت tag النهائي.
- **النطاق الحالي:** **245 قدرة معيارية F001-F245**.
- **الخوارزميات والمحركات المسماة:** **29** اسماً موثقاً في المصدر.
- **نماذج التدريب المسماة:** **2**.
- **العائلات النظامية:** **20**.
- **Evidence IDs:** **EVD-001-EVD-020**.
- **المجموعة الاستراتيجية:** **12/12 Grade A Evidence — Automated + Runtime**.

### القدرات الأخيرة في النطاق

- **F244 — Genetic Breeding with Environmental Impact Analysis — Planned.**
- **F245 — Positive Environmental Impact Evaluation for Camel Breeding — Planned.**

وجودهما يثبت اكتمال النطاق المعياري الحالي ولا يعني نشرهما إنتاجياً.

### العرض الحي

- URL: `https://maksr2030.github.io/SMART-Camel-AI-MVP/`
- GitHub Pages: `built`
- Source: `main/(root)`
- Public: yes
- HTTPS: enforced
- Evidence: `docs/LIVE_DEMO_VERIFICATION.md`

بذلك **G08 مغلقة**.

### سلسلة التحقق الإلزامية

```bash
python scripts/validate.py
node tests/test_core.mjs
node tests/test_phase3.mjs
node tests/test_phase4.mjs
python tests/test_evidence_contract.py
python scripts/security_check.py
python scripts/release_check.py
```

### أدلة CI

- PR #6 دمج Phase 4 إلى `main`.
- GitHub Actions Run #122 اجتاز validator وCore وPhase 3 وPhase 4 وEvidence Contract وSecret Scan وRelease Contract بنجاح.

### وثائق العناية الواجبة العامة

1. `README.md`
2. `docs/ACQUISITION_TECHNICAL_OVERVIEW.md`
3. `docs/FEATURE_REGISTRY.md`
4. `docs/PHASE4_245_RECONCILIATION.md`
5. `docs/SOURCE_RECONCILIATION.md`
6. `docs/DEMO_SCENARIOS.md`
7. `docs/EVIDENCE_CATALOG.md`
8. `docs/PHASE3_GRADE_A_EVIDENCE.md`
9. `docs/STRATEGIC_EVIDENCE_MATRIX.md`
10. `docs/KNOWN_LIMITATIONS.md`
11. `docs/SECURITY.md`
12. `docs/DEPENDENCY_AND_LICENSE_REVIEW.md`
13. `docs/IP_NOTICE.md`
14. `docs/RELEASE_READINESS.md`
15. `docs/LIVE_DEMO_VERIFICATION.md`
16. `docs/RELEASE_NOTES_v1.0-acquisition-demo.md`

### بوابة النشر النهائية

المتبقي لإغلاق G09 هو إنشاء tag ثابت:

`v1.0-acquisition-demo`

على commit النهائي بعد دمج Release Finalization.

### الحدود

هذا الإصدار **Acquisition Demonstrator Release** وليس Production Release. لا يثبت backend إنتاجياً أو أجهزة حية أو تكاملات حكومية حية أو إيرادات أو اكتمال Chain of Title السرية.

## English

This manifest defines the buyer-facing SMART Camel AI Acquisition Demonstrator Release package.

Current scope:

- **245 canonical capabilities, F001-F245**
- **29 source-documented named algorithms/engines**
- **2 named training models**
- **20 canonical system families**
- **EVD-001-EVD-020**
- **12/12 selected strategic capabilities at Evidence Grade A**

The live GitHub Pages demonstrator is verified as built, public and HTTPS-enforced from `main/(root)` at `https://maksr2030.github.io/SMART-Camel-AI-MVP/`, closing G08.

The remaining public release action is G09: publish the fixed `v1.0-acquisition-demo` tag on the final Release Finalization commit. This package remains distinct from Production Readiness.
