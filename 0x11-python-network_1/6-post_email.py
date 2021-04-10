#!/usr/bin/python3
"""email"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 3:
        url = argv[1]
        email = argv[2]
        dicti = {'email': email}
        r = requests.post(url, dic)
        print(r.text)
