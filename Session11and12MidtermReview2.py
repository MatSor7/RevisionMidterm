file_name = 'ReviewFile'
fd = open(file_name, 'a')
while True:
    line = input('Enter a sentence, or press enter to quit: ')
    if line:
        fd.write(line + '\n')
    else:
        break
