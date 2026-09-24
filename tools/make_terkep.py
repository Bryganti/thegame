#!/usr/bin/env python3
"""A világ térképe: 4 régió + a Legio Rail gőzvonal-hálózata + küldetés-adatok."""
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
S = 2

INK = (238, 226, 200, 255)
DIM = (238, 226, 200, 165)
ACCENT = (196, 62, 48, 255)
AMBER = (232, 164, 68, 255)
GREEN = (108, 214, 120, 255)
BRASS = (201, 162, 39, 255)
CYAN = (120, 196, 214, 255)
PARCH = (32, 26, 24, 255)


def f(p, s):
    return ImageFont.truetype(p, int(s * S))


def text(d, xy, s, font, fill, anchor="la"):
    d.text((xy[0] * S, xy[1] * S), s, font=font, fill=fill, anchor=anchor)


def rrect(d, xy, r, fill=None, outline=None, width=2):
    d.rounded_rectangle([xy[0] * S, xy[1] * S, xy[2] * S, xy[3] * S], radius=r * S,
                        fill=fill, outline=outline, width=int(width * S))


def circle(d, cx, cy, r, fill=None, outline=None, width=2):
    d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
              fill=fill, outline=outline, width=int(width * S))


HUE = {
    1: (86, 74, 60),      # város — meleg szürkésbarna
    2: (74, 58, 46),      # erdő/bánya — korom
    3: (44, 62, 70),      # mocsár — hűvös kék
    4: (52, 66, 52),      # kráter — zöld
}

REG = {
    1: dict(n=1, name="HOLLOWMIER ÉS KÜLTERÜLETE", szint="1–5. szint", q=22,
            places="Hollowmier (7 negyed · Saloon-negyed, Fórum, Gőznegyed, Akasztófa-tér, Kikötő, Kráter-domb, régi negyedek) · Kráter-domb · kikötő · külterületi tanyák",
            fam="zombi · vámpír-szolga · kísértet · gólem (prototípus) · farkasember (első)",
            boss="A Kráter-domb őre (mini-boss) · A Vigiles pecsétje (történet-döntés)",
            note="A tanuló régió: itt nyílik a tábortűz, a szerződés-tábla és a bestiárium."),
    2: dict(n=2, name="BLACKBRIAR · VERHOLLOW · NEEDLE RIDGE", szint="5–10. szint", q=22,
            places="Blackbriar (szénégető telep) · Verhollow (bánya és kohó) · Needle Ridge (sziklahegy-hát)",
            fam="farkasember · zombi (bányász) · gólem (agyag-katona) · kísértet · alkat",
            boss="VÉRNÁSZ ★ (legendás) · A mélység (legendás horda)",
            note="Itt derül ki, hogy az agyag-katonák és a vérnász-fiak egyazon műhelyből jönnek."),
    3: dict(n=3, name="SORROW'S REACH · A HIDAK · GALLOWMERE", szint="8–14. szint", q=22,
            places="Sorrow's Reach (félig víz alá került folyófalu) · A Hidak (Gray-híd és komp) · Gallowmere (kápolna, temető)",
            fam="vámpír · kísértet · szellem · léleklámpás · fejnélküli lovas",
            boss="FEJNÉLKÜLI LOVAS ★ (3 fázis) · Karmazsin asszony udvartartása (elit)",
            note="A víz itt mindent megőriz — köztük a fiú nyomát is. A harang a fegyver."),
    4: dict(n=4, name="LAPIDES ULULANTES · CARO DEORUM", szint="12–18. szint", q=22,
            places="Lapides Ululantes (a tiltás kőoszlopai) · zarándok-tábor · Caro Deorum (a legfrissebb kráter) · a szentély alatti labor",
            fam="múmia (Vetchet király) · gólem · kísérlet (alkat) · zombi (mélység) · a Vén Kígyó",
            boss="VALERIUS MENENIUS ★★ (végső) · Karmazsin asszony ★ (ha életben maradt)",
            note="A vonal vége: a gőzvasutat Blackwood építette — hogy a köveket elszállítsa."),
}

W, H = 2100, 1520
im = Image.new("RGBA", (W * S, H * S), (14, 11, 16, 255))
d = ImageDraw.Draw(im)

# ---------------------------------------------------------------- fejléc ----
text(d, (60, 40), "A VILÁG TÉRKÉPE — 4 RÉGIÓ, 88 KÜLDETÉS", f(FONTS, 32), INK)
text(d, (60, 84), "A régiók között CSAK a Legio Rail gőzvonatával lehet közlekedni: jegy kell hozzá, és a járatok nappal indulnak — éjszaka a szerelvény nem hagyja el az állomást.",
     f(FONT, 15), DIM)

# ------------------------------------------------------------- vashálózat ---
band = (60, 130, W - 60, 400)
rrect(d, band, 16, fill=(20, 16, 22, 255), outline=(70, 58, 52, 255), width=3)
text(d, (90, 152), "LEGIO RAIL — FŐVONAL", f(FONTB, 17), BRASS)

xs = [300, 780, 1260, 1790]
ly = 270
d.line([(xs[0]) * S, ly * S, (xs[-1]) * S, ly * S], fill=BRASS, width=int(7 * S))
# sínek
d.line([(xs[0]) * S, (ly - 9) * S, (xs[-1]) * S, (ly - 9) * S], fill=(140, 112, 40, 200), width=int(2 * S))
d.line([(xs[0]) * S, (ly + 9) * S, (xs[-1]) * S, (ly + 9) * S], fill=(140, 112, 40, 200), width=int(2 * S))

for i, x in enumerate(xs):
    r = REG[i + 1]
    # állomás
    circle(d, x, ly, 26, fill=(16, 12, 18, 255), outline=BRASS, width=4)
    circle(d, x, ly, 11, fill=BRASS)
    text(d, (x, ly), str(r["n"]), f(FONTB, 15), (16, 12, 18), anchor="mm")
    # régió-név
    text(d, (x, ly - 78), r["name"].split(" · ")[0], f(FONTB, 18), INK, anchor="ma")
    text(d, (x, ly - 52), r["szint"] + " · " + str(r["q"]) + " küldetés", f(FONTB, 14), AMBER, anchor="ma")
    text(d, (x, ly + 52), r["places"].split(" · ")[0], f(FONT, 13), DIM, anchor="ma")
    # mellékállomások
    for j, off in enumerate((-58, 58)):
        circle(d, x + off, ly, 7, fill=(16, 12, 18, 255), outline=(180, 150, 60, 230), width=2)

text(d, (xs[0], ly + 118), "Hollowmier Grand Station", f(FONT, 12.5), DIM, anchor="ma")
text(d, (xs[1], ly + 118), "Blackbriar Halt · Verhollow Teherpálya", f(FONT, 12.5), DIM, anchor="ma")
text(d, (xs[2], ly + 118), "Sorrow's Reach Megálló · Gallowmere Révpart", f(FONT, 12.5), DIM, anchor="ma")
text(d, (xs[3], ly + 118), "Végállomás: Caro Deorum (zarándokvonal)", f(FONT, 12.5), DIM, anchor="ma")

# --------------------------------------------------------------- kártyák ----
CW, CH = 975, 400
positions = [(60, 442), (60 + CW + 30, 442), (60, 442 + CH + 28), (60 + CW + 30, 442 + CH + 28)]
for i, (x, y) in enumerate(positions):
    r = REG[i + 1]
    c = HUE[i + 1]
    rrect(d, (x, y, x + CW, y + CH), 16, fill=(24, 19, 24, 255), outline=c, width=3)
    rrect(d, (x, y, x + 106, y + CH), 16, fill=(c[0], c[1], c[2], 255))
    rrect(d, (x + 46, y, x + 106, y + CH), 0, fill=(c[0], c[1], c[2], 255))
    text(d, (x + 34, y + 34), str(r["n"]), f(FONTS, 46), INK, anchor="la")
    text(d, (x + 132, y + 34), r["name"], f(FONTS, 21), INK)
    text(d, (x + 132, y + 68), r["szint"] + "   ·   " + str(r["q"]) + " küldetés", f(FONTB, 14.5), AMBER)

    def block(yy, label, body, col=INK):
        text(d, (x + 132, yy), label, f(FONTB, 13.5), col)
        # tördelés
        words, line, lines = body.split(), "", []
        for w in words:
            t = (line + " " + w).strip()
            if len(t) > 92:
                lines.append(line)
                line = w
            else:
                line = t
        lines.append(line)
        for k, ln in enumerate(lines):
            text(d, (x + 132, yy + 20 + k * 19), ln, f(FONT, 13), DIM)
        return yy + 26 + len(lines) * 19

    yy = block(y + 104, "HELYSZÍNEK", r["places"])
    yy = block(yy + 6, "SZÖRNYCSALÁDOK", r["fam"], GREEN)
    yy = block(yy + 6, "BOSS / CSÚCSPONT", r["boss"], ACCENT)
    yy = block(yy + 6, "MIÉRT FONTOS", r["note"], CYAN)

# ---------------------------------------------------------------- lábléc ----
y0 = 442 + 2 * CH + 28 + 34
rrect(d, (60, y0, W - 60, y0 + 200), 14, fill=(20, 16, 22, 255), outline=(70, 58, 52, 255), width=3)
text(d, (90, y0 + 22), "ÍGY LESZ 20+ KÜLDETÉS RÉGIÓNKÉNT — ÉS MIÉRT ISMÉTLŐDNEK A SZÖRNYEK", f(FONTB, 17), INK)

notes = [
    ("22 / régió", "5 történet + 8 tábla + 4 vizsgálat/mentés + 3 elit/legendás + 2 karakter = 22. Négy régió = 88 küldetés."),
    ("34 ismételhető", "a Tábla és az Elit küldetések ismételhetők: ugyanaz a szörnycsalád, de más helyszín, időpont (nappal/éjszaka) és szint."),
    ("Miért ismétlődnek?", "a szörnycsalád régióhoz kötött, mint az élővilág: mocsárban vámpír és kísértet, bányában zombi és gólem. Az ismétlés nem lustaság — ez a világ biológiája."),
    ("Miért nem unalmas?", "1) a 2. találkozásnál ismered a gyenge pontot → gyorsabb, taktikusabb harc; 2) az elit variáns új képességet kap; 3) a jutalom crafting-anyag a bossokhoz."),
    ("A tudás jutalom", "első találkozás: bestiárium-bejegyzés (gyenge pont, ölésmód). Ismétlés: ritka anyag és pénz. Ezért a grind is értelmes."),
    ("Tudomány vagy babona?", "a felszerelést (aether-detektor, gőz-gauntlet) a Mechanicus adja — a tudást (ezüst, karó, só, név) a vadászok. A kettő kiegészíti egymást."),
]
yy = y0 + 58
for t, sub in notes:
    text(d, (90, yy), "•", f(FONTB, 14), AMBER)
    text(d, (112, yy), t, f(FONTB, 13), INK)
    text(d, (420, yy), sub, f(FONT, 12.5), DIM)
    yy += 21

out = im.resize((W, H), Image.LANCZOS).convert("RGB")
out.save("regio_terkep.png", quality=95)
print("kész", out.size)
