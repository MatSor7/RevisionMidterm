file_name = 'x-file.txt'
fd = open(file_name, 'a')
while True:
    line = input('Enter a line (or just press enter to quit): ')
    if line:
        fd.write(line + '\n')
    else:
        break

fd.close()

file_name = "x-file.txt"
fd = open(file_name)  # r is default
print("Here are the contents of the file:")
# print(fd.read())

# Another way is to read line by line
for line in fd:
    # print(line, end="")
    # print(line.strip())
    print(line.replace("\n", ""))
fd.close()
# This shows more experience with Python:
with open(file_name) as fd:
    print("Here are the 3-letter words of the file:")
    for line in fd:
        words = line.split()
        # Next will print every word of the file, but in lists containing each line
        # print(words)
        # Next is if you want 3-letter words.
        for word in words:
            if len(word) == 3:

                print(word)
