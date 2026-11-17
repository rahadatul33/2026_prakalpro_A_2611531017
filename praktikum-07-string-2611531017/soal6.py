# Name: Rahadatul Aisha Tetriana Putri
# NIM: 2611531017
# Question 6

# Soal pemanasan
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# soal 6
full_name = input("name: ")
NIM = input("NIM: ")

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().

clean = full_name.strip() + " " + NIM [-3:]
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + NIM[-3:]
print(username)