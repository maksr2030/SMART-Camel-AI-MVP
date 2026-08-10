(function() {
  const rows = [
    ['F224','security','Post-Quantum Encryption for Veterinary and Trade Data','تشفير ما بعد الكم للبيانات البيطرية والتجارية','Planned','Patent-documented capability','patent-core'],
    ['F225','breeding','Use-Case Optimized Hybrid Breeding','التهجين المحسن حسب حالة الاستخدام','Planned','Patent-documented capability','patent-core'],
    ['F226','commerce','Automated Pre-Trade Health Evaluation','التقييم الصحي الآلي قبل التجارة','Simulated','Patent-documented capability','patent-core'],
    ['F227','commerce','Automated Pre-Trade Genetic Evaluation','التقييم الجيني الآلي قبل التجارة','Simulated','Patent-documented capability','patent-core'],
    ['F228','competition','Automated Competition Scoring Engine','محرك التقييم الآلي للمسابقات','Simulated','Patent-documented capability','patent-core'],
    ['F229','competition','Real-Time Competition Result Generation','توليد نتائج المسابقات في الزمن الحقيقي','Simulated','Patent-documented capability','patent-core'],
    ['F230','festival','Festival Suitability Matching and Participation Recommendation','مطابقة المهرجان الأنسب وتوصية المشاركة','Simulated','Source-reconciled documentation','legacy-detailed'],
    ['F231','integration','Veterinary Authority Integration Adapter','موصل التكامل مع الجهات البيطرية','Mock Integration','Patent-documented capability','patent-core'],
    ['F232','festivalHealth','Festival Participant Health Documentation','توثيق الحالة الصحية للإبل المشاركة في المهرجانات','Planned','Source-reconciled documentation','legacy-veterinary-164-169'],
    ['F233','racingTelemetry','Real-Time Race GPS and Speed Tracking','تتبع الموقع والسرعة أثناء السباقات في الزمن الحقيقي','Planned','Source-reconciled documentation','legacy-veterinary-164-169'],
    ['F234','productivity','Lifecycle Productivity Tracking','تتبع إنتاجية الإبل عبر دورة حياتها','Planned','Source-reconciled documentation','legacy-veterinary-164-169'],
    ['F235','sustainability','Renewable Energy Recommendations for Camel Farms','توصيات الطاقة المتجددة لمزارع الإبل','Planned','Source-reconciled documentation','legacy-farm-sustainability'],
  ];
  const mapped = rows.map(function (f) {
    return { id:f[0], domain:f[1], nameEn:f[2], nameAr:f[3], status:f[4], sourceClass:f[5], sourceTag:f[6] };
  });
  window.SMART_CAMEL_DATA.features.push.apply(window.SMART_CAMEL_DATA.features, mapped);
  window.SMART_CAMEL_DATA.metrics.find(function (m) { return m.key === 'featureCoverage'; }).value = String(window.SMART_CAMEL_DATA.features.length);
})();
