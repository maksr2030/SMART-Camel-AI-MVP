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

  function validateCamelRegistry(records){
    const errors = [];
    if (!Array.isArray(records)) return { valid:false, count:0, errors:['Registry must be an array'] };
    const seen = new Set();
    records.forEach(function(record, index){
      const prefix = 'Record ' + (index + 1);
      const id = normalizeCode(record && record.id);
      if (!/^CAMEL-\d{3}$/.test(id)) errors.push(prefix + ': invalid camel ID');
      if (seen.has(id)) errors.push(prefix + ': duplicate camel ID ' + id);
      seen.add(id);
      ['nameAr','nameEn','breedAr','breedEn','farmAr','farmEn'].forEach(function(key){
        if (!record || !String(record[key] == null ? '' : record[key]).trim()) errors.push(prefix + ': missing ' + key);
      });
      const age = Number(record && record.age);
      const health = Number(record && record.health);
      const activity = Number(record && record.activity);
      if (!Number.isFinite(age) || age <= 0) errors.push(prefix + ': invalid age');
      if (!Number.isFinite(health) || health < 0 || health > 100) errors.push(prefix + ': invalid health');
      if (!Number.isFinite(activity) || activity < 0 || activity > 100) errors.push(prefix + ': invalid activity');
    });
    return { valid:errors.length === 0, count:records.length, errors };
  }

  function findCamelById(records, id){
    const target = normalizeCode(id);
    return (Array.isArray(records) ? records : []).find(function(record){
      return normalizeCode(record.id) === target;
    }) || null;
  }

  function evaluateGeofence(point, boundary, nearThreshold){
    const threshold = nearThreshold == null ? 0.002 : Number(nearThreshold);
    const values = [point && point.lat, point && point.lng, boundary && boundary.minLat, boundary && boundary.maxLat, boundary && boundary.minLng, boundary && boundary.maxLng, threshold].map(Number);
    if (!values.every(Number.isFinite)) throw new TypeError('Geofence inputs must be finite numbers');
    const lat = values[0], lng = values[1], minLat = values[2], maxLat = values[3], minLng = values[4], maxLng = values[5];
    if (minLat >= maxLat || minLng >= maxLng || threshold < 0) throw new RangeError('Invalid geofence boundary or threshold');

    const inside = lat >= minLat && lat <= maxLat && lng >= minLng && lng <= maxLng;
    if (inside) {
      const margin = Math.min(lat - minLat, maxLat - lat, lng - minLng, maxLng - lng);
      return { state: margin <= threshold ? 'near' : 'inside', inside:true, distanceToBoundary:Number(margin.toFixed(6)) };
    }

    const dLat = lat < minLat ? minLat - lat : (lat > maxLat ? lat - maxLat : 0);
    const dLng = lng < minLng ? minLng - lng : (lng > maxLng ? lng - maxLng : 0);
    const distance = Math.sqrt(dLat * dLat + dLng * dLng);
    return { state: distance <= threshold ? 'near' : 'outside', inside:false, distanceToBoundary:Number(distance.toFixed(6)) };
  }

  function calculateMazayenScore(morphology, proportionality, movement){
    const values = [morphology, proportionality, movement].map(Number);
    if (!values.every(Number.isFinite)) throw new TypeError('Mazayen inputs must be finite numbers');
    if (values.some(function(value){ return value < 0 || value > 100; })) throw new RangeError('Mazayen inputs must be between 0 and 100');
    const score = values[0] * 0.40 + values[1] * 0.35 + values[2] * 0.25;
    return Number(score.toFixed(1));
  }

  function createAuctionState(id, startingBid){
    const bid = Number(startingBid);
    if (!normalizeCode(id)) throw new TypeError('Auction ID is required');
    if (!Number.isFinite(bid) || bid < 0) throw new RangeError('Starting bid must be a non-negative number');
    return { id:normalizeCode(id), status:'open', currentBid:bid, bidCount:0 };
  }

  function placeDemoBid(state, amount){
    if (!state || state.status !== 'open') throw new Error('Auction must be open');
    const bid = Number(amount);
    if (!Number.isFinite(bid) || bid <= Number(state.currentBid)) throw new RangeError('Bid must be higher than current bid');
    return {
      id:state.id,
      status:state.status,
      currentBid:bid,
      bidCount:Number(state.bidCount || 0) + 1
    };
  }

  function appendAuditEvent(events, event){
    const list = Array.isArray(events) ? events.slice() : [];
    if (!event || !String(event.type || '').trim()) throw new TypeError('Audit event type is required');
    if (!String(event.messageAr || '').trim() || !String(event.messageEn || '').trim()) throw new TypeError('Bilingual audit messages are required');
    list.unshift({
      sequence:list.length + 1,
      type:String(event.type),
      reference:String(event.reference || ''),
      messageAr:String(event.messageAr),
      messageEn:String(event.messageEn),
      time:event.time || null
    });
    return list;
  }

  const api = {
    ALLOWED_STATUSES,
    normalizeCode,
    verifyDemoCertificate,
    calculateHealthRisk,
    filterFeatures,
    countStatuses,
    validateCamelRegistry,
    findCamelById,
    evaluateGeofence,
    calculateMazayenScore,
    createAuctionState,
    placeDemoBid,
    appendAuditEvent
  };

  root.SMART_CAMEL_CORE = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
