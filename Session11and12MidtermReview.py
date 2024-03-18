# Write a function that forces the user to enter a multiple of 6. Use try except to catch invalid inputs.
def m6():
    """
    A function that returns a multiple of 6
    :return: the multiple of 6 entered by the user
    """
    while True:
        try:
            number = input('Give me a multiple of 6: ')
            number = int(number)
        except ValueError:
            print('That is not a number.')
            continue
        if number % 6 == 0:
            return number
# Definition of function goes all the way to return line.
        print('That number is not a multiple of 6. Try again')


print(f'A multiple of 6 is: {m6()}.')
