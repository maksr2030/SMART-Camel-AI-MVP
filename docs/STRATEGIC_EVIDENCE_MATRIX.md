# Strategic Capability Evidence Matrix | مصفوفة الأدلة للقدرات الاستراتيجية

## العربية

### الهدف

هذه المصفوفة تختار **12 قدرة استراتيجية** من السجل F001-F243 لمرحلة Evidence & Test Closure الأولى. الاختيار لا يعني أن بقية القدرات أقل قيمة؛ الهدف هو إعطاء فريق الاستحواذ مجموعة مركزة يمكن فحصها وتشغيلها وتتبع أدلتها بسرعة.

### درجات الدليل الحالية

- **A — Automated + Runtime:** يوجد اختبار آلي وسلوك عام قابل للتشغيل.
- **B — Runtime:** يوجد سلوك/عرض عام قابل للمراجعة لكنه يحتاج اختباراً آلياً أعمق.
- **C — Structural/Documented:** يوجد سجل أو توثيق أو حالة نضج، لكن لا يوجد بعد مسار تنفيذي كافٍ لإثباته إنتاجياً.

| # | F-ID | القدرة | النضج العام | Evidence ID | الدرجة | ما يثبت الآن | الإغلاق التالي |
|---|---|---|---|---|---|---|---|
| S01 | F001 | الهوية الرقمية للإبل | Implemented | EVD-003 | B | معرفات إبل مستقلة وسجل عرض ثنائي اللغة | إضافة اختبارات schema/uniqueness أوسع وربط ownership/certificate |
| S02 | F002 | السجل الموحد للإبل | Implemented | EVD-003 | B | سجل CAMEL-001 وسجلات اصطناعية متعددة | اختبار CRUD تجريبي عند إضافة backend |
| S03 | F005 | ذكاء الصحة | Simulated | EVD-005 | A | منطق مخاطر قابل للتشغيل والاختبار | مجموعة سيناريوهات مرجعية وبيانات تحقق بيطري منفصلة |
| S04 | F012 | السياج الجغرافي | Demonstrated | EVD-004 | B | تنبيه جغرافي تجريبي ظاهر | محاكاة مسار geofence قابل لإعادة التشغيل ثم GPS sandbox |
| S05 | F019 | كشف الحالات الصحية بالذكاء الاصطناعي | Simulated | EVD-005 | A | نفس Core الصحي المختبر مع حدود إفصاح واضحة | فصل detection model عن risk rule وربط dataset card عند توفره |
| S06 | F022 | محرك المخاطر الموحد | Simulated | EVD-005 | A | Low/Medium/High واختبارات حواف وحد أعلى 100 | توسيع محرك المخاطر متعدد المجالات واختبارات decision table |
| S07 | F026 | إدارة المزايين | Demonstrated | EVD-009 | B | واجهة عرض لمسار المزايين | سيناريو إدخال معايير ونتيجة قابلة لإعادة التنفيذ |
| S08 | F027 | تقييم الجمال بالذكاء الاصطناعي | Simulated | EVD-009 | B | درجة تفسيرية عامة مع إقرار أنها ليست تحكيماً رسمياً | فصل scoring demo قابل للاختبار دون كشف النموذج المملوك |
| S09 | F034 | مزادات الإبل | Demonstrated | EVD-006 | B | مزايدة تجريبية + أثر في سجل الجلسة | state-machine اختبارية للتأهيل والعرض والمزايدة والنتيجة |
| S10 | F040 | الشهادة الرقمية الموثوقة | Demonstrated | EVD-007 | A | مسار تحقق إيجابي/سلبي قابل للاختبار | توقيع/تحقق تشفيري تجريبي منفصل قبل أي ادعاء قانوني |
| S11 | F041 | التحقق عبر QR | Demonstrated | EVD-007 | A | تحقق CAMEL-001 ومنطق رفض الرموز الأخرى | ربط QR payload تجريبي بالمعرف والشهادة |
| S12 | F060 | سجل الأدلة والتدقيق | Implemented | EVD-008 | B | سجل أحداث داخل الجلسة للمزاد والتحقق واللغة | persistence + integrity + export واختبار تسلسل الأحداث |

### لماذا هذه المجموعة؟

تغطي المجموعة خمس طبقات مهمة للمستحوذ:

1. **Identity & Registry** — F001/F002.
2. **Health & Risk Intelligence** — F005/F019/F022.
3. **Field Safety** — F012.
4. **Competitions & Market Operations** — F026/F027/F034.
5. **Trust, Verification & Audit** — F040/F041/F060.

وبذلك يستطيع المراجع رؤية قيمة المنصة من الهوية إلى الذكاء إلى السوق إلى التحقق والتدقيق، دون الادعاء بأن جميع 243 قدرة وصلت إلى المستوى نفسه.

## English

This matrix selects **12 strategic capabilities** for the first Evidence & Test Closure wave. It is an acquisition-review focus set, not a ranking of the remaining capability portfolio.

Current evidence grades are A (automated + runtime), B (runtime), and C (structural/documented). The first wave intentionally prioritizes identity/registry, health/risk, field safety, competitions/market operations, and trust/verification/audit. Each capability remains bound to its public maturity state and evidence limitations.
