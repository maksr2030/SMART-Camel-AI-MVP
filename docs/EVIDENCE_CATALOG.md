# Acquisition Evidence Catalog | سجل أدلة الاستحواذ

## العربية

### الغرض

هذا السجل يحول ادعاءات SMART Camel AI العامة إلى أدلة قابلة للتتبع أثناء العناية الواجبة. كل Evidence ID يحدد الادعاء، F-ID المرتبط إن وجد، نوع الدليل، طريقة التحقق، وحدود ما يثبته الدليل.

### فئات الدليل

- **AT — Automated Test:** اختبار آلي ينجح أو يفشل داخل CI.
- **RE — Runtime Evidence:** سلوك يمكن تشغيله في الـMVP العام.
- **SE — Structural Evidence:** دليل بنيوي من السجل أو الملفات أو المعمارية.
- **DE — Documentation Evidence:** إفصاح أو توثيق محدد يمكن مراجعته.

### EVD-001 — Canonical capability continuity
- **Claim:** السجل العام الحالي يحتوي F001-F245 دون فجوات أو تكرار.
- **Related capability:** F001-F245.
- **Evidence class:** AT + SE.
- **Verification:** `scripts/validate.py`, `tests/test_core.mjs`, `tests/test_phase4.mjs`.
- **Pass condition:** 245 معرفاً متسلسلاً ومتميزاً، مع F244 وF245 ظاهرتين كقدرتين Planned مصدرّيتين.
- **Boundary:** لا يثبت أن جميع القدرات منفذة إنتاجياً.

### EVD-002 — Maturity classification integrity
- **Claim:** كل قدرة تحمل حالة من الحالات العامة الخمس المعتمدة.
- **Related capability:** F001-F245.
- **Evidence class:** AT + SE.
- **Verification:** `tests/test_core.mjs`.
- **Pass condition:** جميع السجلات تستخدم Implemented / Demonstrated / Simulated / Mock Integration / Planned، ومجموع العدادات = 245.
- **Boundary:** حالة النضج ليست شهادة جودة أو اعتماداً خارجياً.

### EVD-003 — Camel identity and registry demonstrator
- **Claim:** الـMVP يعرض سجلات إبل مستقلة بمعرفات وبيانات ثنائية اللغة.
- **Related capability:** F001, F002.
- **Evidence class:** RE + SE.
- **Verification:** واجهة سجل الإبل + فحص بيانات CAMEL-001 في `tests/test_core.mjs`.
- **Boundary:** السجل اصطناعي وليس سجلاً حكومياً حياً.

### EVD-004 — Geofence risk presentation
- **Claim:** الـMVP يعرض تنبيهاً جغرافياً تجريبياً مرتبطاً بالسياج الجغرافي.
- **Related capability:** F012.
- **Evidence class:** RE + SE.
- **Verification:** قسم التنبيهات + `tests/test_phase3.mjs`.
- **Boundary:** لا يثبت اتصال GPS أو سياجاً ميدانياً حياً.

### EVD-005 — Explainable health-risk simulation
- **Claim:** مدخلات الحرارة والنشاط والترطيب تنتج درجة مخاطر ونطاق Low/Medium/High وفق منطق واحد مستخدم في الواجهة والاختبار.
- **Related capability:** F005, F019, F022.
- **Evidence class:** AT + RE.
- **Verification:** `app/core.js`, `app/app.js`, `tests/test_core.mjs`.
- **Pass condition:** سيناريوهات منخفض/متوسط/مرتفع تعطي النطاق المتوقع، مع حد أعلى 100.
- **Boundary:** محاكاة تعليمية وليست تشخيصاً بيطرياً أو نموذجاً سريرياً معتمداً.

### EVD-006 — Auction interaction and trace
- **Claim:** يمكن تنفيذ مزايدة تجريبية ويظهر أثرها في سجل أحداث الجلسة.
- **Related capability:** F034, F060.
- **Evidence class:** RE.
- **Verification:** D07 ثم D09 في `docs/DEMO_SCENARIOS.md`.
- **Boundary:** لا توجد معاملة مالية أو تسوية أو عقد بيع حقيقي.

### EVD-007 — Demonstration certificate verification
- **Claim:** CAMEL-001 ينجح في التحقق، والرموز الأخرى تفشل وفق منطق قابل للاختبار.
- **Related capability:** F040, F041.
- **Evidence class:** AT + RE.
- **Verification:** `app/core.js`, `app/app.js`, `tests/test_core.mjs`, D08.
- **Boundary:** ليست شهادة حكومية أو توقيعاً رقمياً قانونياً.

### EVD-008 — In-session audit trail
- **Claim:** تفاعلات المزاد والتحقق واللغة تسجل كأحداث داخل الجلسة.
- **Related capability:** F060.
- **Evidence class:** RE.
- **Verification:** D07-D09 في `docs/DEMO_SCENARIOS.md`.
- **Boundary:** ليس immutable ledger ولا سجل تدقيق مؤسسياً دائماً.

### EVD-009 — Mazayen evaluation presentation
- **Claim:** يوجد مسار عرض لتقييم المزايين مع درجة تفسيرية ظاهرة.
- **Related capability:** F026, F027.
- **Evidence class:** RE.
- **Verification:** بطاقة Mazayen في الواجهة العامة + `tests/test_phase3.mjs`.
- **Boundary:** الدرجة توضيحية ولا تمثل قرار تحكيم رسمي أو نموذجاً معتمداً.

### EVD-010 — Bilingual public interface
- **Claim:** الواجهة الرئيسية قابلة للتبديل بين العربية والإنجليزية مع تغيير اتجاه الصفحة.
- **Related capability:** Cross-cutting public UX evidence.
- **Evidence class:** RE + SE.
- **Verification:** D01 + `scripts/validate.py`.
- **Boundary:** لا يثبت اكتمال ترجمة جميع الأصول السرية أو المؤسسية.

### EVD-011 — Named algorithm/engine traceability
- **Claim:** 29 خوارزمية ومحركاً مسمىً وموثقاً في المصدر مسجلة دون نشر التنفيذ المملوك.
- **Related capability:** متعدد.
- **Evidence class:** SE + DE.
- **Verification:** `docs/ALGORITHM_ENGINE_REGISTRY.md` + `scripts/validate.py`.
- **Boundary:** Source-documented لا تعني production-validated.

### EVD-012 — Canonical system-family architecture
- **Claim:** 245 قدرة منظمة ضمن 20 عائلة نظامية معيارية.
- **Related capability:** F001-F245.
- **Evidence class:** SE + DE.
- **Verification:** `docs/SYSTEM_FAMILIES.md` + `scripts/validate.py`.
- **Boundary:** العائلات تصنيف معماري وليست 20 منتجات منفصلة.

### EVD-013 — Explicit limitation disclosure
- **Claim:** حزمة DD تعلن 23 قيداً عربياً و23 قيداً إنجليزياً بصورة متطابقة هيكلياً.
- **Related capability:** Cross-cutting governance evidence.
- **Evidence class:** AT + DE.
- **Verification:** `docs/KNOWN_LIMITATIONS.md` + `scripts/validate.py` + `tests/test_evidence_contract.py`.
- **Boundary:** الإفصاح لا يزيل القيد؛ يثبته ويمنع تضخيم الادعاء.

### EVD-014 — Public/private IP boundary
- **Claim:** المستودع يعلن بوضوح أن الخوارزميات الخاصة والأوزان وبيانات التدريب والـChain of Title التفصيلي تبقى خارج الإفصاح العام.
- **Related capability:** Cross-cutting IP evidence.
- **Evidence class:** DE.
- **Verification:** `docs/IP_NOTICE.md` + `tests/test_evidence_contract.py`.
- **Boundary:** إثبات الملكية القانوني الكامل يجب أن يكون في Data Room السرية.

### EVD-015 — Due-diligence package integrity
- **Claim:** الوثائق الأساسية للعناية الواجبة مرتبطة من README ويشترطها CI.
- **Related capability:** Cross-cutting acquisition readiness.
- **Evidence class:** AT + SE + DE.
- **Verification:** `scripts/validate.py`, `tests/test_evidence_contract.py`, `scripts/security_check.py`, `scripts/release_check.py`, `.github/workflows/validate.yml`.
- **Boundary:** اكتمال الحزمة العامة لا يعني اكتمال الفحص القانوني أو المالي أو الأمني الإنتاجي.

## English

This catalog maps public SMART Camel AI claims to traceable acquisition evidence. The current canonical continuity claim is **F001-F245**, with F244 and F245 reconciled in Phase 4 as source-backed Planned capabilities.

**Phase 2 baseline remains EVD-001 through EVD-015.** Phase 3 adds EVD-016-EVD-020 in its separate evidence document. No evidence record converts a Planned, Simulated or Mock Integration capability into a production claim.
