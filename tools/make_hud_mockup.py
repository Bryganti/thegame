#!/usr/bin/env python3
"""Telefonos HUD-mockup a Salem-vadász játékhoz (felülnézetes, 2D)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

S = 2  # supersample factor

INK = (238, 226, 200, 255)
DIM = (238, 226, 200, 150)
ACCENT = (196, 62, 48, 255)      # római vörös
AMBER = (232, 164, 68, 255)
GREEN = (108, 214, 120, 255)
CYAN = (110, 200, 214, 255)
PANEL = (16, 13, 20, 168)
PANEL2 = (10, 8, 13, 205)


def f(path, size):
    return ImageFont.truetype(path, int(size * S))


def circle(d, cx, cy, r, fill=None, outline=None, width=2):
    d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
              fill=fill, outline=outline, width=int(width * S))


def ring_arc(d, cx, cy, r, start, end, color, width):
    d.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
          start, end, fill=color, width=int(width * S))


def text(d, xy, s, font, fill, anchor="la"):
    d.text((xy[0] * S, xy[1] * S), s, font=font, fill=fill, anchor=anchor)


def rrect(d, xy, r, fill=None, outline=None, width=2):
    d.rounded_rectangle([xy[0] * S, xy[1] * S, xy[2] * S, xy[3] * S],
                        radius=r * S, fill=fill, outline=outline, width=int(width * S))


# ---------------------------------------------------------------- canvas ----
W, H = 1310, 1770
canvas = Image.new("RGBA", (W * S, H * S), (10, 8, 14, 255))
d = ImageDraw.Draw(canvas)

PX, PY, PW, PH = 360, 62, 900, 1640          # phone rect
RAD = 54

# ------------------------------------------------------- játékvilág háttere --
world = Image.open("06_topdown.png").convert("RGB")
world = world.resize((1150, 628), Image.LANCZOS)
world = world.filter(ImageFilter.GaussianBlur(0.6))

screen = Image.new("RGBA", (PW * S, PH * S), (12, 10, 16, 255))
wm = world.resize((1150 * S, 628 * S), Image.LANCZOS).convert("RGBA")
# sötétítés
dark = Image.new("RGBA", wm.size, (10, 8, 20, 120))
wm = Image.alpha_composite(wm, dark)

# lágy maszk: középen éles, szélek felé eltűnik
mask = Image.new("L", wm.size, 0)
md = ImageDraw.Draw(mask)
md.ellipse([-260 * S, -40 * S, (1150 + 260) * S, (628 + 130) * S], fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(120 * S))
wm.putalpha(mask)

screen.alpha_composite(wm, ((PW - 1150) // 2 * S, 520 * S))

sm = Image.new("L", screen.size, 255)
smd = ImageDraw.Draw(sm)
smd.rounded_rectangle([0, 0, PW * S - 1, PH * S - 1], radius=RAD * S, fill=255)
screen.putalpha(sm)

# vignetta + alsó/felső sötétítés a HUD olvashatóságához
grad = Image.new("L", (1, PH * S), 0)
gd = ImageDraw.Draw(grad)
for y in range(PH * S):
    yy = y / (PH * S)
    a = 0
    if yy < 0.22:
        a = int(210 * (1 - yy / 0.22))
    elif yy > 0.60:
        a = int(190 * ((yy - 0.60) / 0.40) ** 1.4)
    gd.point((0, y), fill=min(a, 235))
grad = grad.resize((PW * S, PH * S))
scrim = Image.new("RGBA", screen.size, (8, 6, 12, 0))
scrim.putalpha(grad)
screen = Image.alpha_composite(screen, scrim)

# =============================================================== HUD ==========
# (minden koordináta a telefon-képernyő lokális koordinátarendszerében: 900x1640)
d = ImageDraw.Draw(screen)
TOP = f(FONTS, 17)
MID = f(FONTB, 15)
SML = f(FONT, 13)
SMLB = f(FONTB, 13)
TNY = f(FONT, 11)

# ------------------------------------------------------ BAL ALSÓ: JOYSTICK --
jx, jy, jr = 178, 1408, 116
circle(d, jx, jy, jr + 14, fill=(10, 8, 14, 90))
circle(d, jx, jy, jr, fill=(255, 255, 255, 14), outline=(238, 226, 200, 105), width=2.5)
circle(d, jx, jy, jr * 0.52, fill=(238, 226, 200, 46), outline=(238, 226, 200, 130), width=2)
for ang in [(0, 0), (1, 0), (0, 1)]:
    pass
# irányjelző pöttyök
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    circle(d, jx + dx * (jr - 12), jy + dy * (jr - 12), 3.2, fill=(238, 226, 200, 160))
text(d, (jx, jy + jr + 26), "JOYSTICK – MOZGÁS", MID, DIM, anchor="ma")

# --------------------------------------------------- JOBB ALSÓ: HARCGOMBOK --
btns = [
    # (x, y, r, ikon, felirat, kiemelt)
    (690, 1408, 88, "axe", "ÜTÉS 1", True),
    (838, 1272, 62, "gun", "ÜTÉS 3", False),
    (538, 1278, 62, "hammer", "ÜTÉS 2", False),
    (546, 1468, 56, "shield", "VÉD", False),
    (700, 1572, 60, "dash", "KITÉRÉS", False),
]


def icon(d, kind, cx, cy, r, col=INK):
    lw = max(1.6, r * 0.10)
    if kind == "axe":
        d.line([(cx - r * 0.5) * S, (cy + r * 0.6) * S, (cx + r * 0.35) * S, (cy - r * 0.55) * S],
               fill=col, width=int(lw * S))
        d.polygon([(cx + r * 0.05) * S, (cy - r * 0.62) * S, (cx + r * 0.72) * S, (cy - r * 0.15) * S,
                   (cx + r * 0.20) * S, (cy + r * 0.22) * S], outline=col, width=int(lw * S))
    elif kind == "gun":
        d.rounded_rectangle([(cx - r * 0.65) * S, (cy - r * 0.22) * S, (cx + r * 0.62) * S, (cy + r * 0.05) * S],
                            radius=r * 0.12 * S, outline=col, width=int(lw * S))
        d.arc([(cx - r * 0.22) * S, (cy - r * 0.12) * S, (cx + r * 0.14) * S, (cy + r * 0.42) * S],
              180, 360, fill=col, width=int(lw * S))
        d.line([(cx - r * 0.30) * S, (cy + r * 0.44) * S, (cx - r * 0.52) * S, (cy + r * 0.05) * S],
               fill=col, width=int(lw * S))
    elif kind == "hammer":
        d.line([(cx - r * 0.45) * S, (cy + r * 0.60) * S, (cx + r * 0.18) * S, (cy - r * 0.20) * S],
               fill=col, width=int(lw * S))
        d.rounded_rectangle([(cx - r * 0.02) * S, (cy - r * 0.66) * S, (cx + r * 0.62) * S, (cy - r * 0.18) * S],
                            radius=r * 0.08 * S, outline=col, width=int(lw * S))
    elif kind == "shield":
        d.polygon([(cx - r * 0.55) * S, (cy - r * 0.48) * S, (cx + r * 0.55) * S, (cy - r * 0.48) * S,
                   (cx + r * 0.42) * S, (cy + r * 0.18) * S, (cx) * S, (cy + r * 0.66) * S,
                   (cx - r * 0.42) * S, (cy + r * 0.18) * S], outline=col, width=int(lw * S))
    elif kind == "dash":
        for i, off in enumerate([-0.30, 0.10, 0.50]):
            d.line([(cx - r * 0.60 + r * off) * S, (cy - r * 0.55) * S,
                    (cx - r * 0.05 + r * off) * S, (cy) * S], fill=col, width=int(lw * S))
            d.line([(cx - r * 0.05 + r * off) * S, (cy) * S,
                    (cx - r * 0.60 + r * off) * S, (cy + r * 0.55) * S], fill=col, width=int(lw * S))
    elif kind == "hatchet":
        d.line([(cx - r * 0.42) * S, (cy + r * 0.58) * S, (cx + r * 0.22) * S, (cy - r * 0.32) * S],
               fill=col, width=int(lw * S))
        d.polygon([(cx + r * 0.0) * S, (cy - r * 0.30) * S, (cx + r * 0.58) * S, (cy - r * 0.02) * S,
                   (cx + r * 0.10) * S, (cy + r * 0.30) * S], outline=col, width=int(lw * S))
    elif kind == "revolver":
        d.rounded_rectangle([(cx - r * 0.60) * S, (cy - r * 0.20) * S, (cx + r * 0.58) * S, (cy + r * 0.06) * S],
                            radius=r * 0.12 * S, outline=col, width=int(lw * S))
        d.arc([(cx - r * 0.18) * S, (cy - r * 0.10) * S, (cx + r * 0.18) * S, (cy + r * 0.40) * S],
              180, 360, fill=col, width=int(lw * S))
        d.line([(cx - r * 0.28) * S, (cy + r * 0.42) * S, (cx - r * 0.48) * S, (cy + r * 0.06) * S],
               fill=col, width=int(lw * S))
    elif kind == "crossbow":
        d.arc([(cx - r * 0.62) * S, (cy - r * 0.62) * S, (cx + r * 0.62) * S, (cy + r * 0.30) * S],
              200, 340, fill=col, width=int(lw * S))
        d.line([(cx - r * 0.62) * S, (cy + r * 0.06) * S, (cx) * S, (cy - r * 0.16) * S, ], fill=col, width=int(lw * S))
        d.line([(cx + r * 0.62) * S, (cy + r * 0.06) * S, (cx) * S, (cy - r * 0.16) * S], fill=col, width=int(lw * S))
        d.line([(cx) * S, (cy - r * 0.16) * S, (cx) * S, (cy + r * 0.62) * S], fill=col, width=int(lw * S))
    elif kind == "trap":
        d.arc([(cx - r * 0.60) * S, (cy - r * 0.42) * S, (cx + r * 0.60) * S, (cy + r * 0.42) * S],
              0, 360, fill=col, width=int(lw * S))
        for i in range(8):
            import math
            a = math.radians(i * 45)
            x1 = cx + math.cos(a) * r * 0.60
            y1 = cy + math.sin(a) * r * 0.42
            x2 = cx + math.cos(a) * r * 0.86
            y2 = cy + math.sin(a) * r * 0.60
            d.line([x1 * S, y1 * S, x2 * S, y2 * S], fill=col, width=int(lw * S))
    elif kind == "potion":
        d.rounded_rectangle([(cx - r * 0.28) * S, (cy - r * 0.72) * S, (cx + r * 0.28) * S, (cy - r * 0.36) * S],
                            radius=r * 0.08 * S, outline=col, width=int(lw * S))
        d.ellipse([(cx - r * 0.56) * S, (cy - r * 0.34) * S, (cx + r * 0.56) * S, (cy + r * 0.72) * S],
                  outline=col, width=int(lw * S))
        d.ellipse([(cx - r * 0.42) * S, (cy + r * 0.06) * S, (cx + r * 0.42) * S, (cy + r * 0.62) * S], fill=col)


for bx, by, br, k, lab, hi in btns:
    circle(d, bx, by, br + 9, fill=(10, 8, 14, 120))
    circle(d, bx, by, br, fill=(28, 22, 30, 210) if not hi else (46, 28, 26, 225),
           outline=AMBER if hi else (238, 226, 200, 120), width=3 if hi else 2.5)
    icon(d, k, bx, by - br * 0.06, br * 0.70)
    text(d, (bx, by + br + 15), lab, SMLB if hi else SML, INK if hi else DIM, anchor="ma")

# ------------------------------------------------ KÖZÉP: FEGYVERVÁLASZTÓ --
wx, wy = 450, 790
circle(d, wx, wy, 176, fill=(10, 8, 14, 60), outline=(238, 226, 200, 55), width=2)
ring_arc(d, wx, wy, 176, 0, 360, (238, 226, 200, 55), 2)
slots = [
    (wx + 150, wy, "revolver", "REVOLVER", False),
    (wx - 150, wy, "crossbow", "SZÁMSZERÍJ", False),
    (wx, wy + 150, "trap", "CSAPDA", False),
    (wx, wy - 150, "hatchet", "BALTA", True),
]
for sx, sy, k, lab, sel in slots:
    circle(d, sx, sy, 40, fill=(26, 20, 28, 220), outline=AMBER if sel else (238, 226, 200, 110), width=3 if sel else 2)
    icon(d, k, sx, sy, 26)
    text(d, (sx, sy + 56), lab, TNY, INK if sel else DIM, anchor="ma")
circle(d, wx, wy, 62, fill=(22, 16, 24, 230), outline=AMBER, width=3)
icon(d, "hatchet", wx, wy - 2, 40)
text(d, (wx, wy + 262), "FEGYVERVÁLASZTÓ – KÉPERNYŐ KÖZEPE", MID, DIM, anchor="ma")
text(d, (wx, wy + 284), "(a hüvelykujj középre csúsztatásával jelenik meg)", SML, (238, 226, 200, 110), anchor="ma")

# ------------------------------------------------------------ BAL FELSŐ ----
mm = (28, 28, 268, 268)
rrect(d, mm, 14, fill=(12, 10, 16, 210), outline=(238, 226, 200, 120), width=2.5)
# térkép tartalom
rrect(d, (40, 40, 256, 256), 8, fill=(28, 24, 34, 235))
import math
d.line([(40 + 8) * S, 150 * S, 256 * S, 132 * S], fill=(120, 106, 96, 220), width=int(11 * S))  # főút
d.line([(120) * S, 40 * S, 138 * S, 256 * S], fill=(120, 106, 96, 190), width=int(8 * S))
d.line([(196) * S, 130 * S, 250 * S, 236 * S], fill=(120, 106, 96, 170), width=int(6 * S))
for hx, hy, hw, hh in [(56, 168, 34, 26), (100, 60, 30, 24), (196, 62, 38, 30), (208, 170, 30, 28), (58, 76, 26, 22)]:
    rrect(d, (hx, hy, hx + hw, hy + hh), 3, fill=(72, 62, 56, 235), outline=(150, 136, 120, 120), width=1)
# folyó / mocsár
d.line([(44) * S, 232 * S, 110 * S, 244 * S, 180 * S, 236 * S, 252 * S, 246 * S],
       fill=(52, 84, 96, 200), width=int(9 * S), joint="curve")
# POI-k
for px_, py_, col, lab in [(214, 74, ACCENT, "R"), (86, 196, GREEN, "P"), (180, 214, AMBER, "!")]:
    circle(d, px_, py_, 11, fill=(12, 10, 16, 235), outline=col, width=3)
    text(d, (px_, py_ + 1), lab, f(FONTB, 12), col, anchor="mm")
# játékos nyíl
circle(d, 138, 150, 13, fill=(12, 10, 16, 235), outline=INK, width=2)
d.polygon([(138) * S, (137) * S, (146) * S, (155) * S, (138) * S, (151) * S, (130) * S, (155) * S], fill=INK)
text(d, (148, 46), "N", SMLB, DIM, anchor="ma")
text(d, (148, 276), "MINIMAP", MID, DIM, anchor="ma")

# HP-sáv a minimap alatt
hb = (28, 300, 268, 326)
rrect(d, hb, 8, fill=(12, 10, 16, 215), outline=(238, 226, 200, 110), width=2)
rrect(d, (32, 304, 32 + int(232 * 0.78), 322), 6, fill=(168, 46, 40, 235))
text(d, (148, 334), "HP  (javaslat: ide, a minimap alá)", TNY, (238, 226, 200, 130), anchor="ma")

# ----------------------------------------------------------- JOBB FELSŐ ----
text(d, (872, 24), "POTIK", MID, DIM, anchor="ra")
potions = [
    (668, 82, "potion", (196, 64, 56), "2", "gyógy"),
    (764, 82, "potion", (226, 158, 60), "1", "erő"),
    (860, 82, "potion", (96, 190, 210), "3", "látás"),
]
for px_, py_, k, col, cnt, lab in potions:
    circle(d, px_, py_, 44, fill=(10, 8, 14, 130))
    circle(d, px_, py_, 38, fill=(26, 20, 28, 220), outline=(238, 226, 200, 120), width=2.5)
    icon(d, k, px_, py_ - 2, 30, col)
    circle(d, px_ + 30, py_ + 30, 16, fill=(12, 10, 16, 245), outline=col, width=2)
    text(d, (px_ + 30, py_ + 31), cnt, f(FONTB, 15), INK, anchor="mm")
    text(d, (px_, py_ + 62), lab, TNY, DIM, anchor="ma")
text(d, (860, 168), "(töltés: sárga gyűrű körülötte)", TNY, (238, 226, 200, 105), anchor="ra")

# =================================================== ANNOTÁCIÓS OSZLOP =======
col = ImageDraw.Draw(canvas)
text(col, (40, 70), "KONTROLL & HUD", f(FONTS, 26), INK)
text(col, (40, 104), "egykezes, hüvelykujjas", SML, DIM)


def item(y, dotcol, title, lines):
    circle(col, 52, y + 4, 6, fill=dotcol)
    text(col, (70, y), title, MID, INK)
    yy = y + 20
    for ln in lines:
        text(col, (70, yy), ln, SML, DIM)
        yy += 17
    return yy + 16


y = 150
y = item(y, (238, 226, 200, 255), "Bal alsó – joystick",
         ["Bal hüvelykujj: szabad mozgás,", "bármilyen irányba. Fix pozíció,",
          "nem úszik el (mozgás közben", "biztonságosabb)."])
y = item(y, AMBER, "Jobb alsó – 5 harcgomb",
         ["3 ütés (balta / nehéz / lő),", "1 védekezés, 1 kitérés.",
          "A fő ütés a legnagyobb és", "legközelebb a hüvelykujjhoz."])
y = item(y, (232, 164, 68, 255), "Közép – fegyverválasztó",
         ["Kör alakú gyorsválasztó,", "csak váltáskor jelenik meg;",
          "középen a jelenlegi fegyver.", "Lásd: tipp a lap alján."])
y = item(y, INK, "Bal felső – minimap",
         ["N, játékos-nyíl, POI-jelölők:", "R = római helyőrség,  P = poti/bolt,",
          "!  = küldetés. Alatta HP-sáv."])
y = item(y, CYAN, "Jobb felső – potik",
         ["3 ikon darabszámmal:", "gyógyító, erő, éjszakai látás.",
          "Gyűrű = töltés (cooldown)."])

text(col, (40, H - 300), "Amit érdemes még átgondolni:", MID, INK)
notes = [
    "• A középre nyúlás mobilon kényelmetlen –",
    "  a fegyverváltót tedd a jobb hüvelykujj",
    "  alá (rövid húzás a képernyőn), vagy",
    "  tegyél ki egy kompakt fegyver-sávot.",
    "• Nem volt HP-sáv a felsorolásban:",
    "  a minimap alá került (1070 képpont).",
    "• A 2 NPC vadász kaphat kis portré-",
    "  jelzést a minimapon, hogy lásd, hol van.",
]
yy = H - 274
for ln in notes:
    text(col, (40, yy), ln, SML, DIM)
    yy += 17

# ------------------------------------------------------------ telefon-keret -
frame = ImageDraw.Draw(canvas)
canvas.alpha_composite(screen, (PX * S, PY * S))
rrect(frame, (PX, PY, PX + PW, PY + PH), RAD, outline=(70, 58, 52, 255), width=6)
rrect(frame, (PX + 330, PY + 16, PX + 570, PY + 40), 12, fill=(20, 16, 22, 255),
      outline=(70, 58, 52, 255), width=3)
for hy in [(PY + 1520, PY + 1536)]:
    rrect(frame, (PX + 380, hy[0], PX + 520, hy[1]), 8, fill=(238, 226, 200, 60))

out = canvas.resize((W, H), Image.LANCZOS).convert("RGB")
out.save("kontroll_es_hud_terv.png", quality=95)
print("kész:", out.size)
