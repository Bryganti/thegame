# VÉRKŐ — teljes koncepció egy fájlban

> Ez a fájl a repó dokumentumainak összefűzött változata, hogy egyetlen csatolmányként is átadható legyen.


<!-- ============ README.md ============ -->

# VÉRKŐ

> 2D izometrikus, fekvő képernyős akció-RPG mobilra (Godot 4.7).
> Monster hunter × Hades-látvány × cowboy aranykor × római birodalom × steampunk horror.

**Egy mondatban:** A Római Birodalom uralta alternatív vadnyugaton — ahol a mágiát évszázadokkal
ezelőtt betiltották, és az emberiség a gőzbe kapcsolódik — három számkivetett szörnyvadász megbízást
kap egy birodalmi kémtől: találják meg az Elias Weir nevű kisfiút, és adják át a megbízónak.
A fiúnak kő nélkül van varázsereje — évszázadok óta az első —, **az apja pedig a végső ellenség**.

---

## Mi van ebben a repóban?

| Mappa | Tartalom |
|---|---|
| `docs/` | **KONCEPCIO.md** — világ, harci rendszer, HUD, scope · **NEVEK_ES_SZORNYEK.md** — nevek, helyszínek, bestiárium, tutorial |
| `data/` | **quests.csv** — a 88 küldetés (régió, küldetésadó, szörny, ölésmód, felkészülés, jutalom, szint) |
| `art/` | 27 koncepciós kép: vadászok, szörnyek, városok, izometrikus játéknézet, bossok |
| `hud/` | Fekvő HUD-terv, zöld filter demó, színpaletta, régió-térkép |
| `godot/` | **green_filter.gdshader** — a zöldes „halloweeni" színfilter |
| `galeria/` | **koncepcio_galeria.html** — egy lapos, önmagába zárt galéria (duplán kattintva megnyílik) |
| `tools/` | Python szkriptek, amik a képeket/dokumentumokat generálták (újrafuttathatók) |

**Új chatben folytatod?** Olvasd el a **[`CONTINUE_HERE.md`](CONTINUE_HERE.md)** fájlt — benne van a
teljes kánon, az összes meghozott döntés, a nyitott kérdések, és egy **bemásolható üzenet** is.

---

## A világ röviden

- **Korszak:** cowboy aranykor (1800-as évek vége) — **nem** napóleoni kor. Autók nincsenek: ló, szekér, gőzvasút.
- **Róma uralja Amerikát**, de a katonák és a civilek **cowboy ruhát** hordanak, benne **felvarrt,
  hímzett** római jelvényekkel (sas + SPQR). Ókori páncél nincs.
- **Steampunk:** gőz-akvadukt, **Legio Rail** gőzvasút, sárgaréz aether-detektor, Mechanicus kaszt.
- **Az égkő tiltott.** Aki a testébe varratta, több száz évig él — de nem lehet gyereke. Ez a fő rejtély kulcsa.
- **A játékos nem használ követ** és nincs korrupció-rendszer: csak potion, fegyverek és tudás.

## A három vadász

| Ki | Szerep |
|---|---|
| **Vesper Crane** („Varjú") | **A játékos.** Nő, nyomkövetés, bestiárium, aether-detektor. Gladius + puska a hátán, 2 revolver + kés az övén, ezüst lövedékes töltényöv. **A nyakában nincs kő.** |
| **Aurel Mercer** | Fiatal mesterlövész, iker revolver. Titka: az apja mágus volt. |
| **Gaius „Vén Medve" Thorne** | Öreg veterán, potion-öv, gőz-lábsín. Titka: ő ölte meg Aurel apját. |

## A 4 régió és a 88 küldetés

| # | Régió | Szint | Csúcspont | Küldetés |
|---|---|---|---|---|
| 1 | Hollowmier és külterülete | 1–5 | a Kráter-domb őre | 22 |
| 2 | Blackbriar · Verhollow · Needle Ridge | 5–10 | **VÉRNÁSZ ★** | 22 |
| 3 | Sorrow's Reach · A Hidak · Gallowmere | 8–14 | **FEJNÉLKÜLI LOVAS ★** | 22 |
| 4 | Lapides Ululantes · Caro Deorum | 12–18 | **VALERIUS MENENIUS ★★** | 22 |

A régiók között **csak a Legio Rail gőzvonatával** lehet közlekedni (jegy kell; nappal indulnak).

## Alapelvek

1. **Minden szörnyet máshogy kell megölni** — ahogy a legendák tartják (ezüst, karó, só, név, amulett, harang).
2. **A tábortűz vándorol veled** — nem bázis, hanem hub és drámai eszköz.
3. **Izometrikus, fix kamera, fekvő képernyő.**
4. **A tudás a jutalom** — az ismétlődő szörnyeknél is a játékos fejlődik, nem csak a számok.

---

*A képek AI-generált hangulati referencia-koncepciók, nem végleges játék-assetek.*


<!-- ============ CONTINUE_HERE.md ============ -->

# FOLYTATÁS — Vérkő projekt (handoff)

> **Ezt a fájlt használd, ha új chat ablakban folytatod.** A fájl alján van egy
> **bemásolható üzenet** — azt illeszd be az új chatbe, és azonnal felveszi a fonalat.

Utolsó frissítés: 2026-09-24

---

## Mi ez a projekt?

**Vérkő** — 2D **izometrikus**, **fekvő képernyős** akció-RPG **mobilra**, Godot 4.7-ben.
Műfaj: monster hunter (Witcher-stílusú szerződések) × Hades-látvány × vadnyugat × római birodalom × steampunk horror.

**Egy mondatban:** A Római Birodalom uralta alternatív vadnyugaton — ahol a mágiát évszázadokkal
ezelőtt betiltották, és az emberiség a gőzbe kapcsolódik — három számkivetett szörnyvadász megbízást
kap egy birodalmi kémtől: találják meg **Elias Weir** nevű kisfiút, és adják át a megbízónak.
A fiúnak kő nélkül van varázsereje (évszázadok óta az első), **az apja pedig a végső ellenség**.

---

## A KÁNON — ezek a döntések VÉGLEGESEK (ne írd felül őket)

### Korszak és technológia
- **Cowboy aranykor** (1800-as évek vége), **NEM** napóleoni kor. Western ruha: duster, karimás
  cowboy-kalap, töltényöv, sarkantyú. **Autók nincsenek** — ló, szekér, gőzvasút, gőzhajó.
- A **Római Birodalom** uralja Amerikát. A katonák/közemberek **cowboy ruhát** hordanak, benne
  **felvarrt, hímzett** római jelvényekkel (sas + SPQR) — **NINCS ókori páncél**. Ókori páncél csak
  a császári testőrök diszruhája lehet.
- **Steampunk** (a tudomány mint birodalmi vallás): gőz-akvadukt, **Legio Rail** gőzvasút,
  sárgaréz aether-detektor, gőz-gauntlet, Mechanicus kaszt.

### A tiltás (a világ alapszabálya)
- Ókor: meteorzápor → **égkő** a földön. Nyakláncon (lassú, biztonságos) vagy **bőr alá varrva**
  (erős, de elmebajhoz vezet).
- Aki követ varrat a testébe: **több száz évig él, de nem lehet gyereke** ← ez a fő rejtély kulcsa.
- **Nagy Mágusháború** (14–15. sz.): mágusok vs. emberek, az emberek nyertek → a **Vaskonzílium**
  (*Edictum Lapidis*) **betiltotta az égkövet**. Birtoklás = főbenjáró bűn.
- Azóta a Birodalom a **gőzben/tudományban** hisz; a szörnyeket hivatalosan „fertőzésnek" nevezi.
- **A játékos SOHA nem használ követ, és nincs korrupció-rendszer.** Amije van: **potion, fegyverek,
  tudás** (bestiárium + felkészülés).

### A négy vadász (HÁRMAN vannak)
| Ki | Szerep |
|---|---|
| **Vesper Crane** („Varjú") | **A JÁTÉKOS.** Nő, orvos lánya, kitagadta a családja. Nyomkövetés, bestiárium, aether-detektor. Titka: **hallja a szellemeket**. |
| **Aurel Mercer** | Férfi, fiatal mesterlövész, iker revolver, pimasz. Titka: az apja mágus volt. |
| **Gaius „Vén Medve" Thorne** | Férfi, idős, nehéz testű, potion-öv, gőz-lábsín. Titka: **ő ölte meg Aurel apját 30 éve** — és együtt ülnek a tűznél. |

### Vesper felszerelése (kötelező elemek)
- **Gladius** (ezüstözött, római penge) és **puska** a hátán
- **2 revolver** és **kés** az övén
- **Mellkason átfutó töltényöv ezüst lövedékekkel**
- Sárgaréz **aether-detektor**
- **A nyakában NINCS kő**

### Fegyverek (6, egy sávon)
gladius · balta · kés · revolver (ezüst) · sörétes · puska

### Nézet és képernyő
- **Izometrikus (2:1), fix — nem forgatható kamera**
- **Fekvő (landscape) képernyő**, 19.5:9
- Fal-átlátszóság kötelező; a karakter **talpa a gyémánt közepén** (ezt az első napon beállítani!)

### A tábortűz (a játék szíve)
- **Nem bázis, nem építés:** egy tűz, körülötte a vadászok, és **vándorol veled** a történettel.
- Funkciók: potion-főzés, felkészülés (ezüst/tűzolaj/só-vas/karó/víz), szerződés-választás,
  bestiárium, pihenés (napszak-váltás), mentés. Az NPC-k **kijönnek a tűzhöz**.
- A tűz az **egyetlen hely, ahol a zöld filter visszaáll** — a meleg narancs adja a „hazaértem" érzést.

### A szörnyek
- **Minden szörnyet máshogy kell megölni, ahogy a legendák tartják:** zombi = lefejezés, farkasember =
  ezüst, szellem = só/vás/név kimondása, múmia = amulett, vámpír = karó a szívbe, **fejnélküli lovas =
  harang + a lámpás eloltása + ezüst penge** (amíg lovon ül és a lámpás ég: sérthetetlen).
- **A fejnélküli lovas legyőzhető szörny** (3 fázisú boss).

### Zöldes filter (halloweeni hangulat)
- Shader: `godot/green_filter.gdshader` — árnyékemelés zöldbe + telítettség-csökkentés + vignetta.
- Erősség: nappal 0.15 · este 0.40 · erdő/temető 0.55 · mocsár/kráter 0.75 · boss 0.60 + pulzálás.
- **Ne szűrje** a HUD-ot és a portrékat; a sebzés maradjon piros/sárga; legyen színvak-opció.

---

## A 4 RÉGIÓ ÉS A 88 KÜLDETÉS (ez a szerkezet kőbe vésve)

A régiók között **csak a Legio Rail gőzvonatával** lehet közlekedni (jegy kell; **nappal indulnak**).

| # | Régió | Szint | Csúcspont | Küldetés |
|---|---|---|---|---|
| 1 | **Hollowmier és külterülete** | 1–5 | a Kráter-domb őre | 22 |
| 2 | **Blackbriar · Verhollow · Needle Ridge** | 5–10 | **VÉRNÁSZ ★** | 22 |
| 3 | **Sorrow's Reach · A Hidak · Gallowmere** | 8–14 | **FEJNÉLKÜLI LOVAS ★** | 22 |
| 4 | **Lapides Ululantes · Caro Deorum** | 12–18 | **VALERIUS MENENIUS ★★** | 22 |

**22 küldetés régiónként** = 5 történet + 8 tábla (ismételhető) + 4 vizsgálat/mentés +
3 elit/legendás + 2 karakter. **Összesen 88**, ebből 34 ismételhető.

**A szörnyek ismétlődnek — szándékosan:** a szörnycsalád régióhoz kötött, mint az élővilág
(mocsár: vámpír/kísértet; bánya: zombi/gólem). Az ismétlést három dolog menti meg:
1. az első találkozásnál bestiárium-bejegyzés jár → a másodiknál már tudod a gyenge pontot;
2. az elit variáns új képességet kap;
3. a jutalom ritka crafting-anyag a bossokhoz.
Gyakorlati tipp: a 22 táblás/elit küldetést **generálni** kell (régió × szörnycsalád × helyszín ×
időpont × szint), csak a **20 történet-küldetést** kell kézzel megírni. Az adatbázis már így épül fel.

**A vonal rejtélye (IV. felvonás csattanója):** a Legio Rail zarándokvonalát a kráterig
**Blackwood építette** — a vasút a **köveket szállítja**.

---

## A TÖRTÉNET — a csattanók sorrendje

| Felvonás | Amit a játékos hisz | Amit valójában |
|---|---|---|
| I. | Elrabolt gyereket kell megkeresni | Eli nem elrabolt: **elment** valakiért |
| II. | A szörnyek természeti csapások | **Mind ugyanabból a műhelyből** jönnek |
| III. | A megbízó a Birodalom | **Iulia Severa** (a kém) nem az, akinek látszik |
| IV. | A gyerek apja halott | **Él, négyszáz éves, és Hollowmier legbefolyásosabb embere** |
| V. | Meg kell védeni Elit | A kérdés: **mit kezdesz Elivel** (3 befejezés) |

**Főszereplők:**
- **Elias Weir („Eli")** — varázsereje van, **kő nélkül**, évszázadok óta az első. Nem született: **megalkották**; az ára az anyja (**Maren**) élete volt.
- **Valerius Menenius („a Vén Kígyó")** — a fiú apja, a végső ellenség. A legnagyobb mágus; **ő robbantotta ki a Nagy Mágusháborút**; mágiával és tudománnyal alkotja a szörnyeket. Több kő van a testébe varrva → négyszáz éve él. **Polgári álcája: Dr. Asher Blackwood**, a *Blackwood Steamworks* tulajdonosa — **a vadászok tőle vásárolják a felszerelésüket**.
- **Iulia Severa** — birodalmi kém, utazó fényképésznőnek adva ki magát. **Ő adja a megbízást** (a játék elején ezt még nem lehet tudni).

---

## FÁJLOK

```
README.md                 – projekt-áttekintés
CONTINUE_HERE.md          – ez a fájl (folytatáshoz)
docs/KONCEPCIO.md         – teljes tervezési jegyzet (világ, harci, HUD, scope)
docs/NEVEK_ES_SZORNYEK.md – nevek, helyszínek, bestiárium, tutorial
data/quests.csv           – 88 küldetés: régió, adó, szörny, ölésmód, felkészülés, jutalom, szint
godot/green_filter.gdshader – a zöldes filter (CanvasLayer + ColorRect)
galeria/koncepcio_galeria.html – egy lapos, önmagába zárt koncepció-galéria
art/*.jpg                 – 27 koncepciós kép (vadászok, szörnyek, városok, izometrikus nézet)
hud/*.jpg                 – fekvő HUD-terv, zöld filter demó, színpaletta, régió-térkép
tools/*.py                – a képek/dokumentumok generátor-szkriptjei
```

---

## AMI NYITOTT (a következő döntések)

1. **A 20 történet-küldetés lineáris-e** (1→2→3→4) vagy a régiók nyitottak, és csak a szintek tartanak vissza?
   (Ha nyitott: a játékos maga fedezheti fel, hogy a szörnyek egy műhelyből jönnek.)
2. **Severa** végül kinek az oldalán áll — a Birodalomé, a Vén Kígyóé, vagy a sajátjáé?
3. **Eli sorsa** a végén: a Birodalomé (fegyver), az apjáé (örökös), vagy a vadászoké (ember)?
4. **Vesper** elmondja-e, hogy hallja a szellemeket?
5. **Aurel** megtudja-e, hogy Thorne ölte meg az apját — és mit tesz?
6. **Menenius** valóban gonosz-e, vagy négyszáz év magány után csak nem akar egyedül lenni?

---

## KÖVETKEZŐ TECHNIKAI LÉPÉSEK

- **Godot adatrendszer:** `MonsterData` és `QuestData` Resource-osztályok, amik a `quests.csv`-t betöltik
  + GDScript generátor a tábla-küldetésekhez.
- **A 20 történet-küldetés folyamatábrája** (melyik nyitja a következőt, hol a csattanó).
- **Vertical slice terv:** Hollowmier egy utcája + a verhollowi bánya (a zombi-szerződés = a tutorial).
- **Karakter-animáció:** Spine vagy Godot `Skeleton2D` (cutout) — 8 irányos frame-by-frame izometriában nem járható.

---

## BEMÁSOLHATÓ ÜZENET EGY ÚJ CHATHEZ

> Szia! A **Vérkő** nevű játékon dolgozunk — 2D izometrikus, fekvő képernyős mobil akció-RPG
> Godot 4.7-ben, monster hunter (Witcher-stílusú szerződésekkel), Hades-látvánnyal, cowboy
> aranykorban, egy alternatív időkben, ahol **a Római Birodalom uralja Amerikát**, és a mágiát
> (az „égkövet") évszázadokkal ezelőtt betiltották, ezért a világ steampunk tudományra épül.
> A játékos **Vesper Crane** („Varjú"), a másik két vadász **Aurel Mercer** és **Gaius „Vén Medve"
> Thorne**.
>
> Van egy teljes koncepciós csomagom (a repóban: `docs/KONCEPCIO.md`, `docs/NEVEK_ES_SZORNYEK.md`,
> `data/quests.csv`, `art/`, `hud/`, `godot/green_filter.gdshader`). A világ 4 régióra oszlik
> (Hollowmier és külterülete; Blackbriar/Verhollow/Needle Ridge; Sorrow's Reach/A Hidak/Gallowmere;
> Lapides Ululantes/Caro Deorum), amiket **csak a Legio Rail gőzvasútjával** lehet megközelíteni.
> Régiónként 22 küldetés van (88 összesen). Minden szörnyet **másképp** kell megölni, ahogy a
> legendák tartják (ezüstgolyó, lefejezés, karó a szívbe, a név kimondása stb.). A gyerek
> (**Elias Weir**) kő nélkül varázsol — évszázadok óta az első —, és **az apja, Valerius Menenius
> a főgonosz**, aki a Nagy Mágusháborút kirobbantotta és a szörnyeket alkotja; a vadászoknak egy
> **birodalmi kém, Iulia Severa** adta a küldetést, és ezt a játék elején még nem lehet tudni.
>
> Kérlek, először olvasd el a `CONTINUE_HERE.md` és a `docs/KONCEPCIO.md` fájlt, és onnan
> folytassuk. A válaszokat magyarul, közvetlenül, konkrét tippekkel kérem.


<!-- ============ docs/KONCEPCIO.md ============ -->

# VÉRKŐ — Koncepció és tervezési jegyzet

**Korszak:** alternatív **cowboy aranykor** (1800-as évek vége) — a Római Birodalom uralma alatt, gőz-technológiával (steampunk). Autók még nincsenek: **ló, gőzvasút, gőzhajó**.
**Műfaj:** 2D **izometrikus**, **fekvő képernyős** akció-RPG (monster hunter), mobilra
**Hangulati képlet:** Hades vizuális nyelve × The Witcher szerződéses szörnyvadászata × RDR2 vadnyugat × római birodalom × steampunk horror
**Főhős:** **Vesper Crane** („Varjú”) — a játékos karakter
**Motor:** Godot 4.7 (vagy 4.6.1+)

> Kapcsolódó: **`NEVEK_ES_SZORNYEK.md`** · **`kontroll_es_hud_fekvo.png`** (fekvő HUD) · **`zold_filter_demo.png`** + **`godot/green_filter.gdshader`** · **`paletta.png`** · **`koncepcio_galeria.html`**

---

## 1. Logline

> A Római Birodalom uralta alternatív vadnyugaton — ahol a mágiát évszázadokkal ezelőtt betiltották,
> és az emberiség a gőzbe kapaszkodik — **Vesper Crane** és három vadásztársa megbízást kap egy
> birodalmi kémtől: találják meg a fiút, **Elias Weirt**, és adják át a megbízónak.
> **A fiú az utolsó élő mágus — kő nélkül. Az apja pedig az, aki a Nagy Mágusháborút kirobbantotta,
> és aki négyszáz éve minden szörnyet megalkotott.**

---

## 2. A világ rendje

### 2.1 Az idővonal

| Kor | Esemény |
|---|---|
| Ókor | Meteorzápor (**a Nagy Zuhanás**) → **égkő** a földön. A kő nyakláncon (lassú, biztonságos) vagy **bőr alá varrva** (erős, de elmebajhoz vezet) |
| Ókortól | Aki követ varratott a testébe, **több száz évig él** — cserébe **nem lehet gyereke** |
| **A Nagy Mágusháború (14–15. sz.)** | **Menenius indította el.** Mágusok és emberek háborúja. Az emberek nyertek. |
| A **Vaskonzílium** (*Edictum Lapidis*) | **Az égkő birtoklása és használata főbenjáró bűn.** Az emberiség a **tudományra és a gőzre** fordul. |
| 16–18. sz. | Gőzkorszak. Amerika **többnyire római gyarmat** lesz. |
| **A jelen (~1880)** | Hollowmier és a többi gőzváros virágzik, a **Legio Rail** szeli a kontinenst. A szörnyek elszaporodtak — a Birodalom „fertőzésnek" nevezi őket, és fejpénzt fizet. |

### 2.2 A tiltás — és amiért a játékos sem használhat követ

**Az égkő tilos.** A birtoklásáért akasztófa jár, a használatáért máglya.

- A Birodalom **hivatalosan nem hisz a mágiában** — a szörnyek „betegségek". Ez kényelmes hazugság:
  a hatóság tudja az igazat, de nem ismerheti el, mert akkor el kellene ismernie, hogy a tiltás nem működik.
- A vadászok ezért **illegális-közeli** lények: nélkülük nem lehet élni, velük nem lehet együtt élni.
- **A vadászok tudása (ezüst, karó, só és vas, a név kimondása) babonának számít a tudomány korában** — mégis ez az egyetlen, ami működik.

> **A játékos soha nem használ követ.** Nincs korrupció-mérő, nincs tiltott erő. Amije van:
> **potion, fegyverek és tudás** (a bestiárium és a felkészülés). A mágia a világban van jelen —
> az ellenségekben, a szörnyekben és a rejtélyekben —, nem a játékos kezében.

### 2.3 Steampunk — a tudomány mint birodalmi vallás

| Elem | Szerep |
|---|---|
| **Gőz-akvadukt** | A római vízvezetékeket gőzvezetékké alakították: sárgaréz szelepek, nyomásmérők, sziszegő gőz a város fölött |
| **Legio Rail** | Emelt pályás gőzvasút — **a fast-travel**, és ürügy, hogy a világ zónákra tagolódjon |
| **Gőznegyed** | Katránházak, gyárak, munkásnegyedek, korom |
| **Mechanicus kaszt** | A tudós-mérnökök rendje — ők adják a vadászok legális eszközeit |
| **Aether-detektor** | Sárgaréz műszer: **a tiltott mágia nyomait** méri. Vesper első számú eszköze |
| **Gőz-gauntlet, mechanikus protézisek** | Sárgaréz, szelep, nyomásmérő — sérült vadászok és katonák |
| **Nincs autó** | Helyette: lovak, szekér, gőzvasút, gőzhajó |

---

## 3. A fő rejtély: a fiú és az apja

**Ezt a játék elején nem lehet tudni — a játékos csak a nyomokat gyűjti.**

### 3.1 Elias Weir — „Eli”

- **Varázsereje van, de nincs benne kő.** Ez évszázadok óta nem történt meg: a kővel élő mágusok nem tudnak gyereket nemzeni, a nem-mágusok pedig nem tudnak varázsolni.
- Eli tehát **nem született: megalkották.** Az apja négyszáz év alatt minden próbálkozása kudarc volt — Eli az első siker, és az ára egy élet volt (az anyjáé).
- Emiatt **ő a legértékesebb lény a kontinensen**: belőle nem lehet „csak" egy új mágus, hanem egy **mágikus vérvonal** — nemzedékek, akik nem halnak meg száz év alatt, és nem őrülnek meg a kőtől.

### 3.2 Valerius Menenius, a Vén Kígyó — a végső ellenség

- **A legnagyobb mágus, aki valaha élt.** Testébe **több követ** varratott — négyszáz éve él.
- **Ő robbantotta ki a Nagy Mágusháborút**, és ő vesztette el. Az emberek a kövek betiltásával válaszoltak.
- Azóta **mágia és tudomány keverékével alkotja a szörnyeket**: zombik, gólemek, az alkimista, a menyasszony, a fejnélküli lovas — a legtöbb „szörnyeteg" az ő műhelyéből szabadult el.
- **A polgári álcája: Dr. Asher Blackwood**, a *Blackwood Steamworks* tulajdonosa Hollowmier Gőznegyedében.
- **A gyomros:** a vadászok **pont tőle vásárolják a felszerelésüket** — az aether-detektort, az ezüst-bevonatot, a gőz-gombokat. A mecénás, aki a Mechanicus-rendet is pénzeli, az, aki a szörnyeket gyártja.

### 3.3 A birodalmi kém — aki adta a megbízást

- **Iulia Severa ügynök**, a Birodalmi Cursus (a hírszerzés) embere. Utazó fényképésznőnek adja ki magát.
- Ő adja a vadászoknak a megbízást: *„Találjátok meg a fiút, élve, és hozzátok el."* A papíron ez egy egyszerű szerződés.
- **Amit a játék elején senki sem tud:** Severa nem úgy dolgozik, ahogy mondja. A vadászok **megbízható, senkivel sem kapcsolatban lévő civilek**, akiket senki sem gyanúsít — pontosan ezért őket használja. Később kiderül, kinek az oldalán áll (a birodalomé? a Vén Kígyóé? a sajátjáé?), és hogy a vadászok **végig eszközök voltak**.

### 3.4 A csattanók sorrendje (a játék felépítése ezt szolgálja)

| Felvonás | Amit a játékos hisz | Amit valójában |
|---|---|---|
| I. | Egy elrabolt gyereket kell megkeresni | Eli nem elrabolt: **elment** valakiért |
| II. | A szörnyek természeti csapások | **Mind ugyanabból a műhelyből** származnak; az aether-detektor „véletlenül" mindig a helyes irányba mutat |
| III. | A megbízó a Birodalom | Severa egy **harmadik úrnő** szolgálatában áll… vagy a sajátjában |
| IV. | A gyerek apja halott | **Él, négyszáz éves, és Hollowmier legbefolyásosabb embere** |
| V. | Meg kell védeni Elit | **A kérdés nem az, hogy megölöd-e Meneniust, hanem hogy mit kezdesz Elivel** |

---

## 4. A három vadász

**A játékos: Vesper Crane.** A tábortűznél **két férfi vadász** ül — hárman alkotják a csapatot.

| | **Vesper Crane** — *„Varjú”* (**játékos**) | **Aurel Mercer** | **Gaius „Vén Medve” Thorne** |
|---|---|---|---|
| Kor / jelleg | fiatal nő, fürkésző, visszafogott | fiatal férfi, karizmatikus, pimasz | idős férfi, nehéz testű, sebhelyes |
| Eredet | orvos lánya, a családja kitagadta | vándorcirkusz gyereke, eladták a vadászoknak | katona-dezertőr |
| Fegyver | **gladius + puska a hátán; 2 revolver + kés az övén** | iker revolver + sörétes | sörétes + potion-öv + sárgaréz gőz-lábsín |
| Szakterület | **nyomkövetés, bestiárium, aether-detektor** | **harc, fegyverek, reflex** | **főzetek, ellenszerek, a régi babona** |
| Ad a játékosnak | — (ő a játékos) | fegyver-fejlesztés, ütéskombók | potion-receptek, bevonatok, ölésmódok |
| Titka | **hallja a szellemeket — és hazudik róla** | az apja mágus volt | **ő ölte meg Aurel apját 30 éve** |

> **A tábortűz drámai magja:** Thorne és Aurel között ott van egy meg nem beszélt gyilkosság.
> Vesper az, aki összerakja a darabokat — és közben a saját titkát is rejtegeti.
> A tűz drámai íve: nyugodt munka → feszültség → hallgatás → szembesítés.

## 5. A világ szerkezete — 4 régió, 88 küldetés

A világ **négy régióra** oszlik. A régiók között **csak a Legio Rail gőzvonatával** lehet közlekedni:
**jegy kell hozzá**, és a járatok **nappal indulnak** (éjszaka a szerelvény nem hagyja el az állomást).

| # | Régió | Szint | Helyszínek | Szörnycsaládok | Csúcspont |
|---|---|---|---|---|---|
| **1** | **Hollowmier és külterülete** | 1–5 | Hollowmier (7 negyed), Kráter-domb, kikötő, külterületi tanyák | zombi, vámpír-szolga, kísértet, gólem (prototípus) | a Kráter-domb őre (mini-boss) |
| **2** | **Blackbriar · Verhollow · Needle Ridge** | 5–10 | szénégető erdő, bánya- és kohóváros, sziklahegy-hát | farkasember, zombi, gólem, kísértet, alkat | **VÉRNÁSZ ★** |
| **3** | **Sorrow's Reach · A Hidak · Gallowmere** | 8–14 | mocsaras folyófalu, híd és komp, kápolna és temető | vámpír, kísértet, szellem, léleklámpás | **FEJNÉLKÜLI LOVAS ★** (3 fázis) |
| **4** | **Lapides Ululantes · Caro Deorum** | 12–18 | a tiltás kőoszlopai, zarándok-tábor, a legfrissebb kráter | múmia, gólem, alkat, zombi (mélység) | **VALERIUS MENENIUS ★★** |

**A vonal rejtélye:** a Legio Rail utolsó szakaszát — a zarándokvonalat a kráterig — **Blackwood építette**.
A gőzvasút nem a polgárok kényelmét szolgálja: **a köveket szállítja**. Ez a IV. felvonás egyik csattanója.

### 5.1 22 küldetés régiónként — a recept

| Típus | Darab | Mi ez |
|---|---|---|
| **Történet** | 5 | a főszál; soha nem ismételhető, egyedi helyszín és párbeszéd |
| **Tábla** (ismételhető) | 8 | Aggie kocsmájából vagy a szerződés-tábláról; a grind alapja |
| **Vizsgálat / mentés** | 4 | harc nélküli vagy részleges harc: nyomolvasás, NPC-k kimentése |
| **Elit / legendás** | 3 | nehezebb variáns, crafting-anyag jutalommal; a bossok előszobája |
| **Karakter** | 2 | a tábortűz-párbeszédek, a vadászok múltja, Vesper naplója |
| **Összesen** | **22** | négy régió = **88 küldetés** |

**A teljes adatbázis: `quests.csv`** — 88 sor, minden sorban a régió, a küldetésadó NPC, a szörny,
az **ölésmód**, a **felkészülés**, a jutalom, az ismételhetőség és az ajánlott szint.
Ez a fájl **közvetlenül betölthető Godotba** (CSV → `Resource`-tábla vagy `Array[Dictionary]`).

### 5.2 Miért ismétlődnek a szörnyek — és mitől nem lesz unalmas

A szörnycsalád **régióhoz kötött, mint az élővilág**: a mocsárban vámpír és kísértet van, a bányában
zombi és gólem. Az ismétlés nem lustaság — ez a világ biológiája, és **három dolog menti meg**:

1. **A tudás.** Az első találkozásnál a bestiárium bejegyzést kap (gyenge pont, ölésmód). A másodiknál
   már *tudod*, mit kell tenni → gyorsabb, taktikusabb, élvezetesebb harc. **A játékos fejlődése a valódi jutalom.**
2. **Az elit variáns.** Méret, szín és **egy új képesség** (pl. a bányász-zombi robban, a vérnász-fia ketten támad).
3. **A jutalom.** Ismételt küldetés → ritka crafting-anyag, amit a bossokhoz és a gőz-eszközökhöz kell.

> **A "20+ küldetés/régió" nem ambíció, hanem a szerkezet következménye:** ezt a számot a *típusok*
> adják ki (5+8+4+3+2), nem új szörnyek. Az új szörny drága; az új *körülmény* (helyszín, időpont,
> szint, történet) olcsó — és a játékos ugyanannyit kap.

## 6. A tábortűz — a játék szíve

**Nem bázis, nem építés: egy tűz, körülötte a négy vadász, és vándorol veled.**

| Funkció | Mit ad |
|---|---|
| **Potion-főzés** | gyógyító, erő, éjszakai látás |
| **Felkészülés** | ezüst-bevonat, tűzolaj, só-vas, szentelt víz, karó kiválasztása a szerződéshez |
| **Szerződés** | itt olvasod el a megbízást (Severától vagy a szerződés-tábláról) |
| **Párbeszéd** | a három NPC itt ad infót; itt nő a feszültség Thorne és Aurel között |
| **Bestiárium** | a felfedezett gyenge pontok és ölésmódok |
| **Pihenés** | idő múlik, **napszak vált** — éjszaka jönnek a szörnyek; **mentés** |
| **Vendégek** | a küldetésadó NPC-k **kijönnek a tűzhöz** — nem kell a városba visszajárni |

**A tűz mint drámai eszköz, felvonásonként:**
- **I.:** erdőben, nyugodt, mindenki a helyén
- **II.:** falu széle, bánya szája, mocsár — kevesebb élelem, feszültebb párbeszédek
- **III.:** hegyi hágó, vihar — már alig beszélnek egymással
- **IV.:** a tűz körül megjelennek **Eli holmijai** — némán, magyarázat nélkül

> Nulla technológia (nincs építés, nincs NPC-napi rutin), mégis élő: a hub **jön veled**.
> Mobilon ez aranyat ér.

---

## 7. Nézet, képernyő és kamera

- **Izometrikus, fix (nem forgatható) 2:1 kamera.** Mobilon a forgatás drága és zavaró.
- **Fekvő (landscape) képernyő** — ezzel kell tervezni a HUD-ot is: **`kontroll_es_hud_fekvo.png`**
- **Fal-átlátszóság kötelező:** a játékos előtti falak/tetők félig átlátszóvá válnak, különben a karakter eltűnik az épületek mögött.
- **Animáció:** 8 irányos frame-by-frame izometriában öngyilkosság. **Cutout/csontváz** (Spine vagy Godot `Skeleton2D`), vagy 4 irány + tükrözés.
- **A legkritikusabb beállítás:** a karakter **talpa a gyémánt közepére** essen (`TileMapLayer` → `tile_shape = Isometric`, `y_sort_enabled`). Ezt **az első napon**, mielőtt bármit rajzolsz.

---

## 8. Harc, fegyverek és HUD

**Hat fegyver, egy sávon** (a sorrend a játékos igényei szerint: közelitől a távoliig):

| # | Fegyver | Szerep |
|---|---|---|
| 1 | **Gladius** (ezüstözött, római penge) | fő közelharc, 3 ütemű kombó — a szörnyek többségét ez végzi ki |
| 2 | **Balta** | lassabb, nagyobb sebzés, töri a csontot és a pajzsot |
| 3 | **Kés** | gyors, hátulról dupla sebzés; **kegyelmi/lefejező mozdulat** |
| 4 | **Revolver** (ezüst lövedék) | távoli, célzásnál auto-lassítás („vadász-szem"), 6 lövés, utána újratöltés |
| 5 | **Sörétes** | közeli robbanás, lökéshullám — tömeg ellen |
| 6 | **Puska** | nagy hatótáv, pontos, lassú újratöltés — az elit és a boss ellen |

**Vesper felszerelése:** gladius és puska a hátán (átlósan), két revolver és egy kés az övén,
**mellkasán átfutó töltényöv ezüst lövedékekkel**, sárgaréz aether-detektor. **A nyakában nincs kő.**

**HUD (fekvő):**

| Elem | Pozíció |
|---|---|
| Joystick | bal alsó (nagyobb, mert fekvőben van hely) |
| HP-sáv | bal felül, a minimap alatt |
| Minimap | bal felül — **R** = Vigiles, **P** = bolt, **!** = küldetés, **T** = **tábortűz (mozog)** |
| Potik (3) | jobb felül, darabszámmal, gyűrű = töltés |
| Ütések, védekezés, kitérés | jobb alsó, a fő fegyver a legnagyobb |
| **Fegyverválasztó** | **alsó közép — vízszintes 6-os sáv** (fekvőben a köralak helyett; egy húzással végigcsúsztatható) |
| Küldetés-célzó | felső közép (opcionális) |

**Nincs korrupció-mérő** — a játékos nem használ követ.

---

## 9. A zöldes, halloweeni filter

Demó: **`zold_filter_demo.png`** · Shader: **`godot/green_filter.gdshader`**

| Hely | strength |
|---|---|
| nappali Hollowmier | 0.15 |
| este, utca | 0.40 (**a fő hangulat**) |
| erdő, temető | 0.55 |
| mocsár, kráter, legendás zóna | 0.75 |
| boss-harc (fejnélküli lovas!) | 0.60 + lassú pulzálás |

**A tábortűz az egyetlen hely, ahol a filter visszaáll alacsonyra** — a meleg narancs kontrasztja a zöld világgal adja a „hazaértem" érzést.

**Amit ne csináljon:** ne szűrje a HUD-ot és a portrékat; a sebzés-visszajelzés maradjon piros/sárga; színvak-opció és erősség-csúszka kell; mobilon filmszemcse 0.0.

---

## 10. Costume design — cowboy aranykor + Róma

| Ki | Visel |
|---|---|
| **Városi rendőr (Vigiles)** | hosszú bőrkabát, karimás kalap réz sas-jelvénnyel, vörös öv, **csillag alakú réz jelvény sassal**, mélyen hordott revolver |
| **Birodalmi katona** | sötétkék lovas-ing vörös szegéllyel, fekete nadrág, csizma sarkantyúval, vörös nyakkendő, **mellre varrt hímzett sas-jelvény**, karabély |
| **Császári testőr (Praetoriani)** | fekete bőrkabát arany sas-hímzéssel, bőr vállköpeny arany rojttal, fekete kalap díszes réz sassal, fehér kesztyű, kard és iker revolver, **sárgaréz gőzcsövek** a kabát hátán |
| **Vadászok** | kopott duster, karimás kalap, vörös nyakkendő, töltényöv; Vespernél **varjútoll-köpeny** és gladius |

A római jelek **felvarrt, hímzett jelvények** (sas + SPQR), nem ókori páncél.

---

## 11. Scope — a reális út

**A Legio Rail a barátod:** a gőzvasút indokolja, hogy a világ **zónákra** tagolódjon, és a vasút a fast-travel.

1. **Vertical slice (2–4 hónap, 1–2 fő):** Hollowmier egy utcája + a verhollowi bánya, a zombi-szerződés (= a tutorial), a harc, a HUD, a tábortűz — Androidon, fekvő módban.
2. **Egy régió (6–10 hónap):** az **1. régió teljes** (Hollowmier + külterület, 22 küldetés, 1 mini-boss), napszak, tábortűz, gőzvonat.
3. **Nagy játék:** a 2–4. régió (regionális szörnycsaládokkal), a Menenius-szál teljes kibontása, több befejezés.

**Ne, elsőre:** lovaglás, úszás, teljes időjárás, NPC-napi rutin, forgatható kamera, szinkronhang, autók.

**Igen, elsőre:** 1 szörny teljesen kidolgozva · olyan harc, ami üres szobában is élvezetes · a 3 potion · a talp-pozíció az izometrikus rácsban · 30–60 FPS és 15 perces hőteszt.

---

## 12. Nyitott kérdések

1. **Severa** végül kinek az oldalán áll — a Birodalomé, a Vén Kígyóé, vagy a sajátjáé?
2. **Eli** sorsa a végén: a Birodalomé lesz (fegyver), az apjáé (örökös), vagy a vadászoké (ember)?
3. **Vesper** elmondja-e, hogy hallja a szellemeket — és mit jelent ez Elivel, aki maga is „tiszta" mágia?
4. **Aurel** megtudja-e, hogy Thorne ölte meg az apját — és mit tesz?
5. **Menenius** valóban gonosz-e, vagy csak egy apa, aki négyszáz év magány után végre nem egyedül akar lenni?


<!-- ============ docs/NEVEK_ES_SZORNYEK.md ============ -->

# Nevek, helyszínek és a szörny-küldetések rendszere

*Korszak: a cowboy aranykor (1800-as évek vége) — Római Birodalom, gőz-technológia.
A kő (égkő) használata **főbenjáró bűn** a Vaskonzílium óta. Autók nincsenek.*

**A korszak kulcsa:** nem napóleoni kor. Cowboy-kalap, frakk, töltényöv, sarkantyú, lovak és gőzvasút —
a Birodalom jelvényeivel (felvarrt, hímzett sas és SPQR). Ókori páncél nincs, a márvány a
városépítészetben jelenik meg.

---

## 1. Névadási elvek

| Réteg | Szabály | Példa |
|---|---|---|
| **Római hivatalos** | latin, hivatalnoki | *Colonia Corvina*, *Praetor*, *Vigiles* |
| **Telepes / angol** | puritán vagy ó-angol, dísztelen | *Hollowmier*, *Blackbriar*, *Gallowmere* |
| **Bennszülött** | törzsi, a Birodalomtól független | *Kharis*, *Vetchet*, *Owasco-völgy* |
| **Vadász becenév** | tárgyias, kemény, egy szó | „Vén Medve”, „Varjú”, „Prédikátor” |
| **Szörny-név** | a szörnyeknek is legyen nevük! | *„Vérnász”, „Karmazsin asszony”, „Adam Vale”* |

> A szörnyek ne névtelenek legyenek: az „egy farkasember” senkit nem érdekel —
> *„a briari Owen Barlow, aki nappal családapa”* igen.

---

## 2. A szereplők

### A vadászok (hárman)

| Név | Ki ő |
|---|---|
| **Vesper Crane** — *„Varjú”* | **A JÁTÉKOS.** Fiatal nő, orvos lánya, a családja kitagadta. Nyomkövetés, bestiárium, aether-detektor. **Titka: hallja a szellemeket.** |
| **Aurel Mercer** | Fiatal férfi, karizmatikus mesterlövész. Iker revolver, sörétes. **Titka: az apja mágus volt.** |
| **Gaius „Vén Medve” Thorne** | Idős férfi, nehéz testű, sebhelyes. Sörétes, potion-öv, sárgaréz gőz-lábsín. **Titka: ő ölte meg Aurel apját 30 éve.** |

### A fő rejtély szereplői

| Szereplő | Ki ő |
|---|---|
| **Elias Weir** — „Eli” | **A fiú.** Van varázsereje, de **nincs benne kő** — évszázadok óta az első. Nem született: **megalkották.** |
| **Valerius Menenius** — „a Vén Kígyó” | **A végső ellenség. A fiú apja.** A legnagyobb mágus, aki valaha élt; **ő robbantotta ki a Nagy Mágusháborút**, és ő alkotja a szörnyeket mágiával és tudománnyal. Több kő van a testébe varrva: **négyszáz éve él.** Polgári álcája: **Dr. Asher Blackwood**, a *Blackwood Steamworks* tulajdonosa — aki a vadászok felszerelését is gyártja. |
| **Iulia Severa ügynök** | **A birodalmi kém**, aki a vadászoknak a megbízást adta. Utazó fényképésznőnek adja ki magát. A játék elején senki sem tudja, kinek dolgozik. |
| **A fiú anyja** | Csak emlék és egy név: **Maren**. Az ő életébe került Eli. |

### NPC-k, akik küldetést adnak

| Név | Hol | Szerep | Témája |
|---|---|---|---|
| **Cato Vint** | Hollowmier, hullaház | a halottak ismerője | zombik, holttestek, boncolás |
| **Father Bram** | Gallowmere kápolna | pap, aki hisz a szellemekben | szellemek, eltemetés, szertartások |
| **Old Mam Rachel** | Sorrow's Reach mocsár | javasasszony, potion-mester | átkok, léleklámpás, mérgek |
| **Wend Fisk** | Blackbriar szénégető | félénk favágó | farkasember-nyomok |
| **Tribune Livia Corvina** | Hollowmier, Vigiles | birodalmi rendőrtiszt | szerződések, a tiltás betartatása |
| **Isolde Karr** | Hollowmier, Gőznegyed | **mechanica** | a steampunk felszerelés, „a legális erő” hangja |
| **Kharis** | vándorló kereskedő | a Vetchet népének utolsója | sírok, a kő eredeti szertartása |
| **Aggie Dow** | Hollowmier, Saloon-negyed | kocsmáros | pletykák, új szerződések a térképen |

### Szörny-szereplők, akiket nem kell megölni

| Név | Ki ő |
|---|---|
| **Adam Vale** | Az alkimista teremtménye (Frankenstein). Beszél, emlékszik — segítséget kér. |
| **Ada** | A menyasszony. Fél, és nem akar bántani senkit. |
| **Owen Barlow** | A briari farkasember — nappal családapa. |
| **Silas Gray** | Az a katona, aki lelőtte Charon Walsh-t. Az átok őt is üldözi. |

---

## 3. A világ szerkezete — 4 régió

A régiók között **csak a Legio Rail gőzvonatával** lehet közlekedni (jegy kell; nappal indulnak).

| # | Régió | Szint | Mi van benne | Csúcspont |
|---|---|---|---|---|
| 1 | **Hollowmier és külterülete** | 1–5 | a város 7 negyede, Kráter-domb, kikötő, tanyák | a Kráter-domb őre |
| 2 | **Blackbriar · Verhollow · Needle Ridge** | 5–10 | szénégető erdő, bánya és kohó, sziklahegy-hát | **VÉRNÁSZ ★** |
| 3 | **Sorrow's Reach · A Hidak · Gallowmere** | 8–14 | mocsár, híd és komp, kápolna és temető | **FEJNÉLKÜLI LOVAS ★** |
| 4 | **Lapides Ululantes · Caro Deorum** | 12–18 | a tiltás kőoszlopai, zarándok-tábor, a friss kráter | **VALERIUS MENENIUS ★★** |

**22 küldetés régiónként** (5 történet + 8 tábla + 4 vizsgálat/mentés + 3 elit/legendás + 2 karakter),
négy régióban **88 küldetés**. A teljes adatbázis: **`quests.csv`** · a térkép: **`regio_terkep.png`**.

---

## 4. A helyszínek

**A város — NAGY VÁROS, hét negyeddel: HOLLOWMIER** (hivatalosan *Colonia Corvina*)

| Negyed | Hangulat | Mi van itt |
|---|---|---|
| **Saloon-negyed** | sár, olajlámpás, zongora, kártya | Aggie kocsmája, szerződés-tábla, pletykák |
| **A Fórum** | fehér márvány a sárban | Praetor palotája, bíróság, Vigiles-parancsnokság |
| **Gőznegyed** (*Vicus Vaporis*) | zúgás, gőz, korom | katránházak, gyárak, **Blackwood Steamworks**, Legio Rail pályaudvar |
| **Az Akasztófa-tér** | üres, szél fúj | kivégzések, tiltott kő-kereskedők, a vadászok munkaterülete |
| **A Kikötő** | köd, hajókürt | csempészek, gőzhajók |
| **A Kráter-domb** | zöld ragyogás | a tiltott meteor-kráter szentély, római zarándok-tábor |
| **A régi negyedek** | téglaházak, sűrű lakosság | őslakos, afrikai és kínai közösségek |

**A négy falu:**

| Falu | Hangulat | Szörnye |
|---|---|---|
| **BLACKBRIAR** | szénégető telep, korom, kivágott erdő | farkasember |
| **SORROW'S REACH** | félig víz alá került folyófalu, mocsár | vámpír, léleklámpás |
| **GALLOWMERE** | folyami átkelő, kápolna, régi temető, komp | szellemek |
| **VERHOLLOW** | bánya- és kohóváros, vörös izzás | zombik, gólem, az alkimista |

**Vadvidék:**

| Név | Mi van ott |
|---|---|
| **NEEDLE RIDGE** (Tűgerinc) | a legendás **Vérnász** vadászterülete |
| **A HIDAK** | a Gray-híd és a komp — **a fejnélküli lovas** köröz itt |
| **LAPIDES ULULANTES** (Üvöltő Kövek) | a Vaskonzílium kőoszlopai — a tiltás színhelye |
| **CARO DEORUM** (Az Istenhús) | a legfrissebb kráter, zöld szentély — a végső helyszín |

---

## 5. A szörnyek és a küldetéseik

**Az alapelv: minden szörnyet máshogy kell megölni — ahogy a legendák tartják.**
Ez ingyen ad tartalmat: nem kell új csapás-animáció, csak új **szabály**.

### 5.1 A szerződés-tábla (válogatás a 88-ból)

| # | Szörny | Hol | Ki adja | **Az ölés módja** | Mit tanít meg |
|---|---|---|---|---|---|
| 1 | **Zombi** — munkás-holt | Verhollow bánya | Cato Vint | **Lefejezés** — a fej nélküli test tovább jár | **A TUTORIAL**: mozgás, gladius, blokk, potion |
| 2 | **Léleklámpás** | Sorrow's Reach | Old Mam Rachel | **Eloltani** — vízzel vagy sárral | célzás, tárgyhasználat, lopakodás |
| 3 | **Farkasember** — Owen Barlow | Blackbriar | Wend Fisk | **Ezüst** — golyó *és* penge; a tűz csak gyorsítja | dodge-időzítés, felkészülés, holdfázis |
| 4 | **Szellem** — a megégetett nevek | Üvöltő Kövek | Father Bram | **Só, vas, és a neve kimondása** — elbocsátani, nem elpusztítani | nyomolvasás, döntés |
| 5 | **Múmia** — Kópharisz | a sírhalom | Kharis | **Az amulett eltávolítása** — a test megáll | körbejárás, gyenge pont, csapdák |
| 6 | **Gólem** — agyag-katona | Verhollow kohó | Isolde Karr | **A mágikus pecsét elpusztítása** | irányított célzás, mobilitás |
| 7 | **FEJNÉLKÜLI LOVAS** — Charon Walsh | **A HIDAK** | Father Bram | **Előbb megállítani** (templomi harang, szentelt föld, só-vonal), **utána ezüst pengével** (gladius) leütni. Amíg lovon ül és a lámpása ég, **sérthetetlen.** | boss-harc: fázisok, környezet-használat, a harang |
| 8 | **Vámpír** — lobogósok | Sorrow's Reach | Aggie Dow | **Karó a szívbe** + ezüst + nem szabad belépnie a küszöbön | napszak, szűk terek, fény |
| 9 | **Az alkimista** | Verhollow labor | Adam Vale | **Villám** és a szív — vagy a varratok elvágása | beszélgetés, csapdák, erkölcsi döntés |
| 10 | **A menyasszony** — Ada | Verhollow kripta | Adam Vale | **Az ezüst-kötés elvágása** | párharc: védd meg, ne öld meg |
| 11 | **Vérnász** ★ | Needle Ridge | Vén Medve Thorne | **A testébe varrt kő kivágása** — ezüst nem hat rá | kombinált boss, minden gomb |
| 12 | **Karmazsin asszony** ★ | régi villa | Iulia Severa | **Napfény, ezüst, a meghívás megtagadása** | napszak-tervezés, boss-fázisok |
| ★ | **Valerius Menenius** | Caro Deorum | — | **A saját kövei ellene fordítása** — négyszáz év terhét visszaadni | végső boss, több befejezés |

### 5.2 A fejnélküli lovas — miért jó boss?

- **Nem győzhető le pusztán sebzéssel.** Három fázis:
  1. **A hajsza** — a lovas végigvágtat a hídon; a játékos csak kitérni tud, miközben keresi a harangkötelet.
  2. **A megállítás** — meghúzza a gallowmere-i kápolna harangját: a ló megbokrosodik, a lovas leveti a lámpást.
  3. **A vég** — amíg a lámpás ég, sérthetetlen; el kell oltania (sár/víz), és ezüst pengével (gladius) végezni vele.
- **A lore:** Charon Walsh komp-üzemeltető volt; Silas Gray katona lőtte le egy vita miatt. Az átok nemcsak Walsh-t, **Gray-t is** üldözi — a küldetés végén a játékos dönthet, hogy Gray-t is megmenti-e.

### 5.3 A családok (variáns-logika)

| Család | Alap | Elit | Legendás |
|---|---|---|---|
| Zombi | munkás-holt | bányász-őr | a Verhollow-i mélység |
| Farkasember | barlow-i falka | „Vérnász fiai” | **Vérnász** |
| Vámpír | lobogós szolga | udvartartás | **Karmazsin asszony** |
| Kísértet | léleklámpás, sír-madarak | boszorkány-szellem | a megégetett nevek kórusa |
| Sír-őr | múmia-őrök | Kópharisz | a Vetchet király sírja |
| Élettelen | agyag-katona | kohó-őr | a pecsétes óriás |
| Kísérlet | szökevény-alkat | a menyasszony | **az alkimista** |

> 7 család × 3 szint = 21 ellenség, de csak **7 csapásmintát** kell megtervezni.
> Az elit és legendás variáns: méret, szín, egy plusz képesség. Mobilon ez a reális út.

### 5.4 A vadászat ritmusa (Witcher-érzés)

1. **Szerződés** — Severától vagy a tábláról.
2. **Nyomolvasás** — a helyszínen 2-3 tény (holttest, kaparás, tanú), aether-detektorral.
3. **Felkészülés a tűznél** — ezüst, tűzolaj, só-vas, karó, víz kiválasztása. **A rossz felkészülés nem kudarc: 3× hosszabb harc.**
4. **A vadászat** — a szörny viselkedése a nyomoktól függ.
5. **Döntés** — a végén néha nem az a kérdés, hogy meg tudod-e ölni, hanem hogy **meg kell-e**.

---

## 6. A tutorial — az első szerződés (a zombi)

| Szakasz | Mit mutat be | Hogyan |
|---|---|---|
| Hollowmier, hullaház | joystick, camera | sétálj Catóhoz, ő adja a szerződést |
| Verhollow, bánya bejárata | gladius, ütéskombó | két lassú zombi, olvasható támadással |
| Bányafolyosó | blokk és kitérés | egy zombi rádtámad — ki kell védeni |
| Bányafenék | **a lefejezés szabálya** | az első zombi nem hal meg ütéstől: a játék megtanítja, hova kell ütni |
| Napvilág | potion és felkészülés | Cato átadja az első receptet |
| A tábortűz | a hub megnyílik | itt ismered meg Aurelt, Thorne-t és Ezékielt |
| Szerződés-tábla | a világ megnyílik | három új szerződés kerül fel — köztük **A HIDAK** |

> A tutorial nem külön pálya, hanem **maga az első szörny** — elegánsabb és olcsóbb.

---

## 7. A zöldes filter

- Demó: **`zold_filter_demo.png`** · Shader: **`godot/green_filter.gdshader`**
- Erősség helyszínenként: nappal 0.15 · este 0.40 · erdő/temető 0.55 · mocsár/kráter 0.75 · **boss-harc 0.60 + lassú pulzálás**
- A **tábortűznél visszaáll 0.15-re** — ez adja a „hazaértem" érzést.
- **Ne szűrd át** a HUD-ot, a portrékat és a dialógus-hátteret; a sebzés-visszajelzés maradjon piros/sárga; színvak-opció és erősség-csúszka kell.

---

## 8. Nyitott kérdések

1. **Severa** végül kinek az oldalán áll?
2. **Eli** sorsa: a Birodalomé, az apjáé, vagy a vadászoké?
3. **Vesper** elmondja-e, hogy hallja a szellemeket — és mit jelent ez Elivel, aki maga is „tiszta" mágia?
4. **Aurel** megtudja-e, hogy Thorne ölte meg az apját?
5. **Menenius** valóban gonosz-e, vagy négyszáz év magány után csak nem akar egyedül lenni?
