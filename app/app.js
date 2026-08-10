(function(){
  const data=window.SMART_CAMEL_DATA;
  const core=window.SMART_CAMEL_CORE;
  const translations={
    ar:{eyebrow:'النموذج الأولي العام',title:'منصة الإبل الذكية',subtitle:'بيئة تشغيل رقمية موحدة لهوية الإبل وصحتها ومزارعها وأنسابها وأسواقها ومسابقاتها ومخاطرها.',demoBadge:'بيانات عرض تجريبية',commandCenter:'مركز القيادة',heroTitle:'صورة تشغيلية موحدة لقطاع الإبل',heroText:'يعرض هذا النموذج بيانات اصطناعية ومحاكاة تشغيلية لإثبات بنية المنصة وقدراتها دون الادعاء بوجود نشر إنتاجي أو تكامل حكومي حي.',exploreFeatures:'استعرض الميزات',runSimulation:'شغّل المحاكاة',operationalView:'الحالة التشغيلية',camelRegistry:'سجل الإبل',synthetic:'اصطناعي',alerts:'التنبيهات',riskSignals:'إشارات المخاطر',aiSimulation:'محاكاة الذكاء',healthRiskTitle:'محرك مخاطر صحة الإبل',healthRiskText:'غيّر المؤشرات التالية لإنتاج درجة مخاطر تفسيرية تجريبية.',simulated:'محاكاة',temperature:'درجة الحرارة',activity:'النشاط',hydration:'الترطيب',riskScore:'درجة المخاطر',interpretation:'التفسير',featureRegistry:'سجل الميزات',platformCapabilities:'قدرات المنصة',featureRegistryText:'سجل موحد يوضح المجال والحالة ونوع الإثبات لكل قدرة في الإصدار العام.',allStatuses:'كل الحالات',marketplace:'السوق',auctionEngine:'محرك المزادات',auctionText:'محاكاة مسار التأهيل والعرض والمزايدة والنتيجة مع سجل أحداث واضح.',placeDemoBid:'نفّذ مزايدة تجريبية',competitions:'المسابقات',beautyEvaluation:'تقييم المزايين',beautyText:'نموذج تفسيري لعرض كيفية تجميع معايير الشكل والتناسق والحركة دون كشف نموذج مملوك.',demoScore:'درجة العرض',traceability:'التتبع',certificateVerification:'التحقق من الشهادة',certificateText:'أدخل رمز العرض CAMEL-001 للتحقق من هوية الجمل وسلامة سجل الشهادة التجريبية.',verify:'تحقق',auditEvidence:'الأدلة والتدقيق',auditTrail:'سجل الأحداث',footer:'SMART Camel AI MVP. جميع بيانات هذا العرض اصطناعية أو توضيحية.',registeredCamels:'الإبل المسجلة',activeFarms:'المزارع النشطة',healthAlerts:'تنبيهات الصحة',activeAuctions:'المزادات النشطة',connectedSensors:'المستشعرات المتصلة',featureCoverage:'الميزات المسجلة',id:'المعرف',name:'الاسم',breed:'السلالة',age:'العمر',health:'الصحة',low:'منخفض',medium:'متوسط',high:'مرتفع',riskLow:'المؤشرات الحالية ضمن النطاق التجريبي منخفض المخاطر.',riskMedium:'توجد مؤشرات تستدعي المتابعة والتحقق البشري.',riskHigh:'المؤشرات التجريبية تستدعي رفع الأولوية والمراجعة البيطرية.',bidPlaced:'تم تسجيل مزايدة تجريبية بقيمة 1,275,000 ريال سعودي.',verified:'تم التحقق من CAMEL-001 وسجل الشهادة التجريبية سليم.',notVerified:'رمز غير معروف في بيانات العرض.',search:'بحث في الميزات'},
    en:{eyebrow:'Public MVP Demonstrator',title:'SMART Camel AI',subtitle:'A unified digital operating environment for camel identity, health, farms, lineage, markets, competitions and risk.',demoBadge:'Demonstration Data',commandCenter:'Command Center',heroTitle:'A Unified Operating View of the Camel Sector',heroText:'This demonstrator uses synthetic data and operational simulation to prove platform structure and capabilities without claiming production deployment or live government integration.',exploreFeatures:'Explore Features',runSimulation:'Run Simulation',operationalView:'Operational View',camelRegistry:'Camel Registry',synthetic:'Synthetic',alerts:'Alerts',riskSignals:'Risk Signals',aiSimulation:'AI Simulation',healthRiskTitle:'Camel Health Risk Engine',healthRiskText:'Adjust the following indicators to generate an illustrative explainable risk score.',simulated:'Simulated',temperature:'Temperature',activity:'Activity',hydration:'Hydration',riskScore:'Risk Score',interpretation:'Interpretation',featureRegistry:'Feature Registry',platformCapabilities:'Platform Capabilities',featureRegistryText:'A unified registry showing the domain, maturity status and public evidence type for each capability.',allStatuses:'All statuses',marketplace:'Marketplace',auctionEngine:'Auction Engine',auctionText:'Demonstrates qualification, listing, bidding and outcome flow with a visible event record.',placeDemoBid:'Place Demo Bid',competitions:'Competitions',beautyEvaluation:'Beauty Evaluation',beautyText:'An explainable demonstration of how morphology, proportionality and movement criteria can be combined without exposing a proprietary model.',demoScore:'Demo Score',traceability:'Traceability',certificateVerification:'Certificate Verification',certificateText:'Enter demonstration code CAMEL-001 to verify camel identity and the synthetic certificate record.',verify:'Verify',auditEvidence:'Evidence and Audit',auditTrail:'Event Trail',footer:'SMART Camel AI MVP. All records in this demonstrator are synthetic or illustrative.',registeredCamels:'Registered Camels',activeFarms:'Active Farms',healthAlerts:'Health Alerts',activeAuctions:'Active Auctions',connectedSensors:'Connected Sensors',featureCoverage:'Registered Features',id:'ID',name:'Name',breed:'Breed',age:'Age',health:'Health',farm:'Farm',low:'Low',medium:'Medium',high:'High',riskLow:'Current indicators remain within the synthetic low-risk range.',riskMedium:'Some indicators require follow-up and human verification.',riskHigh:'Synthetic indicators justify higher priority and veterinary review.',bidPlaced:'A demonstration bid of SAR 1,275,000 was recorded.',verified:'CAMEL-001 verified and the synthetic certificate record is valid.',notVerified:'Unknown code in the demonstration dataset.',search:'Search features'}
  };

  if(!core) throw new Error('SMART_CAMEL_CORE is required before app.js');

  let lang='ar';
  const audit=[];
  const $=(id)=>document.getElementById(id);
  const t=(key)=>translations[lang][key]||key;

  function logEvent(ar,en,type){audit.unshift({time:new Date(),ar,en,type});renderAudit();}

  function renderTranslations(){
    document.documentElement.lang=lang;
    document.documentElement.dir=lang==='ar'?'rtl':'ltr';
    document.querySelectorAll('[data-i18n]').forEach(el=>{const key=el.dataset.i18n;if(translations[lang][key])el.textContent=translations[lang][key];});
    $('langToggle').textContent=lang==='ar'?'English':'العربية';
    $('featureSearch').placeholder=t('search');
  }

  function renderKpis(){$('kpis').innerHTML=data.metrics.map(m=>`<article class="kpi"><strong>${m.value}</strong><span>${t(m.key)}</span></article>`).join('');}

  function renderCamels(){
    const rows=data.camels.map(c=>`<tr><td>${c.id}</td><td>${lang==='ar'?c.nameAr:c.nameEn}</td><td>${lang==='ar'?c.breedAr:c.breedEn}</td><td>${c.age}</td><td><span class="health">${c.health}%</span></td><td>${c.activity}%</td><td>${lang==='ar'?c.farmAr:c.farmEn}</td></tr>`).join('');
    $('camelTableWrap').innerHTML=`<table><thead><tr><th>${t('id')}</th><th>${t('name')}</th><th>${t('breed')}</th><th>${t('age')}</th><th>${t('health')}</th><th>${t('activity')}</th><th>${t('farm')}</th></tr></thead><tbody>${rows}</tbody></table>`;
  }

  function renderAlerts(){$('alertsList').innerHTML=data.alerts.map(a=>`<div class="alert ${a.level}"><strong>${lang==='ar'?a.titleAr:a.titleEn}</strong><small>${lang==='ar'?a.textAr:a.textEn}</small></div>`).join('');}

  function renderFeatures(){
    const filtered=core.filterFeatures(data.features,$('featureSearch').value,$('featureStatus').value);
    $('featureGrid').innerHTML=filtered.map(f=>`<article class="feature"><span class="id">${f.id}</span><h3>${lang==='ar'?f.nameAr:f.nameEn}</h3><p>${f.domain}</p><span class="status-pill">${f.status}</span></article>`).join('');
    const counts=core.countStatuses(data.features);
    $('featureStats').innerHTML=Object.entries(counts).map(([k,v])=>`<span class="mini-stat">${k}: ${v}</span>`).join('')+`<span class="mini-stat">Total: ${data.features.length}</span>`;
  }

  function calculateRisk(){
    const temp=parseFloat($('temperature').value),activity=parseInt($('activity').value,10),hydration=parseInt($('hydration').value,10);
    $('temperatureOut').textContent=temp.toFixed(1)+' °C';$('activityOut').textContent=activity;$('hydrationOut').textContent=hydration;
    const result=core.calculateHealthRisk(temp,activity,hydration);
    $('riskScore').textContent=result.score;$('riskLabel').textContent=t(result.band);$('riskExplanation').textContent=t(result.explanationKey);
  }

  function renderAudit(){
    if(!audit.length){const initial=lang==='ar'?`تم تحميل بيانات العرض وتسجيل ${data.features.length} قدرة في السجل العام.`:`Demonstration data loaded and ${data.features.length} capabilities registered in the public feature registry.`;$('auditLog').innerHTML=`<div class="audit-item"><time>Session start</time><span>${initial}</span><small>system</small></div>`;return;}
    $('auditLog').innerHTML=audit.slice(0,8).map(e=>`<div class="audit-item"><time>${e.time.toLocaleTimeString(lang==='ar'?'ar-SA':'en-GB')}</time><span>${lang==='ar'?e.ar:e.en}</span><small>${e.type}</small></div>`).join('');
  }

  function renderAll(){renderTranslations();renderKpis();renderCamels();renderAlerts();renderFeatures();calculateRisk();renderAudit();}

  $('langToggle').addEventListener('click',()=>{lang=lang==='ar'?'en':'ar';renderAll();logEvent('تم تغيير اللغة إلى '+(lang==='ar'?'العربية':'الإنجليزية'),'Language changed to '+(lang==='ar'?'Arabic':'English'),'ui');});
  document.querySelectorAll('[data-target]').forEach(btn=>btn.addEventListener('click',()=>$(btn.dataset.target).scrollIntoView({behavior:'smooth'})));
  ['temperature','activity','hydration'].forEach(id=>$(id).addEventListener('input',calculateRisk));
  $('featureSearch').addEventListener('input',renderFeatures);$('featureStatus').addEventListener('change',renderFeatures);
  $('bidButton').addEventListener('click',()=>{$('bidResult').textContent=t('bidPlaced');logEvent('تم تنفيذ مزايدة تجريبية وتسجيلها في سجل الأحداث.','A demonstration bid was executed and recorded in the event trail.','auction');});
  $('verifyButton').addEventListener('click',()=>{const ok=core.verifyDemoCertificate($('verifyCode').value);$('verifyResult').textContent=t(ok?'verified':'notVerified');logEvent(ok?'تم التحقق من الشهادة التجريبية لـ CAMEL-001.':'فشل التحقق من رمز غير موجود في بيانات العرض.',ok?'The synthetic certificate for CAMEL-001 was verified.':'Verification failed for a code not present in the demo dataset.','verification');});

  renderAll();
})();
