import random

# Step 1
guess = input("guess a letter: ").lower()
word_list = ["ardvark", "baboon", "camel"]
# random_index = random.randint(0, len(word_list) - 1) <-- My appriach
# random_word = word_list[random_index]

random_word = random.choice(word_list)
# random_word_chars = [*random_word] <-- for loop is automatically going through all the letters
# no need to create a list before. anyhow, nice to know how to create easy a list.

for letter in random_word:
   if letter == guess:
    print("right")
   else:
     print("wrong")



    

