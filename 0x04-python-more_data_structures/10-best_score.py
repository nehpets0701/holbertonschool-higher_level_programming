#!/usr/bin/python3
def best_score(a_dictionary):
    check = 0

    if len(a_dictionary) == 0:
       return None

    for x in a_dictionary:
        if a_dictionary.get(x) > check:
            check = a_dictionary.get(x)
    return check
