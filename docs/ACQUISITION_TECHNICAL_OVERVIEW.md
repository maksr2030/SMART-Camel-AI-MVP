# Acquisition Technical Overview | النظرة التقنية للاستحواذ

## العربية

### 1. الملخص التنفيذي

SMART Camel AI هي محفظة منصة واسعة النطاق لقطاع الإبل، منظمة حالياً في **245 سجل قدرة معيارية F001-F245، 29 خوارزمية/محركاً مسمىً وموثقاً في المصدر، نموذجَي تدريب مسميين، و20 عائلة نظامية معيارية**. المستودع العام هو Demonstrator قابل للتشغيل والمراجعة، وليس النسخة الإنتاجية الكاملة ولا مخزن الملكية الفكرية السرية.

كان baseline التاريخي في Phase 1 يقف عند F243. أضافت Phase 4 قدرتين مصدرّيتين مستقلتين F244 وF245، ويعامل runtime والـCI النطاق الحالي باعتباره F001-F245.

هدف حزمة العناية الواجبة هو تمكين المستحوذ من التمييز بسرعة بين:

- ما هو منفذ في الـMVP العام.
- ما هو قابل للاستعراض كمسار وظيفي.
- ما هو محاكاة.
- ما هو Mock Integration.
- ما هو موثق في المصدر لكنه Planned.
- ما يبقى سرياً داخل Data Room ولا ينبغي نشره للعامة.

### 2. الأصول التقنية العامة الحالية

- واجهة عربية/إنجليزية ثابتة قابلة للتشغيل بلا حزم runtime خارجية.
- سجل runtime مستمر **F001-F245** مع حالة نضج لكل سجل.
- baseline تاريخي F001-F243 + Phase 4 reconciliation addendum لـF244-F245.
- سجل مستقل لأسماء 29 خوارزمية ومحركاً موثقاً في المصدر.
- خريطة 20 عائلة نظامية.
- محرك مخاطر صحي توضيحي قابل للتفاعل.
- سجل إبل وعرض KPI وتنبيهات توضيحية.
- مسار geofence تجريبي قابل للاختبار.
- scoring demonstrator للمزايين.
- state-machine تجريبية للمزاد.
- مسار تحقق شهادة تجريبية.
- سجل أحداث ثنائي اللغة داخل الجلسة.
- 20 Evidence IDs عبر Phase 2 وPhase 3.
- 12/12 قدرة استراتيجية عند Evidence Grade A — Automated + Runtime.
- GitHub Actions validation لتسلسل السجل، الأدلة، Phase 3 وPhase 4.

### 3. نموذج الإثبات للاستحواذ

يتم تقييم كل ادعاء وفق السلسلة:

**Claim → Canonical F-ID → Source/Evidence Class → Public Maturity → Reproducible Demo/Test → Limitation → Production Closure Plan**

لا يكفي وجود عنوان أو كود تاريخي لإثبات الجاهزية الإنتاجية.

### 4. طبقات المعمارية

1. **Identity & Registry** — الهوية، السجل، الملكية، الشهادات والتتبع.
2. **Operations** — المزارع، القطعان، الصحة، التغذية، التكاثر، السباقات، المسابقات، المهرجانات والمزادات.
3. **Sensing & Field Intelligence** — IoT، GPS، الكاميرات، البيانات الحيوية والمخاطر.
4. **AI & Analytics** — التحليل، التنبؤ، التوصيات، الجمال، السوق، الجينات والسلوك.
5. **Environment & Sustainable Genetics** — البيئة والرعي والموارد، F244 للتحسين الوراثي مع تحليل الأثر البيئي، وF245 لتقييم الأثر البيئي الإيجابي للتربية.
6. **Evidence & Governance** — maturity registry، source reconciliation، audit events، security/evidence controls.
7. **Integration** — الجهات البيطرية والحكومية والبيئية والأسواق والخدمات الخارجية؛ جميع الاتصالات العامة الحالية Mock Integration ما لم يذكر خلاف ذلك.

### 5. أهم مجالات القيمة

- هوية وسجل ودليل ملكية للإبل.
- صحة وسلوك ورفاه وبيانات حيوية.
- جينات وأنساب وتكاثر وتحسين وراثي.
- ربط التحسين الوراثي بالاستدامة والأثر البيئي.
- مزايين وتحكيم وكشف تلاعب متعدد الوسائط.
- سباقات ومنافسات ومهرجانات.
- مزادات وسوق وتجارة ولوجستيات.
- إنتاج وجودة وسلسلة توريد.
- بيئة ورعي وسلامة ميدانية.
- طبقة تحليل وتنبؤ موحدة.
- طبقة تكامل وحوكمة وأدلة.

### 6. حالة المنتج اليوم

**نقطة القوة:** نطاق وظيفي موثق ومنظم من 245 قدرة، واجهة تشغيل عامة، سجل نضج صريح، مطابقة مصدر، CI متعدد الطبقات، وEvidence Grade A لمجموعة استراتيجية من 12 قدرة.

**الفجوة الرئيسية:** أغلب القيمة المستقبلية لا تزال تحتاج productionization واختبارات تشغيلية/أمنية/ميدانية، ولا توجد بعد حزمة backend/data/IAM/deployment كاملة مثبتة في المستودع العام.

### 7. خطة Productionization المقترحة للمستحوذ

بدلاً من محاولة تنفيذ 245 قدرة دفعة واحدة، يوصى بموجات:

**Wave A — Acquisition Demonstration Core (10-20 capabilities):** الهوية/السجل، الصحة، المخاطر، التتبع، المزاد، الشهادة، المزايين، سجل الأدلة، التحليلات، وقدرات مختارة من الجينات/التكاثر/التغذية/الاستدامة.

**Wave B — Enterprise Core:** backend، database، IAM، audit persistence، API، observability، deployment، backup/DR، security controls.

**Wave C — Field/Device Validation:** IoT، GPS، كاميرات حرارية، biosensors، milk sensors، race telemetry، pregnancy/labor sensors.

**Wave D — Institutional Integrations:** جهات حكومية/بيطرية، تجارة، دفع، لوجستيات، بيانات بيئية، وربط أسواق.

**Wave E — Advanced AI/Immersive:** نماذج متخصصة، AR/VR/3D، كشف تلاعب متقدم، ونطاقات تحليلية تحتاج بيانات تدريب واعتماداً ميدانياً.

### 8. أسئلة المشتري التي يجب أن تجيب عنها Data Room

- من يملك الكود والخوارزميات والملفات التاريخية؟
- ما الذي سينتقل قانونياً في الصفقة؟
- ما القدرات التي لها كود تنفيذي خاص خارج المستودع العام؟
- ما البيانات المطلوبة لتدريب أو معايرة النماذج؟
- ما التبعيات أو حقوق الطرف الثالث؟
- ما الذي تم اختباره؟ وبأي بيانات؟ ومن تحقق منه؟
- ما تكلفة ومدة نقل أهم 10-20 قدرة إلى Production؟
- ما متطلبات الأجهزة والتكاملات والاعتمادات؟
- ما مخاطر الأمن والخصوصية والبيانات الجينية/الصحية/الموقعية؟
- ما خطة التشغيل والصيانة والدعم بعد نقل الأصل؟

### 9. مؤشر جاهزية العناية الواجبة

- **R0 — Unmapped**
- **R1 — Documented**
- **R2 — Reproducible Evidence**
- **R3 — Production Candidate**
- **R4 — Independently Validated**

الوضع الحالي يرفع Scope Documentation / Source Reconciliation / Structural Validation / Strategic Runtime Evidence إلى R1-R2، بينما Production Security، Field Validation، Enterprise Backend، Commercial Evidence وIndependent Validation تحتاج مراحل لاحقة.

### 10. الوثائق المرتبطة

- `FEATURE_REGISTRY.md` — baseline التاريخي F001-F243.
- `PHASE4_245_RECONCILIATION.md` — F244-F245 والنطاق الحالي F001-F245.
- `DEMO_SCENARIOS.md` — خطوات قابلة لإعادة التشغيل.
- `KNOWN_LIMITATIONS.md` — ما لا يجب الادعاء بأنه جاهز.
- `SECURITY.md` — نموذج التهديدات وخطة الضوابط.
- `IP_NOTICE.md` — حدود الملكية والإفصاح وما يلزم داخل Data Room.
- `EVIDENCE.md` — مصفوفة الأدلة العامة.
- `SOURCE_RECONCILIATION.md` — منهج مطابقة المصادر.
- `ALGORITHM_ENGINE_REGISTRY.md` — سجل الأسماء الخوارزمية.
- `SYSTEM_FAMILIES.md` — التجميع المعماري.
- `PHASE3_GRADE_A_EVIDENCE.md` و`STRATEGIC_EVIDENCE_MATRIX.md` — إغلاق Evidence Grade A.

## English

SMART Camel AI is currently represented as a broad technology portfolio normalized into **245 canonical capabilities F001-F245, 29 source-documented named algorithms/engines, two named training models and 20 canonical system families**. The public repository is an executable demonstrator and diligence evidence surface, not the confidential production codebase or private IP data room.

The historical Phase 1 baseline ended at F243. Phase 4 reconciles F244 and F245 as independent source-backed Planned capabilities and makes F001-F245 the current runtime and CI boundary.

The acquisition diligence model is:

**Claim → Canonical F-ID → Source/Evidence Class → Public Maturity → Reproducible Demo/Test → Limitation → Production Closure Plan**

The strongest current evidence is in scope normalization, source reconciliation, public demonstration, automated strategic-capability evidence and structural CI. The principal remaining diligence work is production backend/data/IAM, security hardening, field validation, confidential IP chain-of-title evidence, third-party license/SBOM review, commercial proof and independent validation.
