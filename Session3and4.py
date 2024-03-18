# Operators/Assignments on variables.
a = 2
print(a+2.0)
a /= 2
print(a)
b = 3
print(a**b)
b -= a
print(b+2)
c = a > b
print(c and a)
print(a+b+c)
# Getting input.
name = input("What is your name? ")
age = input("How old are you? ")
print("Hello, ", name, "!", sep="")
age = int(age)  # Convert string to integer
birth_year = 2023 - age
print(name, ", you were born in ", birth_year, ".", sep="")

GOAT = input("Who is the G.O.A.T? ")
