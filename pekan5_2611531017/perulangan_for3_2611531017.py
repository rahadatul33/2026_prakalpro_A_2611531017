# Buat file dengan nama perulangan_for3_NIM.py
# Buat progam untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Progam ini menggunakan fungsi input()

ulang_1017 = int(input("Masukkan jumlah perulangan: "))

jumlah_1017 = 0
for i_1017 in range(1, ulang_1017 + 1):
    print(i_1017, end=" ")
    jumlah_1017 = jumlah_1017 + i_1017

    if i_1017 < ulang_1017:
        print(" + ", end="")
    else:
        print(" = ", jumlah_1017, end="")
print()
print("Jumlah =", jumlah_1017)