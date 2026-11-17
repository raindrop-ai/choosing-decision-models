import test from 'node:test';
import assert from 'node:assert/strict';
import { htmlPath, resolveLink, renderMarkdown } from './build.mjs';
import { checkPrivacy } from './privacy.mjs';

const files = new Set(['README.md','MANIFEST.json','docs/methods.md','docs/assets/raindrop-logo.jpg','questions/README.md','questions/retrieval/a.md','results/baseline_predictions.csv','licenses/sources/example/LICENSE.md','workers/example.py']);
test('Markdown links work from nested pages and directory indexes', () => {
  assert.equal(htmlPath('README.md'),'index.html');
  assert.equal(htmlPath('questions/README.md'),'questions/index.html');
  assert.equal(resolveLink('../../README.md','questions/retrieval/a.md',files),'../../index.html');
  assert.equal(resolveLink('../questions/README.md#retrieval','docs/methods.md',files),'../questions/index.html#retrieval');
  assert.equal(resolveLink('../questions','docs/methods.md',files),'../questions/index.html');
  assert.equal(resolveLink('#scoring','docs/methods.md',files),'#scoring');
  for (const base of ['https://private-site.pages.github.io/','https://raindrop-ai.github.io/choosing-decision-models/']) {
    const link = resolveLink('../../README.md','questions/retrieval/a.md',files);
    assert.equal(new URL(link,new URL(htmlPath('questions/retrieval/a.md'),base)).href,new URL('index.html',base).href);
  }
});
test('Unlisted, private and executable links cannot enter the website', () => {
  for (const href of ['../../.local/secret.json','javascript:alert(1)','data:text/html,hello','//tracker.invalid/a','/etc/passwd','../missing.md','%2e%2e/%2e%2e/%2e%2e/README.md']) {
    assert.equal(resolveLink(href,'docs/methods.md',files),null,href);
  }
  assert.equal(resolveLink('https://tracker.invalid/pixel.png','README.md',files,true),null);
  assert.equal(resolveLink('docs/assets/raindrop-logo.jpg','README.md',files,true),'docs/assets/raindrop-logo.jpg');
  assert.equal(resolveLink('results/baseline_predictions.csv','README.md',files),'https://github.com/raindrop-ai/choosing-decision-models/blob/main/results/baseline_predictions.csv');
});
test('Manifest and inventoried directories remain clickable without exposing unknown paths', () => {
  assert.equal(resolveLink('MANIFEST.json','README.md',files),'https://github.com/raindrop-ai/choosing-decision-models/blob/main/MANIFEST.json');
  assert.equal(resolveLink('../licenses/sources/','docs/methods.md',files),'https://github.com/raindrop-ai/choosing-decision-models/tree/main/licenses/sources');
  assert.equal(resolveLink('../workers/','docs/methods.md',files),'https://github.com/raindrop-ai/choosing-decision-models/tree/main/workers');
  assert.equal(resolveLink('../workers/','docs/methods.md',files,true),null);
  assert.equal(resolveLink('../unknown/','docs/methods.md',files),null);
});
test('Untrusted question markup is escaped while disclosures remain usable', () => {
  const rendered = renderMarkdown('<script>alert(1)</script>\n\n<img src=x onerror=alert(1)>\n\n<details><summary>Answers</summary>\n\n[unsafe](javascript:alert%281%29)\n\n</details>','README.md',files);
  assert.ok(!rendered.includes('<script>'));
  assert.ok(!rendered.includes('<img src=x'));
  assert.ok(!rendered.includes('href="javascript:'));
  assert.ok(rendered.includes('<details><summary>Answers</summary>'));
  assert.ok(rendered.includes('</details>'));
});
test('Generator comments stay hidden without removing the results or literal code', () => {
  const rendered = renderMarkdown('<!-- RESULTS_PREVIEW_START -->\n\n| Model | Accuracy |\n| --- | --- |\n| Jev | 88.8% |\n\n<!-- RESULTS_PREVIEW_END -->\n\n```html\n<!-- literal code -->\n```', 'README.md', files);
  assert.ok(!rendered.includes('RESULTS_PREVIEW_START'));
  assert.ok(!rendered.includes('RESULTS_PREVIEW_END'));
  assert.ok(rendered.includes('<table>'));
  assert.ok(rendered.includes('Jev'));
  assert.ok(rendered.includes('88.8%'));
  assert.ok(rendered.includes('&lt;!-- literal code --&gt;'));
});
test('Unmodified license text gets a readable page heading', () => {
  const rendered = renderMarkdown('MIT License\n\nCopyright (c) Example\n', 'licenses/sources/example/LICENSE.md', files);
  assert.ok(rendered.startsWith('<h1 id="mit-license">MIT License</h1>'));
  assert.ok(rendered.includes('Copyright (c) Example'));
});
test('The README website callout is shown on GitHub without a redundant link on the website', () => {
  const source = '# Guide\n\n**[Browse the companion website](https://raindrop-ai.github.io/choosing-decision-models/)**\n\n[Read the post](https://www.raindrop.ai/blog/choosing-decision-models/)';
  assert.ok(source.includes('Browse the companion website'));
  const rendered = renderMarkdown(source, 'README.md', files);
  assert.ok(!rendered.includes('Browse the companion website'));
  assert.ok(rendered.includes('Read the post'));
});
test('Deployment accepts the planned public repository without changing access settings', () => {
  const repo = {full_name:'raindrop-ai/choosing-decision-models',visibility:'internal'};
  assert.throws(() => checkPrivacy({...repo,full_name:'another/repository'}, {public:true,build_type:'workflow',html_url:'https://raindrop-ai.github.io/choosing-decision-models/'}));
  const privateSite = {public:false,build_type:'workflow',html_url:'https://symmetrical-tribble-9e2vwqp.pages.github.io/'};
  const publicSite = {public:true,build_type:'workflow',html_url:'https://raindrop-ai.github.io/choosing-decision-models/'};
  for (const pages of [privateSite, publicSite, {...privateSite, public:true}]) {
    for (const visibility of ['internal','public']) assert.doesNotThrow(() => checkPrivacy({...repo,visibility},pages));
    for (const visibility of ['private',undefined]) assert.throws(() => checkPrivacy({...repo,visibility},pages));
    for (const publicValue of [undefined,null,'true']) assert.throws(() => checkPrivacy(repo,{...pages,public:publicValue}));
    for (const html_url of ['https://example.com/', 'https://raindrop-ai.github.io/another-project/', 'https://symmetrical-tribble-9e2vwqp.pages.github.io/?unexpected=true']) assert.throws(() => checkPrivacy(repo,{...pages,html_url}));
    assert.throws(() => checkPrivacy(repo,{...pages,build_type:'legacy'}));
  }
  assert.throws(() => checkPrivacy(repo,{...publicSite,public:false}));
});
