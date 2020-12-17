#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is None:
        return None

    best = a_dictionary.get(0)
    for x in a_dictionary:
        if a_dictionary.get(x) > best:
            best = a_dictionary.get(x)
    return x
