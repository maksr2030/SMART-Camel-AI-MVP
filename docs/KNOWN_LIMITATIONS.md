# Known Limitations | القيود المعروفة

## العربية

### الغرض

هذه الوثيقة جزء من حزمة العناية الواجبة التقنية لمنصة SMART Camel AI. هدفها منع الخلط بين اتساع النطاق المعماري وبين مستوى التنفيذ الحالي، وتقديم قائمة صريحة بالحدود التي يجب أن يعرفها أي مستحوذ أو مراجع تقني قبل اتخاذ قرار استثماري أو تقني.

### حدود الإصدار العام الحالي

1. **الإصدار العام MVP وليس نظام إنتاج كامل.** واجهة العرض الحالية مصممة لإثبات البنية ومسارات مختارة، وليست بديلاً عن منصة تشغيل وطنية أو مؤسسية مكتملة.
2. **بيانات العرض اصطناعية أو توضيحية.** سجلات الإبل، مؤشرات الصحة، المستشعرات، المزادات والنتائج في الواجهة العامة لا تمثل بيانات عملاء أو شركاء حقيقيين.
3. **لا توجد أجهزة IoT حية متصلة بالإصدار العام.** بيانات المستشعرات تمثيلية، ولا يثبت المستودع اتصالاً فعلياً بأطواق أو كاميرات أو أجهزة GPS أو أجهزة تحليل حليب أو مستشعرات حمل وولادة.
4. **لا يوجد تكامل حكومي أو بيطري أو بيئي حي.** جميع نقاط التكامل المعلمة Mock Integration لا تمثل اتصالاً إنتاجياً مع جهة خارجية.
5. **ليست جميع F001-F243 منفذة.** كل قدرة تحمل حالة نضج مستقلة: Implemented أو Demonstrated أو Simulated أو Mock Integration أو Planned.
6. **الخوارزميات الـ29 Source-Documented وليست جميعها نماذج إنتاجية متحققة.** وجود اسم أو منطق أو مثال كود في المصدر لا يثبت دقة إنتاجية أو اعتماداً مستقلاً أو صلاحية ميدانية.
7. **لا توجد نتائج دقة AI معتمدة منشورة.** لا يجب استخدام عبارات مثل 95% accuracy أو تخفيض النفوق/التكلفة كناتج مثبت ما لم يرفق اختبار مستقل وبيانات ومنهجية قابلة للمراجعة.
8. **المخرجات الصحية ليست تشخيصاً بيطرياً.** محرك المخاطر الحالي توضيحي، والقدرات المتعلقة بالأمراض والحمل والولادة والإجهاد الحراري والجينات تحتاج بيانات سريرية/بيطرية واعتماداً ميدانياً قبل الاستخدام التشخيصي.
9. **قدرات كشف التلاعب التصويري غير معتمدة كفحص رسمي.** CT، الأشعة تحت الحمراء، الموجات فوق الصوتية والتصوير الطيفي ممثلة كقدرات مخطط لها أو محاكاة ولا تمثل نظام تفتيش رسمي معتمد.
10. **الأنظمة الصوتية/فوق الصوتية/الضوئية للحماية والتوجيه تحتاج تحققاً ميدانياً واشتراطات رفاه الحيوان.** لا يقدم الإصدار العام دليلاً على فعالية ميدانية أو سلامة تشغيلية لهذه الأساليب.
11. **لا يوجد تقييم سوقي أو مالي معتمد.** أي تقدير قيمة جمل أو توقع سوقي داخل نطاق المنصة يجب اعتباره تحليلاً توضيحياً حتى يتم ربطه ببيانات سوق حقيقية ومنهج تقييم موثق.
12. **لا توجد معاملات مالية حقيقية.** مسار المزاد الحالي Demonstration فقط ولا يعالج أموالاً أو مدفوعات أو تسوية قانونية.
13. **الشهادات الحالية تجريبية.** CAMEL-001 مثال تحقق داخل MVP وليست شهادة حكومية أو بيطرية أو قانونية.
14. **لا توجد بنية إنتاجية موثقة للتوافر العالي أو التعافي من الكوارث.** الإصدار العام ثابت وخفيف، ولا يثبت HA/DR أو RTO/RPO أو multi-region deployment.
15. **لا توجد منظومة IAM إنتاجية.** الواجهة العامة لا تمثل نظام مستخدمين وأدوار وصلاحيات مؤسسية مكتمل.
16. **لا توجد قاعدة بيانات إنتاجية.** البيانات الحالية مضمّنة في ملفات JavaScript لأغراض العرض.
17. **لا توجد اختبارات أداء/تحميل إنتاجية منشورة.** لم يثبت بعد throughput أو latency أو concurrency لسيناريوهات تشغيل وطنية أو مؤسسية.
18. **لا توجد شهادة أمنية أو امتثال رسمي.** وجود توثيق أمني أو قدرات تشفير مخطط لها لا يعني ISO 27001 أو SOC 2 أو أي اعتماد أمني آخر.
19. **تشفير ما بعد الكم F224 Planned فقط.** لا يحتوي المستودع العام على تنفيذ تشفيري ما بعد كم ولا يقدم ادعاء اعتماد.
20. **الواقع الافتراضي/المعزز، 3D، blockchain والبث الحي ليست قدرات إنتاجية مثبتة في الإصدار العام** ما لم تكن حالة السجل تشير بوضوح إلى غير ذلك.
21. **الملكية الفكرية الخاصة غير منشورة.** الخوارزميات الأصلية، الأوزان، بيانات التدريب، منطق التقييم السري وملفات المصدر الخاصة تبقى خارج المستودع العام.
22. **الاعتماد على طرف ثالث لم يكتمل بعد كـSBOM قانوني نهائي.** الإصدار العام متعمد أن يكون خفيفاً بلا حزم runtime خارجية، لكن حزمة الاستحواذ النهائية يجب أن تتضمن مراجعة أوسع لكل أصل أو مكتبة أو أداة مستخدمة عبر دورة التطوير.
23. **لا توجد إيرادات أو تكاملات تجارية مثبتة داخل هذا المستودع.** لا يجوز تفسير اتساع النطاق أو الـMVP كإثبات إيراد أو عقد أو شراكة.

### ما يلزم لإزالة هذه القيود

- اختيار 10-20 قدرة استراتيجية ورفعها إلى Implemented/Demonstrated قوي مع اختبارات وسيناريوهات قابلة للتكرار.
- بناء backend وقاعدة بيانات وهوية وصلاحيات وتدقيق إنتاجي.
- بناء test pyramid: unit, integration, end-to-end, security, performance.
- توثيق deployment architecture وخطط backup/restore وRTO/RPO.
- تنفيذ مراجعة أمنية وThreat Model واختبارات SAST/DAST/secret/dependency scanning.
- تنفيذ برامج تحقق ميداني للقدرات التي تعتمد أجهزة أو صحة حيوان أو استشعاراً فيزيائياً.
- إنشاء Data Room سرية للأصول الخاصة، العقود، سجلات الملكية الفكرية والأدلة غير العامة.

## English

### Purpose

This document is part of the SMART Camel AI technical due-diligence package. It explicitly separates architectural scope from current execution maturity so that an acquirer can evaluate the platform without relying on inflated or ambiguous claims.

### Current public-release limitations

1. The public release is an MVP demonstrator, not a complete production platform.
2. Demonstration records and metrics are synthetic or illustrative.
3. No live physical IoT devices are connected to the public release.
4. No live government, veterinary-authority or environmental-platform integration is claimed.
5. Not all F001-F243 capabilities are implemented; every record carries an explicit maturity state.
6. The 29 named algorithms/engines are source-documented, not all independently validated production models.
7. No certified AI accuracy metrics are published.
8. Health outputs are illustrative and are not veterinary diagnosis.
9. Imaging-based manipulation detection is not represented as an approved official inspection system.
10. Acoustic, ultrasonic, light and deterrence concepts require field validation and animal-welfare review.
11. Market valuation and forecasting remain illustrative until connected to validated market datasets and methodology.
12. No real financial transactions are processed.
13. Demonstration certificates are not government, veterinary or legal certificates.
14. No production high-availability or disaster-recovery architecture has yet been evidenced.
15. No production IAM/role/permission system is evidenced in the public MVP.
16. No production database is used; demonstration data is stored in JavaScript assets.
17. No production load/performance benchmark is published.
18. No formal security or compliance certification is claimed.
19. F224 post-quantum encryption remains Planned and no public cryptographic implementation is published.
20. VR/AR, 3D, blockchain and live-streaming capabilities are not production-proven unless their registry maturity explicitly states otherwise.
21. Proprietary algorithms, model weights, training data and confidential decision logic are intentionally excluded from the public repository.
22. A final legal/software-component SBOM and third-party license review is still required for acquisition diligence.
23. The repository does not evidence revenue, commercial contracts or live partner integrations.

### Closure work

The principal closure path is to productionize a selected 10-20 strategic capabilities, strengthen automated testing and security evidence, document deployability and recovery, validate physical/health-dependent functions in controlled programs, and maintain confidential IP/legal evidence in a restricted acquisition data room.
