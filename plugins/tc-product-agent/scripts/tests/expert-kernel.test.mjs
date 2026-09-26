import assert from 'node:assert/strict';
import { mkdtempSync, cpSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import test from 'node:test';
import { validateExpertKernel } from '../validate-expert-kernel.mjs';

const source = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');

test('bundled candidate preserves IDs, relative references and frozen standards', () => {
  assert.equal(validateExpertKernel(source).capabilities, 48);
});

const mutations = [
  ['unknown ID', 'skills/jq-product-expert/chapters/ch02-product-logic.md', body => body.replace('### P1-1 ', '### P1-99 '), /ID\/name mismatch/],
  ['name drift', 'skills/jq-product-expert/chapters/ch02-product-logic.md', body => body.replace('### P1-1 产品价值及目标理解能力', '### P1-1 新能力'), /ID\/name mismatch/],
  ['missing reference', 'skills/jq-product-expert/SKILL.md', body => body.replace('(chapters/ch01-foundation.md)', '(chapters/missing.md)'), /Missing reference/],
  ['frozen definition edit', 'skills/tc-product-agent/references/standards/00-foundation.md', body => body + '\nchanged\n', /Frozen standard changed/],
  ['frozen source edit', 'skills/tc-product-agent/sources/产品领域专家能力要求模型_完整版_最新.md', body => body + '\nchanged\n', /Frozen source changed/],
  ['local dependency', 'skills/jq-product-expert/SKILL.md', body => body + '\n[Local](/Users/example/input.md)\n', /Local dependency/],
  ['package escape', 'skills/jq-product-expert/SKILL.md', body => body + '\n[Outside](../../../outside.md)\n', /Escaped package/],
];

for (const [name, relative, mutate, message] of mutations) {
  test(`rejects ${name}`, () => {
    const temporary = mkdtempSync(path.join(os.tmpdir(), 'jq-expert-check-'));
    try {
      for (const skill of ['tc-product-agent', 'jq-product-expert']) {
        cpSync(path.join(source, 'skills', skill), path.join(temporary, 'skills', skill), { recursive: true });
      }
      const file = path.join(temporary, relative);
      writeFileSync(file, mutate(readFileSync(file, 'utf8')));
      assert.throws(() => validateExpertKernel(temporary), message);
    } finally {
      rmSync(temporary, { recursive: true, force: true });
    }
  });
}
