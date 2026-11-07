# STATUS — MaryCarolWebsite (furryfaces.net)

_Last updated: 2026-11-07_

## What this project is

A from-scratch rebuild of **furryfaces.net**, the pet-portrait site of **Mary Carol
Stunkel** (`mcstunkel@aol.com`) — a friend of Kipp's and his screenwriting reader.
She trades script notes with him; this rebuild is a favor, not a paid job.

The original site: Dreamweaver, c. 2007, last modified Sept 2015. A `<frameset>`
wrapping an `<iframe>`, with the homepage slideshow built on **Adobe Flash**
(`slideshow.htm.swf`, Dreamweaver's ImageViewer.swc component). Flash has been
dead since 2020, so the slideshow had been rendering nothing for years.

Kipp has **GoDaddy delegate access** to her account (domain + hosting live there),
and **Hostinger collaborator access** to a separate account she created later.

## Current state: DONE and PUBLISHED, awaiting her verdict

Two complete rebuilds exist. Both are live and were verified from the outside.

**Live for her review (send this one link):**
https://paleturquoise-jellyfish-432913.hostingersite.com/

- Version A (faithful): …/faithful/
- Version B (catalogue): …/catalogue/

**Also live on GitHub Pages** (same content, published first):
https://kippk-collab.github.io/furryfaces/

**Repo:** https://github.com/kippk-collab/furryfaces — **PUBLIC** (Kipp approved
this explicitly for these two review sites; every other repo on the account is
private). `main` = source + build scripts. `gh-pages` = only what gets served.

## The two versions

| | |
|---|---|
| `site/` → "faithful" | Her existing look — black surround, `#333439` charcoal panel, white bold-italic display type — modernised, responsive, no frames, real text. Archivo + Spectral. |
| `site-bold/` → "catalogue" | A reskin as an exhibition catalogue: warm paper `#f2ede3`, Bodoni Moda display, oxblood accent, photographs as numbered plates in mats, paper grain, drop caps, click-to-enlarge lightbox. |

**The load-bearing design constraint:** the catalogue skin **never upscales a
photograph past its native size**. Her source images are tiny (see below), and
that single rule is what makes them read as plates in a monograph instead of as
low-resolution web images. Do not "fix" this by making images fill the viewport.

## Facts worth not re-deriving

- **Her photos are minuscule.** Gallery: 290×277 → 600×400, longest edge never
  exceeds **600px**, most capped at 400px in one dimension (a 2007 batch-export
  setting). Slideshow: ≤443px. Pet of the Month: ≤455px. Posing: ~250px.
- **Re-encoding alone took assets from 9 MB → 2.3 MB with identical pixels.** The
  2007 JPEG encoder was simply bad (290 KB for a 600×400).
- **The 32 gallery titles only ever existed as GIF images of text.** They were
  transcribed by hand from the GIFs (rendered to a contact sheet and read) and are
  now real text, e.g. "Is it me or are they making sofas smaller? — Goliath, the
  Great Dane". **Her original spellings/typos are deliberately preserved**
  (Rotweiller, Retreiver, Malanois, Oy Vei). Do not correct them.
- The nav was sliced GIFs too, so until this rebuild the site had **no
  machine-readable text at all**.
- Contact is a `mailto:` only — no form. Phone: (732) 922-3216.
- **furryfaces.net still has no valid SSL.** Port 443 answers with a *self-signed*
  certificate. That is a GoDaddy hosting-panel fix (free SSL + `.htaccess`
  redirect), not a code fix. Unresolved.
- The GoDaddy delegate-access email was never found in `kippkoenig@gmail.com` — it
  went to `scriptscribe@gmail.com`. Moot now; he's already in.

## Architecture

```
content.py       ← ALL her words, single source of truth, shared by both builders
site/            ← faithful build output
site-bold/       ← catalogue build output
legacy/          ← byte-for-byte wget mirror of the 2007 site (reference)
dist/            ← upload zip (gitignored)
build_assets.py  ← legacy/ images → slugified, re-encoded, thumbs + data.json
build_pages.py   ← content.py → site/*.html
build_bold.py    ← content.py → site-bold/*.html
```

Pages are **generated**, not hand-edited. Edit `content.py`, re-run the builders.
Editing `site/*.html` directly will be overwritten on the next build.

`PREVIEW_NOINDEX = True` in `content.py` puts `<meta name="robots"
content="noindex, nofollow">` on every page of both builds plus a disallow-all
`robots.txt`. **Flip to False and rebuild for a real launch** or the live site
will be invisible to Google.

Note: Hostinger **overrides** the uploaded `robots.txt` on `.hostingersite.com`
preview domains, serving its own (blocks Googlebot, allows everything else). The
per-page meta tag still applies and is the stronger signal.

## Deploy

**Hostinger (hers)** — the GIT tab offers only GitHub/GitLab **OAuth**, and the
buttons are greyed out under collaborator access. So deployment is a zip upload:

1. `zip` built from the `gh-pages` branch → `dist/furryfaces-review.zip`
2. hPanel → Files → File Manager → `public_html` → Upload → Extract
3. The Extract dialog **requires a folder name** (blank is rejected), so extract
   into `tmp/` then move the four items up to `public_html` root and delete `tmp/`.

**GitHub Pages** — `gh-pages` branch, served at root. Push to redeploy.

## What's next (nothing is blocked on code)

1. **Kipp sends Mary Carol the landing link.** Deliberately neutral — "Version A"
   and "Version B", no steer. Her unprompted reaction is the useful signal.
2. She picks one. Then: flip `PREVIEW_NOINDEX`, rebuild, deploy, point
   furryfaces.net at it, fix SSL.
3. **Ask her for the original high-res photos.** Biggest available win. The 400px
   cap is so uniform it's clearly an export setting, so originals likely exist.
   Drop into `legacy/images/gallery_big/`, re-run `build_assets.py`. Recommended
   target: **2000px long edge, JPEG q85** (lightbox at 2× retina is the binding
   constraint). Tell her not to resize or crop — and **not to email them** (AOL
   and Apple Mail silently shrink attachments); use Dropbox/Drive.
4. **Offered but not built:** responsive `srcset` (480/960/1920) in
   `build_assets.py`, ready to add the moment bigger photos arrive.
5. **Her content is stale** — exhibitions list stops in 2008, Pet of the Month has
   been the same two Basset Hounds for ~18 years. Worth raising with her.

## Decisions made

- **Faithful first, reskin second.** Kipp chose "same look, modern + responsive"
  when asked; the catalogue version was built afterward as a speculative trial
  he explicitly asked for, on the existing small photos.
- **Both versions kept.** Neither is thrown away until she chooses.
- **Landing page is neutral on purpose.** No recommendation shown to her.
- **Public repo accepted** for these two sites only, after Kipp confirmed.
- Serif body copy (Spectral) in the faithful version instead of the original's
  small Arial — flagged to Kipp as a judgment call, he didn't object.
