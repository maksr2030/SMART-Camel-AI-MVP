(function(root){
  'use strict';

  const ALLOWED_STATUSES = ['Implemented','Demonstrated','Simulated','Mock Integration','Planned'];

  function normalizeCode(value){
    return String(value == null ? '' : value).trim().toUpperCase();
  }

  function verifyDemoCertificate(value){
    return normalizeCode(value) === 'CAMEL-001';
  }

  function calculateHealthRisk(temperature, activity, hydration){
    const temp = Number(temperature);
    const active = Number(activity);
    const hydrated = Number(hydration);
    if (![temp, active, hydrated].every(Number.isFinite)) {
      throw new TypeError('Health-risk inputs must be finite numbers');
    }

    let score = 0;
    score += Math.max(0, Math.abs(temp - 38.2) - 0.4) * 18;
    score += Math.max(0, 60 - active) * 0.65;
    score += Math.max(0, 70 - hydrated) * 0.8;
    score = Math.min(100, Math.max(0, Math.round(score)));

    let band = 'low';
    let explanationKey = 'riskLow';
    if (score >= 35) {
      band = 'medium';
      explanationKey = 'riskMedium';
    }
    if (score >= 65) {
      band = 'high';
      explanationKey = 'riskHigh';
    }

    return { score, band, explanationKey };
  }

  function filterFeatures(features, query, status){
    const list = Array.isArray(features) ? features : [];
    const q = String(query == null ? '' : query).trim().toLowerCase();
    const selectedStatus = status || 'all';
    return list.filter(function(feature){
      const text = [feature.id, feature.nameAr, feature.nameEn, feature.domain]
        .map(function(value){ return String(value == null ? '' : value); })
        .join(' ')
        .toLowerCase();
      const statusMatch = selectedStatus === 'all' || feature.status === selectedStatus;
      const queryMatch = !q || text.includes(q);
      return statusMatch && queryMatch;
    });
  }

  function countStatuses(features){
    const counts = {};
    ALLOWED_STATUSES.forEach(function(status){ counts[status] = 0; });
    (Array.isArray(features) ? features : []).forEach(function(feature){
      counts[feature.status] = (counts[feature.status] || 0) + 1;
    });
    return counts;
  }

  const api = {
    ALLOWED_STATUSES,
    normalizeCode,
    verifyDemoCertificate,
    calculateHealthRisk,
    filterFeatures,
    countStatuses
  };

  root.SMART_CAMEL_CORE = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
