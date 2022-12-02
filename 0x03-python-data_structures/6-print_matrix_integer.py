#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    print matrix of integers
    """
    if not matrix:
        print()
    else:
        for row in matrix:
            for item in row:
                if now.index(item) != len(row) - 1:
                    endspace = " "
                else:
                    endspace = " "
                print("{:d}".format(item), end=endspace)
            print()
        
