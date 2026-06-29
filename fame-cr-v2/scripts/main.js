/* FAME CRYPT — etkileşimler */
(function () {
  "use strict";

  /* ---- Mobil menü ---------------------------------------------------- */
  const toggle = document.querySelector(".nav__toggle");
  const menu = document.getElementById("navMenu");
  if (toggle && menu) {
    toggle.addEventListener("click", () => {
      const open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    menu.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      })
    );
  }

  /* ---- Header scroll durumu ------------------------------------------ */
  const header = document.querySelector(".site-header");
  if (header) {
    const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- Reveal-on-scroll ---------------------------------------------- */
  const reveals = document.querySelectorAll(".reveal");
  if (reveals.length && "IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("is-visible");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("is-visible"));
  }

  /* ---- Marquee'leri kusursuz döngü için klonla ----------------------- */
  document.querySelectorAll(".marquee__track").forEach((track) => {
    track.innerHTML += track.innerHTML;
  });

  /* ---- Müfredat kartları (akordeon) ---------------------------------- */
  document.querySelectorAll(".edu-card__header").forEach((btn) => {
    btn.addEventListener("click", () => {
      const card = btn.closest(".edu-card");
      const open = card.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", String(open));
    });
  });

  /* ---- CV bırakma kutusu --------------------------------------------- */
  const dz = document.querySelector(".cv-dropzone");
  const fileInput = document.getElementById("cvInput");
  if (dz && fileInput) {
    const label = dz.querySelector("[data-cv-label]");
    dz.addEventListener("click", () => fileInput.click());
    dz.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        fileInput.click();
      }
    });
    ["dragover", "dragenter"].forEach((ev) =>
      dz.addEventListener(ev, (e) => {
        e.preventDefault();
        dz.classList.add("is-drag");
      })
    );
    ["dragleave", "drop"].forEach((ev) =>
      dz.addEventListener(ev, (e) => {
        e.preventDefault();
        dz.classList.remove("is-drag");
      })
    );
    const showName = (name) => {
      if (label) label.textContent = name;
    };
    dz.addEventListener("drop", (e) => {
      const f = e.dataTransfer.files[0];
      if (f) {
        fileInput.files = e.dataTransfer.files;
        showName(f.name);
      }
    });
    fileInput.addEventListener("change", () => {
      if (fileInput.files[0]) showName(fileInput.files[0].name);
    });
  }
})();
