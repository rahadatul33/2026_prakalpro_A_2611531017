# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1017 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_1017 = [int(angka.strip()) for angka in input_data_1017.split(",")]

nilai_dicari_1017 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1017 = nilai_dicari_1017 in data_1017
print("\nOperator keanggotaan IN")
print(nilai_dicari_1017, "in", data_1017, "=", hasil_1017)

# Operator not in
hasil_1017 = nilai_dicari_1017 not in data_1017
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1017, "not in", data_1017, "=", hasil_1017)


print("\n========================================")
print("2. OPERATOR IDENTITAS")
print("========================================")

# objek1 menggunakan list dari input pengguna
objek1_1017 = data_1017

# objek2 merujuk pada objek yang sama dengan objek1
objek2_1017 = objek1_1017

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1017 = data_1017.copy()

print("objek1 =", objek1_1017)
print("objek2 =", objek2_1017)
print("objek3 =", objek3_1017)

# Operator is
hasil_1017 = objek1_1017 is objek2_1017
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_1017)

# Operator is not
hasil_1017 = objek1_1017 is not objek3_1017
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_1017)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_1017 is objek3_1017)
print("objek1 == objek3 =", objek1_1017 == objek3_1017)