#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] == '+':
        print(add(int(sys.argv[1]), int(sys.argv[3])))
    elif sys.argv[2] == '-':
        print(sub(int(sys.argv[1]), int(sys.argv[3])))
    elif sys.argv[2] == '*':
        print(mul(int(sys.argv[1]), int(sys.argv[3])))
    elif sys.argv[2] == '/':
        print(div(int(sys.argv[1]), int(sys.argv[3])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
