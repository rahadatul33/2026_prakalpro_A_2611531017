PASS_SCORE = 65

n = int(input("Number of students: "))
total = 0
passed = 0

for i in range(1, n + 1):
    print("Student", i)
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))
    total += score
    if score >= PASS_SCORE:
        passed += 1

average = total / n
print("Total score:", total)
print("Average score:", average)
print("Passed:", passed)