# Furry Faces — furryfaces.net

A rebuild of Mary Carol Stunkel's pet-portrait site. The original (Dreamweaver,
c. 2007, last touched Sept 2015) used a `<frameset>`, an `<iframe>` inside it, and
one Flash object for the homepage slideshow. Flash has been dead since 2020, so
the slideshow showed nothing on any current browser.

Same look, same words, same photographs — no plugins, works on phones.

## Two versions

| | |
|---|---|
| `site/` | **Faithful.** Her existing look — black surround, charcoal panel — modernised and made responsive. Safe choice. |
| `site-bold/` | **Catalogue.** A reskin: warm paper, Bodoni display type, photographs presented as numbered plates in mats. Same words, same photos. |

Both read their copy from `content.py`, so text is edited once and both rebuild.

Preview them side by side:

```sh
(cd site      && python3 -m http.server 8765 &)   # → localhost:8765
(cd site-bold && python3 -m http.server 8766 &)   # → localhost:8766
```

The catalogue skin deliberately never enlarges a photograph past its native
size. That constraint is what makes 430px scans read as plates in a monograph
rather than as low-resolution web images — it turns the limitation into the
design.

## Layout

```
content.py       ← all of Mary Carol's words, shared by both builders
site/            ← faithful version (this is what gets uploaded to the server)
  *.html         ← 10 pages, plain static HTML
  assets/css/    ← one stylesheet
  assets/js/     ← site.js (behaviour) + data.js (gallery contents)
  assets/img/    ← all photographs, re-encoded
site-bold/       ← catalogue version
legacy/          ← byte-for-byte copy of the old site, for reference
build_assets.py  ← regenerates assets/img from legacy/ (already run)
build_pages.py   ← regenerates site/*.html
build_bold.py    ← regenerates site-bold/*.html
```

## What changed, and why

| Old | New |
|---|---|
| Flash slideshow (`slideshow.htm.swf`) | CSS/JS slideshow — same 11 photos, same order, same 3-second fade |
| `<frameset>` + nested `<iframe>` | Ordinary pages. Every page has its own URL and works with the back button |
| 32 separate `gallery_NN-x.htm` pages | One gallery page; each photo deep-links, e.g. `gallery.html#oldfaithfulyankee` |
| Nav and photo titles were GIF **images of text** | Real text — readable by Google and by screen readers |
| Fixed 865px tables | Responsive; readable on a phone |
| ~9 MB of assets | ~2.3 MB, identical pixels, just encoded properly |
| `mailto:` only | `mailto:` plus a tappable phone link |

The 32 photo titles and breed captions ("Magic a la Mondrian — Magic, the
Appaloosa") only ever existed inside GIFs. They were transcribed and are now
real text. Mary Carol's original spellings were kept as she wrote them.

## Editing content

Text lives in `content.py`. Edit it there, then rebuild whichever versions you
are still using:

```sh
python3 build_pages.py   # site/
python3 build_bold.py    # site-bold/
```

To preview locally:

```sh
cd site && python3 -m http.server 8765
# then open http://localhost:8765
```

## Deploying

Upload the **contents of `site/`** to the web root on GoDaddy hosting
(cPanel → File Manager, or FTP). It's static — nothing needs to run server-side.

Keep the old files around until the new ones are confirmed working.

## Known issues / not yet done

1. **No SSL certificate.** `https://furryfaces.net` currently serves a
   self-signed certificate, so browsers warn on it and Chrome marks the site
   "Not secure." Fix in the GoDaddy hosting panel (free SSL is included with
   most plans), then force HTTPS with an `.htaccess` redirect.
2. **The source photographs are small.** The largest is 600px wide; most are
   ~430px. They were sized for 2007 monitors and look soft on a modern screen.
   If Mary Carol still has the originals, re-exporting them at 1600px would make
   the gallery dramatically better. Nothing else needs to change — drop them in
   `legacy/images/gallery_big/` and re-run `build_assets.py`.
3. **Content is stale.** The exhibitions list stops in 2008 and "Pet of the
   Month" has been Cleo & Bailey for about eighteen years. Worth asking her.
