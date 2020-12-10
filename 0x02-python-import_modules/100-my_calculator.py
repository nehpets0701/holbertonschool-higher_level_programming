#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    x = int(sys.argv[1])
    y = int(sys.argv[3])

    if sys.argv[2] == "+":
        print("{} + {} = {}".format(x, y, add(x, y)))
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(x, y, sub(x, y)))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(x, y, mul(x, y)))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(x, y, div(x, y)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
