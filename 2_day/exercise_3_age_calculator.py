# A calculator wich calculates how much time is left untill the age of 90

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num = 90 - int(age)
get_days = num * 365
get_weeks = num * 52
get_months = num * 12

print(f"You have {get_days} days, {get_weeks} weeks, and {get_months} months left.")
