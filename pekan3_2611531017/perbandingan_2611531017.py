# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_1017 = int(input("Input angka-1: "))
angka2_1017 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_1017 = angka1_1017 > angka2_1017
print("\nOperator lebih besar dari")
print("angka1_1017 > angka2_1017", hasil_1017)

# Lebih kecil dari
hasil_1017 = angka1_1017 < angka2_1017
print("\nOperator lebih kecil dari")
print("angka1_1017 < angka2_1017", hasil_1017)

# Lebih besar dari atau sama dengan
hasil_1017 = angka1_1017 >= angka2_1017
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_1017 >= angka2_1017", hasil_1017)

# Lebih kecil dari atau sama dengan
hasil_1017 = angka1_1017 <= angka2_1017
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_1017 <= angka2_1017 = ", hasil_1017)

# Sama dengan
hasil_1017 = angka1_1017 == angka2_1017
print("\nOperator sama dengan")
print("angka1_1017 == angka2_1017 =", hasil_1017)

# Tidak sama dengan
hasil_1017 = angka1_1017 != angka2_1017
print("\nOperator tidak sama dengan")
print("angka1_1017 != angka2_1017 =", hasil_1017)

# Tambahan: perbandingan berantai dalam Python
hasil_1017 = 0 < angka1_1017 < 100
print("\nPerbandingan berantai")
print("0 < angka1_1017 < 100 =", hasil_1017)

hasil_1017 = 0 < angka2_1017 < 100
print("0 < angka2_1017 < 100 =", hasil_1017)