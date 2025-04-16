# Perkalian Matriks 5×5

## Deskripsi
Kode ini mendemonstrasikan perkalian matriks 5x5 dalam Python. Program mengalikan dua matriks (A dan B) dan menampilkan hasil perkaliannya.

## Matriks yang Digunakan
### Matriks A
```
[
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
```

### Matriks B
```
[
    [26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45],
    [46, 47, 48, 49, 50]
]
```

## Cara Kerja
1. Program menginisialisasi dua matriks 5x5 (A dan B)
2. Membuat matriks hasil (result) dengan ukuran 5x5
3. Melakukan perkalian matriks dengan tiga loop bersarang:
   - Loop pertama (`i`) untuk baris matriks A
   - Loop kedua (`j`) untuk kolom matriks B
   - Loop ketiga (`k`) untuk menghitung dot product antara baris A dan kolom B
4. Setiap elemen hasil dihitung dengan rumus: 
   `result[i][j] = Σ(A[i][k] * B[k][j])` untuk k dari 0 sampai 4
5. Hasil perkalian matriks ditampilkan ke layar

## Output
Program akan menampilkan matriks hasil perkalian dengan format:
```
Hasil perkalian matriks: 
[baris 1]
[baris 2]
...
[baris 5]
```

## Cara Menjalankan
1. Pastikan Python terinstal di sistem Anda
2. Simpan kode dalam file dengan ekstensi .py (misalnya: matrix_multiplication.py)
3. Jalankan di terminal/command prompt dengan perintah: `python matrix_multiplication.py`

## Catatan
- Program ini khusus untuk matriks berukuran 5x5
- Untuk matriks dengan ukuran berbeda, perlu mengubah nilai dalam loop dan definisi matriks
