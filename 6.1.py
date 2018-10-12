#Your Python file will:

#Read and Display the list of names from the file
#Display the number of names that are read from the file (You will need a variable to keep a count of the number of items read from the file.)
name_file = open('names.txt', 'r')
counter = int(0)

# write a for loop to read in all of the lines, and print them on the screen, add 1 to counter for each line
line = name_file.readline()

while line != '':
    counter = counter + 1
    line = name_file.readline()
    print(line)
print(counter)
name_file.close()
