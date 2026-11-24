number_of_rows = 4
seats_per_row = 5
# Write your code below

# 1. Buat denah kosong
seats = []
for baris in range(number_of_rows):
    baris_kursi = []
    for kolom in range(seats_per_row):
        baris_kursi.append(".")
    seats.append(baris_kursi)

jumlah_terisi= 0

# 2. Ulangi sampai pengguna mengetik baris 0
while True:
    for baris in range(number_of_rows):
        print(f"Row {baris + 1}:", " ".join(seats[baris]))

    nomor_baris = int(input("Row (0 to stop): "))
    if nomor_baris == 0:
        break

    nomor_kursi = int(input("Seat: "))

    # 3. Cek kursi
    if nomor_baris < 1 or nomor_baris > number_of_rows or nomor_kursi < 1 or nomor_kursi > seats_per_row:
        print("Invalid seat.")
    elif seats[nomor_baris - 1][nomor_kursi - 1] == "X":
        print("Seat already taken.")
    else:
        seats[nomor_baris - 1][nomor_kursi - 1] = "X"
        jumlah_terisi += 1
        print("Seat booked.")

# 4. Hasil akhir
print("Seats taken:", jumlah_terisi)