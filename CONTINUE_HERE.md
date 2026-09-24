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
