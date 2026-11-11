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

The Actions workflow builds and tests pull requests. It deploys updates to `main` only when both of these settings are verified:

- The repository visibility is **Internal**.
- The Pages website visibility is **Private**, with **GitHub Actions** selected as its build source.

A repository administrator configures these in [Settings → Pages](https://github.com/raindrop-ai/judgment-calls/settings/pages). Private Pages requires GitHub Enterprise Cloud. It restricts the website to people with read access to this repository; an internal repository alone does not restrict a public Pages website. Use the private address shown in Settings after configuration.

The workflow never enables Pages automatically or changes visibility. Missing settings or an inability to verify them stops deployment. To publish publicly later, deliberately update the deployment check and Pages visibility after publication is approved.

[GitHub’s documentation on private Pages](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site) · [Companion README](../README.md)
