PASS_SCORE = 65

n = int(input("Number of students: "))
while n <= 0:
    print("Number of students must be greater than 0.")
    n = int(input("Number of students: "))
total = 0
passing_students = 0

for i in range(1, n + 1):
    print("Student", i)
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        score = int(input("Enter score: "))
    total += score
    if score >= PASS_SCORE:
        passing_students += 1
    if i == 1 :
        lowest_score = score
    else:
        if score < lowest_score:
            lowest_score = score


average = total / n
print("Total score:", total)
print("Number of passing students:", passing_students)
print("Lowest score:", lowest_score)
print("Average score:", average)