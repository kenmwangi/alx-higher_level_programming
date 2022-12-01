#!/usr/bin/python3

from sys import argv

from task import add, sub, mul, div

operators = ["+", "-", "*", "/"]
arg_len = len(argv)

if __name__ = "__main__":
    if (arg_len - 1) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a, b = int(argv[1]), int(argv[3])
        if argv[2] == '+':
            print(f"{a:d} + {b:d} = {add(a, b):d}")
        elif argv[2] == "-":
            print(f"{a:d} - {b:d} = {sub(a, b):d}")
        elif argv[2] == "*":
            print(f"{a:d} * {b:d} = {mul(a, b):d}")
        else:
            print(f"{a:d} / {b:d} = {div(a, b):d}")
