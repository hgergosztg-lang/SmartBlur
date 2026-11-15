# SmartBlur
# SmartBlur – Mesterséges intelligencián alapuló képanonimizáló alkalmazás

## 1. A projekt bemutatása

A SmartBlur egy Python nyelven fejlesztett képanonimizáló alkalmazás, amely mesterséges intelligencia segítségével automatikusan felismeri és elhomályosítja a képeken található emberi arcokat és gépjárművek rendszámtábláit.

A projekt célja a személyes adatok és a magánszféra védelme, az érzékeny képi információk automatikus felismerésével és anonimizálásával.

## 2. Főbb funkciók

- Emberi arcok automatikus felismerése
- Személyek és gépjárművek felismerése
- Rendszámtáblák felismerése
- Automatikus képanonimizálás Gaussian blur eljárással
- Felismert arcok és rendszámok darabszámának megjelenítése
- Eredeti és anonimizált kép összehasonlítása
- Feldolgozott kép letöltése

## 3. Felhasznált technológiák

- **Python:** a programozási nyelv
- **Streamlit:** felhasználói felület létrehozása
- **OpenCV:** képfeldolgozás és a YuNet modell futtatása
- **Ultralytics YOLO26n:** objektumfelismerés
- **YuNet:** arcfelismerés
- **YOLO rendszámfelismerő modell:** rendszámtáblák helyének meghatározása
- **NumPy:** képi adatok feldolgozása
- **Pillow:** képek kezelése
- **ONNX:** gépi tanulási modellek formátuma

## 4. Projekt felépítése

```text
SmartBlur/
├── src/
│   ├── app.py
│   └── pipeline.py
├── models/
├── README.md
├── AI_USAGE.md
├── requirements.txt
└── .gitignore
```

## 5. Telepítés

A repository letöltése:

```bash
git clone https://github.com/hgergosztg-lang/SmartBlur.git
cd SmartBlur
```

Virtuális környezet létrehozása:

```bash
python -m venv .venv
```

Virtuális környezet aktiválása Windows rendszeren:

```powershell
.\.venv\Scripts\activate
```

Szükséges csomagok telepítése:

```bash
pip install -r requirements.txt
```

A működéshez szükséges előre betanított modelleket le kell tölteni, majd a megfelelő modellmappákba kell helyezni.

## 6. A program futtatása

Az alkalmazás elindítása:

```bash
python -m streamlit run src/app.py
```

A program ezután a böngészőben, helyi webes felületen használható.

## 7. Alkalmazott gépi tanulási modellek

**YOLO26n:** Általános objektumfelismerő modell, amely többek között személyeket és gépjárműveket képes felismerni.

**YuNet:** Arcfelismerő modell, amely ONNX formátumban, az OpenCV FaceDetectorYN felületén keresztül működik.

**YOLO rendszámfelismerő modell:** A gépjárművek rendszámtábláinak helyét határozza meg a képeken.

A projekt előre betanított modelleket használ, nem saját neurális hálózat tanításával működik.

## 8. A képfeldolgozás folyamata

1. A felhasználó feltölt egy képet.
2. A YOLO26n modell felismeri a személyeket és a gépjárműveket.
3. A program a felismert személyek területén belül arcfelismerést végez.
4. A felismert gépjárművek területén belül megtörténik a rendszámtáblák felismerése.
5. A program kiszűri az esetleges többszörös találatokat.
6. A felismert érzékeny képrészletekre Gaussian blur eljárást alkalmaz.
7. Az alkalmazás megjeleníti az anonimizált képet és a felismerési statisztikákat.

## 9. A projekt korlátai

A felismerés pontosságát befolyásolhatja a kép minősége, a megvilágítás, az objektumok mérete és az esetleges takarás.

A rendszer nem garantálja minden arc és rendszám felismerését, ezért különösen fontos a különböző képeken történő tesztelés.

A rendszámfelismerő modell a rendszámtábla helyét határozza meg, de nem olvassa ki annak szövegét (OCR).

## 10. Készítő

Egyéni egyetemi projekt – Python programozás és gépi tanulás.
