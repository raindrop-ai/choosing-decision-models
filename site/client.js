const navButton = document.querySelector('#nav-toggle');
const nav = document.querySelector('#navigation');
navButton.addEventListener('click', () => {
  const open = navButton.getAttribute('aria-expanded') !== 'true';
  navButton.setAttribute('aria-expanded', String(open));
  nav.toggleAttribute('data-open', open);
});
const dialog = document.querySelector('#search-dialog');
const input = document.querySelector('#search-input');
const status = document.querySelector('#search-status');
const results = document.querySelector('#search-results');
const home = new URL(document.body.dataset.home, location.href);
let index, loading, revision = 0;
async function openSearch() {
  dialog.showModal(); input.focus();
  if (!loading) loading = fetch(new URL(document.body.dataset.search, location.href)).then(response => {
    if (!response.ok) throw new Error('Search index unavailable'); return response.json();
  }).then(data => { index = data; }).catch(() => { status.textContent = 'Search is unavailable. Use the navigation to browse.'; loading = null; });
  await loading; if (input.value) await search();
}
document.querySelector('#search-open').addEventListener('click', openSearch);
document.querySelector('#search-close').addEventListener('click', () => dialog.close());
document.addEventListener('keydown', event => {
  if ((event.key === '/' || ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k')) && !['INPUT','TEXTAREA'].includes(document.activeElement?.tagName)) {
    event.preventDefault(); if (!dialog.open) openSearch();
  }
});
async function search() {
  const request = ++revision;
  await loading;
  if (request !== revision || !index) return;
  const words = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
  results.replaceChildren();
  if (!words.length) { status.textContent = 'Type to search questions, variants and documentation.'; return; }
  const matches = index.map(entry => {
    const title = entry.title.toLowerCase(), route = entry.path.toLowerCase(), excerpt = entry.excerpt.toLowerCase();
    if (!words.every(word => title.includes(word) || route.includes(word) || excerpt.includes(word))) return null;
    return { entry, score:words.reduce((n,word) => n + (title.includes(word) ? 8 : 0) + (route.includes(word) ? 4 : 0),0) + (entry.path.startsWith('docs/') ? 2 : 0) };
  }).filter(Boolean).sort((a,b) => b.score - a.score);
  status.textContent = matches.length ? `${matches.length.toLocaleString()} matches${matches.length > 40 ? ' · showing the first 40' : ''}` : 'No matches. Try fewer words or a question ID.';
  for (const {entry} of matches.slice(0,40)) {
    const li = document.createElement('li'), a = document.createElement('a'), title = document.createElement('strong'), excerpt = document.createElement('small');
    a.href = new URL(entry.path, home).href; title.textContent = entry.title; excerpt.textContent = entry.excerpt;
    a.append(title,excerpt); li.append(a); results.append(li);
  }
}
input.addEventListener('input', search);
