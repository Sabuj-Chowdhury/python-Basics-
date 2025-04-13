# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children.
# Everyone gets a $2 discount on Wednesday.

age = int (input("Enter your age: "))
price = 8 if age<18 else 12
day = input("day? :").lower()
# print(day)


if day == 'wednesday' :
    print(f"Ticket:${price -2}")
else:
    print(f"Ticket:${price}")