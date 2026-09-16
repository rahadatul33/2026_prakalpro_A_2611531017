print ("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_1017 = input(str("Masukkan Nama Mahasiswa : "))
jenis_kelamin_1017 = input ("Masukkan Jenis Kelamin (L/P) : ")
umur_1017 = int(input("Masukkan Umur : "))
skor_tes_awal_1017 = float(input("Masukkan Skor Tes Awal : "))

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

alamat_1017 = """
Komplek Pekanbaru,
Kec. Sukajadi,
Kota Pekanbaru """
id_token_sinyal = 100+3j

print("Nama Mahasiswa :", nama_1017, "|", "Tipe :", type(nama_1017))
print("Jenis Kelamin :", jenis_kelamin_1017, "|", "Tipe :", type(jenis_kelamin_1017))
print("Alamat Domisili :", alamat_1017, "|", "Tipe :", type(alamat_1017))
print("Umur :", umur_1017, "tahun", "|", "Tipe :", type(umur_1017))
print("Skor Tes Awal :", skor_tes_awal_1017, "|", "Tipe :", type (skor_tes_awal_1017))
print("ID Token Sinyal :", id_token_sinyal, "|", "Tipe :", type (id_token_sinyal))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

batas_1017 = 75.0

print("Batas Minimum Nilai:", batas_1017)
if skor_tes_awal_1017 >= batas_1017:
    hasil_1017 = True
else:
    hasil_1017 = False
print("Apakah dinyatakan lulus?:", hasil_1017, "|", "Tipe :", type (hasil_1017))