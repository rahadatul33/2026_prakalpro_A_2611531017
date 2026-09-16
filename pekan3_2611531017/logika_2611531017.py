# Buat nama file dengan nama logika_NIM
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1017 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_1017 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1_1017 =", a1_1017)
print("A2_1017 =", a2_1017)

# Konjungsi: bernilai True jika keduanya True
hasil_1017 = a1_1017 and a2_1017
print("\nKonjungsi (AND)")
print("A1_1017 and A2_1017 =", hasil_1017)

# Disjungsi: bernilai True jika salah satunya True
hasil_1017 = a1_1017 or a2_1017
print("\nDisjungsi (OR)")
print("A1_1017 or A2_1017 =", hasil_1017)

# Negasi A1: membalik nilai A1
hasil_1017 = not a1_1017
print("\nNegasi A1 (NOT)")
print("not A1_1017 =", hasil_1017)

# Negasi A2: membalik nilai A2
hasil_1017 = not a2_1017
print("\nNegasi A2 (NOT)")
print("not A2_1017 =", hasil_1017)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1017 = a1_1017 != a2_1017
print("\nDisjungsi Eksklusif (XOR)")
print("A1_1017 XOR A2_1017 =", hasil_1017)