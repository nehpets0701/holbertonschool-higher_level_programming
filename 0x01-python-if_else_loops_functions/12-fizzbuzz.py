#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 15 == 0 and x != 0:
            print("FizzBuzz ", end="")
        elif x % 3 == 0 and x != 0:
            print("Fizz ", end="")
        elif x % 5 == 0 and x != 0:
            if x != 100:
                print("Buzz ", end="")
            else:
                print("Buzz ", end="")
        else:
            print("{} ".format(x), end="")
