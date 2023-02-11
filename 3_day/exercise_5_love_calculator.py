# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
T = name1.lower().count("t") + name2.lower().count("t")
R = name1.lower().count("r") + name2.lower().count("r")
U = name1.lower().count("u") + name2.lower().count("u")
E = name1.lower().count("e") + name2.lower().count("e")

num_one = T + R + U + E

L = name1.lower().count("t") + name2.lower().count("l")
O = name1.lower().count("r") + name2.lower().count("o")
V = name1.lower().count("u") + name2.lower().count("v")
E = name1.lower().count("e") + name2.lower().count("e")

num_two = L + O + V + E

total_score = int(str(num_one) + str(num_two))

if total_score < 10 and total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
    
    