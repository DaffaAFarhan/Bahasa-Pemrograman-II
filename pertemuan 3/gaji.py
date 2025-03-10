nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status: ").lower()
gol = input("Masukkan Golongan: ").lower()

gaji = 0
bonus = 0

if status == "tetap" or status == "pegawai tetap":
    gaji = 1000000
    if gol == "a":
        bonus = 200000
    elif gol == "b":
        bonus = 400000
    elif gol == "c":
        bonus = 550000
    else:
        print("Golongan tidak valid!")
elif status == "honorer" or status == "honor":
    gaji = 750000
    if gol == "a":
        bonus = 150000
    elif gol == "b":
        bonus = 275000
    elif gol == "c":
        bonus = 480000
    else:
        print("Golongan tidak valid!")
else:
    print("Status tidak valid!")

if gaji > 0 and bonus > 0:
    total = gaji + bonus
    print("=== DATA KARYAWAN ===")
    print("Nama :", nama)
    print("Nik :", nik)
    print("Gaji :", gaji)
    print("Bonus :", bonus)
    print("Total Gaji :", total)
else:
    print("Tidak Dapat Menampilkan Gaji Anda")
