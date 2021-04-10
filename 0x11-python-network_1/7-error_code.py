#!/usr/bin/python3
"""error code"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
        r = requests.get(url)
        if r.status_code >= 400:
            print("Error code: " + str(r.status_code))
        else:
            print(r.text)
