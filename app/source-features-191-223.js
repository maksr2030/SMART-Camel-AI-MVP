(function() {
  const rows = [
  ['F191','audience','Star Rating System','نظام التقييم بالنجوم','Demonstrated','Source-reconciled documentation','legacy-detailed'],
  ['F192','rewards','Digital Badges','الشارات الرقمية','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F193','media','Photo and Video Evaluation','تقييم الصور والفيديو','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F194','audience','Direct Audience Evaluation','التقييم المباشر من الجمهور','Demonstrated','Source-reconciled documentation','legacy-detailed'],
  ['F195','audience','Creative Competition Management','إدارة مسابقات الإبداع','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F196','virtualExperience','Virtual Camel Evaluation','التقييم الافتراضي للإبل','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F197','virtualExperience','Virtual Festivals','المهرجانات الافتراضية','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F198','digitalFiles','Digital Camel Competition Files','الملفات الرقمية لمسابقات الإبل','Demonstrated','Source-reconciled documentation','legacy-detailed'],
  ['F199','analytics','Performance File Export','تصدير ملفات الأداء','Demonstrated','Source-reconciled documentation','legacy-detailed'],
  ['F200','analytics','Dynamic Performance Graphs','الرسوم البيانية الديناميكية للأداء','Implemented','Source-reconciled documentation','legacy-detailed'],
  ['F201','analytics','Camel Performance Comparison','مقارنة أداء الإبل','Implemented','Source-reconciled documentation','legacy-detailed'],
  ['F202','analytics','Performance Influencing-Factor Analysis','تحليل العوامل المؤثرة في الأداء','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F203','analytics','Shareable Performance Graphs','مشاركة رسوم الأداء','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F204','predictive','Future Camel Performance Forecasting','التنبؤ المستقبلي بأداء الإبل','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F205','recommendation','Automated Performance Tips','النصائح التلقائية للأداء','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F206','virtualExperience','Virtual-Reality Performance Simulation','محاكاة الأداء بالواقع الافتراضي','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F207','auction','Auction Attendance and Monitoring','إدارة الحضور والمتابعة في المزادات','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F208','auction','Global Electronic Camel Auctions','المزادات الإلكترونية العالمية للإبل','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F209','auction','Artificial-Intelligence Camel Value Analysis','تحليل قيمة الإبل بالذكاء الاصطناعي','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F210','fraud','Camel Fraud and Counterfeit Detection','كشف التزييف والغش في الإبل','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F211','beautyAI','Female Camel Beauty and Agility Evaluation','تقييم جمال ورشاقة إناث الإبل','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F212','beautyAI','Gender-Specific Beauty Evaluation','تقييم الجمال حسب الجنس','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F213','beautyAI','Breed and Gender Combined Beauty Criteria','معايير الجمال المدمجة حسب السلالة والجنس','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F214','commerce','International Camel Import and Export Workflow','مسار استيراد وتصدير الإبل الدولي','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F215','logistics','International Camel Shipment Tracking','تتبع شحنات الإبل الدولية','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F216','data','Global Camel Data Hub','المركز العالمي لبيانات الإبل','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F217','community','Professional Camel Community Network','شبكة التواصل المهني لقطاع الإبل','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F218','experience','User Satisfaction and Experience Analytics','تحليل رضا المستخدمين وتحسين التجربة','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F219','security','Security Audit and Data Protection','التدقيق الأمني وحماية البيانات','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F220','finance','Camel Production Economic Analysis','التحليل الاقتصادي لإنتاج الإبل','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F221','advisory','Personalized Breeder Advisory','الدعم الاستشاري الشخصي للمربين','Simulated','Source-reconciled documentation','legacy-detailed'],
  ['F222','training','Virtual Training and Interactive Learning','التدريب الافتراضي والتعلم التفاعلي','Planned','Source-reconciled documentation','legacy-detailed'],
  ['F223','training','Digital Training Certification','الشهادات الرقمية للتدريب','Planned','Source-reconciled documentation','legacy-detailed'],
  ];
  const mapped = rows.map(function (f) {
    return { id:f[0], domain:f[1], nameEn:f[2], nameAr:f[3], status:f[4], sourceClass:f[5], sourceTag:f[6] };
  });
  window.SMART_CAMEL_DATA.features.push.apply(window.SMART_CAMEL_DATA.features, mapped);
  window.SMART_CAMEL_DATA.metrics.find(function (m) { return m.key === 'featureCoverage'; }).value = String(window.SMART_CAMEL_DATA.features.length);
})();
