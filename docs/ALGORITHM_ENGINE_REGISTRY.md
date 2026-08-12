# سجل الخوارزميات والمحركات | Algorithm & Engine Registry

## العربية

### الغرض

هذه الوثيقة تفصل أسماء الخوارزميات والمحركات التي ظهرت صراحة في ملفات المصدر التاريخية لمنصة SMART Camel AI عن **سجل القدرات الحالي F001-F245**. وجود اسم خوارزمية أو مثال كود في وثيقة مصدر يثبت وجود تصميم أو منطق موثق في المحفظة، لكنه لا يثبت تلقائياً وجود نموذج إنتاجي مدرّب أو دقة مثبتة أو نشر حي.

**النتيجة المعيارية الحالية: 29 خوارزمية ومحركاً مسمىً وموثقاً في المصدر، إضافة إلى نموذجَي تدريب مسميين بصورة مستقلة.**

إضافة F244 وF245 في Phase 4 رفعت عدد القدرات إلى 245 فقط؛ لم تُحتسب كأسماء خوارزمية جديدة لأن المطابقة لم تثبت اسم محرك مستقل جديد فوق الـ29 الموجودة.

لا ينشر هذا المستودع العام الأكواد الأصلية أو الأوزان أو مجموعات التدريب أو قواعد القرار الخاصة.

### 29 خوارزمية ومحركاً موثقاً

| # | الاسم الموثق في المصدر | العائلة الوظيفية | العلاقة بالسجل العام |
|---|---|---|---|
| 1 | Health Anomaly Detection Algorithm | الصحة الحيوية | F005 / F019 |
| 2 | Camel Breed Classification Algorithm | التعرف على السلالة | F236 |
| 3 | Geo-Behavioral Camel Tracker | التتبع والسلوك الجغرافي | F012 / F154 / F155 / F156 |
| 4 | Smart Camel Event Orchestrator | المسابقات وإدارة الأحداث | F032 / F163 / F228 / F229 |
| 5 | Goal-Based Genetic Matchmaker | التزاوج والتحسين الجيني | F108 / F109 / F225 / F244 cross-domain context |
| 6 | Adaptive Camel Feed Optimizer | التغذية التكيفية | F237 |
| 7 | Live Milk Composition Classifier | جودة الحليب أثناء الإنتاج | F124 / F128 |
| 8 | Infectious Risk Anticipator | مخاطر العدوى | F098 / F099 / F151 |
| 9 | Vaccination Compliance Predictor | الالتزام بالتطعيمات | F092 |
| 10 | CamelFaceID | الهوية البيومترية | F238 |
| 11 | ThermoPattern AI Detector | المراقبة الصحية الحرارية | F239 |
| 12 | CamelBehaviorNet | تحليل السلوك | F008 / F101 / F102 / F153 |
| 13 | SleepStageCamelAI | النوم والرفاه | F240 |
| 14 | MoodTrackCamelAI | الحالة السلوكية والرفاه | F061 / F101 |
| 15 | HeatRiskPredictorCamel | الإجهاد الحراري | F241 |
| 16 | CamelBioVitalAI | الصحة والسلوك والنشاط الحيوي | F005 / F008 / F019 |
| 17 | CamelMilkAI | تحليل جودة حليب الإبل | F124 / F128 |
| 18 | CamelLaborPredictAI | الحمل والولادة | F243 |
| 19 | BehaviorPredictionAlgo | سلوك المناطق الخطرة | F102 / F155 |
| 20 | MoodClassificationViaAudioVisual | التصنيف السلوكي متعدد الوسائط | F061 / F153 / F187 |
| 21 | Integrated Health Analysis Algorithm | التحليل الصحي المتكامل | F005 / F019 / F022 |
| 22 | Early Disease Prediction Algorithm | التنبؤ المبكر بالأمراض | F091 |
| 23 | Smart Treatment Recommendation Algorithm | دعم التوصيات الصحية | F020 / F093 |
| 24 | Biosensor Accuracy Optimization Algorithm | جودة بيانات المستشعرات | F007 / F019 |
| 25 | Camel Beauty Smart Judging Algorithm | تحكيم المزايين | F027 / F068 / F228 |
| 26 | Motion and Performance Analysis Algorithm | الحركة والأداء | F067 / F172 / F178 |
| 27 | Concurrent Events Management Algorithm | إدارة الفعاليات المتزامنة | F163 |
| 28 | Integrated Scoring Algorithm | تجميع درجات المسابقات | F228 / F229 |
| 29 | Performance Predictive Analysis Algorithm | التنبؤ بأداء المسابقات | F178 / F204 |

### نماذج التدريب المسماة في المصدر

- **CamelBehaviorClassifier** — نموذج تصنيف سلوكي مرتبط بتحليل اقتراب الإبل من المناطق الخطرة.
- **CamelEmotionNet** — نموذج موثق لتحليل مؤشرات السلوك/الرفاه من بيانات مرئية وصوتية.

### قاعدة الإفصاح

- عبارة **Source-documented** تعني أن الاسم أو التصميم ورد في ملفات المصدر التي جرى فحصها.
- لا تعني العبارة أن الخوارزمية منشورة إنتاجياً أو مدربة على مجموعة بيانات معتمدة أو خضعت لاختبار مستقل.
- لا يكرر هذا السجل الخوارزمية إذا ظهرت بالعربية والإنجليزية أو في أكثر من نسخة من الملف نفسه.
- القدرة الجديدة لا ترفع عدد الخوارزميات إلا إذا ظهر اسم/محرك مستقل قابل للفصل في المصدر.
- الأمثلة البرمجية التاريخية لا تُنشر هنا لحماية حدود الملكية الفكرية وتقليل مخاطر تفسيرها كتنفيذ إنتاجي.

## English

This document separates explicitly named algorithms and engines found in the historical SMART Camel AI source portfolio from the **current F001-F245 capability registry**.

**Current normalized result: 29 source-documented named algorithms and engines, plus two independently named training models.**

Phase 4 increased the canonical capability scope to 245 through F244 and F245, but it did **not** increase the named algorithm/engine count because no additional independently named engine was established by that reconciliation.

A named algorithm or source code example demonstrates documented design intent or source logic; it does not automatically prove a trained production model, validated accuracy, certification, or live deployment. Proprietary code, model weights, training datasets and confidential decision rules remain excluded from the public repository.
