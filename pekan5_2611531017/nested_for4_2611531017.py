# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_1017 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1017 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1017 = tinggi_1017
    c_1017 = a_1017
    lebar_1017 = (2 * tinggi_1017) - 2

    for i_1017 in range(1, tinggi_1017 + 1):
        b_1017 = c_1017 + 1

        for j_1017 in range(1, lebar_1017 + 1):

            # Baris atas dan bawah
            if i_1017 == 1 or i_1017 == tinggi_1017:
                if j_1017 == 1 or j_1017 == lebar_1017:
                    print("#", end="")
                else:
                    print("=", end="")

                    # Baris isi
            else:
                if j_1017 == 1 or j_1017 == lebar_1017:
                    print("|", end="")
                else:
                    if j_1017 == c_1017:
                        print("<", end="")
                    elif j_1017 == b_1017:
                        print(">", end="")
                    elif j_1017 == (lebar_1017 - c_1017):
                        print("<", end="")
                    elif j_1017 == (lebar_1017 - c_1017 + 1):
                        print(">", end="")
                    elif j_1017 > b_1017 and j_1017 < (lebar_1017 - c_1017):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_1017 -= 2

        if a_1017 <= 0:
            c_1017 = (-a_1017) + 2
        else:
            c_1017 = a_1017