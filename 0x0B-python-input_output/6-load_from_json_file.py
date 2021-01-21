#!/usr/bin/python3
"""function"""
import json


def load_from_json_file(filename):
    """function"""
    with open(filename) as file:
        return json.loads(file.read())
        file.close()
