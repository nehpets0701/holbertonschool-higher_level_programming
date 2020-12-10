#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if len(argv) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

if sys.argv[2] == '+':
    print(add(sys.argv[1], sys.argv[3]))
elif sys.argv[2] == '-':
    print(sub(sys.argv[1], sys.argv[3]))
elif sys.argv[2] == '*':
    print(mul(sys.argv[1], sys.argv[3]))
elif sys.argv[2] == '/':
    print(div(sys.argv[1], sys.argv[3]))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
