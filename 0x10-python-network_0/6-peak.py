#!/usr/bin/python3

def find_peak(list_of_integers):
    for x in range(len(list_of_integers)):
        if x == len(list_of_integers) - 1:
            if list_of_integers[x] >= list_of_integers[x-1]:
                if list_of_integers[x] >= 0:
                    return list_of_integers[x]
        elif x == 0:
            if list_of_integers[x] >= list_of_integers[x+1]:
                if list_of_integers[x] >= 0:
                    return list_of_integers[x]
        elif list_of_integers[x] >= list_of_integers[x-1] and list_of_integers[x] >= list_of_integers[x+1]:
            if list_of_integers[x] >= 0:
                return list_of_integers[x]
