# Source Feature Reconciliation | مطابقة ميزات المصادر

## العربية

### الغرض

يوثق هذا الملف منهج تحويل وثائق منصة الإبل الذكية التاريخية إلى سجل قدرات عام موحد وقابل للتدقيق داخل MVP.

السجل الحالي يستخدم معرفات معيارية جديدة من F001 إلى F223. هذه المعرفات ليست ادعاءً بأن الوثائق التاريخية استخدمت التسلسل نفسه، وإنما هي طبقة توحيد تمنع تضارب الأرقام بين نسخ المنصة القديمة.

### ما الذي تمت مراجعته

تضمنت محفظة المصدر التي تمت مطابقتها عدة أجيال من وثائق HTML عربية وإنجليزية، وملفات تغطي المزارع والصحة والجينات والرعي والمزايين والمهرجانات والمزادات والأسواق والمنتجات والبيئة، إضافة إلى نماذج الإيرادات المرتبطة بالخدمات التشغيلية للمنصة.

أظهرت المراجعة ثلاثة أنماط رئيسية:

1. وثائق تفصيلية تسمي قدرات فعلية وتشرح الوصف والهدف والفوائد وآلية العمل، ومنها سلسلة تفصيلية وصلت تاريخياً إلى نطاق الميزة 78 مع تحسينات وأنظمة فرعية كثيرة.
2. وثيقة مستقلة توثق الميزة التاريخية 169 الخاصة بإدارة الكفاءة الجينية وتحسين السلالات.
3. ملف فهرس من 1 إلى 200، إلا أن السجلات 1 إلى 170 فيه مولدة بقالب عام متكرر، بينما السجلات 171 إلى 200 تحمل أسماء ووظائف تفصيلية حقيقية.

### قاعدة الإثبات

لا يتم احتساب رقم أو عنوان كقدرة موثقة لمجرد ظهوره في قائمة أو قالب.

يقبل السجل العام القدرة عندما يتوفر واحد أو أكثر من الآتي:

- اسم وظيفي مميز مع وصف واضح.
- هدف وفوائد وآلية عمل مستقلة.
- نموذج واجهة أو منطق تجريبي سابق يوضح السلوك المقصود.
- ظهور متكرر متسق في أكثر من وثيقة عربية أو إنجليزية.
- ارتباط واضح بنظام فرعي مستقل مثل الصحة أو الجينات أو الرعي أو المزادات أو المهرجانات.

ويرفض كدليل مستقل:

- النصوص العامة المكررة آلياً.
- القوالب الفارغة.
- أرقام الميزات دون اسم أو وصف وظيفي.
- الادعاء بأن وجود كود توضيحي قديم يثبت جاهزية إنتاجية.

### نتيجة المطابقة الحالية

بعد دمج السجل الأساسي للـMVP مع القدرات التفصيلية المستخرجة من محفظة المصدر، يحتوي السجل العام الحالي على 223 سجل قدرة معيارية.

هذا الرقم يمثل Capability Records وليس بالضرورة 223 منتجاً مستقلاً. بعض السجلات هي محركات أو تدفقات أو قدرات فرعية داخل عائلة أكبر، وهو الأسلوب الأنسب للعرض التقني والعناية الواجبة لأنه يمنع ضغط عدة وظائف مختلفة تحت اسم تسويقي واحد.

### علاقة الترقيم القديم بالجديد

يجب عدم تفسير F169 مثلاً على أنه الميزة التاريخية رقم 169. بادئة F هي رقم قياسي جديد داخل سجل MVP فقط.

عند بناء حزمة العناية الواجبة الكاملة يمكن إضافة Legacy Crosswalk مستقل يربط كل F-ID بالوثيقة التاريخية ورقم الميزة القديم عندما يكون الرقم القديم موثوقاً.

### حدود الإفصاح

المستودع العام يعرض أسماء القدرات وحالة النضج والتجارب العامة فقط. لا ينشر ملفات المصدر الخاصة أو الخوارزميات المملوكة أو النماذج السرية أو وثائق الملكية الفكرية أو التقييمات التجارية الخاصة.

## English

### Purpose

This document records the method used to convert the historical SMART Camel AI source portfolio into one normalized, auditable public capability registry for the MVP.

The current registry uses new canonical identifiers F001 through F223. These identifiers do not claim that the historical documents used the same sequence. They form a normalization layer that prevents conflicts between legacy numbering schemes.

### Reviewed source patterns

The reviewed portfolio contains multiple generations of Arabic and English HTML documentation covering farms, health, genetics, grazing, Mazayen, festivals, auctions, marketplaces, products and environmental operations, together with revenue models describing operational service lines.

Three important patterns were identified:

1. Detailed source documents name real capabilities and describe objectives, benefits and operating logic. A substantial legacy sequence reaches the historical feature-78 range and includes many additional subsystems and enhancements.
2. A separate document explicitly records historical feature 169 for camel genetic-efficiency management and breed improvement.
3. A 1-to-200 index exists, but records 1 through 170 in that file are generated generic placeholders, while records 171 through 200 contain specific named functions and descriptions.

### Evidence rule

A number or heading is not counted as a documented capability merely because it appears in a list or template.

A capability is accepted into the normalized public registry when one or more of the following are present:

- a distinct functional name and meaningful description;
- an independent objective, benefit set and operating method;
- an earlier interface or demonstrator logic showing intended behavior;
- consistent appearance across Arabic or English source material;
- a clear independent subsystem boundary such as health, genetics, grazing, auctions or festival operations.

The following are not accepted as independent evidence:

- automatically repeated generic text;
- empty feature skeletons;
- feature numbers with no functional identity;
- the assumption that historical sample code proves production readiness.

### Current reconciliation result

After combining the initial MVP registry with source-derived granular capabilities, the current public registry contains 223 canonical capability records.

This is a count of capability records, not a claim that the platform contains 223 separate products. Some records are engines, workflows or sub-capabilities within larger capability families. This is intentional and supports technical due diligence by avoiding the compression of materially different functions into one marketing label.

### Legacy numbering versus canonical numbering

For example, F169 must not be interpreted as historical feature number 169. The F prefix is a new canonical MVP registry identifier only.

A later due-diligence package can add a separate legacy crosswalk linking each F-ID to its historical document and legacy feature number where that legacy number is reliable.

### Disclosure boundary

The public repository exposes capability names, maturity classifications and public demonstrations only. It does not publish private source documents, proprietary algorithms, confidential models, intellectual-property evidence files or private commercial valuation material.
