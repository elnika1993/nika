# davaleba 2
a = int(input("Enter number "))
if a < 5:
    print("Please enter number higher then 5")
elif a > 50:
    print("Please enter number lower then 50")
while 5 <= a <= 50:
    a = a + 3
    if a == 12:
        print("ar davbechdav")
        continue
    if a == 51 or a == 52 or a == 53:
        continue
    print(a)
