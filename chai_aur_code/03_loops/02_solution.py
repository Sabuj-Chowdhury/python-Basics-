# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int (input("n : "))

sum = 0

for i in range(1,n+1):
    if i % 2 == 0:
        sum +=i
  
#printing the sum of positive numbers        
print(sum)