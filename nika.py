print("Hello")
usd = 3.1   # official exchange rate for USD: 3.1
euro = 3.5  # official exchange rate for EURO: 3.5
lari = float(input("Please enter amount you want to exchange: "))
answer = float(input("Please enter unique code: 1 for usd; 2 for euro: "))
if answer == 1 and lari == 300:
    print("Not my fault.")
elif answer == 2 and lari == 350:
    print("Also not my fault.")
elif answer == 1:
    print(lari * usd)
elif answer == 2:
    print(lari * euro)
else:
    print("This is error.")
