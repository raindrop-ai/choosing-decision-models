import assert from 'node:assert/strict';
import { pathToFileURL } from 'node:url';

export function checkPrivacy(repository, pages) {
  assert.equal(repository.full_name, 'raindrop-ai/judgment-calls', 'Unexpected deployment repository');
  assert.equal(repository.visibility, 'internal', 'Keep the repository internal until publication is approved');
  assert.equal(pages.public, false, 'Pages must be configured as PRIVATE before deploying');
  assert.equal(pages.build_type, 'workflow', 'Select GitHub Actions as the Pages build source');
  const url = new URL(pages.html_url);
  assert.equal(url.protocol, 'https:');
  assert.ok(url.hostname.endsWith('.pages.github.io'), 'Expected a private GitHub Pages address');
}

async function github(resource) {
  const response = await fetch(`https://api.github.com/repos/raindrop-ai/judgment-calls${resource}`, {
    headers: { Authorization: `Bearer ${process.env.GITHUB_TOKEN}`, Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' }
  });
  if (!response.ok) throw new Error(`Cannot verify private Pages configuration (HTTP ${response.status}). An administrator must configure private Pages in repository Settings → Pages. No deployment has been enabled.`);
  return response.json();
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  if (!process.env.GITHUB_TOKEN) throw new Error('GITHUB_TOKEN is required to verify access settings');
  checkPrivacy(await github(''), await github('/pages'));
  console.log('Verified: internal repository, private GitHub Pages, GitHub Actions build source.');
}
