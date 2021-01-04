#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for y in range(x):
        try:
            print("{:d}".format(y), end="")
        except:
            break
    print("")
    return y
