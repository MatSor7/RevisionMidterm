hi = "Hello dude"
print(dir(hi))
help(hi.isupper)
print(hi)
# Indexing
print(hi[2])
print(hi[-2])
bye = "Bye"
# Addition is overloaded, so is multiplication.
print(hi + " " + bye)
print(3*hi)
# Length.
print(len(hi))
# Strings are iterable.
for letter in hi:
    print(letter)
i = len(hi) - 1
while i >= 0:
    print(hi[i], end="")
    i -= 1
    break

print()
i = 0
while i < len(hi):  # While i is less than length of hi, continue loop:
    print(hi[len(hi)-i-1], end="")  # Print hi starting from length of hi-i-1, end with nothing.
    i += 1  # Add one to i, loop continues till i == len(hi).

print("")
# Slicing
print(hi[3:5])
print(hi[3::])
print(hi[::3])
print(hi[1::2])
print(hi[::-1])

print("This is a sentence and i want the words".split(" "))

text = "Bob goes to school. Bob likes to play tennis. I am friends with Bob."
print(text.find("Bob"))
print(text.rfind("Bob"))
i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1

# f-string
name = input("What is your name? ")
print(f"Hello, your name is {name}. 45x93 is {45*93}.")

sentence = "How are you today, my dear sir; You look one-of-a-kind!"
print(sentence)
punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)
