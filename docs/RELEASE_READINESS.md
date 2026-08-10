# Acquisition Release Readiness | جاهزية إصدار الاستحواذ

## العربية

### الغرض

هذه الوثيقة هي بوابة قرار لإصدار SMART Camel AI العام المخصص للفحص الأولي من مستحوذ أو فريق تقني. وهي تفصل بين **Acquisition Demonstrator Readiness** وبين **Production Readiness**.

### الحالة الحالية

| البوابة | الحالة | الدليل الحالي | ما يزال مطلوباً |
|---|---|---|---|
| G01 — Canonical Scope | Ready in branch | F001-F245 متصل وفريد في runtime والاختبارات | اجتياز PR CI النهائي |
| G02 — Source Reconciliation | Ready in branch | F001-F243 baseline + F244-F245 Phase 4 addendum | Data Room pointers للمصادر السرية |
| G03 — Strategic Evidence | Ready | 12/12 قدرات استراتيجية Grade A Evidence | Production validation منفصل |
| G04 — Evidence IDs | Ready | EVD-001-EVD-020 | توسيع evidence حسب تقدم productionization |
| G05 — Automated Tests | Ready in branch | validator + core + Phase 3 + Phase 4 + evidence contract | PR CI أخضر على head النهائي |
| G06 — Public Secret Scan | Ready in branch | `scripts/security_check.py` | PR CI أخضر + مراجعة مستقلة قبل الصفقة |
| G07 — Dependency/License Review | Documented | `DEPENDENCY_AND_LICENSE_REVIEW.md` | SBOM ومراجعة قانونية للنسخة الإنتاجية |
| G08 — Live Stable Demo | Pending | لا يوجد دليل موثق داخل المستودع حتى الآن | رابط تشغيل حي ومستقر والتحقق الخارجي منه |
| G09 — Fixed Acquisition Release Tag | Pending | لا يوجد tag نهائي بعد | إنشاء tag بعد CI + live demo verification |
| G10 — Chain of Title | Pending Confidential | checklist في `IP_NOTICE.md` | ملفات الملكية والتنازلات/المساهمين داخل Data Room |
| G11 — Production Security | Pending | Threat Model عام | IAM، backend security، SAST/DAST، pentest، key management، IR |
| G12 — Production Backend/Data | Pending | Public static demonstrator فقط | API، DB، persistence، backup/DR، observability |
| G13 — Field Validation | Pending | محاكاة/تصميم لعدد من قدرات الأجهزة | أجهزة وبيانات حقيقية وبروتوكولات تحقق ميداني |
| G14 — Commercial Evidence | Pending | لا يوجد إيراد/عقد مثبت في المستودع العام | عقود/إيرادات/LOIs أو فصلها صراحة عن forecast |
| G15 — Independent Validation | Pending | CI داخلي للمستودع | مراجعة مستقلة تقنية/أمنية/ميدانية حسب نطاق الصفقة |

### تعريف Ready

لا تعتبر البوابة Ready لمجرد وجود وثيقة. يجب أن يكون الدليل قابلاً لإعادة الفحص أو مرتبطاً بأثر واضح، وأن تبقى حدود ما لا يثبته الدليل معلنة.

### تعريف Acquisition Demonstrator Candidate

يمكن تسمية الإصدار **Acquisition Demonstrator Candidate** فقط عندما تتحقق الشروط التالية معاً:

1. F001-F245 كاملة دون فجوات أو تكرار.
2. جميع اختبارات CI المعلنة خضراء على PR/head النهائي.
3. فحص الأسرار والملفات الحساسة ناجح.
4. README والوثائق العامة متسقة على 245.
5. الرابط الحي مستقر ومتحقق منه خارج بيئة المطور.
6. Known Limitations وIP boundaries ظاهرة.

### تعريف Acquisition Release

لا يتم إنشاء tag مثل `v1.0-acquisition-demo` إلا بعد تحقق Acquisition Demonstrator Candidate وإثبات الرابط الحي. إنشاء tag لا يعني Production Ready.

### ما لا يعنيه هذا الإصدار

- لا يعني أن 245 قدرة منفذة إنتاجياً.
- لا يعني وجود اعتماد بيطري أو حكومي.
- لا يعني وجود أجهزة أو IoT حية.
- لا يعني وجود backend مؤسسي أو IAM إنتاجي.
- لا يعني وجود إيرادات أو عقود مثبتة.
- لا يعني اكتمال Chain of Title أو الفحص القانوني السري.

## English

This document is the decision gate for a buyer-facing SMART Camel AI acquisition demonstrator. It explicitly separates **Acquisition Demonstrator Readiness** from **Production Readiness**.

The current branch has automated/public evidence for the F001-F245 canonical scope, 12/12 strategic Grade A evidence paths, EVD-001-EVD-020, Phase 4 reconciliation, a public secret/sensitive-file scan and a dependency/license diligence note.

A final acquisition-demo tag must not be created until the final PR CI is green and a stable live demo has been independently verified. Production backend, IAM, field validation, confidential Chain of Title, production security testing, commercial proof and independent validation remain separate diligence gates.
