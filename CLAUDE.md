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
