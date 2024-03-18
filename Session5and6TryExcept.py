# Try/Except. Working around errors.
try:
    num = input("Give me a number: ")
    num = int(num)
    num2 = input("Give me another number: ")
    num2 = int(num2)
    result = num / num2
except ValueError:
    print("Please give me a proper number.")
except ZeroDivisionError:
    print("The second number cannot be zero.")
except:
    print("SOme other error i did not foresee.")
else:
    print("The result of the division is: ", result)
finally:
    print("Thank you for cooperating, have a nice day.")
