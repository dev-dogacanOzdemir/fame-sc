/* FAME CRYPT — etkileşimler */
(function () {
  "use strict";

  /* ---- Mobil menü ---------------------------------------------------- */
  const toggle = document.querySelector(".nav__toggle");
  const menu = document.getElementById("navMenu");
  if (toggle && menu) {
    const dropdownLinks = menu.querySelectorAll(".nav__link--dropdown");
    const isMobileNav = () => window.matchMedia("(max-width: 940px)").matches;

    toggle.addEventListener("click", () => {
      const open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });

    dropdownLinks.forEach((link) => {
      link.setAttribute("aria-haspopup", "true");
      link.setAttribute("aria-expanded", "false");
      link.addEventListener("click", (e) => {
        if (!isMobileNav()) return;
        e.preventDefault();
        const item = link.closest(".nav__item--has-dropdown");
        const open = item.classList.toggle("is-open");
        link.setAttribute("aria-expanded", String(open));
      });
    });

    menu.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", (e) => {
        if (a.classList.contains("nav__link--dropdown") && isMobileNav()) return;
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        menu.querySelectorAll(".nav__item--has-dropdown.is-open").forEach((item) => {
          item.classList.remove("is-open");
          item.querySelector(".nav__link--dropdown")?.setAttribute("aria-expanded", "false");
        });
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

  /* ---- Sponsorluk afişleri: tıklayınca büyüt ------------------------- */
  const sponsorCards = document.querySelectorAll(".sponsor-card");
  if (sponsorCards.length) {
    const lightbox = document.createElement("div");
    lightbox.className = "sponsor-lightbox";
    lightbox.setAttribute("role", "dialog");
    lightbox.setAttribute("aria-modal", "true");
    lightbox.setAttribute("aria-label", "Etkinlik görseli");
    lightbox.innerHTML = `
      <div class="sponsor-lightbox__frame">
        <button class="sponsor-lightbox__close" type="button" aria-label="Kapat">×</button>
        <img class="sponsor-lightbox__image" alt="" />
      </div>
    `;
    document.body.appendChild(lightbox);

    const lightboxImage = lightbox.querySelector(".sponsor-lightbox__image");
    const closeButton = lightbox.querySelector(".sponsor-lightbox__close");
    let previousFocus = null;

    const closeLightbox = () => {
      lightbox.classList.remove("is-open");
      document.body.classList.remove("is-lightbox-open");
      if (previousFocus) previousFocus.focus();
    };

    sponsorCards.forEach((card) => {
      card.setAttribute("tabindex", "0");
      card.setAttribute("aria-label", "Etkinlik görselini büyüt");
      const openLightbox = () => {
        const img = card.querySelector("img");
        if (!img || !lightboxImage) return;
        previousFocus = card;
        lightboxImage.src = img.currentSrc || img.src;
        lightboxImage.alt = img.alt;
        lightbox.classList.add("is-open");
        document.body.classList.add("is-lightbox-open");
        closeButton.focus();
      };
      card.addEventListener("click", openLightbox);
      card.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openLightbox();
        }
      });
    });

    closeButton.addEventListener("click", closeLightbox);
    lightbox.addEventListener("click", (e) => {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && lightbox.classList.contains("is-open")) closeLightbox();
    });
  }

  /* ---- Müfredat kartları: sol liste + sağ detay paneli ---------------- */
  const eduHeaders = document.querySelectorAll(".edu-card__header");
  if (eduHeaders.length) {
    const grid = document.querySelector(".curriculum-grid");
    const detail = document.createElement("aside");
    detail.className = "edu-detail-panel";
    detail.setAttribute("aria-live", "polite");
    detail.innerHTML = `
        <div class="edu-detail__header">
          <span class="edu-detail__icon" aria-hidden="true"></span>
          <div>
            <p class="edu-detail__eyebrow">Seçili eğitim</p>
            <h3 class="edu-detail__title"></h3>
            <p class="edu-detail__summary"></p>
          </div>
        </div>
        <div class="edu-detail__content"></div>
    `;
    grid.appendChild(detail);

    const detailIcon = detail.querySelector(".edu-detail__icon");
    const detailTitle = detail.querySelector(".edu-detail__title");
    const detailSummary = detail.querySelector(".edu-detail__summary");
    const detailContent = detail.querySelector(".edu-detail__content");

    const selectEduCard = (card) => {
      const content = card.querySelector(".edu-card__content");
      const title = card.querySelector(".edu-card__title")?.textContent.trim() || "";
      const summary = card.querySelector(".edu-card__summary")?.textContent.trim() || "";
      const icon = card.querySelector(".edu-card__icon")?.textContent.trim() || "";
      if (!content) return;

      document.querySelectorAll(".edu-card.is-open").forEach((openCard) => {
        openCard.classList.remove("is-open");
        openCard.querySelector(".edu-card__header")?.setAttribute("aria-expanded", "false");
        openCard.querySelector(".edu-card__header")?.setAttribute("aria-pressed", "false");
      });

      card.classList.add("is-open");
      card.querySelector(".edu-card__header")?.setAttribute("aria-expanded", "true");
      card.querySelector(".edu-card__header")?.setAttribute("aria-pressed", "true");
      detailIcon.textContent = icon;
      detailTitle.textContent = title;
      detailSummary.textContent = summary;
      detailContent.innerHTML = content.outerHTML;
      detail.classList.remove("is-ready");
      requestAnimationFrame(() => detail.classList.add("is-ready"));
    };

    eduHeaders.forEach((btn) => {
      btn.setAttribute("aria-pressed", "false");
      btn.addEventListener("click", () => {
        selectEduCard(btn.closest(".edu-card"));
      });
    });

    selectEduCard(eduHeaders[0].closest(".edu-card"));
  }

  /* ---- Ürün vitrin sekmeleri (Yönetici Paneli / Çalışma Modları) ----- */
  document.querySelectorAll(".ps-tabs").forEach((tabs) => {
    tabs.querySelectorAll(".ps-tab").forEach((tab) => {
      tab.addEventListener("click", () => {
        const idx = tab.dataset.tab;
        const scope = tabs.parentElement;
        tabs.querySelectorAll(".ps-tab").forEach((t) => {
          t.classList.remove("is-active");
          t.setAttribute("aria-selected", "false");
        });
        scope.querySelectorAll(".ps-panel").forEach((p) => p.classList.remove("is-active"));
        tab.classList.add("is-active");
        tab.setAttribute("aria-selected", "true");
        const panel = scope.querySelector(`.ps-panel[data-panel="${idx}"]`);
        if (panel) panel.classList.add("is-active");
      });
    });
  });

  /* ---- Kariyer mail şablonu ve başvuru formu ------------------------- */
  const careerForm = document.querySelector("[data-career-form]");
  const kvkkConsent = document.getElementById("kvkkConsent");
  const applicationDownload = document.getElementById("applicationFormDownload");
  const formDownloadNote = document.querySelector("[data-form-download-note]");

  if (careerForm) {
    careerForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const firstName = document.getElementById("careerFirstName")?.value.trim() || "Ad";
      const lastName = document.getElementById("careerLastName")?.value.trim() || "Soyad";
      const fullName = `${firstName} ${lastName}`.trim();
      const subject = `${fullName} - İş Başvurusu`;
      const body = `Merhaba,\n\nFAME CRYPT bünyesindeki uygun pozisyonlar için iş başvurumu iletiyorum.\n\nCV dosyamı ve doldurulmuş iş başvuru formunu e-posta ekinde paylaşıyorum.\n\nBilgilerinize sunarım.\n\nSaygılarımla,\n${fullName}`;
      window.location.href = `mailto:info@famecrypt.com.tr?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });
  }

  if (kvkkConsent && applicationDownload) {
    const syncDownloadState = () => {
      const enabled = kvkkConsent.checked;
      applicationDownload.classList.toggle("is-disabled", !enabled);
      applicationDownload.setAttribute("aria-disabled", String(!enabled));
      if (formDownloadNote) {
        formDownloadNote.textContent = enabled
          ? "KVKK onayı alındı. Formu indirebilirsiniz."
          : "Formu indirmek için KVKK onayı gereklidir.";
      }
    };

    kvkkConsent.addEventListener("change", syncDownloadState);
    applicationDownload.addEventListener("click", (e) => {
      if (!kvkkConsent.checked) {
        e.preventDefault();
        kvkkConsent.focus();
        if (formDownloadNote) formDownloadNote.textContent = "Lütfen indirmeden önce KVKK onayını işaretleyin.";
      }
    });
    syncDownloadState();
  }
})();
