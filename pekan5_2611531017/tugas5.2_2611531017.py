# Buat file dengan nama tugas5_nim.py
# Program Jam Pasir Kristal Palindromik Berbingkai menggunakan for bersarang
# Nama variabel ditambah 4 digit nim terakhir contoh: n_1234
# Program ini menggunakan fungsi input()

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_1017 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Bingkai atas
print("#", end="")
for garis_1017 in range(4 * n_1017 + 5):
    print("=", end="")
print("#", end="")
print()

# Fase 1: jam pasir atas (baris N turun sampai 1)
for i_1017 in range(1, n_1017 + 1):
    baris_1017 = n_1017 - i_1017 + 1
    print("|", end="")
    print(" ", end="")
    for kiri_1017 in range(2 * (n_1017 - baris_1017)):
        print(" ", end="")
    for mundur_1017 in range(1, baris_1017 + 1):
        print(baris_1017 - mundur_1017 + 1, end="")
        print(" ", end="")
    print("<*>", end="")
    for maju_1017 in range(1, baris_1017 + 1):
        print(" ", end="")
        print(maju_1017, end="")
    for kanan_1017 in range(2 * (n_1017 - baris_1017)):
        print(" ", end="")
    print(" ", end="")
    print("|", end="")
    print()

# Fase 2: poros titik pusat
print("|", end="")
for kiri_1017 in range(2 * n_1017 + 1):
    print(" ", end="")
print("<*>", end="")
for kanan_1017 in range(2 * n_1017 + 1):
    print(" ", end="")
print("|", end="")
print()

# Fase 3: jam pasir bawah (baris 1 naik sampai N)
for baris_1017 in range(1, n_1017 + 1):
    print("|", end="")
    print(" ", end="")
    for kiri_1017 in range(2 * (n_1017 - baris_1017)):
        print(" ", end="")
    for mundur_1017 in range(1, baris_1017 + 1):
        print(baris_1017 - mundur_1017 + 1, end="")
        print(" ", end="")
    print("<*>", end="")
    for maju_1017 in range(1, baris_1017 + 1):
        print(" ", end="")
        print(maju_1017, end="")
    for kanan_1017 in range(2 * (n_1017 - baris_1017)):
        print(" ", end="")
    print(" ", end="")
    print("|", end="")
    print()

# Bingkai bawah
print("#", end="")
for garis_1017 in range(4 * n_1017 + 5):
    print("=", end="")
print("#", end="")
print()
