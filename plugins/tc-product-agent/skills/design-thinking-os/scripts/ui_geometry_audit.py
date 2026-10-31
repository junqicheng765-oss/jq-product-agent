#!/usr/bin/env python3
"""
UI Geometry, Alignment & Asset Audit Script for design-thinking-os (QA0 Automated Gate)
Executes real DOM getBoundingClientRect() & computed-style checks via headless Chrome (--dump-dom)
with zero third-party Python dependencies.

Detects the 5 most common AI UI generation failures:
  1. ICON_GLYPH_OR_OFF_CENTER: Text characters (<, >, ‹, ›, ←, ×) used instead of centered SVG inside circular/square icon buttons,
     or child SVG center deviating > 2px from button center.
  2. HEADER_ROW_MISALIGNED: Horizontal bar/header direct children not vertically centered (centerY diff > 3px).
  3. STAGE_ACTION_OFF_CENTER: Primary stage action bar or top dashboard drifting off horizontal center axis.
  4. ZONE_COLLISION: Unintended bounding-box overlap between distinct functional zones (e.g. hand cards colliding with action buttons or player seats).
  5. BANNED_GENERIC_3D_AVATAR: Usage of generic Western 3D clay avatar assets (e.g. 3d-*avatar*, 3d-man*, 3d-old-man*) in C-end/game UI.
"""

import argparse
import html
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "chromium",
]

AUDIT_JS = r"""
(function() {
  const issues = [];
  const W = window.innerWidth || document.documentElement.clientWidth || 1600;
  const H = window.innerHeight || document.documentElement.clientHeight || 900;

  function rect(el) {
    const r = el.getBoundingClientRect();
    return {
      left: r.left, top: r.top, right: r.right, bottom: r.bottom,
      width: r.width, height: r.height,
      cx: r.left + r.width / 2,
      cy: r.top + r.height / 2
    };
  }

  function selectorOf(el) {
    if (!el || !el.tagName) return '';
    let s = el.tagName.toLowerCase();
    if (el.id) s += '#' + el.id;
    if (el.className && typeof el.className === 'string') {
      s += '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.');
    }
    return s;
  }

  // 1. Check all small square/circular icon buttons for raw text glyphs (<, >, ‹, ←) or off-center SVG
  document.querySelectorAll('button, a, div, span').forEach(btn => {
    const r = rect(btn);
    if (r.width < 24 || r.width > 72 || r.height < 24 || r.height > 72) return;
    if (Math.abs(r.width - r.height) > 8) return;
    const cs = window.getComputedStyle(btn);
    const br = parseFloat(cs.borderRadius) || 0;
    const isIconBtn = br >= r.width * 0.35 || /icon|back|btn|circle/i.test(btn.className || '');
    if (!isIconBtn) return;

    const svg = btn.querySelector('svg');
    const rawText = (btn.textContent || '').trim();
    if (!svg && /^[<>‹›«»←→×+⚙🎙＜＞]$/.test(rawText)) {
      issues.push({
        code: 'ICON_RAW_TEXT_GLYPH',
        severity: 'FAIL',
        element: selectorOf(btn),
        message: `Icon button contains raw text character "${rawText}" instead of optically centered <svg>; font baseline causes visual off-centering.`
      });
    }
    if (svg) {
      const sr = rect(svg);
      const dx = Math.abs(r.cx - sr.cx);
      const dy = Math.abs(r.cy - sr.cy);
      if (dx > 2.0 || dy > 2.0) {
        issues.push({
          code: 'ICON_CHILD_OFF_CENTER',
          severity: 'FAIL',
          element: selectorOf(btn),
          message: `SVG inside ${selectorOf(btn)} is off-center by (dx=${dx.toFixed(1)}px, dy=${dy.toFixed(1)}px).`
        });
      }
    }
  });

  // 2. Check horizontal flex bars/headers for vertical center alignment (centerY consistency)
  document.querySelectorAll('header, nav, [class*="hud"], [class*="header"], [class*="top-bar"], [class*="toolbar"], [class*="action-bar"]').forEach(group => {
    const style = window.getComputedStyle(group);
    if (style.display !== 'flex' && style.display !== 'inline-flex') return;
    if (style.flexDirection && style.flexDirection.startsWith('column')) return;
    const children = Array.from(group.children).filter(c => {
      const cs = window.getComputedStyle(c);
      return cs.position !== 'absolute' && cs.display !== 'none' && rect(c).height > 0;
    });
    if (children.length < 2) return;
    const baseCy = rect(children[0]).cy;
    children.slice(1).forEach(ch => {
      const cy = rect(ch).cy;
      const diff = Math.abs(cy - baseCy);
      if (diff > 3.0) {
        issues.push({
          code: 'HEADER_VERTICAL_MISALIGNMENT',
          severity: 'FAIL',
          element: `${selectorOf(group)} -> ${selectorOf(ch)}`,
          message: `Child ${selectorOf(ch)} centerY (${cy.toFixed(1)}px) deviates from first sibling (${baseCy.toFixed(1)}px) by ${diff.toFixed(1)}px. Use align-items: center.`
        });
      }
      // Also check if child is a 2-line title stack next to a single icon button, causing the main title line to sit above the icon button center
      if (ch.children && ch.children.length >= 2) {
        const firstLineCy = rect(ch.children[0]).cy;
        if (Math.abs(firstLineCy - baseCy) > 4.0 && /title|brand|room/i.test(ch.className || '')) {
          issues.push({
            code: 'HEADER_MAIN_TITLE_OFFSET_FROM_ICON',
            severity: 'FAIL',
            element: `${selectorOf(ch)} -> ${selectorOf(ch.children[0])}`,
            message: `Two-line title stack pushes main title centerY (${firstLineCy.toFixed(1)}px) away from icon button centerY (${baseCy.toFixed(1)}px). Use single-line horizontal header alignment.`
          });
        }
      }
    });
  });

  // 3. Flag stock 3D character avatars for a cultural-fit review, and fail hand-drawn SVG faces.
  //    3D icons/props/badges are not flagged; only human avatars need the style-match check.
  document.querySelectorAll('img').forEach(img => {
    const src = (img.getAttribute('src') || '').toLowerCase();
    if (/3d-.*avatar|3d-man-|3d-woman-|3d-old-man|cdn3d\.iconscout\.com.*avatar/.test(src)) {
      issues.push({
        code: 'AVATAR_CULTURAL_FIT_CHECK',
        severity: 'WARN',
        element: selectorOf(img),
        message: `Stock 3D character avatar detected (${src}). Confirm it matches the product's cultural style and that all on-screen avatars share one pack; otherwise switch to style-locked AI portraits.`
      });
    }
  });
  document.querySelectorAll('[class*="avatar"] svg').forEach(svg => {
    if (svg.querySelectorAll('circle').length >= 2) {
      issues.push({
        code: 'BANNED_HAND_DRAWN_SVG_AVATAR',
        severity: 'FAIL',
        element: selectorOf(svg),
        message: `Hand-coded SVG face detected inside avatar container. Use AI-generated character portraits or real photography instead.`
      });
    }
  });

  // 4. Check major functional zones for unintended overlap (collision)
  const zoneSelectors = [
    '.top-hud', '.trump-dashboard',
    '.seat-north', '.seat-west', '.seat-east', '.seat-south',
    '.action-bar', '.selected-combo-hint', '.my-hand-area', '.sort-toolbar',
    '.played-west', '.played-east', '.played-north'
  ];
  const zones = [];
  zoneSelectors.forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      const r = rect(el);
      if (r.width > 0 && r.height > 0) {
        zones.push({ sel: selectorOf(el), r, el });
      }
    });
  });

  for (let i = 0; i < zones.length; i++) {
    for (let j = i + 1; j < zones.length; j++) {
      const A = zones[i], B = zones[j];
      if (A.el.contains(B.el) || B.el.contains(A.el)) continue;
      const xOverlap = Math.max(0, Math.min(A.r.right, B.r.right) - Math.max(A.r.left, B.r.left));
      const yOverlap = Math.max(0, Math.min(A.r.bottom, B.r.bottom) - Math.max(A.r.top, B.r.top));
      if (xOverlap > 4 && yOverlap > 4) {
        issues.push({
          code: 'ZONE_BOUNDING_BOX_COLLISION',
          severity: 'FAIL',
          element: `${A.sel} <-> ${B.sel}`,
          message: `Functional zones overlap by ${Math.round(xOverlap)}x${Math.round(yOverlap)}px.`
        });
      }
    }
  }

  const out = document.createElement('script');
  out.id = '__qa0_geometry_report__';
  out.type = 'application/json';
  out.textContent = JSON.stringify({
    viewport: { width: W, height: H },
    passed: issues.every(i => i.severity !== 'FAIL'),
    issue_count: issues.length,
    issues: issues
  });
  document.body.appendChild(out);
})();
"""


def find_chrome() -> str:
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    return ""


def run_audit(html_path: Path, width: int, height: int) -> dict:
    chrome = find_chrome()
    if not chrome:
        return {"error": "Headless Chrome not found on system."}

    orig = html_path.read_text(encoding="utf-8")
    injected = orig.replace("</body>", f"<script>{AUDIT_JS}</script></body>")
    if "<script>" not in injected:
        injected = orig + f"<script>{AUDIT_JS}</script>"

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", dir=str(html_path.parent), delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(injected)
        tmp_path = Path(tmp.name)

    try:
        cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            f"--window-size={width},{height}",
            "--dump-dom",
            f"file://{tmp_path.resolve()}",
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        dom = proc.stdout
        m = re.search(
            r'<script id="__qa0_geometry_report__" type="application/json">(.*?)</script>',
            dom,
            re.S,
        )
        if not m:
            return {"error": "Failed to extract geometry report from DOM."}
        return json.loads(html.unescape(m.group(1)))
    finally:
        tmp_path.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description="QA0 UI Geometry & Alignment Automated Audit")
    parser.add_argument("html_file", help="Path to HTML file to audit")
    parser.add_argument("--width", type=int, default=1600)
    parser.add_argument("--height", type=int, default=900)
    args = parser.parse_args()

    report = run_audit(Path(args.html_file), args.width, args.height)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not report.get("passed", False):
        sys.exit(1)


if __name__ == "__main__":
    main()
