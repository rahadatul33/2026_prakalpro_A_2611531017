PASS_SCORE = 65

n = int(input("Number of students: "))
total = 0
passed = 0

for i in range(1, n + 1):
    print("Student", i)
    score = int(input("Enter score: "))
    total += score

average = total / n
print("Total score:", total)
print("Average score:", average)