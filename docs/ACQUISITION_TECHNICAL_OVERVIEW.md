# Acquisition Technical Overview | النظرة التقنية للاستحواذ

## العربية

### 1. الملخص التنفيذي

SMART Camel AI هي محفظة منصة واسعة النطاق لقطاع الإبل، منظمة حالياً في **243 سجل قدرة معيارية، 29 خوارزمية/محركاً مسمىً وموثقاً في المصدر، نموذجَي تدريب مسميين، و20 عائلة نظامية معيارية**. المستودع العام هو Demonstrator قابل للتشغيل والمراجعة، وليس النسخة الإنتاجية الكاملة ولا مخزن الملكية الفكرية السرية.

هدف حزمة العناية الواجبة الحالية هو تمكين المستحوذ من التمييز بسرعة بين:

- ما هو منفذ في الـMVP العام.
- ما هو قابل للاستعراض كمسار وظيفي.
- ما هو محاكاة.
- ما هو Mock Integration.
- ما هو موثق في المصدر لكنه Planned.
- ما يبقى سرياً داخل Data Room ولا ينبغي نشره للعامة.

### 2. الأصول التقنية العامة الحالية

- واجهة عربية/إنجليزية ثابتة قابلة للتشغيل بلا حزم runtime خارجية.
- سجل قدرات F001-F243 مع حالة نضج لكل سجل.
- ملفات مطابقة مصدر ومنهج لمنع العد المكرر أو القوالب العامة.
- سجل مستقل لأسماء 29 خوارزمية ومحركاً موثقاً في المصدر.
- خريطة 20 عائلة نظامية.
- محرك مخاطر صحي توضيحي قابل للتفاعل.
- سجل إبل وعرض KPI وتنبيهات توضيحية.
- مسار مزايدة تجريبي.
- مسار تحقق شهادة تجريبية.
- سجل أحداث داخل الجلسة.
- GitHub Actions validation لتسلسل السجل وبنية الملفات.

### 3. نموذج الإثبات المقترح للاستحواذ

يجب تقييم كل ادعاء وفق السلسلة التالية:

**Claim → Canonical F-ID → Source/Evidence Class → Public Maturity → Reproducible Demo/Test → Limitation → Production Closure Plan**

لا يكفي وجود عنوان أو كود تاريخي لإثبات الجاهزية الإنتاجية.

### 4. طبقات المعمارية

1. **Identity & Registry** — الهوية، السجل، الملكية، الشهادات والتتبع.
2. **Operations** — المزارع، القطعان، الصحة، التغذية، التكاثر، السباقات، المسابقات، المهرجانات والمزادات.
3. **Sensing & Field Intelligence** — IoT، GPS، الكاميرات، البيانات الحيوية والمخاطر.
4. **AI & Analytics** — التحليل، التنبؤ، التوصيات، الجمال، السوق، الجينات والسلوك.
5. **Evidence & Governance** — maturity registry، source reconciliation، audit events، security/evidence controls.
6. **Integration** — الجهات البيطرية والحكومية والبيئية والأسواق والخدمات الخارجية؛ جميع الاتصالات العامة الحالية Mock Integration ما لم يذكر خلاف ذلك.

### 5. أهم مجالات القيمة

من زاوية تقنية للاستحواذ، أعلى مجالات التمايز ليست مجرد «إدارة مزرعة»، وإنما تجميع عدة طبقات في أصل واحد:

- هوية وسجل ودليل ملكية للإبل.
- صحة وسلوك ورفاه وبيانات حيوية.
- جينات وأنساب وتكاثر وتحسين وراثي.
- مزايين وتحكيم وكشف تلاعب متعدد الوسائط.
- سباقات ومنافسات ومهرجانات.
- مزادات وسوق وتجارة ولوجستيات.
- إنتاج وجودة وسلسلة توريد.
- بيئة ورعي وسلامة ميدانية.
- طبقة تحليل وتنبؤ موحدة.
- طبقة تكامل وحوكمة وأدلة.

### 6. حالة المنتج اليوم

**نقطة القوة:** نطاق وظيفي موثق ومنظم، واجهة تشغيل عامة، سجل نضج صريح، مطابقة مصدر، CI بنيوي، وحدود إفصاح أفضل من قائمة ميزات تسويقية.

**الفجوة الرئيسية:** أغلب القيمة المستقبلية لا تزال تحتاج productionization واختبارات تشغيلية/أمنية/ميدانية، ولا توجد بعد حزمة backend/data/IAM/deployment كاملة مثبتة في المستودع العام.

### 7. خطة Productionization المقترحة للمستحوذ

بدلاً من محاولة تنفيذ 243 قدرة دفعة واحدة، يوصى بموجات:

**Wave A — Acquisition Demonstration Core (10-20 capabilities):**
هوية/سجل، صحة، مخاطر، تتبع، مزاد، شهادة، مزايين، سجل أدلة، تحليلات، وقدرتان أو ثلاث من الجينات/التكاثر/التغذية.

**Wave B — Enterprise Core:**
backend، database، IAM، audit، API، observability، deployment، backup/DR، security controls.

**Wave C — Field/Device Validation:**
IoT، GPS، كاميرات حرارية، biosensors، milk sensors، race telemetry، pregnancy/labor sensors.

**Wave D — Institutional Integrations:**
جهات حكومية/بيطرية، تجارة، دفع، لوجستيات، بيانات بيئية، وربط أسواق.

**Wave E — Advanced AI/Immersive:**
نماذج متخصصة، AR/VR/3D، كشف تلاعب متقدم، ونطاقات تحليلية تحتاج بيانات تدريب واعتماداً ميدانياً.

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

نستخدم خمس درجات لكل مجال:

- **R0 — Unmapped**
- **R1 — Documented**
- **R2 — Reproducible Evidence**
- **R3 — Production Candidate**
- **R4 — Independently Validated**

الوضع الحالي للمستودع العام يرفع **Scope Documentation / Source Reconciliation / Structural Validation** إلى R1-R2، بينما Production Security، Field Validation، Enterprise Backend، Commercial Evidence وIndependent Validation تحتاج مراحل لاحقة.

### 10. الوثائق المرتبطة

- `FEATURE_REGISTRY.md` — سجل المطابقة لكل F-ID.
- `DEMO_SCENARIOS.md` — خطوات قابلة لإعادة التشغيل.
- `KNOWN_LIMITATIONS.md` — ما لا يجب الادعاء بأنه جاهز.
- `SECURITY.md` — نموذج التهديدات وخطة الضوابط.
- `IP_NOTICE.md` — حدود الملكية والإفصاح وما يلزم داخل Data Room.
- `EVIDENCE.md` — مصفوفة الأدلة العامة.
- `SOURCE_RECONCILIATION.md` — منهج مطابقة المصادر.
- `ALGORITHM_ENGINE_REGISTRY.md` — سجل الأسماء الخوارزمية.
- `SYSTEM_FAMILIES.md` — التجميع المعماري.

## English

SMART Camel AI is currently represented as a broad technology portfolio normalized into **243 canonical capabilities, 29 source-documented named algorithms/engines, two named training models and 20 canonical system families**. The public repository is an executable demonstrator and diligence evidence surface, not the confidential production codebase or private IP data room.

The acquisition diligence model is:

**Claim → Canonical F-ID → Source/Evidence Class → Public Maturity → Reproducible Demo/Test → Limitation → Production Closure Plan**

The strongest current evidence is in scope normalization, source reconciliation, public demonstration and structural CI. The principal remaining diligence work is production backend/data/IAM, deeper functional and security testing, field validation for device/health-dependent capabilities, confidential IP chain-of-title evidence, third-party license/SBOM review, commercial proof and independent validation.
