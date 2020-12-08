#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "Last digit of "
s5 = " and is greater than 5"
s6 = " and is less than 6 and not 0"
if number > 0:
    if number % 10 == 0:
        print("Last digit of {:d} is 0 and is 0".format(number))
    elif number % 10 > 5:
        print(s + "{:d} is {:d}".format(number, number % 10) + s5)
    elif number % 10 < 6 and number % 10 != 0:
        print(s + "{:d} is {:d}".format(number, number % 10) + s6)
if number < 0:
    if number % -10 == 0:
        print("Last digit of {:d} is 0 and is 0".format(number))
    elif number % -10 > 5:
        print(s + "{:d} is {:d}".format(number, number % -10) + s5)
    elif number % -10 < 6 and number % -10 != 0:
        print(s + "{:d} is {:d}".format(number, number % -10) + s6)
