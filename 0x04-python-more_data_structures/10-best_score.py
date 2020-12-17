#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is None:
        return None
    bestKey = a_dictionary[0]
    for x in a_dictionary:
        if a_dictionary[x] > a_dictionary[bestKey]:
            bestKey = x
    return x
