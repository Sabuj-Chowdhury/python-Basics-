#  Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# Get user input for age
age = int (input("enter your age: "))
# Check the age group and print the corresponding message
if age <13:
    print("you are a child")
elif age >= 13 and age <= 19:
    print("you are a teenager")
elif age >= 20 and age <= 59:
    print("you are an adult")
elif age >= 60:
    print("you are a senior")
else:
    print("invalid age")
