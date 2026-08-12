# Strategic Capability Evidence Matrix | مصفوفة الأدلة للقدرات الاستراتيجية

## العربية

### الهدف

هذه المصفوفة تركز على **12 قدرة استراتيجية** من السجل الحالي F001-F245 حتى يستطيع فريق الاستحواذ فحص سلسلة الأدلة بسرعة. بعد Phase 3 أصبحت القدرات الاثنتا عشرة جميعها **Grade A من ناحية Evidence**، أي أن لكل واحدة مساراً عاماً قابلاً للتشغيل واختباراً آلياً لنفس المنطق أو العقد الوظيفي.

F244 وF245 جزء من النطاق المعياري الحالي F001-F245 لكنهما ليستا ضمن مجموعة الـ12 الاستراتيجية الحالية، وتبقيان Planned وفق مطابقة Phase 4.

> Grade A لا تعني Production Ready ولا تغيّر حالة النضج المنشورة للقدرة.

### درجات الدليل

- **A — Automated + Runtime:** يوجد اختبار آلي وسلوك عام قابل للتشغيل.
- **B — Runtime:** يوجد سلوك عام ولكن الاختبار الآلي غير مكتمل.
- **C — Structural/Documented:** يوجد توثيق أو سجل دون مسار تنفيذي كافٍ.

| # | F-ID | القدرة | النضج العام | Evidence ID | الدرجة | ما يثبت الآن | الإغلاق التالي قبل Production |
|---|---|---|---|---|---|---|---|
| S01 | F001 | الهوية الرقمية للإبل | Implemented | EVD-016 | A | schema للسجل + uniqueness + lookup لـCAMEL-001 + عرض runtime | backend identity store، auth، lifecycle controls |
| S02 | F002 | السجل الموحد للإبل | Implemented | EVD-016 | A | سجل متعدد الصفوف يمر عبر validation آلي عند التشغيل | CRUD API، persistence، concurrency، backup/restore |
| S03 | F005 | ذكاء الصحة | Simulated | EVD-005 | A | منطق مخاطر قابل للتشغيل والاختبار | بيانات تحقق بيطري، validation protocol، model governance |
| S04 | F012 | السياج الجغرافي | Demonstrated | EVD-017 | A | Inside/Near/Outside من Core واحد مستخدم في الواجهة والاختبار | GPS sandbox ثم أجهزة ميدانية وتنبيه خارجي |
| S05 | F019 | كشف الحالات الصحية بالذكاء الاصطناعي | Simulated | EVD-005 | A | Core صحي مختبر مع حدود إفصاح | detection model منفصل + dataset card + veterinary validation |
| S06 | F022 | محرك المخاطر الموحد | Simulated | EVD-005 | A | Low/Medium/High واختبارات حواف وسقف 100 | multi-domain risk engine + decision tables + calibration |
| S07 | F026 | إدارة المزايين | Demonstrated | EVD-018 | A | scoring demonstrator قابل لإعادة التنفيذ | workflow كامل للمسابقة، roles، evidence package |
| S08 | F027 | تقييم الجمال بالذكاء الاصطناعي | Simulated | EVD-018 | A | scoring function مختبر بمدخلات وحدود واضحة | نموذج مملوك منفصل، validation مع خبراء، bias/error analysis |
| S09 | F034 | مزادات الإبل | Demonstrated | EVD-019 | A | state transitions للمزاد + رفض bid غير صالح + runtime interaction | bidder identity، persistence، payment/settlement خارج MVP |
| S10 | F040 | الشهادة الرقمية الموثوقة | Demonstrated | EVD-007 | A | تحقق إيجابي/سلبي قابل للاختبار | cryptographic signing، key management، revocation |
| S11 | F041 | التحقق عبر QR | Demonstrated | EVD-007 | A | تحقق CAMEL-001 ومنطق رفض الرموز الأخرى | QR payload موقّع + anti-replay + scanner integration |
| S12 | F060 | سجل الأدلة والتدقيق | Implemented | EVD-020 | A | event sequence + bilingual messages + references + runtime log | persistence، integrity controls، export، retention/WORM حسب الحاجة |

### نتيجة Phase 3

**12 من 12 قدرة استراتيجية = Grade A Evidence.**

المجموعة تغطي:

1. Identity & Registry — F001/F002.
2. Health & Risk Intelligence — F005/F019/F022.
3. Field Safety — F012.
4. Competitions & Market Operations — F026/F027/F034.
5. Trust, Verification & Audit — F040/F041/F060.

الهدف من هذه النتيجة هو تقوية العناية الواجبة التقنية، وليس الإيحاء بأن جميع الوظائف أصبحت أنظمة إنتاجية أو معتمدة.

## English

The current canonical registry spans **F001-F245**. The selected strategic set now has **12/12 capabilities at Evidence Grade A — Automated + Runtime** after Phase 3. F244 and F245 are part of the current canonical scope but remain source-backed Planned capabilities outside this 12-capability strategic evidence set.

Grade A means the public runtime path is backed by automated verification of the same shared logic or functional contract. It does **not** mean production readiness and does not alter published maturity states.

New Phase 3 evidence mapping:

- F001/F002 → EVD-016.
- F012 → EVD-017.
- F026/F027 → EVD-018.
- F034 → EVD-019.
- F060 → EVD-020.

Previously Grade A capabilities retain EVD-005 and EVD-007. Production closure requirements remain explicitly separate from evidence grade.
