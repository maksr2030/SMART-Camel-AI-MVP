(function() {
  const rows = [
    ['F236','breedRecognition','AI Camel Breed Recognition','التعرف الذكي على سلالات الإبل','Planned','Source-documented detailed capability','final-source-algorithmic'],
    ['F237','feedingControl','Closed-Loop Adaptive Feeding Control','التحكم التكيفي المغلق في تغذية الإبل','Planned','Source-documented detailed capability','final-source-algorithmic'],
    ['F238','biometricIdentity','Facial Biometric Camel Identification','التعرف البيومتري على الإبل ببصمة الوجه','Planned','Source-documented detailed capability','final-source-algorithmic'],
    ['F239','thermalHealth','Thermal-Camera Health Monitoring','المراقبة الصحية الحرارية بالكاميرات','Planned','Source-documented detailed capability','final-source-algorithmic'],
    ['F240','sleepWellbeing','Camel Sleep Monitoring and Quality Analysis','تتبع نوم الإبل وتحليل جودته','Planned','Source-documented detailed capability','final-source-algorithmic'],
    ['F241','heatStress','Camel Heat-Stress Early Warning','الإنذار المبكر بالإجهاد الحراري للإبل','Planned','Source-documented detailed capability','final-source-algorithmic'],
    ['F242','geneticHealth','Genetic Disease Risk Analysis','تحليل مخاطر الأمراض الوراثية','Planned','Source-documented detailed capability','final-source-algorithmic'],
    ['F243','reproductionHealth','Pregnancy and Labor Monitoring','مراقبة الحمل والولادة في الإبل','Planned','Source-documented detailed capability','final-source-algorithmic'],
  ];
  const mapped = rows.map(function (f) {
    return { id:f[0], domain:f[1], nameEn:f[2], nameAr:f[3], status:f[4], sourceClass:f[5], sourceTag:f[6] };
  });
  window.SMART_CAMEL_DATA.features.push.apply(window.SMART_CAMEL_DATA.features, mapped);
  window.SMART_CAMEL_DATA.metrics.find(function (m) { return m.key === 'featureCoverage'; }).value = String(window.SMART_CAMEL_DATA.features.length);
})();
