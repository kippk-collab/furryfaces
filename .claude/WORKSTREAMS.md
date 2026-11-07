# WORKSTREAMS — MaryCarolWebsite

_Last updated: 2026-11-07_

Tracks the parallel threads of the furryfaces.net rebuild. See `STATUS.md` for
the single-session summary and the live URLs.

---

## 1. The rebuild itself — ✅ COMPLETE

Two full static builds, 10 pages each, generated from `content.py`.

Pages: `index`, `gallery`, `exhibitions`, `pricing`, `expectations`, `posing`,
`comments`, `bio`, `contact`, `pet-of-the-month`.

**Done:**
- Flash slideshow replaced with CSS/JS matching the original `flashvars` exactly
  (11 photos, same order, 3s delay, fade, loop, autoplay). The catalogue skin
  uses fade-out-then-in rather than a crossfade, because the plates differ in
  aspect ratio and a straight crossfade left one ghosting behind the other.
- `<frameset>` + nested `<iframe>` → ordinary pages with real URLs.
- 32 `gallery_NN-x.htm` pages → one deep-linkable gallery (`#slug`, arrow keys,
  thumbnail rail) in the faithful skin; a uniform plate grid + lightbox in the
  catalogue skin.
- All text-as-GIF replaced with real text (nav, page titles, 32 plate captions).
- Responsive at 390px: faithful collapses to a hamburger, catalogue to "CONTENTS".
- Assets re-encoded 9 MB → 2.3 MB, same pixels.

**Verified** (not assumed): both skins loaded in Chrome at desktop and 390px;
slideshow, lightbox, keyboard nav and deep links exercised; zero console errors;
a script checks every `src`/`href` in every page resolves — 0 missing.

**Do not:** hand-edit `site/*.html` or `site-bold/*.html`. They are build output.

---

## 2. Publishing — ✅ COMPLETE (two targets live)

| Target | URL | Mechanism |
|---|---|---|
| Hostinger (her account) | paleturquoise-jellyfish-432913.hostingersite.com | zip upload to `public_html` |
| GitHub Pages | kippk-collab.github.io/furryfaces/ | `gh-pages` branch |

Both verified from the outside with real HTTP checks (all pages, CSS, JS, sample
images → 200 over HTTPS; correct titles; noindex present).

**Hostinger Git deploy is a dead end** under collaborator access — the GIT tab
offers only GitHub/GitLab OAuth and the buttons are disabled. Revisiting it would
mean either Mary Carol connecting from her own login, or binding Kipp's GitHub
account into her hosting account permanently. Judged not worth it for a static
site that changes rarely; zip upload is the path.

**To update either target:** rebuild → regenerate `dist/furryfaces-review.zip`
from `gh-pages` → re-upload (Hostinger), and/or push `gh-pages` (Pages).

---

## 3. Her decision — ⏸ BLOCKED ON MARY CAROL

The only open thread. Kipp sends the neutral landing link; she picks A or B.

Guidance already given to Kipp: send the link **without commentary**, because
the fastest way to bias her is to explain Version B first.

Prediction on file: the catalogue version is the better-designed object, but it
argues "this is fine art." Her own copy is warmer than that (four cats, fluent
"catonese"). If she identifies as an exhibiting artist — and the exhibitions page
shows a decade of one-woman shows — it lands. If she thinks of herself as someone
who takes lovely pictures of your dog, the black version is closer to instinct.

---

## 4. Go-live tasks — ⏸ QUEUED behind #3

Once she chooses:

1. `PREVIEW_NOINDEX = False` in `content.py`, rebuild both/whichever, redeploy.
2. Point **furryfaces.net** at the chosen host.
3. **Fix SSL.** Currently self-signed → browsers flag "Not secure". GoDaddy
   hosting panel includes free SSL on most plans; then force HTTPS via
   `.htaccess`. This is independent of everything else and could be done now.
4. Decide whether the site stays on GoDaddy (where the domain is) or moves to
   her new Hostinger account (where the preview already lives). Moving means a
   DNS change + a fresh certificate, not a migration — the files are in place.

---

## 5. Photo resolution — ⏸ NEEDS AN ASK

Biggest available quality win, costs no code.

Request to make of her: *"the original scans or camera files, biggest versions,
straight off the drive, unresized."* Not 2000px — ask for the maximum, we
downsize. Warn: don't crop, don't edit, **don't email them** (AOL/Apple Mail
shrink attachments silently); Dropbox or Drive.

On arrival: drop into `legacy/images/gallery_big/`, re-run `build_assets.py`.
Then optionally add `srcset` generation (480/960/1920) — offered, not yet built.

Realistic expectation: she may only have the 400px exports. Nothing breaks if so,
which is exactly why the catalogue skin caps display at native size.

---

## 6. Content freshness — 💤 DORMANT, worth raising

Exhibitions end in 2008. "Pet of the Month" has been Cleo & Bailey for ~18 years.
Preserved verbatim per the brief ("keep everything the same"), but she may want
to update them. Not Kipp's call to make unilaterally.

---

## Housekeeping notes for a future session

- `~/Dev/MaryCarolWebsite` has **no top-level `CLAUDE.md`** and **no vault
  strategy file**. `/save` reported this; run "update the vault" to establish one
  and wire the `Vault strategy file:` pointer if this project continues.
- Audio chimes were already configured (`02_descending_zip_whistle.1.aif` /
  `03_bubbly_pluck_loop.1.aif`) and are in `~/.claude/sound-map.md`.
- Side effect of this session: **`LyricEngine` was flipped from public to
  private** on GitHub at Kipp's request after a visibility audit. Zero forks,
  stars, watchers or Pages, so nothing broke. An offer to audit its git history
  for leaked secrets was made and **not yet taken up** — worth revisiting in that
  project.
