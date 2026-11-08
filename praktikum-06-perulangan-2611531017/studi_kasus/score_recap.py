PASS_SCORE = 65

n = int(input("Number of students: "))
while n <= 0:
    print("Invalid student count")
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
    if i == 1 :
        lowest_score = score
    else:
        if score < lowest_score:
            lowest_score = score


average = total / n
print("Total score:", total)
print("Average score:", average)
print("Passed:", passed)
print("Lowest score:", lowest_score)