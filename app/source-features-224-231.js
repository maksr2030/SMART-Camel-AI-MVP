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
  ];
  const mapped = rows.map(function (f) {
    return { id:f[0], domain:f[1], nameEn:f[2], nameAr:f[3], status:f[4], sourceClass:f[5], sourceTag:f[6] };
  });
  window.SMART_CAMEL_DATA.features.push.apply(window.SMART_CAMEL_DATA.features, mapped);
  window.SMART_CAMEL_DATA.metrics.find(function (m) { return m.key === 'featureCoverage'; }).value = String(window.SMART_CAMEL_DATA.features.length);
})();
