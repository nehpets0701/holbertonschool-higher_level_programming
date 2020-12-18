#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    weight = 0
    for x in my_list:
        sum += x[0] * x[1]
        weight += x[1]
    return sum / weight
