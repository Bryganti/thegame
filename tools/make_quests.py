#!/usr/bin/env python3
"""CARO DEORUM — küldetés-adatbázis (4 régió, 20+ küldetés/régió) -> quests.csv
A CSV közvetlenül betölthető Godotba (FileAccess.get_csv_line vagy Resource-táblába)."""

# --- szörny-profilok: ölésmód, felkészülés, tipikus jutalom -------------------
MON = {
    "zombi":        ("Lefejezés — a fej nélküli test tovább jár", "ezüst penge, tűz, fejvadász-csapda", "rothadt égkő-töredék, csontpor"),
    "zombi_elit":   ("Lefejezés — a fej nélküli test tovább jár", "ezüst penge, tűzolaj, lánc-csapda", "bányász-pecsét, ólomtömb"),
    "farkasember":  ("Ezüst — golyó és penge; a tűz csak gyorsítja", "ezüst lövedék, ezüst penge, holdfázis-ismeret", "ezüst-érctörmelék, sörte"),
    "szellem":      ("Só, vas, és a neve kimondása — elbocsátani", "só és vas, gyász-szalag, a név ismerete", "lélekszilánk, dermedt lepel"),
    "kísértet":     ("Só, vas; a tárgyát kell eltemetni", "só és vas, szentelt víz, a tárgy", "hamu, régi fénykép"),
    "vámpír":       ("Karó a szívbe + ezüst + a küszöb tisztelete", "karó, ezüst, szentelt víz, fény", "vámpír-agyar, karmazsin selyem"),
    "vámpír_elit":  ("Karó a szívbe + ezüst + a küszöb tisztelete", "karó, ezüst, tükör, fény", "udvartartás-jelvény, arany bilincs"),
    "múmia":        ("Az amulett eltávolítása — a test megáll", "tűz, véső, csapda a körungozáshoz", "ókori amulett, vászontekercs"),
    "gólem":        ("A mágikus pecsét elpusztítása", "gőzkalapács, sav, irányított célzás", "pecsét-töredék, agyagmag"),
    "alkat":        ("A varratok elvágása / villám — őket lehet nem megölni", "kés, villám-vezető, beszélgetés", "kapocs-ötvözet, lombik"),
    "múmia_boss":   ("Az amulett eltávolítása — a test megáll", "tűz, véső, csapdák", "királyi amulett, égkő-töredék"),
    "lovas":        ("Megállítani (harang, só-vonal), eloltani a lámpást, ezüst penge", "harangkövél, só és vas, ezüst penge, sár", "Walsh lámpása, patkó"),
    "vernasz":      ("A testébe varrt kő kivágása — ezüst nem hat rá", "minden: ezüst, tűz, csapdák, gőz", "vérnász-sörte, óriás kőtöredék"),
    "karmazsin":    ("Napfény, ezüst, a meghívás megtagadása", "tükör, ezüst, nappali roham", "karmazsin pecsétgyűrű, udvari napló"),
    "menenius":     ("A saját kövei ellene fordítása", "négy évszázad összes vadász-tudása", "a Vén Kígyó kövei"),
    "—":            ("Nincs harc — nyomolvasás, párbeszéd, döntés", "—", "információ, térkép, bizalom"),
}

# --- küldetések: (név, típus, ki adja, szörny, ismételhető, szint, megjegyzés) --
R = {}

R[1] = ("HOLLOWMIER ÉS KÜLTERÜLETE", 1, 5, "Hollowmier, Kráter-domb, kikötő, külterületi tanyák", [
    ("A tetem a hullaházban", "Történet", "Cato Vint", "zombi", "nem", "1", "TUTORIAL: mozgás, gladius, blokk, potion"),
    ("A Weir-ház", "Történet", "Iulia Severa", "—", "nem", "1", "A fiú háza feldúlva — az első nyomok, harc nélkül"),
    ("A Vigiles pecsétje", "Történet", "Tribune Livia Corvina", "zombi", "nem", "2", "A fejpénz-rendszer bevezetése; csorda a kikötőben"),
    ("A fényképésznő asszony", "Történet", "Iulia Severa", "vámpír", "nem", "3", "Severa kísérete a Kráter-dombig — a kém bemutatása"),
    ("A fekete füst", "Történet", "Isolde Karr", "gólem", "nem", "4", "Szivárgás a Blackwood Steamworksnél — gólem-prototípus"),
    ("Patkányok a katakombában", "Tábla", "Aggie Dow", "zombi", "igen", "1", "Első ismételhető szerződés"),
    ("Az akasztófa-tér lakói", "Tábla", "Aggie Dow", "szellem", "igen", "2", "Éjszakai szerződés — a tér bitófái alatt"),
    ("Az eltűnt bányászok", "Tábla", "Cato Vint", "zombi_elit", "igen", "3", ""),
    ("Kikötői ládák", "Tábla", "Tribune Livia Corvina", "kísértet", "igen", "3", "Csempészett lámpások a raktárban"),
    ("Vérfoltok a Fórumnál", "Tábla", "Isolde Karr", "vámpír", "igen", "4", "Vámpír-szolga a márvány között"),
    ("Orvvadász a külterületen", "Tábla", "Wend Fisk", "farkasember", "igen", "4", ""),
    ("A sírásó éjszakái", "Tábla", "Father Bram", "kísértet", "igen", "3", ""),
    ("Ezüsthiány", "Gyűjtés", "Old Mam Rachel", "—", "igen", "2", "Ezüst-érc és ólom begyűjtése a külterületről"),
    ("A potion-recept", "Gyűjtés", "Gaius „Vén Medve” Thorne", "—", "nem", "2", "Gyógynövény + égkő nélküli főzés első receptje"),
    ("A harmadik vadász", "Karakter", "Aurel Mercer", "—", "nem", "2", "A tábor feszültsége: Aurel és Thorne múltja"),
    ("Aggie pletykái", "Vizsgálat", "Aggie Dow", "—", "nem", "2", "Három helyszín, három vallomás"),
    ("Az orvvadász-csapda", "Vizsgálat", "Wend Fisk", "—", "nem", "3", "Csapdák felállítása — a vadászat előkészítése"),
    ("A bányász-őr", "Elit", "Cato Vint", "zombi_elit", "igen", "4", ""),
    ("Karmazsin szolga a villában", "Elit", "Iulia Severa", "vámpír_elit", "igen", "5", ""),
    ("A Kráter-domb őre", "Mini-boss", "Tribune Livia Corvina", "gólem", "nem", "5", "A tiltott szentély kapujában"),
    ("Vesper naplója", "Karakter", "— (Vesper)", "—", "nem", "1", "A bestiárium első kötete — a játékos hangja"),
    ("A Vén Medve figyelmeztetése", "Karakter", "Gaius „Vén Medve” Thorne", "—", "nem", "3", "Thorne elmondja, mit tett a Tisztogatáson — félig"),
])

R[2] = ("BLACKBRIAR · VERHOLLOW · NEEDLE RIDGE", 5, 9, "szénégető erdő, bánya- és kohóváros, sziklahegy-hát", [
    ("A briari farkas", "Történet", "Wend Fisk", "farkasember", "nem", "5", "Owen Barlow: megölöd vagy leleplezed?"),
    ("A bányamélység", "Történet", "Cato Vint", "zombi_elit", "nem", "6", "Lefelé a víz alatti szintekbe"),
    ("A kohó pecsétje", "Történet", "Isolde Karr", "gólem", "nem", "6", "Agyag-katonák a kohóban"),
    ("Az alkimista naplója", "Történet", "Adam Vale", "alkat", "nem", "8", "A teremtmény kér segítséget a teremtője ellen"),
    ("Vérnász fiai", "Történet", "Gaius „Vén Medve” Thorne", "farkasember", "nem", "9", "Az első út a hágóra"),
    ("Szénégető-korcsvadászat", "Tábla", "Wend Fisk", "farkasember", "igen", "5", ""),
    ("A kohó kísértete", "Tábla", "Father Bram", "kísértet", "igen", "6", "Gép-áldozatok a füstben"),
    ("Agyag-katonák", "Tábla", "Isolde Karr", "gólem", "igen", "7", ""),
    ("A bánya omlása", "Mentés", "Cato Vint", "zombi", "nem", "6", "Három bányász kimentése"),
    ("Ezüst a vénhez", "Gyűjtés", "Gaius „Vén Medve” Thorne", "—", "igen", "6", "Ezüst-bevonat receptjének anyagai"),
    ("Vérnyomok a hágón", "Vizsgálat", "Aurel Mercer", "farkasember", "igen", "7", "Nyomolvasás + les a hágón"),
    ("A gőzkazán szelleme", "Tábla", "Isolde Karr", "kísértet", "igen", "7", ""),
    ("A mélység láncai", "Gyűjtés", "Cato Vint", "—", "igen", "8", "Óriás csont és kapocs-ötvözet"),
    ("Owen Barlow háza", "Vizsgálat", "Wend Fisk", "—", "nem", "5", "Bizonyíték — a döntés előkészítése"),
    ("A menyasszony hírei", "Vizsgálat", "Adam Vale", "—", "nem", "8", "Rejtett nyom a labor felé"),
    ("Isolde Karr műhelye", "Vizsgálat", "Isolde Karr", "—", "nem", "7", "Gőz-gauntlet és aether-detektor fejlesztése"),
    ("A hágó térképe", "Felfedezés", "Aurel Mercer", "—", "nem", "9", "Needle Ridge feltárása"),
    ("Vérnász fiai — elit horda", "Elit", "Gaius „Vén Medve” Thorne", "farkasember", "igen", "9", ""),
    ("A kohó-őr", "Elit", "Isolde Karr", "gólem", "igen", "9", ""),
    ("A mélység (legendás)", "Legendás", "Cato Vint", "zombi_elit", "nem", "10", "Sok száz holt egyszerre"),
    ("VÉRNÁSZ ★", "Legendás boss", "Gaius „Vén Medve” Thorne", "vernasz", "nem", "12", "BOSS: a testébe varrt kő kivágása"),
    ("Aurel és Thorne", "Karakter", "Aurel Mercer", "—", "nem", "8", "A feszültség kiéleződik a tűznél"),
])

R[3] = ("SORROW'S REACH · A HIDAK · GALLOWMERE", 8, 13, "mocsaras folyófalu, a Gray-híd és a komp, kápolna és temető", [
    ("A víz alatti házak", "Történet", "Old Mam Rachel", "vámpír", "nem", "8", "A vámpírok és a mocsár"),
    ("A lámpás, ami nem alszik el", "Történet", "Old Mam Rachel", "kísértet", "nem", "8", "A léleklámpás eredete"),
    ("A HIDAK", "Történet", "Father Bram", "lovas", "nem", "10", "Az első találkozás: csak a hajsza-fázis"),
    ("A harang szava", "Történet", "Father Bram", "—", "nem", "10", "A gallowmere-i harang és a szentelt föld"),
    ("A fiú nyoma a mocsárban", "Történet", "— (Vesper)", "—", "nem", "11", "FŐSZÁL: Eli járt itt"),
    ("Lobogósok a csónakházban", "Tábla", "Aggie Dow", "vámpír", "igen", "8", ""),
    ("A mocsár fényei", "Tábla", "Old Mam Rachel", "kísértet", "igen", "9", ""),
    ("A komp-átkelő", "Védelem", "Father Bram", "szellem", "igen", "9", "Utasok átkeltetése éjszaka"),
    ("Az eltemetetlen nevek", "Tábla", "Father Bram", "szellem", "igen", "9", ""),
    ("A híd alatt", "Tábla", "Aurel Mercer", "kísértet", "igen", "10", ""),
    ("Eltűnt halászok", "Tábla", "Aggie Dow", "vámpír_elit", "igen", "11", ""),
    ("Só és vas", "Gyűjtés", "Gaius „Vén Medve” Thorne", "—", "igen", "8", "Só, réz, ezüst — a régi tudás alapanyagai"),
    ("Az éjszakai révész", "Vizsgálat", "Father Bram", "—", "nem", "10", "Charon Walsh nyoma"),
    ("Father Bram iratai", "Vizsgálat", "Father Bram", "—", "nem", "9", "A gallowmere-i kripta"),
    ("Silas Gray háza", "Vizsgálat", "Aurel Mercer", "—", "nem", "10", "A gyilkosság bizonyítéka"),
    ("A kripta térképe", "Vizsgálat", "Old Mam Rachel", "—", "nem", "10", "Meg kell találni a koponyát"),
    ("Mam Rachel átkai", "Gyűjtés", "Old Mam Rachel", "—", "nem", "9", "Szentelt víz és védőfőzet"),
    ("Karmazsin asszony udvartartása", "Elit", "Iulia Severa", "vámpír_elit", "igen", "12", ""),
    ("A mélyvíz asszonyai", "Elit", "Old Mam Rachel", "kísértet", "igen", "12", ""),
    ("FEJNÉLKÜLI LOVAS ★", "Legendás boss", "Father Bram", "lovas", "nem", "14", "BOSS: hajsza → harang → oltás → ezüst penge"),
    ("Vesper és a szellemek", "Karakter", "— (Vesper)", "—", "nem", "12", "Vesper titka közel kerül a felszínhez"),
    ("Gray megmentése", "Karakter", "Father Bram", "—", "nem", "13", "Döntés: az átok másik áldozata"),
])

R[4] = ("LAPIDES ULULANTES · CARO DEORUM", 12, 18, "a tiltás kőoszlopai, zarándok-tábor, a legfrissebb kráter", [
    ("A kőoszlopok", "Történet", "Gaius „Vén Medve” Thorne", "szellem", "nem", "12", "A Vaskonzílium színhelye — Thorne ott volt"),
    ("A zarándokok", "Történet", "Tribune Livia Corvina", "—", "nem", "12", "Római zarándok-tábor a kráternél — a tiltás képmutatása"),
    ("A mélyből jövő", "Történet", "Isolde Karr", "alkat", "nem", "13", "Kísérleti alanyok szöktek meg a szentély alatti laborból"),
    ("Aki építette a vonalat", "Történet", "— (Vesper)", "—", "nem", "14", "FŐSZÁL: a Legio Rail Blackwood műve"),
    ("Az apa", "Történet", "Iulia Severa", "menenius", "nem", "16", "Menenius leleplezése"),
    ("A pec séstes óriás", "Tábla", "Isolde Karr", "gólem", "igen", "13", ""),
    ("A megégetett nevek kórusa", "Tábla", "Father Bram", "szellem", "igen", "13", ""),
    ("A Vetchet király sírja", "Tábla", "Kharis", "múmia_boss", "nem", "14", ""),
    ("A mélység csordája", "Tábla", "Cato Vint", "zombi_elit", "igen", "13", ""),
    ("Az élő alkat", "Tábla", "Adam Vale", "alkat", "igen", "14", ""),
    ("A menyasszony", "Mentés", "Adam Vale", "alkat", "nem", "14", "Ada: védd meg, ne öld meg"),
    ("Az alkimista", "Tábla", "Adam Vale", "alkat", "nem", "15", "Villám és a szív — vagy a varratok"),
    ("Ezüst-vér", "Gyűjtés", "Gaius „Vén Medve” Thorne", "—", "igen", "15", "A végső felkészülés alapanyagai"),
    ("Menenius naplói", "Vizsgálat", "— (Vesper)", "—", "nem", "15", "Négy évszázad feljegyzései"),
    ("Maren sírja", "Vizsgálat", "Gaius „Vén Medve” Thorne", "—", "nem", "15", "Eli anyja — az ár, amit fizettek"),
    ("Severa igazi arca", "Vizsgálat", "Tribune Livia Corvina", "—", "nem", "16", "A kém leleplezése"),
    ("A vonal vége", "Vizsgálat", "Isolde Karr", "—", "nem", "16", "Miért épült a vasút a kráterig"),
    ("A kráter őrei", "Elit", "Kharis", "gólem", "igen", "17", "Vegyes elit horda"),
    ("Karmazsin asszony ★", "Legendás boss", "Iulia Severa", "karmazsin", "nem", "17", "Ha a III. régióban nem esett el"),
    ("VALERIUS MENENIUS ★★", "Végső boss", "—", "menenius", "nem", "18", "A saját kövei ellene fordítása"),
    ("A négy vadász", "Karakter", "— (Vesper)", "—", "nem", "16", "A tábortűz utolsó éjszakája"),
    ("Eli döntése", "Karakter", "—", "—", "nem", "18", "Három befejezés előkészítése"),
])

# ---------------------------------------------------------------- CSV -------
import csv

rows = []
qid = 0
for rnum in (1, 2, 3, 4):
    rname, lvl_from, lvl_to, places, quests = R[rnum]
    for (name, qtype, giver, mon, rep, lvl, note) in quests:
        qid += 1
        kill, prep, reward = MON[mon]
        rows.append({
            "id": f"Q{qid:03d}",
            "regio": rname,
            "regio_szint": f"{lvl_from}-{lvl_to}",
            "helyszin": places.split(",")[0].strip() if qtype in ("Történet",) else "",
            "küldetés": name,
            "típus": qtype,
            "ki_adja": giver,
            "szörny": mon.replace("_", " ") if mon != "—" else "—",
            "ölésmód": kill,
            "felkészülés": prep,
            "jutalom": reward,
            "ismételhető": rep,
            "ajánlott_szint": lvl,
            "megjegyzés": note,
        })

with open("quests.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

total = len(rows)
story = sum(1 for r in rows if r["típus"] == "Történet")
reps = sum(1 for r in rows if r["ismételhető"] == "igen")
print(f"quests.csv: {total} küldetés  (történet: {story}, ismételhető: {reps})")
for rnum in (1, 2, 3, 4):
    n = sum(1 for r in rows if r["regio"] == R[rnum][0])
    print(f"  R{rnum}: {n} küldetés — {R[rnum][0]}")
