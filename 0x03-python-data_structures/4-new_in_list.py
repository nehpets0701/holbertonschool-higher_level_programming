#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new = []
        for i in range(0, len(my_list)):
            if i == idx:
                new.append(element)
            else:
                new.append(my_list[i])
    return new
