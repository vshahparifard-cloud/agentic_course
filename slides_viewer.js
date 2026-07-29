/**
 * Interactive Presentation & Slide Viewer JS
 * Agentic AI Course Hub (2026)
 */

(function () {
    const slideManifest = {
        session_1: {
            title: "جلسه اول: اکوسیستم جمنای، کلود و مدل‌های هوش مصنوعی",
            slides: Array.from({ length: 33 }, (_, i) => `slides/session_1/slide_${i + 1}.png`),
            pdf: "جلسه اول_ اکوسیستم جمنای و مدل_های هوش مصنوعی (آپدیت ۲۰۲۶).pdf"
        },
        session_2: {
            title: "جلسه دوم: تسلط همه‌جانبه بر Google Antigravity",
            slides: Array.from({ length: 18 }, (_, i) => `slides/session_2/slide_${i + 1}.png`),
            pdf: "جلسه دوم_ تسلط بر Google Antigravity (آپدیت ۲۰۲۶).pdf"
        },
        session_3: {
            title: "جلسه سوم: معماری RAG و حافظه ایجنت‌ها",
            slides: Array.from({ length: 13 }, (_, i) => `slides/session_3/slide_${i + 1}.png`),
            pdf: "جلسه سوم_ تسلط بر RAG و سیستم_های آگاه به زمینه.pdf"
        },
        session_4: {
            title: "جلسه چهارم: ارکستراسیون پیشرفته ایجنت‌ها و Observability",
            slides: Array.from({ length: 19 }, (_, i) => `slides/session_4/slide_${i + 1}.png`),
            pdf: "جلسه چهارم_ مهندسی پیشرفته ایجنت_ها و Observability (1).pdf"
        }
    };

    let currentSessionKey = null;
    let currentSlideIndex = 0;
    let touchStartX = 0;
    let touchEndX = 0;

    // DOM Elements
    const modal = document.getElementById("slideModal");
    const modalTitle = document.getElementById("modalSessionTitle");
    const slideImg = document.getElementById("currentSlideImage");
    const slideCounter = document.getElementById("slideCounterText");
    const progressBarInner = document.getElementById("slideProgressBarInner");
    const thumbnailsContainer = document.getElementById("slideThumbnails");
    const btnPrev = document.getElementById("btnPrevSlide");
    const btnNext = document.getElementById("btnNextSlide");
    const btnClose = document.getElementById("btnCloseModal");
    const btnFullscreen = document.getElementById("btnToggleFullscreen");
    const btnDownloadPdf = document.getElementById("btnDownloadPdf");

    // Initialize slide viewer
    function init() {
        if (!modal) return;

        // Button clicks
        btnClose?.addEventListener("click", closeViewer);
        btnPrev?.addEventListener("click", prevSlide);
        btnNext?.addEventListener("click", nextSlide);
        btnFullscreen?.addEventListener("click", toggleFullscreen);

        // Keyboard navigation
        document.addEventListener("keydown", handleKeyDown);

        // Touch events for mobile swipe
        const viewport = document.querySelector(".slide-viewport");
        if (viewport) {
            viewport.addEventListener("touchstart", (e) => {
                touchStartX = e.changedTouches[0].screenX;
            }, { passive: true });

            viewport.addEventListener("touchend", (e) => {
                touchEndX = e.changedTouches[0].screenX;
                handleSwipe();
            }, { passive: true });
        }

        // Close modal on background overlay click
        modal.addEventListener("click", (e) => {
            if (e.target === modal) closeViewer();
        });
    }

    window.openSlideViewer = function (sessionKey) {
        if (!slideManifest[sessionKey]) return;
        currentSessionKey = sessionKey;
        currentSlideIndex = 0;

        const data = slideManifest[sessionKey];
        if (modalTitle) modalTitle.textContent = data.title;
        if (btnDownloadPdf) btnDownloadPdf.href = data.pdf;

        renderThumbnails();
        updateSlideView();

        modal.classList.add("active");
        document.body.style.overflow = "hidden";
    };

    function closeViewer() {
        if (!modal) return;
        modal.classList.remove("active");
        document.body.style.overflow = "";
        if (document.fullscreenElement) {
            document.exitFullscreen().catch(() => {});
        }
    }

    function updateSlideView() {
        if (!currentSessionKey) return;
        const slides = slideManifest[currentSessionKey].slides;
        const total = slides.length;

        // Ensure index in bounds
        if (currentSlideIndex < 0) currentSlideIndex = 0;
        if (currentSlideIndex >= total) currentSlideIndex = total - 1;

        // Update image with smooth fade
        slideImg.style.opacity = "0.3";
        const newSrc = slides[currentSlideIndex];
        
        const tempImg = new Image();
        tempImg.src = newSrc;
        tempImg.onload = () => {
            slideImg.src = newSrc;
            slideImg.style.opacity = "1";
        };
        tempImg.onerror = () => {
            slideImg.src = newSrc;
            slideImg.style.opacity = "1";
        };

        // Preload next image
        if (currentSlideIndex + 1 < total) {
            const nextPreload = new Image();
            nextPreload.src = slides[currentSlideIndex + 1];
        }

        // Counter text
        if (slideCounter) {
            slideCounter.textContent = `اسلاید ${currentSlideIndex + 1} از ${total}`;
        }

        // Progress bar percentage
        if (progressBarInner) {
            const pct = ((currentSlideIndex + 1) / total) * 100;
            progressBarInner.style.width = `${pct}%`;
        }

        // Update active thumbnail
        const thumbs = thumbnailsContainer.querySelectorAll(".thumb-item");
        thumbs.forEach((t, idx) => {
            if (idx === currentSlideIndex) {
                t.classList.add("active");
                t.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
            } else {
                t.classList.remove("active");
            }
        });

        // Update button disabled state
        if (btnPrev) btnPrev.disabled = currentSlideIndex === 0;
        if (btnNext) btnNext.disabled = currentSlideIndex === total - 1;
    }

    function renderThumbnails() {
        if (!thumbnailsContainer || !currentSessionKey) return;
        thumbnailsContainer.innerHTML = "";
        const slides = slideManifest[currentSessionKey].slides;

        slides.forEach((src, idx) => {
            const thumb = document.createElement("div");
            thumb.className = `thumb-item ${idx === 0 ? "active" : ""}`;
            thumb.innerHTML = `
                <img src="${src}" alt="اسلاید ${idx + 1}" loading="lazy">
                <span class="thumb-num">${idx + 1}</span>
            `;
            thumb.addEventListener("click", () => {
                currentSlideIndex = idx;
                updateSlideView();
            });
            thumbnailsContainer.appendChild(thumb);
        });
    }

    function nextSlide() {
        if (!currentSessionKey) return;
        const total = slideManifest[currentSessionKey].slides.length;
        if (currentSlideIndex < total - 1) {
            currentSlideIndex++;
            updateSlideView();
        }
    }

    function prevSlide() {
        if (currentSlideIndex > 0) {
            currentSlideIndex--;
            updateSlideView();
        }
    }

    function toggleFullscreen() {
        if (!document.fullscreenElement) {
            modal.requestFullscreen().catch(err => {
                console.error("Error attempting fullscreen:", err);
            });
        } else {
            document.exitFullscreen().catch(() => {});
        }
    }

    function handleSwipe() {
        const threshold = 50;
        if (touchEndX < touchStartX - threshold) {
            // Swipe Left -> Next Slide (or Prev depending on RTL)
            nextSlide();
        }
        if (touchEndX > touchStartX + threshold) {
            // Swipe Right -> Prev Slide
            prevSlide();
        }
    }

    function handleKeyDown(e) {
        if (!modal.classList.contains("active")) return;

        switch (e.key) {
            case "ArrowLeft":
            case "PageDown":
                nextSlide();
                break;
            case "ArrowRight":
            case "PageUp":
                prevSlide();
                break;
            case " ":
                e.preventDefault();
                nextSlide();
                break;
            case "Escape":
                closeViewer();
                break;
            case "f":
            case "F":
                toggleFullscreen();
                break;
        }
    }

    document.addEventListener("DOMContentLoaded", init);
})();
