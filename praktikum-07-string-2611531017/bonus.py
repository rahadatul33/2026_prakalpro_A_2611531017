# Name: Rahadatul Aisha Tetriana Putri
# NIM: 2611531017
# Question bonus

kalimat = input("Masukkan kalimat: ")

bersih = kalimat.lower().replace(" ", "")
terbalik = bersih[::-1]

if bersih == terbalik:
    print("Palindrome")
else:
    print("Not a palindrome")