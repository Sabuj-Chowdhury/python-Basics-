pet = input("Pet's species : ").lower()
age = int (input("Age : "))
if (pet == 'cat'):
    if age <2:
        print("Puppy food")
    else:
        print(f"Senior {pet} food")

if(pet == 'dog'):
    if age <2:
        print("Puppy food")
    else:
        print(f"Senior {pet} food")