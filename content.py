"""All of Mary Carol's words, in one place.

Both builders (build_pages.py → site/, build_bold.py → site-bold/) import from
here, so the copy only ever has to be edited once. Fragments are plain HTML with
no styling classes, so either skin can wrap them however it likes.
"""

# These builds are review copies. While this is True every page carries a
# noindex tag and a disallow-all robots.txt, so Google never files the preview
# alongside (or instead of) her real site. Flip to False for a real launch.
PREVIEW_NOINDEX = True

EMAIL = "MaryCarol@furryfaces.net"
PHONE = "(732) 922-3216"
PHONE_HREF = "+17329223216"
BUSINESS = "MC Squared Productions"
TOWN = "Neptune, New Jersey"

NAV = [
    ("index.html", "home"),
    ("gallery.html", "photo gallery"),
    ("exhibitions.html", "exhibitions"),
    ("pricing.html", "pricing"),
    ("expectations.html", "what to expect"),
    ("posing.html", "posing pets"),
    ("comments.html", "client comments"),
    ("bio.html", "bio"),
    ("contact.html", "contact"),
]

TAGLINE = "Classic animal portraits, captured in your home."

# ---------------------------------------------------------------- bio

BIO_LEDE = ("After thirty years as a video producer and director, Mary Carol Stunkel "
            "decided to focus on one picture at a time and began the serious study of "
            "her long-time hobby, photography.")

BIO_BODY = """<p>Now equally at home in the dark room pursuing her specialty of black-and-white
infrared and in the digital realm, Mary Carol is reveling in the challenge of communicating
through images without sound. She is president of MC Squared Productions in Neptune, New Jersey.
When not working behind the lens, Mary Carol is a published short story writer and adjunct
professor at Monmouth University.</p>

<p>Furry Faces blends her visual arts expertise with her genuine love of animals to produce
portraits that capture your pet's spirit.</p>"""

BIO_QUOTE = ("Although I take photos of animals who aren't addressing the camera, it is the "
             "directed gaze that most holds my interest. I don't look for just cute pets, but "
             "furry faces whose eyes are soul windows through which we see the unprompted "
             "yearnings, joy, wisdom, and non-judgmental nature of our four-legged companions.")

BIO_CLOSE = """<p>Each of the creatures who gaze at you in her images said something worth hearing
to Mary Carol. She hopes they'll speak to you too.</p>"""

# -------------------------------------------------------- what to expect

EXPECT_LEDE = ("First make sure you've allowed enough time in your schedule. "
               "A Furry Faces photo session takes two to three hours.")

EXPECT_BODY = """<p>It would be rude to take a picture of someone without being properly introduced,
so I take a while to establish a trusting relationship with your pet while he or she is allowed to
investigate my equipment. I never begin until I get what my husband calls the
&ldquo;sniff-biff&rdquo; of approval.</p>

<p>Since I work almost exclusively at your location, I'll need to be shown some of your pet's
favorite places and listen to your concerns or ideas for backgrounds. Part of why I'm able to make
your animals look comfortable is because they are on a familiar chair or backyard spot. I'll be
prepared when we shoot indoors, but I much prefer using natural light. Animals don't appreciate
flashed lights any more than humans do, so I never use them.</p>

<p>Then we start taking pictures. Unlike some photographers, I require that the owner or someone
who knows the pet well be present throughout the session. You'll probably want to give up before I
do, and you may find your pet quite exhausted at the end of the session &mdash; but the results
will be worth the effort. By the way, the strange barks, meows, chirps and whistles are probably
just me trying to get your pet's attention.</p>

<p>Finally, sit back, pet your furry friend, and wait for the results. I usually have finished
photos in about a week.</p>"""

# ------------------------------------------------------------- posing

POSING_LEDE = ("My own private experience poll has proven that few pets really understand the "
               "simple commands <em>sit</em> and <em>stay</em>.")

POSING_BODY = """<p>Since this is more often than not the norm, please don't be apologetic if your
pet falls into this category. However, both for you and your animal's happiness I strongly advise a
bit of training. Like discipline for children, animals who understand limits are more secure and
happier. It certainly helps my job, and will make living with your pet even more rewarding.</p>

<p>Since I shoot with quite slow exposures and no flash, to get the kind of close-up clarity we both
expect, an animal that stays on command makes for a quicker and more pleasant session &mdash; for
the owner, for the animal, and for me too.</p>

<p>Models get big bucks for a reason, but many of my subjects can be coaxed to work very hard to
show me their best. And I'm not proud&hellip; have treats available. When all else fails, we can use
a leash. I've become very proficient at painting out bridles, leashes and collars. I'll never tell
if you don't.</p>

<p>A special word for cat owners&hellip; just help me find a room where we can shut the doors and
they can't hide. I share my house with four cats and speak fluent &ldquo;catonese.&rdquo;</p>"""

POSING_PHOTOS = ["1", "2", "4", "5", "6"]

# ------------------------------------------------------------- pricing

PRICING_LEDE = ("For your convenience and your pet's comfort, Mary Carol comes to your home "
                "to capture your pet's best expressions.")

PRICE = "$395"
PRICE_LABEL = "Complete location package"

PACKAGE = [
    "Photo session at your home",
    "Three 5&thinsp;&times;&thinsp;7 matted photographs (different shots)",
    "One 11&thinsp;&times;&thinsp;14 matted photograph",
    "Six wallet-size photographs",
]

PRICING_NOTES = """<p>Custom pet photo cards with your personalized greeting are available in boxed
sets of twelve.</p>

<p>Unframed matted copies of all the Furry Faces on this site are available for purchase.
Email or call for a price list.</p>"""

# --------------------------------------------------------- exhibitions

EXHIBITIONS = [
    ("Recent / Upcoming", [
        ("Brick Library, Brick, NJ", "Jan – February 2008"),
        ("Shoot: The Photography Show — Gallery 125, Trenton, NJ", "Sept. 14 – Nov. 3, 2007"),
        ("9116: 20 Artists Remember — Brookdale Community College, Western Monmouth Campus Gallery",
         "Sept. 2007"),
    ]),
    ("One-Woman Shows — Current / Upcoming", [
        ("Ocean County Library – Berkeley Branch, Bayville, NJ", "September &amp; October 2007"),
    ]),
    ("Completed One-Woman Shows", [
        ("RSI Bank – Long Branch, NJ", "Jan / Feb 2007"),
        ("Ocean County Library", "December 2006"),
        ("Brookdale Community College – Freehold Gallery", "November 2006"),
        ("Guild of Creative Art – Shrewsbury, NJ", "April 2006"),
        ("Marlboro Free Public Library", "April / May 2006"),
        ("Jackson Library", "July / August 2005"),
        ("Monmouth County Library Headquarters, Manalapan, NJ", "April 2005"),
        ("Ocean County Library – Lakewood, NJ", "September 2004"),
        ("Ocean County Library – Toms River, NJ", "August 2004"),
        ("Monmouth County Wall Public Library – Wall, NJ", "January 2004"),
    ]),
    ("Rotating Exhibits", [
        ("Kennington Court – Tinton Falls, NJ", "since June 2006"),
        ("Art of Skin Care – Spring Lake, NJ", "since May 2006"),
        ("Belmar Wall Animal Hospital", "since November 2005"),
        ("Brick Town Veterinary Clinic", "since August 2004"),
        ("Art Alliance, Red Bank, NJ", "Nov. 2004"),
        ("Freehold County Clerk's Office – Freehold, NJ", "bimonthly since July 2003"),
        ("The Blood Center – Shrewsbury, NJ", "since August 2003"),
    ]),
    ("Permanent Exhibits", [
        ("Monmouth Medical Center – West Long Branch, NJ", ""),
    ]),
]

# ------------------------------------------------------------ comments

QUOTES = [
    ("Mary Carol caught the essential spirit and dignity in my dog. Since the death of my pet, "
     "the photographs mean all that much more to me.", "K Koos", "Mantoloking, NJ"),
    ("Mary Carol has the uncanny ability to show what you see in your pet. The portraits have "
     "as much personality as the pet.", "Kim Widener", "Rumson, NJ"),
    ("Her photos captured not only the outside of my dog, but also the inside. His personality "
     "can be seen in your pictures and that's what makes them so special.",
     "Steve Schechter", "Manalapan, NJ"),
    ("You know instantly that Mary Carol loves what she does. Mary Carol has the patience of a "
     "saint in getting the shot you and she have in mind.", "Carole Butler", "Neptune, NJ"),
    ("Mary Carol makes friends with your pet, then does not quit until she captures its essence "
     "on film.", "Chela St. Onge", "Rumson, NJ"),
]

# ------------------------------------------------------ pet of the month

PET_TITLE = "Cleo &amp; Bailey, Basset Hounds"

PET_BODY = """<p>I couldn't stop taking pictures of this pair of charmers. Those eyes!!</p>

<p>Cleo, the older one with the darker ears and more white on her face, was a Christmas puppy.
She was a surprise under the tree with a bow. Her face wasn't white then, but reportedly turned
white over night&hellip; after a really bad thunder storm. I'm told she still hides at the first
rumble.</p>

<p>Bailey was a rescue puppy. She was adopted from a New York City shelter and was quite literally
skin and bones, even after two weeks of shelter care. Obviously she is well and happy in her adopted
New Jersey home. However, she still has a bit of the wanderer in her, and once ran off and was found
at the Little Silver train station watching the NYC commuters.</p>

<p>These girls, like most Bassets, are very happy dogs and would have far preferred to play rather
than pose &mdash; but they were quite patient models&hellip; until they decided they were done.
Then, no matter what treat was offered or what funny noise I made, they just wanted to nap&hellip;
as you can see in their looks in the last two photos.</p>"""
