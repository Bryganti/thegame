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
