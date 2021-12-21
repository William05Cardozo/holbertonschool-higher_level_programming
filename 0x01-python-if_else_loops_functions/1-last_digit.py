#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = number % 10

if number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, num))
elif number == 0:
    print("Last digit of {:d} is {:d} is zero".format(number, num))
elif number < 6 and number != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, num))
