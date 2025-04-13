num = int(input("number : "))
fact = 1


while num>0:
    # fact=fact *num
    # num= num-1
    fact *=num
    num -=1

print(f"factorial is {fact}")