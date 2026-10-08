# CLAUDE.md — Curry09.github.io

Personal academic homepage built on the **acad-homepage** Jekyll template (minimal-mistakes based), deployed via GitHub Pages. The whole site is essentially one page: `_pages/about.md`.

## 🌏 This site is bilingual (English + 中文) — the #1 rule

The site has a **中 / EN** language switch (floating button, top-right). It works entirely client-side: every visible string exists **twice** — an English copy and a Chinese copy — and CSS shows only one at a time based on a class on `<html>` (`lang-en` / `lang-zh`).

> **RULE: Any change to visible content MUST be made in BOTH languages.**
> Never add, edit, or remove a piece of visible text in only one language. If you add a news item, a paper, an award, etc. in English, add the matching Chinese (and vice-versa). If you only have one language, ask the user for the other before committing — do not leave a half-translated page.

### How the bilingual markup works

**1. Inline text** (paragraphs, list items, headings) — wrap each language in a span:

```html
<span class="lang-en">English text here</span><span class="lang-zh">中文文本</span>
```

Keep the two spans **adjacent with no space between them** (a stray space shows up when switching). Markdown *inside* a span renders normally: `**bold**`, `[link](url)`, `*italic*` all work.

**2. Section headings** — keep the shared emoji outside the spans, and pin an explicit ID so nav anchors never break:

```markdown
# 🔥 <span class="lang-en">News</span><span class="lang-zh">最新动态</span> {#news}
```

The `{#news}` is required — `_data/navigation.yml` links to `/#news`, `/#internships`, `/#publications`, `/#honors-and-awards`, `/#education`. If you rename or add a section, keep the ID in sync with the nav file.

> ⚠️ **The ID must start with a letter, not a hyphen.** kramdown only consumes the `{#id}` attribute when the ID begins with a letter; an ID like `{#-news}` is left in the rendered page as literal text (and the heading never gets the ID, so the nav anchor breaks). Use `{#news}`, never `{#-news}`.

**3. Publications** — paper **titles and author lists stay English-only** (academic convention). Only the bullet descriptions under each paper are bilingual (wrap each bullet's text in the two spans). Badges, images, links, dates are shared (written once, no spans).

### Where each translatable surface lives

| Surface | File | How |
|---|---|---|
| Page body (intro, news, internships, publication blurbs, honors, education) | `_pages/about.md` | `.lang-en` / `.lang-zh` spans |
| Nav bar labels | `_data/navigation.yml` (`title` + `title_zh`) rendered by `_includes/masthead.html` | one entry per language |
| Sidebar name / bio / location | `_config.yml` author block: `name`+`name_zh`, `bio`+`bio_zh`, `location`+`location_zh` | rendered by `_includes/author-profile.html` |
| Sidebar blurb under avatar | `_config.yml`: `sidebar_blurb` + `sidebar_blurb_zh` | `description` stays English (used for SEO) |

### The switching machinery (rarely needs changing)

- CSS + pre-paint language script: `_includes/head/custom.html`
- Toggle button + click handler: `_includes/lang-toggle.html` (included from `_layouts/default.html`)
- Default language for first-time visitors: **English**. The choice is saved in `localStorage` under `site-lang`.

## Local preview

```bash
bundle exec jekyll serve   # then open http://localhost:4000
```

Click the **中 / EN** button and confirm BOTH languages look right before committing.

## Citation counts (Semantic Scholar)

Per-paper citation counts in the Publications list, plus a total + h-index line
under the heading, come from the **Semantic Scholar Graph API**. They render as
shields.io badges with the Semantic Scholar logo (`logo=semanticscholar`,
`-fff?logoColor=000`), matching the hand-written Paper/Code/Dataset badges.

> shields.io treats `-` and `_` as separators inside a `/badge/` path segment,
> so `s2Badge()` doubles them. An unescaped `h-index` renders a *"404 badge not
> found"* image, which is easy to miss.

| Piece | Where |
|---|---|
| Crawler (one API call, retries on 429) | `semantic_scholar_crawler/main.py` |
| Daily job, force-pushes to the `semantic-scholar-stats` branch | `.github/workflows/semantic_scholar_crawler.yaml` |
| Page-side fetch + DOM fill | `_includes/fetch_semantic_scholar_stats.html` (loaded via `_includes/scripts.html`) |
| Markers in the page | `_pages/about.md` — `#s2_total_cit_wrapper` and one `<span class='show_s2_citations' data='<arxiv-id>'>` per paper |

**Adding a paper:** put the usual `arxiv.org/abs/<id>` Paper badge on the badge
line and append `<span class='show_s2_citations' data='<id>'></span>`. Nothing
else to configure — the crawler scrapes the arXiv ids out of the Publications
section of `about.md`, so a paper that isn't on the Semantic Scholar author
profile (co-author disambiguation slips happen) still gets looked up directly.

Notes:
- The author id lives in the workflow (`SEMANTIC_SCHOLAR_AUTHOR_ID`, currently
  `2399060433`); override it with a repo variable of the same name. An optional
  `SEMANTIC_SCHOLAR_API_KEY` secret raises the rate limit but isn't needed.
- Every paper shows its own count, 0 included. If the branch is missing or the
  fetch fails the page just renders without citations — no broken text, no
  dangling `|`.
- Numbers lag reality: the job runs daily at 08:30 UTC and jsDelivr caches a
  branch path for up to ~12h. Run the workflow manually from the Actions tab to
  refresh sooner.
- The data is read through jsDelivr unless `citation_stats_use_cdn` in
  `_config.yml` is set to `false`; raw.githubusercontent.com is unreachable
  from mainland China, so the CDN is the default rather than the opt-in.
- Semantic Scholar is the **only** citation source. The upstream template's
  Google Scholar pipeline (`google_scholar_crawler`, its workflow, and
  `_includes/fetch_google_scholar_stats.html`) was removed deliberately — don't
  reintroduce it. `docs/README-zh.md` is upstream template documentation and
  still describes it. The Google Scholar *profile links* in `about.md` and the
  sidebar are unrelated and stay.
- Run the crawler locally with:
  `cd semantic_scholar_crawler && SEMANTIC_SCHOLAR_AUTHOR_ID=2399060433 python main.py`
