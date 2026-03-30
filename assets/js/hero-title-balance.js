import {
  layoutWithLines,
  prepareWithSegments,
} from "https://cdn.jsdelivr.net/npm/@chenglou/pretext@0.0.3/dist/layout.js";

(function () {
  const title = document.querySelector("[data-hero-balanced-title]");
  if (!title) {
    return;
  }

  const rawText = (title.textContent || "").trim();
  if (!rawText) {
    return;
  }

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let prepared = null;
  let lastSignature = "";
  let rafId = 0;

  title.dataset.rawText = rawText;
  title.setAttribute("aria-label", rawText);

  function toCanvasFont(style) {
    const parts = [
      style.fontStyle,
      style.fontVariant,
      style.fontWeight,
      style.fontStretch,
      style.fontSize,
      style.fontFamily,
    ].filter(Boolean);

    return parts.join(" ");
  }

  function parseLineHeight(style) {
    const lineHeight = parseFloat(style.lineHeight);
    const fontSize = parseFloat(style.fontSize);

    if (Number.isFinite(lineHeight)) {
      return lineHeight;
    }

    return fontSize * 0.95;
  }

  function lineWordCount(text) {
    return text.trim().split(/\s+/).filter(Boolean).length;
  }

  function scoreCandidate(lines, containerWidth) {
    if (!lines.length) {
      return Number.POSITIVE_INFINITY;
    }

    const widths = lines.map(function (line) {
      return line.width;
    });
    const widest = Math.max.apply(null, widths);
    const average = widths.reduce(function (sum, width) {
      return sum + width;
    }, 0) / widths.length;
    const raggedness = widths.reduce(function (sum, width) {
      return sum + Math.pow(average - width, 2);
    }, 0);
    const lastWidth = widths[widths.length - 1];
    const lineCountPenalty = Math.abs(lines.length - 4) * 220;
    const widthPenalty = (containerWidth - widest) * 0.45;
    const orphanPenalty = lastWidth < widest * 0.58 ? Math.pow((widest * 0.58) - lastWidth, 2) * 0.16 : 0;
    const singleWordPenalty = lineWordCount(lines[lines.length - 1].text) <= 1 ? 900 : 0;

    return raggedness + lineCountPenalty + widthPenalty + orphanPenalty + singleWordPenalty;
  }

  function renderLines(lines) {
    const fragment = document.createDocumentFragment();

    lines.forEach(function (line, index) {
      const item = document.createElement("span");
      item.className = "hero__title-line";
      item.style.setProperty("--hero-line-index", String(index));
      item.textContent = line.text.replace(/\s+$/u, "");
      fragment.appendChild(item);
    });

    title.replaceChildren(fragment);
    title.classList.add("hero__title--balanced");

    if (reduceMotion.matches) {
      title.classList.add("hero__title--motionless");
    } else {
      title.classList.remove("hero__title--motionless");
    }
  }

  function chooseLayout(containerWidth, lineHeight) {
    const baseline = layoutWithLines(prepared, containerWidth, lineHeight);
    let bestLines = baseline.lines;
    let bestScore = scoreCandidate(bestLines, containerWidth);
    const minWidth = Math.max(containerWidth * 0.68, 220);
    const steps = containerWidth < 420 ? 12 : 18;

    for (let step = 0; step <= steps; step += 1) {
      const width = minWidth + ((containerWidth - minWidth) * step) / steps;
      const candidate = layoutWithLines(prepared, width, lineHeight);

      if (candidate.lineCount < 2 || candidate.lineCount > 6) {
        continue;
      }

      if (candidate.lineCount > baseline.lineCount + 1) {
        continue;
      }

      const score = scoreCandidate(candidate.lines, containerWidth);
      if (score + 1 < bestScore) {
        bestLines = candidate.lines;
        bestScore = score;
      }
    }

    return bestLines;
  }

  function balanceTitle() {
    const style = window.getComputedStyle(title);
    const containerWidth = title.clientWidth;

    if (!containerWidth) {
      return;
    }

    const font = toCanvasFont(style);
    const signature = [font, rawText].join("||");
    if (signature !== lastSignature) {
      prepared = prepareWithSegments(rawText, font);
      lastSignature = signature;
    }

    const lineHeight = parseLineHeight(style);
    const lines = chooseLayout(containerWidth, lineHeight);
    renderLines(lines);
  }

  function scheduleBalance() {
    window.cancelAnimationFrame(rafId);
    rafId = window.requestAnimationFrame(balanceTitle);
  }

  document.documentElement.classList.add("has-pretext-hero");

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(scheduleBalance);
  } else {
    scheduleBalance();
  }

  window.addEventListener("resize", scheduleBalance, { passive: true });

  if (window.ResizeObserver) {
    const observer = new ResizeObserver(scheduleBalance);
    observer.observe(title);
  }
})();
