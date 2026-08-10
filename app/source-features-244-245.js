(function() {
  const rows = [
    ['F244','sustainableGenetics','Genetic Breeding with Environmental Impact Analysis','التحسين الوراثي مع تحليل الأثر البيئي','Planned','Source-documented detailed capability','legacy-source-environmental-genetics'],
    ['F245','positiveEnvironmentalImpact','Positive Environmental Impact Evaluation for Camel Breeding','تقييم الأثر البيئي الإيجابي لتربية الإبل','Planned','Source-documented detailed capability','legacy-source-environmental-impact'],
  ];
  const mapped = rows.map(function (f) {
    return { id:f[0], domain:f[1], nameEn:f[2], nameAr:f[3], status:f[4], sourceClass:f[5], sourceTag:f[6] };
  });
  window.SMART_CAMEL_DATA.features.push.apply(window.SMART_CAMEL_DATA.features, mapped);
  window.SMART_CAMEL_DATA.metrics.find(function (m) { return m.key === 'featureCoverage'; }).value = String(window.SMART_CAMEL_DATA.features.length);
})();
