#!/usr/bin/env python3
"""Generate the static pages for site/.

Every page shares the same masthead, nav and footer, so they're assembled here
rather than copy-pasted nine times. Edit the content below and re-run:

    python3 build_pages.py

Output is plain static HTML — nothing on the server needs to run it.
"""

import json
import os

import content
from content import EMAIL, NAV, PHONE, PHONE_HREF

OUT = "site"

PAW = (
    '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<ellipse cx="7" cy="8" rx="2.1" ry="2.8"/><ellipse cx="12" cy="6.2" rx="2.1" ry="2.9"/>'
    '<ellipse cx="17" cy="8" rx="2.1" ry="2.8"/><ellipse cx="20.2" cy="12.6" rx="1.8" ry="2.3"/>'
    '<path d="M12 11.2c3.1 0 5.6 2.4 5.6 5.1 0 2-1.6 3.2-3.6 3.2-1 0-1.4-.3-2-.3s-1 .3-2 .3'
    'c-2 0-3.6-1.2-3.6-3.2 0-2.7 2.5-5.1 5.6-5.1Z"/></svg>'
)


def nav(active):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        links.append(f'          <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(links)


def shell(active, title, description, body, extra_head="", extra_scripts=""):
    """Wrap page body in the shared chrome."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="Mary Carol Stunkel">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/site/banner.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..700;1,400..700&family=Spectral:ital,wght@0,400;0,600;1,400;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
{extra_head}</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="masthead">
  <a href="index.html">
    <img class="masthead__banner" src="assets/img/site/banner.jpg" width="850" height="108"
         alt="Furry Faces — classic animal portraits by Mary Carol Stunkel">
  </a>
</header>

<nav class="nav" aria-label="Main">
  <div class="nav__inner">
    <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-list">
      <span class="nav__toggle-bars" aria-hidden="true"></span> menu
    </button>
    <ul class="nav__list" id="nav-list">
{nav(active)}
    </ul>
  </div>
</nav>

<main class="shell" id="main">
{body}
</main>

<footer class="footer">
  <div class="footer__inner">
    <div>Furry Faces &middot; MC Squared Productions &middot; Neptune, New Jersey</div>
    <div>
      <a href="mailto:{EMAIL}">{EMAIL}</a> &middot;
      <a href="tel:{PHONE_HREF}">{PHONE}</a>
    </div>
    <div><a href="pet-of-the-month.html">Pet of the Month</a> &middot;
      Photographs &copy; Mary Carol Stunkel. All rights reserved.</div>
  </div>
</footer>

{extra_scripts}<script src="assets/js/site.js"></script>
</body>
</html>
"""


def panel(title, inner, title_visible=True):
    heading = f'    <h1 class="page-title">{title}</h1>\n' if title_visible else \
              f'    <h1 class="visually-hidden">{title}</h1>\n'
    return f'  <div class="panel">\n{heading}{inner}\n  </div>'


# ---------------------------------------------------------------- home

def home_page(data):
    slides = []
    for i, s in enumerate(data["slides"]):
        active = " is-active" if i == 0 else ""
        loading = "" if i == 0 else ' loading="lazy"'
        slides.append(
            f'        <img class="slideshow__slide{active}" src="assets/img/slideshow/{s["slug"]}.jpg"'
            f' width="{s["w"]}" height="{s["h"]}" alt="{s["alt"]}"{loading}>'
        )
    dots = "\n".join(
        f'          <button class="slideshow__dot{" is-active" if i == 0 else ""}" type="button"'
        f' aria-label="Show photograph {i + 1}"></button>'
        for i in range(len(data["slides"]))
    )
    body = f"""  <div class="panel">
    <h1 class="visually-hidden">Furry Faces — classic animal portraits by Mary Carol Stunkel</h1>
    <div class="home">
      <div class="slideshow" data-slideshow>
{chr(10).join(slides)}
        <div class="slideshow__controls">
          <button class="slideshow__btn" type="button" data-slideshow-prev aria-label="Previous photograph">&#8249;</button>
          <div class="slideshow__dots">
{dots}
          </div>
          <button class="slideshow__btn" type="button" data-slideshow-next aria-label="Next photograph">&#8250;</button>
          <button class="slideshow__btn" type="button" data-slideshow-play aria-label="Pause slideshow">&#10074;&#10074;</button>
        </div>
      </div>
      <div class="home__aside">
        <img class="home__logo" src="assets/img/site/images-by-mcs.gif" width="322" height="197"
             alt="Images by Mary Carol Stunkel">
        <p class="home__tag">Classic animal portraits, captured in your home.</p>
        <a class="home__cta" href="gallery.html">See the photo gallery</a>
        <br>
        <a class="pet-badge" href="pet-of-the-month.html">{PAW} Pet of<br>the Month</a>
      </div>
    </div>
  </div>"""
    return shell(
        "index.html",
        "Furry Faces — Classic Animal Portraits by Mary Carol Stunkel",
        "Fine-art pet portraits photographed in your own home by Mary Carol Stunkel "
        "of MC Squared Productions, Neptune, New Jersey.",
        body,
    )


# ------------------------------------------------------------- gallery

def gallery_page(data):
    items = data["gallery"]
    thumbs = "\n".join(
        f'        <button class="gallery__thumb" type="button" data-gallery-thumb'
        f' aria-current="{"true" if i == 0 else "false"}">'
        f'<img src="assets/img/gallery/thumbs/{it["slug"]}.jpg" width="178" height="130"'
        f' alt="{it["title"]}" loading="lazy"></button>'
        for i, it in enumerate(items)
    )
    first = items[0]
    body = f"""  <div class="panel">
    <h1 class="page-title">Photo Gallery</h1>
    <div class="gallery" data-gallery>
      <div class="gallery__rail" role="group" aria-label="Choose a photograph">
{thumbs}
      </div>

      <div class="gallery__stage">
        <figure class="gallery__figure">
          <img class="gallery__image" data-gallery-image
               src="assets/img/gallery/{first['slug']}.jpg"
               width="{first['w']}" height="{first['h']}"
               alt="{first['title']} — {first['subject']}">
        </figure>
      </div>

      <div class="gallery__meta">
        <h2 class="gallery__title" data-gallery-title>{first['title']}</h2>
        <p class="gallery__subject" data-gallery-subject>{first['subject']}</p>
        <div class="gallery__nav">
          <button class="gallery__arrow" type="button" data-gallery-prev aria-label="Previous photograph">&#8249;</button>
          <button class="gallery__arrow" type="button" data-gallery-next aria-label="Next photograph">&#8250;</button>
          <span class="gallery__count" data-gallery-count>1 of {len(items)}</span>
        </div>
      </div>
    </div>

    <p class="gallery__note">
      Unframed matted copies of every photograph on this site are available for purchase.
      <a href="mailto:{EMAIL}">Email Mary Carol</a> or call {PHONE} for a price list.
    </p>
  </div>"""
    return shell(
        "gallery.html",
        "Photo Gallery — Furry Faces",
        "Thirty-two animal portraits by Mary Carol Stunkel — dogs, cats and horses "
        "photographed in their own homes.",
        body,
        extra_scripts='<script src="assets/js/data.js"></script>\n',
    )


# ---------------------------------------------------------- exhibitions

def exhibitions_page():
    blocks = []
    for heading, rows in content.EXHIBITIONS:
        lis = "\n".join(
            f'        <li><span>{where}</span><span>{when}</span></li>'
            for where, when in rows
        )
        blocks.append(f'      <h2>{heading}</h2>\n      <ul>\n{lis}\n      </ul>')
    inner = '    <div class="exhibits">\n' + "\n".join(blocks) + "\n    </div>"
    return shell(
        "exhibitions.html",
        "Exhibitions — Furry Faces",
        "Galleries, libraries and one-woman shows exhibiting the animal photography "
        "of Mary Carol Stunkel.",
        panel("Exhibitions", inner),
    )


# -------------------------------------------------------------- pricing

def pricing_page():
    inner = f"""    <div class="prose">
      <p class="lede">For your convenience and your pet's comfort, Mary Carol comes to your
      home to capture your pet's best expressions.</p>
    </div>

    <div class="package">
      <p class="package__price">$395</p>
      <p class="package__label">Complete location package</p>
      <ul>
        <li>Photo session at your home</li>
        <li>Three 5&thinsp;&times;&thinsp;7 matted photographs (different shots)</li>
        <li>One 11&thinsp;&times;&thinsp;14 matted photograph</li>
        <li>Six wallet-size photographs</li>
      </ul>
    </div>

    <div class="prose">
      <p>Custom pet photo cards with your personalized greeting are available in boxed sets of twelve.</p>
      <p>Unframed matted copies of all the Furry Faces on this site are available for purchase.
      Email or call for a price list.</p>
      <p>For more information, please contact Mary Carol at MC Squared Productions:<br>
      <a href="mailto:{EMAIL}">{EMAIL}</a><br>
      <a href="tel:{PHONE_HREF}">{PHONE}</a></p>
    </div>"""
    return shell(
        "pricing.html",
        "Pricing — Furry Faces",
        "The complete Furry Faces location package: an in-home photo session with matted "
        "prints, $395. Custom pet photo cards also available.",
        panel("Pricing", inner),
    )


# --------------------------------------------------------- expectations

def expectations_page():
    inner = """    <div class="prose">
      <p class="lede">First make sure you've allowed enough time in your schedule.
      A Furry Faces photo session takes two to three hours.</p>

      <p>It would be rude to take a picture of someone without being properly introduced,
      so I take a while to establish a trusting relationship with your pet while he or she is
      allowed to investigate my equipment. I never begin until I get what my husband calls
      the &ldquo;sniff-biff&rdquo; of approval.</p>

      <p>Since I work almost exclusively at your location, I'll need to be shown some of your
      pet's favorite places and listen to your concerns or ideas for backgrounds. Part of why
      I'm able to make your animals look comfortable is because they are on a familiar chair or
      backyard spot. I'll be prepared when we shoot indoors, but I much prefer using natural
      light. Animals don't appreciate flashed lights any more than humans do, so I never use them.</p>

      <p>Then we start taking pictures. Unlike some photographers, I require that the owner or
      someone who knows the pet well be present throughout the session. You'll probably want to
      give up before I do, and you may find your pet quite exhausted at the end of the session
      &mdash; but the results will be worth the effort. By the way, the strange barks, meows,
      chirps and whistles are probably just me trying to get your pet's attention.</p>

      <p>Finally, sit back, pet your furry friend, and wait for the results. I usually have
      finished photos in about a week.</p>
    </div>"""
    return shell(
        "expectations.html",
        "What to Expect — Furry Faces",
        "What happens during a Furry Faces pet portrait session: natural light, no flash, "
        "two to three hours in your own home.",
        panel("What to Expect", inner),
    )


# --------------------------------------------------------------- posing

def posing_page():
    photos = ["1", "2", "4", "5", "6"]
    strip = "\n".join(
        f'      <img src="assets/img/posing/{p}.jpg" alt="A Furry Faces portrait session in progress" loading="lazy">'
        for p in photos
    )
    inner = f"""    <div class="prose">
      <p class="lede">My own private experience poll has proven that few pets really understand
      the simple commands <em>sit</em> and <em>stay</em>.</p>

      <p>Since this is more often than not the norm, please don't be apologetic if your pet falls
      into this category. However, both for you and your animal's happiness I strongly advise a
      bit of training. Like discipline for children, animals who understand limits are more secure
      and happier. It certainly helps my job, and will make living with your pet even more rewarding.</p>

      <p>Since I shoot with quite slow exposures and no flash, to get the kind of close-up clarity
      we both expect, an animal that stays on command makes for a quicker and more pleasant session
      &mdash; for the owner, for the animal, and for me too.</p>

      <p>Models get big bucks for a reason, but many of my subjects can be coaxed to work very hard
      to show me their best. And I'm not proud&hellip; have treats available. When all else fails,
      we can use a leash. I've become very proficient at painting out bridles, leashes and collars.
      I'll never tell if you don't.</p>

      <p>A special word for cat owners&hellip; just help me find a room where we can shut the doors
      and they can't hide. I share my house with four cats and speak fluent &ldquo;catonese.&rdquo;</p>
    </div>

    <div class="photo-strip">
{strip}
    </div>"""
    return shell(
        "posing.html",
        "Posing Pets — Furry Faces",
        "Notes on posing pets for a portrait session, from photographer Mary Carol Stunkel.",
        panel("Posing Pets", inner),
    )


# ------------------------------------------------------------- comments

def comments_page():
    figs = "\n".join(
        f"""      <figure class="quote">
        <p>&ldquo;{q}&rdquo;</p>
        <figcaption>&mdash; {who}, {where}</figcaption>
      </figure>"""
        for q, who, where in content.QUOTES
    )
    inner = f'    <div class="quotes">\n{figs}\n    </div>'
    return shell(
        "comments.html",
        "Client Comments — Furry Faces",
        "What clients say about their Furry Faces pet portraits.",
        panel("Client Comments", inner),
    )


# ------------------------------------------------------------------ bio

def bio_page():
    inner = """    <div class="with-figure">
      <div class="prose">
        <p class="lede">After thirty years as a video producer and director, Mary Carol Stunkel
        decided to focus on one picture at a time and began the serious study of her long-time
        hobby, photography.</p>

        <p>Now equally at home in the dark room pursuing her specialty of black-and-white infrared
        and in the digital realm, Mary Carol is reveling in the challenge of communicating through
        images without sound. She is president of MC Squared Productions in Neptune, New Jersey.
        When not working behind the lens, Mary Carol is a published short story writer and adjunct
        professor at Monmouth University.</p>

        <p>Furry Faces blends her visual arts expertise with her genuine love of animals to produce
        portraits that capture your pet's spirit.</p>

        <blockquote class="pull">
          <p>Although I take photos of animals who aren't addressing the camera, it is the directed
          gaze that most holds my interest. I don't look for just cute pets, but furry faces whose
          eyes are soul windows through which we see the unprompted yearnings, joy, wisdom, and
          non-judgmental nature of our four-legged companions.</p>
        </blockquote>

        <p>Each of the creatures who gaze at you in her images said something worth hearing to
        Mary Carol. She hopes they'll speak to you too.</p>

        <p><a href="contact.html">Click here to contact Mary Carol</a>.</p>
      </div>
      <img src="assets/img/site/mary-carol.jpg" alt="Mary Carol Stunkel" loading="lazy">
    </div>"""
    return shell(
        "bio.html",
        "Bio — Mary Carol Stunkel, Furry Faces",
        "Mary Carol Stunkel: thirty years a video producer and director, now a photographer of "
        "animals in Neptune, New Jersey.",
        panel("Bio", inner),
    )


# -------------------------------------------------------------- contact

def contact_page():
    inner = f"""    <div class="contact-card">
      <div class="contact-lines">
        <strong>Mary Carol Stunkel</strong>
        MC Squared Productions<br>
        Neptune, New Jersey<br>
        <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        <a href="tel:{PHONE_HREF}">{PHONE}</a>
      </div>
      <img src="assets/img/site/cat-in-a-case.jpg" alt="A cat curled up in a camera case" loading="lazy">
    </div>"""
    return shell(
        "contact.html",
        "Contact — Furry Faces",
        f"Contact Mary Carol Stunkel at MC Squared Productions — {EMAIL} — {PHONE}.",
        panel("Contact", inner),
    )


# ------------------------------------------------------- pet of the month

def pet_page(data):
    pets = data["pet"]
    thumbs = "\n".join(
        f'        <button class="gallery__thumb" type="button" data-pet-thumb'
        f' data-full="assets/img/pet/{p["slug"]}.jpg" aria-current="{"true" if i == 0 else "false"}">'
        f'<img src="assets/img/pet/thumbs/{p["slug"]}.jpg" width="178" height="130"'
        f' alt="Cleo and Bailey, Basset Hounds" loading="lazy"></button>'
        for i, p in enumerate(pets)
    )
    first = pets[0]
    inner = f"""    <div class="with-figure">
      <div class="prose">
        <p class="lede">Meet Cleo &amp; Bailey, Basset Hounds.</p>
        <p>I couldn't stop taking pictures of this pair of charmers. Those eyes!!</p>
        <p>Cleo, the older one with the darker ears and more white on her face, was a Christmas
        puppy. She was a surprise under the tree with a bow. Her face wasn't white then, but
        reportedly turned white over night&hellip; after a really bad thunder storm. I'm told she
        still hides at the first rumble.</p>
        <p>Bailey was a rescue puppy. She was adopted from a New York City shelter and was quite
        literally skin and bones, even after two weeks of shelter care. Obviously she is well and
        happy in her adopted New Jersey home. However, she still has a bit of the wanderer in her,
        and once ran off and was found at the Little Silver train station watching the NYC commuters.</p>
        <p>These girls, like most Bassets, are very happy dogs and would have far preferred to play
        rather than pose &mdash; but they were quite patient models&hellip; until they decided they
        were done. Then, no matter what treat was offered or what funny noise I made, they just
        wanted to nap&hellip; as you can see in their looks in the last two photos.</p>
      </div>

      <div class="pet-viewer" data-pet>
        <div class="pet-viewer__stage">
          <img data-pet-image src="assets/img/pet/{first['slug']}.jpg"
               alt="Cleo and Bailey, Basset Hounds">
        </div>
        <div class="pet-viewer__thumbs">
{thumbs}
        </div>
      </div>
    </div>"""
    return shell(
        "pet-of-the-month.html",
        "Pet of the Month — Furry Faces",
        "This month's Furry Faces: Cleo and Bailey, two Basset Hounds from New Jersey.",
        panel("Pet of the Month", inner),
    )


def main():
    data = json.load(open(f"{OUT}/assets/js/data.json"))

    # Data for the gallery viewer, as a plain script (works over file:// too).
    with open(f"{OUT}/assets/js/data.js", "w") as fh:
        fh.write("window.FF_DATA = " + json.dumps(data, indent=1) + ";\n")

    pages = {
        "index.html": home_page(data),
        "gallery.html": gallery_page(data),
        "exhibitions.html": exhibitions_page(),
        "pricing.html": pricing_page(),
        "expectations.html": expectations_page(),
        "posing.html": posing_page(),
        "comments.html": comments_page(),
        "bio.html": bio_page(),
        "contact.html": contact_page(),
        "pet-of-the-month.html": pet_page(data),
    }
    for name, html in pages.items():
        with open(os.path.join(OUT, name), "w") as fh:
            fh.write(html)
        print("wrote", name, len(html), "bytes")


if __name__ == "__main__":
    main()
