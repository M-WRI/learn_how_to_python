# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_of_people = len(names) - 1
random_index = random.randint(0, number_of_people)
name = names[random_index]

print(f"{name} is going to buy the meal today!")
