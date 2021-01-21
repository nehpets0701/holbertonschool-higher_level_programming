#!/usr/bin/python3
"""function"""
import json


def save_to_json_file(my_obj, filename):
    """function"""
    with open(filename) as file:
        file.write(json.dumps(my_obj))
        file.close()
