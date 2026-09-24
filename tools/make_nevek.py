#!/usr/bin/env python3
"""Névjelölt-mockup: 3 cím a key artra égetve (pontos betűkkel, nem AI-generálva)."""
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONTSB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
S = 2

INK = (238, 226, 200)
CREAM = (240, 232, 210)
GOLD = (203, 168, 78)
BRASS = (201, 162, 39)
GREEN = (150, 226, 156)
RED = (198, 74, 56)
DIM = (238, 226, 200, 175)

W, H = 2120, 1560
im = Image.new("RGBA", (W * S, H * S), (12, 9, 14, 255))


def text(d, xy, s, font, fill, anchor="la"):
    d.text((xy[0] * S, xy[1] * S), s, font=font, fill=fill, anchor=anchor)


def spaced(d, xy, s, font, fill, sp, anchor="ma"):
    """Betűközzel írt szöveg (címekhez)."""
    widths = [d.textlength(ch, font=font) / S for ch in s]
    total = sum(widths) + sp * (len(s) - 1)
    x = xy[0] - total / 2 if anchor == "ma" else (xy[0] - total if anchor == "ra" else xy[0])
    for ch, w in zip(s, widths):
        d.text((x * S, xy[1] * S), ch, font=font, fill=fill, anchor="ls")
        x += w + sp
    return total


def f(p, s):
    return ImageFont.truetype(p, int(s * S))


# ---------------------------------------------------------------- fejléc ----
d = ImageDraw.Draw(im)
text(d, (60, 40), "NÉVJELÖLTEK — A DÖNTÉS: CARO DEORUM", f(FONTSB, 30), INK)
text(d, (60, 84), "A választott cím a CARO DEORUM (a bal oldali). Ez a lap a döntés dokumentuma; a logó-változatok a caro_deorum_logo.png fájlon.",
     f(FONT, 15), DIM)

CANDS = [
    dict(
        title="CARO DEORUM", lang="latin", font="serifb", size=44, sp=7, col=GOLD,
        accent=("ISTENHÚS", "a kő neve a légiósok száján"),
        tag="A vadnyugat, amit Róma ural —\nés a mágia, amit négyszáz éve betiltottak.",
        why="A világ hivatalos nyelve a latin, tehát a cím is az. Jelentése: „az istenek húsa” —\na kő szlengje a birodalmi katonák között. Egyszerre szép és hátborzongató,\nés a történet végső helyszíne is így hívják (Caro Deorum kráter).",
        hue=(18, 14, 20, 210),
    ),
    dict(
        title="SALT AND IRON", lang="SÓ ÉS VAS", font="sansb", size=40, sp=9, col=CREAM,
        accent=("SÓ ÉS VAS", "a két anyag, ami a szörnyeket öli"),
        tag="A világ a gőzben hisz.\nA vadászok tudják, mi működik igazán.",
        why="A folkloréban a só és a vas űzi el a szellemeket — a játékban ez a vadászok\ntudománya, szemben a birodalom gőz-technológiájával. Angol és magyar cím\nugyanaz: ritka és erős páros egy Steamen megjelenő játéknál.",
        hue=(22, 12, 12, 210),
    ),
    dict(
        title="HOLLOWMIER", lang="a város", font="serifb", size=44, sp=6, col=GREEN,
        accent=("HOLLOWMIER", "a gyarmat fővárosa a Hollow partján"),
        tag="Ahol a márvány és a korom\nugyanabban az utcában lakik.",
        why="A helynév mint cím — mint a Bloodborne Yharnamja vagy a Hollow Knight Hallownestje.\nNyugati hangzás, kísérteties jelentés („hollow” = üreges). Ha a sorozat bővül,\na cím a városhoz kötődik, a világ köré épül.",
        hue=(12, 20, 16, 210),
    ),
]

px, py, pw, ph = 60, 150, 640, 1146
gap = 40
key = Image.open("/home/user/koncepcio/24_keyart_vesper.png").convert("RGB")

for i, c in enumerate(CANDS):
    x = px + i * (pw + gap)
    cover = key.resize((pw * S, ph * S), Image.LANCZOS).convert("RGBA")

    # felső és alsó sötétítő sáv a szöveg olvashatóságához
    grad = Image.new("L", (1, ph * S), 0)
    gd = ImageDraw.Draw(grad)
    for y in range(ph * S):
        t = y / (ph * S)
        a = 0
        if t < 0.30:
            a = int(235 * (1 - t / 0.30) ** 0.7)
        elif t > 0.72:
            a = int(235 * ((t - 0.72) / 0.28) ** 0.8)
        gd.point((0, y), fill=min(a, 240))
    strip = Image.new("RGBA", cover.size, c["hue"])
    strip.putalpha(grad.resize(cover.size))
    cover = Image.alpha_composite(cover, strip)

    im.alpha_composite(cover, (x * S, py * S))
    cd = ImageDraw.Draw(im)
    cd.rounded_rectangle([x * S, py * S, (x + pw) * S, (py + ph) * S], radius=8 * S,
                         outline=(90, 74, 66, 255), width=4 * S)

    # nyelv / műfaj jelölés
    text(cd, (x + pw / 2, py + 34), c["lang"], f(FONTB, 15), (238, 226, 200, 190), anchor="ma")

    # cím
    fonts_map = {"serifb": FONTSB, "sansb": FONTB}
    tw = spaced(cd, (x + pw / 2, py + 130), c["title"], f(fonts_map[c["font"]], c["size"]), c["col"] + (255,), c["sp"])
    # vonal a cím alatt
    cd.line([((x + pw / 2 - tw / 2) * S, (py + 148) * S), ((x + pw / 2 + tw / 2) * S, (py + 148) * S)],
            fill=c["col"] + (200,), width=int(2 * S))

    # akcentus + tagline az alsó sávban
    accent, sub = c["accent"]
    text(cd, (x + pw / 2, py + ph - 128), accent, f(FONTSB, 21), c["col"] + (255,), anchor="ma")
    text(cd, (x + pw / 2, py + ph - 100), sub, f(FONT, 13.5), (238, 226, 200, 200), anchor="ma")
    for k, line in enumerate(c["tag"].split("\n")):
        text(cd, (x + pw / 2, py + ph - 62 + k * 26), line, f(FONTS, 18), CREAM + (255,), anchor="ma")

    # indoklás a kép alatt
    yy = py + ph + 26
    text(cd, (x + 8, yy), "MIÉRT JÓ:", f(FONTB, 13.5), c["col"] + (255,))
    for k, line in enumerate(c["why"].split("\n")):
        text(cd, (x + 8, yy + 24 + k * 22), line, f(FONT, 13.5), DIM)

# ---------------------------------------------------------------- lábléc ----
y0 = py + ph + 26 + 24 + 3 * 22 + 26
d = ImageDraw.Draw(im)
text(d, (60, y0), "TOVÁBBI JELÖLTEK (tartalék):", f(FONTB, 14), INK)
extra = ("LAPIS SANGUINIS (latin: vérkő) · VIGIL OF CROWS (a Varjú és a hollók) · "
         "A MURDER OF HUNTERS („murder” = varjúcsapat — Vesper nevére és a csapatra is utal) · "
         "EZÜST ÉS GŐZ · SILVER AND SALT · HOLLOW FRONTIER · A VASKONZÍLIUM (Edictum Lapidis)")
text(d, (60, y0 + 26), extra, f(FONT, 13), DIM)
text(d, (60, y0 + 54), "Kerülendő: Vérkő (David Gemmell-regény magyar címe ugyanebben a műfajban) · Godflesh (zenekar) · Cold Iron (létező VR-játék) · Salt & Sanctuary-rokonság miatt a „Salt and X” forma kockázatos.",
     f(FONT, 13), (198, 120, 100, 255))

out = im.resize((W, H), Image.LANCZOS).convert("RGB")
out.save("/home/user/koncepcio/nevek_mockup.png", quality=95)
print("kész", out.size)
