#!/usr/bin/python3
"""request id"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    r = urllib.request.Request(argv[1])
    with urllib.request.urlopen(r) as response:
        header = response.info()
        print(header['X-Request-Id'])
