# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int (input("Enter your Score: "))


if score>=90 and score <=100:
    print("A")
elif score>=80 and score <=89:
    print("B")
elif score >=70 and score <=79:
    print("C")
elif score >=60 and score <=69:
    print("D")
elif score<60:
    print("F")
else:
    print("Invalid Score")