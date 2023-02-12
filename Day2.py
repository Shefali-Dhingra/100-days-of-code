print("Tip Calculator!")

bill = float(input("Enter Total bill amount: "))

tip = float(input("Enter Tip Percentage: "))

p = int(input("Enter no. of people to split the bill: "))

print(f'Each Person should pay: {round((bill + (tip*bill) / 100 ),2) / p }')
