#!/usr/bin/python3
"""peak problem"""


def find_peak(list_of_integers):
    """wrapper function"""
    if list_of_integers == []:
        return None
    return(find(list_of_integers, 0, len(list_of_integers) - 1))

def find(numlist, low, high):
    """real function"""
    size = high - low
    mid = low + int(size/2)
    if low == high or ((numlist[mid - 1] < numlist[mid]) and
                       (numlist[mid + 1] < numlist[mid])):
        return numlist[mid]
    elif numlist[mid + 1] > numlist[mid]:
        return find(numlist, mid + 1, high)
    else:
        return find(numlist, low, mid - 1)
