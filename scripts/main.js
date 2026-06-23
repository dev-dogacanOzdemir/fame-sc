/* FAME CRYPT — main.js
   Marquee'leri kesintisiz döngü için klonlar ve mobil menüyü yönetir. */

/** Alt klasördeki sayfalar (pages/) için görsel yolunu "../" ile düzeltir. */
const ASSET_BASE = window.location.pathname.includes("/pages/") ? "../" : "";

/** PARTNERS listesinden marquee <li>'leri üretir. Görsel varsa <img>, yoksa metin. */
function renderPartners(trackId) {
  const track = document.getElementById(trackId);
  if (!track || typeof PARTNERS === "undefined") return;

  track.innerHTML = PARTNERS.map((p) => {
    const style = p.scale ? ` style="--logo-scale:${p.scale}"` : "";
    const inner = p.file
      ? `<img src="${ASSET_BASE}assets/images/partners/${p.file}" alt="${p.name}" loading="lazy" />`
      : `<span>${p.name}</span>`;
    return `<li class="partner-logo" title="${p.name}"${style}>${inner}</li>`;
  }).join("");
}

/** PARTNERS listesinden grid hücreleri üretir (Kurumsal sayfası). */
function renderPartnerGrid(gridId) {
  const grid = document.getElementById(gridId);
  if (!grid || typeof PARTNERS === "undefined") return;

  grid.innerHTML = PARTNERS.map((p) => {
    if (p.file) {
      return `<div class="partner-cell" title="${p.name}">
        <img src="${ASSET_BASE}assets/images/partners/${p.file}" alt="${p.name}" loading="lazy" />
        <span class="partner-cell__name">${p.name}</span>
      </div>`;
    }
    return `<div class="partner-cell partner-cell--text" title="${p.name}">${p.name}</div>`;
  }).join("");
}

/** Track içeriğini ikiye katlar → -50% kaydırmada dikişsiz döngü. */
function setupMarquee(trackId) {
  const track = document.getElementById(trackId);
  if (!track) return;
  const items = Array.from(track.children);
  items.forEach((item) => track.appendChild(item.cloneNode(true)));
}

/** Görünür alana giren .reveal öğelerine .is-visible ekler (tek seferlik). */
function setupReveal() {
  const items = document.querySelectorAll(".reveal");
  if (!items.length) return;

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) {
    items.forEach((el) => el.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  items.forEach((el) => observer.observe(el));
}

document.addEventListener("DOMContentLoaded", () => {
  renderPartners("partners-track");
  renderPartnerGrid("partner-grid");
  setupMarquee("partners-track");
  setupMarquee("staff-track");
  setupReveal();

  // Mobil menü aç/kapa
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".nav");
  toggle?.addEventListener("click", () => {
    if (!nav) return;
    const open = !nav.classList.contains("is-open");
    nav.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", String(open));
  });
});
