/* ---- recipe: app-bar ---- */
(function () {
  var bars = document.querySelectorAll('.r-appbar:not(.r-appbar--overlay)');
  function sync() { bars.forEach(function (b) { if (window.scrollY > 4) b.dataset.scrolled = ''; else if (!b.hasAttribute('data-static')) b.removeAttribute('data-scrolled'); }); }
  window.addEventListener('scroll', sync, { passive: true });
})();

/* ---- recipe: sheet ---- */
document.querySelectorAll('[data-open]').forEach(function (b) {
  if (b.dataset.bound) return; b.dataset.bound = '1';
  b.addEventListener('click', function () { var d = document.getElementById(b.dataset.open); d && (d.showModal ? d.showModal() : d.setAttribute('open', '')); });
});
document.querySelectorAll('dialog.r-sheet').forEach(function (d) {
  d.addEventListener('click', function (e) { if (e.target === d || e.target.closest('[data-close]')) d.close(); });
});

/* ---- recipe: chip-group ---- */
document.querySelectorAll('.r-chip[aria-pressed]').forEach(function (c) {
  c.addEventListener('click', function () { c.setAttribute('aria-pressed', String(c.getAttribute('aria-pressed') !== 'true')); });
});

/* ---- recipe: photo-card ---- */
document.querySelectorAll('.r-photo__save').forEach(function (b) {
  b.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); b.setAttribute('aria-pressed', String(b.getAttribute('aria-pressed') !== 'true')); });
});

/* ---- recipe: toast ---- */
(function () {
  var region = document.querySelector('.r-toast-region');
  window.rToast = function (text, actionLabel) {
    var t = document.createElement('div'); t.className = 'r-toast';
    t.innerHTML = '<span class="r-ico r-ico-sm i-check" aria-hidden="true"></span><span class="r-toast__text"></span>' + (actionLabel ? '<button class="r-toast__action"></button>' : '');
    t.querySelector('.r-toast__text').textContent = text;
    if (actionLabel) t.querySelector('.r-toast__action').textContent = actionLabel;
    region.appendChild(t);
    setTimeout(function () { t.dataset.leaving = '1'; setTimeout(function () { t.remove(); }, 200); }, 3000);
  };
  document.querySelectorAll('[data-toast]').forEach(function (b) { b.addEventListener('click', function () { rToast(b.dataset.toast, '撤销'); }); });
})();
