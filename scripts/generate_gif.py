#!/usr/bin/env python3
"""
Generate assets/icon.gif from the Big Picture icon design.

Usage:
    pip install pillow
    python scripts/generate_gif.py
    python scripts/generate_gif.py --size 512 --fps 60 --bg dark
"""

import argparse
import math
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

# ---------------------------------------------------------------------------
# Design constants
# ---------------------------------------------------------------------------

BASE_COLOR = (9, 105, 218)   # #0969da

# (radius, stroke_width, opacity, period_seconds, clockwise, dash_deg, gap_deg)
RINGS = [
    (115, 3, 0.20, 12.0, True,   36, 18),
    ( 85, 4, 0.38,  9.0, False,  26, 13),
    ( 55, 5, 0.62,  5.0, True,   18,  9),
    ( 28, 6, 0.88,  3.0, False,  12,  6),
]

DOT_R_MIN = 8
DOT_R_MAX = 11
DOT_PULSE_SEC = 2.0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def draw_dashed_circle(draw, cx, cy, radius, stroke_w, color, offset_deg, dash_deg, gap_deg):
    x0, y0 = cx - radius, cy - radius
    x1, y1 = cx + radius, cy + radius
    step = dash_deg + gap_deg
    angle = offset_deg % 360
    drawn = 0
    while drawn < 360:
        end_deg = min(dash_deg, 360 - drawn)
        # PIL arc: 0° = 3 o'clock; subtract 90 so 0° = 12 o'clock
        draw.arc([x0, y0, x1, y1],
                 angle - 90,
                 angle + end_deg - 90,
                 fill=color, width=stroke_w)
        angle = (angle + step) % 360
        drawn += step


def make_frame(frame_idx, total_frames, size, scale, bg_rgba):
    rs = size * scale
    img = Image.new("RGBA", (rs, rs), bg_rgba)
    draw = ImageDraw.Draw(img)
    cx = cy = rs // 2
    t = frame_idx / total_frames  # 0..1 over one loop

    for radius, sw, alpha, period_sec, clockwise, dash, gap in RINGS:
        # how many full loops does this ring complete over `total_frames`?
        # total_frames covers `total_frames / fps` seconds
        pass  # computed below per-ring in caller

    for radius, sw, alpha, period_sec, clockwise, dash, gap in RINGS:
        r_s   = radius * scale
        sw_s  = max(1, sw * scale)
        a_int = int(255 * alpha)
        color = BASE_COLOR + (a_int,)
        # offset in degrees for this frame
        offset = (frame_idx / (period_sec * _fps)) * 360
        if not clockwise:
            offset = -offset
        draw_dashed_circle(draw, cx, cy, r_s, sw_s, color, offset, dash, gap)

    # Center dot pulse
    pulse = 0.5 + 0.5 * math.sin(t * 2 * math.pi * (_total_sec / DOT_PULSE_SEC))
    dot_r = int((DOT_R_MIN + (DOT_R_MAX - DOT_R_MIN) * pulse) * scale)
    draw.ellipse([cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r],
                 fill=BASE_COLOR + (255,))

    return img.resize((size, size), Image.LANCZOS)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate Big Picture animated GIF")
    parser.add_argument("--size",   type=int, default=256, help="Output size in px (default 256)")
    parser.add_argument("--fps",    type=int, default=30,  help="Frames per second (default 30)")
    parser.add_argument("--loops",  type=int, default=2,   help="Seconds of animation to render (default 2)")
    parser.add_argument("--scale",  type=int, default=3,   help="Supersample scale for antialiasing (default 3)")
    parser.add_argument("--bg",     choices=["transparent", "white", "dark"], default="white",
                        help="Background color (default white)")
    parser.add_argument("--out",    type=str, default=None, help="Output path (default assets/icon.gif)")
    args = parser.parse_args()

    global _fps, _total_sec
    _fps = args.fps
    _total_sec = args.loops

    total_frames = args.fps * args.loops
    duration_ms  = 1000 // args.fps

    if args.bg == "transparent":
        bg_rgba = (0, 0, 0, 0)
    elif args.bg == "dark":
        bg_rgba = (13, 17, 23, 255)   # GitHub dark background
    else:
        bg_rgba = (255, 255, 255, 255)

    out_path = Path(args.out) if args.out else Path(__file__).parent.parent / "assets" / "icon.gif"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Rendering {total_frames} frames at {args.size}px ({args.fps}fps, {args.loops}s)…")
    frames_rgba = [
        make_frame(i, total_frames, args.size, args.scale, bg_rgba)
        for i in range(total_frames)
    ]

    # Convert to palette mode for GIF
    gif_frames = []
    for f in frames_rgba:
        if args.bg == "transparent":
            # Composite on white for GIF (GIF transparency is 1-bit)
            white = Image.new("RGBA", f.size, (255, 255, 255, 255))
            white.paste(f, mask=f.split()[3])
            f = white
        gif_frames.append(
            f.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=255)
        )

    gif_frames[0].save(
        out_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=True,
    )
    print(f"Saved → {out_path}  ({out_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
