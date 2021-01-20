#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename) as file:
        file.write(json.dumps(my_obj))
        file.close()
