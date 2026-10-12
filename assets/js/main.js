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

    var filterBtns = document.querySelectorAll(".filters button");
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var f = btn.getAttribute("data-filter");
        filterBtns.forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
        document.querySelectorAll(".pub").forEach(function (p) {
          p.hidden = !(f === "all" || p.getAttribute("data-type") === f);
        });
        document.querySelectorAll(".pub-group").forEach(function (g) {
          g.hidden = !g.querySelector(".pub:not([hidden])");
        });
      });
    });

    var copyBtn = document.getElementById("copy-bio");
    if (copyBtn) copyBtn.addEventListener("click", function () {
      var text = document.querySelector(".bio").textContent.trim();
      var done = function () { copyBtn.textContent = "Copied"; setTimeout(function () { copyBtn.textContent = "Copy bio"; }, 1500); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
    });

    var y = document.getElementById("year");
    if (y) y.textContent = new Date().getFullYear();
  });
})();
