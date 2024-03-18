def find_divisors(num):
    """
    A function that returns a list of all the divisors of the parameter
    :param num: an integer
    :return: The divisors of the parameter
    """
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


print(find_divisors(20))
