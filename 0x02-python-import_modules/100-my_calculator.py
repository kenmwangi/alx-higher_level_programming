#!/usr/bin/python3

from sys import argv

from main import add, sub, mul, div

operators = ["+", "-", "*", "/"]
arg_len = len(argv)

if __name__ == "__main__":
    if (arg_len - 1) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a, b = int(argv[1]), int(argv[3])
        if argv[2] == '+':
            print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        elif argv[2] == "-":
            print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        elif argv[2] == "*":
            print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
        else:
            print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
