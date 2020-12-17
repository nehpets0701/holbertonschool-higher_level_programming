#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for x in range(len(my_list)):
        if my_list[x] not in my_list[:x]:
            sum += my_list[x]
    return sum
