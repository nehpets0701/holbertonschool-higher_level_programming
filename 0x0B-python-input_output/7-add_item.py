#!/usr/bin/python3
"""script"""
from sys import argv

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
try:
    new = load(file)
except:
    with open(file, 'w'):
        new = []
new += argv[1:]
save(new, file)
