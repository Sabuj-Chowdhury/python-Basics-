extra_shot = input("Do you want extra shot? (yes/no) ").lower()
coffee_order = input("Order size? ")

if extra_shot == 'yes':
    print(f"{coffee_order} coffee with extra shot!")
else:
    print(f"{coffee_order} coffee with no extra shot!")