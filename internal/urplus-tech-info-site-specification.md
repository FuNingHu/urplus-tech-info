# UR+ Tech Info Site Specification

Status: internal reference. This file is Markdown. Keep it out of the Sphinx toctree and off GitHub Pages.

Audience: people who maintain this documentation site. Public readers do not see this file.

Public site: [https://funinghu.github.io/urplus-tech-info/](https://funinghu.github.io/urplus-tech-info/)

## 1. Purpose

UR+ Tech Info is the PolyScope X technical guide for UR+ partners. It explains how a product fits the Universal Robots platform: how to scope the work, what to deliver, how to test, how to maintain the product after launch, and how to implement specific URCap behavior.

SDK detail stays on the Universal Robots SDK documentation. This site keeps the process a partner needs and the practices that have been verified.

Public pages are in English. The copyright holder is Universal Robots A/S. The author line is UR Development Consultant Team.

## 2. Readers

Public readers are the hardware, software, and documentation people at a UR+ partner, and the UR Development Consultant who works with them.

Readers already know Universal Robots, URCap, and URScript. Pages do not define those terms. PolyScope 5 appears only where it differs from PolyScope X: a URCap built for PolyScope 5 does not run on PolyScope X, while URScript does.

## 3. Two kinds of content

Both kinds of article live on the same site. They use different navigation groups and a different style.

### 3.1 Process articles

Process articles state the requirements and deliverables of the partner program. Current pages:


| Group                 | Pages                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| General               | Key Updates for PolyScope X, Product Life Cycle Management                                                           |
| Development & Testing | Development Deliverables, Resources for Development, Technical Scoping, Testing Methodology, Self-Testing Checkpoint |
| About                 | Version History                                                                                                      |


A process article states requirements and who is responsible. One page answers what the partner does and what UR supports. SDK click-by-click steps stay out of these pages.

### 3.2 Practice articles

Practice articles describe a procedure verified on a specific PolyScope X SDK and URSim. Current pages sit at the end of Development & Testing:

- Overview - URCap Contributions
- Cursor AI-Assisted URCap Development
- USB Passthrough for URCap Backend on URSim
- Change a Smart Skill Title by URCap
- [Debugging Tool] Tool Modbus Driver
- Create Additional Program Node

A practice article names the SDK version and the URSim or PolyScope version used for verification. Reference code points to an SDK `/samples/` path when one exists. Otherwise it points to an example repository that the public can open. Screenshots live in `docs/source/images/`. Widths are in section 5.6.

When a debugging-tool article offers a URCapX download, the link targets that tool's releases page.

## 4. Information architecture

Sources live in `docs/source/`. One public article is one `.rst` file. `index.rst` has two lists, and a new article updates both:

1. The visible links in the page body.
2. The hidden `toctree`. The sidebar reads only the `toctree`.

Sidebar groups stay General, Development & Testing, and About. A new process article goes into the matching process group. A new practice article goes with the other practice articles in Development & Testing and gets a Version History row.

Cross-links use `:doc:`. A related practice sits at the end of the concept it belongs to.

## 5. Style

Public pages share one visual system. An article does not set its own body font, heading font, font size, or text color. Those come from the Read the Docs theme and from `docs/source/_static/custom.css`.

### 5.1 Voice

Write in clear technical English. Use short paragraphs. Address the reader as "you" in a procedure. A process article states the requirement and who is responsible. A practice article is a sequence the reader can follow.

Name the product, screen, file, and contribution type as they appear in PolyScope X or the SDK. Keep PolyScope 5 in the sentence that states the difference from PolyScope X.

A practice article opens with the environment it was checked on: SDK version, URSim or PolyScope version, and the date of the last check. Use a `note` admonition for that line when the rest of the page is a procedure.

### 5.2 Fonts

The theme loads these families. Do not replace them in an article.


| Use                                    | Font stack                                                                                |
| -------------------------------------- | ----------------------------------------------------------------------------------------- |
| Body text, sidebar, version menu       | Lato, Proxima Nova, Helvetica Neue, Arial, sans-serif                                     |
| Headings                               | Roboto Slab, ff-tisa-web-pro, Georgia, Arial, sans-serif                                  |
| Code, inline literals, terminal badges | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, Courier, monospace |


Lato and Roboto Slab are the theme's web fonts. The later names are the fallbacks when those fonts are unavailable.

### 5.3 Page chrome

- Theme: `sphinx_rtd_theme`.
- Logo and browser icon: `docs/source/images/urplus_logo.png`.
- Sidebar stays visible while the page scrolls. Navigation expands to four levels and does not collapse.
- The content column uses the width left beside the sidebar. `custom.css` sets `.wy-nav-content { max-width: none; }`.
- Each page shows an Edit on GitHub link. The version flyout stays at the bottom left of the sidebar.

### 5.4 Headings, lists, and tables

- The file title is a top-level heading. Sections under it use the next heading level. Keep the underline long enough for the title text.
- Use a numbered list for a sequence and a bullet list for items with no order.
- A table uses the normal Sphinx table. It stretches to the content width. Text inside a cell wraps. The first column is bold and about 18% of the table width. This rule is for the deliverable-style tables the stylesheet targets.

### 5.5 Code and terminals

Put commands and source in a `code-block` with the language that matches the text:


| Language     | When                                                |
| ------------ | --------------------------------------------------- |
| `urscript`   | URScript. The site lexer colors `if` and `end`.     |
| `bash`       | A Linux, WSL2, or container shell                   |
| `powershell` | Windows PowerShell                                  |
| `typescript` | A URCap frontend file                               |
| `json`       | `contribution.json`, i18n files, and other JSON     |
| `yaml`       | Compose and similar config                          |
| `text`       | Output, a path list, or a fragment with no language |


When a command runs in a specific terminal, put a badge on the line above the code block. The badge is a raw HTML span. The class is `term-badge` plus one of `term-wsl2`, `term-powershell`, `term-devcontainer`, or `term-ursim`. The badge is monospace, bold, and about 0.82 em, with a colored background from `custom.css`.

File names, paths, function names, and values the reader must replace go in inline literals, for example ``/samples/``.

### 5.6 Figures

Store screenshots in `docs/source/images/`. Give every image alt text.

Default figure width is 60% of the content column. Use 80% when the screenshot is a wide layout. Use 100% only for a diagram that becomes unreadable below full width, such as the project workflow. A small result crop may be 30%.

### 5.7 Admonitions

Use the standard Sphinx admonitions for a callout:

- `note` for the tested version, a scope reminder, or a related article.
- `warning` for a limit that causes the wrong result if ignored.
- `important` for a condition the reader checks before continuing.
- A named admonition, such as `Download` or `Notes`, for a block that needs its own label.

### 5.8 Links

A link that leaves this site opens in a new tab. Write it as raw HTML with `target="_blank"`. This covers SDK docs, GitHub, forms, release notes, and a URCapX releases page.

A link to another page on this site uses `:doc:` and opens in the same tab. The version menu also stays in the same tab and changes only the version.

## 6. Versions

The site has two version tracks. They identify different snapshots.

### 6.1 Documentation revision

`docs/source/version_history.rst` is the public revision log. Each row has a revision, a change description, a date, and an accountable person. `release` in `docs/source/conf.py` matches the latest row. The current revision is 1.12.0.

A reader-visible content change does all three of the following:

1. Add a row to Version History.
2. Set `release` in `conf.py` to that same revision.
3. Put an annotated tag on the commit that contains the content. The tag name is `v` plus the revision, for example `v1.12.0`.

Revisions 1.0.0 through 1.2.0 have no separate tag, because those updates share one commit. Revisions 1.10.0 and 1.11.0 are unused. Later content revisions continue upward from 1.12.0.

A change that only touches the build, the theme, or dependencies, and that readers cannot see, does not get a new revision or a new documentation tag.

### 6.2 Git branch and tags

`main` is the moving latest documentation. `v1.12.0` stays on the commit that was tagged. Later commits may land on `main` after that tag, so the bottom-left menu lists both `main` and `v1.12.0`.

The version menu uses one Versions list. `main` comes first. Tags follow, newest first. `main` is the current documentation. A tag is the documentation frozen at that tag.

The build includes the `main` branch and tags whose names match `v<major>.<minor>.<patch>`.

## 7. Publishing

A push to `main` makes GitHub Actions build `main` and every matching tag with sphinx-multiversion, then deploy the result to GitHub Pages. A tag push on its own does not start that build. After the tag is on GitHub, a build of `main` is what adds the tag to the menu.

A pull request runs one `sphinx-build` and does not deploy.

Published pages live in version directories:

- `https://funinghu.github.io/urplus-tech-info/` redirects to `main`.
- The current article is `/urplus-tech-info/main/<page>.html`.
- A frozen article is `/urplus-tech-info/v1.12.0/<page>.html`.
- An older article URL that omits `/main/` or a version directory returns 404.

If an older version has no equivalent article, the version menu opens that version's home page.

Local preview uses `make html` or `make.bat html` from the `docs` directory. After a title or `toctree` edit, clean the build before building again, or the sidebar keeps the old title. GitHub Actions always builds from a clean tree.

## 8. Build constraints

Dependencies are listed in `requirements.txt` at the repository root. Sphinx stays below 9. `sphinx-multiversion` 0.2.4 calls `Config.read()` with a positional argument, and Sphinx 9 rejects that call at the start of the build.

Public pages use Sphinx and the Read the Docs theme. The bottom-left version menu is that theme's version flyout. URScript has no built-in highlighter, so `conf.py` registers a small lexer that colors `if` and `end`.

Build output is `docs/build/` and stays uncommitted.

## 9. Material that stays unpublished

Keep the following in the repository or on a local machine. Leave it out of `docs/source/` and out of `index.rst`:

- This specification and other internal notes.
- Implementation details from private repositories, including license-key format and activation logic.
- SDK or product plans that are not cleared for publication.

## 10. Done criteria for a content release

A reader-visible update is released when all of the following are true:

1. The article is English reStructuredText, and it appears both in the visible list in `index.rst` and in the matching `toctree`.
2. A practice article names the SDK version and the URSim or PolyScope version used for verification.
3. The page uses the theme fonts, a `code-block` language from section 5.5, and figure widths from section 5.6. An external link opens in a new tab. An in-site link uses `:doc:`.
4. Version History has a new row, and `release` in `conf.py` matches that row.
5. The content commit has a `vX.Y.Z` tag, and that tag is on GitHub.
6. `main` is pushed and the Actions build succeeds.
7. The public `/main/` page opens, and the version menu lists the new tag.

