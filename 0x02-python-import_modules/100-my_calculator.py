#!/usr/bin/python3
import calculator_1
import sys

if len(argv) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

if sys.argv[2] == '+':
    print(calculator_1.add(sys.argv[1], sys.argv[3]))
elif sys.argv[2] == '-':
    print(calculator_1.sub(sys.argv[1], sys.argv[3]))
elif sys.argv[2] == '*':
    print(calculator_1.mul(sys.argv[1], sys.argv[3]))
elif sys.argv[2] == '/':
    print(calculator_1.div(sys.argv[1], sys.argv[3]))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1) 