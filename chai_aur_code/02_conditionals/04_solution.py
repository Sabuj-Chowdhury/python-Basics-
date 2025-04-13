# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Fruit: ").lower()
color = input("Green, Yellow or Brown :").lower()


if (color == 'green'):
    print(f"{fruit}: Unripe")
elif (color == 'yellow'):
    print(f"{fruit}: Ripe")
else:
    print(f"{fruit}: Overripe")