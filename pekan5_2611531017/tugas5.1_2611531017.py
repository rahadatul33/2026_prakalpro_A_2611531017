# BUat file dengan nama tugas5_Nim.py
# Program segitiga bintang menggunakan perulangan for
# Program ini menggunakan fungsi input()

tinggi_1017 = int(input("Masukkan tinggi segitiga: "))

for i_1017 in range(1, tinggi_1017 + 1):
    # spasi di kiri supaya bentuknya rata tengah
    for j_1017 in range(tinggi_1017 - i_1017):
        print(" ", end="")
    # bintang, tiap bintang diikuti satu spasi
    for k_1017 in range(i_1017):
        print("*", end=" ")
    print()  # pindah ke baris berikutnya