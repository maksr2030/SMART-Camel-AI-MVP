# Source Feature Reconciliation | مطابقة ميزات المصادر

## العربية

### الغرض

يوثق هذا الملف منهج تحويل وثائق منصة SMART Camel AI التاريخية ومواد براءة الاختراع والملفات البيطرية والتشغيلية وملفات الخوارزميات إلى سجل قدرات عام موحد وقابل للتدقيق داخل MVP.

السجل الحالي يستخدم معرفات معيارية من **F001 إلى F245**. هذه المعرفات لا تدّعي أن الوثائق التاريخية استخدمت التسلسل نفسه؛ هي طبقة توحيد تمنع تضارب الأرقام بين نسخ المنصة القديمة.

### أنماط المصادر التي تمت مراجعتها

أظهرت محفظة المصدر ستة أنماط رئيسية:

1. وثائق تفصيلية تسمي قدرات فعلية وتشرح الوصف والهدف والفوائد وآلية العمل.
2. ملفات بيطرية وتشغيلية توثق قدرات مستقلة في الصحة، السباقات، الإنتاجية والكفاءة الجينية.
3. ملفات فهرسة تاريخية من 1 إلى 190 و1 إلى 200؛ بعضها يحتوي قوالب عامة مكررة، لذلك لم يُقبل الترقيم وحده كدليل.
4. مواد براءة اختراع مطولة ومختصرة؛ قُبلت فقط الوحدات ذات الحدود التقنية المميزة بعد إزالة التكرار.
5. ملفات إدارة مزارع واستدامة تتضمن تشغيل الموارد والطاقة والبيئة.
6. ملفات خوارزمية أخيرة توثق قدرات وأسماء محركات ونماذج تدريب بصورة أكثر تحديداً.

### قاعدة القبول

لا يتم احتساب رقم أو عنوان كقدرة موثقة لمجرد ظهوره في قائمة أو قالب. تقبل القدرة عندما يتوفر واحد أو أكثر من الآتي:

- اسم وظيفي مميز مع وصف واضح.
- هدف وفوائد وآلية عمل مستقلة.
- نموذج واجهة أو منطق تجريبي يوضح السلوك المقصود.
- ظهور متكرر ومتسق في أكثر من وثيقة.
- ارتباط واضح بنظام فرعي مستقل.
- ذكر صريح داخل وصف تقني لبراءة أو ملف خوارزمي يحدد وظيفة قابلة للفصل هندسياً.

ويرفض كدليل مستقل:

- النصوص العامة المكررة آلياً.
- القوالب الفارغة.
- أرقام الميزات دون اسم أو وصف وظيفي.
- إعادة تسمية قدرة موجودة دون حد وظيفي جديد.
- مجرد وجود كود توضيحي قديم كإثبات جاهزية إنتاجية.
- خصائص عامة مثل تحسين تجربة المستخدم أو رفع الدقة إذا لم تمثل قدرة تشغيل مستقلة.

### نتيجة المطابقة الحالية

بعد دمج السجل الأساسي مع جميع الدفعات التي تمت مراجعتها، ثم مطابقة Phase 4 للقدرات البيئية/الوراثية التي لم تكن ممثلة كـF-ID مستقل، يحتوي السجل العام الحالي على:

- **245 Canonical Capability Records** من F001 إلى F245.
- **29 Source-Documented Named Algorithms & Engines** في سجل مستقل.
- **20 Canonical System Families** كطبقة تنظيم معماري أعلى.
- **2 Independently Named Training Models** موثقة كمصادر، وليست ادعاءً بنماذج إنتاجية معتمدة.

كان سجل Phase 1 التاريخي ينتهي عند F243. تحتفظ `FEATURE_REGISTRY.md` بهذا baseline لأغراض التتبع، بينما تضيف `PHASE4_245_RECONCILIATION.md` F244 وF245 ويعامل runtime والـCI النطاق الحالي باعتباره F001-F245.

### طبقة البراءة F224-F231

- F224: تشفير ما بعد الكم للبيانات البيطرية والتجارية.
- F225: التهجين المحسن حسب حالة الاستخدام.
- F226: التقييم الصحي الآلي قبل التجارة.
- F227: التقييم الجيني الآلي قبل التجارة.
- F228: محرك التقييم الآلي للمسابقات.
- F229: توليد نتائج المسابقات في الزمن الحقيقي.
- F230: مطابقة المهرجان الأنسب وتوصية المشاركة.
- F231: موصل التكامل مع الجهات البيطرية.

### الطبقة البيطرية والتشغيلية F232-F235

- F232: توثيق الحالة الصحية للإبل المشاركة في المهرجانات.
- F233: تتبع الموقع والسرعة أثناء السباقات في الزمن الحقيقي.
- F234: تتبع إنتاجية الإبل عبر دورة حياتها.
- F235: توصيات الطاقة المتجددة لمزارع الإبل.

### الطبقة الخوارزمية F236-F243

- F236: التعرف الذكي على سلالات الإبل.
- F237: التحكم التكيفي المغلق في تغذية الإبل.
- F238: التعرف البيومتري على الإبل ببصمة الوجه.
- F239: المراقبة الصحية الحرارية بالكاميرات.
- F240: تتبع نوم الإبل وتحليل جودته.
- F241: الإنذار المبكر بالإجهاد الحراري للإبل.
- F242: تحليل مخاطر الأمراض الوراثية.
- F243: مراقبة الحمل والولادة في الإبل.

### مطابقة Phase 4 — F244-F245

بعد مراجعة إضافية لملفات المصدر التاريخية، قُبلت قدرتان مستقلتان كانتا موصوفتين بعنوانين ووظيفتين منفصلتين ولم تكونا ممثلتين كـF-ID مستقلين في السجل السابق:

- **F244 — التحسين الوراثي مع تحليل الأثر البيئي / Genetic Breeding with Environmental Impact Analysis.**
- **F245 — تقييم الأثر البيئي الإيجابي لتربية الإبل / Positive Environmental Impact Evaluation for Camel Breeding.**

كلاهما بقي **Planned** لأن المصدر يثبت الهوية الوظيفية والتصميم، ولا يثبت نشرهما الإنتاجي أو تحققاً ميدانياً مستقلاً.

لم تُكرر قدرات موجودة سابقاً لمجرد اختلاف الاسم. F244 قُبل لأنه يجمع قرار التزاوج الوراثي بتحليل الأثر البيئي ومحاكاة الأجيال المستقبلية كمسار مستقل، وF245 قُبل لأن مخرجه الأساسي هو تقييم المساهمة البيئية الإيجابية للتربية وليس مجرد مراقبة بيئية أو إدارة رعي.

### فصل الخوارزميات عن القدرات

تم إنشاء `ALGORITHM_ENGINE_REGISTRY.md` لتسجيل 29 اسماً موثقاً في المصدر دون رفع عدد القدرات بسبب كل اسم خوارزمية. الأسماء المصدرية لا تعني تلقائياً أن الخوارزمية مدربة على بيانات معتمدة أو تمتلك دقة مثبتة أو منشورة إنتاجياً أو حاصلة على اعتماد.

### فصل العائلات النظامية

تم إنشاء `SYSTEM_FAMILIES.md` لتنظيم **245 قدرة** في 20 عائلة نظامية معيارية. هذه الطبقة تساعد المراجع والمستحوذ على فهم المنصة كمعمارية مترابطة بدلاً من قائمة ميزات مسطحة.

### علاقة الترقيم القديم بالجديد

يجب عدم تفسير F169 مثلاً على أنه الميزة التاريخية رقم 169. بادئة F هي رقم قياسي جديد داخل سجل MVP فقط. يمكن لاحقاً بناء Legacy Crosswalk خاص بالعناية الواجبة يربط F-ID بالمصدر التاريخي عندما يكون الرقم القديم موثوقاً.

### حدود الإفصاح

المستودع العام يعرض أسماء القدرات وحالات النضج والأسماء العامة للخوارزميات والعائلات النظامية فقط. لا ينشر ملفات المصدر الخاصة أو الأكواد المملوكة أو الأوزان أو مجموعات التدريب أو وثائق الملكية الفكرية الداخلية أو التقييمات التجارية السرية.

## English

This document records the normalization method used to convert historical SMART Camel AI source material, patent-related documents, veterinary/operating files and algorithm-focused sources into one auditable public capability registry.

The current canonical registry is **F001-F245**. Canonical F-IDs are a modern normalization layer and do not claim that historical files used the same numbering.

The current reconciled result is:

- **245 Canonical Capability Records**, F001-F245.
- **29 Source-Documented Named Algorithms & Engines**.
- **20 Canonical System Families**.
- **2 Independently Named Training Models** recorded as source evidence.

The historical Phase 1 acquisition baseline ended at F243. Phase 4 adds two independently described source capabilities while retaining that historical baseline for traceability:

- **F244 — Genetic Breeding with Environmental Impact Analysis — Planned.**
- **F245 — Positive Environmental Impact Evaluation for Camel Breeding — Planned.**

These two records are not counted merely to increase the total. F244 has a distinct breeding-decision boundary combining genetic selection, environmental impact and future-generation simulation. F245 has a distinct evaluation output focused on the positive environmental contribution of camel breeding. Both remain Planned because the source supports design identity rather than production deployment or independent field validation.

Capabilities, named algorithms, training models and system families remain separate counting layers. The public repository exposes normalized names, maturity and diligence boundaries while excluding proprietary source code, model weights, datasets and confidential IP records.
