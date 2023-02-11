print("Welcome to the tip calculator")
total = input("What is the total bill? $")
percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to splitt the bill? ")

tip_per_person = (float(total) / int(people)) * (int(percent)/100 + 1)
final_amount = "{:.2f}".format(tip_per_person)

print(f"Each person should pay: ${final_amount}")