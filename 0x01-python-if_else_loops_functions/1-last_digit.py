#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number = number % 10

if number > 5:
    print("is {:d} and is greater than 5".format(number))
elif number == 0:
    print("is {:d} is zero".format(number))
elif number < 6 and number != 0:
    print("is {:d} and is less than 6 and not 0".format(number))
