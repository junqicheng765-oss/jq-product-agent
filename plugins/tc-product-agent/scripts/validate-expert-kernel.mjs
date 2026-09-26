import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const frozen = {
  '00-foundation.md': '30313c5d2c20eb4b73ad8fc76ab0eb0dded1fec6ea56056f67de530ac6459ad0',
  'P1-product-logic.md': '1e29c5ce0abb1dbab03ec5c919fe825f5443739e18e7a1d809dc870671db91ab',
  'P2-cognition.md': '1257711df64b06ba3bcead4178961a14a379d7c39849da458ccf2f3871220b45',
  'P3-semantics.md': '3e91602868d7a647d8d08b4f3319d03b969b94717a7bd49aaa4fb1f267767e26',
  'P4-structure.md': '6c6ed0b13f05491f0f3717b1c5367a30a507c6d2a4a182ae68c725b31623ae7f',
  'P5-interaction.md': '9f54a8361998e65d39607195711d6856f68339eaabdb2fe9cf3b94a34399fb73',
  'P6-process.md': '8cb5ac15b4c085981af9861ec79c9ac015a91784bb5985d99d793fbb3c731cb0',
  'P7-perception.md': 'b9bc058e16ac4fce0ec0b8ffad221b8d644203fa94ecacddee1b19c632d06542',
};

function filesIn(dir) {
  return readdirSync(dir).flatMap(name => {
    const file = path.join(dir, name);
    return statSync(file).isDirectory() ? filesIn(file) : [file];
  });
}

export function validateExpertKernel(pluginRoot) {
  const root = path.resolve(pluginRoot);
  const expert = path.join(root, 'skills/jq-product-expert');
  const main = path.join(root, 'skills/tc-product-agent');
  const index = readFileSync(path.join(main, 'references/04-产品判断能力索引.md'), 'utf8');
  const canonical = new Map([...index.matchAll(/^\| (P[1-7]-\d+) \| ([^|]+) \|/gm)]
    .map(match => [match[1], match[2].trim()]));
  assert.equal(canonical.size, 48, 'Canonical index must contain 48 unique IDs');
  const found = new Map();
  let links = 0;
  for (const file of filesIn(expert)) {
    if (!file.endsWith('.md') && !file.endsWith('.yaml')) continue;
    const body = readFileSync(file, 'utf8');
    assert(!/\/Users\/|file:\/\/|\.codex\/skills\//.test(body), `Local dependency: ${file}`);
    for (const match of body.matchAll(/^### (P[1-7]-\d+) (.+)$/gm)) {
      const [id, name] = [match[1], match[2].trim().replace(/能力$/, '')];
      assert(!found.has(id), `Duplicate ID: ${id}`);
      assert.equal(name, canonical.get(id), `ID/name mismatch: ${id}`);
      found.set(id, name);
    }
    for (const match of body.matchAll(/\[[^\]\n]*\]\(([^)\n]+)\)/g)) {
      const href = match[1];
      assert(!/^(?:[a-z]+:|\/)/i.test(href), `External expert dependency: ${href}`);
      const target = path.resolve(path.dirname(file), decodeURIComponent(href.split('#')[0]));
      const relative = path.relative(root, target);
      assert(relative !== '..' && !relative.startsWith(`..${path.sep}`), `Escaped package: ${href}`);
      assert(existsSync(target), `Missing reference: ${href}`);
      links += 1;
    }
  }
  assert.equal(found.size, canonical.size, 'Expert must cover every canonical ID');
  for (const [name, expected] of Object.entries(frozen)) {
    const bytes = readFileSync(path.join(main, 'references/standards', name));
    assert.equal(createHash('sha256').update(bytes).digest('hex'), expected, `Frozen standard changed: ${name}`);
  }
  const source = readFileSync(path.join(main, 'sources/产品领域专家能力要求模型_完整版_最新.md'));
  assert.equal(createHash('sha256').update(source).digest('hex'),
    'a20d8eaac40a858af8fdd847834febcc3b5fb2b5372dd7b0bc319d9a67a3dde4', 'Frozen source changed');
  return { capabilities: found.size, links, frozenStandards: Object.keys(frozen).length, frozenSources: 1 };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
  console.log(JSON.stringify(validateExpertKernel(root)));
}
