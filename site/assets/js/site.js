/* Furry Faces — behaviour.
   Three small widgets, no dependencies:
     1. the homepage slideshow (replaces the Flash ImageViewer)
     2. the gallery viewer (replaces the 32 static gallery_NN-x.htm pages)
     3. the mobile nav toggle
   Everything degrades: with JS off the first image of each set still renders. */

(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- mobile nav ------------------------------------------- */

  var toggle = document.querySelector(".nav__toggle");
  var navList = document.getElementById("nav-list");
  if (toggle && navList) {
    toggle.addEventListener("click", function () {
      var open = navList.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  /* ---------- slideshow -------------------------------------------- */
  /* Matches the original Flash settings: 3s per slide, fade, loop, autoplay. */

  var show = document.querySelector("[data-slideshow]");
  if (show) {
    var slides = Array.prototype.slice.call(show.querySelectorAll(".slideshow__slide"));
    var dots = Array.prototype.slice.call(show.querySelectorAll(".slideshow__dot"));
    var playBtn = show.querySelector("[data-slideshow-play]");
    var index = 0;
    var timer = null;
    var playing = !reduceMotion;

    function render(next) {
      index = (next + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle("is-active", i === index); });
      dots.forEach(function (d, i) {
        d.classList.toggle("is-active", i === index);
        d.setAttribute("aria-current", i === index ? "true" : "false");
      });
    }

    function start() {
      stop();
      timer = window.setInterval(function () { render(index + 1); }, 3000);
      playing = true;
      if (playBtn) {
        playBtn.textContent = "❚❚";
        playBtn.setAttribute("aria-label", "Pause slideshow");
      }
    }

    function stop() {
      if (timer) { window.clearInterval(timer); timer = null; }
      playing = false;
      if (playBtn) {
        playBtn.textContent = "▶";
        playBtn.setAttribute("aria-label", "Play slideshow");
      }
    }

    dots.forEach(function (d, i) {
      d.addEventListener("click", function () { render(i); stop(); });
    });

    var prev = show.querySelector("[data-slideshow-prev]");
    var next = show.querySelector("[data-slideshow-next]");
    if (prev) prev.addEventListener("click", function () { render(index - 1); stop(); });
    if (next) next.addEventListener("click", function () { render(index + 1); stop(); });
    if (playBtn) {
      playBtn.addEventListener("click", function () { playing ? stop() : start(); });
    }

    // Don't burn cycles (or battery) while the tab is hidden.
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) { if (playing) { stop(); playing = true; } }
      else if (playing) { start(); }
    });

    render(0);
    if (!reduceMotion) start();
  }

  /* ---------- gallery viewer ---------------------------------------- */

  var gallery = document.querySelector("[data-gallery]");
  if (gallery && window.FF_DATA && window.FF_DATA.gallery) {
    var items = window.FF_DATA.gallery;
    var img = gallery.querySelector("[data-gallery-image]");
    var title = gallery.querySelector("[data-gallery-title]");
    var subject = gallery.querySelector("[data-gallery-subject]");
    var count = gallery.querySelector("[data-gallery-count]");
    var thumbs = Array.prototype.slice.call(gallery.querySelectorAll("[data-gallery-thumb]"));
    var current = 0;

    function show(i, pushHash) {
      current = (i + items.length) % items.length;
      var item = items[current];
      img.src = "assets/img/gallery/" + item.slug + ".jpg";
      img.width = item.w;
      img.height = item.h;
      img.alt = item.title + " — " + item.subject;
      title.textContent = item.title;
      subject.textContent = item.subject;
      count.textContent = (current + 1) + " of " + items.length;
      thumbs.forEach(function (t, n) {
        t.setAttribute("aria-current", n === current ? "true" : "false");
      });
      document.title = item.title + " — Furry Faces";
      if (pushHash) {
        history.replaceState(null, "", "#" + item.slug);
      }
      // keep the active thumb in view on the scrolling rail
      var active = thumbs[current];
      if (active && active.scrollIntoView) {
        active.scrollIntoView({ block: "nearest", inline: "nearest" });
      }
    }

    thumbs.forEach(function (t, n) {
      t.addEventListener("click", function () { show(n, true); });
    });

    var gPrev = gallery.querySelector("[data-gallery-prev]");
    var gNext = gallery.querySelector("[data-gallery-next]");
    if (gPrev) gPrev.addEventListener("click", function () { show(current - 1, true); });
    if (gNext) gNext.addEventListener("click", function () { show(current + 1, true); });

    document.addEventListener("keydown", function (e) {
      if (e.target.matches("input, textarea")) return;
      if (e.key === "ArrowLeft") { show(current - 1, true); }
      if (e.key === "ArrowRight") { show(current + 1, true); }
    });

    function fromHash() {
      var slug = window.location.hash.replace("#", "");
      var found = items.findIndex(function (it) { return it.slug === slug; });
      show(found > -1 ? found : 0, false);
    }
    window.addEventListener("hashchange", fromHash);
    fromHash();
  }

  /* ---------- pet of the month viewer -------------------------------- */

  var pet = document.querySelector("[data-pet]");
  if (pet) {
    var petImg = pet.querySelector("[data-pet-image]");
    var petThumbs = Array.prototype.slice.call(pet.querySelectorAll("[data-pet-thumb]"));
    petThumbs.forEach(function (t) {
      t.addEventListener("click", function () {
        petImg.src = t.dataset.full;
        petImg.alt = t.querySelector("img").alt;
        petThumbs.forEach(function (o) { o.setAttribute("aria-current", String(o === t)); });
      });
    });
  }
})();
