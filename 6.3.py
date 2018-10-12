num_file = open('numbers2.txt', 'r')
line = num_file.readline()
line = line.rstrip('\n')
total = 0
counter = 0
try:
    for line in num_file:
        amount = float(line)
        total = amount + total
        counter = counter + 1
    average = total / counter
    print("There is", counter, "numbers.")
    print("The total is", total)
    print("The average is", format(average, '.2f'))
except ValueError:
    print("There is an invalid string in the data entry")
