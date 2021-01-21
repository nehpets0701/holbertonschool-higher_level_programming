#!/usr/bin/python3
"""function"""
import json


def save_to_json_file(my_obj, filename):
    """function"""
    with open(filename, 'w') as file:
        return file.write(json.dumps(my_obj))
        file.close()
