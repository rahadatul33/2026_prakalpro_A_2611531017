print("=== SISTEM TRANSAKSI TOKO ===")

nama_pelanggan_1017 = input("Masukkan Nama Pelanggan : ")
status_pelanggan_1017 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_1017 = int(input("Masukkan Total Belanja : "))
jumlah_barang_1017 = int(input("Masukkan Jumlah Barang : "))
promo_1017 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan                      : ", nama_pelanggan_1017)
print("Status Pelanggan (member/nonmember) : ", status_pelanggan_1017)
print("Total Belanja                       : RP ", total_belanja_1017)
print("Jumlah Barang                       : ", jumlah_barang_1017)
print("Kode Promo                          : ", promo_1017)

kode_promo_1017 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {total_belanja_1017 >= 200000}")
print(f"Jumlah Barang >= 3         : {jumlah_barang_1017 >= 3}")
print(f"Status Member              : {status_pelanggan_1017 == 'member'}")
print(f"Kode Promo Tersedia        : {promo_1017 in kode_promo_1017}")
print(f"Mendapatkan Diskon         : {jumlah_barang_1017 >= 3 or total_belanja_1017 >= 200000}")
print(f"Mendapatkan Promo          : {promo_1017 in kode_promo_1017}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                     : RP{0.07 * total_belanja_1017}")
print(f"Total Pembayaran           : RP{total_belanja_1017 - 0.07 * total_belanja_1017}")
print(f"Rata-rata Harga Barang     : RP{(total_belanja_1017 - 0.07 * total_belanja_1017) / jumlah_barang_1017}")

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses                         : ...")
print(f"Member Access                          : {status_pelanggan_1017 == 'member'}")
print(f"Promo Access                           : {promo_1017 in kode_promo_1017}")
print("Free Shipping Access                   : ...")

print("\n=== OPERASI BITWISE ===")
print("\n=== Kode Status Transaksi ===")
print(f"{format(int(status_pelanggan_1017 == 'member'), '04b')} | {format(int(total_belanja_1017 >= 200000) << 1, '04b')} | {format(int(jumlah_barang_1017 >= 3) << 2, '04b')} | {format(int(promo_1017 in kode_promo_1017) << 3, '04b')}")
print(f"Kode Biner : {format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3, '04b')}")
print(f"Kode Desimal : {int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3, '04b')} & {format(int(status_pelanggan_1017 == 'member') << 0, '04b')}")
print(f"Hasil Biner   : {format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3 & int(status_pelanggan_1017 == 'member') << 0, '04b')}")
print(f"Hasil Desimal : {int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3 & int(status_pelanggan_1017 == 'member') << 0}")

print("Cek Promo")
print(f"{format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3, '04b')} & {format(int(promo_1017 in kode_promo_1017) << 3, '04b')}")
print(f"Hasil Biner   : {format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3 & int(promo_1017 in kode_promo_1017) << 3, '04b')}")
print(f"Hasil Desimal : {int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3 & int(promo_1017 in kode_promo_1017) << 3}")

print("\n=== Perbandingan Status ===")
print(f"Kode transaksi : {format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3, '04b')}")
print("Kode Referensi : 1011")
print(f"{format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3, '04b')} ^ 1011 ")
print(f"Hasil Biner   : {format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3 ^ 1011, '04b')}")
print(f"Hasil Desimal : {int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3 ^ 1011}")

print("\n=== Shift ===")
print(f"{format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3, '04b')} << 1 ")
print(f"Hasil Biner   : {format(int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3 << 1, '04b')}")
print(f"Hasil Desimal : {int(status_pelanggan_1017 == 'member') << 0 | int(total_belanja_1017 >= 200000) << 1 | int(jumlah_barang_1017 >= 3) << 2 | int(promo_1017 in kode_promo_1017) << 3 << 1}")

print("\n=== SELESAI ===")