# Buat file dengan nama if2_nim.py
# Buat progam untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Progam ini menggunakan fungsi input()

ipk_1017 = float(input("Masukkan IPK : "))

if ipk_1017 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str(ipk_1017))

else:
    print("Anda Tidak Lulus")
print("Program Selesai")