# deklarasi variabel dengan tipe data Boolean
is_lulus_1017 = True
is_cumlaude_1017 = True

# Menggunakan Boolean
nilai_1017 = 85
batas_lulus_1017 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_1017= nilai_1017 >= batas_lulus_1017 # Hasilnya akan True

print("=== Check Kelulusan===")
print("Nilai:", nilai_1017)
print("Apakah Lulus?", status_kelulusan_1017)
if is_lulus_1017 and is_cumlaude_1017:
    print("Selamat, Anda lulus dengan predikat Cum Laude! ")