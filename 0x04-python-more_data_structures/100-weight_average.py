#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for num in my_list:
        average += num[0] * num[1]
        div += tup[1]
    return float(average / div)
