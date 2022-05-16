# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person shoul pay (150.00 / 5) * 1.12

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?\n")[1:])

tip = float("1."+input("What percentage tip would you like to give? 10, 12, or 15?\n"))

people = int(input("How many people to split the bill?\n"))

print("Each person should pay: ${:.2f}".format( (total_bill/people)*tip ) )

