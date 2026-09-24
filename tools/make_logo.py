#!/usr/bin/env python3
"""CARO DEORUM — logó-változatlap (3 tipográfiai irány + méretpróba)."""
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONTSB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
S = 2

INK = (238, 226, 200)
CREAM = (243, 236, 216)
GOLD = (203, 168, 78)
BRASS = (201, 162, 39)
GREEN = (140, 224, 150)
DIM = (238, 226, 200, 170)


def f(p, s):
    return ImageFont.truetype(p, int(s * S))


def text(d, xy, s, font, fill, anchor="la"):
    d.text((xy[0] * S, xy[1] * S), s, font=font, fill=fill, anchor=anchor)


def spaced(d, xy, s, font, fill, sp, anchor="ma"):
    widths = [d.textlength(ch, font=font) / S for ch in s]
    total = sum(widths) + sp * (len(s) - 1)
    x = xy[0] - total / 2 if anchor == "ma" else (xy[0] - total if anchor == "ra" else xy[0])
    for ch, w in zip(s, widths):
        d.text((x * S, xy[1] * S), ch, font=font, fill=fill, anchor="ls")
        x += w + sp
    return total


W, H = 2100, 1480
im = Image.new("RGBA", (W * S, H * S), (13, 10, 16, 255))
d = ImageDraw.Draw(im)

text(d, (60, 40), "CARO DEORUM — A CÍM ÉS A LOGÓ", f(FONTSB, 30), INK)
text(d, (60, 84), "latin: „az istenek húsa” — a kő birodalmi hivatalos neve, és a végső helyszín neve a játékban",
     f(FONT, 15), DIM)

# ------------------------------------------------------------------ A ------
rrect_y = 150
PANELS = [
    dict(x=60, y=150, w=1290, h=470, kind="A"),
    dict(x=60, y=650, w=630, h=470, kind="B"),
    dict(x=720, y=650, w=630, h=470, kind="C"),
]
d.rounded_rectangle([60 * S, 150 * S, 1350 * S, 620 * S], radius=14 * S,
                    fill=(20, 16, 22, 255), outline=(70, 58, 52, 255), width=3 * S)
text(d, (90, 172), "A — FŐ IRÁNY: SZERIF, SZÉLES BETŰKÖZ", f(FONTB, 15), BRASS)
spaced(d, (705, 400), "CARO DEORUM", f(FONTSB, 76), CREAM + (255,), 16)
# vonal + SPQR-sáv
d.line([(260 * S, 425 * S), (1150 * S, 425 * S)], fill=GOLD + (200,), width=int(2 * S))
spaced(d, (705, 470), "SÓ ÉS VAS", f(FONTS, 24), GOLD + (255,), 26)
text(d, (705, 560), "A hivatalos birodalmi hangsúly. Ez kerül a borítóra és a key artra —\n"
                    "a betűköz adja a „régi, hivatalos pecsét” érzést.",
     f(FONT, 14), DIM, anchor="ma")

for p in PANELS[1:]:
    d.rounded_rectangle([p["x"] * S, p["y"] * S, (p["x"] + p["w"]) * S, (p["y"] + p["h"]) * S],
                        radius=14 * S, fill=(20, 16, 22, 255), outline=(70, 58, 52, 255), width=3 * S)

# ------------------------------------------------------------------ B ------
text(d, (90, 672), "B — ZÖLD IZZÁS (horror / trailer)", f(FONTB, 15), GREEN)
cx = 60 + 630 / 2
# zöld derengés a betűk alatt
glow = Image.new("RGBA", im.size, (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
spaced(gd, (cx, 890), "CARO", f(FONTSB, 62), (60, 160, 80, 150), 12)
spaced(gd, (cx, 960), "DEORUM", f(FONTSB, 62), (60, 160, 80, 150), 12)
from PIL import ImageFilter
glow = glow.filter(ImageFilter.GaussianBlur(18 * S))
im.alpha_composite(glow)
d = ImageDraw.Draw(im)
spaced(d, (cx, 890), "CARO", f(FONTSB, 62), CREAM + (255,), 12)
spaced(d, (cx, 960), "DEORUM", f(FONTSB, 62), GREEN + (255,), 12)
text(d, (cx, 1010), "a betűk alján zöld derengés — a kráter fénye", f(FONT, 13.5), DIM, anchor="ma")
text(d, (cx, 1060), "Trailerhez, horror-marketinghez,\na borító hátuljára.", f(FONT, 13.5), DIM, anchor="ma")

# ------------------------------------------------------------------ C ------
text(d, (750, 672), "C — FÉMNYOMOTT WESTERN (borító / ikon)", f(FONTB, 15), BRASS)
cx2 = 720 + 630 / 2
# réz "nyomólap" hatás: sötét sáv + fény
d.rounded_rectangle([(cx2 - 240) * S, 850 * S, (cx2 + 240) * S, 990 * S], radius=8 * S,
                    fill=(38, 28, 18, 255), outline=(150, 118, 52, 220), width=3 * S)
spaced(d, (cx2, 920), "CARO", f(FONTB, 46), (232, 196, 110, 255), 6)
spaced(d, (cx2, 968), "DEORUM", f(FONTB, 46), (232, 196, 110, 255), 6)
text(d, (cx2, 1030), "fémnyomott, sárgaréz", f(FONT, 13.5), DIM, anchor="ma")
text(d, (cx2, 1080), "Ez a változat kis méretben (64 px)\nis működik — a részletes\ndíszítés a kicsiben elveszik.", f(FONT, 13.5), DIM, anchor="ma")

# ------------------------------------------------------------- méretpróba --
d.rounded_rectangle([60 * S, 1150 * S, 2040 * S, 1400 * S], radius=14 * S,
                    fill=(19, 15, 20, 255), outline=(70, 58, 52, 255), width=3 * S)
text(d, (90, 1172), "MÉRETPRÓBA — a logó 64 px szélességig olvasható kell legyen", f(FONTB, 15), BRASS)
for i, (size, label) in enumerate(((40, "~1500 px (borító)"), (28, "~1050 px (key art)"),
                                    (19, "~700 px (menü)"), (13, "~470 px (ikon)"))):
    x = 300 + i * 570
    spaced(d, (x, 1282), "CARO DEORUM", f(FONTSB, size), CREAM + (255,), size * 0.16)
    text(d, (x, 1312), label, f(FONT, 12), DIM, anchor="ma")
text(d, (90, 1350), "Tipp: készüljön KÉT változat — részletes (marketing, borító) és egyszerű (ikon, könyvtár, splash).",
     f(FONT, 13.5), DIM)

out = im.resize((W, H), Image.LANCZOS).convert("RGB")
out.save("/home/user/koncepcio/caro_deorum_logo.png", quality=95)
print("kész", out.size)
