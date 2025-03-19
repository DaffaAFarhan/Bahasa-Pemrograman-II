nama = input("Nama karyawan: ")
nik = input("NIK karyawan: ")
statuskar = input("Status: ").lower()
golkar = input("Golongan: ").lower()

status = ["tetap", "honor"]
gol = ["a", "b", "c"]

if statuskar == "tetap" or statuskar == "pegawai tetap":
    gaji = 1000000
    if golkar == "a":
        bonus = 200000
    elif golkar == "b":
        bonus = 400000
    elif golkar == "c":
        bonus = 550000
    else:
        print("Golongan tidak valid!")
        bonus = 0
    total = gaji + bonus

elif statuskar == "honor" or statuskar == "honorer":
    gaji = 750000
    if golkar == "a":
        bonus = 150000
    elif golkar == "b":
        bonus = 275000
    elif golkar == "c":
        bonus = 480000
    else:
        print("Golongan tidak valid!")
        bonus = 0
    total = gaji + bonus

else:
    print("Status tidak valid!")
    gaji = 0
    bonus = 0
    total = 0

print("\n=== DATA KARYAWAN ===")
print("Nama        :", nama)
print("NIK         :", nik)
print("Status      :", statuskar)
print("Golongan    :", golkar)
print("Gaji        :", gaji)
print("Bonus       :", bonus)
print("Total Gaji  :", total)
