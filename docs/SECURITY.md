# Security Baseline & Threat Model | خط الأساس الأمني ونموذج التهديدات

## العربية

### نطاق هذه الوثيقة

هذه الوثيقة تصف الوضع الأمني **للـMVP العام الحالي** وما يجب استكماله قبل أي نشر إنتاجي أو استحواذ تقني نهائي. لا تمثل شهادة امتثال أو اختبار اختراق مستقل.

### خصائص الإصدار العام الحالية

- واجهة HTML/CSS/JavaScript ثابتة وخفيفة بلا قاعدة بيانات أو backend إنتاجي.
- لا توجد مفاتيح API أو بيانات اعتماد لازمة لتشغيل العرض العام.
- لا توجد بيانات ملاك أو شركاء أو سجلات بيطرية حقيقية في الإصدار العام.
- التكاملات الخارجية ممثلة كـMock Integration ولا توجد اتصالات حكومية أو بيطرية حية.
- الخوارزميات الخاصة والأوزان وبيانات التدريب وقواعد القرار السرية ليست ضمن المستودع العام.

هذه الخصائص تقلل سطح الهجوم في الـMVP، لكنها لا تعفي النسخة الإنتاجية المستقبلية من ضوابط الأمن المؤسسي.

### الأصول المطلوب حمايتها

1. هوية الإبل والسجلات والملكية والشهادات.
2. بيانات الملاك والمربين والمزارع عند إدخالها مستقبلاً.
3. السجلات الصحية والبيطرية والجينية.
4. بيانات المواقع والمسارات والمستشعرات.
5. بيانات المزادات والمعاملات والتقييمات.
6. الخوارزميات المملوكة، الأوزان، قواعد التحكيم ونماذج القرار.
7. سجلات التدقيق والأدلة وسلسلة المصدر.
8. مفاتيح التكامل والاعتمادات والأسرار في أي نشر إنتاجي.

### الجهات/المهاجمون المحتملون

- مستخدم غير مصرح له يحاول الوصول إلى سجلات حساسة.
- مشارك في مزاد أو مسابقة يحاول التلاعب بالبيانات أو النتيجة.
- طرف داخلي يسيء استخدام الصلاحيات.
- مهاجم خارجي يستهدف API أو البنية السحابية المستقبلية.
- طرف يحاول سرقة الخوارزميات أو إعادة بناء قواعد التقييم.
- جهاز IoT مزيف أو مخترق يرسل قياسات كاذبة.
- مهاجم يحاول تغيير سجل الملكية أو الشهادة أو السجل الصحي.
- هجوم supply-chain عبر مكتبة أو أداة أو pipeline.

### التهديدات الأساسية وضوابط الإغلاق المطلوبة

| التهديد | أثره | وضع MVP العام | المطلوب للإنتاج |
|---|---|---|---|
| Unauthorized access | كشف أو تعديل بيانات حساسة | لا توجد حسابات إنتاجية | IAM، MFA، RBAC/ABAC، session controls |
| Data tampering | تزوير صحة/ملكية/نتائج | بيانات العرض محلية | signed events، DB constraints، audit integrity |
| API abuse | تسريب/تعديل/DoS | لا يوجد API إنتاجي | API gateway، authN/Z، rate limiting، schema validation |
| IoT spoofing | قراءات كاذبة | لا أجهزة حية | device identity، certificate provisioning، signed telemetry |
| Algorithm/IP extraction | فقدان أسرار تجارية | التنفيذ الخاص غير منشور | service isolation، access control، code/model vaulting |
| Auction manipulation | ضرر تجاري وقانوني | مزاد تجريبي فقط | transactional integrity، anti-fraud، immutable audit |
| Certificate forgery | تغيير هوية أو ملكية | شهادة تجريبية | signing keys، PKI/key management، revocation model |
| Genetic/health privacy breach | كشف بيانات حساسة | لا بيانات حقيقية | encryption، consent, retention, access logging |
| Supply-chain compromise | إدخال كود ضار | runtime عام بلا حزم خارجية | SBOM، dependency pinning، provenance، SCA |
| Secret leakage | اختراق خدمات خارجية | لا أسرار لازمة للعرض | secret scanning، vault, rotation, least privilege |
| CI/CD compromise | نشر كود غير موثوق | validation workflow موجود | protected branches، required reviews/checks، signed releases |
| Availability attack | توقف الخدمة | static MVP | WAF/CDN، autoscaling، DR, monitoring, incident response |

### الحد الأدنى المطلوب قبل Production Due Diligence

1. Threat model رسمي لكل من Web/API/IoT/AI/Data layers.
2. IAM architecture مع MFA وRBAC/ABAC وفصل الواجبات.
3. تشفير TLS للنقل وencryption-at-rest للبيانات الحساسة.
4. إدارة مفاتيح وأسرار مركزية مع rotation.
5. SAST وSCA وsecret scanning في CI.
6. DAST واختبار اختراق مستقل للنسخة المرشحة للإنتاج.
7. SBOM ومراجعة تراخيص كل المكونات.
8. Centralized logging/SIEM وحماية سجل التدقيق.
9. Incident Response Plan وsecurity contact process.
10. Backup/restore validation وخطة DR.
11. حماية API: schema validation, authorization, rate limits, replay protection عند الحاجة.
12. هوية وتوثيق أجهزة IoT، secure boot/firmware signing عند استخدام أجهزة ميدانية.
13. AI-specific controls: dataset provenance، model/version registry، input validation، output confidence/abstention، human override، monitoring for drift.
14. Privacy/data-governance assessment للبيانات الصحية والجينية وبيانات المواقع.
15. مراجعة مستقلة قبل الادعاء بأي اعتماد أو جاهزية أمنية مؤسسية.

### تصنيف الأدلة الأمنية

- **E0 — Not evidenced:** فكرة/متطلب فقط.
- **E1 — Documented:** موثق في المعمارية أو السياسة.
- **E2 — Automated check:** اختبار/فحص آلي قابل للتكرار.
- **E3 — Demonstrated control:** الضابط يعمل في بيئة عرض/اختبار.
- **E4 — Independent validation:** تحقق طرف مستقل أو اختبار اختراق/تدقيق رسمي.

الهدف قبل الاستحواذ التقني المتقدم هو أن تكون الضوابط الحرجة E2-E3 على الأقل، مع E4 للأمن عالي الحساسية قبل نشر إنتاجي فعلي.

### حدود الإفصاح

هذه الوثيقة لا تنشر مفاتيح أو أسراراً أو تفاصيل استغلال أو منطقاً أمنياً خاصاً. تفاصيل البنية الخاصة وتقارير الاختراق الكاملة يجب أن توضع في Data Room مقيدة الصلاحية وتحت NDA.

## English

### Scope

This document describes the **current public MVP security posture** and the control work required before production deployment or final technical acquisition diligence. It is not a certification or an independent penetration-test report.

### Current public-MVP characteristics

- Lightweight static HTML/CSS/JavaScript presentation with no production backend or database.
- No API keys or credentials are required to run the public demonstrator.
- No real owner, partner, veterinary or genetic records are published.
- External integrations are Mock Integration only.
- Proprietary algorithms, weights, training datasets and confidential decision rules are excluded.

### Required production-security work

Production readiness requires formal threat modelling, IAM/MFA/RBAC, encryption, centralized secret/key management, SAST/SCA/secret scanning, DAST and independent penetration testing, an SBOM and license review, protected CI/CD, centralized logging and incident response, tested backup/DR, API abuse controls, authenticated IoT devices, and AI-specific provenance/version/monitoring controls.

### Evidence scale

- **E0 — Not evidenced**
- **E1 — Documented**
- **E2 — Automated check**
- **E3 — Demonstrated control**
- **E4 — Independently validated**

Critical controls should reach at least E2-E3 for advanced acquisition diligence, with E4 targeted for high-risk production security before live deployment.
