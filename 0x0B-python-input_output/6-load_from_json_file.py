#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename) as file:
        str = file.read()
        json.load(str)
        file.close()
