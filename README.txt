ARUCO Q&A WEBAR – PACHET
=========================

CE PRIMIȚI
- index.html — aplicație Web care detectează markere ArUco și afișează Întrebare/Răspuns.
- qna.json — 10 întrebări (Fake vs. Real) cu răspuns asociat (ID 0..9). Modificați liber.
- generate_aruco.py — script pentru generarea markerelor ArUco reale (ID 0..9).
- print_guide.html — ghid de print pentru markere.
- (opțional) markers/ — după ce generați cu scriptul.

PAȘI RAPIZI
1) PE PC: instalați Python 3.8+ și rulați:
   pip install opencv-contrib-python
   python generate_aruco.py
   -> se creează folderul "markers" cu aruco_00.png ... aruco_09.png
2) PRINT: tipăriți marker-ele (6–9 cm, cu margini albe).
3) RULARE WEBAR:
   - Deschideți "index.html" într-un server local (ex: cu Python):
       python -m http.server 8000
     apoi în browser accesați http://localhost:8000
   - Pe telefon, deschideți aceeași adresă în rețeaua locală sau încărcați tot folderul pe Netlify/GitHub Pages.
4) SCANARE: Apropiați marker-ul de cameră; apare cardul cu Întrebare. Apăsați pe buton pentru a vedea Răspunsul.

NOTĂ
- Dacă deschideți "index.html" direct din fișier fără server, unele browsere pot bloca încărcarea qna.json sau accesul la cameră.
- js-aruco (CDN) poate avea diferențe de comportament între telefoane; lumină bună ajută mult la detectare.
