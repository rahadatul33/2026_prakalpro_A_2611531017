# Buat file dengan nama Konstanta_1017.py
# Progam ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1017

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_1017 = float(input('Masukan nilai jari-jari:'))
luas_1017 = PI * jari_1017 * jari_1017
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1017, luas_1017))