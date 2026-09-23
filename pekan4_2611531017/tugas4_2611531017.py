# =========================================================
# Program: Sistem Loket Terpadu & Audit Transaksi
#          Ekspedisi Wahana - Alpro Adventure Park
# Materi : if, if-else, if-elif-else, multi-if, match-case
# Semua variabel diakhiri NIM: 1017
# =========================================================

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# ---------------------------------------------------------
# 1. Input Data Pengunjung
# ---------------------------------------------------------
nama_1017 = input("Masukkan Nama Pengunjung        : ")
umur_1017 = int(input("Input umur anda                 : "))
sim_1017 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]

# ---------------------------------------------------------
# 2. Pemilihan Wahana Menggunakan Match-Case
# ---------------------------------------------------------
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")
paket_1017 = int(input("Masukkan nomor paket (1-5)      : "))

match paket_1017:
    case 1:
        nama_wahana_1017 = "Wahana Safari Rimba"
        harga_satuan_1017 = 50000
    case 2:
        nama_wahana_1017 = "Wahana Arung Jeram"
        harga_satuan_1017 = 75000
    case 3:
        nama_wahana_1017 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1017 = 120000
    case 4:
        nama_wahana_1017 = "Wahana Roller Coaster Kilat"
        harga_satuan_1017 = 100000
    case 5:
        nama_wahana_1017 = "Wahana All-Access VIP"
        harga_satuan_1017 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

# ---------------------------------------------------------
# 3. Input Jumlah Tiket & Member/Promo
# ---------------------------------------------------------
jumlah_tiket_1017 = int(input("Masukkan jumlah tiket           : "))

# --- If tunggal: validasi kelogisan jumlah tiket ---
if jumlah_tiket_1017 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

is_member_1017 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_1017 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# ---------------------------------------------------------
# 4. Validasi Izin Kendali Wahana (If-Elif-Else + Operator Logika)
# ---------------------------------------------------------
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_1017 == 3:
    if umur_1017 >= 17 and sim_1017 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_1017 >= 17 and sim_1017 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_1017 < 17 and sim_1017 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_1017 >= 10:
        print("Status Akses: Anda diperbolehkan menaiki wahana ini.")
    else:
        print("Status Akses: Anda belum cukup umur untuk menaiki wahana ini.")

# ---------------------------------------------------------
# 5. Akumulasi Diskon Bertingkat (Multi-If Terpisah)
# ---------------------------------------------------------
subtotal_1017 = harga_satuan_1017 * jumlah_tiket_1017
total_diskon_persen_1017 = 0

if subtotal_1017 >= 200000:
    total_diskon_persen_1017 += 10  # Diskon Belanja Besar

if is_member_1017 in ['y', 'ya']:
    total_diskon_persen_1017 += 5   # Diskon Member

if kode_promo_valid_1017 in ['y', 'ya']:
    total_diskon_persen_1017 += 15  # Diskon Voucher Promo

if jumlah_tiket_1017 >= 5:
    total_diskon_persen_1017 += 5   # Diskon Tambahan Rombongan

# ---------------------------------------------------------
# 6. Evaluasi Kelulusan Audit (If-Else)
# ---------------------------------------------------------
nominal_diskon_1017 = subtotal_1017 * (total_diskon_persen_1017 / 100)
total_bayar_1017 = subtotal_1017 - nominal_diskon_1017

if total_bayar_1017 > 300000:
    catatan_layanan_1017 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
    
# ---------------------------------------------------------
# 7. Cetak Rincian Pembayaran
# ---------------------------------------------------------
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_1017:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_1017}% (Rp {nominal_diskon_1017:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_1017:,.0f}")
if total_bayar_1017 > 300000:
    print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
print(" Catatan Layanan  : Terima Kasih Telah Berkunjung")
print("Program Selesai")