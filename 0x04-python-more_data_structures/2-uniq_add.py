#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum = 0
    for number in my_set:
        sum += number
    return sum
