"""Иконка приложения: розовые полоски + шоколадная звезда в горошек."""
import math
from pathlib import Path
from PIL import Image, ImageDraw
OUT = Path(__file__).parent / "docs"
def star(cx, cy, R, r, n=5, rot=-90):
    pts = []
    for k in range(2 * n):
        a = math.radians(rot + k * 180 / n); rr = R if k % 2 == 0 else r
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts
for size in (180, 512):
    S = 1024; im = Image.new("RGB", (S, S), "#FFD6E6"); d = ImageDraw.Draw(im)
    for x in range(0, S, 140):
        d.rectangle([x + 70, 0, x + 92, S], fill="#FFB3CF"); d.rectangle([x + 112, 0, x + 118, S], fill="#FFFFFF")
    pts = star(512, 540, 400, 170)
    d.polygon(pts, fill="#3E2420")
    mask = Image.new("L", (S, S), 0); ImageDraw.Draw(mask).polygon(star(512, 540, 330, 140), fill=255)
    dots = Image.new("RGB", (S, S), "#FF4F9A"); dd = ImageDraw.Draw(dots)
    for y in range(0, S, 56):
        for x in range(0, S, 56):
            ox = 28 if (y // 56) % 2 else 0
            dd.ellipse([x + ox - 9, y - 9, x + ox + 9, y + 9], fill="#FFE1EE")
    im.paste(dots, (0, 0), mask)
    sp = star(820, 210, 120, 30, 4, -90); d.polygon(sp, fill="#FFD23F", outline="#3E2420")
    im.resize((size, size), Image.LANCZOS).save(OUT / f"icon-{size}.png")
