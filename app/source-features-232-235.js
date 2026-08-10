(function() {
  const rows = [
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
