#!/usr/bin/env python3
"""Színpaletta-lap a key artból: kinyert színek + felhasználási szabály."""
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

INK = (238, 226, 200)
DIM = (238, 226, 200, 165)
S = 2


def f(p, s):
    return ImageFont.truetype(p, int(s * S))


W, H = 1500, 1060
im = Image.new("RGBA", (W * S, H * S), (14, 11, 17, 255))
d = ImageDraw.Draw(im)


def text(xy, s, font, fill, anchor="la"):
    d.text((xy[0] * S, xy[1] * S), s, font=font, fill=fill, anchor=anchor)


def rrect(xy, r, fill=None, outline=None, width=2):
    d.rounded_rectangle([xy[0] * S, xy[1] * S, xy[2] * S, xy[3] * S], radius=r * S,
                        fill=fill, outline=outline, width=int(width * S))


# keyart bal oldalra
key = Image.open("11_keyart_1800.png").convert("RGB")
kh = 760
kw = int(key.width * kh / key.height)
key = key.resize((kw * S, kh * S), Image.LANCZOS)
im.alpha_composite(key.convert("RGBA"), (40 * S, 96 * S))
rrect((40, 96, 40 + kw, 96 + kh), 6, outline=(70, 58, 52, 255), width=4)

# színek kinyerése
q = Image.open("09_salem_1800.png").convert("RGB").resize((260, 160))
q = q.quantize(colors=14, method=Image.MEDIANCUT).convert("RGB")
cols = sorted(q.getcolors(100000), reverse=True)
cols = [c for _, c in cols]
cols = [c for c in cols if sum(c) > 60][:6]

x0 = 40 + kw + 50
text((x0, 60), "SZÍNPALETTA", f(FONTS, 30), INK)
text((x0, 100), "a key artból kinyerve – ezt tartsd a teljes játékban", f(FONT, 15), DIM)

text((x0, 150), "Környezet & semleges", f(FONTB, 15), INK)
y = 176
for c in cols[:6]:
    rrect((x0, y, x0 + 90, y + 46), 6, fill=c + (255,), outline=(255, 255, 255, 40), width=1)
    text((x0 + 106, y + 6), "#%02X%02X%02X" % c, f(FONTB, 15), INK)
    text((x0 + 106, y + 26), "R%d G%d B%d" % c, f(FONT, 12), DIM)
    y += 56

text((x0, y + 14), "Kiemelések – csak ezekre a célokra használd", f(FONTB, 15), INK)
y += 42
ACCENTS = [
    ((214, 92, 60), "TŰZ / RÓMAI VÖRÖS", "gyújtás, robbanás, legionárius jelvény, HP-vesztes"),
    ((232, 164, 68), "LÁMPA / BOROSTYÁN", "fényforrás, tűz, potion-ikon, a UI aktív elemei"),
    ((130, 220, 140), "METEOR-ZÖLD", "varázs, szörny-lélek, a kövek ereje, kivégzés-FX"),
    ((150, 196, 214), "HOLDFÉNY / CIÁN", "szellemek, köd, éjszakai ambient, ghost-anya"),
    ((238, 226, 200), "CSONTFEHÉR", "UI szöveg, csontok, kiemelések, kontúrok"),
]
for c, name, use in ACCENTS:
    rrect((x0, y, x0 + 90, y + 46), 6, fill=c + (255,), outline=(255, 255, 255, 60), width=1)
    text((x0 + 106, y + 2), name, f(FONTB, 15), INK)
    text((x0 + 106, y + 21), "#%02X%02X%02X" % c, f(FONT, 12), c + (255,))
    text((x0 + 106, y + 36), use, f(FONT, 12), DIM)
    y += 62

text((x0, y + 12), "Szabályok, amik összetartják a látványt", f(FONTB, 15), INK)
y += 40
rules = [
    "1. A varázs/szörny-lélek ERA mindig zöld, minden más marad fakó – ez adja",
    "    a „hol van a varázslat” vizuális nyelvét.",
    "2. Minden fényforrás meleg (borostyán), minden árnyék hűvös (lila-kék).",
    "3. A római jelenlét vörös+arany+fehér márvány; a telepes jelenlét fa+barna+szürke.",
    "4. A szörnyeknek erős sziluettjük legyen kis méretben is (balta, kalap, csuklya).",
    "5. Szellemeknél SOHA ne legyen tömör fekete kontúr – halvány, lebegő körvonal.",
]
for r in rules:
    text((x0, y), r, f(FONT, 13.5), DIM)
    y += 20

out = im.resize((W, H), Image.LANCZOS).convert("RGB")
out.save("paletta.png", quality=95)
print("kész", out.size)
