# Acquisition Release Manifest | بيان إصدار الاستحواذ

## العربية

### هوية الحزمة

- **المنتج:** SMART Camel AI MVP.
- **نوع الحزمة:** Public Acquisition Demonstrator Candidate — قبل اعتماد الرابط الحي والـrelease tag.
- **النطاق الحالي:** **245 قدرة معيارية F001-F245**.
- **الخوارزميات والمحركات المسماة:** **29** اسماً موثقاً في المصدر.
- **نماذج التدريب المسماة:** **2**.
- **العائلات النظامية:** **20**.
- **Evidence IDs:** **EVD-001-EVD-020**.
- **المجموعة الاستراتيجية:** **12/12 Grade A Evidence — Automated + Runtime**.

### القدرات الأخيرة في النطاق

- **F244 — Genetic Breeding with Environmental Impact Analysis — Planned.**
- **F245 — Positive Environmental Impact Evaluation for Camel Breeding — Planned.**

وجودهما في الحزمة يثبت اكتمال النطاق المعياري الحالي ولا يعني نشرهما إنتاجياً.

### نقطة تشغيل الـMVP

- `index.html`
- ملفات البيانات/القدرات المحلية تحت `app/`.
- `app/core.js` للمنطق العام المشترك بين runtime والاختبارات.
- لا يتطلب runtime العام package manager أو قاعدة بيانات أو مفاتيح سرية.

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

لا تعتبر الحزمة مرشح إصدار استحواذ صالحاً إذا فشل أي أمر من هذه الأوامر.

### وثائق العناية الواجبة العامة

1. `README.md` — نقطة الدخول العامة.
2. `docs/ACQUISITION_TECHNICAL_OVERVIEW.md` — النظرة التقنية للمستحوذ.
3. `docs/FEATURE_REGISTRY.md` — سجل Phase 1 التفصيلي F001-F243.
4. `docs/PHASE4_245_RECONCILIATION.md` — إغلاق F244-F245 والنطاق الحالي F001-F245.
5. `docs/SOURCE_RECONCILIATION.md` — منهج المطابقة وإزالة التكرار.
6. `docs/DEMO_SCENARIOS.md` — D01-D10.
7. `docs/EVIDENCE_CATALOG.md` و`docs/PHASE3_GRADE_A_EVIDENCE.md` — Evidence IDs.
8. `docs/STRATEGIC_EVIDENCE_MATRIX.md` — 12/12 Grade A.
9. `docs/KNOWN_LIMITATIONS.md` — 23 قيداً عربياً + 23 إنجليزياً.
10. `docs/SECURITY.md` — Threat Model وضوابط Phase 4 العامة.
11. `docs/DEPENDENCY_AND_LICENSE_REVIEW.md` — سطح الاعتماديات وحدود الترخيص.
12. `docs/IP_NOTICE.md` — حدود الملكية العامة ومتطلبات Chain of Title.
13. `docs/RELEASE_READINESS.md` — بوابات G01-G15.

### حالة البوابات غير المغلقة علناً

تبقى العناصر التالية خارج ادعاء الجاهزية الحالية:

- **Live Stable Demo:** Pending حتى تحقق رابط حي فعلياً من خارج بيئة المطور.
- **Fixed Acquisition Release Tag:** Pending حتى CI النهائي + live demo verification.
- **Chain of Title:** Pending Confidential داخل Data Room.
- **Production Security / Backend / Field Validation / Commercial Evidence / Independent Validation:** مراحل منفصلة.

### قاعدة الإصدار

لا يجوز وصف هذه الحزمة بأنها Production Ready. الوصف الصحيح قبل إغلاق G08/G09 هو **Acquisition Demonstrator Candidate**. بعد اجتياز PR CI النهائي والتحقق المستقل من الرابط الحي يمكن إنشاء tag استحواذ ثابت، من دون أن يتحول ذلك تلقائياً إلى ادعاء Production Ready.

## English

This manifest defines the buyer-facing public SMART Camel AI acquisition package.

Current normalized scope:

- **245 canonical capabilities, F001-F245.**
- **29 source-documented named algorithms/engines.**
- **2 named training models.**
- **20 canonical system families.**
- **EVD-001-EVD-020.**
- **12/12 selected strategic capabilities at Evidence Grade A — Automated + Runtime.**

F244 and F245 are included as source-backed Planned capabilities. The mandatory validation chain is `validate.py`, core/Phase3/Phase4 tests, evidence contract, security check and release check.

A stable live demo, fixed acquisition release tag, confidential Chain of Title, production security/backend, field validation, commercial evidence and independent validation remain separate gates. Until the live-demo and final-PR gates are closed, the correct designation is **Acquisition Demonstrator Candidate**, not Production Ready.
