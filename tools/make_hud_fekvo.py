#!/usr/bin/env python3
"""FEKVŐ (landscape) HUD-terv — izometrikus jelenet, Vesper Crane (játékos)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
S = 2

INK = (238, 226, 200, 255)
DIM = (238, 226, 200, 158)
ACCENT = (196, 62, 48, 255)
AMBER = (232, 164, 68, 255)
GREEN = (108, 214, 120, 255)
BRASS = (201, 162, 39, 255)
CYAN = (110, 200, 214, 255)
PANEL = (14, 11, 18, 190)


def f(p, s):
    return ImageFont.truetype(p, int(s * S))


def text(d, xy, s, font, fill, anchor="la"):
    d.text((xy[0] * S, xy[1] * S), s, font=font, fill=fill, anchor=anchor)


def circle(d, cx, cy, r, fill=None, outline=None, width=2):
    d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
              fill=fill, outline=outline, width=int(width * S))


def rrect(d, xy, r, fill=None, outline=None, width=2):
    d.rounded_rectangle([xy[0] * S, xy[1] * S, xy[2] * S, xy[3] * S], radius=r * S,
                        fill=fill, outline=outline, width=int(width * S))


def icon(d, kind, cx, cy, r, col=INK):
    lw = max(1.6, r * 0.11)
    w = int(lw * S)
    if kind == "gladius":
        d.line([(cx - r * 0.05) * S, (cy - r * 0.62) * S, (cx - r * 0.05) * S, (cy + r * 0.30) * S], fill=col, width=w)
        d.polygon([(cx - r * 0.22) * S, (cy - r * 0.62) * S, (cx + r * 0.12) * S, (cy - r * 0.62) * S,
                   (cx + r * 0.05) * S, (cy - r * 0.86) * S, (cx - r * 0.15) * S, (cy - r * 0.86) * S], outline=col, width=w)
        d.line([(cx - r * 0.40) * S, (cy + r * 0.30) * S, (cx + r * 0.30) * S, (cy + r * 0.30) * S], fill=col, width=w)
        d.line([(cx - r * 0.05) * S, (cy + r * 0.30) * S, (cx - r * 0.05) * S, (cy + r * 0.68) * S], fill=col, width=w)
    elif kind == "axe":
        d.line([(cx - r * 0.42) * S, (cy + r * 0.62) * S, (cx + r * 0.26) * S, (cy - r * 0.50) * S], fill=col, width=w)
        d.polygon([(cx - r * 0.02) * S, (cy - r * 0.60) * S, (cx + r * 0.62) * S, (cy - r * 0.22) * S,
                   (cx + r * 0.12) * S, (cy + r * 0.16) * S], outline=col, width=w)
    elif kind == "knife":
        d.polygon([(cx - r * 0.55) * S, (cy + r * 0.30) * S, (cx + r * 0.18) * S, (cy - r * 0.42) * S,
                   (cx + r * 0.42) * S, (cy - r * 0.10) * S, (cx - r * 0.30) * S, (cy + r * 0.44) * S],
                  outline=col, width=w)
        d.line([(cx - r * 0.58) * S, (cy + r * 0.34) * S, (cx - r * 0.78) * S, (cy + r * 0.62) * S], fill=col, width=w)
    elif kind == "revolver":
        d.rounded_rectangle([(cx - r * 0.62) * S, (cy - r * 0.18) * S, (cx + r * 0.58) * S, (cy + r * 0.08) * S],
                            radius=r * 0.12 * S, outline=col, width=w)
        d.arc([(cx - r * 0.44) * S, (cy - r * 0.26) * S, (cx + r * 0.02) * S, (cy + r * 0.26) * S],
              200, 340, fill=col, width=w)
        d.line([(cx - r * 0.30) * S, (cy + r * 0.40) * S, (cx - r * 0.50) * S, (cy + r * 0.06) * S], fill=col, width=w)
    elif kind == "shotgun":
        d.line([(cx - r * 0.72) * S, (cy - r * 0.16) * S, (cx + r * 0.72) * S, (cy - r * 0.16) * S], fill=col, width=int(w * 1.4))
        d.line([(cx - r * 0.72) * S, (cy + r * 0.04) * S, (cx + r * 0.72) * S, (cy + r * 0.04) * S], fill=col, width=int(w * 1.4))
        d.polygon([(cx - r * 0.78) * S, (cy - r * 0.30) * S, (cx - r * 0.42) * S, (cy - r * 0.26) * S,
                   (cx - r * 0.42) * S, (cy + r * 0.42) * S, (cx - r * 0.78) * S, (cy + r * 0.26) * S], outline=col, width=w)
    elif kind == "rifle":
        d.line([(cx - r * 0.78) * S, (cy - r * 0.10) * S, (cx + r * 0.78) * S, (cy - r * 0.10) * S], fill=col, width=int(w * 1.3))
        d.polygon([(cx - r * 0.80) * S, (cy - r * 0.34) * S, (cx - r * 0.34) * S, (cy - r * 0.24) * S,
                   (cx - r * 0.34) * S, (cy + r * 0.40) * S, (cx - r * 0.80) * S, (cy + r * 0.20) * S], outline=col, width=w)
        d.line([(cx - r * 0.20) * S, (cy - r * 0.28) * S, (cx - r * 0.10) * S, (cy + r * 0.14) * S], fill=col, width=w)
    elif kind == "shield":
        d.polygon([(cx - r * 0.55) * S, (cy - r * 0.48) * S, (cx + r * 0.55) * S, (cy - r * 0.48) * S,
                   (cx + r * 0.42) * S, (cy + r * 0.18) * S, (cx) * S, (cy + r * 0.66) * S,
                   (cx - r * 0.42) * S, (cy + r * 0.18) * S], outline=col, width=w)
    elif kind == "dash":
        for off in (-0.30, 0.10, 0.50):
            d.line([(cx - r * 0.60 + r * off) * S, (cy - r * 0.55) * S,
                    (cx - r * 0.05 + r * off) * S, (cy) * S], fill=col, width=w)
            d.line([(cx - r * 0.05 + r * off) * S, (cy) * S,
                    (cx - r * 0.60 + r * off) * S, (cy + r * 0.55) * S], fill=col, width=w)
    elif kind == "potion":
        d.rounded_rectangle([(cx - r * 0.28) * S, (cy - r * 0.72) * S, (cx + r * 0.28) * S, (cy - r * 0.36) * S],
                            radius=r * 0.08 * S, outline=col, width=w)
        d.ellipse([(cx - r * 0.56) * S, (cy - r * 0.34) * S, (cx + r * 0.56) * S, (cy + r * 0.72) * S],
                  outline=col, width=w)
        d.ellipse([(cx - r * 0.42) * S, (cy + r * 0.06) * S, (cx + r * 0.42) * S, (cy + r * 0.62) * S], fill=col)


# ------------------------------------------------------------------ vászon --
FW, FH = 2400, 1080                     # játék-frame (19.5:9-hez közel)
PADx, TOP = 300, 118
CANW = FW + PADx * 2
CANH = TOP + FH + 330
canvas = Image.new("RGBA", (CANW * S, CANH * S), (13, 10, 16, 255))
d = ImageDraw.Draw(canvas)

text(d, (PADx, 34), "KONTROLL & HUD — FEKVŐ KÉPERNYŐ (landscape)", f(FONTS, 30), INK)
text(d, (PADx, 76), "19.5:9 · izometrikus nézet · cowboy aranykor + Róma · Vesper Crane, a játékos",
     f(FONT, 15), DIM)

# ------------------------------------------------- háttér (izometrikus jelenet)
bg = Image.open("23_izometrikus_vesper.png").convert("RGB")
sc = FW / bg.width
bg = bg.resize((FW * S, int(bg.height * sc) * S), Image.LANCZOS)
top_crop = max(0, (bg.height - FH * S) // 3)
bg = bg.crop((0, top_crop, FW * S, top_crop + FH * S))
screen = bg.convert("RGBA")

grad = Image.new("L", (1, FH * S), 0)
gd = ImageDraw.Draw(grad)
for y in range(FH * S):
    yy = y / (FH * S)
    a = 0
    if yy < 0.20:
        a = int(150 * (1 - yy / 0.20))
    elif yy > 0.66:
        a = int(175 * ((yy - 0.66) / 0.34) ** 1.4)
    gd.point((0, y), fill=min(a, 220))
scrim = Image.new("RGBA", screen.size, (8, 6, 12, 0))
scrim.putalpha(grad.resize((FW * S, FH * S)))
screen = Image.alpha_composite(screen, scrim)
d = ImageDraw.Draw(screen)

# =============================================================== HUD =========
# --- BAL FELSŐ: minimap ---
MM = (56, 44, 296, 284)
rrect(d, MM, 14, fill=PANEL, outline=(238, 226, 200, 120), width=2.5)
rrect(d, (68, 56, 284, 272), 8, fill=(28, 24, 34, 235))
d.line([(70) * S, 168 * S, 282 * S, 150 * S], fill=(120, 106, 96, 220), width=int(12 * S))
d.line([(150) * S, 58 * S, 168 * S, 270 * S], fill=(120, 106, 96, 190), width=int(9 * S))
d.line([(210) * S, 150 * S, 274 * S, 258 * S], fill=(120, 106, 96, 170), width=int(7 * S))
for hx, hy, hw, hh in [(80, 180, 34, 26), (110, 70, 30, 24), (214, 70, 40, 30), (230, 186, 30, 28)]:
    rrect(d, (hx, hy, hx + hw, hy + hh), 3, fill=(72, 62, 56, 235), outline=(150, 136, 120, 120), width=1)
for px_, py_, col, lab in [(236, 86, ACCENT, "R"), (100, 214, GREEN, "P"), (192, 232, AMBER, "!"), (128, 140, (240, 140, 60), "T")]:
    circle(d, px_, py_, 12, fill=(12, 10, 16, 235), outline=col, width=3)
    text(d, (px_, py_ + 1), lab, f(FONTB, 13), col, anchor="mm")
circle(d, 168, 168, 14, fill=(12, 10, 16, 235), outline=INK, width=2)
d.polygon([(168) * S, (154) * S, (177) * S, (175) * S, (168) * S, (171) * S, (159) * S, (175) * S], fill=INK)
text(d, (176, 60), "N", f(FONTB, 14), DIM, anchor="ma")
text(d, (176, 292), "MINIMAP", f(FONTB, 13), DIM, anchor="ma")

# --- BAL FELSŐ: HP + potik állapot ---
rrect(d, (56, 316, 400, 348), 9, fill=PANEL, outline=(238, 226, 200, 115), width=2)
rrect(d, (61, 321, 61 + int((400 - 61 - 5) * 0.76), 343), 7, fill=(168, 46, 40, 238))
text(d, (64, 322), "HP  76 / 100", f(FONTB, 13), INK)
text(d, (176, 372), "T = tábortűz (mozog veled)", f(FONT, 12.5), (238, 226, 200, 125), anchor="ma")

# --- JOBB FELSŐ: potik ---
text(d, (FW - 60, 30), "POTIK", f(FONTB, 14), DIM, anchor="ra")
potions = [("potion", (196, 64, 56), "2", "gyógy"),
           ("potion", (226, 158, 60), "1", "erő"),
           ("potion", (96, 190, 210), "3", "látás")]
for i, (k, col, cnt, lab) in enumerate(potions):
    px_ = FW - 90 - i * 118
    py_ = 108
    circle(d, px_, py_, 46, fill=(10, 8, 14, 130))
    circle(d, px_, py_, 40, fill=(26, 20, 28, 225), outline=(238, 226, 200, 120), width=2.5)
    icon(d, k, px_, py_ - 2, 32, col)
    circle(d, px_ + 32, py_ + 32, 17, fill=(12, 10, 16, 245), outline=col, width=2)
    text(d, (px_ + 32, py_ + 33), cnt, f(FONTB, 16), INK, anchor="mm")
    text(d, (px_, py_ + 66), lab, f(FONTB, 12.5), DIM, anchor="ma")

# --- BAL ALSÓ: joystick ---
jx, jy, jr = 232, FH - 232, 132
circle(d, jx, jy, jr + 14, fill=(10, 8, 14, 100))
circle(d, jx, jy, jr, fill=(255, 255, 255, 16), outline=(238, 226, 200, 110), width=2.5)
circle(d, jx, jy, jr * 0.52, fill=(238, 226, 200, 48), outline=(238, 226, 200, 135), width=2)
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    circle(d, jx + dx * (jr - 12), jy + dy * (jr - 12), 3.4, fill=(238, 226, 200, 165))
text(d, (jx, jy + jr + 28), "JOYSTICK — MOZGÁS", f(FONTB, 13.5), DIM, anchor="ma")

# --- JOBB ALSÓ: harcgombok ---
btns = [
    (FH - 200, 1740, 96, "gladius", "ÜTÉS 1 · GLADIUS", True),
    (FH - 372, 1990, 74, "revolver", "ÜTÉS 2 · REVOLVER", False),
    (FH - 402, 1530, 74, "shotgun", "ÜTÉS 3 · SÖRÉTES", False),
    (FH - 372, 1690, 62, "shield", "VÉD", False),
    (FH - 108, 1960, 66, "dash", "KITÉRÉS", False),
]
for by, bx, br, k, lab, hi in btns:
    circle(d, bx, by, br + 10, fill=(10, 8, 14, 130))
    circle(d, bx, by, br, fill=(28, 22, 30, 215) if not hi else (48, 28, 26, 230),
           outline=AMBER if hi else (238, 226, 200, 120), width=3 if hi else 2.5)
    icon(d, k, bx, by - br * 0.05, br * 0.72)
    text(d, (bx, by + br + 16), lab, f(FONTB, 12.5) if hi else f(FONT, 12), INK if hi else DIM, anchor="ma")

# --- ALSÓ KÖZÉP: fegyverválasztó sáv (6 fegyver) ---
weapons = [("gladius", "GLADIUS"), ("axe", "BALTA"), ("knife", "KÉS"),
           ("revolver", "REVOLVER"), ("shotgun", "SÖRÉTES"), ("rifle", "PUSKA")]
slot_w, gap = 108, 16
total = len(weapons) * slot_w + (len(weapons) - 1) * gap
x0 = FW / 2 - total / 2
ys = FH - 132
rrect(d, (x0 - 26, ys - 74, x0 + total + 26, ys + 74), 18, fill=(12, 10, 16, 175), outline=(238, 226, 200, 70), width=2)
for i, (k, lab) in enumerate(weapons):
    sx = x0 + i * (slot_w + gap) + slot_w / 2
    sel = (i == 0)
    rrect(d, (sx - slot_w / 2, ys - 62, sx + slot_w / 2, ys + 62), 12,
          fill=(46, 28, 26, 230) if sel else (26, 20, 28, 220),
          outline=AMBER if sel else (238, 226, 200, 105), width=3 if sel else 2)
    icon(d, k, sx, ys - 12, 30)
    text(d, (sx, ys + 34), lab, f(FONTB, 12) if sel else f(FONT, 11.5), INK if sel else DIM, anchor="ma")
    text(d, (sx - slot_w / 2 + 8, ys - 56), str(i + 1), f(FONTB, 12), (238, 226, 200, 120))
text(d, (FW / 2, ys + 92), "FEGYVERVÁLASZTÓ — 6 fegyver, vízszintes sáv (a középső köralak helyett, hogy elférjen és elérhető legyen)",
     f(FONTB, 13), DIM, anchor="ma")

# --- KÖZÉP: küldetés-célzó (opcionális) ---
rrect(d, (FW / 2 - 300, 44, FW / 2 + 300, 96), 10, fill=(12, 10, 16, 150), outline=(238, 226, 200, 65), width=2)
text(d, (FW / 2, 70), "CÉL:  Találd meg a fiút — a nyomok Blackbriar felé vezetnek", f(FONTB, 15), INK, anchor="mm")

# ------------------------------------------------ annotáció a frame alatt ----
canvas.alpha_composite(screen, (PADx * S, TOP * S))
d = ImageDraw.Draw(canvas)
rrect(d, (PADx, TOP, PADx + FW, TOP + FH), 10, outline=(90, 74, 66, 255), width=5)

y0 = TOP + FH + 30
cols = [
    ("BAL OLDAL — a bal hüvelykujj", [
        "JOYSTICK: fix pozíció, szabad mozgás. Landscape-ben több hely van,",
        "ezért a joystick nagyobb lehet (132 px sugár) — kényelmesebb.",
        "MINIMAP: bal felső (R = Vigiles, P = bolt, ! = küldetés,",
        "T = tábortűz, ami MOZOG veled).",
        "HP-sáv a minimap alatt. Nincs korrupció-mérő: a játékos",
        "nem használ követ, csak potit, fegyvert és tudást.",
    ]),
    ("JOBB OLDAL — a jobb hüvelykujj", [
        "HARCGOMBOK: 3 ütés + védekezés + kitérés,",
        "a fő fegyver (gladius) a legnagyobb és legközelebb.",
        "POTIK: jobb felső, 3 ikon darabszámmal;",
        "a gyűrű körülötte a töltést mutatja.",
        "A gombok 200 px-re a saroktól — a hüvelykujj",
        "természetes ívén, nem a képernyő szélén.",
    ]),
    ("ALSÓ KÖZÉP — fegyverválasztó", [
        "6 fegyver: gladius, balta, kés, revolver, sörétes, puska.",
        "Landscape-ben a köralak helyett vízszintes sáv a jó:",
        "elfér, és a hüvelykujj egy húzással végigcsúsztathat rajta.",
        "A kiválasztott fegyver határozza meg, mit csinálnak",
        "az ütésgombok: pl. gladius = közelharc-kombó,",
        "revolver = gyors lövés, sörétes = közeli robbanás.",
    ]),
]
cw = (FW - 60) / 3
for i, (title, lines) in enumerate(cols):
    x = PADx + i * (cw + 30)
    text(d, (x, y0), title, f(FONTB, 15.5), AMBER)
    yy = y0 + 28
    for ln in lines:
        text(d, (x, yy), ln, f(FONT, 13), DIM)
        yy += 21

# ------------------------------------------------------ magyarázó sáv -------
y0 = y0 + 200
text(d, (PADx, y0), "MIÉRT EZ A JOBB LANDSCAPE-BEN:", f(FONTB, 15.5), INK)
notes = [
    ("• 200 px szélső margó", "a hüvelykujj nem ér el a képernyő szélére — a gombok beljebb kerüljenek"),
    ("• Biztonságos zóna", "a notch/kijelző-lyuk landscape-ben oldalt van: 90 px oldalmargó, és semmi fontos elem oda nem kerül"),
    ("• A HUD-ot ne a filter szűrje", "a csontfehér és borostyán elemek a zöld világ fölött is jól olvashatók maradjanak"),
    ("• A portrait-mód megtartása", "ha eldobod a fekvőt, minden gomb-variánst újra kell tervezni — döntsd el korán"),
]
for i, (t, sub) in enumerate(notes):
    text(d, (PADx, y0 + 32 + i * 24), t, f(FONTB, 13.5), INK)
    text(d, (PADx + 240, y0 + 32 + i * 24), sub, f(FONT, 13), DIM)

out = canvas.resize((CANW, CANH), Image.LANCZOS).convert("RGB")
out.save("kontroll_es_hud_fekvo.png", quality=95)
print("kész", out.size)
