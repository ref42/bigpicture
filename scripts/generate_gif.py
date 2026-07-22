#!/usr/bin/env python3
"""
Generate animated Big Picture icon.

Outputs:
  assets/icon.gif   — animated GIF  (dark bg, for README / embedding)
  assets/icon.apng  — animated PNG  (true alpha, for video / design tools)

Usage:
    pip install pillow numpy
    python scripts/generate_gif.py
    python scripts/generate_gif.py --size 512 --fps 60 --loops 4
"""

import argparse
import math
import sys
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError:
    sys.exit("Requirements missing: pip install pillow numpy")

# ── Design ────────────────────────────────────────────────────────────────────

BASE_COLOR = np.array([9, 105, 218], dtype=np.float32)   # #0969da

# (radius as fraction of half-canvas, stroke as fraction of full size,
#  opacity, period_seconds, clockwise, dash_degrees, gap_degrees)
RINGS = [
    (0.90, 0.011, 0.20, 12.0, True,   36, 18),
    (0.66, 0.014, 0.38,  9.0, False,  26, 13),
    (0.43, 0.018, 0.62,  5.0, True,   18,  9),
    (0.22, 0.023, 0.88,  3.0, False,  12,  6),
]

DOT_FRAC_MIN = 0.038   # dot radius as fraction of half-canvas
DOT_FRAC_MAX = 0.054
DOT_PULSE_SEC = 2.0

DARK_BG = np.array([13, 17, 23], dtype=np.float32)   # GitHub dark

# ── Per-frame renderer ────────────────────────────────────────────────────────

def render_frame(size: int, frame_idx: int, fps: int, total_sec: float) -> Image.Image:
    """Return an RGBA PIL image for one frame, rendered with numpy antialiasing."""
    half = size / 2.0

    # Pixel coordinate grids (centre of each pixel)
    yi, xi = np.mgrid[0:size, 0:size]
    dx = xi.astype(np.float32) - half + 0.5
    dy = yi.astype(np.float32) - half + 0.5
    dist  = np.sqrt(dx * dx + dy * dy)
    angle = np.degrees(np.arctan2(dy, dx)) % 360.0   # 0 = 3 o'clock

    # Transparent canvas (RGBA float)
    canvas = np.zeros((size, size, 4), dtype=np.float32)

    t = frame_idx / (fps * total_sec)

    for r_frac, sw_frac, opacity, period, cw, dash, gap in RINGS:
        radius = r_frac * half
        stroke = max(1.5, sw_frac * size)

        offset = (frame_idx / (period * fps)) * 360.0
        if not cw:
            offset = -offset

        # Signed distance from ring centreline → soft AA coverage
        ring_sdf = np.abs(dist - radius) - stroke * 0.5
        coverage = np.clip(-ring_sdf + 0.5, 0.0, 1.0)   # 1px feather

        # Dash mask from angle
        angle_rel = (angle - offset) % 360.0
        in_dash = (angle_rel % (dash + gap)) < dash

        alpha = coverage * in_dash * opacity   # shape (H,W)

        # Alpha-over compositing
        a3 = alpha[:, :, np.newaxis]
        canvas[:, :, :3] = BASE_COLOR * a3 + canvas[:, :, :3] * (1.0 - a3)
        canvas[:, :,  3] = alpha * 255.0 + canvas[:, :, 3] * (1.0 - alpha)

    # Centre dot with smooth pulse
    pulse  = 0.5 + 0.5 * math.sin(t * 2 * math.pi * (total_sec / DOT_PULSE_SEC))
    dot_r  = (DOT_FRAC_MIN + (DOT_FRAC_MAX - DOT_FRAC_MIN) * pulse) * half
    dot_cv = np.clip(dot_r - dist + 0.5, 0.0, 1.0)

    d3 = dot_cv[:, :, np.newaxis]
    canvas[:, :, :3] = BASE_COLOR * d3 + canvas[:, :, :3] * (1.0 - d3)
    canvas[:, :,  3] = dot_cv * 255.0 + canvas[:, :, 3] * (1.0 - dot_cv)

    return Image.fromarray(np.clip(canvas, 0, 255).astype(np.uint8), "RGBA")


def composite_on_dark(rgba: Image.Image) -> Image.Image:
    """Composite RGBA frame onto dark background for GIF export."""
    bg = Image.new("RGBA", rgba.size, (int(DARK_BG[0]), int(DARK_BG[1]), int(DARK_BG[2]), 255))
    bg.paste(rgba, mask=rgba.split()[3])
    return bg.convert("RGB")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Generate Big Picture animated icon")
    p.add_argument("--size",  type=int,   default=384,  help="Output px (default 384)")
    p.add_argument("--fps",   type=int,   default=60,   help="Frames per second (default 60)")
    p.add_argument("--loops", type=float, default=3.0,  help="Seconds to render (default 3)")
    p.add_argument("--gif",   action="store_true", default=True,  help="Output GIF (dark bg)")
    p.add_argument("--apng",  action="store_true", default=True,  help="Output APNG (alpha)")
    args = p.parse_args()

    root        = Path(__file__).parent.parent / "assets"
    root.mkdir(parents=True, exist_ok=True)
    total_frames = int(args.fps * args.loops)
    duration_ms  = round(1000 / args.fps)

    print(f"Rendering {total_frames} frames  {args.size}px  {args.fps}fps …")
    rgba_frames = [
        render_frame(args.size, i, args.fps, args.loops)
        for i in range(total_frames)
    ]

    # ── GIF (dark background, palette quantisation) ───────────────────────
    gif_path = root / "icon.gif"
    rgb_frames = [composite_on_dark(f) for f in rgba_frames]
    p_frames   = [f.convert("P", palette=Image.ADAPTIVE, colors=255) for f in rgb_frames]
    p_frames[0].save(
        gif_path, save_all=True, append_images=p_frames[1:],
        duration=duration_ms, loop=0, optimize=False,
    )
    print(f"GIF  → {gif_path}  ({gif_path.stat().st_size // 1024} KB)")

    # ── APNG (true alpha) ─────────────────────────────────────────────────
    apng_path = root / "icon.apng"
    rgba_frames[0].save(
        apng_path, save_all=True, append_images=rgba_frames[1:],
        duration=duration_ms, loop=0,
    )
    print(f"APNG → {apng_path}  ({apng_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
