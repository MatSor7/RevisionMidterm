def words_3(filename):
    """
    Find 3-letter words in the file
    :param filename: Name of the file
    :return: Nothing
    """
    punctuation = ",!?.\n"
    with open(filename, 'r') as file:
        for line in file:
            for p in punctuation:
                line = line.replace(p, "")
            words = line.split(" ")
            for word in words:
                if len(word) == 3:
                    print(word)
    return


words_3('ReviewFile')
