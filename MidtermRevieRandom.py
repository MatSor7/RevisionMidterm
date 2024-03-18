# Write a program that adds 10 random numbers and prints the answer.
import random

# generate n random integers between a and b
n = 10
a = 1
b = 100
rand_nums = [random.randint(a, b) for _ in range(n)]

# calculate the sum of the random integers
rand_sum = sum(rand_nums)

# print the results
print("Random integers:", rand_nums)
print("Sum of random integers:", rand_sum)
