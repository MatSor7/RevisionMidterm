result = 0
for i in range(0,10):
    result += i
print("The sum of the first 9 numbers is:", result)

result = 0
text = "1234567890"
for i in range(0,10):
    result += int(i)
print("The sum of the first 9 numbers is:", result)

divisor = 3
for num in range(0, 12, 3):
    print(num/divisor)

for letter in "aloha":
    print(letter)

num = 0
while num <= 5:
    print(num)
    num += 2

print("Out")
print(num)

num = 0
count = 0
while num <= 19:
    if num % 3 == 0:
        count += 1
    num += 1

print("Numbers divisible by 3:", count)

import random

lives = 3
while lives > 0:
    print("You have", lives, "lives left.")
    dice = random.randint(1, 6)
    print("You rolled a", dice)
    if dice == 6:
        print("\n\nYOU WIN!\n\n")
        break
    else:
        lives -= 1
print("Thank you for playing. Goodbye.")
