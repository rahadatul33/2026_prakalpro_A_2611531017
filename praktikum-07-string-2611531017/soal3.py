# Name: Rahadatul Aisha Tetriana Putri
# NIM: 2611531017
# Question 3

# Bagian A
text = "Informatika"
print(text[10])
print(text.upper())
print(text)

# Bagian B
text = "Rahadatul Aisha Tetriana Putri"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)

