import random

# Step 1
word_list = ["ardvark", "baboon", "camel"]

# random_index = random.randint(0, len(word_list) - 1) <-- My appriach
# random_word = word_list[random_index]

random_word = random.choice(word_list)
print(f"the random word is {random_word}...")

# random_word_chars = [*random_word] <-- for loop is automatically going through all the letters
# no need to create a list before. anyhow, nice to know how to create easy a list.

display = []
for _ in random_word:
  display += '_'

print(display)

end_of_game = False
while not end_of_game:
   guess = input("guess a letter: ").lower()
   for i in range(len(random_word)):
    if random_word[i] == guess:
        display[i] = guess
        
    print(display)
    if '_' not in display:
       end_of_game = True




    

