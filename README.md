# UTS Computer Vision
## Nama : Muhammad Panca Prasetya
## NIM : 43050230001

---

## Deskripsi Karakter
**Orbi (Orange Binary)** adalah karakter kucing berwarna **oranye cerah** dengan mata hitam dan hidung merah muda gelap.  
Nama **Orbi** berasal dari singkatan **Orange Binary**, melambangkan kucing digital yang hidup di dunia komputer.  
Orbi dibuat menggunakan pustaka **OpenCV** dan **NumPy**, digambar dari bentuk dasar seperti **lingkaran**, **segitiga (polygon)**, dan **garis**.

---

## Transformasi yang Diterapkan
Program ini menampilkan berbagai **operasi transformasi geometrik dan bitwise** pada gambar karakter Orbi:

### Transformasi Geometrik:
1. **Translasi** → Menggeser posisi kucing ke kanan dan bawah.  
2. **Rotasi** → Memutar kucing sebesar 50 derajat.  
3. **Resize** → Mengubah ukuran gambar menjadi lebih kecil.  
4. **Crop** → Mengambil sebagian wajah tengah Orbi.

### Operasi Aritmatika:
- `cv2.add()` → Menambah kecerahan gambar.  
- `cv2.subtract()` → Mengurangi kecerahan gambar.

### Operasi Bitwise:
1. **cv2.bitwise_and()** → Menampilkan bagian kucing saja menggunakan mask.  
2. **cv2.bitwise_or()** → Menggabungkan kucing dengan background.  
3. **cv2.bitwise_not()** → Membuat efek negatif (invers warna) pada kucing.

---

## Screenshot Hasil Akhir
Berikut contoh hasil akhir gabungan karakter Orbi dan background (`bitwise_or.png`):
<img width="500" height="500" alt="bitwise_or" src="https://github.com/user-attachments/assets/c316f2d7-8ec5-4e5c-9070-16bcecdef419" />
