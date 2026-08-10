# معمارية SMART Camel AI | SMART Camel AI Architecture

## العربية

هذا النموذج العام يستخدم معمارية عرض خفيفة بلا اعتماديات runtime خارجية حتى يمكن تشغيله ومراجعته بسهولة. الهدف هو فصل إثبات القدرة الوظيفية عن الأسرار التنفيذية للمنصة الكاملة.

**النطاق المعياري الحالي: F001-F245.** يحتفظ Phase 1 بخط أساس تاريخي F001-F243، وتضيف Phase 4 F244 وF245 ضمن نفس المعمارية دون تحويلهما إلى تنفيذ إنتاجي.

### الطبقات

1. **طبقة الهوية والسجل**
   - هوية رقمية لكل جمل.
   - بيانات السلالة والعمر والمزرعة والحالة.
   - سجل الملكية والشهادات والتتبع.

2. **طبقة التشغيل**
   - المزارع والقطعان.
   - الصحة والتغذية والنشاط.
   - السباقات والمزايين والمهرجانات والمزادات.

3. **طبقة الاستشعار والمخاطر**
   - بيانات مستشعرات اصطناعية.
   - السياج الجغرافي والرعي والمخاطر البيئية.
   - محرك مخاطر صحي تفسيري تجريبي.

4. **طبقة الذكاء والتحليل**
   - التوصيات والتنبؤ والتحليل.
   - تقييمات تجريبية للمزايين والسوق والجودة.
   - جميع المخرجات في الإصدار العام موسومة بوضوح عندما تكون محاكاة.

5. **طبقة الجينات والاستدامة البيئية**
   - الجينات والأنساب والتكاثر والتحسين الوراثي.
   - **F244** يربط قرار التحسين الوراثي بتحليل الأثر البيئي ومحاكاة الأجيال المستقبلية.
   - **F245** يمثل قدرة مستقلة لتقييم الأثر البيئي الإيجابي لتربية الإبل.
   - كلاهما Planned ولا يثبت تحققاً ميدانياً أو تكاملاً بيئياً حياً.

6. **طبقة الأدلة والتدقيق**
   - سجل قدرات مركزي F001-F245.
   - حالة واضحة لكل قدرة.
   - Evidence IDs قابلة للتتبع.
   - سجل أحداث للمحاكاة والتفاعلات المهمة.
   - بوابات Release Readiness وفحص أسرار عام في Phase 4.

7. **طبقة التكامل**
   - نقاط تكامل مع البيئة والجهات الحكومية والبيطرية موضحة كـMock Integration فقط.
   - لا يدّعي هذا الإصدار وجود اتصال حي بجهة حكومية أو نظام إنتاجي.

### تصنيف النضج

- Implemented: وظيفة منفذة مباشرة داخل النموذج العام.
- Demonstrated: مسار وظيفي ظاهر ويمكن استعراضه ولكن ليس نظام إنتاج كامل.
- Simulated: نتيجة أو محرك يستخدم بيانات أو منطق محاكاة لإثبات السلوك.
- Mock Integration: نقطة تكامل معروضة مع عدم وجود اتصال خارجي حي.
- Planned: ضمن النطاق المعماري ولم تدخل بعد في الإصدار التشغيلي العام.

## English

The public MVP uses a lightweight dependency-minimized architecture so it can be opened, reviewed and demonstrated easily while separating functional evidence from protected implementation details.

**Current canonical scope: F001-F245.** Phase 1 preserves a historical F001-F243 baseline, while Phase 4 adds F244 and F245 as source-backed Planned capabilities.

The architecture is organized into identity/registry, operations, sensing/risk, intelligence/analytics, genetics/environmental sustainability, evidence/audit, and integration layers. F244 connects genetic-improvement decisions with environmental-impact analysis and future-generation simulation. F245 represents independent positive-environmental-impact evaluation for camel breeding. Neither is represented as production deployed.

The evidence layer includes the canonical registry, explicit maturity states, Evidence IDs, in-session audit evidence, Phase 4 release-readiness gates and a public secret/sensitive-file scan. External institutional integrations remain Mock Integration unless separately verified.
