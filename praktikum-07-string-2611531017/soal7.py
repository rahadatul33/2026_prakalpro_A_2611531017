# Name: Rahadatul Aisha Tetriana Putri
# NIM: 2611531017
# Question 7

name = "rahadatul aisha tetriana putri"
nim = "2611531017"

username = name.split()[0] + nim[-3:]
intake = "20" + nim[:2]
lebar_kartu = 30
garis = "=" * lebar_kartu

print(garis)
print("STUDENT CARD".center(lebar_kartu))
print(garis)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print(garis)
