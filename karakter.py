import cv2
import numpy as np
import os

# Buat folder output
os.makedirs("output", exist_ok=True)

# Buat Karaker
# Buat kanvas
canvas = np.full((500, 500, 3), 255, dtype = np.uint8)

# WArna
orange = (0, 140, 255)
red = (60, 60, 200)
black = (0, 0, 0)

# Titik pusat kepala
cx, cy = 250, 260
radius = 100

# Telinga kiri
ear_left = np.array([[cx - 80, cy - 60], [cx - 40, cy -150], [cx - 10, cy - 60]], np.int32)
cv2.fillPoly(canvas, [ear_left], orange)
cv2.polylines(canvas, [ear_left], True, black, 1) # Outline

# Telinga kanan
ear_left = np.array([[cx + 80, cy - 60], [cx + 40, cy -150], [cx + 10, cy - 60]], np.int32)
cv2.fillPoly(canvas, [ear_left], orange)
cv2.polylines(canvas, [ear_left], True, black, 1) # Outline

# Kepala
cv2.circle(canvas, (cx, cy), radius, orange, -1)
cv2.circle(canvas, (cx, cy), radius, black, 1) # outline

# Mata
cv2.circle(canvas, (cx - 40, cy - 20), 12, black, -1)
cv2.circle(canvas, (cx + 40, cy - 20), 12, black, -1)

# Hidung
cv2.circle(canvas, (cx, cy + 10), 8, red, -1)
cv2.circle(canvas, (cx, cy + 10), 8, black, 1) # Outline

# Mulut
cv2.line(canvas, (cx, cy + 18), (cx - 15, cy + 35), black, 1)
cv2.line(canvas, (cx, cy + 18), (cx + 15, cy + 35), black, 1)

# Kumis Kiri
cv2.line(canvas, (cx - 30, cy + 15), (cx - 85, cy + 5), black, 1)
cv2.line(canvas, (cx - 30, cy + 20), (cx - 85, cy + 20), black, 1)
cv2.line(canvas, (cx - 30, cy + 25), (cx - 85, cy + 35), black, 1)

# Kumis Kanan
cv2.line(canvas, (cx + 30, cy + 15), (cx + 85, cy + 5), black, 1)
cv2.line(canvas, (cx + 30, cy + 20), (cx + 85, cy + 20), black, 1)
cv2.line(canvas, (cx + 30, cy + 25), (cx + 85, cy + 35), black, 1)

cv2.imwrite("output/karakter.png", canvas)

# TRANSFORMASI
# Translasi
rows, cols = canvas.shape[:2]
M_translate = np.float32([[1, 0, 80], [0, 1, 50]]) # Geser 80 kanan 50 bawah
translated = cv2.warpAffine(canvas, M_translate, (cols, rows))
cv2.imwrite("output/translate.png", translated)

# Rotasi
M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), 50, 1) # Pusat rotasi di tengah, 50 derajat
rotated = cv2.warpAffine(canvas, M_rotate, (cols, rows))
cv2.imwrite("output/rotate.png", rotated)

# Resize
resized = cv2.resize(canvas, (200, 200)) # Mengecilkan ukuran
cv2.imwrite("output/resize.png", resized)

# Cropped
cropped = canvas[120:280, 120:280] # Ambil sebagian wajah tengah
cv2.imwrite("output/crop.png", cropped)

# Bitwise & aritmatika
# Baca background
background = cv2.imread("img/background.jpg")

# resize background
background = cv2.resize(background, (500, 500))

# cv2.add (Tambah kecerahan)
add_result = cv2.add(canvas, (50, 50, 50, 0))
cv2.imwrite("output/add.png", add_result)

# cv2.subtract (Kurangi kecerahan)
sub_result = cv2.subtract(canvas, (50, 50, 50, 0))
cv2.imwrite("output/sub.png", sub_result)

# Buat mask dengan threshold untuk deteksi bentuk kucing
gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Inverse mask
mask_inv = cv2.bitwise_not(mask)

# AND
bitwise_and = cv2.bitwise_and(canvas, canvas, mask=mask) # Ambil area kucing saja
bg_part = cv2.bitwise_and(background, background, mask=mask_inv) # Ambil background yang tidak tertutup kucing
cv2.imwrite("output/bitwise_and.png", bitwise_and)

# OR -> gabungkan kucing dan background
bitwise_or = cv2.bitwise_or(bitwise_and, bg_part)
cv2.imwrite("output/bitwise_or.png", bitwise_or)

# NOT -> efek negatif kucing
bitwise_not = cv2.bitwise_not(canvas)
cv2.imwrite("output/bitwise_not.png", bitwise_not)


# tanpilan semua hasil
cv2.imshow("Kucing", canvas)
cv2.imshow("Translate", translated)
cv2.imshow("Rotate", rotated)
cv2.imshow("Resize", resized)
cv2.imshow("Crop", cropped)
cv2.imshow("Add", add_result)
cv2.imshow("Sub", sub_result)
cv2.imshow("Bitwise And", bitwise_and)
cv2.imshow("Bitwise Or", bitwise_or)
cv2.imshow("Bitwise Not", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()