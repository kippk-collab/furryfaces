"""One-off: copy legacy assets into site/, slugified, with generated thumbs."""
import os, re, json, shutil
from PIL import Image, ImageOps

L = "legacy"
OUT = "site/assets/img"

GALLERY = [
    ("MagicMondrian.jpg",        "Magic a la Mondrian",                          "Magic, the Appaloosa"),
    ("Reflection.jpg",           "Reflection of Perfection",                     "BooBoo Kitty, the Persian"),
    ("SafeBehindMom.jpg",        "Safe Behind Mom",                              "Cholo, a Powder Puff Chinese Crested"),
    ("TheDogDayS.jpg",           "The Dog Days of Summer",                       "Dakota, Cassidy & Eli, Golden Retrievers"),
    ("Anyoneforwalk.jpg",        "Anyone for a Walk?",                           "Cocoa, the brown Labrador"),
    ("IsmellMouse.jpg",          "I Smell a Mouse",                              "Owen, the Tabby"),
    ("GoliathSittingPretty.jpg", "Is it me or are they making sofas smaller?",   "Goliath, the Great Dane"),
    ("TheNobleGentleman.jpg",    "A Noble Gentleman",                            "Cappy, the Quarter horse"),
    ("All-seeingEyes.jpg",       "The All-Seeing Eyes",                          "Igloo, the Italian Greyhound"),
    ("IonlyHaveEyes.jpg",        "I only have eyes for you",                     "Timber, the white Husky"),
    ("ToPlayorNot.jpg",          "To play or not to play?",                      "Ting-the-Terrible, a Singapura"),
    ("TheSoundof.jpg",           "The Sound of my Master's Voice",               "Mako, the yellow Labrador"),
    ("TheArtfulDodger.jpg",      "The Artful Dodger",                            "Boris, the Silky Terrier"),
    ("What's4breakfast.jpg",     "What's for Breakfast?",                        "Eckman, the Norwegian Fjord horse"),
    ("FamilyHierarchy.jpg",      "Family Hierarchy",                             "Gracie, Roxie, Mazzy (the Mom) & Bogie, Boston Terriers"),
    ("OnDuty.jpg",               "On Duty",                                      "Ono, a Belgian Malanois, Military Working dog"),
    ("ImightBeFriend.jpg",       "I might be your friend",                       "Cholo, a Powder Puff Chinese Crested"),
    ("BeepABoo.jpg",             "Peek-a-boo",                                   "Portia, the Tabby"),
    ("CanWeTalk.jpg",            "Can We Talk?",                                 "Rocky, the Bichon Frise"),
    ("RealHomelandSecurity.jpg", "Real Homeland Security",                       "Maya, the German Shepherd"),
    ("MyFurryBookworm.jpg",      "My Furry Bookworm",                            "Ting-the-Terrible, a Singapura"),
    ("CanineConcntration.jpg",   "Canine Concentration",                         "Polly, the Rotweiller"),
    ("TheCalltheWild.jpg",       "The Call of the Wild",                         "Posey, the Abyssinian"),
    ("IDidn'tdoIt.jpg",          "I didn't do it",                               "Gromit, the Jack Russell Terrier"),
    ("MyGrassGreener.jpg",       "My Grass is Greener!",                         "Bailey, the Basset Hound"),
    ("OeyVey!.jpg",              "Oy Vei",                                       "Cleo, the Basset Hound"),
    ("momandme.jpg",             "Mom and Me: Perfect Together",                 "Sadie, a Yorkie Terrier"),
    ("OldFaithfulYankee .jpg",   "Old Faithful",                                 "Yankee, the Golden Retreiver"),
    ("TwoBeauties.jpg",          "Two Dark Eyed Beauties",                       "Fuzzy & Lily, English Spaniels"),
    ("ThiswayIsit.jpg",          "This is the way I sit!",                       "Bodhi, the Swiss Mountain Dog"),
    ("Double-the-Fun.jpg",       "Reclining Nudes",                              "Whitey & Littleman, Bearded Collies"),
    ("PuttinonRitz.jpg",         "Puttin' on the Ritz",                          "Madonna the 10 week old kitten"),
]

def slug(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", os.path.splitext(s)[0]).strip("-").lower()
    return re.sub(r"-+", "-", s)

def save(im, path, quality=82):
    im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)

os.makedirs(f"{OUT}/gallery/thumbs", exist_ok=True)
items = []
for fn, title, subject in GALLERY:
    src = f"{L}/images/gallery_big/{fn}"
    s = slug(fn)
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        save(im, f"{OUT}/gallery/{s}.jpg")
        w, h = im.size
        t = ImageOps.fit(im, (178, 130), Image.LANCZOS, centering=(0.5, 0.4))
        save(t, f"{OUT}/gallery/thumbs/{s}.jpg", 80)
    items.append({"slug": s, "title": title, "subject": subject, "w": w, "h": h})

# ---- homepage slideshow (same 11 images, same order as the Flash flashvars)
SLIDES = ["Chloe", "Okay-you-have-our-attention-Corgies", "Tabby-on-Table", "The-Three-Tenors",
          "Why-the-long-face-Sunkist", "King-in-his-castle", "If-this-were-Egypt",
          "Magic-in-a-magic-land", "The-Immovable-Object-Bozwell", "Regal-Beagle-2", "Ying-Yang"]
SLIDE_ALT = {
    "Chloe": "Chloe", "Okay-you-have-our-attention-Corgies": "Okay, you have our attention",
    "Tabby-on-Table": "Tabby on the table", "The-Three-Tenors": "The Three Tenors",
    "Why-the-long-face-Sunkist": "Why the long face, Sunkist?", "King-in-his-castle": "King in his castle",
    "If-this-were-Egypt": "If this were Egypt", "Magic-in-a-magic-land": "Magic in a magic land",
    "The-Immovable-Object-Bozwell": "The Immovable Object, Bozwell", "Regal-Beagle-2": "Regal Beagle",
    "Ying-Yang": "Ying and Yang",
}
os.makedirs(f"{OUT}/slideshow", exist_ok=True)
slides = []
for name in SLIDES:
    src = f"{L}/images/slideshow/{name}.jpg"
    s = slug(name)
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        save(im, f"{OUT}/slideshow/{s}.jpg")
        w, h = im.size
    slides.append({"slug": s, "alt": SLIDE_ALT[name], "w": w, "h": h})

# ---- pet of the month glider
os.makedirs(f"{OUT}/pet/thumbs", exist_ok=True)
pet = []
for fn in sorted(os.listdir(f"{L}/p7hg_img_2/fullsize")):
    s = slug(fn.replace("_large", "").replace("_Large", ""))
    with Image.open(f"{L}/p7hg_img_2/fullsize/{fn}") as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        save(im, f"{OUT}/pet/{s}.jpg")
        w, h = im.size
        t = ImageOps.fit(im, (178, 130), Image.LANCZOS, centering=(0.5, 0.4))
        save(t, f"{OUT}/pet/thumbs/{s}.jpg", 80)
    pet.append({"slug": s, "alt": s.replace("-", " ").title(), "w": w, "h": h})

# ---- posing page photos + misc site chrome
os.makedirs(f"{OUT}/posing", exist_ok=True)
for fn in sorted(os.listdir(f"{L}/images/posing")):
    with Image.open(f"{L}/images/posing/{fn}") as im:
        save(ImageOps.exif_transpose(im).convert("RGB"), f"{OUT}/posing/{slug(fn)}.jpg")

os.makedirs(f"{OUT}/site", exist_ok=True)
for fn, dest in [("home-chloe.jpg", "home-chloe.jpg"), ("MC.jpg", "mary-carol.jpg"),
                 ("catInAcase.jpg", "cat-in-a-case.jpg"), ("Goliath-_B.jpg", "goliath.jpg"),
                 ("Master-of.jpg", "master-of.jpg"), ("on-red-chair-2.jpg", "on-red-chair.jpg"),
                 ("Pee-Wee.jpg", "pee-wee.jpg"), ("Sebastian--_A.jpg", "sebastian.jpg")]:
    src = f"{L}/images/{fn}"
    if os.path.exists(src):
        with Image.open(src) as im:
            save(ImageOps.exif_transpose(im).convert("RGB"), f"{OUT}/site/{dest}")

# header banner: the two sliced halves recombined into one image
with Image.open(f"{L}/images/top_01.jpg") as a, Image.open(f"{L}/images/top_02.jpg") as b:
    banner = Image.new("RGB", (a.width + b.width, max(a.height, b.height)), (0, 0, 0))
    banner.paste(a.convert("RGB"), (0, 0)); banner.paste(b.convert("RGB"), (a.width, 0))
    save(banner, f"{OUT}/site/banner.jpg", 88)
shutil.copy2(f"{L}/images/images_by mcs.gif", f"{OUT}/site/images-by-mcs.gif")

json.dump({"gallery": items, "slides": slides, "pet": pet},
          open("site/assets/js/data.json", "w"), indent=1)
print("gallery", len(items), "slides", len(slides), "pet", len(pet))
