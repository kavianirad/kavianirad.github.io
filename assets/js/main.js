// Theme toggle, mobile menu, BibTeX toggles and publication filters.
(function () {
  var root = document.documentElement;

  function storedTheme() {
    try { return localStorage.getItem("theme"); } catch (e) { return null; }
  }
  function currentTheme() {
    var t = root.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function paintIcon() {
    var btn = document.getElementById("theme-toggle");
    if (!btn) return;
    var dark = currentTheme() === "dark";
    btn.innerHTML = dark ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
    btn.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  }

  var saved = storedTheme();
  if (saved) root.setAttribute("data-theme", saved);

  document.addEventListener("DOMContentLoaded", function () {
    paintIcon();

    var themeBtn = document.getElementById("theme-toggle");
    if (themeBtn) themeBtn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
      paintIcon();
    });

    var menuBtn = document.getElementById("menu-toggle");
    var links = document.getElementById("nav-links");
    if (menuBtn && links) menuBtn.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });

    document.querySelectorAll("[data-bib]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var el = document.getElementById(btn.getAttribute("data-bib"));
        if (el) el.classList.toggle("open");
      });
    });

    // Publication filters: type (journal, conference, ...) and period (PhD / M.Sc.).
    var state = { type: "all", era: "all", q: "" };
    var eraToggle = document.querySelector(".era-toggle");
    if (eraToggle) state.era = "phd";  // homepage: PhD papers by default
    function applyFilters() {
      document.querySelectorAll(".pub").forEach(function (p) {
        var text = p.getAttribute("data-search") || (p.textContent + " " + (p.closest(".pub-group") ? p.closest(".pub-group").querySelector(".pub-year").textContent : "")).toLowerCase();
        p.setAttribute("data-search", text);
        p.hidden = !((state.type === "all" || p.getAttribute("data-type") === state.type) &&
                     (state.era === "all" || p.getAttribute("data-era") === state.era) &&
                     state.q.split(/\s+/).every(function (w) { return !w || text.indexOf(w) !== -1; }));
      });
      document.querySelectorAll(".pub-group").forEach(function (g) {
        g.hidden = !g.querySelector(".pub:not([hidden])");
      });
      var empty = document.querySelector(".no-pubs");
      if (empty) empty.hidden = !!document.querySelector(".pub:not([hidden])");
      var count = document.getElementById("pub-count");
      if (count) {
        var shown = document.querySelectorAll(".pub:not([hidden])").length, total = document.querySelectorAll(".pub").length;
        count.textContent = shown === total ? "" : "Showing " + shown + " of " + total + " publications";
      }
    }
    function wire(selector, attr, key) {
      var btns = document.querySelectorAll(selector);
      btns.forEach(function (btn) {
        btn.addEventListener("click", function () {
          state[key] = btn.getAttribute(attr);
          btns.forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
          applyFilters();
        });
      });
    }
    wire("[data-filter]", "data-filter", "type");
    wire("[data-era-filter]", "data-era-filter", "era");
    var search = document.getElementById("pub-search");
    if (search) {
      var initial = new URLSearchParams(location.search).get("q");
      if (initial) { search.value = initial; state.q = initial.toLowerCase().trim(); }
      search.addEventListener("input", function () { state.q = search.value.toLowerCase().trim(); applyFilters(); });
    }
    if (document.querySelector(".pub")) applyFilters();

    var toTop = document.getElementById("to-top");
    if (toTop) {
      var onScroll = function () { toTop.hidden = window.scrollY < 600; };
      window.addEventListener("scroll", onScroll, { passive: true });
      onScroll();
      toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
    }

    var copyBtn = document.getElementById("copy-bio");
    if (copyBtn) copyBtn.addEventListener("click", function () {
      var text = document.querySelector(".bio").textContent.trim();
      var done = function () { copyBtn.textContent = "Copied"; setTimeout(function () { copyBtn.textContent = "Copy bio"; }, 1500); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
    });

    document.querySelectorAll(".cite-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var text = btn.getAttribute("data-cite");
        var done = function () { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = "Cite"; }, 1500); };
        if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () { window.prompt("Copy citation:", text); });
        else window.prompt("Copy citation:", text);
      });
    });

    // Google Scholar citation counts, refreshed daily by a GitHub Action.
    var badges = document.querySelectorAll(".scholar-badge");
    if (badges.length && window.fetch) {
      fetch("https://raw.githubusercontent.com/kavianirad/kavianirad.github.io/google-scholar-stats/gs_data.json", { cache: "no-cache" })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (data) {
          var pubs = data.publications || {};
          var google = data.source !== "semantic_scholar";
          badges.forEach(function (b) {
            var p = pubs[b.getAttribute("data-title")];
            if (!p) return;
            var n = b.querySelector(".sb-n");
            n.textContent = p.citations;
            n.hidden = false;
            if (p.url) b.href = p.url;
            if (!google) {
              b.title = "Citations (Semantic Scholar)";
              b.querySelector(".sb-l").innerHTML = '<i class="fa-solid fa-quote-right"></i> cited';
            }
          });
          if (google) document.querySelectorAll("[data-stat]").forEach(function (el) {
            var v = data[el.getAttribute("data-stat")];
            if (v) el.textContent = v;
          });
          var u = document.getElementById("scholar-updated");
          if (u && data.updated) u.textContent = google ? " (as of " + data.updated + ")"
            : "; per-paper citation counts from Semantic Scholar, updated daily (last update " + data.updated + ")";
        })
        .catch(function () {});
    }

    var y = document.getElementById("year");
    if (y) y.textContent = new Date().getFullYear();
  });
})();
