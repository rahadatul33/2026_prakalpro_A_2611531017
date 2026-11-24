menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

# 1. Membaca data penjualan (nested loop)
for hari in range(1, number_of_days + 1):
    penjualan_hari_ini = []                      # list baru untuk satu hari
    for nama_menu in menus:
        jumlah_porsi = int(input(f"Day {hari}, {nama_menu}: "))
        penjualan_hari_ini.append(jumlah_porsi)  # simpan ke list hari ini
    sales.append(penjualan_hari_ini)             # simpan satu hari ke sales

# 2. Total porsi setiap hari 
print("Total per day:")
for baris in range(len(sales)):
    total_hari = 0
    for kolom in range(len(sales[baris])):
        total_hari += sales[baris][kolom]
    print(f"Day {baris + 1}: {total_hari}")

# 3. Total setiap menu 
menu_totals = []
for kolom in range(len(menus)):
    total_menu = 0
    for baris in range(len(sales)):
        total_menu += sales[baris][kolom]
    menu_totals.append((menus[kolom], total_menu))
print("Total per menu:", menu_totals)

# 4. Mencari menu terlaris
menu_terlaris = menu_totals[0][0]
porsi_terlaris = menu_totals[0][1]
for name, total in menu_totals:
    if total > porsi_terlaris:
        menu_terlaris = name
        porsi_terlaris = total
print(f"Best seller: {menu_terlaris} ({porsi_terlaris})")