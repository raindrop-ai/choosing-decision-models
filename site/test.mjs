import test from 'node:test';
import assert from 'node:assert/strict';
import { htmlPath, resolveLink, renderMarkdown } from './build.mjs';
import { checkPrivacy } from './privacy.mjs';

const files = new Set(['README.md','docs/methods.md','docs/assets/raindrop-logo.jpg','questions/README.md','questions/retrieval/a.md','results/baseline_predictions.csv']);
test('Markdown links work from nested pages and directory indexes', () => {
  assert.equal(htmlPath('README.md'),'index.html');
  assert.equal(htmlPath('questions/README.md'),'questions/index.html');
  assert.equal(resolveLink('../../README.md','questions/retrieval/a.md',files),'../../index.html');
  assert.equal(resolveLink('../questions/README.md#retrieval','docs/methods.md',files),'../questions/index.html#retrieval');
  assert.equal(resolveLink('../questions','docs/methods.md',files),'../questions/index.html');
  assert.equal(resolveLink('#scoring','docs/methods.md',files),'#scoring');
  for (const base of ['https://private-site.pages.github.io/','https://raindrop-ai.github.io/judgment-calls/']) {
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
  assert.equal(resolveLink('results/baseline_predictions.csv','README.md',files),'https://github.com/raindrop-ai/judgment-calls/blob/main/results/baseline_predictions.csv');
});
test('Untrusted question markup is escaped while disclosures remain usable', () => {
  const rendered = renderMarkdown('<script>alert(1)</script>\n\n<img src=x onerror=alert(1)>\n\n<details><summary>Answers</summary>\n\n[unsafe](javascript:alert%281%29)\n\n</details>','README.md',files);
  assert.ok(!rendered.includes('<script>'));
  assert.ok(!rendered.includes('<img src=x'));
  assert.ok(!rendered.includes('href="javascript:'));
  assert.ok(rendered.includes('<details><summary>Answers</summary>'));
  assert.ok(rendered.includes('</details>'));
});
test('Deployment verifies the internal repository and explicit private or public Pages settings', () => {
  const repo = {full_name:'raindrop-ai/judgment-calls',visibility:'internal'};
  const privateSite = {public:false,build_type:'workflow',html_url:'https://symmetrical-tribble-9e2vwqp.pages.github.io/'};
  const publicSite = {public:true,build_type:'workflow',html_url:'https://raindrop-ai.github.io/judgment-calls/'};
  for (const pages of [privateSite, publicSite, {...privateSite, public:true}]) {
    assert.doesNotThrow(() => checkPrivacy(repo,pages));
    for (const visibility of ['public','private',undefined]) assert.throws(() => checkPrivacy({...repo,visibility},pages));
    for (const publicValue of [undefined,null,'true']) assert.throws(() => checkPrivacy(repo,{...pages,public:publicValue}));
    for (const html_url of ['https://example.com/', 'https://raindrop-ai.github.io/another-project/', 'https://symmetrical-tribble-9e2vwqp.pages.github.io/?unexpected=true']) assert.throws(() => checkPrivacy(repo,{...pages,html_url}));
    assert.throws(() => checkPrivacy(repo,{...pages,build_type:'legacy'}));
  }
  assert.throws(() => checkPrivacy(repo,{...publicSite,public:false}));
});
