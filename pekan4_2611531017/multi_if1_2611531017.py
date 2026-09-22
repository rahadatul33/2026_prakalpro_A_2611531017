# Buat file dengan nama multi_if1.py
# Buat progam untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Progam ini menggunakan fungsi input()

umur_1017 = int(input("Input umur anda : "))
sim_1017 = input("Apakah Anda Sudah Punya Sim C (y/t) : ") [0]

if umur_1017 >= 17  and sim_1017 == 'y':
    print("Anda Sudah Dewasa dan boleh bawa motor")

if umur_1017 >= 17 and sim_1017 != 'y':
    print("Anda Sudah Dewasa tetapi tidak boleh bawa motor")

if umur_1017 < 17 and sim_1017 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_1017 < 17 and sim_1017 != 'y':
    print("Anda Belum Cukup Umur bawa motor")