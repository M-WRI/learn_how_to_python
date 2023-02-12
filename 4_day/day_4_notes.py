# Random numbers
import random
import some_file

random_number = random.randint(1, 100)

print(random_number)
print(some_file.number, "<--- importet number from other file")

random_float = random.random() # Random Float
print(random_float)

random_float_zero_five = random.uniform(0, 5) # Random Float in range
print(random_float_zero_five)

# Lists
some_list = ["some", "list"] # The array in JS/TS is called list in Python