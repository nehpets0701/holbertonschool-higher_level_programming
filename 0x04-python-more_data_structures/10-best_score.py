#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    bestKey = list(a_dictionary.keys())[0]
    for x in a_dictionary:
        if a_dictionary[x] > a_dictionary[bestKey]:
            bestKey = x
    return bestKey
