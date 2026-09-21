#!/usr/bin/env python3
"""Generate site-bold/ — the "catalogue" skin.

Same words and same photographs as site/, presented as an exhibition catalogue:
warm paper, didone display type, plates in mats. Copy lives in content.py, so
editing text there updates both skins.

    python3 build_bold.py
"""

import json
import os
import shutil

import content
from content import EMAIL, NAV, PHONE, PHONE_HREF

OUT = "site-bold"
SRC_ASSETS = "site/assets/img"

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..700;1,6..96,400..700"
         "&family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..600&display=swap")


def nav_links(active):
    return "\n".join(
        f'        <li><a href="{href}"'
        f'{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for href, label in NAV
    )


def shell(active, title, description, body, scripts=""):
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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="assets/css/catalogue.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="masthead">
  <p class="label masthead__eyebrow">Classic Animal Portraits &middot; Established 2003</p>
  <h1 class="masthead__title"><a href="index.html">Furry Faces</a></h1>
  <p class="masthead__sub">Photographs by Mary Carol Stunkel &middot; {content.TOWN}</p>
</header>

<nav class="nav" aria-label="Main">
  <div class="nav__rules">
    <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-list">Contents</button>
    <ul class="nav__list" id="nav-list">
{nav_links(active)}
    </ul>
  </div>
</nav>

<main class="page" id="main">
{body}
</main>

<footer class="footer">
  <p class="footer__name">Furry Faces</p>
  <p class="footer__line">{content.BUSINESS} &middot; {content.TOWN}</p>
  <p class="footer__line">
    <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="tel:{PHONE_HREF}">{PHONE}</a>
  </p>
  <p class="footer__line">Photographs &copy; Mary Carol Stunkel. All rights reserved.</p>
</footer>

{scripts}<script src="assets/js/catalogue.js"></script>
</body>
</html>
"""


def page_head(eyebrow, title):
    return f"""  <div class="page-head">
    <p class="label">{eyebrow}</p>
    <h2 class="page-head__title">{title}</h2>
  </div>"""


# ---------------------------------------------------------------- home

def home_page(data):
    slides = "\n".join(
        f'          <img class="viewer__slide{" is-active" if i == 0 else ""}"'
        f' src="assets/img/slideshow/{s["slug"]}.jpg" width="{s["w"]}" height="{s["h"]}"'
        f' alt="{s["alt"]}"{"" if i == 0 else " loading=\"lazy\""}>'
        for i, s in enumerate(data["slides"])
    )
    ticks = "\n".join(
        f'            <button class="viewer__tick{" is-active" if i == 0 else ""}" type="button"'
        f' aria-label="Plate {i + 1}"></button>'
        for i in range(len(data["slides"]))
    )
    body = f"""  <div class="opening">
    <div>
      <p class="label reveal reveal--1">Portraits made at home, in natural light</p>
      <p class="opening__statement reveal reveal--2">
        The eyes are <em>soul windows.</em>
      </p>
      <div class="prose opening__body reveal reveal--3">
        <p>For more than twenty years Mary Carol Stunkel has photographed dogs, cats and
        horses where they actually live &mdash; on the familiar chair, in the backyard,
        never with a flash, never in a studio.</p>
      </div>
      <div class="opening__actions reveal reveal--4">
        <a class="button" href="gallery.html">View the plates</a>
        <a class="button button--quiet" href="pet-of-the-month.html">Pet of the month</a>
      </div>
    </div>

    <figure class="plate viewer reveal reveal--2" data-viewer>
      <div class="plate__mat">
        <div class="viewer__stage">
{slides}
        </div>
      </div>
      <figcaption class="plate__caption">
        <span class="plate__number" data-viewer-number>Plate 01 / {len(data["slides"]):02d}</span>
        <p class="plate__title" data-viewer-caption>{data["slides"][0]["alt"]}</p>
        <div class="viewer__bar">
          <div class="viewer__ticks">
{ticks}
          </div>
          <button class="viewer__pause" type="button" data-viewer-pause>Pause</button>
        </div>
      </figcaption>
    </figure>
  </div>"""
    return shell(
        "index.html",
        "Furry Faces — Animal Portraits by Mary Carol Stunkel",
        "Fine-art pet portraits photographed in your own home by Mary Carol Stunkel, "
        "MC Squared Productions, Neptune, New Jersey.",
        body,
    )


# ------------------------------------------------------------- gallery

def gallery_page(data):
    items = data["gallery"]
    cells = []
    for i, it in enumerate(items):
        number = f"{i + 1:02d}"
        cells.append(f"""      <figure class="hang__item">
        <button class="hang__button" type="button" data-plate
                data-full="assets/img/gallery/{it['slug']}.jpg"
                data-title="{it['title']}" data-subject="{it['subject']}" data-number="{number}">
          <div class="plate__mat">
            <div class="plate__frame">
              <img class="plate__img" src="assets/img/gallery/{it['slug']}.jpg"
                   width="{it['w']}" height="{it['h']}"
                   alt="{it['title']} — {it['subject']}" loading="lazy">
            </div>
          </div>
          <figcaption class="plate__caption">
            <span class="plate__number">Plate {number}</span>
            <p class="plate__title">{it['title']}</p>
            <p class="plate__subject">{it['subject']}</p>
          </figcaption>
        </button>
      </figure>""")

    body = f"""{page_head(f"Thirty-two plates", "The Gallery")}

    <div class="hang">
{chr(10).join(cells)}
    </div>

    <p class="prose" style="margin-top:3.5rem">
      Unframed matted copies of every plate are available for purchase.
      <a href="mailto:{EMAIL}">Write to Mary Carol</a> or call {PHONE} for a price list.
    </p>

  <div class="lightbox" data-lightbox role="dialog" aria-modal="true" aria-label="Photograph">
    <button class="lightbox__close" type="button" data-lightbox-close aria-label="Close">&times;</button>
    <button class="lightbox__nav lightbox__nav--prev" type="button" data-lightbox-prev aria-label="Previous">&#8249;</button>
    <button class="lightbox__nav lightbox__nav--next" type="button" data-lightbox-next aria-label="Next">&#8250;</button>
    <div class="lightbox__inner">
      <img class="lightbox__img" data-lightbox-image src="" alt="">
      <div class="lightbox__caption">
        <span class="plate__number" data-lightbox-number></span>
        <p class="plate__title" data-lightbox-title></p>
        <p class="plate__subject" data-lightbox-subject></p>
      </div>
    </div>
  </div>"""
    return shell(
        "gallery.html",
        "The Gallery — Furry Faces",
        "Thirty-two animal portraits by Mary Carol Stunkel — dogs, cats and horses "
        "photographed in their own homes.",
        body,
    )


# ---------------------------------------------------------- exhibitions

def exhibitions_page():
    groups = []
    for heading, rows in content.EXHIBITIONS:
        lis = "\n".join(
            f'          <li><span>{where}</span>'
            f'<span class="record__when">{when}</span></li>'
            for where, when in rows
        )
        groups.append(f"""      <div class="record__group">
        <h3 class="record__heading">{heading}</h3>
        <ul>
{lis}
        </ul>
      </div>""")
    body = f"""{page_head("Where the work has hung", "Exhibitions")}

    <div class="record">
{chr(10).join(groups)}
    </div>"""
    return shell(
        "exhibitions.html",
        "Exhibitions — Furry Faces",
        "Galleries, libraries and one-woman shows exhibiting the animal photography of "
        "Mary Carol Stunkel.",
        body,
    )


# -------------------------------------------------------------- pricing

def pricing_page():
    lis = "\n".join(
        f'          <li><span>{i + 1:02d}</span><span>{line}</span></li>'
        for i, line in enumerate(content.PACKAGE)
    )
    body = f"""{page_head("Commissions", "Pricing")}

    <p class="lede">{content.PRICING_LEDE}</p>

    <div class="tariff">
      <div>
        <p class="tariff__price">{content.PRICE}</p>
        <p class="label">{content.PRICE_LABEL}</p>
      </div>
      <ul>
{lis}
      </ul>
    </div>

    <div class="prose">
      {content.PRICING_NOTES}
      <p>For more information, please write to Mary Carol at {content.BUSINESS}:<br>
      <a href="mailto:{EMAIL}">{EMAIL}</a><br>
      <a href="tel:{PHONE_HREF}">{PHONE}</a></p>
    </div>"""
    return shell(
        "pricing.html",
        "Pricing — Furry Faces",
        f"The complete Furry Faces location package: an in-home session with matted prints, "
        f"{content.PRICE}.",
        body,
    )


# ----------------------------------------------------- essays (3 pages)

def essay_page(active, eyebrow, title, lede, prose, description, figure=""):
    body = f"""{page_head(eyebrow, title)}

    <div class="spread">
      <div>
        <p class="lede">{lede}</p>
        <div class="prose prose--essay">
          {prose}
        </div>
      </div>
      {figure}
    </div>"""
    return shell(active, f"{title} — Furry Faces", description, body)


def plate_figure(src, alt, number, title, subject=""):
    sub = f'<p class="plate__subject">{subject}</p>' if subject else ""
    return f"""<figure class="plate">
        <div class="plate__mat">
          <div class="plate__frame">
            <img class="plate__img" src="{src}" alt="{alt}" loading="lazy">
          </div>
        </div>
        <figcaption class="plate__caption">
          <span class="plate__number">{number}</span>
          <p class="plate__title">{title}</p>
          {sub}
        </figcaption>
      </figure>"""


def posing_page():
    strip = "\n".join(
        f'      <img src="assets/img/posing/{p}.jpg" alt="A Furry Faces session in progress" loading="lazy">'
        for p in content.POSING_PHOTOS
    )
    body = f"""{page_head("A note to owners", "Posing Pets")}

    <div class="prose prose--essay">
      <p class="lede" style="font-family:var(--display)">{content.POSING_LEDE}</p>
      {content.POSING_BODY}
    </div>

    <div class="strip">
{strip}
    </div>"""
    return shell(
        "posing.html", "Posing Pets — Furry Faces",
        "Notes on posing pets for a portrait session, from photographer Mary Carol Stunkel.",
        body,
    )


# ------------------------------------------------------------- comments

def comments_page():
    figs = "\n".join(
        f"""      <figure>
        <blockquote>&ldquo;{q}&rdquo;</blockquote>
        <figcaption>{who} &middot; {where}</figcaption>
      </figure>"""
        for q, who, where in content.QUOTES
    )
    body = f"""{page_head("In their own words", "Client Comments")}

    <div class="testimony">
{figs}
    </div>"""
    return shell(
        "comments.html", "Client Comments — Furry Faces",
        "What clients say about their Furry Faces pet portraits.", body,
    )


# -------------------------------------------------------------- contact

def contact_page():
    body = f"""{page_head("Enquiries", "Contact")}

    <div class="spread">
      <div class="contact-block">
        <strong>Mary Carol Stunkel</strong>
        {content.BUSINESS}<br>
        {content.TOWN}<br>
        <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        <a href="tel:{PHONE_HREF}">{PHONE}</a>
      </div>
      {plate_figure("assets/img/site/cat-in-a-case.jpg",
                    "A cat curled up in a camera case", "Frontispiece",
                    "Travelling companion")}
    </div>"""
    return shell(
        "contact.html", "Contact — Furry Faces",
        f"Contact Mary Carol Stunkel at {content.BUSINESS} — {EMAIL} — {PHONE}.", body,
    )


# ------------------------------------------------------ pet of the month

def pet_page(data):
    pets = data["pet"]
    plates = "\n".join(
        f"""      <figure class="hang__item">
        <button class="hang__button" type="button" data-plate
                data-full="assets/img/pet/{p['slug']}.jpg"
                data-title="Cleo &amp; Bailey" data-subject="Basset Hounds" data-number="{i + 1:02d}">
          <div class="plate__mat">
            <div class="plate__frame">
              <img class="plate__img" src="assets/img/pet/{p['slug']}.jpg"
                   width="{p['w']}" height="{p['h']}" alt="Cleo and Bailey, Basset Hounds" loading="lazy">
            </div>
          </div>
          <figcaption class="plate__caption">
            <span class="plate__number">Plate {i + 1:02d}</span>
          </figcaption>
        </button>
      </figure>"""
        for i, p in enumerate(pets)
    )
    body = f"""{page_head("Pet of the month", content.PET_TITLE)}

    <div class="prose prose--essay" style="margin-bottom:3rem">
      {content.PET_BODY}
    </div>

    <div class="hang">
{plates}
    </div>

  <div class="lightbox" data-lightbox role="dialog" aria-modal="true" aria-label="Photograph">
    <button class="lightbox__close" type="button" data-lightbox-close aria-label="Close">&times;</button>
    <button class="lightbox__nav lightbox__nav--prev" type="button" data-lightbox-prev aria-label="Previous">&#8249;</button>
    <button class="lightbox__nav lightbox__nav--next" type="button" data-lightbox-next aria-label="Next">&#8250;</button>
    <div class="lightbox__inner">
      <img class="lightbox__img" data-lightbox-image src="" alt="">
      <div class="lightbox__caption">
        <span class="plate__number" data-lightbox-number></span>
        <p class="plate__title" data-lightbox-title></p>
        <p class="plate__subject" data-lightbox-subject></p>
      </div>
    </div>
  </div>"""
    return shell(
        "pet-of-the-month.html", "Pet of the Month — Furry Faces",
        "This month's Furry Faces: Cleo and Bailey, two Basset Hounds from New Jersey.",
        body,
    )


def main():
    os.makedirs(OUT, exist_ok=True)
    data = json.load(open("site/assets/js/data.json"))

    # photographs are shared with the other skin
    dest = f"{OUT}/assets/img"
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(SRC_ASSETS, dest)

    bio_figure = plate_figure("assets/img/site/mary-carol.jpg", "Mary Carol Stunkel",
                              "Portrait", "The photographer")

    pages = {
        "index.html": home_page(data),
        "gallery.html": gallery_page(data),
        "exhibitions.html": exhibitions_page(),
        "pricing.html": pricing_page(),
        "expectations.html": essay_page(
            "expectations.html", "Before the session", "What to Expect",
            content.EXPECT_LEDE, content.EXPECT_BODY,
            "What happens during a Furry Faces portrait session: natural light, no flash, "
            "two to three hours in your own home."),
        "posing.html": posing_page(),
        "comments.html": comments_page(),
        "bio.html": essay_page(
            "bio.html", "The photographer", "Mary Carol Stunkel",
            content.BIO_LEDE,
            content.BIO_BODY +
            f'\n<blockquote class="pull-quote"><p>&ldquo;{content.BIO_QUOTE}&rdquo;</p></blockquote>\n' +
            content.BIO_CLOSE,
            "Mary Carol Stunkel: thirty years a video producer and director, now a "
            "photographer of animals in Neptune, New Jersey.",
            bio_figure),
        "contact.html": contact_page(),
        "pet-of-the-month.html": pet_page(data),
    }
    for name, html in pages.items():
        with open(os.path.join(OUT, name), "w") as fh:
            fh.write(html)
        print("wrote", name, len(html), "bytes")


if __name__ == "__main__":
    main()
