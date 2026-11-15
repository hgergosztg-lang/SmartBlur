# Mesterséges intelligencia használatának dokumentációja – SmartBlur

## 1. Felhasznált AI-eszközök

- **ChatGPT:** programozási segítség, hibakeresés, kódmagyarázat és dokumentáció elkészítése.

## 2. AI segítségével támogatott fejlesztési feladatok

### 2.1. Projektfelépítés megtervezése

**Cél:** Az alkalmazás felépítésének és főbb komponenseinek megtervezése.

**Példa a használt utasításra:**

„Segíts megtervezni egy Python alkalmazást, amely képeken felismeri az arcokat és a gépjárművek rendszámait, majd elhomályosítja ezeket.”

**Eredmény:** Javaslat az alkalmazás felhasználói felületének és képfeldolgozó részének különválasztására.

**Saját módosítás és ellenőrzés:** A javasolt felépítés a projekt követelményeihez lett igazítva.

### 2.2. YOLO objektumfelismerés integrálása

**Cél:** Előre betanított objektumfelismerő modell használata.

**Példa a használt utasításra:**

„Hogyan használhatom az Ultralytics YOLO modellt Pythonban személyek és autók felismerésére egy képen?”

**Eredmény:** Segítség a modell betöltéséhez, a képek feldolgozásához és a felismerési osztályok szűréséhez.

**Saját módosítás és ellenőrzés:** A megoldás a YOLO26n modellhez lett igazítva és helyi képeken tesztelve.

### 2.3. Arcfelismerés megvalósítása

**Cél:** A YuNet arcfelismerő modell integrálása OpenCV segítségével.

**Példa a használt utasításra:**

„Hogyan tudok egy YuNet ONNX modellt betölteni és használni az OpenCV FaceDetectorYN segítségével?”

**Eredmény:** Segítség a modell inicializálásához és az arcfelismerés megvalósításához.

**Saját módosítás és ellenőrzés:** A modell betöltése és a felismerési folyamat tesztelve lett. A modell elérési útját egy betöltési hiba megoldása érdekében módosítani kellett.

### 2.4. Képek anonimizálása

**Cél:** A felismert arcok és rendszámok elhomályosítása.

**Példa a használt utasításra:**

„Hogyan alkalmazhatok Gaussian blur eljárást egy kép meghatározott téglalap alakú területein OpenCV segítségével?”

**Eredmény:** Segítség a képrészletek kiválasztásához és az elmosási művelet alkalmazásához.

**Saját módosítás és ellenőrzés:** Az elmosási eljárás beépítésre került a képfeldolgozó folyamatba, majd tesztképeken ellenőrizve lett.

### 2.5. Felhasználói felület kialakítása

**Cél:** A Streamlit alapú felhasználói felület elkészítése.

**Példa a használt utasításra:**

„Hogyan készíthetek Streamlit alkalmazást, amely képfeltöltést, képfeldolgozást és az eredmény letöltését is lehetővé teszi?”

**Eredmény:** Segítség a képfeltöltés, az eredmény megjelenítése és a letöltési funkció megvalósításához.

**Saját módosítás és ellenőrzés:** A felület a SmartBlur működéséhez lett igazítva, majd helyi környezetben tesztelve.

## 3. Ellenőrzés és saját fejlesztői munka

Az AI által javasolt megoldások nem kerültek automatikusan elfogadásra. A kódok ellenőrzése, módosítása és tesztelése a helyi fejlesztői környezetben történt.

Az AI-eszközök programozási segítséget nyújtottak, de a végleges megvalósítás, a modellek integrálása és a projekt működésének ellenőrzése a fejlesztő feladata volt.

## 4. Összegzés

A ChatGPT a projekt során elsősorban a rendszer felépítésének megtervezésében, a programozási feladatok megoldásában, a hibakeresésben és a dokumentáció elkészítésében nyújtott segítséget.
