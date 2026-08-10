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
load('app/source-features-244-245.js');
load('app/core.js');

const data = context.window.SMART_CAMEL_DATA;
const core = context.window.SMART_CAMEL_CORE;

assert.equal(data.features.length, 245, 'Phase 4 requires exactly 245 canonical capability records');
const ids = Array.from(data.features, f => f.id);
const expected = Array.from({ length: 245 }, (_, i) => `F${String(i + 1).padStart(3, '0')}`);
assert.equal(ids.join(','), expected.join(','), 'Capability IDs must remain continuous F001-F245');
assert.equal(new Set(ids).size, 245, 'Capability IDs must remain unique');

const f244 = data.features.find(f => f.id === 'F244');
const f245 = data.features.find(f => f.id === 'F245');
assert.ok(f244, 'F244 must exist');
assert.ok(f245, 'F245 must exist');
assert.equal(f244.status, 'Planned');
assert.equal(f245.status, 'Planned');
assert.equal(f244.nameEn, 'Genetic Breeding with Environmental Impact Analysis');
assert.equal(f245.nameEn, 'Positive Environmental Impact Evaluation for Camel Breeding');
assert.equal(f244.sourceTag, 'legacy-source-environmental-genetics');
assert.equal(f245.sourceTag, 'legacy-source-environmental-impact');

const environmental = core.filterFeatures(data.features, 'environmental impact', 'Planned');
assert.ok(environmental.some(f => f.id === 'F244'), 'F244 must be discoverable by search/filter');
assert.ok(environmental.some(f => f.id === 'F245'), 'F245 must be discoverable by search/filter');

const metric = data.metrics.find(m => m.key === 'featureCoverage');
assert.ok(metric, 'featureCoverage metric must exist');
assert.equal(metric.value, '245', 'Runtime featureCoverage KPI must equal 245');

console.log('SMART Camel AI Phase 4 reconciliation tests passed.');
console.log('Canonical scope: 245 continuous unique records F001-F245');
console.log('F244: source-backed Planned capability verified');
console.log('F245: source-backed Planned capability verified');
console.log('Runtime feature coverage KPI: 245');
