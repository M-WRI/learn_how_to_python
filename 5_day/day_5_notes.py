# For Loop
list_one = ["item_1","item_2","item_3","item_4","item_5","item_6"]

for item in list_one:
    print(item)
    print(f"{item} this is a frase")

# For Loops with range function
total_count = 0
for number in range(1, 101):
    total_count += number

print(total_count, "<--- Total count")