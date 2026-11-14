import { readFile, writeFile, mkdir, rm, lstat, realpath } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { Marked } from 'marked';

export const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const repository = 'https://github.com/raindrop-ai/choosing-decision-models';
export const escape = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#39;');
export const htmlPath = file => file.endsWith('/README.md') ? file.slice(0, -9) + 'index.html' : file === 'README.md' ? 'index.html' : file.replace(/\.md$/, '.html');
export const slug = text => text.toLowerCase().replace(/<[^>]*>/g, '').replace(/[^\p{L}\p{N}\s-]/gu, '').trim().replace(/\s+/g, '-');

export function resolveLink(href, current, inventory, image = false) {
  if (!href || /[\u0000-\u001f\u007f\\]/.test(href)) return null;
  if (href.startsWith('#')) return image ? null : href;
  if (/^[a-z][a-z\d+.-]*:/i.test(href)) {
    return !image && /^(https?:|mailto:)/i.test(href) ? href : null;
  }
  if (href.startsWith('//') || href.startsWith('/')) return null;
  const match = href.match(/^([^?#]*)(.*)$/);
  let name;
  try { name = path.posix.normalize(path.posix.join(path.posix.dirname(current), decodeURIComponent(match[1]))); }
  catch { return null; }
  if (!inventory.has(name) && inventory.has(`${name}/README.md`)) name += '/README.md';
  if (!inventory.has(name) || name.startsWith('../')) return null;
  const suffix = match[2];
  const relative = target => path.posix.relative(path.posix.dirname(htmlPath(current)), target);
  if (name.endsWith('.md')) return image ? null : relative(htmlPath(name)) + suffix;
  if (/\.(jpg|jpeg|png|webp|gif)$/i.test(name)) return relative(name) + suffix;
  if (image) return null;
  const encoded = name.split('/').map(encodeURIComponent).join('/');
  return `${repository}/blob/main/${encoded}${suffix}`;
}

export function renderMarkdown(source, current, inventory) {
  const navigationTitle = navigationTitles.get(current);
  const originalTitle = (source.match(/^# (.+)$/m) || [])[1];
  const engine = new Marked({ gfm: true });
  engine.use({ renderer: {
    html({ text }) {
      // Dataset passages are untrusted. Preserve only the disclosure tags used by our Markdown.
      return text.split(/(<[^>]*>)/).map(part => {
        if (!part.startsWith('<')) return escape(part);
        return /^<\/?(?:details|summary)\s*>$|^<br\s*\/?>$/i.test(part) ? part : escape(part);
      }).join('');
    },
    link(token) {
      const href = resolveLink(token.href, current, inventory);
      const text = this.parser.parseInline(token.tokens);
      return href ? `<a href="${escape(href)}">${text}</a>` : text;
    },
    image(token) {
      const href = resolveLink(token.href, current, inventory, true);
      return href ? `<img src="${escape(href)}" alt="${escape(token.text)}" loading="lazy">` : escape(token.text);
    },
    heading(token) {
      const id = slug(token.text);
      const originalId = originalTitle ? slug(originalTitle) : '';
      const alias = token.depth === 1 && navigationTitle && originalId && originalId !== id ? `<span id="${escape(originalId)}" aria-hidden="true"></span>` : '';
      return `<h${token.depth} id="${escape(id)}">${alias}${this.parser.parseInline(token.tokens)}</h${token.depth}>\n`;
    }
  }});
  // The website supplies its own logo in the header. GitHub retains the README's image.
  if (current === 'README.md') {
    source = source.replace(/^<a href="https:\/\/www\.raindrop\.ai\/">[\s\S]*?<\/a>\s*/, '');
  }
  if (navigationTitle) source = source.replace(/^# .+$/m, `# ${navigationTitle}`);
  return engine.parse(source);
}

export const sections = [
  ['Explore', [['Overview','README.md'],['Questions','questions/README.md'],['Question variants','variants/README.md'],['Binary subset','questions/binary-subset.md']]],
  ['Findings', [['Baseline results','docs/results.md'],['Context changes','docs/variant-results.md']]],
  ['Understand', [['Methods','docs/methods.md'],['How variants were made','docs/variant-methods.md'],['Source terms','docs/data-sharing.md']]],
  ['Reproduce', [['Baseline experiment','docs/reproduction.md'],['Variant experiment','docs/variant-reproduction.md'],['Connect a model','docs/connecting-models.md'],['Recover question texts','docs/recovering-inputs.md']]],
  ['About', [['Licenses','licenses/README.md'],['Contribute & contact','CONTRIBUTING.md']]]
];
const navigationTitles = new Map(sections.flatMap(([, items]) => items.map(([title, file]) => [file, title])));
const pageTitle = (source, file) => navigationTitles.get(file) ?? (source.match(/^# (.+)$/m) || [])[1] ?? file;

function document(source, current, inventory) {
  const rel = target => path.posix.relative(path.posix.dirname(htmlPath(current)), target);
  const title = pageTitle(source, current);
  const nav = sections.map(([label, items]) => `<div class="nav-section"><span>${label}</span>${items.map(([text,file]) => `<a ${file === current ? 'aria-current="page" ' : ''}href="${escape(rel(htmlPath(file)))}">${text}</a>`).join('')}</div>`).join('');
  const github = `${repository}/blob/main/${current.split('/').map(encodeURIComponent).join('/')}`;
  const contents = [...source.matchAll(/^## (.+)$/gm)].map(([,text]) => `<a href="#${escape(slug(text))}">${escape(text)}</a>`).join('');
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'none'">
<meta name="robots" content="noindex,nofollow"><meta name="color-scheme" content="light dark"><title>${escape(title)} · Raindrop research</title>
<link rel="icon" href="${rel('docs/assets/raindrop-logo.jpg')}"><link rel="stylesheet" href="${rel('site-assets/styles.css')}"><script defer src="${rel('site-assets/client.js')}"></script></head>
<body data-search="${rel('site-assets/search.json')}" data-home="${rel('index.html')}"><a class="skip" href="#content">Skip to content</a>
<header><a class="brand" href="${rel('index.html')}"><img src="${rel('docs/assets/raindrop-logo.jpg')}" width="38" height="38" alt="Raindrop"><span>Deciding between decision models</span></a><button id="search-open" type="button">Search questions & docs <kbd>/</kbd></button><a class="github" href="${repository}">GitHub ↗</a><button id="nav-toggle" type="button" aria-expanded="false" aria-controls="navigation">Menu</button></header>
<div class="layout"><nav id="navigation" aria-label="Companion">${nav}</nav><main id="content"><div class="page-tools"><a href="${github}">View on GitHub ↗</a></div><article>${renderMarkdown(source,current,inventory)}</article><footer><a href="https://www.raindrop.ai/">Raindrop</a> · <a href="${rel('CONTRIBUTING.html')}">Questions or corrections?</a></footer></main><aside aria-label="On this page">${contents ? '<span>On this page</span>' + contents : ''}</aside></div>
<dialog id="search-dialog"><div class="search-top"><label for="search-input">Search the companion</label><button id="search-close" type="button" aria-label="Close search">×</button></div><input id="search-input" type="search" placeholder="Try gift exchange, recall, or a question ID" autocomplete="off"><p id="search-status" role="status">Type to search questions, variants and documentation.</p><ol id="search-results"></ol></dialog></body></html>`;
}

export async function build() {
  const output = path.join(root, 'site/output');
  const inventory = JSON.parse(await readFile(path.join(root,'MANIFEST.json'),'utf8')).sha256;
  const files = new Set(Object.keys(inventory));
  // Verify every source before publishing. Only this inventory is eligible for rendering/copying.
  for (const file of files) {
    if (path.posix.normalize(file) !== file || file.startsWith('/') || file.split('/').some(part => ['..','.git','.local','node_modules'].includes(part))) throw new Error(`Unsafe inventory path: ${file}`);
    const sourcePath = path.join(root, file);
    const actual = await realpath(sourcePath);
    if (!actual.startsWith(root + path.sep)) throw new Error(`Inventory path escapes repository: ${file}`);
    const stat = await lstat(sourcePath);
    if (!stat.isFile() || stat.isSymbolicLink()) throw new Error(`Non-file inventory entry: ${file}`);
    const bytes = await readFile(sourcePath);
    if (createHash('sha256').update(bytes).digest('hex') !== inventory[file]) throw new Error(`Inventory mismatch: ${file}. Update MANIFEST.json before building.`);
  }
  await rm(output,{recursive:true,force:true});
  await mkdir(path.join(output,'site-assets'),{recursive:true});
  const search = []; let count = 0, size = 0;
  for (const file of files) {
    if (!file.endsWith('.md')) continue;
    const source = await readFile(path.join(root,file),'utf8');
    const html = document(source,file,files);
    const target = path.join(output,htmlPath(file));
    await mkdir(path.dirname(target),{recursive:true});
    await writeFile(target,html);
    size += Buffer.byteLength(html); count++;
    const title = pageTitle(source, file);
    const snippet = source.match(/## (?:Context|Question)\n([\s\S]*?)(?=\n## |$)/)?.[1] || source;
    search.push({title, path:htmlPath(file), excerpt:snippet.replace(/^#.*$/gm,'').replace(/<[^>]*>/g,'').replace(/[\[\]>*`]/g,'').replace(/\s+/g,' ').trim().slice(0,450)});
  }
  for (const file of files) {
    if (!file.startsWith('docs/assets/') || !/\.(jpg|png|webp|gif)$/i.test(file)) continue;
    await mkdir(path.dirname(path.join(output,file)),{recursive:true});
    await writeFile(path.join(output,file),await readFile(path.join(root,file)));
  }
  for (const file of ['styles.css','client.js']) await writeFile(path.join(output,'site-assets',file),await readFile(path.join(root,'site',file)));
  await writeFile(path.join(output,'site-assets/search.json'),JSON.stringify(search));
  await writeFile(path.join(output,'.nojekyll'),'');
  await writeFile(path.join(output,'robots.txt'),'User-agent: *\nDisallow: /\n');
  console.log(`Built ${count.toLocaleString()} pages (${Math.round(size/1024/1024)} MiB HTML). Output: site/output`);
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) await build();
