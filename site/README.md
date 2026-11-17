# Companion website

The website renders this repository’s Markdown pages with persistent navigation, search and light/dark themes. Question pages, variants and methods remain ordinary Markdown files, so editing them updates both GitHub and the website.

## Preview on your computer

Install [Node.js 22 or later](https://nodejs.org/en/download) and Python 3, then run these commands from the repository root:

```bash
npm ci --prefix site --ignore-scripts
npm test --prefix site
npm run build --prefix site
python3 -m http.server 3003 --bind 127.0.0.1 --directory site/output
```

Open <http://127.0.0.1:3003/>. Stop the server with Ctrl+C. The build checks source hashes against `MANIFEST.json`, renders the included Markdown pages and copies the bundled logo. Dataset downloads, model setup and fresh inference are not needed. Code and data links open their corresponding files on GitHub.

## GitHub Pages

The Actions workflow builds and tests pull requests and deploys updates to `main`. It accepts an **Internal** repository before launch or a **Public** repository after launch, verifies that GitHub reports the website’s visibility, and requires **GitHub Actions** as the Pages build source. It accepts the companion’s private address or its public address, <https://raindrop-ai.github.io/choosing-decision-models/>. The workflow does not change repository visibility; an administrator makes the repository public at launch.

Website access is separate from repository access. A **Public** Pages website can be read without a GitHub account while the repository stays internal. Code and download links on GitHub still require repository access. A **Private** website is restricted to people with read access to the repository.

A repository administrator changes website visibility in [Settings → Pages](https://github.com/raindrop-ai/choosing-decision-models/settings/pages). The workflow never changes access settings. After changing visibility, use the website address shown in Settings; the public address can differ from the private one.

[GitHub’s documentation on Pages visibility](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site) · [Companion README](../README.md)
