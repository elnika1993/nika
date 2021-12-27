n = int(input("Enter number: "))
sum = 0

for i in range(1, n+1):
     factorial = 1
     for b in range(1, i + 1):
         factorial = factorial * b
     sum = sum + factorial
print(sum)
