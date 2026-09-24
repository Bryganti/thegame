#!/usr/bin/env python3
"""Vérkő — koncepció-galéria (cowboy aranykor + Róma + steampunk, izometrikus)."""
import base64, io
from PIL import Image

ITEMS = [
    ("regio_terkep.png", "A világ térképe — 4 régió, 88 küldetés", "A régiók között **csak a Legio Rail gőzvonatával** lehet közlekedni: jegy kell, és nappal indulnak. Régióként **22 küldetés** (5 történet + 8 tábla + 4 vizsgálat + 3 elit + 2 karakter) — négy régióban 88."),
    ("27_legio_rail.png", "A Legio Rail", "A gőzvasút-állomás: western fa-depó + márvány római oszlopok, sárgaréz szelepek, zöld üveglámpások. **Ez a régiók közötti egyetlen közlekedés** — és a IV. felvonás csattanója: a vonalat Blackwood építette, hogy a köveket szállítsa."),
    ("15_hollowmier.png", "Hollowmier", "A gyarmat fővárosa: western saloonok, márvány római fórum, gőz-akvadukt szelepekkel, Legio Rail, sárgaréz és korom — a háttérben a tiltott kráter zölden izzik."),
    ("24_keyart_vesper.png", "Vesper Crane — key art", "A játékos: **gladius és puska a hátán, 2 revolver és kés az övén, mellkasán ezüst lövedékes töltényöv** — a nyakában nincs kő."),
    ("21_vesper_jatekos.png", "Vesper Crane — karakterterv", "Részletes felszerelés-lap: gladius hüvelyben, iker revolver, vadászkés, ezüst lövedékes töltényöv és a sárgaréz **aether-detektor** (a tiltott mágia mérőműszere)."),
    ("22_harom_vadasz.png", "A három vadásztárs", "**Aurel Mercer** (mesterlövész, iker revolver) és **Gaius „Vén Medve” Thorne** (gőz-lábsín, potion-öv, só és vas). Ők ketten ülnek a tábortűznél Vesperrel — ők a rendszerek hangjai: Aurel a harcé, Thorne a főzeteké és a régi tudásé."),
    ("17_tabor_tuz.png", "A tábortűz", "Nem bázis: **egy tűz, körülötte a vadászok, és vándorol veled.** Potion-főzés, felkészülés, párbeszéd, mentés — a hub jön veled, nem kell ingázni."),
    ("23_izometrikus_vesper.png", "Játék közben — izometrikus", "A tényleges játékkamera (fekvő): 2:1 izometria, gyémánt talajlapok, saloonok, római oszlopok, sárgaréz gőzvezetékek, lámpásfény-kör Vesper körül."),
    ("kontroll_es_hud_fekvo.png", "Kontroll & HUD — FEKVŐ", "Joystick balra, **6 fegyveres vízszintes sáv alul középen** (gladius, balta, kés, revolver, sörétes, puska), 3 ütés + védekezés + kitérés jobbra, minimap és HP balra fent, potik jobbra fent."),
    ("13_romai_hatalom_cowboy.png", "Róma a vadnyugaton", "Városi rendőr (Vigiles), birodalmi katona, császári testőr (Praetoriani), szenátor és bounty marshal — cowboy ruhában, **felvarrt sas- és SPQR-jelvénnyel**, sárgaréz steampunk részletekkel."),
    ("25_fejnelkuli_lovas.png", "A fejnélküli lovas — BOSS", "Charon Walsh. **Amíg lovon ül és a lámpása ég, sérthetetlen.** Előbb meg kell állítani (harang, szentelt föld, só-vonal), el kell oltani a lámpást, és csak azután végezni vele ezüst pengével."),
    ("26_fogonos_magus.png", "Valerius Menenius — a Vén Kígyó", "**A fiú apja és a végső ellenség.** A legnagyobb mágus, aki valaha élt: ő robbantotta ki a Nagy Mágusháborút, és ő alkotja a szörnyeket. Testébe több követ varratott — négyszáz éve él. Polgári álcája: **Dr. Asher Blackwood**."),
    ("02_szornyek.png", "Bestiárium", "Farkasember, zombi, szellem, múmia, az alkimista és a teremtménye. Mindegyiket **másképp** kell megölni — ahogy a legendák tartják."),
    ("zold_filter_demo.png", "A zöldes filter", "Ugyanaz a jelenet három erősséggel. Árnyékemelés zöldbe + telítettség-csökkentés + vignetta. A tábortűznél visszaáll — ez adja a „hazaértem” érzést."),
    ("paletta.png", "Színpaletta", "A key artból kinyert színek és a „mit szabad mire használni” szabályok."),
]

QUESTS = [
    ("1", "Zombi — munkás-holt", "Verhollow bánya", "Cato Vint", "Lefejezés — a fej nélküli test tovább jár", "A TUTORIAL: mozgás, gladius, blokk, potion"),
    ("2", "Léleklámpás", "Sorrow's Reach", "Old Mam Rachel", "Eloltani — vízzel vagy sárral", "célzás, tárgyhasználat, lopakodás"),
    ("3", "Farkasember — Owen Barlow", "Blackbriar", "Wend Fisk", "Ezüst — golyó és penge; a tűz csak gyorsítja", "dodge-időzítés, felkészülés, holdfázis"),
    ("4", "Szellem — a megégetett nevek", "Üvöltő Kövek", "Father Bram", "Só, vas, és a neve kimondása", "nyomolvasás, döntés: elbocsátani vagy elpusztítani"),
    ("5", "Múmia — Kópharisz", "a sírhalom", "Kharis", "Az amulett eltávolítása", "körbejárás, gyenge pont, csapdák"),
    ("6", "Gólem — agyag-katona", "Verhollow kohó", "Isolde Karr", "A mágikus pecsét elpusztítása", "irányított célzás, mobilitás"),
    ("7", "FEJNÉLKÜLI LOVAS — Charon Walsh", "A HIDAK", "Father Bram", "Megállítani (harang, só), eloltani a lámpást, ezüst penge", "BOSS: fázisok, környezet-használat"),
    ("8", "Vámpír — lobogósok", "Sorrow's Reach", "Aggie Dow", "Karó a szívbe + ezüst + a küszöb", "napszak, szűk terek, fény-használat"),
    ("9", "Az alkimista", "Verhollow labor", "Adam Vale", "Villám és a szív — vagy a varratok elvágása", "beszélgetés, csapdák, erkölcsi döntés"),
    ("10", "A menyasszony — Ada", "Verhollow kripta", "Adam Vale", "Az ezüst-kötés elvágása", "párharc: védd meg, ne öld meg"),
    ("11", "Vérnász ★", "Needle Ridge", "Vén Medve Thorne", "A testébe varrt kő kivágása", "kombinált boss — minden gomb"),
    ("12", "Karmazsin asszony ★", "régi villa", "Iulia Severa", "Napfény, ezüst, a meghívás megtagadása", "napszak-tervezés, boss-fázisok"),
    ("★", "Valerius Menenius — a Vén Kígyó", "Caro Deorum", "—", "A saját kövei ellene fordítása", "végső boss, több befejezés"),
]
REGION_ROWS = """
      <tr><td>1</td><td><b>Hollowmier és külterülete</b></td><td>1–5</td><td>7 negyed · Kráter-domb · kikötő · tanyák</td><td>zombi · vámpír-szolga · kísértet · gólem</td><td>a Kráter-domb őre</td><td>22</td></tr>
      <tr><td>2</td><td><b>Blackbriar · Verhollow · Needle Ridge</b></td><td>5–10</td><td>szénégető erdő · bánya és kohó · sziklahegy-hát</td><td>farkasember · zombi · gólem · kísértet · alkat</td><td><b>VÉRNÁSZ ★</b></td><td>22</td></tr>
      <tr><td>3</td><td><b>Sorrow's Reach · A Hidak · Gallowmere</b></td><td>8–14</td><td>mocsaras folyófalu · híd és komp · kápolna és temető</td><td>vámpír · kísértet · szellem · léleklámpás</td><td><b>FEJNÉLKÜLI LOVAS ★</b></td><td>22</td></tr>
      <tr><td>4</td><td><b>Lapides Ululantes · Caro Deorum</b></td><td>12–18</td><td>a tiltás kőoszlopai · zarándok-tábor · a friss kráter</td><td>múmia · gólem · alkat · zombi · a Vén Kígyó</td><td><b>VALERIUS MENENIUS ★★</b></td><td>22</td></tr>
"""

quest_rows = "\n".join(
    f"<tr><td>{n}</td><td><b>{m}</b></td><td>{h}</td><td>{a}</td><td class='kill'>{k}</td><td>{t}</td></tr>"
    for n, m, h, a, k, t in QUESTS)

NAMES = [
    ("A játékos", [
        ("Vesper Crane — „Varjú”", "A JÁTÉKOS. Nyomkövetés, bestiárium, aether-detektor. Titka: hallja a szellemeket."),
        ("Felszerelés", "gladius és puska a hátán; 2 revolver és kés az övén; ezüst lövedékes töltényöv a mellkasán. A nyakában NINCS kő."),
    ]),
    ("A két vadásztárs (a tábortűznél)", [
        ("Aurel Mercer", "Fiatal mesterlövész, iker revolver. Titka: az apja mágus volt."),
        ("Gaius „Vén Medve” Thorne", "Öreg veterán, potion-öv, gőz-lábsín. Titka: ő ölte meg Aurel apját."),
    ]),
    ("A fő rejtély", [
        ("Elias Weir — „Eli”", "A fiú. Varázsereje van, kő nélkül — évszázadok óta az első. Nem született: megalkották."),
        ("Valerius Menenius — „a Vén Kígyó”", "A legnagyobb mágus; ő robbantotta ki a Nagy Mágusháborút, ő alkotja a szörnyeket. Négyszáz éve él. Polgári álcája: Dr. Asher Blackwood."),
        ("Iulia Severa ügynök", "A birodalmi kém, aki a megbízást adta. Utazó fényképésznek adja ki magát. Senki sem tudja, kinek dolgozik."),
        ("Maren", "Eli anyja — csak emlék és egy név. Az ő életébe került a fiú."),
    ]),
    ("Az NPC-k, akik küldetést adnak", [
        ("Cato Vint", "Hollowmier, hullaház — a halottak ismerője."),
        ("Father Bram", "Gallowmere kápolna — szellemek, harang, szertartások."),
        ("Old Mam Rachel", "Sorrow's Reach mocsár — potion-mester, léleklámpás."),
        ("Wend Fisk", "Blackbriar szénégető — farkasember-nyomok."),
        ("Tribune Livia Corvina", "A Vigiles tisztje — szerződések, a tiltás betartatása."),
        ("Isolde Karr", "Mechanica a Gőznegyedből — a steampunk felszerelés, a „legális erő” hangja."),
        ("Kharis", "A Vetchet népének utolsója — a sírok és a kő szertartása."),
        ("Aggie Dow", "Hollowmier kocsmárosa — pletykák, új szerződések."),
    ]),
    ("Szörny-szereplők, akiket nem kell megölni", [
        ("Adam Vale", "Az alkimista teremtménye. Beszél, emlékszik — segítséget kér."),
        ("Ada", "A menyasszony. Fél, és nem akar bántani senkit."),
        ("Owen Barlow", "A briari farkasember — nappal családapa."),
        ("Silas Gray", "Az a katona, aki lelőtte Charon Walsh-t. Az átok őt is üldözi."),
    ]),
    ("Hollowmier — a város", [
        ("Saloon-negyed", "sár, olajlámpás, zongora — Aggie kocsmája, szerződés-tábla"),
        ("A Fórum", "fehér márvány a sárban — bíróság, Vigiles-parancsnokság"),
        ("Gőznegyed (Vicus Vaporis)", "katránházak, gyárak, Blackwood Steamworks, pályaudvar"),
        ("Az Akasztófa-tér", "kivégzések, tiltott kő-kereskedők, a vadászok munkaterülete"),
        ("A Kikötő", "köd, hajókürt, csempészek"),
        ("A Kráter-domb", "a tiltott szentély, római zarándok-tábor"),
        ("A régi negyedek", "őslakos, afrikai és kínai közösségek"),
    ]),
    ("A falvak és a vadvidék", [
        ("BLACKBRIAR", "szénégető telep, korom — farkasember"),
        ("SORROW'S REACH", "félig víz alá került folyófalu — vámpír, léleklámpás"),
        ("GALLOWMERE", "folyami átkelő, kápolna — szellemek"),
        ("VERHOLLOW", "bánya- és kohóváros — zombik, gólem, az alkimista"),
        ("A HIDAK", "a Gray-híd és a komp — a fejnélküli lovas"),
        ("NEEDLE RIDGE", "Tűgerinc — a legendás Vérnász területe"),
        ("LAPIDES ULULANTES", "Üvöltő Kövek — a Vaskonzílium kőoszlopai"),
        ("CARO DEORUM", "Az Istenhús — a friss kráter, a végső helyszín"),
    ]),
]
name_blocks = "\n".join(
    f"""<div class="box"><h4>{t}</h4><ul>""" +
    "".join(f"<li><b>{n}</b> — {d}</li>" for n, d in items) + "</ul></div>"
    for t, items in NAMES)


def b64(path, maxw=1000, quality=76):
    im = Image.open(path).convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


cards = "\n".join(
    f"""
    <figure class="card">
      <img src="{b64(fn)}" alt="{title}" loading="lazy">
      <figcaption><h3>{title}</h3><p>{cap}</p></figcaption>
    </figure>""" for fn, title, cap in ITEMS)

HTML = f"""<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vérkő — koncepciós galéria</title>
<style>
  :root {{
    --ink:#eee2c8; --dim:#eee2c8a8; --bg:#0e0b11; --panel:#17131c;
    --red:#d65c3c; --amber:#e8a444; --green:#82dc8c; --brass:#c9a227;
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:
      radial-gradient(120% 60% at 50% -10%, #241d20 0%, transparent 60%),
      radial-gradient(80% 40% at 8% 100%, #14211b 0%, transparent 55%),
      var(--bg);
    color:var(--ink);
    font:16px/1.6 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
    padding:0 0 70px;
  }}
  header {{ max-width:1120px; margin:0 auto; padding:54px 24px 8px; }}
  .kicker {{ letter-spacing:.34em; text-transform:uppercase; font-size:11px;
    font-family:ui-sans-serif,system-ui,sans-serif; color:var(--brass); }}
  h1 {{ font-size:clamp(44px,9vw,96px); margin:.06em 0 .06em; letter-spacing:.02em; }}
  h1 span {{ color:var(--red); }}
  .logline {{ font-size:clamp(17px,2.1vw,21px); max-width:78ch; }}
  .logline b {{ color:var(--green); font-weight:600; }}
  .meta {{ display:flex; flex-wrap:wrap; gap:8px; margin:22px 0 0; padding:0; list-style:none;
    font-family:ui-sans-serif,system-ui,sans-serif; font-size:12.5px; }}
  .meta li {{ border:1px solid #ffffff2e; border-radius:999px; padding:5px 12px; color:var(--dim); }}
  main {{ max-width:1120px; margin:0 auto; padding:0 24px; }}
  .grid {{ display:grid; gap:22px; grid-template-columns:repeat(auto-fit,minmax(330px,1fr)); margin-top:34px; }}
  .card {{ margin:0; background:var(--panel); border:1px solid #ffffff1a; border-radius:14px;
    overflow:hidden; display:flex; flex-direction:column; }}
  .card img {{ width:100%; display:block; background:#000; }}
  .card figcaption {{ padding:14px 18px 18px; }}
  .card h3 {{ margin:0 0 6px; font-size:18.5px; }}
  .card p {{ margin:0; color:var(--dim); font-size:14.5px; }}
  .card p b {{ color:var(--ink); }}
  section {{ margin-top:50px; }}
  h2 {{ font-size:26px; margin:0 0 14px; border-bottom:1px solid #ffffff1f; padding-bottom:10px; }}
  .cols {{ display:grid; gap:18px; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); }}
  .box {{ background:var(--panel); border:1px solid #ffffff1a; border-radius:12px; padding:16px 18px; }}
  .box h4 {{ margin:0 0 10px; font-size:16px; color:var(--amber); }}
  .box p, .box ul {{ margin:0; color:var(--dim); font-size:14.5px; }}
  .box li {{ margin:7px 0; }}
  .box li b {{ color:var(--ink); font-weight:600; }}
  ul {{ padding-left:18px; }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; }}
  th,td {{ text-align:left; padding:9px 10px; border-bottom:1px solid #ffffff14; vertical-align:top; }}
  th {{ color:var(--amber); font-weight:600; font-size:12.5px; text-transform:uppercase; letter-spacing:.08em; }}
  td {{ color:var(--dim); }}
  td:first-child {{ color:#eee2c866; font-family:ui-monospace,monospace; }}
  td b {{ color:var(--ink); font-weight:600; }}
  td.kill {{ color:var(--green); }}
  .rule {{ border-left:3px solid var(--red); padding:6px 0 6px 14px; color:var(--ink); margin:18px 0; }}
  .tblwrap {{ overflow-x:auto; }}
  footer {{ max-width:1120px; margin:54px auto 0; padding:0 24px; color:#eee2c866; font-size:13px; }}
  code {{ font-family:ui-monospace,monospace; font-size:13px; color:var(--brass); }}
  .twist {{ background:linear-gradient(180deg,#1d1420,#17131c); border:1px solid #d65c3c55; }}
  .twist h4 {{ color:var(--red); }}
</style>
</head>
<body>
<header>
  <div class="kicker">Cowboy aranykor · Római birodalom · Steampunk · Izometrikus · Fekvő · Mobil</div>
  <h1>VÉR<span>KŐ</span></h1>
  <p class="logline">A Római Birodalom uralta alternatív vadnyugaton — ahol a mágiát évszázadokkal ezelőtt
  betiltották, és az emberiség a gőzbe kapaszkodik — <b>Vesper Crane</b> és három vadásztársa megbízást kap
  egy birodalmi kémtől: találják meg a fiút, <b>Elias Weirt</b>, és adják át a megbízónak.
  A fiú az utolsó élő mágus — kő nélkül. <b>Az apja pedig az, aki a Nagy Mágusháborút kirobbantotta,
  és aki négyszáz éve minden szörnyet megalkotott.</b></p>
  <ul class="meta">
    <li>Fekvő képernyő</li><li>2D izometrikus akció-RPG</li><li>Minden szörnyet másképp kell megölni</li>
    <li>Vándorló tábortűz</li><li>A kő tiltott — a játékos sem használhatja</li><li>Főhős: Vesper Crane</li>
  </ul>
</header>

<main>
  <div class="grid">{cards}
  </div>

  <section>
    <h2>A világ rendje — a tiltás</h2>
    <div class="rule">A <b>Nagy Mágusháború</b> (14–15. sz.) után az emberek győztek, és a <b>Vaskonzílium</b>
      betiltotta az égkövet: a birtoklása főbenjáró bűn. Azóta a Birodalom a <b>gőzben és a mértékben</b> hisz.
      Harc közben a tudomány nem segít — a szörnyeket ezüst, karó, só és vas öli meg.</div>
    <div class="cols">
      <div class="box"><h4>A Birodalom hazugsága</h4><p>Hivatalosan nincs mágia — a szörnyek „fertőzés”.
        A hatóság pontosan tudja, mi történik, de nem ismerheti el, mert akkor el kellene ismernie,
        hogy a tiltás nem működik.</p></div>
      <div class="box"><h4>A vadászok helye</h4><p>Illegális-közeli lények: nélkülük nem lehet élni, velük nem
        lehet együtt élni. Nincs polgárjoguk, nincs temetőjük.</p></div>
      <div class="box"><h4>A játékos eszközei</h4><p><b>Potion, fegyverek és tudás.</b> Nincs köve, nincs
        korrupció-mérő, nincs tiltott erő. A mágia a világban van: az ellenségekben és a rejtélyekben.</p></div>
      <div class="box"><h4>A kő ára</h4><p>Aki követ varrat a testébe, <b>több száz évig él — de nem lehet
        gyereke.</b> Ez a kulcs a fő rejtélyhez.</p></div>
    </div>
  </section>

  <section>
    <h2>A fő rejtély — amit a játék elején nem lehet tudni</h2>
    <div class="cols">
      <div class="box twist"><h4>Elias Weir — a fiú</h4><p>Varázsereje van, de <b>nincs benne kő</b> —
        évszázadok óta az első. Nem született: <b>megalkották</b>, és az ára az anyja élete volt.
        Belőle nem „csak” egy mágus lenne, hanem egy <b>mágikus vérvonal</b>.</p></div>
      <div class="box twist"><h4>Valerius Menenius — az apa</h4><p>A legnagyobb mágus, aki valaha élt.
        <b>Ő robbantotta ki a Nagy Mágusháborút</b>, és ő alkotja a szörnyeket mágiával és tudománnyal.
        Több kő van a testébe varrva: <b>négyszáz éve él</b>.</p></div>
      <div class="box twist"><h4>Dr. Asher Blackwood — az álca</h4><p>A <b>Blackwood Steamworks</b> úrnak
        látszik Hollowmier Gőznegyedében. <b>A vadászok pont tőle vásárolják a felszerelésüket</b> —
        az aether-detektort is. A mecénás, aki szörnyeket gyárt.</p></div>
      <div class="box twist"><h4>Iulia Severa — a kém</h4><p>Birodalmi ügynök, utazó fényképésznőnek adva ki
        magát. <b>Ő adta a megbízást.</b> A vadászok megbízható, senkivel sem kapcsolatban lévő civilek —
        pontosan ezért használja őket.</p></div>
    </div>
    <div class="rule">A csattanók sorrendje: elrabolt gyerek → a szörnyek egy műhelyből → Severa nem az,
      akinek látszik → <b>a gyerek apja él és Hollowmier legbefolyásosabb embere</b> → a végső kérdés nem az,
      hogy megölöd-e Meneniust, hanem hogy <b>mit kezdesz Elivel</b>.</div>
  </section>

  <section>
    <h2>A három vadász</h2>
    <div class="rule">A játékos: <b>Vesper Crane</b>. A tábortűznél <b>két férfi vadász</b> ül — hárman alkotják a csapatot.</div>
    <div class="cols">
      <div class="box"><h4>Vesper Crane — „Varjú” (JÁTÉKOS)</h4><ul>
        <li>nyomkövetés, bestiárium, aether-detektor</li>
        <li><b>gladius + puska a hátán; 2 revolver + kés az övén</b></li>
        <li>ezüst lövedékes töltényöv a mellkasán</li>
        <li>titka: <b>hallja a szellemeket</b> — és hazudik róla</li>
      </ul></div>
      <div class="box"><h4>Aurel Mercer</h4><p>Fiatal mesterlövész, iker revolver, pimasz. Titka:
        az apja mágus volt.</p></div>
      <div class="box"><h4>Gaius „Vén Medve” Thorne</h4><p>Öreg veterán, potion-öv, sárgaréz gőz-lábsín.
        <b>Titka: ő ölte meg Aurel apját</b> — és a tűznél ülnek egymás mellett.</p></div>
    </div>
  </section>

  <section>
    <h2>A tábortűz — a játék szíve</h2>
    <div class="rule">Nem bázis, nem építés: <b>egy tűz, körülötte a vadászok, és vándorol veled.</b></div>
    <div class="cols">
      <div class="box"><h4>Amire jó</h4><ul>
        <li>potion-főzés (gyógyító, erő, éjszakai látás)</li>
        <li>felkészülés a szerződéshez (ezüst, tűzolaj, só-vas, karó, víz)</li>
        <li>szerződés-választás, bestiárium, párbeszéd</li>
        <li>pihenés → <b>napszak vált</b>; mentés</li>
        <li>az NPC-k <b>kijönnek a tűzhöz</b> — nem kell a városba visszajárni</li>
      </ul></div>
      <div class="box"><h4>A tűz mint drámai eszköz</h4><ul>
        <li><b>I.:</b> erdőben, nyugodt, mindenki a helyén</li>
        <li><b>II.:</b> falu széle, bánya szája, mocsár — feszültebb párbeszédek</li>
        <li><b>III.:</b> hegyi hágó, vihar — már alig beszélnek egymással</li>
        <li><b>IV.:</b> a tűz körül megjelennek <b>Eli holmijai</b> — némán</li>
      </ul></div>
      <div class="box"><h4>Miért jó nekünk</h4><p>Nulla technológia: nincs építés, nincs NPC-napi rutin,
        nincs útvonal-tervezés. Mégis élő — a hub jön veled. Mobilon ez aranyat ér. És a tűz az
        <b>egyetlen hely, ahol a zöld filter visszaáll</b>: a meleg narancs adja a „hazaértem” érzést.</p></div>
    </div>
  </section>

  <section>
    <h2>Hat fegyver, egy sáv</h2>
    <div class="tblwrap"><table>
      <tr><th>#</th><th>Fegyver</th><th>Szerep</th></tr>
      <tr><td>1</td><td><b>Gladius</b> (ezüstözött, római penge)</td><td>fő közelharc, 3 ütemű kombó — a szörnyek többségét ez végzi ki</td></tr>
      <tr><td>2</td><td><b>Balta</b></td><td>lassabb, nagyobb sebzés, töri a csontot és a pajzsot</td></tr>
      <tr><td>3</td><td><b>Kés</b></td><td>gyors, hátulról dupla sebzés; kegyelmi/lefejező mozdulat</td></tr>
      <tr><td>4</td><td><b>Revolver</b> (ezüst lövedék)</td><td>távoli, célzásnál auto-lassítás („vadász-szem”), 6 lövés</td></tr>
      <tr><td>5</td><td><b>Sörétes</b></td><td>közeli robbanás, lökéshullám — tömeg ellen</td></tr>
      <tr><td>6</td><td><b>Puska</b></td><td>nagy hatótáv, pontos, lassú — elit és boss ellen</td></tr>
    </table></div>
    <p style="color:var(--dim);font-size:14.5px;margin-top:14px">Fekvőben a fegyverválasztó <b>vízszintes
      sáv</b> a képernyő alján (a középső köralak helyett): elfér, és a hüvelykujj egy húzással végigcsúsztathat rajta.
      Autók nincsenek — ló, szekér, gőzvasút és gőzhajó van.</p>
  </section>

  <section>
    <h2>Izometrikus + fekvő — négy döntés, amit korán hozz meg</h2>
    <div class="cols">
      <div class="box"><h4>1. Kamera</h4><p><b>Nem forgatható.</b> Fix 2:1 izometria, fekvő képernyő.
        Mobilon a forgatás drága és zavaró.</p></div>
      <div class="box"><h4>2. Fal-átlátszóság</h4><p><b>Kötelező.</b> A játékos előtti falak és tetők félig
        átlátszóvá válnak — enélkül a karakter eltűnik az épületek mögött.</p></div>
      <div class="box"><h4>3. Animáció</h4><p>8 irányos frame-by-frame izometriában <b>öngyilkosság</b>.
        Cutout/csontváz (Spine vagy Godot <code>Skeleton2D</code>), vagy 4 irány + tükrözés.</p></div>
      <div class="box"><h4>4. Talp-pozíció</h4><p><code>TileMapLayer</code> → <code>tile_shape = Isometric</code>,
        <code>y_sort_enabled</code>, és a karakter <b>talpa a gyémánt közepére</b> essen. Ezt az első napon
        állítsd be, mielőtt bármit rajzolnál.</p></div>
    </div>
  </section>

  <section>
    <h2>A világ szerkezete — 4 régió, 88 küldetés</h2>
    <div class="rule">A régiók között <b>csak a Legio Rail gőzvonatával</b> lehet közlekedni: jegy kell hozzá,
      és a járatok <b>nappal indulnak</b> — éjszaka a szerelvény nem hagyja el az állomást. A teljes
      küldetés-adatbázis (88 sor, ölésmóddal, felkészüléssel, jutalommal) a <code>quests.csv</code> fájlban van.</div>
    <div class="tblwrap"><table>
      <tr><th>#</th><th>Régió</th><th>Szint</th><th>Helyszínek</th><th>Szörnycsaládok</th><th>Csúcspont</th><th>Küldetés</th></tr>
      {REGION_ROWS}
    </table></div>
    <div class="cols" style="margin-top:18px">
      <div class="box"><h4>22 küldetés régiónként — a recept</h4><ul>
        <li><b>5 történet</b> — a főszál, soha nem ismételhető</li>
        <li><b>8 tábla</b> — ismételhető, a grind alapja</li>
        <li><b>4 vizsgálat / mentés</b> — harc nélkül vagy kevés harcsal</li>
        <li><b>3 elit / legendás</b> — crafting-anyag jutalommal</li>
        <li><b>2 karakter</b> — tábortűz-párbeszéd, Vesper naplója</li>
      </ul></div>
      <div class="box"><h4>Miért ismétlődnek a szörnyek — és mitől nem unalmas</h4>
        <p>A szörnycsalád <b>régióhoz kötött, mint az élővilág</b>: mocsárban vámpír és kísértet, bányában
        zombi és gólem. Az ismétlést három dolog menti meg: <b>1.</b> az első találkozásnál a bestiárium
        bejegyzést kap — a másodiknál már tudod a gyenge pontot, ezért gyorsabb és taktikusabb a harc;
        <b>2.</b> az elit variáns új képességet kap; <b>3.</b> a jutalom ritka crafting-anyag a bossokhoz.</p></div>
      <div class="box"><h4>A vonal rejtélye</h4><p>A Legio Rail utolsó szakaszát — a zarándokvonalat a kráterig —
        <b>Blackwood építette</b>. A gőzvasút nem a polgárok kényelmét szolgálja: <b>a köveket szállítja</b>.
        Ez a IV. felvonás egyik csattanója.</p></div>
    </div>
  </section>

  <section>
    <h2>Minden szörnyet máshogy kell megölni</h2>
    <div class="rule">Ez ingyen adja a tartalmat: nem kell új csapás-animáció, csak új <em>szabály</em>.
      Válogatás a 88 küldetésből:</div>
    <div class="tblwrap"><table>
      <tr><th>#</th><th>Szörny</th><th>Hol</th><th>Ki adja</th><th>Az ölés módja</th><th>Mit tanít meg</th></tr>
      {quest_rows}
    </table></div>
    <div class="cols" style="margin-top:18px">
      <div class="box"><h4>A fejnélküli lovas — miért jó boss?</h4><ol>
        <li><b>A hajsza:</b> végigvágtat a hídon, a játékos csak kitérni tud, amíg keresi a harangkötelet</li>
        <li><b>A megállítás:</b> meghúzza a gallowmere-i kápolna harangját — a ló megbokrosodik, a lámpás leesik</li>
        <li><b>A vég:</b> amíg a lámpás ég, sérthetetlen; el kell oltani, és ezüst pengével végezni vele</li>
      </ol></div>
      <div class="box"><h4>A variánsok (ingyen tartalom)</h4><p>Szörnycsaládonként alap / elit / legendás szint:
        méret, szín és egy plusz képesség. Mobilon ez az egyetlen reális út, hogy egy szörnycsaládból
        három élmény legyen.</p></div>
    </div>
  </section>

  <section>
    <h2>Névjegyzék</h2>
    <div class="cols">{name_blocks}</div>
  </section>

  <section>
    <h2>Scope — a reális út</h2>
    <div class="cols">
      <div class="box"><h4>1. Vertical slice · 2–4 hónap</h4><p>Hollowmier egy utcája + a verhollowi bánya,
        a zombi-szerződés (egyben a tutorial), a harc, a HUD és a tábortűz — Androidon, fekvő módban.</p></div>
      <div class="box"><h4>2. Egy régió · 6–10 hónap</h4><p>Hollowmier + 4 falu + 3 vadvidék, 6–8 szerződés,
        3 boss (köztük a fejnélküli lovas), napszak, gőzvasút.</p></div>
      <div class="box"><h4>3. Nagy játék</h4><p>További régiók, a Menenius-szál teljes kibontása, több befejezés.</p></div>
      <div class="box"><h4>Ne, elsőre</h4><ul><li>lovaglás, úszás, teljes időjárás</li>
        <li>NPC-napi rutin, forgatható kamera</li><li>szinkronhang, autók</li></ul></div>
    </div>
  </section>
</main>

<footer>
  Vérkő — koncepciós jegyzet. A képek hangulati referencia-koncepciók (AI-generált vázlatok), nem végleges
  játék-assetek. Részletes jegyzet: <code>KONCEPCIO.md</code> · <code>NEVEK_ES_SZORNYEK.md</code> ·
  <code>godot/green_filter.gdshader</code> · HUD: <code>kontroll_es_hud_fekvo.png</code>
</footer>
</body>
</html>"""

with open("koncepcio_galeria.html", "w", encoding="utf-8") as f:
    f.write(HTML)
print("koncepcio_galeria.html", round(len(HTML) / 1024 / 1024, 2), "MB")
