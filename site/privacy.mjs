import assert from 'node:assert/strict';
import { pathToFileURL } from 'node:url';

export function checkPrivacy(repository, pages) {
  assert.equal(repository.full_name, 'raindrop-ai/judgment-calls', 'Unexpected deployment repository');
  assert.equal(repository.visibility, 'internal', 'The repository must remain internal');
  assert.equal(typeof pages.public, 'boolean', 'Pages visibility must be explicitly reported by GitHub');
  assert.equal(pages.build_type, 'workflow', 'Select GitHub Actions as the Pages build source');
  const url = new URL(pages.html_url);
  assert.equal(url.protocol, 'https:');
  const privateAddress = 'https://symmetrical-tribble-9e2vwqp.pages.github.io/';
  const allowedAddresses = pages.public
    ? [privateAddress, 'https://raindrop-ai.github.io/judgment-calls/']
    : [privateAddress];
  assert.ok(allowedAddresses.includes(url.href), 'Unexpected companion website address');
}

async function github(resource) {
  const response = await fetch(`https://api.github.com/repos/raindrop-ai/judgment-calls${resource}`, {
    headers: { Authorization: `Bearer ${process.env.GITHUB_TOKEN}`, Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' }
  });
  if (!response.ok) throw new Error(`Cannot verify Pages configuration (HTTP ${response.status}). Check repository Settings → Pages. No access settings have been changed.`);
  return response.json();
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  if (!process.env.GITHUB_TOKEN) throw new Error('GITHUB_TOKEN is required to verify access settings');
  const repository = await github('');
  const pages = await github('/pages');
  checkPrivacy(repository, pages);
  console.log(`Verified: internal repository, ${pages.public ? 'public' : 'private'} GitHub Pages, GitHub Actions build source.`);
}
