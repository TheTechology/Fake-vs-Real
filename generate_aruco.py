# generate_aruco.py
# Generează 10 markere ArUco (ID 0..9) în folderul "markers".
# Necesită: pip install opencv-contrib-python
import os, cv2
aruco = cv2.aruco
dictionary = aruco.Dictionary_get(aruco.DICT_4X4_50)
size = 800  # px, potrivit pentru print A4 (poți micșora în print)
outdir = "markers"
os.makedirs(outdir, exist_ok=True)
for i in range(10):
    marker = aruco.drawMarker(dictionary, i, size)
    path = os.path.join(outdir, f"aruco_{i:02d}.png")
    cv2.imwrite(path, marker)
    print("Salvat:", path)
print("Gata. Tipărește imaginile cu margine albă (quiet zone) ~5-8 mm.")
