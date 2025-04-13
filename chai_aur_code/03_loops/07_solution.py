# number = int (input("Number : "))

while True:
    number = int (input("Number between 1 and 10 : "))
    if 1<=number<=10:
        print("Thanks!")
        break
    else:
        print("Invalid Number")