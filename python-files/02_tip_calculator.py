print("Welcome to the tip calculator!")

total = float(input("What was the total bill?\n"))
people = int(input("How many people to split the bill?\n"))
percentage = float(input("What tip percentage would you like to give? 10, 12 or 15?\n"))

total_divided = round((percentage / 100 + 1) * total / people, 2)

print("Each person should pay: ${:.2f}".format(total_divided))
