num_file = open('numbers.txt', 'r')
line = num_file.readline()
line = line.rstrip('\n')
total = 0
counter = 0
for line in num_file:
    amount = float(line)
    total = amount + total
    counter = counter + 1
average = total / counter
print("There is", counter, "numbers.")
print("The total is", total)
print("The average is", format(average, '.2f'))
