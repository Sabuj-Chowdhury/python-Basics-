password = input("Password? :")

char_len= len(password)
# print(char_len)

if char_len<6:
    print("Weak")
elif char_len<11:
    print("Medium")
else:
    print("Strong")