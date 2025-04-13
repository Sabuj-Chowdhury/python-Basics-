string = input("String: ")

for char in string:
    if string.count(char) == 1:
        print(f"non-repeated char is {char}")
        break