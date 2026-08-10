# Dependency & License Review | مراجعة الاعتماديات والتراخيص

## العربية

### الغرض

هذه الوثيقة تلخص سطح الاعتماديات العامة في SMART Camel AI MVP لأغراض العناية الواجبة التقنية. هي مراجعة عامة للمستودع وليست رأياً قانونياً نهائياً في الملكية أو الترخيص.

### نتيجة التحقق في Phase 4

تم التحقق مباشرة من فرع Phase 4 الحالي من عدم وجود:

- `package.json`.
- `requirements.txt`.
- `LICENSE` عام.

ويحرس `scripts/release_check.py` هذه الحدود في إصدار الاستحواذ الحالي؛ إضافة أي ملف منها مستقبلاً يجب أن تقترن بمراجعة الاعتماديات/الترخيص وتحديث الوثائق قبل السماح بمرور Release Gate.

### Runtime العام

الإصدار العام يعمل باستخدام:

- HTML.
- CSS.
- JavaScript داخل المستودع.

لا يعتمد runtime الحالي على npm packages أو CDN scripts أو SDKs مدفوعة أو قواعد بيانات أو خدمات SaaS خارجية. `index.html` يحمل ملفات محلية فقط، ويتم فحص ذلك آلياً في `scripts/security_check.py`.

### GitHub Actions

الـCI يستخدم إجراءات GitHub الرسمية التالية:

- `actions/checkout@v4`.
- `actions/setup-python@v5`.

هذه اعتماديات CI وليست اعتماديات runtime للمنتج.

### Python / Node

- اختبارات Python تستخدم المكتبة القياسية فقط.
- اختبارات Node تستخدم وحدات Node القياسية فقط (`assert`, `fs`, `vm`).
- لا يوجد `package.json` مطلوب لتشغيل الـMVP العام.
- لا يوجد ملف متطلبات Python مطلوب للـMVP العام.

### ملف LICENSE

لا يوجد في الحزمة العامة الحالية ملف `LICENSE` يمنح تلقائياً حقوق استخدام أو إعادة توزيع للملكية الفكرية الخاصة. الوصول العام إلى المستودع لا يعني بيعاً أو تنازلاً أو ترخيصاً ضمنياً للأصول الخاصة. المرجع العام لحدود الملكية هو `docs/IP_NOTICE.md`، أما شروط الصفقة أو الترخيص فتحدد قانونياً في مستندات منفصلة.

### ما يجب إغلاقه قبل صفقة استحواذ نهائية

1. سجل رسمي لكل مكون طرف ثالث مستخدم في النسخة الإنتاجية المستقبلية.
2. SBOM للنسخة المرشحة للإنتاج.
3. مراجعة تراخيص أي مكتبات أو نماذج أو datasets تدخل بعد MVP العام.
4. إثبات حقوق المساهمين/المتعاقدين إن وجدوا.
5. تحديد Background IP وTransferred IP وExcluded IP في مستند الصفقة.
6. مراجعة قانونية مستقلة قبل الإغلاق.

## English

The public SMART Camel AI MVP has a deliberately minimal dependency surface. Phase 4 directly verified that the current branch does not contain `package.json`, `requirements.txt`, or a public `LICENSE` file.

The runtime uses repository-local HTML, CSS and JavaScript only. There are no required npm packages, external CDN runtime scripts, paid SDKs, databases or SaaS services. CI uses official GitHub Actions (`actions/checkout@v4`, `actions/setup-python@v5`), while Python and Node tests rely only on their standard libraries.

No public `LICENSE` file currently grants blanket reuse or redistribution rights over proprietary platform IP. Public repository access must not be interpreted as an assignment, sale or implied license. `scripts/release_check.py` protects the current release boundary so that introducing package manifests or a public license requires an explicit diligence update before the acquisition-release gate can pass.
