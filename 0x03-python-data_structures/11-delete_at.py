#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    copy = my_list
    if idx < 0:
        return "None"
    elif idx >= len(my_list):
        return "None"
    del my_list[idx]
    return my_list
