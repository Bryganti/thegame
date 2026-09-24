#!/usr/bin/env python3
"""Zöldes 'halloweeni' filter — 3 erősségi fokozat demója ugyanazon a jeleneten."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
INK = (238, 226, 200)
DIM = (238, 226, 200, 170)
S = 2


def f(p, s):
    return ImageFont.truetype(p, int(s * S))


def lum(img):
    return (img @ np.array([0.2126, 0.7152, 0.0722], dtype=np.float32))[..., None]


def smoothstep(a, b, x):
    t = np.clip((x - a) / (b - a), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def grade(img, tint=(0.84, 1.10, 0.87), sat=0.85, lift=0.10,
          lift_col=(0.045, 0.115, 0.075), vig=0.30, strength=0.4):
    """img: float32 0..1, HxWx3"""
    # telítettség
    L = lum(img)
    g = L + (img - L) * sat
    # színezet
    g = g * np.array(tint, dtype=np.float32)
    # árnyékok felemelése zöldbe (ez adja a "spooky" érzést)
    amt = (lift * (1.0 - np.clip(L, 0, 1)))
    g = g * (1.0 - amt) + np.array(lift_col, dtype=np.float32) * amt
    # vignetta
    h, w, _ = img.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt(((xx / w) - 0.5) ** 2 + ((yy / h) - 0.5) ** 2) / 0.7071
    g = g * (1.0 - vig * smoothstep(0.45, 1.0, d))[..., None]
    # erősség
    g = img + (g - img) * strength
    return np.clip(g, 0, 1)


src = np.asarray(Image.open("12_topdown_1800.png").convert("RGB")).astype(np.float32) / 255.0
h, w, _ = src.shape
pw = 640
ph = int(h * pw / w)


def panel(a):
    return Image.fromarray((a * 255).astype(np.uint8)).resize((pw * S, ph * S), Image.LANCZOS)


panels = [
    ("A — SZŰRŐ NÉLKÜL", panel(src), "alap jelenet"),
    ("B — HALLOWEEN-ZÖLD (finom)",
     panel(grade(src, strength=0.40, sat=0.88, lift=0.09, vig=0.26)),
     "strength 0.40 · saturation 0.88 · lift 0.09"),
    ("C — MOCSÁR-ZÖLD (erős)",
     panel(grade(src, strength=0.75, sat=0.62, lift=0.16,
                 lift_col=(0.03, 0.13, 0.08), tint=(0.80, 1.16, 0.84), vig=0.42)),
     "strength 0.75 · saturation 0.62 · lift 0.16"),
]

GAP, PAD, TOPH, CAPH = 28, 34, 92, 108
W = PAD * 2 + pw * 3 + GAP * 2
H = TOPH + ph + CAPH + 250 + 120
im = Image.new("RGBA", (W * S, H * S), (14, 11, 17, 255))
d = ImageDraw.Draw(im)


def text(xy, s, font, fill, anchor="la"):
    d.text((xy[0] * S, xy[1] * S), s, font=font, fill=fill, anchor=anchor)


text((PAD, 30), "A ZÖLDES FILTER — HALLOWEENI HANGULAT", f(FONTS, 27), INK)
text((PAD, 66), "ugyanaz a jelenet, három erősségi fokozat — a szűrő hangulatot ad, de nem nyeli el a játékmenetet",
     f(FONT, 14.5), DIM)

for i, (title, img, sub) in enumerate(panels):
    x = PAD + i * (pw + GAP)
    im.alpha_composite(img.convert("RGBA"), (x * S, TOPH * S))
    d.rounded_rectangle([x * S, TOPH * S, (x + pw) * S, (TOPH + ph) * S],
                        radius=8 * S, outline=(90, 74, 66, 255), width=3 * S)
    text((x, TOPH + ph + 14), title, f(FONTB, 16), INK)
    text((x, TOPH + ph + 38), sub, f(FONT, 13), DIM)

# alsó magyarázat
y = TOPH + ph + CAPH
text((PAD, y), "Mit csinál pontosan a szűrő (a Godotban ugyanez a shader):", f(FONTB, 15), INK)
lines = [
    ("1. Árnyékemelés zöldbe (lift)", "a fekete mélyülő helyett zöldesen dereng — ettől lesz „kísérteties”, nem csak zöld."),
    ("2. Telítettség csökkentése", "a fakó világban a vér és a meteor-zöld jobban kiugrik."),
    ("3. Színezet (tint)", "pirosakat visszafogja, zöldeket emel — a tűz narancs marad, a hold ezüstös-zöld."),
    ("4. Vignetta", "a képernyő széle sötétedik, a játékos közepe világos marad."),
    ("5. Erősség-keverés", "0.0 = ki, 0.4 = este, 0.75 = kráter / legendás zóna. Területenként változtatható."),
]
yy = y + 30
for t, sub in lines:
    text((PAD, yy), "•", f(FONTB, 14), (130, 220, 140))
    text((PAD + 18, yy), t, f(FONTB, 14), INK)
    text((PAD + 260, yy), sub, f(FONT, 13.5), DIM)
    yy += 26

text((PAD, yy + 16), "FIGYELEM:", f(FONTB, 14), (214, 92, 60))
notes = [
    "• A UI-t (HP, potik, ikonok) NE szűrd át — a csontfehér és borostyán elemek így is „kívül maradnak” a világon, és jól olvashatók.",
    "• Színvak-barát opció kell: zöld-szűrőben a deuteranopiásoknak elveszik a kontraszt — adj egy erősség-csúszkát a beállításokba.",
    "• A sebzés- és méreg-visszajelzés maradjon PIROS/SÁRGA, ne zöld — különben a játékos nem látja, mi történik.",
    "• Az NPC-portrékat és a dialógus-hátteret szűrő nélkül hagyd: a meleg bőrtónus adja a kontrasztot a zöld világgal.",
]
yy += 42
for n in notes:
    text((PAD, yy), n, f(FONT, 13), DIM)
    yy += 22

out = im.resize((W, H), Image.LANCZOS).convert("RGB")
out.save("zold_filter_demo.png", quality=95)
print("kész", out.size)
