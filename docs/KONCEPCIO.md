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
