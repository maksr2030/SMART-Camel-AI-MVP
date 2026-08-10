import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const context = { window: {} };
vm.createContext(context);

function load(path) {
  vm.runInContext(fs.readFileSync(path, 'utf8'), context, { filename: path });
}

load('app/data.js');
load('app/source-features-091-140.js');
load('app/source-features-141-190.js');
load('app/source-features-191-223.js');
load('app/source-features-224-231.js');
load('app/source-features-232-235.js');
load('app/source-features-236-243.js');
load('app/core.js');

const data = context.window.SMART_CAMEL_DATA;
const core = context.window.SMART_CAMEL_CORE;

assert.ok(core, 'SMART_CAMEL_CORE must load');
assert.equal(data.features.length, 243, 'Capability registry must contain 243 records');

const expectedIds = Array.from({ length: 243 }, (_, i) => `F${String(i + 1).padStart(3, '0')}`);
const actualIds = Array.from(data.features, f => f.id);
assert.equal(actualIds.join(','), expectedIds.join(','), 'F001-F243 must be continuous and ordered');
assert.equal(new Set(actualIds).size, 243, 'Capability IDs must be unique');

for (const feature of data.features) {
  assert.ok(feature.nameAr, `${feature.id} must have Arabic name`);
  assert.ok(feature.nameEn, `${feature.id} must have English name`);
  assert.ok(core.ALLOWED_STATUSES.includes(feature.status), `${feature.id} has unsupported maturity status`);
}

const counts = core.countStatuses(data.features);
assert.equal(Object.values(counts).reduce((sum, value) => sum + value, 0), 243, 'Maturity counts must sum to 243');
for (const status of core.ALLOWED_STATUSES) assert.ok(counts[status] > 0, `${status} must be represented`);

const low = core.calculateHealthRisk(38.2, 72, 78);
assert.equal(low.score, 0);
assert.equal(low.band, 'low');
assert.equal(low.explanationKey, 'riskLow');

const medium = core.calculateHealthRisk(40.5, 40, 60);
assert.equal(medium.band, 'medium');
assert.ok(medium.score >= 35 && medium.score < 65);

const high = core.calculateHealthRisk(42, 0, 0);
assert.equal(high.band, 'high');
assert.equal(high.score, 100, 'Risk score must be capped at 100');
assert.throws(() => core.calculateHealthRisk('x', 50, 50), /finite numbers/);

assert.equal(core.verifyDemoCertificate('CAMEL-001'), true);
assert.equal(core.verifyDemoCertificate(' camel-001 '), true);
assert.equal(core.verifyDemoCertificate('CAMEL-999'), false);

const planned243 = core.filterFeatures(data.features, 'F243', 'Planned');
assert.equal(planned243.length, 1);
assert.equal(planned243[0].nameEn, 'Pregnancy and Labor Monitoring');

const pregnancySearch = core.filterFeatures(data.features, 'pregnancy', 'all');
assert.ok(pregnancySearch.some(f => f.id === 'F243'));

const identitySearch = core.filterFeatures(data.features, 'الهوية الرقمية', 'Implemented');
assert.ok(identitySearch.some(f => f.id === 'F001'));

assert.ok(data.camels.some(c => c.id === 'CAMEL-001'), 'Synthetic registry must include CAMEL-001');
assert.ok(data.alerts.some(a => /geofence/i.test(a.titleEn)), 'Synthetic alerts must include geofence evidence');

console.log('SMART Camel AI core evidence tests passed.');
console.log('Capabilities: 243 continuous F001-F243');
console.log(`Maturity counts: ${JSON.stringify(counts)}`);
console.log('Health-risk bands: low / medium / high verified');
console.log('Certificate verification: positive and negative paths verified');
console.log('Feature search/filter and synthetic evidence records verified');
