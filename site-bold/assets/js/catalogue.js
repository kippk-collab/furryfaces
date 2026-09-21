/* Furry Faces — catalogue skin behaviour: opening slideshow, plate lightbox,
   small-screen nav. No dependencies; everything degrades without JS. */

(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- nav --------------------------------------------------- */

  var toggle = document.querySelector(".nav__toggle");
  var list = document.getElementById("nav-list");
  if (toggle && list) {
    toggle.addEventListener("click", function () {
      var open = list.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.textContent = open ? "Close" : "Contents";
    });
  }

  /* ---------- opening slideshow ------------------------------------- */

  var viewer = document.querySelector("[data-viewer]");
  if (viewer) {
    var slides = [].slice.call(viewer.querySelectorAll(".viewer__slide"));
    var ticks = [].slice.call(viewer.querySelectorAll(".viewer__tick"));
    var pause = viewer.querySelector("[data-viewer-pause]");
    var caption = viewer.querySelector("[data-viewer-caption]");
    var number = viewer.querySelector("[data-viewer-number]");
    var i = 0;
    var timer = null;

    function paint(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle("is-active", k === i); });
      ticks.forEach(function (t, k) { t.classList.toggle("is-active", k === i); });
      if (caption) caption.textContent = slides[i].getAttribute("alt");
      if (number) {
        number.textContent = "Plate " + String(i + 1).padStart(2, "0") +
          " / " + String(slides.length).padStart(2, "0");
      }
    }

    function play() {
      stop();
      timer = setInterval(function () { paint(i + 1); }, 4000);
      if (pause) pause.textContent = "Pause";
    }

    function stop() {
      if (timer) { clearInterval(timer); timer = null; }
      if (pause) pause.textContent = "Play";
    }

    ticks.forEach(function (t, k) {
      t.addEventListener("click", function () { paint(k); stop(); });
    });
    if (pause) {
      pause.addEventListener("click", function () { timer ? stop() : play(); });
    }
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) { stop(); } else if (!reduceMotion) { play(); }
    });

    paint(0);
    if (!reduceMotion) play();
  }

  /* ---------- plate lightbox ---------------------------------------- */

  var box = document.querySelector("[data-lightbox]");
  var plates = [].slice.call(document.querySelectorAll("[data-plate]"));
  if (box && plates.length) {
    var boxImg = box.querySelector("[data-lightbox-image]");
    var boxTitle = box.querySelector("[data-lightbox-title]");
    var boxSubject = box.querySelector("[data-lightbox-subject]");
    var boxNumber = box.querySelector("[data-lightbox-number]");
    var at = 0;
    var lastFocus = null;

    function open(n) {
      at = (n + plates.length) % plates.length;
      var p = plates[at];
      boxImg.src = p.dataset.full;
      boxImg.alt = p.dataset.title + " — " + p.dataset.subject;
      boxTitle.textContent = p.dataset.title;
      boxSubject.textContent = p.dataset.subject;
      boxNumber.textContent = "Plate " + p.dataset.number;
      box.classList.add("is-open");
      document.body.style.overflow = "hidden";
      box.querySelector("[data-lightbox-close]").focus();
    }

    function close() {
      box.classList.remove("is-open");
      document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    }

    plates.forEach(function (p, n) {
      p.addEventListener("click", function () { lastFocus = p; open(n); });
    });

    box.querySelector("[data-lightbox-close]").addEventListener("click", close);
    box.querySelector("[data-lightbox-prev]").addEventListener("click", function () { open(at - 1); });
    box.querySelector("[data-lightbox-next]").addEventListener("click", function () { open(at + 1); });
    box.addEventListener("click", function (e) { if (e.target === box) close(); });

    document.addEventListener("keydown", function (e) {
      if (!box.classList.contains("is-open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") open(at - 1);
      if (e.key === "ArrowRight") open(at + 1);
    });
  }
})();
